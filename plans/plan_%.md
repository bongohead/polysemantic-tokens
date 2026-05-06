# Plan: Polytok Token `" %"`

## Objective

Create `dsv2/samples_%.yaml` with 100 realistic samples for each meaning label:

- `percentage`
- `modulo`
- `latex_comment`

Every sample must contain the exact token `" %"` at least once: one ASCII space immediately followed by the ASCII percent sign. Every occurrence of `" %"` inside a sample must match that sample's `meaning_label`.

Use the current dsv2 flat YAML schema, matching files such as `dsv2/samples_-.yaml`: one top-level item per meaning label, with `token`, `meaning_label`, and `text_samples` fields. There is no old `ds/` source file for this token, so the plan is the source of truth for the label boundaries and distribution.

This token is high-risk because the same surface form appears in ordinary percentages, code operators, TeX comments, printf/template placeholders, URL encodings, SQL wildcards, and shell snippets. The leading space is part of the token. A sample with `95%` does not contain the target token, but `95 %`, `win_rate %`, `x % 7`, and `\alpha % old notation` do.

## Exact-Token Notes

- The target is literal ASCII space plus ASCII percent: `" %"`.
- A visible comment marker at the start of a line, `% comment`, does not contain the target. An indented LaTeX comment line such as `  % TODO` does contain the target because at least one ordinary ASCII space precedes `%`.
- A tab before `%` is not the target token. If indentation matters, ensure there is an actual ASCII space immediately before `%`.
- `100%` and `\%` do not contain the target token. They can still distract human review, so avoid them unless there is a strong corpus-realism reason.
- Every exact `" %"` counts, including occurrences inside strings, comments, code, tables, HTML text, OCR output, YAML values, and Markdown.
- Do not rely on the sample "mostly" being one sense. If one `" %"` is a percentage and another is modulo or a LaTeX comment marker, the sample is invalid.
- Percent signs without a leading space are not target occurrences, but they can make review harder. Prefer samples where all percent signs either share the active label or are absent.
- Avoid non-ASCII percent-like signs and fullwidth spacing tricks. Do not use fullwidth percent, thin-space percent conventions, or escaped Markdown as substitutes for the literal token.

## File And YAML Notes

- Name the dataset file `dsv2/samples_%.yaml` and quote the path in shell commands when needed.
- In YAML, the token field must be quoted exactly as `token: " %"`. Do not write an unquoted percent value.
- LaTeX samples need careful YAML quoting because backslashes inside double-quoted YAML strings can become escape sequences. Prefer single-quoted YAML strings or block scalars for LaTeX-heavy samples, or double every backslash if using double quotes.
- If using single-quoted YAML strings, double any literal apostrophe inside the sample. If using block scalars, still verify the exact target token appears and no leading indentation accidentally changes intended text.
- Run a YAML parser after creation and after large edits. The percent sign itself is safe in quoted strings, but LaTeX backslashes, tabs, and copied control characters are common failure points.

## Realism Standard

Samples should feel like a mixed C4/HPLT-style slice, not curated punctuation demonstrations. Use raw excerpts directly when plausible: spreadsheets, scraped tables, OCR forms, health stats, weather rows, business metrics, source code, tests, compiler output, notebooks, LaTeX manuscripts, `.sty` fragments, Beamer slides, README snippets, issue comments, forum posts, email chains, logs, and partial documents.

Good data can be clipped, mundane, redundant, noisy, or surrounded by adjacent page residue. Include plausible artifacts such as table headers, repeated footers, old navigation text, cookie boilerplate, OCR line breaks, copied spreadsheet formulas, broken Markdown tables, collapsed comments, generated reports, stale captions, and partial source files.

Avoid source-intro wrappers such as `spreadsheet excerpt:`, `code sample:`, `LaTeX source says`, `the page shows`, or `copied from`. The sample should be the artifact itself, not a description of the artifact. A natural in-artifact occurrence such as `discount %` in a table header, `bucket = hash % shard_count` in code, or `\end{proof} % sketch only` in TeX is fine only if the target token's meaning is still correct for the label.

## Distribution Guidance

Use approximate distributions, not exact quotas.

