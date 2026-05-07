#!/usr/bin/env python3
"""Check text-sample length distributions for polytok YAML files.

The parser intentionally handles the simple repo-local sample format without
requiring PyYAML. It supports both current dsv2 files:

    - token: " -"
      meaning_label: "subtraction_operator"
      text_samples:
        - "..."

and older ds files with a nested meanings list:

    - token: " -"
      meanings:
        - meaning_label: "subtraction_negative_operator"
          text_samples:
            - "..."
"""

from __future__ import annotations

import argparse
import ast
import re
import statistics
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


DEFAULT_CHAR_BUCKETS = (100, 250, 750, 1500)
DEFAULT_WORD_BUCKETS = (20, 50, 140, 280)
BUCKET_NAMES = ("very_short", "short", "medium", "long", "extra")


@dataclass(frozen=True)
class Sample:
    label: str
    line: int
    text: str


def parse_quoted_scalar(raw: str, line_no: int) -> str:
    """Parse the quoted scalar after a YAML list marker.

    The dataset stores samples as one-line double-quoted strings with escaped
    newlines. Python's string literal parser handles that subset well.
    """
    raw = raw.strip()
    if not raw:
        raise ValueError(f"line {line_no}: empty text sample")
    try:
        value = ast.literal_eval(raw)
    except (SyntaxError, ValueError) as exc:
        raise ValueError(
            f"line {line_no}: sample is not a supported one-line quoted string"
        ) from exc
    if not isinstance(value, str):
        raise ValueError(f"line {line_no}: sample value is not a string")
    return value


def parse_samples(path: Path) -> list[Sample]:
    label: str | None = None
    in_text_samples = False
    samples: list[Sample] = []

    label_re = re.compile(r"^\s*-?\s*meaning_label:\s*(['\"])(.+?)\1\s*$")
    text_samples_re = re.compile(r"^\s*text_samples:\s*$")
    sample_re = re.compile(r"^\s*-\s+(.+)\s*$")
    structural_keys = (
        "token:",
        "meaning_label:",
        "meanings:",
        "text_samples:",
    )

    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        label_match = label_re.match(line)
        if label_match:
            label = label_match.group(2)
            in_text_samples = False
            continue

        if text_samples_re.match(line):
            if label is None:
                raise ValueError(f"line {line_no}: text_samples appears before meaning_label")
            in_text_samples = True
            continue

        if not in_text_samples:
            continue

        stripped = line.strip()
        if not stripped:
            continue

        if any(stripped.startswith(key) for key in structural_keys):
            in_text_samples = False
            continue

        match = sample_re.match(line)
        if not match:
            continue

        raw_value = match.group(1)
        if any(raw_value.startswith(key) for key in structural_keys):
            in_text_samples = False
            continue

        samples.append(Sample(label=label or "(unknown)", line=line_no, text=parse_quoted_scalar(raw_value, line_no)))

    if not samples:
        raise ValueError(f"{path}: no text samples found")
    return samples


def word_count(text: str) -> int:
    return len(re.findall(r"\S+", text))


def metric_value(text: str, metric: str) -> int:
    if metric == "chars":
        return len(text)
    if metric == "words":
        return word_count(text)
    raise ValueError(f"unsupported metric: {metric}")


def parse_buckets(raw: str | None, metric: str) -> tuple[int, int, int, int]:
    if raw is None:
        return DEFAULT_WORD_BUCKETS if metric == "words" else DEFAULT_CHAR_BUCKETS

    try:
        values = tuple(int(part.strip()) for part in raw.split(","))
    except ValueError as exc:
        raise SystemExit("--buckets must be four comma-separated integers") from exc

    if len(values) != 4:
        raise SystemExit("--buckets must contain exactly four thresholds")
    if any(value <= 0 for value in values) or tuple(sorted(values)) != values:
        raise SystemExit("--buckets thresholds must be positive and increasing")
    return values  # type: ignore[return-value]


def bucket_name(value: int, thresholds: tuple[int, int, int, int]) -> str:
    if value < thresholds[0]:
        return "very_short"
    if value < thresholds[1]:
        return "short"
    if value < thresholds[2]:
        return "medium"
    if value < thresholds[3]:
        return "long"
    return "extra"


def percentile(values: list[int], q: float) -> int:
    if not values:
        return 0
    ordered = sorted(values)
    if len(ordered) == 1:
        return ordered[0]
    pos = (len(ordered) - 1) * q
    lo = int(pos)
    hi = min(lo + 1, len(ordered) - 1)
    frac = pos - lo
    return round(ordered[lo] * (1 - frac) + ordered[hi] * frac)


