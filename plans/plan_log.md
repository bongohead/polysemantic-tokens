# Plan: Polytok Token `" log"`

## Objective

Create `dsv2/samples_log.yaml` with 100 realistic samples for each meaning label:

- `logarithm`
- `record_or_log_file`
- `wood_log`

Every sample must contain the exact token `" log"` at least once. Every occurrence of `" log"` inside a sample must match that sample's `meaning_label`.

This token is high-risk because it appears as a standalone word, a function name, a command/API concept, and a prefix inside longer words. Treat lowercase exact matches carefully. Avoid unrelated continuations such as ` login`, ` logout`, ` logic`, ` logical`, ` logistics`, ` logo`, ` logjam`, and casual phrases like ` log in` unless the sample's meaning is genuinely the written-record sense, which `log in` is not.

## Exact-String Notes

The target is a literal space followed by lowercase `log`.

- ` log`, ` logs`, ` logged`, ` logging`, ` logbook`, ` logarithm`, ` logarithmic`, ` log-likelihood`, ` log10`, and ` lognormal` contain the exact token and must be semantically correct for the active label.
- `Log`, `log` at the beginning of a sample or line, `\log`, `.log`, `console.log`, `logger.log`, `/var/log`, `app.log`, and `error_log` do not by themselves satisfy the exact token, though they may appear as surrounding context if another exact target occurrence is present.
- Avoid relying on punctuation-adjacent forms such as `(log x)` or `/log` unless there is also a clear exact `" log"` elsewhere.
- If a non-target form appears in the sample, keep it semantically compatible with the label when possible so the whole excerpt still feels coherent.

## Realism Standard

Samples should feel like mixed C4/HPLT-style web data rather than curated examples. Use raw excerpts when plausible: math notes, code, terminal output, config files, telemetry tables, bug reports, lab notebooks, ship journals, attendance records, cabin listings, firewood ads, woodworking forums, OCR pages, scraped HTML, transcripts, emails, and partial comments.

Good samples can be clipped, redundant, malformed, or surrounded by adjacent page residue. Include plausible artifacts such as table headers, repeated footers, old nav text, copied comments, timestamps, stack traces, CSV columns, OCR line breaks, stale captions, ad placeholders, PDF page headers, and thread metadata.

Avoid source-intro wrappers such as `math example:`, `the log file says`, `firewood listing:`, or `snippet:` unless such labels are genuinely part of the artifact. The sample should be the artifact itself, not a description of the artifact.

## Distribution Guidance

Use approximate distributions, not exact quotas.

- Length: include a few very short fragments, many short and medium samples, and a meaningful minority of long messy samples.
- Token placement: do not start any sample with `" log"`. In longer samples, ensure the target token also appears late in the sequence sometimes, not only near the beginning.
- Token density: use enough target tokens to make the meaning clear, but avoid stuffing. Math and record/log-file samples can naturally repeat ` log`; wood samples often need fewer repetitions.
- Source mix: include technical, educational, workplace, commercial, informal, historical, structured, and crawled/OCR styles.
- Voice and tone: vary between neutral machine output, terse notes, confused users, polished documentation, academic prose, ads, support tickets, forum replies, and mundane personal writing.
- Completeness: not every sample should be self-contained. Some should start or end abruptly as if scraped from the middle of a page.
- Case: the target token is lowercase `" log"`. Uppercase `Log` can appear for realism, but it does not satisfy the target by itself and should not be relied on.

## `logarithm`

Semantic rule: `" log"` refers to the mathematical logarithm or a derived mathematical/statistical quantity based on logarithms.

Good examples:

- `take log x before fitting the line`
- `loss = -sum(y * log p)`
- `plot log(count) against time`
- `log_2 n`, `log10(value)`, `natural log`
- `log-likelihood`, `log odds`, `log scale`, `log transform`

Include:

- Raw math, homework, lecture notes, proofs, derivations, asymptotic analysis, information theory, probability, statistics, econometrics, calculus, numerical methods, and machine learning loss functions.
- Code and notebooks where `log` is a math function: Python/R/Julia/Matlab snippets, NumPy/PyTorch/TensorFlow expressions, SQL analytics, parser tests, spreadsheet formulas, and plotting code.
- Research fragments: log-likelihood, log posterior, log odds, log hazard, log returns, log-normal/lognormal discussion, entropy/cross-entropy, and log-sum-exp.
- Educational content with messy formatting: quiz answers, worksheets, scanned formula sheets, LaTeX-ish text, StackExchange-style replies, and markdown tables.
- Contexts where base is explicit or implicit: natural log, base 10 log, base 2 log, common log, ` log1p`, ` log2`, and ` log10`.
- Longer mathematical words that contain the exact token and remain sense-aligned: ` logarithm`, ` logarithmic`, ` logarithms`, and ` logarithmically`.

Exclude:

- File/application logs: `error log`, `server log`, `debug log`.
- Written records: `captain's log`, `call log`, `lab log`, `activity log`.
- Wood: `split log`, `cedar log`, `log pile`.
- Authentication phrases: `log in`, `log out`, `login`, `logout`.
- Unrelated words beginning with the same letters: `logic`, `logical`, `logistics`, `logo`, `logjam`.
- Timber-industry verbs and nouns unless the exact occurrence is clearly the mathematical term, which it usually will not be.

Guidance:

- This label can lean technical because mathematical `log` is common in formulas, code, ML, statistics, and documentation.
- Use raw formulas and code generously. Do not turn every sample into a natural-language explanation of what a logarithm is.
- Avoid overconcentrating on one topic such as cross-entropy. Mix asymptotics, pH, decibels, finance, biology, astronomy, regression, complexity, and classroom algebra.
- Be careful with `log` in code: in many codebases it means logging output rather than logarithm. Only use code where imports, variables, or surrounding text make the math sense unambiguous.
- Hyphenated or compound terms such as `log-likelihood`, `log-scale`, and `lognormal` are acceptable only when the occurrence clearly means logarithm-derived.
- Rotate surface forms: standalone ` log`, function-call ` log(...)`, base-marked ` log2`/` log10`, prose ` natural log`, compound ` log-likelihood`, and full-word ` logarithm`/` logarithmic`.

## `record_or_log_file`

Semantic rule: `" log"` refers to a written/typed record, log file, event stream, journal entry, or the act of recording an event. This includes software logs and human records, but not authentication.

Good examples:

- `check the error log after restart`
- `audit log retained for 90 days`
- `Captain's log, supplemental`
- `please log each sample before freezing it`
- `call log shows three missed attempts`
- `journalctl wrote the same log line twice`

Include:

- Software and operations data: server logs, access logs, debug logs, syslog/journald output, CI logs, Kubernetes pod logs, app telemetry, crash logs, ETL job logs, device logs, and support bundles.
- Written records: ship logs, flight logs, dive logs, maintenance logs, visitor logs, incident logs, field logs, lab logs, reading logs, mileage logs, work logs, and classroom behavior logs.
- Verbs and gerunds when the sense is recording: `log the result`, `logging temperature`, `logged by the nurse`, `logger`, `logbook`.
- Raw artifacts: timestamps, severity levels, stack traces, JSON log events, CSV exports, ticket notes, audit tables, monitoring alerts, emailed reports, and copied terminal snippets.
- Mundane administrative text: sign-in sheets, compliance records, meeting action logs, patrol logs, volunteer hour logs, equipment checkout logs, and generated reports.
- Developer/documentation contexts where the exact token appears as text: ` log file`, ` log line`, ` log level`, ` log stream`, ` log rotation`, ` log collector`, and ` log retention`.

Exclude:

- Mathematical logarithms: `log x`, `log-likelihood`, `natural log`, `log scale`.
- Wood: `fireplace log`, `fallen log`, `sawn log`.
- Authentication/action phrases: `log in`, `log into`, `log out`, `login page`, `logout button`. These are not written records.
- Unrelated prefixes: `logic`, `logical`, `logistics`, `logo`.
- Timber operations where `logging` means cutting trees rather than recording data.