- Length: include a few very short fragments, many short and medium samples, and a meaningful minority of long messy samples.
- Token placement: do not start any sample with `" %"`. Avoid making most samples put the first target token in the first few characters. In longer samples, include some target occurrences late in the body.
- Semantic setup before first target: by the time the first exact `" %"` appears, the meaning should already be clear from preceding words, code comments, source syntax, headers, or local context. Prefer `percentage rate 44 %`, `// parity remainder\nrow % 2`, and `\section{Methods} % draft` over samples where the first percent sign arrives before the reader knows whether it is a unit, operator, or comment.
- Token density: percentages often use several ` %` values in tables and reports; modulo often repeats in code and tests; LaTeX comments can appear at line ends or on indented comment lines. Avoid artificial stuffing.
- Source mix: include technical, educational, workplace, commercial, informal, structured, crawled/OCR, auto-generated, and conversational styles where they fit each label.
- Voice and tone: vary between neutral machine output, terse notes, confused user text, polished documentation, academic source, generated reports, frustrated bug reports, and raw data dumps.
- Completeness: not every sample should be self-contained. Some can start or end abruptly as if scraped from the middle of a page.
- Cross-contamination: because percent signs are common in code and reports, choose formats that do not accidentally introduce another `" %"` sense.

## Label-Specific Realism And Balance

These are taste guides, not quotas:

- `percentage`: the spaced form is common in PDF/OCR text layers, translated or international pages, tables, copied slides, and machine-generated reports. Do not force unnatural English prose like every news sentence used `12 %`; put many examples in formats where the spacing is natural.
- `percentage`: many samples should be structured or semi-structured, but include enough prose around survey results, budget notes, medical/admin metrics, weather, grades, and forum comments that the label is not only spreadsheet rows. Avoid the repeated pattern `metric 1 %, metric 2 %, metric 3 %, then curator note about an export/page problem`.
- `modulo`: the spaced form is very natural in code because operators are often padded. Let this label be the most code-dominant, with tests, raw snippets, and source-native comments doing more work than after-the-fact explanation.
- `modulo`: simple parity checks are common but should not dominate. Each 20-sample batch should include at least several non-parity uses such as sharding, wrapping, recurrence, sampling, or normalization.
- `modulo`: include a minority of non-code habitats: number theory prose, clock arithmetic worksheets, modular exponentiation explanations, remainder tables, parser fixtures, textbook exercises, and StackOverflow/forum answers where the explanation itself is the artifact.
- `latex_comment`: the spaced form is natural as a trailing TeX comment after source or an indented comment-only line. Avoid making it mostly prose that explains LaTeX; the corpus slice should look like source files and template fragments. Avoid making nearly every sample a compact 5-12 line snippet with one comment; include some full preambles, whole environments, larger figure/table blocks, and diff hunks.
- `latex_comment`: TeX often uses `%` with no leading space to gobble line endings. Those are realistic but do not contain the target token; do not let them substitute for actual `" %"` occurrences.

## Diversity Dimensions To Track

Track these dimensions during each 20-sample round so the dataset does not collapse into a few easy templates:

- Source format: prose, spreadsheet rows, CSV/TSV exports, Markdown tables, HTML tables, OCR/PDF text, monitoring dashboards, code files, unit tests, notebook cells, compiler logs, LaTeX source, Beamer slides, package/class files, email fragments, chat/forum posts, product/admin pages, and generated reports.
- Surface form: `95 %`, `+4.2 %`, `rate %`, `pct %`, `n % 2`, `hash % buckets`, `i % len`, `  % comment`, `\item text % comment`, and `\end{...} % trailing note`.
- First-token position: early table cell after headers, mid-sentence, formula body, later code line, later LaTeX source line, late footer/repeated metric, and long sample with repeated target occurrences.
- Cleanliness: clean educational text, raw copied rows, partial excerpts, OCR noise, page residue, ad/footer contamination, broken formatting, generated boilerplate, and rough human notes.
- Voice/register: neutral machine output, terse analyst notes, confused student or user, bureaucratic report, polished docs, casual forum reply, excited community post, dry academic source, and test/log output.
- Domain spread: education, finance, retail, health, sports, elections, weather, science, software, systems, algorithms, contests, publishing, arXiv-style research, municipal docs, employment/admin, ecommerce, and hobbies.
- Completeness and length: clipped fragments, short rows, medium artifacts, and long messy sequences with target use not confined to the opening.

## `percentage`

Semantic rule: `" %"` denotes a percentage, percentage unit, percent column, percent change, percent rate, percent likelihood, or percent-complete value. The target percent sign must mean "per hundred" or mark a field whose values are percentages.

Good examples:

- `success rate 97 % after excluding retries`
- `discount % | margin % | tax %`
- `battery went from 43 % to 18 % during the call`
- `YoY change +6.4 %`
- `The survey reports 12 % undecided`