def summarize(values: list[int]) -> dict[str, int | float]:
    return {
        "count": len(values),
        "min": min(values),
        "p25": percentile(values, 0.25),
        "median": round(statistics.median(values)),
        "p75": percentile(values, 0.75),
        "p90": percentile(values, 0.90),
        "max": max(values),
        "avg": round(statistics.fmean(values), 1),
    }


def format_bucket_ranges(thresholds: tuple[int, int, int, int]) -> str:
    return (
        f"very_short <{thresholds[0]}, "
        f"short {thresholds[0]}-{thresholds[1] - 1}, "
        f"medium {thresholds[1]}-{thresholds[2] - 1}, "
        f"long {thresholds[2]}-{thresholds[3] - 1}, "
        f"extra >={thresholds[3]}"
    )


def print_table(rows: Iterable[dict[str, object]]) -> None:
    rows = list(rows)
    headers = [
        "label",
        "count",
        "min",
        "p25",
        "median",
        "p75",
        "p90",
        "max",
        "avg",
        *BUCKET_NAMES,
    ]
    widths = {
        header: max(len(header), *(len(str(row.get(header, ""))) for row in rows))
        for header in headers
    }

    def fmt(row: dict[str, object]) -> str:
        return "  ".join(str(row.get(header, "")).rjust(widths[header]) for header in headers)

    print(fmt({header: header for header in headers}))
    print("  ".join("-" * widths[header] for header in headers))
    for row in rows:
        print(fmt(row))


def build_rows(
    samples: list[Sample],
    metric: str,
    thresholds: tuple[int, int, int, int],
) -> list[dict[str, object]]:
    by_label: dict[str, list[Sample]] = defaultdict(list)
    for sample in samples:
        by_label[sample.label].append(sample)

    rows: list[dict[str, object]] = []
    for label in sorted(by_label):
        values = [metric_value(sample.text, metric) for sample in by_label[label]]
        bucket_counts = Counter(bucket_name(value, thresholds) for value in values)
        row: dict[str, object] = {"label": label, **summarize(values)}
        row.update({name: bucket_counts.get(name, 0) for name in BUCKET_NAMES})
        rows.append(row)

    all_values = [metric_value(sample.text, metric) for sample in samples]
    all_buckets = Counter(bucket_name(value, thresholds) for value in all_values)
    total_row: dict[str, object] = {"label": "ALL", **summarize(all_values)}
    total_row.update({name: all_buckets.get(name, 0) for name in BUCKET_NAMES})
    rows.append(total_row)
    return rows


def print_longest_shortest(samples: list[Sample], metric: str, count: int) -> None:
    if count <= 0:
        return

    ranked = sorted(samples, key=lambda sample: metric_value(sample.text, metric))
    print(f"\nShortest {count}:")
    for sample in ranked[:count]:
        print(f"  {sample.label}:{sample.line}  {metric_value(sample.text, metric)}")
    print(f"\nLongest {count}:")
    for sample in reversed(ranked[-count:]):
        print(f"  {sample.label}:{sample.line}  {metric_value(sample.text, metric)}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Check length distribution by meaning_label for samples_*.yaml files."
    )
    parser.add_argument("path", type=Path, help="Path to a samples_*.yaml file")
    parser.add_argument(
        "--metric",
        choices=("chars", "words"),
        default="chars",
        help="Length metric to bucket and summarize. Default: chars",
    )
    parser.add_argument(
        "--buckets",
        help=(
            "Four comma-separated thresholds. Defaults: "
            f"chars={','.join(map(str, DEFAULT_CHAR_BUCKETS))}; "
            f"words={','.join(map(str, DEFAULT_WORD_BUCKETS))}"
        ),
    )
    parser.add_argument(
        "--extremes",
        type=int,
        default=0,
        metavar="N",
        help="Also print the N shortest and N longest samples with file line numbers.",
    )
    args = parser.parse_args(argv)

    if not args.path.exists():
        print(f"error: file not found: {args.path}", file=sys.stderr)
        return 2

    thresholds = parse_buckets(args.buckets, args.metric)
    try:
        samples = parse_samples(args.path)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"File: {args.path}")
    print(f"Metric: {args.metric}")
    print(f"Buckets: {format_bucket_ranges(thresholds)}")
    print(f"Samples: {len(samples)}\n")
    print_table(build_rows(samples, args.metric, thresholds))
    print_longest_shortest(samples, args.metric, args.extremes)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