Guidance:

- This label should be especially diverse and messy because real logs and records are abundant in web corpora.
- Do not make every sample a polished "check the log" sentence. Include raw timestamped lines, JSON, terminal excerpts, service dashboards, email forwards, paper-form OCR, and human notes.
- Record-related samples can include many target tokens, but make sure every one is the record sense. If a stack trace contains math code using `log(x)`, do not use it for this label.
- `log file`, `log entry`, `log line`, `log level`, `log rotation`, `logbook`, and `logging` are valid when they refer to recording events.
- Avoid accidental `log in` strings in support tickets and UI docs; authentication is a separate sense and should be excluded.
- Rotate between machine records, human-written records, and verbs of recording. Avoid letting software error logs crowd out field logs, call logs, maintenance logs, and journal/logbook excerpts.

## `wood_log`

Semantic rule: `" log"` refers to a physical piece of wood from a tree, whether whole, split, cut, stacked, burned, milled, floated, or used as building material.

Good examples:

- `split the oak log before stacking it`
- `a wet log rolled off the pile`
- `cedar log siding needs oil`
- `fireplace log was too long for the stove`
- `the trail crossed a fallen log`
- `log cabin wall settled after winter`

Include:

- Firewood, camping, fireplaces, woodstoves, sawmills, forestry, woodworking, lumber yards, log cabins, trail maintenance, river cleanup, playground equipment, rustic furniture, and natural-history text.
- Ads and listings: firewood sales, cabin rentals, sawmill inventory, chainsaw/splitter products, campground notes, homestead blogs, Craigslist-style posts, ecommerce reviews, and building-material pages.
- Messy artifacts: product specs, delivery tickets, scraped classifieds, OCR from forestry manuals, forum posts, park notices, cabin inspection notes, recipe/blog sidebars only if the wood sense remains clear.
- Physical states and operations: green log, dry log, split log, peeled log, cedar log, oak log, saw log, veneer log, rotten log, log pile, log stack, log splitter, log deck.
- Physical measurements and commerce: diameter, length, board feet, cords, moisture content, species, delivery tickets, sawmill grades, splitter tonnage, stove clearances, and trail obstacle reports.

Exclude:

- Mathematical logarithms: `log x`, `log scale`, `natural log`.
- Records and files: `event log`, `visitor log`, `captain's log`, `debug log`, `log entry`.
- Authentication: `log in`, `logout`, `login`.
- Metaphorical or lexicalized uses where no physical wood piece is present: `logjam` as political delay, `sleep like a log`, `bump on a log`.
- Timber-industry `logging` if the sample never refers to actual logs as pieces of wood.

Guidance:

- This label should feel more everyday/commercial/outdoor than technical, but include some structured data from sawmills, forestry inventories, product specs, and cabin construction notes.
- Use singular and plural forms naturally. `logs` contains the exact token as the beginning of ` logs`, and is valid when it means pieces of wood.
- Include some scenes with one log and some with piles, cords, bundles, trucks, cabins, trails, and sawmill measurements.
- Avoid making the label just cozy fireplace prose. Mix practical, muddy, commercial, safety, maintenance, and awkward scraped data.
- Be cautious with `log cabin`: acceptable when the construction material is clearly physical logs, but do not let cabin-rental text drift into `guest log` or `activity log`.
- Rotate between wild/outdoor contexts, retail listings, construction, sawmill/forestry data, home heating, craft/woodworking, and accident/safety notes.

## Cross-Meaning Hazards

Inspect these cases manually during dataset creation:

- ` log in`, ` log into`, ` logged in`, ` logging in`: authentication, exclude from all three labels unless rewritten.
- ` logging`: record sense if software/data recording; timber sense if cutting trees; avoid in `wood_log` unless actual wood logs are also present and every target occurrence is wood-related.
- ` logbook`: usually record sense.
- ` lognormal`, `log-normal`, ` logit`, `logistic regression`: often math/statistics adjacent. `lognormal` can be logarithm-derived; `logistic` is not a logarithm and should generally be excluded despite the prefix.
- ` log odds`: mathematics/statistics, not record.
- `\log`, `.log`, `/var/log`, and `console.log`: visually relevant but not exact target occurrences unless another `" log"` appears.
- ` blog`, `catalog`, `dialog`, `prolog`: usually do not contain the exact leading-space token, but avoid contrived text that makes them ambiguous.
- `log` in code: may be math function, logger call, or console output. Use only when the intended sense is unmistakable.
- `captain's log`: record sense, even if fictional/sci-fi styled.
- `saw log`: wood sense, a log intended for sawing, not the verb "saw" plus record.

## Dataset Creation Strategy

Build `dsv2/samples_log.yaml` in rounds of about 20 samples per label, then review and revise before adding the next round.

For each `logarithm` round, deliberately cover several of:

- Formula/proof fragments, classroom exercises, statistical modeling, ML/code loss functions, finance/returns, signal scales such as dB or pH, plots/axes, and messy notebook/table exports.
- Surface forms such as ` log`, ` log(x)`, ` log2`, ` log10`, ` natural log`, ` log-likelihood`, ` log odds`, ` logarithm`, and ` logarithmic`.

For each `record_or_log_file` round, deliberately cover several of:

- Raw machine logs, log-file documentation, monitoring alerts, support tickets, audit/compliance exports, human sign-in records, ship/flight/dive/field logs, maintenance notes, lab records, and school/workplace forms.
- Surface forms such as ` log`, ` logs`, ` log file`, ` log entry`, ` log line`, ` log level`, ` logbook`, ` logged`, and ` logging`.

For each `wood_log` round, deliberately cover several of:

- Firewood ads, stove/fireplace use, trail/park notes, sawmill inventory, forestry measurements, cabin construction, product reviews, camping text, woodworking forums, delivery tickets, and OCR/manual fragments.
- Surface forms such as ` log`, ` logs`, ` split log`, ` oak log`, ` cedar log`, ` saw log`, ` log pile`, ` log cabin`, ` log splitter`, and ` log deck`.

After each round:

- Search every exact `" log"` occurrence and classify it manually.
- Scan for ` login`, ` logout`, ` logic`, ` logical`, ` logistics`, ` logo`, ` log in`, and ` logged in`.
- Check that the first exact target token is not at the beginning and is not always in the first clause.
- Check that long samples contain some late target occurrences.
- Rebalance if a label is becoming too tidy, too explanatory, too software-heavy, too classroom-heavy, or too cozy/outdoorsy.
- Validate YAML structure before continuing.

## QA Checklist

Per sample:

- Contains exact lowercase token `" log"` at least once.
- Every occurrence of `" log"` has the target meaning, including occurrences inside longer lowercase words such as `logs`, `logged`, `logging`, `logbook`, or `lognormal`.
- Does not start with the token and usually delays the first occurrence by several tokens.
- Avoids curator-style source introductions unless they are naturally part of the artifact.
- Is plausible as web/SFT corpus text, with realistic messiness and no theatrical over-explanation.
- Avoids unrelated `login`, `logout`, `logic`, `logical`, `logistics`, `logo`, and authentication phrases.
- Is valid YAML when inserted into `dsv2/samples_log.yaml`.

Per meaning:

- Exactly 100 samples.
- Lengths, source types, voices, formats, emotional registers, and token counts are visibly varied.
- No dominant opening pattern, topic cluster, or narrative template.
- Includes rough/partial/crawled material without simply labeling the source type.
- Has target tokens distributed across early, middle, and late positions, especially in longer samples.
- Includes short fragments, medium artifacts, and some long messy samples.
- Manually inspect high-risk cases where software logs, math logs, and wood logs can appear near each other.