Include:

- Tables and reports with values such as `0 %`, `5 %`, `12.5 %`, `100 %`, negative percentages, plus-signed changes, and confidence/probability percentages.
- Spreadsheet exports, CSV/TSV rows, dashboards, analytics reports, financial summaries, election returns, sports stats, weather/humidity pages, gradebooks, lab results, health/admin data, product ratings, app telemetry, and generated PDFs.
- Natural language where the spaced percent style is plausible: OCR/PDF text layers, European or translated pages, school worksheets, research prose, scraped government pages, old CMS tables, and copied slide text.
- Column headers and labels such as `growth %`, `fee %`, `APR %`, `completion %`, and `humidity %` where the percent sign labels percentage units.
- Messy data with repeated headers, footers, ad residue, clipped charts, mobile table exports, stale notes, and copied workbook formulas.

Exclude:

- Modulo operators: `i % 2`, `hash % buckets`, `value % MOD`.
- LaTeX comment delimiters: `\section{Intro} % old title`.
- Escaped percent literals in LaTeX: `50 \%` does not contain the target and should not be used as the target.
- Percent-format placeholders and template syntax: `printf(" %d")`, `strftime(" %Y")`, `LIKE ' %abc'`, `%(name)s`, `%{var}`, `%USERPROFILE%`.
- URL encodings, encodings, or path fragments: `%20`, `%2F`, `LIKE '%foo%'`; these usually do not contain the exact target, but avoid them.
- CSS or layout code where `%` is a size unit, such as `width: 80 %`. It is technically a percentage, but the spaced form is often invalid or typo-like in real CSS. Use report/table percentage sources instead.
- A literal percent sign used as an unknown marker, wildcard, shell prompt, or arbitrary symbol.

Guidance:

- This label should lean heavily toward real-world reports and tables because the spaced style `45 %` is especially common in copied PDF/OCR, government stats, translated pages, and spreadsheet exports.
- Do not over-explain percentages in a tutor voice. Raw rows, broken tables, screenshots converted to text, chart captions, and ordinary reports are often better.
- Avoid curator labels at the start, especially `clinic waiting room survey:`, `job log chunk:`, `locked sheet header...`, or `page source says...`. If the artifact needs a header, make it part of the artifact itself, such as CSV headers, email headers, table labels, or visible UI text.
- If a percentage column header is itself a target occurrence, establish it as a percentage before or at the header. `Annual percentage rate,APR %` is clearer than a bare `APR %` row that could feel like a format placeholder.
- Do not let the section collapse into dashboard rows followed by comments about a broken export, stale footer, mobile crawl, or PDF text layer. Some messy extraction artifacts are good; a repeated curator-auditor arc is bad.
- Include some prose, but avoid making the label mostly "X percent of people..." sentences.
- Use `rate %` and similar headers in moderation; too many header-only samples will become repetitive.
- In longer samples, put some ` %` values after body text, repeated table headers, chart footers, or copied notes so the target is not always near the start.
- If a sample includes code or config, make sure any `" %"` still denotes percentage, not modulo or formatting. Prefer labels like `threshold_percent_display: "87 %"` only when the colon itself is not the target of this dataset and the percent is unambiguously a percentage.

## `modulo`

Semantic rule: `" %"` is the modulo or remainder operator. It takes a left operand and a right operand and returns or tests the remainder. The target percent sign should be part of executable code, pseudocode, math-like code, tests, formulas, or algorithmic text where the operation is unambiguous.

Good examples:

- `if (i % 2 == 0) even.push(i);`
- `bucket = hash % shard_count`
- `return ((x % m) + m) % m`
- `WHERE user_id % 10 = 3`
- `assert rotate(17 % 5) == 2`

Include:

- Raw code in Python, JavaScript, TypeScript, C/C++, Java, Rust, Go, PHP, Ruby, SQL dialects, shell arithmetic, notebook cells, and pseudocode.
- Unit tests, property tests, parser fixtures, contest problems, algorithm notes, hash-bucketing code, ring buffers, cyclic indexing, parity checks, clock arithmetic, calendar recurrence, sharding, sampling, pagination, and graphics/game loops.
- Compiler/build/test output when the source line shows ` %` as modulo and the surrounding diagnostics do not introduce another target meaning.
- Educational programming exercises, code review comments, issue fragments, Stack Overflow-like replies, README examples, CI logs, generated docs, and messy notebook exports.
- Multiple modulo operations in one sample when natural: normalization, nested modulo, negative remainder handling, or repeated test cases.

