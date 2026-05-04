# Plan: Polytok Token `" -"`

## Objective

Maintain `dsv2/samples_-.yaml` with 100 realistic samples for each meaning label:

- `subtraction_operator`
- `list_item_denoter`
- `text_separator_informal`

Every sample must contain the exact token `" -"` at least once. Every occurrence of `" -"` inside a sample must match that sample's `meaning_label`.

## Realism Standard

Samples should feel like a mixed C4/HPLT-style slice, not like polished prompt examples. Use raw excerpts directly when possible: code, SQL, proof fragments, tables, docs, comments, forums, chats, OCR, pasted emails, web pages, product text, class material, logs, captions, and partial notes.

Good data can be clipped, mundane, oddly formatted, redundant, or surrounded by irrelevant web residue. Keep artifacts plausible and adjacent to the text: HTML tags, cookie text, repeated footers, table cells, OCR errors, sidebars, stale headers, broken captions, collapsed comments, and copied navigation.

Avoid unnecessary context intros. Do not repeatedly start samples with phrases like `source:`, `snippet:`, `copied from`, `A user said`, `The page says`, `Dashboard note`, or `Teacher note`. A few natural labels are fine when they are part of the artifact, but most samples should begin with the actual text, formula, line, list, comment, or table row.

## Distribution Guidance

Use approximate distributions, not exact quotas.

- Length: include a few very short fragments, many short and medium samples, and a meaningful minority of long or extra-long messy samples.
- Token density: use enough instances to make the meaning clear. Longer samples should often contain the token later in the text, not only in the first sentence.
- Source mix: include everyday web text, technical/workplace text, educational material, rough scraped/OCR material, structured data, and informal social/comment text.
- Voice and tone: vary between neutral machine-like output, terse notes, confused human messages, polished docs, research prose, ads, support text, and raw logs.
- Completeness: not every sample should be self-contained. Some can start or end abruptly as if scraped from the middle of a page.
- Openings: avoid starting any sample with the token. Prefer several tokens of context before the first `" -"`, except where the surrounding math/code/table structure immediately establishes the meaning.

## `subtraction_operator`

Semantic rule: `" -"` is binary subtraction with a clear left operand and right operand.

Good examples:

- `net = gross - tax`
- `18 - 7`
- `C2 - D2`
- `count - 1`
- `forecast - actual`
- `SELECT total - refunded AS net`
- `(f(x+h) - f(x)) / h`

Include:

- Raw math, proofs, derivations, LaTeX-ish excerpts, statistics, probability, numerical methods, matrices, calculus, algebra, and research fragments.
- Code, SQL, parser tests, compiler/build logs, telemetry, metrics, notebooks, and formulas embedded in technical docs.
- Worksheets, answer keys, spreadsheet rows, tables, invoices, budgets, lab/engineering measurements, analytics, and everyday calculations.
- Positive, zero, and negative results where the binary operation is still clear.

Exclude:

- Unary negative: `x = - 7`, `it was - 2`.
- Informal separators: `late - again`.
- List markers: ` - item`.
- Ranges and hyphenation: `12-15 minutes`, `pre-tax`.
- Command flags or double-dash artifacts: `cmd -v`, ` -- option`.

Guidance:

- This label should lean technical and multi-use because subtraction naturally repeats in formulas, code, proofs, and tables.
- Do not over-explain arithmetic in natural language. Raw formulas, proof steps, code blocks, and table excerpts are often better.
- Avoid making this label mostly accounting or everyday examples; it needs substantial deep math and technical material.
- Messy artifacts must not introduce another meaning of `" -"`. Use colons, pipes, commas, or unspaced hyphens for unrelated separators.

## `list_item_denoter`

Semantic rule: `" -"` marks a list item.

Good examples:

- `Need by Friday:\n - signed form\n - deposit receipt`
- `items:\n - id: 104\n   name: spare filter`
- `Meeting notes\nParking\n - visitor lot\n - meter cards`

Include:

- Personal lists, shopping/packing notes, reminders, recipes, event plans, and household scraps.
- README/wiki/docs lists, YAML-like excerpts, release notes, configs, issue templates, support checklists, QA steps, and incident notes.
- School/LMS fragments, agendas, meeting notes, job posts, newsletters, ecommerce lists, OCR/PDF text, HTML snippets, emails, chats, and forum posts.
- Nested, repeated, or interrupted lists in longer samples.

Exclude:

- Subtraction: `total - discount`.
- Informal separators: `done - finally`.
- Command flags or options where the dash is not a bullet.

Guidance:

- Most samples should have multiple list markers, with some one- or two-item scraps and some long nested/messy lists.
- In long samples, place list markers throughout the sequence, not only at the top.
- Keep non-list prose from accidentally using `" -"` as a separator or subtraction operator.
- Avoid overusing tidy `label:\n - item` patterns; mix in broken exports, HTML, OCR, emails, comments, and partial pages.

## `text_separator_informal`

Semantic rule: `" -"` is an informal dash-like separator between clauses, notes, labels, or afterthoughts.

Good examples:

- `coffee was fine - the music was too loud`
- `status says shipped - tracking still has no scan`
- `photo caption: west gate - rain starting again`

Include:

- Reviews, comments, chats, casual posts, emails, captions, newsletters, support notes, transcripts, listings, and rough page text.
- Human fragments with mild messiness: edits, side comments, duplicated footers, mobile scrape artifacts, stale snippets, and partial replies.
- Some code comments or UI text where the dash acts like an informal separator, not an operator or option marker.

Exclude:

- Arithmetic or formulas: `10 - 3`, `price - tax`.
- Line-start bullets: ` - item`.
- Double-dash signature/markup artifacts where the exact token is part of ` --`.
- Command flags or option syntax.

Guidance:

- This label usually needs fewer token uses per sample than subtraction or lists. One or two separators often feels most realistic.
- Do not turn every sentence into an `X - Y` pattern. Vary placement, length, and surrounding text.
- Make sure separator samples do not look like math, table formulas, or list items.

## QA Checklist

Per sample:

- Contains exact token `" -"`.
- Every occurrence has the target meaning.
- Does not start with the token, and usually does not place it extremely early.
- Avoids source-intro wrappers unless the wrapper is genuinely part of the raw text.
- Is plausible as web/SFT corpus text, not a meta-example about the label.
- Is valid YAML.

Per meaning:

- Exactly 100 samples.
- Lengths, token counts, source types, tones, and formats are visibly varied.
- No dominant opening pattern, topic cluster, or narrative template.
- Includes rough/partial/crawled material without making artifacts theatrical.
- Manually inspect high-risk cases: unary negatives, line-start hyphens, arithmetic in separator/list labels, informal dashes in subtraction/list labels, command flags, and ` --` double-dash artifacts.