Exclude:

- Percentages: `ratio 30 %`, `progress %`, `discount %`, `100 % complete`.
- LaTeX comments: `\draw (0,0) % note`.
- Format strings and printf/strftime placeholders: `" %d"`, `" %02d"`, `" %Y-%m-%d"`, `format(" %s", name)`.
- SQL `LIKE` wildcard patterns or shell globs where `%` is not remainder.
- Python old-style string formatting: `"value %s" % name` contains at least one formatting use; avoid it even if another `%` is modulo.
- Jinja, Make, batch, environment, URL, or templating percent syntax: `%{var}`, `%(name)s`, `%PATH%`, `%20`, `{% if %}`.
- Natural-language uses such as "modulo % operator" unless the target percent sign is the operator in an expression.
- Mathematical congruence notation using `mod` without `%`; it does not contain the target.

Guidance:

- This label should be code-heavy and can be comparatively dense with target tokens.
- Avoid polished tutorial paragraphs that explain modulo in the same voice repeatedly. Prefer raw code, tests, bug reports, contest fragments, snippets with missing imports, and copied CI output.
- Also avoid the opposite monotony: `code block -> one-line outside narrator comment` repeated across most samples. If explanation is needed, make it source-native (`// parity remainder`, SQL comments, test names) or make the whole sample a direct forum/tutorial/worksheet answer.
- For pure-code samples, add semantic setup before the first target operator when needed: comments like `// clock fields are remainders`, `# parity remainder`, `-- seconds_part is the remainder`, or surrounding function/test names. This satisfies the clarity-before-token rule without turning code into prose.
- Include at least several samples where modulo lives outside ordinary code: remainder worksheets, modular arithmetic prose, number theory notes, clock arithmetic, cryptography/checksum explanations, parser fixtures, and textbook-style questions.
- Balance simple parity examples with richer uses: hash buckets, wraparound indexing, circular buffers, randomized splits, calendar recurrence, graphics tiling, DSP/sample windows, protocol sequence numbers, and database partitioning.
- Be careful with code comments. A comment like `// 50 % rollout` would introduce a percentage target inside a modulo sample and invalidate it.
- Be careful with `%` inside strings. A string literal `"n % 2"` may be an instructional expression rather than executable code, but it can still be modulo if the context is parser/tests. A string literal `" %d"` is formatting, not modulo.
- Long samples should include target operators beyond the first lines, not just one `i % 2` near the top followed by unrelated code.

## `latex_comment`

Semantic rule: `" %"` marks a TeX/LaTeX comment delimiter. The percent sign begins a comment, causes TeX to ignore the rest of the line, or intentionally suppresses end-of-line whitespace as a comment marker. The exact token usually appears as an end-of-line comment after code, an indented comment line, or a trailing note after a macro/environment.

Good examples:

- `\title{Draft} % replace before submission`
- `\begin{align} % keep equation numbers`
- `\begin{proof} ...  % TODO: tighten proof`
- `\end{frame} % backup slide`
- `\usepackage{microtype} % loaded after fonts`

Include:

- Raw `.tex`, `.sty`, `.cls`, BibLaTeX-adjacent, Beamer, TikZ, PGFPlots, theorem/proof, table, equation, macro, package option, preamble, arXiv source, Overleaf conflict, and conference template fragments.
- End-of-line comments after LaTeX commands, environment boundaries, equations, table rows, TikZ paths, package declarations, bibliography settings, and custom macros.
- Indented comment-only lines, especially inside source blocks, as long as the sample does not begin with the target token.
- Messy source artifacts: merge conflict surroundings without off-label percent uses, copied Overleaf logs, old template comments, duplicated class-file notes, line wrapping, bad indentation, generated `.aux`-adjacent snippets if the percent sign is truly a comment marker.
- Human source comments with TODOs, reviewer notes, disabled lines, template warnings, style reminders, and partial drafts.

Exclude:

- Percentages in text or table values: `response rate 84 %`, `50 % of cases`.
- Escaped percent symbols printed in LaTeX output: `50 \%` does not contain the exact target and is not a comment delimiter.
- Modulo operators in code or pseudocode.
- BibTeX field values, URLs, DOI encodings, `arXiv:`, or package paths containing percent encodings.
- Comment text that itself contains a spaced percent value, such as `% success 70 %`, because that second `" %"` is a percentage inside the comment text.
- Percent-format placeholders or TeX macro names from unrelated languages pasted into a LaTeX sample.
- Plain Markdown or shell comments using `%` as an arbitrary marker unless the context is clearly TeX/LaTeX.

Guidance:

- This label should be source-like, not prose about LaTeX comments. Let the sample look like raw TeX.
- Use a mix of comment-only lines and trailing comments after real LaTeX code, but avoid making most samples a list of consecutive commented lines. Real files often have long stretches of source with a single trailing comment.
- Include occasional longer source artifacts: full preambles, complete Beamer documents, whole table/figure environments, listing configurations, letters, recipe/booklet environments, grant or journal templates, and diff hunks. These counterbalance the natural sameyness of short `\command % comment` snippets.
- Some line-start `%` comments are realistic but do not contain the exact target unless indented. Make sure every sample also has at least one exact `" %"`.
- Avoid placing ` %` at the very beginning of a sample. Start with a command, text line, environment, conflict marker, or previous source line before any indented comment.
- Keep comments varied: TODOs, disabled alternatives, template instructions, reminders about spacing, author notes, package warnings, figure/table notes, and proof-draft comments.
- In long samples, distribute comments across the source rather than only placing one trailing comment at the first line.
- Do not accidentally include percentage data in tables. If a LaTeX table needs percent values, use words, counts, or escaped `\%` without target occurrences, or choose another table.

## Cross-Meaning Hazards

Inspect these cases manually during dataset creation:

- `progress 75 %` is percentage; `i % 75` is modulo; `\item progress % old phrasing` is LaTeX comment.
- `rate %` is a percentage column header, not modulo.
- `a % b % c` is modulo if all operands are code/formula values.
- `x %= m` is modulo assignment when the language gives `%=` remainder-assignment semantics and the operands are numeric or index-like.
- R `x %% m` can be modulo because the target `" %"` is the first half of the `%%` remainder operator, but use it sparingly and make the R context clear. Do not confuse it with R `%in%`, `%/%`, `%>%`, or custom infix operators.
- `50 \%` is not the target token; `50 %` is a percentage outside LaTeX comments.
- `\newcommand{\pct}{\%} % printed percent` has one non-target escaped percent and one target LaTeX comment delimiter; it can be valid for `latex_comment` if no spaced percentage appears in the comment text.
- `printf(" %d", n)` and `strftime(" %Y")` contain target-like formatting placeholders, not any of the three desired labels.
- `printf("%%")`, `format!("{} %", x)`, and escaped literal percent signs are formatting or literal-output machinery, not modulo or percentage unless the surrounding value is truly a displayed percentage.
- `"value %s" % name` mixes string-format placeholder and formatting operator; avoid it for modulo.
- `LIKE ' %admin'`, `ILIKE '%foo%'`, and SQL wildcard fragments are not modulo.
- `url %20 encoded`, `%2F`, or copied query strings are URL encoding or text residue, not percentage/modulo/comment.
- `{% if user %}` and `{% endif %}` are template delimiters, not LaTeX comments or modulo.
- `%USERPROFILE%`, `%PATH%`, Windows batch variables, and Make automatic variables are not target labels.
- MATLAB, Octave, PostScript, Stata, and similar `%` comment syntaxes are comments, but not `latex_comment`. Avoid them for this dataset unless the artifact is unambiguously TeX/LaTeX.
- TeX ` %%` comment banners are LaTeX comments when they occur in TeX source, but they are visually noisy because the target is only the first percent in `%%`. Use sparingly and prefer ordinary trailing or indented comments.
- CSS `width: 80 %` is a percentage unit, but it is usually less realistic than report/table percentage text and can sit awkwardly near code. Do not use it as a planned source family.
- Shell prompts or REPL prompts using `%` are arbitrary prompt symbols, not target labels.
- In LaTeX samples, every exact `" %"` must be a comment delimiter. Do not include comment prose that says `20 % slower` or a table cell with `80 %`.
- In modulo samples, avoid comments or logs that say `95 % passing`, `CPU 12 %`, or `rollout %`.
- In percentage samples, avoid code rows like `if (n % 2)` even if the surrounding report is about percent metrics.

## Dataset Creation Strategy

Build `dsv2/samples_%.yaml` in rounds of about 20 samples per label, then review and revise before adding the next round.

For each `percentage` round, deliberately cover several of:

- OCR/PDF reports, spreadsheet exports, CSV/TSV tables, KPI dashboards, election/sports/weather stats, finance/retail metrics, gradebooks, lab/health results, product ratings, survey summaries, slide text, scraped HTML tables, generated emails, and informal comments.
- Surface forms such as `0 %`, `3.5 %`, `+12 %`, `-8 %`, `100 %`, `rate %`, `margin %`, `completion %`, and `humidity %`.
- Short fragments, medium report/table extracts, and long messy pages where values appear late as well as early.

For each `modulo` round, deliberately cover several of:

- Parity checks, cyclic indexing, ring buffers, array wrapping, hash buckets, database sharding, randomized train/test splits, date/calendar recurrence, graphics tiling, game loops, DSP/sample windows, contest problems, SQL partitions, parser tests, and negative modulo normalization.
- Languages and artifacts such as Python, JS/TS, C/C++, Java, Rust, Go, PHP, Ruby, SQL, shell arithmetic, notebooks, unit tests, CI logs, README snippets, issue comments, and raw code review fragments.
- Surface forms such as `i % 2`, `idx % len`, `hash % buckets`, `((x % m) + m) % m`, `$((n % 10))`, `user_id % 100`, `frame % period`, `x %= period`, and occasional R `x %% period`.

For each `latex_comment` round, deliberately cover several of:

- Preambles, article bodies, theorem/proof fragments, align environments, tables without percent data, figures, TikZ/PGFPlots, Beamer frames, `.sty`/`.cls` snippets, conference templates, arXiv source, Overleaf notes, disabled source lines, merge-conflict-adjacent text, and raw copied source with indentation issues.
- Surface forms such as `\command{...} % comment`, `\begin{env} % note`, `\end{env} % note`, `  % TODO`, table rows with trailing comments, and macro definitions with trailing comments.
- Comments that are operationally plausible: template reminders, package warnings, author TODOs, spacing notes, disabled alternatives, reviewer notes, figure/table labels, and proof-draft markers.

After each round:

- Search for every exact `" %"` and classify it manually.
- For `percentage`, search for code-like patterns around the target: letters/operators on both sides, `if`, `return`, `% 2`, `% n`, `hash %`, `idx %`, `printf`, `strftime`, `LIKE`, `{%`, `%}`. Reject off-label uses.
- For `modulo`, search for percent values and report labels: ` % complete`, `rate %`, `margin %`, `100 %`, `CPU`, `battery`, `discount`, `confidence`, `humidity`, `rollout`, `passed`. Reject percentage targets and template/formatting targets.
- For `modulo`, also search for composite percent syntax: `%=`, `%%`, `%in%`, `%/%`, `%>%`, `{%`, and `%}`. Keep `%=` only for remainder assignment, keep R `%%` only for clear modulo, and reject the other infix/template forms.
- For `latex_comment`, search for percentage values inside comments and tables: `\d+ %`, `rate %`, `confidence %`, `100 %`, plus formatting/template markers. Confirm each target percent begins a TeX comment.
- Check that no sample starts with `" %"` and that first-token positions vary.
- Check that long samples contain some late target tokens, not only an early header, first formula, or first source line.
- Rebalance if a label becomes too tidy, too explanatory, too spreadsheet-heavy, too parity-example-heavy, too TypeScript/Python-heavy, or too Overleaf-template-heavy.
- Validate YAML structure before continuing.

## Mechanical QA Helpers

Use these as aids, not replacements for reading every sample:

- Parse the YAML and confirm exactly three top-level label groups, 100 samples per label, and `token == " %"` for every group.
- Count exact `" %"` occurrences per sample. Flag samples with only one very early occurrence and long tail text; those often need late-token reinforcement or shortening.
- For `percentage`, flag target occurrences followed by identifier-like operands or digits that look like code divisors, such as ` % 2`, ` % n`, ` % len`, ` % bucket`, ` % period`, ` %=`, or ` %%`.
- For `modulo`, flag target occurrences followed by nothing, punctuation, words like `complete`, or report-unit terms. Also flag nearby `printf`, `strftime`, `LIKE`, `format`, `template`, `rollout`, `CPU`, `battery`, and `confidence`.
- For `latex_comment`, flag target occurrences that are not preceded by plausible TeX source on the same line or indentation at line start. Also flag any later ` %` inside the comment text that reads as a percentage value.
- Scan for `https`, `http`, `%20`, `%2F`, `{%`, `%}`, `%USER`, `%PATH`, `%in%`, `%/%`, `%>%`, `LIKE`, `strftime`, `printf`, and `format(` across the whole file.
- Run a length distribution check after each 100-sample label is complete, then manually inspect clusters of near-identical openings.
- Mechanical flags are review prompts, not automatic failures. For example, `x %% m` may be valid R modulo, and `threshold_display = "87 %"` may be valid percentage display text if the sample is otherwise clean.

## QA Checklist

Per sample:

- Contains at least one exact ASCII `" %"`.
- Every exact `" %"` has the target meaning for the active label.
- By the first exact `" %"`, the local context already makes the active meaning clear. Do not make the reader wait until after the target token to learn whether it was a percentage unit, remainder operator, or TeX comment.
- Does not start with `" %"`, and usually avoids placing the first target token in the first one or two tokens.
- Avoids curator-style source introductions unless the introduction is naturally part of the artifact and its target token has the active meaning.
- Is plausible as web/SFT corpus text, with realistic messiness and no theatrical over-explanation.
- Avoids off-label percent uses such as percentages in modulo/comment samples, modulo in percentage/comment samples, TeX comments in percentage/modulo samples, format placeholders, SQL wildcards, URL encodings, template delimiters, batch variables, and arbitrary prompt symbols.
- Is valid YAML when inserted into `dsv2/samples_%.yaml`.

Per meaning:

- Exactly 100 samples.
- Lengths, source types, voices, formats, emotional registers, and token counts are visibly varied.
- No dominant opening pattern, topic cluster, or narrative template.
- Includes rough/partial/crawled material without simply labeling the source type.
- Has target tokens distributed across early, middle, and late positions, especially in longer samples.
- Includes short fragments, medium artifacts, and some long messy samples.
- Manually inspect high-risk mixed-context cases where percentage, modulo, LaTeX comments, format placeholders, and template syntax can appear near each other.

## Always-Check Alignment Before Sampling

Use this plan as a live audit sheet after every 20-sample batch:

1. Semantic purity: classify every exact `" %"` in the batch, not just the first one.
2. Realistic messiness: include raw rows, broken pages, comments, code, source files, logs, OCR, generated reports, and clipped fragments where they naturally fit the label.
3. Voice variety: include neutral machine output, terse humans, confused users/students, bureaucratic text, casual comments, and dry technical source. Avoid a single calm explainer voice.
4. Token placement: no sample starts with `" %"`. Long samples need some late target tokens.
5. No curator wrappers: avoid `snippet:`, `example:`, `LaTeX source:`, and similar unless they are truly part of the artifact and do not add off-label target tokens.
6. Length variety: include short scraps, medium excerpts, and long messy sequences for every label.
7. Template avoidance: watch for too many `metric % | value %` tables, `i % 2` parity snippets, or `\command{} % TODO` trailing-comment lines.
8. Abruptness: include some samples that start or end mid-artifact.
9. Non-natural-language: percentage needs tables/reports, modulo needs raw code/tests/logs, and `latex_comment` needs TeX source rather than prose.
10. Tone: keep most text flat and mundane, but include occasional frustration, confusion, excitement, or stale autogenerated weirdness.
11. Domain balance: prevent over-concentration in analytics dashboards, parity code, or Overleaf templates.
12. False-friend review: scan placeholders, formatting, templates, SQL wildcards, URL encodings, shell prompts, R custom operators, and non-LaTeX comment syntaxes.
13. First-token semantic setup: spot-check the first `" %"` in every sample. The preceding context should already signal the intended label.
14. Final semantic reread: if any target occurrence feels like "maybe", rewrite or discard the sample.

## Plan Self-Review Notes

Initial harsh checks before dataset creation:

1. Correctness hinges on the exact leading space. The plan explicitly distinguishes `95%`, `95 %`, `\%`, line-start `%`, indented `  %`, and trailing LaTeX comments.
2. The three labels are separated by function, not by surrounding domain. Code can contain percentage strings, reports can contain code snippets, and LaTeX can contain percent data, so future samples must classify every exact `" %"`.
3. `percentage` has enough non-prose sources: reports, OCR, tables, dashboards, gradebooks, health/lab data, elections, sports, weather, finance, retail, and generated PDFs.
4. `modulo` is not allowed to become only `i % 2`; the plan forces hash buckets, circular indexing, sharding, recurrence, graphics, DSP, tests, SQL, shell arithmetic, and negative-normalization examples.
5. `latex_comment` is source-first and forbids percent values inside comment text, which is a subtle but important contamination risk.
6. The plan calls out template delimiters, formatting placeholders, SQL wildcards, URL encodings, batch variables, and shell prompts because those are likely false friends for this token.
7. Distribution guidance includes late target use, abrupt scraps, long messy samples, voice variation, and non-natural-language artifacts, matching `always_check.md`.

Review pass 1 refinements:

1. Removed a vague `modulo % branch` prose example because it could train a non-operator use of `%` under `modulo`. Replaced it with an actual modulo expression.
2. Tightened CSS percentage guidance. `width: 80 %` is a percentage, but it is awkward enough in real CSS that report/table sources should carry the label instead.
3. Removed generic Makefile snippets from the modulo include list. Make `%` is often a pattern wildcard or automatic-variable context, not remainder arithmetic.

Review pass 2 refinements:

1. Added file and YAML notes because this token starts with a space and includes `%`, which makes exact quoting non-negotiable.
2. Added LaTeX-specific YAML guidance. Backslashes in double-quoted YAML can silently become escapes or hard parser errors, so future LaTeX samples should use single quotes, block scalars, or doubled backslashes.

Review pass 3 refinements:

1. Added label-specific realism guidance so future samples place `percentage` in contexts where spaced percent is natural, instead of forcing awkward ordinary prose.
2. Made the expected distribution asymmetry explicit: `modulo` should be code-dominant, while `percentage` should be table/report-heavy and `latex_comment` should be TeX-source-heavy.
3. Called out TeX no-space `%` comments as realistic but non-target, preventing them from accidentally replacing exact `" %"` examples.

Review pass 4 refinements:

1. Added composite operator handling for `%=` and R `%%`, both of which can legitimately encode modulo while still containing the exact target substring.
2. Added explicit exclusions for R `%in%`, `%/%`, `%>%`, template delimiters, formatting escapes, and non-LaTeX comment syntaxes that would otherwise look deceptively close.
3. Added review searches for `%=` and `%%` so future modulo samples distinguish remainder operators from formatting, pipe, membership, integer division, and TeX banner comments.

Review pass 5 refinements:

1. Added mechanical QA helpers for parsing, counting exact token occurrences, scanning false friends, and checking length/opening distribution.
2. Made the mechanical checks explicitly subordinate to manual semantic review, since `x %% m` and displayed percentage strings can be valid depending on context.

Review pass 6 refinements:

1. Added an explicit `always_check.md` alignment section to connect the token-specific plan to the standing dataset-quality rubric.
2. Named the three biggest future template risks: repeated percent-metric tables, parity-only modulo snippets, and generic TeX trailing TODO comments.

Review pass 7 refinements:

1. Rewrote the standalone indented LaTeX comment good example so it no longer models a sample that starts with the exact target token.

Review pass 8 refinements:

1. Clarified line-start comments and indentation: `% comment` has no target token, `  % comment` does, and a tab before `%` does not count as `" %"`.

Review pass 9 refinements:

1. Removed the remaining soft allowance for CSS/layout percentage samples. The label has enough natural report/table sources without relying on typo-like CSS.

Review pass 10 refinements after full dataset iteration:

1. Added the "semantic setup before first target" rule. The final dataset needed several modulo code snippets adjusted so a source-native comment or prose phrase established `remainder`, `wrap`, `parity`, `clock`, or `checksum` before the first `" %"`.
2. Tightened `percentage` guidance around curator labels. Samples like `clinic waiting room survey:` or `job log chunk:` were replaced with actual artifact text, explicit rate labels, or CSV-like rows.
3. Added a warning against the percentage template that dominated early drafts: several metrics with ` %`, followed by a calm note about a stale footer, PDF text layer, mobile crawl, or export problem.

Review pass 11 refinements after modulo rewrites:

1. Added a specific warning against `code block -> one-line outside narrator comment`. This was the main late-stage modulo failure mode even after domain/language diversity improved.
2. Added guidance to prefer pure code, code comments, test names, direct forum/prose answers, and worksheet text over stapled-on explanations.
3. Added non-code modulo habitats explicitly: modular arithmetic prose, clock arithmetic, cryptography/checksum explanations, remainder tables, parser fixtures, and textbook exercises.

Review pass 12 refinements after LaTeX rewrites:

1. Rebalanced LaTeX guidance away from "many samples can have several comment delimiters." The finished dataset worked better when most samples had sparse comments, with only a few multi-comment cases.
2. Added a requirement for occasional longer LaTeX artifacts: full preambles, complete environments, Beamer documents, listing configs, letters, recipe/booklet fragments, grant templates, and diff hunks.
3. Kept the source-first rule: the section should look like TeX files, not prose describing TeX comments.
