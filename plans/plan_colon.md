# Plan: Polytok Token `":"`

## Objective

Create `dsv2/samples_colon.yaml` with 100 realistic samples for each meaning label:

- `introduces_a_list`
- `time_separator`
- `function_type_annotation`

Every sample must contain the exact token `":"` at least once. Every colon character inside a sample must match that sample's `meaning_label`.

Use the current dsv2 flat YAML schema, matching files such as `dsv2/samples_-.yaml`: one top-level item per meaning label, with `token`, `meaning_label`, and `text_samples` fields. Do not copy the old nested `meanings:` structure from `ds/samples_colon.yaml`.

This token is especially high-risk because it is a single punctuation character. A sample can be invalidated by one stray URL, timestamp, Python block colon, JSON key-value colon, line-number reference, ratio, emoticon, or speaker label. Treat every colon as a target occurrence and classify every one.

The old `ds/samples_colon.yaml` is useful as a rough label source, but it is too clean and repetitive. It also mixes meanings in several places, especially `time_separator` samples with `15:45:` message punctuation and `function_type_annotation` samples with Python trailing block colons or object-literal colons. The v2 file should be much stricter and much messier.

## Exact-Character Notes

The target is the literal ASCII colon character.

- Every `:` counts, regardless of surrounding spaces, case, code formatting, or whether it appears inside punctuation such as `::`, `://`, `12:30`, `name: value`, or `x: string`.
- Fullwidth colon (U+FF1A) and visually similar punctuation should not be used as substitutes.
- Do not rely on the sample "mostly" being one sense. If even one colon has another function, rewrite or discard the sample.
- Avoid accidental colons from common web artifacts unless they are the intended label: `https://`, `mailto:`, `C:\`, `localhost:3000`, `file.ts:42:13`, `node:20`, `John 3:16`, `3:2`, `:)`, `:hover`, `std::vector`, `value::int`, `a[1:3]`, and `cond ? a : b`.
- Because the token is only one character, the first colon can easily occur too early. Do not start any sample with `:`, and avoid making most samples begin with a one-word label like `Status:` or `Note:`. When a real artifact naturally begins that way, balance it with other samples that have row prefixes, preceding prose, table headers, or partial scraped context before the first colon.

## Realism Standard

Samples should feel like a mixed C4/HPLT-style slice, not curated punctuation demonstrations. Use raw excerpts directly when plausible: forms, headers, emails, scraped pages, config fragments, code signatures, subtitles, schedules, support tickets, OCR forms, product specs, school materials, monitoring exports, calendar rows, forum/chat fragments, and partial documents.

Good samples can be clipped, mundane, redundant, noisy, or surrounded by adjacent page residue. Include plausible artifacts such as table headers, repeated footers, old navigation text, cookie boilerplate, OCR line breaks, collapsed comments, CSV/TSV rows, HTML fragments, copied email headers, subtitle cue blocks, and generated docs.

Avoid source-intro wrappers such as `form:`, `timestamp example:`, `code snippet:`, `the page says`, or `copied text:` unless such labels are genuinely part of the artifact and their colon has the active meaning. The sample should be the artifact itself, not a description of it.

## Lessons From The Old File

Use the old `ds/samples_colon.yaml` only as a starting taxonomy. It should not set the quality or boundary standard.

- The first label was narrowed from the old broad `introduces_what_follows` sense to `introduces_a_list`. V2 must reject broad key-value, speaker-label, header, CSS, and explanatory-only colons unless the colon is introducing a list of multiple items, examples, or steps.
- `time_separator` often mixes valid clock colons with invalid label colons, such as `Timeline of events:` or `15:45:` before a message. V2 time samples should use schedule/table/log formats where every colon is inside the time value.
- `function_type_annotation` overuses Python and TypeScript teaching examples. Many old Python examples contain trailing block colons, `if:`/`else:` colons, or dict/object-literal colons, so they are invalid under the stricter rule.
- Several old samples begin with curator framing such as `Here's a Python snippet:`. V2 samples should usually begin as the artifact itself: code, row, copied field, schedule line, or paragraph.
- Long old samples often stay clean and self-contained. V2 should include noisier, partial, crawled, and mechanically generated excerpts while still keeping every colon semantically pure.

## Distribution Guidance

Use approximate distributions, not exact quotas.

- Length: include a few very short fragments, many short and medium samples, and a meaningful minority of long messy samples.
- Token placement: do not start any sample with `:`. Avoid making first-colon positions monotonous; for this token, a form field or clock at the very beginning can make many samples look samey even when technically valid. In longer samples, ensure some colons occur in the middle or late in the sequence, not only in the first line.
- Token density: `introduces_a_list` is usually lower than the code/time labels, but long scraped list artifacts can have several list-introducing colons. `function_type_annotation` can naturally have many colons. `time_separator` can repeat heavily in logs, subtitles, tables, and schedules. Avoid artificial stuffing.
- Source mix: include technical, educational, workplace, commercial, informal, structured, crawled/OCR, auto-generated, and conversational styles where they fit each label.
- Voice and tone: vary between neutral machine output, terse notes, confused users, polished docs, bureaucratic forms, excited announcements, frustrated support text, and raw copied data.
- Completeness: not every sample should be self-contained. Some can start or end abruptly as if scraped from the middle of a page.
- Cross-contamination: because colons are common in artifact metadata, choose formats that do not accidentally introduce another colon sense.

## Diversity Dimensions To Track

Track these dimensions during each 20-sample round so the dataset does not collapse into a few easy templates:

- Source format: prose, form fields, tables, email/header blocks, config, code signatures, subtitles, logs, OCR/PDF text, scraped HTML, comments, chat/forum fragments, product/admin text, and generated docs.
- Colon surface form: single prose colon, repeated label-value colons, multi-component times, timestamp ranges, callback signatures, return type annotations, double-colon type signatures, and nested callable types.
- First-colon position: early but not first character, mid-sentence, table-body, late paragraph, late code line, and repeated throughout long artifacts.
- Cleanliness: clean instructional text, raw copied rows, partial excerpts, OCR noise, page residue, ad/footer contamination, broken formatting, and generated boilerplate.
- Voice/register: neutral machine output, terse human notes, confused support/user text, bureaucratic forms, polished docs, excited community posts, and dry academic or technical prose.
- Domain spread: education, software, operations, transit, media, health/admin, commerce, legal, HR, events, household, research, and hobbies.
- Completeness and length: clipped fragments, short rows, medium documents, and long messy sequences with late target use.

## `introduces_a_list`

Semantic rule: `:` appears after a clause or phrase and introduces a list of items, examples, options, steps, required materials, categories, symptoms, files, or other multiple entries. The left side sets up what the list will contain. This is narrower than the earlier broad "introduces what follows" label.

Good examples:

- `Bring three things: gloves, a mug, and sunscreen`
- `The kit includes: charger, manual, and spare strap`
- `Requirements: node 20, pnpm, sqlite file in ./data`
- `She tried everything: restarting, clearing cache, switching browsers`
- `Banned items: glass bottles, sparklers, drones, open flames`

Include:

- Inline prose list introducers, including casual or partial sentences.
- Headings or short phrases that introduce multiple items, such as `Requirements:`, `Supplies:`, `Banned items:`, or `Changed files:`.
- Messy scraped list contexts where every colon introduces a list: newsletter fragments, recipe notes, forum replies, product pages, school packets, release checklists, OCR/PDF text, collapsed tables, and comment threads.
- Single colon samples with one list, and longer artifacts with several list-introducing colons.

Exclude:

- Explanatory or elaboration colons with no list: `The answer was obvious: nobody had checked the lock`.
- Key-value, header, metadata, CSS, localization, config, and form-field colons when the right side is a single value: `Color: blue`, `Content-Type: application/json`, `checkout.pay_now: Pay now`.
- Speaker labels and dialogue labels: `ALICE: the printer is jammed`.
- Function/type annotations, timestamps, URLs, ratios, line-column references, object literals, YAML mappings, CSS declarations, ternaries, slices, namespace operators, and emoticons.

Guidance:

- Do not turn this into a wall of administrative field labels. Mix household notes, product pages, recipes, support/checklist text, research excerpts, school materials, forums, newsletters, release notes, messy HTML, and OCR fragments.
- The list can be short, but the section as a whole needs some medium and long scraped artifacts with late colons.
- If a line looks like `Label: single value`, reject or rewrite it. If it looks like `Label: item, item, item`, it can fit, but do not overuse this field-label surface.
- Every colon in the sample must introduce a list. One timestamp, CSS property, email header, speaker tag, type annotation, or URL invalidates the sample for this label.

## Superseded Earlier Broad Label: `introduces_what_follows`

Historical note only: do not use this broad label for the current YAML. The current first label is `introduces_a_list`, and it excludes key-value, header, speaker-label, CSS/property, and explanatory-only colon uses. The material below is kept only to explain earlier review history and old-file failure modes.

Semantic rule: `:` introduces, identifies, labels, or points forward to content that follows. This includes prose list-introducing colons, label-value fields, headings, speaker labels, message headers, property declarations, and mapping delimiters, as long as every colon in the sample has that "what follows belongs to or elaborates the preceding cue" function.

Good examples:

- `Please send these files: waiver, receipt, and the signed cover sheet`
- `case 481 Status: pending review`
- `Maya wrote back: send the shorter version`
- `Content-Type: text/html`
- `shipping_notice:\n  carrier: postal\n  service: ground`
- `button_label: Continue`

Include:

- Prose list introducers, explanations, appositives, announcements, Q/A items, titles/subtitles, section headings, photo captions, and quoted speech.
- Label-value artifacts: forms, intake sheets, product specs, inventory rows, issue templates, bug reports, moderation exports, LMS fields, support macros, and OCR forms.
- Conventional commit and changelog prefixes such as `fix:`, `feat:`, `docs:`, and `breaking change:` when the colon introduces the following summary.
- Email and web headers: `From:`, `To:`, `Subject:`, `Content-Type:`, newsletter fields, cookie banner settings, and generated notification templates.
- Mapping/config/property syntax where the colon introduces a value: YAML front matter, simple JSON-like fragments, CSS declarations, localization files, package metadata, HTTP headers, and API docs with field/value lines. Keep all colons in the same label-value role; do not mix in typed function signatures.
- Dialogue and transcript labels such as `OP:`, `AGENT:`, or `SPEAKER_02:` when the colon introduces the following utterance. Avoid adding timestamp colons in the same sample.
- Messy scraped material: breadcrumbs, sidebars, repeated form fields, partial HTML tables, flattened PDF text, duplicated footer labels, ad copy with fields, and spreadsheet exports.

Exclude:

- Time and duration separators: `09:30`, `14:03:52`, `00:01:04,500`.
- Function or callable type annotations: `name: string`, `fn parse(x: &str)`.
- URLs, URI schemes, drive letters, host ports, and paths: `https://`, `mailto:`, `C:\`, `localhost:8080`.
- Container image tags, version tags, package coordinates, and registry references: `node:20`, `postgres:16-alpine`, `repo/image:latest`.
- Ratios, scores, chapter/verse references, citations, and line-column references: `3:1`, `2:0`, `John 3:16`, `file.ts:42:13`.
- CSS pseudo-selectors, Python slices, ternary operators, namespace operators, emoticons, and emoji shortcodes: `:hover`, `a[1:3]`, `x ? y : z`, `std::map`, `:)`, `:warning:`.
- Python, YAML, or code examples where one colon is a block delimiter, slice delimiter, or other non-introducing syntax.

Guidance:

- This label should be broad but not bland. Avoid making it mostly polished sentences like `The list is as follows: ...`.
- Rotate between human prose, raw form fields, structured configs, headers, comments, partial emails, product pages, school worksheets, legal/medical/HR forms, and scraped OCR.
- Label-value samples can contain many colons, but all values should be plausible and all colon uses must remain label-value or introduction. Avoid URLs inside contact fields; use `site example dot com` or omit the URL.
- Be careful with real headers whose values contain other colon types. `Date: Tue, 05 May 2026 18:30:00 GMT` mixes a header colon and time colons, so it is invalid for this label.
- A short field-first fragment can be valid, but do not let the label become a wall of `Status:`, `Note:`, `Name:`, and `Subject:` openings. Use surrounding rows, pasted headers, OCR fragments, or preceding body text to vary where the first colon lands.
- Speaker-label samples should not also contain timestamp colons. Use plain speaker labels or use dashes/commas for surrounding metadata.
- In CSS samples, use declarations such as `color: #333; margin: 0;` only. Avoid selectors like `a:hover` because that colon is not introducing a value.

## `time_separator`

Semantic rule: `:` separates components of a time, elapsed duration, media timestamp, clock reading, time-zone offset, or similar temporal quantity. Every colon must be between temporal components, usually digits.

Good examples:

- `The train leaves at 07:45 and reaches Albany at 10:12`
- `2025-07-12T14:03:52Z INFO user session started`
- `cue 17 00:01:04,800 --> 00:01:07,200`
- `race split 00:18:44.2 after lap four`
- `maintenance window 22:00-02:00 UTC`
- `offset -04:00 in the exported calendar row`

Include:

- Schedules, transit notices, school timetables, TV/radio listings, shift rosters, clinic appointment rows, event agendas, and calendar exports.
- System and application logs that use timestamps, but only when later punctuation does not add label colons. Prefer `2025-07-12T14:03:52Z INFO started` over `14:03:52: started`.
- SRT/WebVTT subtitle cues, podcast/audiobook chapter timestamps, video editing cue sheets, transcript timing blocks, and media QA logs.
- Stopwatch and duration data: race splits, lab timers, cooking timers, call durations, uptime/downtime windows, backup elapsed times, audio lengths, and cron summaries.
- Structured rows: CSV/TSV exports, tables, monitoring samples, timetable grids, and schedule fragments where all colons are inside time values.
- 12-hour and 24-hour clocks, seconds, milliseconds, ranges, timezone offsets, ISO times, and repeated clock entries.

Exclude:

- Any label or message-introducing colon: `Time: 09:00`, `Start: 11:30`, `INFO:`, `Speaker:`.
- Timestamps followed by a punctuation colon: `15:45:` has a valid time colon and an invalid introducing colon.
- Ratios, sports scores, Bible/chapter references, legal citations, dictionary entries, and proportions: `3:2`, `Luke 4:8`, `Title 12:102`.
- URLs, host ports, IPv6/MAC addresses, file/line references, version metadata, and hashes.
- Function type annotations, key-value fields, JSON/YAML, CSS declarations, slices, ternary operators, emoticons, and namespace operators.
- Docker/image tags, package tags, and versioned identifiers such as `python:3.12` or `redis:7`.
- Chat transcripts that combine timestamps and speaker labels like `[12:04] Alex:`. Use timestamp-only rows or remove the speaker-label colon.

Guidance:

- The safest time samples have every colon surrounded by digits or by a timezone offset pattern. Still manually inspect offsets and ISO strings.
- Logs should look raw, but avoid the common `timestamp: message` format because the final colon changes meaning.
- For subtitle and log-like samples, avoid making every sample begin with `00:...` or an ISO timestamp. Add realistic cue numbers, table rows, dates without colons, comma-delimited metadata, or preceding transcript text when it fits.
- Do not make this label only meeting reminders. Mix media cues, transit, log timestamps, race splits, security camera exports, shift rosters, appointment reminders, cooking/lab timers, and scraped schedule tables.
- Long samples should include times throughout the body, such as a timetable with ad residue or a subtitle fragment with multiple cue blocks.
- When a line needs metadata, use commas, pipes, brackets without colons, or words instead of labels with colons.

## `function_type_annotation`

Semantic rule: `:` marks a declared type in code, with emphasis on functions, methods, callbacks, closures, callable types, function-like schema signatures, and everyday typed locals that appear in code/function context. The colon binds a parameter, receiver, callback, function value, return position, typed local, inline callable field, or method field to a type. Every colon in the sample must be a type annotation, not a runtime key-value delimiter or block delimiter.

Good examples:

- `function parseLine(input: string, strict: boolean): ParsedLine { return parse(input, strict); }`
- `const score = (row: Row, weight: number): number => row.value * weight`
- `const gain: number = 0.7`
- `handler: Callable[[Request], Response] = make_handler()`
- `fun lookupUser(id: String, limit: Int): List<User>`
- `fn decode(src: &str, allow_empty: bool) -> Result<Token, Error>`
- `def fold[A](xs: List[A], zero: A)(f: (A, A) => A): A = xs.foldLeft(zero)(f)`
- `type Handler = (req: Request, next: NextFn) => Response`

Include:

- Real TypeScript and Flow syntax, `.d.ts` files, typed callbacks, React/Node handler signatures, generated JSDoc/TypeDoc signatures, and generated SDK function declarations.
- Kotlin, Swift, Scala, Rust, Hack/PHP return types, OCaml/F# typed functions, Haskell function signatures, and other real languages where colons are part of function or callable type declarations.
- GraphQL or schema-like callable fields when the field has arguments and a return type, such as `search(q: String, limit: Int): [Result!]`.
- Function type aliases and callback fields: `onSave: (draft: Draft) => Promise<void>`, `compare: (a: Row, b: Row) => number`.
- Incidental local/constant annotations in real code, especially when they surround or feed typed functions: `const speed: number = 5`, `let cutoff: f32 = 0.2`, `handler: Callable[[Request], Response] = make_handler()`.
- Scientific and numerical code with real type-annotation syntax, including Julia-style `arg::Type` and return annotations when they are declaration annotations rather than namespace/cast syntax.
- Compiler or documentation fragments that print function signatures, provided file-location colons are removed or rewritten.
- Messy code-adjacent artifacts: minified declarations, generated docs tables, copied issue comments, README API sections, partial diffs, CI snippets, and editor hover text, as long as every colon remains type-annotation syntax.

Exclude:

- Python full function definitions such as `def f(x: int) -> int:` because the trailing colon is a block delimiter, not a type annotation.
- Object literals and runtime maps: `return { ok: true }`, JSON responses, YAML configs, CSS declarations, and package metadata.
- Standalone data-model fields with no callable/function/code-execution context, especially if they read like a schema of records rather than executable code. Incidental local variable annotations are allowed when they appear as real code and every colon is a declared-type colon.
- Generic constraints, trait bounds, and where-clauses that use colon for subtyping or bounds rather than an annotated value: `fn run<T: Debug>`, `func decode<T: Codable>`.
- URLs, timestamps, file/line locations, labels, speaker tags, ternary operators, slices, namespace operators, and CSS pseudo-selectors.
- Fake or hypothetical languages. Do not repeat the old-file pattern of saying Go "uses" colon annotations when it does not.
- TypeScript snippets that also contain object-literal returns or labels with colons. If the function must return an object, use constructor calls, tuples, `Object.assign`, or omit the body.

Guidance:

- This label should be code-heavy, but not only neat TypeScript examples. Mix language families and artifact types.
- TypeScript and Flow are useful because parameter and return annotations both use colons, but avoid object literals, object destructuring aliases, `case:` labels, and ternaries.
- Rust, Swift, Kotlin, Scala, OCaml/F#, and GraphQL help diversify surface form while keeping colon semantics clean. Prefer simple concrete parameter and return types over generic bounds that add another colon sense.
- Haskell `::` can be used sparingly for function type signatures, because both colons participate in the type-signature operator. Avoid C++/Rust namespace `::`, which is not a type annotation.
- Python may appear only in surrounding non-colon text or in callable variable annotations such as `handler: Callable[[Request], Response]` if the sample is clearly about function types. Avoid `def ...:` blocks.
- Comments can easily introduce stray label colons. Prefer raw signatures with minimal comments, or comments without colons.
- Documentation excerpts should use signature/code lines or tables whose colons are all type annotations. Avoid surrounding headings like `Parameters:`, `Returns:`, `Example:`, or front matter unless the heading itself introduces a list for `introduces_a_list`.

## Cross-Meaning Hazards

Inspect these cases manually during dataset creation:

- `Start: 09:00` mixes an introducing colon and a time colon. Do not use it for either label.
- `2025-07-12 14:03:52: message` mixes time separators with a message-introducing colon.
- `[12:04] Alex:` mixes a time separator with a speaker-label colon.
- `function f(x: string): string { return { ok: true }; }` mixes function type annotations with object-literal key-value colons.
- `def f(x: int) -> int:` mixes a Python parameter annotation with a block colon.
- `style={{ color: red }}` or `a:hover { color: red }` can mix CSS declaration colons with pseudo-selector or object syntax. CSS/property colons are no longer valid for the first label unless the only colon in the sample is a list-introducing colon outside the CSS itself.
- `https://example.com`, `mailto:`, `tel:`, `urn:`, `C:\`, and `localhost:3000` are not any of the three target labels as written.
- `node:20`, `postgres:16`, `redis:7`, `image:tag`, and similar container/package tags are not any of the three target labels, even if they appear as YAML values after a valid label colon.
- `file.ts:42:13`, stack traces, compiler locations, and grep results are line/column delimiters, not time or introduction.
- `std::vector`, `Foo::bar`, `Module::name`, Rust paths, and PostgreSQL casts such as `value::int` are namespace/scope/cast operators, not Haskell-style function type signatures.
- `a[1:3]`, `slice(1:3)`, and `cond ? yes : no` are range or alternative delimiters, not the target labels.
- `3:1`, `2:0`, `16:9`, `John 3:16`, `RFC 9110:section`, and `Title 42:1983` are ratio/score/reference uses, not time.
- `:)`, `:D`, `:shrug:`, and Markdown/admonition markers are emotive or markup uses. Avoid them.

## Dataset Creation Strategy

Build `dsv2/samples_colon.yaml` in rounds of about 20 samples per label, then review and revise before adding the next round.

For each `introduces_a_list` round, deliberately cover several of:

- Prose list introducers, requirements lists, supply/material lists, changed-file lists, symptoms, answer choices, recipe/shop lists, release checklists, research variable lists, school packets, forum replies, scraped HTML text, OCR/PDF fragments, and messy commerce or newsletter fragments.
- Surface forms such as `Bring:`, `Requirements:`, `Supplies:`, `Banned items:`, `Changed files:`, `Try:`, `Examples:`, and mid-sentence lead-ins like `she tried everything:`. Do not overuse any one of these, and reject speaker/header/CSS/key-value singletons.

For each `time_separator` round, deliberately cover several of:

- Transit/event schedules, shift rosters, appointment reminders, logs with ISO timestamps, subtitle cues, video/audio chapter marks, race splits, lab/cooking timers, call durations, monitoring windows, security camera exports, calendar rows, and scraped timetable tables.
- Surface forms such as `09:30`, `14:03:52`, `00:01:04,500`, `22:00-02:00`, `2025-07-12T14:03:52Z`, `-04:00`, and `1:05:33 elapsed`.

For each `function_type_annotation` round, deliberately cover several of:

- TypeScript/Flow functions, arrow callbacks, `.d.ts` declarations, callback type aliases, Kotlin/Swift/Rust/Scala signatures, OCaml/F# typed functions, Haskell function signatures, GraphQL resolver-like fields, generated SDK docs, README API references, issue comments, and compiler/editor hover snippets.
- Surface forms such as `arg: Type`, `): ReturnType`, `handler: (req: Request) => Response`, `fun f(x: T): U`, `fn f(x: T)`, `field(arg: T): U`, and `name :: A -> B`.

After each round:

- Search every colon and classify it manually.
- For `introduces_a_list`, search for `://`, `:\d`, `::`, `:\)`, `:D`, `:hover`, `?:`, `[...:...]`, function-signature patterns, CSS/property syntax, speaker labels, headers, and time-looking patterns. Treat these as likely failures. A valid first-label colon should introduce multiple list items, not a single field value.
- For `time_separator`, search for colon not surrounded by digits or timezone-offset context; reject `label:`, `timestamp: message`, ratios, URLs, and speaker tags.
- For `function_type_annotation`, search for `{.*:`, `return {`, `def .*:`, `case .*:`, `://`, `::`, `?:`, slices, timestamps, and file locations. Manually distinguish valid Haskell signatures or inline parameter object types from namespace paths, casts, object literals, and block labels.
- Check that no sample starts with `:` and that first-colon positions vary.
- Check that long samples contain some late colons, not only an early header field.
- Rebalance if a label becomes too tidy, too explanatory, too TypeScript-heavy, too meeting-schedule-heavy, too form-field-heavy, or too centered on one domain.
- Validate YAML structure before continuing.

## QA Checklist

Per sample:

- Contains at least one ASCII `:`.
- Every `:` has the target meaning for the active label.
- Does not start with `:` and usually avoids placing the first colon in the first one or two tokens.
- Avoids curator-style source introductions unless the introduction is naturally part of the artifact and its colon has the target meaning.
- Is plausible as web/SFT corpus text, with realistic messiness and no theatrical over-explanation.
- Avoids off-label colon uses such as URLs, non-target timestamps or labels, line numbers, ratios, emoticons, slices, ternaries, namespace operators, and Python block colons.
- Is valid YAML when inserted into `dsv2/samples_colon.yaml`.

Per meaning:

- Exactly 100 samples.
- Lengths, source types, voices, formats, emotional registers, and token counts are visibly varied.
- No dominant opening pattern, topic cluster, or narrative template.
- Includes rough/partial/crawled material without simply labeling the source type.
- Has target colons distributed across early, middle, and late positions, especially in longer samples.
- Includes short fragments, medium artifacts, and some long messy samples.
- Manually inspect high-risk mixed-context cases where time, introduction, and type-annotation colons can appear near each other.

## Review Pass 2026-05-04

This pass responded to the structural review of `time_separator` and `function_type_annotation`, using `always_check.md` as the audit list. I re-read the reference diversity file, re-scanned the current YAML, then replaced or materially rewrote more than 30 too-clean or too-templated samples. The biggest repairs were: many `time_separator` rows no longer end with the same dashboard/thumbnail/repeated-time beat; many `function_type_annotation` rows are no longer interface/protocol/trait API blocks with a "docs lost examples" closer; and several `introduces_what_follows` samples now start in the artifact instead of narrating the artifact.

Checklist answers, answered harshly:

1. Correct, unambiguous meaning: mostly satisfied after repeated scans. Time samples now have only time-component colons in the time section; the only regex hit there is the YAML `token: ":"` line. Function hazards for URLs, paths, object-literal returns, Python block colons, ternaries, emoticons, and `:hover` are clean. I still need to keep manually distinguishing valid Haskell/Julia type syntax from namespace/cast-like `::` in future passes.
2. Diversity in type and messiness: improved, but not perfect. `time_separator` now has personal notes, HTML fragments, SRT/WebVTT cues, logs, travel rows, rosters, lab timers, transit grids, media sheets, and very short fragments. `function_type_annotation` now includes confused users, compiler/editor snippets, scientific code, game physics, firmware, shader/audio, parsers, bioinformatics, and finance math. Residual risk: some generated-doc/API-reference samples remain and should be watched.
3. Dirty data and unique messy data: stronger than before. There are OCR/PDF artifacts, sidebars, copied rows, broken code fences, missing screenshots, notebook crashes, forum replies, spreadsheet scraps, mobile-page residue, and clipped exports. I reduced descriptions like "the page says" and replaced many with raw body text.
4. Voice diversity: improved. There is still plenty of neutral machine output, but also confused learners, forum commenters, maintainers, nurses/front-desk notes, operators, students, support agents, and terse personal notes. Residual risk: the neutral generated-doc voice is still present in function samples, just no longer dominant.
5. Token placement and late use: checked. No sample starts with `:`. Many longer samples contain target colons throughout the body or late in the sequence, especially logs, schedules, label-value artifacts, and code blocks. Residual risk: label-value intro samples naturally have early first colons, so the surrounding formats must stay varied.
6. Avoid introductory phrases and curator labels: improved. I removed many leading narrations and made numerous samples start mid-artifact. Some samples still begin with natural artifact headers like `From:` or `PATIENT NAME:` because those are valid corpus-like beginnings; that is acceptable but should not become the only pattern.
7. Length diversity: current length check is balanced enough but still imperfect. Latest distribution is: `time_separator` 7 very short, 41 short, 51 medium, 1 long; `function_type_annotation` 19 short, 75 medium, 6 long; `introduces_what_follows` 1 very short, 20 short, 68 medium, 11 long. The harsh note is that time is now intentionally much less long-heavy, but may be slightly overcorrected toward short/medium.
8. Repetitive arcs/templates: major improvement. The old time tic of "schedule/log, then dashboard froze/repeated/copied HH:MM" was heavily reduced. The old function tic of "interface with 5-7 methods, then docs clipped/lost examples" was heavily reduced. Residual pattern risk remains in scattered generated docs and route/schedule exports.
9. Abrupt/incomplete starts and endings: yes. Samples now include mid-column timetables, partial subtitle blocks, raw rows, code snippets without imports, forum extracts, broken screenshots, and clipped notes.
10. Not only natural language: satisfied. The dataset includes code, CSS/config/header-like artifacts, logs, SRT/WebVTT, EDL/timecode, CSV-like rows, schemas, type signatures, compiler/editor contexts, OCR forms, and scheduling grids.
11. Tone and emotional register: improved. Most samples remain flat, as realistic web data should, with some confusion, frustration, mundane operational notes, casual personal text, and dry bureaucratic text. The tone is not all calm explainer voice anymore.
12. Topic/domain balance: improved. Time is not just operations dashboards; function is not just SDK panels/stores/users/orders. Domains now include audio DSP, game physics, hardware/firmware, parsers, bioinformatics, scientific computation, transit, healthcare/admin, education, commerce, legal, household, events, and media.
13. Correctness again: rechecked after edits. The strict time scan is clean; the function hazard scan is clean; YAML length/count validation reports 300 samples with 100 per label. Remaining risk is not semantic contamination so much as distributional taste: future passes should keep attacking any cluster that starts to feel like one voice or one export shape.

## Review Pass 2026-05-04 23:15

This pass responded to the later critique that `function_type_annotation` was still too visually repetitive and that all labels needed more realistic diversity. I re-read `always_check.md`, checked the reference `dsv2/samples_-.yaml`, rewrote another set of function samples away from vertical signature blocks, added more incidental locals, compiler/editor/forum/notebook contexts, and dirtied several too-clean `introduces_what_follows` tail samples. I waited until after 23:15 local time before this final validation and checklist update.

Final validation snapshot:

- Timestamp: `2026-05-04T23:15:33-04:00`.
- Sample count: 300 total, 100 per label.
- Length distribution: `function_type_annotation` 0 very short, 61 short, 36 medium, 3 long; `introduces_what_follows` 1 very short, 18 short, 74 medium, 7 long; `time_separator` 7 very short, 41 short, 51 medium, 1 long.
- Duplicate first-80-character starts: 0.
- Samples starting with `:`: 0.
- Samples without `:`: 0.
- Per-label hazard scans: clean for intro/time/function sample ranges.
- Function structural checks: first-line signature-like blocks 0, docs-clipped/lost-examples closers 0, interface/protocol/trait hits 0, language-taxonomy starts 0.
- First-colon placement: function average index 56.4 with 0 early under index 12; intro average index 31.6 with 19 early; time average index 23.2 with 26 early. The intro/time early counts are expected for field and timestamp artifacts, but still worth watching.

Checklist answers, answered harshly:

1. Correct, unambiguous meaning: satisfied by the final scans and manual review. The risky cases are intentional: CSS declaration colons are only in the intro label, time colons are only in time artifacts, and Haskell/Julia-style type colons are only in function type samples. Residual risk is low but not zero because the colon is too common to trust by vibe alone.
2. Diversity in type and messiness: much better than the criticized version. Function samples now include locals, CI fragments, editor hovers, forum questions, notebooks, code review comments, error excerpts, firmware, parsing, audio, physics, biology, shaders, finance, and scientific snippets. Intro and time also have more abrupt and dirty artifacts. Residual issue: intro remains naturally field-heavy.
3. Dirty data and unique messy data: improved. There are OCR/PDF fragments, missing screenshots, clipped panes, broken code fences, copied chat/forum text, subtitle blocks, logs, mobile scrape residue, spreadsheet-like rows, and admin exports. I would still add more truly malformed machine text in a future pass if this label set needed another round.
4. Voice diversity: improved. The function section no longer speaks mostly as generated API docs. It now has confused learners, reviewers, maintainers, lab/studio operators, terse notes, and ordinary code-adjacent chatter. Most text remains neutral, which is realistic.
5. Token placement and late use: acceptable. No sample starts with the target token, no sample lacks it, and longer rows generally keep colons in the body. Harsh note: intro and time naturally put many first colons early; this is semantically appropriate but visually easy to overdo.
6. Avoid introductory phrases and curator labels: materially improved. I removed language-taxonomy starts from function samples and replaced many "this is a scrape/page" openings with actual artifact text. Some valid artifact headers remain, such as message headers and medical/form fields.
7. Length diversity: acceptable but imperfect. The prior function section was too long/clean; it is now short-heavy at 61 short samples, which better reflects incidental annotations but may be slightly overcorrected. Time has only 1 long sample after removing dense monotony; this is intentional but should be monitored.
8. Repetitive arcs/templates: the major tics are gone. Time no longer has the repeated "schedule/log then dashboard froze/repeated HH:MM" closer. Function no longer has the repeated "interface/protocol with 4-8 methods then docs clipped" skeleton. Residual repetition is more local: `const`/`let` and typed callback syntax still appear often, but not as the whole section's structure.
9. Abrupt/incomplete excerpts: yes. Many samples now start mid-column, mid-thread, mid-notebook, or with cropped context, and several end as if the scrape cut off.
10. Not only human natural language: satisfied. The file includes code, type snippets, logs, SRT/WebVTT, CSS/config/localization/header-like data, CSV-like rows, schedules, OCR forms, and generated text.
11. Tone and emotional register: acceptable. Most samples are flat or operational, with some confusion, frustration, casual notes, student questions, and review comments. It is no longer one calm explainer voice.
12. Topic/domain balance: improved. Function now covers game physics, audio DSP, shaders, hardware/firmware, parsers, bioinformatics, chemistry, finance/math, robotics, MIDI, thermal cameras, and web UI. Time covers transit, media, lab/cooking, logs, rosters, travel, sports, clinics, security, and schedules. Intro covers commerce, support, medical/admin, education, legal, HR, forms, product specs, headers, configs, and scraped pages.
13. Correctness again: final answer is yes, with the same harsh caveat: correctness is strongest where the regex scans can catch obvious contamination, but the real protection is repeated manual classification. I do not see remaining semantic cross-contamination; the remaining risks are distributional, especially intro's field-label density and function's short/typed-local skew.

## Review Pass 2026-05-05 01:42

This pass continued the 1am review rather than stopping at the clock. The user explicitly extended the floor to 01:40 and disallowed idle pauses, so I used the time for active audits and additional rewrites. The main issues addressed were: `introduces_what_follows` still had too many first colons near the front and too many vertical label-value stacks; `time_separator` was semantically strong but still front-loaded many timestamps; `function_type_annotation` still had some prose cadence and a few typed-local samples that were technically valid but not unmistakably callable/function-context.

Edits in this continuation:

- Rewrote additional `introduces_what_follows` samples to remove early first-colon placement. Final first-colon count under index 20 is 0.
- Rewrote 20+ `introduces_what_follows` vertical label blocks into inline scraped paragraphs or prose fragments. The stricter literal-`\n` vertical-stack count fell from 54 to 19, and the maximum vertical run fell from 18 to 7.
- Restored long intro coverage after the vertical-stack rewrites made the section too medium-heavy. `introduces_what_follows` now has 2 long samples again.
- Reworked 18 `time_separator` samples by adding natural no-colon lead-in context before early timestamps. Early first-colon count fell from 52 before this continuation to 34.
- Reworked function samples to reduce the repeated "code lines plus commenter/student/reviewer says/asks" cadence. Residual marker counts after the pass are much lower, and no `::` or ` : ` tokenization-risk forms remain.
- Added explicit callable/function context to typed-local samples that could have been confused with generic field labels.

Final validation snapshot:

- Timestamp: `2026-05-05T01:41:58-04:00`.
- Sample count: 300 total, exactly 100 per label.
- Samples starting with `:`: 0.
- Samples without `:`: 0.
- Exact duplicate samples: 0.
- Duplicate first-100-character starts: 0.
- Length distribution: `function_type_annotation` 5 very short, 49 short, 44 medium, 2 long; `introduces_what_follows` 1 very short, 12 short, 85 medium, 2 long; `time_separator` 3 very short, 44 short, 52 medium, 1 long.
- First-colon placement: `introduces_what_follows` early under index 20 is 0; `function_type_annotation` early is 0; `time_separator` early is 34, which is still high but appropriate for timestamp-heavy artifacts and improved from the earlier 52.
- Strict hazard scans: clean for intro/time/function sample ranges.
- Function structural risks: `::` 0, ` : ` 0, `CSV` 0, `typed as` 0, `type was` 0, `came from` 1.

Checklist answers, answered harshly:

1. Correct, unambiguous meaning: satisfied by scans and spot reads. Intro colons introduce following content, time colons separate time components, and function colons annotate types. Remaining risk is human, not obvious regex contamination.
2. Diversity and messiness: improved again. Intro now has fewer pure field stacks and more inline scraped pages, prose fragments, cached UI text, forum residue, and mixed document fragments. Time and function retained their broader source spread.
3. Dirty data: stronger. The section now has more cached-page residue, OCR-like snippets, hidden columns, screenshots, forum exports, tool output, and cropped artifacts without over-narrating every source.
4. Voice diversity: improved but not perfect. Function no longer leans as much on the same reviewer/student/commenter sentence, though code-adjacent human prose is still present.
5. Token placement: substantially improved. No samples start with `:`, intro and function have no early first-colon cases, and time is less front-loaded while staying realistic.
6. Avoid curator labels: improved. Some artifact headers remain because they are realistic, but many label-first openings were converted into mid-context fragments.
7. Length diversity: repaired after a regression. Intro briefly lost long samples during vertical-stack cleanup; two long intro samples were restored without returning to vertical templates.
8. Repetitive arcs/templates: improved. The worst function arcs and intro vertical stacks are reduced. Harsh residual: 19 intro samples still have 5+ literal-newline label rows, but that is now a minority rather than the dominant structure.
9. Abrupt/incomplete excerpts: yes. More samples now begin mid-export, mid-thread, after a missing header, or with a cropped pane.
10. Not only natural language: satisfied. There are code signatures, CSS/copy exports, headers, configs, logs, SRT/WebVTT-like cues, schedules, OCR pages, product fragments, and issue/forum text.
11. Tone/register: acceptable. Mostly neutral operational text, with some confused, terse, annoyed, bureaucratic, and casual fragments.
12. Topic/domain balance: acceptable after the function rewrite. Function now spans parser work, audio, robotics, firmware, bio/science, rendering, UI, compiler, and data tools; intro covers admin, commerce, school, legal, support, CMS, records, forms, and community artifacts; time remains broad.
13. Correctness again: I do not see semantic cross-contamination after the final checks. The remaining weakness is distributional taste, not target-label correctness: the intro section still has some label-value artifacts because that is a real colon use, but it no longer dominates the way it did.

## Review Pass 2026-05-05 02:15

This pass responded to the critique that `function_type_annotation` was still structurally monotone, too competent in voice, too dependent on cropped/missing-context frames, and sometimes not clearly function-shaped. I re-read `always_check.md`, repeatedly audited the current function section, rewrote a large batch of function samples, and then switched the final scans to label-aware parsing after noticing fixed line ranges can drift.

Edits in this continuation:

- Replaced the remaining ambiguous field-list shapes such as bare `path: string` / `mode: FileMode` with full callable signatures.
- Removed the repeated cropped/missing/hidden/screenshot/hover framing from `function_type_annotation`.
- Added and diversified beginner questions, linter/build output, generated tables, markup fragments, README snippets, full-ish source files, diffs, compiler notes, tooltips, and forum/LMS/Stack Overflow style contexts.
- Reduced generic SDK-domain residue by replacing several `UserId`/report/order/panel-style examples with more specific domains.
- Added one genuinely long function/API artifact after the rewrite made the function section too uniformly medium-length.
- Caught and corrected a temporary overcorrection in the first two `time_separator` samples; final time samples now have only digit-time colons, while intro/function have no timestamp-style leaks.

Final validation snapshot:

- Timestamp: `2026-05-05T02:15:31-04:00`.
- Sample count: 300 total, exactly 100 per label.
- Samples starting with `:`: 0.
- Samples without `:`: 0.
- Exact duplicate samples: 0.
- Length distribution: `function_type_annotation` 4 very short, 18 short, 77 medium, 1 long; `introduces_what_follows` 1 very short, 12 short, 85 medium, 2 long; `time_separator` 3 very short, 44 short, 52 medium, 1 long.
- First-colon placement: `function_type_annotation` early under index 20 is 0 and under index 45 is 25; `introduces_what_follows` early under index 20 is 0 and under index 45 is 20; `time_separator` early under index 20 is 34 and under index 45 is 84, which is expected for timestamp artifacts.
- Label-aware hazard scans: 0 hits for intro, time, and function.
- Function-specific old-tic checks: `crop`, `cropped`, `clipped`, `hidden`, `missing`, `below`, `screenshot`, `hover`, `interface`, `protocol`, `trait`, `docs page`, `string instead of number`, `UserId`, and `Panel` are all 0 in the function label.
- Ambiguous field-pair scan for function samples: 0.

Checklist answers, answered harshly:

1. Correct, unambiguous meaning: satisfied by label-aware scans and manual review. I found and fixed a late time/intro mix-up, which is exactly why the final scan is label-aware rather than line-range based.
2. Diversity and messiness: much better. Function now includes diagnostics, source files, markup, generated tables, tutorials, tooltips, review fragments, forum/LMS questions, and raw code-adjacent scraps.
3. Dirty data: improved. The section no longer feels like polished API reference only; it has CI output, copied printer/API cards, table rows, code fences, comments, markdown, and abrupt snippets.
4. Voice diversity: improved but not perfect. There are confused beginners and terse logs now, not only competent senior-developer prose. Harsh note: code-adjacent prose still appears often because type annotations are naturally code-adjacent.
5. Token placement: acceptable. No sample starts with `:`, no function sample has a first colon before index 20, and only 25 function samples have first colon before index 45.
6. Avoid curator labels: improved but not completely eliminated. I converted many starts into raw artifact text, though some artifact headers remain because they are realistic and useful.
7. Length diversity: acceptable. Function has 4 very short and 1 long sample now; time and intro keep their previous spread. Function could still use a second long natural source file in a future pass, but it no longer has the old all-medium paste feel.
8. Repetitive arcs/templates: major improvement. The old signature-block-plus-cropped-context and signature-block-plus-type-was-string arcs are gone by scan. Residual risk is local repetition from code signatures themselves, which is inherent to this label.
9. Abrupt/incomplete excerpts: yes. Samples now include mid-thread questions, partial tables, output snippets, copied cards, source excerpts, and small one-line artifacts.
10. Not only natural language: satisfied. Function samples are heavily code/tooling based; intro and time retain forms, schedules, logs, OCR-like rows, HTML, and scraped fragments.
11. Tone/register: improved. Most are flat or operational, with some confused, frustrated, tutorial, reviewer, and student voices.
12. Topic/domain balance: improved. Function now covers parsers, audio DSP, firmware, MIDI, robotics, shaders, bioinformatics, chemistry, game/quest code, thermal cameras, scheduling, auth, and UI, rather than generic SDK panels/users/orders.
13. Correctness again: final answer is yes after the label-aware hazard checks. The biggest remaining risk is not semantic contamination but future distributional taste: if iterating again, I would keep looking for repeated code-prose rhythms and add a few more raw full-file/source contexts.

## Review Pass 2026-05-05 02:29

This pass responded to the follow-up critique that `function_type_annotation` was still the weakest section: too narrow in voice, too close to competent tutorial prose, still not diverse enough in source formats, and skewed toward similar Rust/Swift/Kotlin-like function shapes. I re-read `always_check.md`, sampled the problematic function rows by issue, rewrote another large batch of samples, and reran label-aware checks after each rewrite cluster.

Edits in this continuation:

- Sampled 25 function rows for voice range and rewrote the section toward confused students, angry issue reporters, Stack Overflow/Discord/LMS posts, IDE/Pylance/mypy/pyright output, review threads, generated docs, and terse copied tool output.
- Sampled all `FAILED`/failed/test-output-like rows. The old `FAILED test name` sandwich pattern is gone; remaining matches are ordinary prose such as "failed drive test", one tiny `selection test output`, and one LMS autograder context.
- Sampled 25 function rows for format diversity and added source files with imports, TypeScript declaration snippets, PR diffs, generated API pages with nav/cookie junk, completion menus, compiler output, blog prose, Stack Overflow questions, and notebook/source fragments.
- Sampled 25 function rows for language/source-shape skew. Reduced `fn ` string hits from the earlier 58 to 23, raised TypeScript/Python/Hack/callable contexts, and removed misleading real-language labels from pseudo-code snippets.
- Cleaned up residual `Panel` as a generic-domain scan false positive in the function section. UI wording now uses view/list/menu/output where needed.
- Sampled the 6 flagged `introduces_what_follows` key-style border cases. I left them because their colons still introduce following values and that field-label shape is a realistic colon use, but I would keep watching this section in future passes so localization/config-style rows do not start to dominate again.

Final validation snapshot:

- Timestamp: `2026-05-05T02:29:14-04:00`.
- Sample count: 300 total, exactly 100 per label.
- Samples starting with `:`: 0.
- Samples without `:`: 0.
- Exact duplicate samples: 0.
- Duplicate first-100-character starts: 0.
- Function duplicate first-70-character starts: 0.
- Length distribution: `function_type_annotation` 2 very short, 25 short, 72 medium, 1 long; `introduces_what_follows` 1 very short, 12 short, 85 medium, 2 long; `time_separator` 3 very short, 44 short, 52 medium, 1 long.
- First-colon placement: `function_type_annotation` early under index 20 is 0 and under index 45 is 18; `introduces_what_follows` early under index 20 is 0 and under index 45 is 20; `time_separator` early under index 20 is 34 and under index 45 is 84.
- Label-aware hazard scans: 0 hits for intro, time, and function.
- Function repetition scans after edits: `cropped` 0, `missing` 0, `hidden` 0, `Panel` 0, `string instead of number` 0, `::` 0, ` : ` 0.
- Function format/voice marker scan: `student` 14, `beginner` 5, `angry` 4, `furious` 1, `review` 12, `output` 6, `tooltip` 3, `completion` 4, `generated` 2, `Stack Overflow` 4, `Discord` 1, `LMS` 3, `blog` 2, `source` 7, `import` 7.
- Function language/source-shape scan: `function ` 45, `fn ` 23, `fun ` 28, `func ` 15, `proc ` 2, `val ` 16, `let ` 9, `const ` 18, `Callable` 16, `TypeScript` 4, `Python` 4, `Hack` 2, `Swift` 3, `Kotlin` 2, `Rust` 8, `Nim` 8, `Elm` 0. These are rough string markers rather than a taxonomy, but they show the section no longer has the previous `fn` dominance.

Checklist answers, answered harshly:

1. Correct, unambiguous meaning: satisfied by label-aware scans and spot review. I still dislike any pseudo-language snippet with invented syntax, so I removed misleading language labels where exact syntax was questionable.
2. Diversity and messiness: substantially improved in function. There is more raw source, output, docs residue, pasted UI text, and forum junk. Harsh note: many samples are still code-adjacent because the meaning itself is code-adjacent.
3. Dirty data: improved. The new rows include generated API pages, cookie/nav residue, compiler/IDE output, code fences, diff hunks, completion menus, copied notebook cells, and abrupt forum text.
4. Voice diversity: improved. The section now has confused beginners, angry reporters, students, reviewers, terse tools, and generated docs. Harsh note: reviewer/student voices are still common enough to keep monitoring.
5. Token placement: acceptable. Function has 0 first-colon cases before index 20 and only 18 before index 45; no sample starts with the token.
6. Avoid curator labels: improved but imperfect. Some artifact-like openers remain because real scraped pages often start with a file/source/output cue. I removed the most misleading language labels rather than pretending all snippets were complete source files.
7. Length diversity: acceptable but not ideal. Function has a healthier short/medium spread and 1 long sample; I would add one more long full-source/API artifact in a future pass.
8. Repetitive arcs/templates: improved. The failed-test sandwich and cropped/missing-frame crutches are gone by scan. Residual risk is repeated "snippet plus human comment" rhythm, though it is now mixed with raw output/source/docs.
9. Abrupt/incomplete excerpts: yes. Several samples now start mid-question, mid-source, mid-output, or as copied UI/tool fragments without explanation.
10. Not only natural language: satisfied. Function is mostly code/tooling; intro and time retain forms, CSS/copy exports, schedules, OCR-ish rows, logs, and scraped fragments.
11. Tone/register: better. Most remains neutral and operational, with enough confusion, frustration, and terse automated text to break the single-competent-developer voice.
12. Topic/domain balance: improved. Function now spans checkout, audio DSP, shaders, robotics, firmware, parser/compiler work, bio/chemistry, games, auth, printers, spectrometers, thermal cameras, radio/weather, and spreadsheet merging.
13. Correctness again: final answer remains yes after the stricter scans. The remaining weakness is distributional, not semantic: future passes should keep attacking code-prose rhythm and add more complete messy source/output artifacts.

## Review Pass 2026-05-05 14:15

This pass responded to the critique that `function_type_annotation` was now technically solid but still distributionally too narrow: too many samples followed "signature block plus confused/angry human", audio/physics/game/sensor vocabulary was overrepresented, and full-file/source/docs contexts were still too rare. I sampled the function section by each issue, rewrote the sampled rows directly, then did a second harsh pass after noticing I had introduced a new `Row`/`Report`/`Policy` skew while removing the old one.

Edits in this continuation:

- Sampled 40+ rows containing confusion/complaint/tutorial-human markers such as `student`, `beginner`, `asks`, `why`, `angry`, `dictionary`, `map entry`, `not JSON`, and `not YAML`; rewrote those toward raw source, generated docs, build output, notebook cells, API cards, and clean tutorials without misunderstanding arcs.
- Sampled 25+ rows from the overrepresented audio/physics/game/sensor cluster; replaced most of that vocabulary with web apps, database clients, CLI utilities, package/build tooling, cache layers, import pipelines, test runners, auth/policy engines, queues, and generated API pages.
- Added two longer full-source/class-shaped function artifacts: a database client TypeScript source sample and a queue job runner class sample.
- Removed the old `FAILED`/test sandwich residue and reduced human-reaction framing. The function section now has zero matches for `student`, `beginner`, `asks`, `why`, `thought`, `angry`, `furious`, `complaint`, `commenter`, `reply`, `reviewer`, `grader`, `learner`, `confused`, `dictionary`, `map entry`, `not JSON`, `not YAML`, and `not a label`.
- After the first rewrite pass created a new data/report skew, sampled `Row`/`Report`/`Policy` rows and converted a smaller batch into asset export, email cleanup, catalog pages, CLI records, audit events, document rendering, support tickets, and import records.

Final validation snapshot:

- Timestamp floor satisfied: final checks continued past the 14:15 target.
- Sample count: 300 total, exactly 100 per label.
- Samples starting with `:`: 0.
- Samples without `:`: 0.
- Exact duplicate samples: 0.
- Duplicate first-100-character starts: 0.
- Length distribution: `function_type_annotation` 2 very short, 15 short, 81 medium, 2 long; `introduces_what_follows` 1 very short, 12 short, 85 medium, 2 long; `time_separator` 3 very short, 44 short, 52 medium, 1 long.
- First-colon placement: `function_type_annotation` early under index 20 is 0 and under index 45 is 13; `introduces_what_follows` early under index 20 is 0 and under index 45 is 20; `time_separator` early under index 20 is 34 and under index 45 is 84.
- Label-aware hazard scans: 0 hits for intro, time, and function.
- Old overrepresented domain markers in function after edits: `Audio` 0, `Midi` 0, `Sensor` 0, `SampleBuffer` 0, `Frequency` 0, `Decibel` 0, `GameState` 0, `physics` 0, `Ray` 0, `Thermal` 0, `Spectrometer` 0.
- New residual skew markers after cleanup: `Row` 21, `Report` 17, `Policy` 18. This is much better than the accidental peak but still worth watching.
- Source/format markers after edits: `source` 23, `generated` 7, `docs` 4, `tutorial` 4, `import` 14, `class` 2.

Checklist answers, answered harshly:

1. Correct, unambiguous meaning: satisfied by label-aware scans. I also removed one borderline build-output line where `expected message: QueueMessage` could have looked like a field label rather than a quoted annotation.
2. Diversity and messiness: improved. Function now has more raw source, generated docs, build output, code fences, API cards, notebook cells, PR hunks, and full-class source.
3. Dirty data: improved. There is still not enough truly ugly CI/stack-trace material, but the polished tutorial voice no longer dominates.
4. Voice diversity: deliberately reduced human-reaction voice because it was overrepresented. The section now leans more toward artifacts than people explaining or complaining.
5. Token placement: strong. Function has no first colon before index 20 and only 13 before index 45.
6. Avoid curator labels: mixed. Some source/artifact labels remain, but many are realistic file or generated-page openings. The samples no longer read like every one was introduced by a curator.
7. Length diversity: improved from the previous pass. Function now has 2 long samples and a reasonable short/medium spread, though still no extra-long artifacts.
8. Repetitive arcs/templates: much improved. The "confused about the colon" arc is no longer structurally dominant; targeted markers are at zero.
9. Abrupt/incomplete excerpts: yes. There are generated docs, source snippets, output fragments, tables, and code fences that start without explanation.
10. Not only natural language: satisfied. Function is now mostly code/tooling artifacts rather than natural-language explanation.
11. Tone/register: flatter and more realistic for code corpora. The loss of emotional voice is intentional here because the previous version overused confusion and complaint.
12. Topic/domain balance: improved but still imperfect. Old audio/physics/game/sensor overrepresentation is removed; new mild skew toward data/import/report/policy remains and should be monitored next.
13. Correctness again: clean by scans and spot checks. The remaining concern is distributional taste, not semantic contamination.

## Review Pass 2026-05-05 14:27

This pass responded to the critique that all three labels still had too much "contextual intro, then actual text" structure. I re-read `dsv2/samples_-.yaml` for the stronger pattern: many samples simply start as the artifact itself, with OCR rows, logs, formulas, snippets, comments, ads, and footer junk already mixed in, rather than announcing the artifact first. I then sampled roughly 20+ rows per meaning label and removed or rewrote descriptor openings.

Edits in this continuation:

- `introduces_what_follows`: rewrote 20+ samples so they start with actual forum text, CSS, email headers, form fields, wiki fields, chat lines, listing fields, release rows, worksheet rows, or support fields instead of "scan/export/paste" narration.
- `time_separator`: rewrote 25+ samples so schedule/log/timestamp artifacts start directly with cue numbers, timestamp rows, bib splits, roster rows, route rows, call rows, or ISO timestamps. Restored one long direct schedule artifact after the descriptor removals shortened the section.
- `function_type_annotation`: rewrote 30+ samples so they start with imports, direct signatures, diff hunks, callable assignments, generated declarations, or package/source code rather than file/source descriptors. Added a few real code/import lines to avoid making every first colon occur immediately after removing the preface.
- Compared against the `samples_-` style explicitly: the target was less narration about a source and more raw artifact texture.

Final validation snapshot:

- Timestamp: `2026-05-05T14:27:13-04:00`.
- Sample count: 300 total, exactly 100 per label.
- Samples starting with `:`: 0.
- Samples without `:`: 0.
- Exact duplicate samples: 0.
- Duplicate first-100-character starts: 0.
- Label-aware hazard scans: 0 hits for intro, time, and function.
- Descriptor-newline candidates after cleanup: `introduces_what_follows` 0, `time_separator` 0, `function_type_annotation` 5. The remaining function cases are source/import/package lines (`from customer_import...`, `import { Cursor }...`, `package web.forms`) rather than narrator-style descriptions.
- Length distribution: `function_type_annotation` 2 very short, 18 short, 78 medium, 2 long; `introduces_what_follows` 1 very short, 16 short, 82 medium, 1 long; `time_separator` 4 very short, 45 short, 50 medium, 1 long.
- First-colon placement: `function_type_annotation` early under index 20 is 12 and under index 45 is 33; `introduces_what_follows` early under index 20 is 17 and under index 45 is 36; `time_separator` early under index 20 is 64 and under index 45 is 95. This increased because many samples now begin directly with real fields/timestamps/code rather than a preface.

Checklist answers, answered harshly:

1. Correct, unambiguous meaning: satisfied by label-aware scans after every edit batch.
2. Diversity and messiness: improved. The rows now more often look like raw artifacts rather than a generated description of artifacts.
3. Dirty data: improved in all labels; there are more direct headers, source lines, CSS, route rows, timestamp rows, diff hunks, and field blocks.
4. Voice diversity: less narrator voice, which was the main issue. Some human text remains where it is the artifact itself.
5. Token placement: mixed. Removing intros necessarily moved many first colons earlier, especially time and intro. This is acceptable for raw timestamp and field artifacts but should be watched if it starts to feel front-loaded again.
6. Avoid curator labels: major improvement. The explicit descriptor-newline formula is now nearly gone.
7. Length diversity: acceptable but slightly weaker for intro than before; intro has only 1 long sample now. Time regained 1 long sample.
8. Repetitive arcs/templates: improved. The "descriptor line, newline, actual content" template was cut by well over half and eliminated entirely in intro/time by the heuristic scan.
9. Abrupt/incomplete excerpts: improved. More samples now begin in the middle of rows or code, as scraped text often does.
10. Not only natural language: satisfied. This pass increased raw CSS/code/log/schedule/table presence.
11. Tone/register: flatter and more artifact-like, which is better for this specific complaint.
12. Topic/domain balance: improved modestly by touching all three labels, though function still has some data/admin/code-tooling skew from previous passes.
13. Correctness again: clean by scans. The remaining residual is distributional: a few function samples still start with source-file/package/import lines, but those are real artifact text rather than contextual narration.

## Review Pass 2026-05-05 14:54

This pass responded to the critique that the file still had major distribution problems after the prior cleanup: `time_separator` was still too schedule/table/log dense, `function_type_annotation` still looked too much like stacked signatures, `introduces_what_follows` still leaned too hard on field inventories, and all sections needed more messy, broken, informal, and incidental real-world texture. I re-read `always_check.md`, sampled across each meaning label, and made another broad rewrite rather than optimizing only the weakest label.

Edits in this continuation:

- `time_separator`: sampled 35+ dense schedule/log/table/timing rows and replaced many with short incidental fragments: annoyed texts, appointment scraps, recipe/cooking notes, wet timetable scraps, news/event prose, phone screenshots, clinic reminders, and casual comments with only 1-3 time colons. Kept a minority of dense subtitles, EDLs, logs, and schedules so the label still covers naturally high-density time artifacts.
- `function_type_annotation`: sampled 30+ repetitive signature-stack rows and rewrote them into fuller source/test/diagnostic contexts: imports, structs/classes with fields, TypeScript tests, PR diffs, compiler/IDE panels, GraphQL-like mutation signatures, callable locals, Rust/Kotlin/Swift/Hack/Nim style bodies, and confused/frustrated code-adjacent discussion. Added no-colon source context to reduce early-colon front-loading without restoring curator-style introductions.
- `introduces_what_follows`: sampled 25+ field-label/inventory rows and rewrote many into explanatory prose, titles/subtitles, quoted speech, inline lists, broken HTML/CSS, forum quote rows, changelog lines, newsletter fragments, and OCR-ish artifacts. Stripped several descriptor openers so samples start as the artifact itself.
- Cross-section messiness: added or preserved ad overlays, broken hero images, sticky template residue, cache/sidebar/footer junk, all-caps replies, smudged paper, misread rows, and abrupt partial fragments.
- Voice: added more informal and irritated human voice, especially in `time_separator` and `introduces_what_follows`, while keeping function from reverting to the old all-confused-beginner pattern.

Final validation snapshot:

- Timestamp: `2026-05-05T14:54:09-04:00`.
- Sample count: 300 total, exactly 100 per label.
- Samples starting with `:`: 0.
- Samples without `:`: 0.
- Exact duplicate samples: 0.
- Duplicate first-100-character starts: 0.
- Label-aware hazard scans: 0 hits for `introduces_what_follows`, `time_separator`, and `function_type_annotation`.
- Length distribution: `function_type_annotation` 1 very short, 17 short, 80 medium, 2 long; `introduces_what_follows` 1 very short, 39 short, 59 medium, 1 long; `time_separator` 28 very short, 53 short, 18 medium, 1 long.
- First-colon placement: `function_type_annotation` early under index 20 is 1 and under index 45 is 28; `introduces_what_follows` early under index 20 is 22 and under index 45 is 30; `time_separator` early under index 20 is 42 and under index 45 is 89.
- Colon density: `time_separator` now has 40 samples with 3 or fewer colons and 35 samples with 10 or more colons, which is a much healthier mix than the previous wall-of-tables shape. `introduces_what_follows` has 59 samples with 3 or fewer colons. `function_type_annotation` remains naturally code-dense, with 11 samples at 3 or fewer colons and 16 at 10 or more.
- Function repetition markers after edits: `physics` 0, `audio` 0, `game` 0, `sensor` 0, `Row` 16, `Report` 13, `Policy` 17, `function ` 30, `fn ` 11, `fun ` 11, `func ` 5, `Callable` 9, `IDE` 9. These are rough markers, but the section is no longer dominated by one language family or one subject domain.

Checklist answers, answered harshly:

1. Correct, unambiguous meaning: yes by label-aware scans and spot review. I still had to watch every single colon because CSS, timestamps, diffs, and code diagnostics invite accidental cross-label contamination.
2. Diversity and messiness: much improved. Time now has actual incidental prose; intro now has more explanatory and quoted-speech colons; function has more full source/test/diagnostic contexts. Harsh note: function still visually reads as code-heavy because the meaning demands code.
3. Dirty data: improved across all labels. The file now includes ad overlays, broken HTML, CSS remnants, footer/cache residue, wet paper, clipped screenshots, sticky notes, raw code, diffs, generated docs, and tool output.
4. Voice diversity: improved. Time includes annoyed, casual, funny, and messy human voice; intro includes all-caps frustration and bureaucratic/flat/system voices; function has a little confusion/frustration without making that the dominant narrative.
5. Token placement: better for function after smoothing. Function early-under-20 is down to 1 and early-under-45 is 28. Time is still early because real time fragments often begin with the time itself; this is acceptable but remains a known distributional pressure.
6. Avoid contextual intros: improved but not perfect. I removed many obvious descriptor-newline wrappers. Some file/package/import/module lines remain because they are artifact text, not curator captions. Harsh note: function still has a few prose-y artifact openers like hover/paste/panel fragments.
7. Length diversity: improved for time and intro in the direction requested. Time now has many very short/short incidental samples. Harsh note: only 4 total long samples remain across the file, so future passes could add one long messy intro artifact and one long source file if length breadth becomes the next priority.
8. Repetitive arcs/templates: substantially improved. Time is no longer mostly table/log walls. Function is less "stack of 4 signatures plus note" and has more classes, variables, tests, diffs, and diagnostics. Intro is less pure label inventory, though field-label artifacts still form an expected chunk.
9. Abrupt/incomplete excerpts: yes. Many samples now begin mid-artifact or mid-thread, and some end as clipped rows, footer residue, or incomplete pasted source.
10. Not only natural language: satisfied. The file includes code, CSS, HTML, forms, changelogs, subtitles, logs, schedules, config-like text, raw docs fragments, and tool output.
11. Tone/register: better balanced. Most text remains neutral or operational, but there are now casual texts, annoyed support snippets, all-caps user replies, wry notes, and sterile machine-ish outputs.
12. Topic/domain balance: improved. Function no longer overweights audio/physics/game/sensor domains. Time spans travel, appointments, recipes, transit, media, clinics, backups, races, kitchens, and logs. Intro spans support, education, commerce, legal, civic, medical, product, archive, and newsletter material.
13. Number skipped in `always_check.md`: no separate question.
14. Avoid intro->linebreak->actual-text templates: much improved. I explicitly stripped descriptor rows in intro, time, and function. Residual examples are mostly realistic imports, package lines, code fences, or artifact headings rather than narrator captions.
15. Correctness again: clean by final hazard scans. The remaining risk is taste/distributional, not semantic: future passes should keep watching function descriptor residue and intro field-label dominance, but this pass fixed the most serious structural monotony called out in the critique.

## Review Pass 2026-05-05 15:45

This pass responded to the most important semantic critique: the first label was too broad and was incorrectly allowing key-value, speaker-label, header, CSS/property, and explanatory-only colon uses. I changed the active first label to `introduces_a_list`, rebuilt the section around list-introducing colons only, and kept the old `introduces_what_follows` material only as a superseded historical note in this plan.

Edits in this continuation:

- `introduces_a_list`: renamed the YAML label, reworked the definition and exclusions, sampled the section for singleton/non-list colon fragments, and fixed the one bad list sample where `attempted fixes so far: all of them` was not actually a list. I also trimmed several descriptor-style openers so more rows begin as the list artifact itself.
- `time_separator`: kept the improved incidental-time distribution and replaced one duplicate dense EDL-style wall with a shorter prose export note. Dense logs/subtitles/schedules remain, but they are no longer the whole section.
- `function_type_annotation`: sampled the remaining human-wrapper and answer/reply/beginner/paste pattern, then rewrote another batch into raw imports, declarations, locals, generated signatures, callable assignments, and code-like fragments. After that, I corrected the overcorrection where raw function rows had pulled too many first colons near the front by adding real import/package/module context instead of narrator captions.
- Cross-label semantic checks were rerun after the edits. The one detected function hazard was `::runCommand`, which I replaced because `::` is not the single-colon type-annotation use needed here.

Final validation snapshot:

- Timestamp: `2026-05-05 15:45:21 America/New_York`.
- Sample count: 300 total, exactly 100 per label.
- Samples starting with `:`: 0.
- Samples without `:`: 0.
- Exact duplicate samples: 0.
- Duplicate first-100-character starts: 0.
- Label-aware hazard scans: 0 hits for `introduces_a_list`, `time_separator`, and `function_type_annotation`.
- `introduces_a_list` singleton-list check: 0 suspicious colon fragments.
- Length distribution: `function_type_annotation` 0 very short, 21 short, 77 medium, 2 long; `introduces_a_list` 18 very short, 51 short, 30 medium, 1 long; `time_separator` 28 very short, 54 short, 17 medium, 1 long.
- First-colon placement: `function_type_annotation` early under index 20 is 0 and under index 45 is 31; `introduces_a_list` early under index 20 is 4 and under index 45 is 36; `time_separator` early under index 20 is 41 and under index 45 is 88.
- Colon density: `function_type_annotation` has 6 samples with 3 or fewer colons and 15 with 10 or more; `introduces_a_list` has 96 with 3 or fewer and 0 with 10 or more; `time_separator` has 40 with 3 or fewer and 34 with 10 or more.
- Literal escaped newline samples: `introduces_a_list` 29, `time_separator` 42, `function_type_annotation` 96. The high function value is mostly real multiline code/source structure, not descriptor-newline wrappers.

Checklist answers, answered harshly:

1. Correct, unambiguous meaning: much stronger now. The active first label is no longer broad `introduces_what_follows`; every colon in `introduces_a_list` should introduce a multi-item list. The final list singleton scan and hazard scan are clean.
2. Diversity and messiness: improved but not perfect. Time and list now have strong short/incidental coverage, and function has more raw source and declarations. Harsh note: `function_type_annotation` still looks code-dense, because this meaning is code-dense, and future passes could add more complete source-file contexts.
3. Dirty data: adequate. There are OCR/PDF fragments, broken HTML, ad/footer/sidebar residue, raw code, diffs, generated docs, schedule rows, subtitles, and casual text. Harsh note: function still has less ugly CI/stack-trace texture than ideal.
3. Voice diversity: better across time and list, intentionally flatter in function after the confusion/complaint arc became overused. Harsh note: list still has a lot of neutral "artifact says/includes/asks" phrasing.
4. Token placement: acceptable after the final function repair. Function has 0 first colons before index 20. Time remains early-heavy, but timestamps often naturally begin early. List has only 4 before index 20.
5. Avoid introductory phrases: improved. I removed more descriptor openers, especially in function and the list label. Harsh note: some artifact-heading starts remain, but they are usually the text itself rather than a curator label.
6. Length diversity: adequate, not luxurious. The file has many short and medium samples and 4 long samples total. Harsh note: one or two more long messy artifacts would still help.
7. Avoid starting with the token: satisfied. No sample starts with `:`.
8. Repetitive arcs/templates: much improved. The old "schedule/log wall", "signature block plus explanation", and broad intro-colon memo arcs are no longer dominant. Harsh note: repeated code-signature rhythm remains the main residual risk for function.
9. Abrupt/incomplete excerpts: satisfied. Many rows start or end mid-artifact, with clipped schedules, partial HTML, copied code, OCR fragments, and footer/sidebar residue.
10. Not only natural language: satisfied. The file includes code, type declarations, diffs, subtitles, logs, schedules, HTML, docs fragments, forms, lists, and prose.
11. Tone/register: acceptable. Most text is neutral, as it should be, with some casual, frustrated, messy, and bureaucratic voices. Harsh note: the list section could still use a few more truly odd or badly written human fragments.
12. Topic/domain balance: acceptable after the function cleanup. Function no longer overweights audio/physics/game/sensor domains; time and list span transit, media, household, education, research, commerce, health/admin, software, and community material.
13. Number skipped in `always_check.md`: there is no separate question 13 in the source checklist.
14. Avoid intro-descriptor and intro-linebreak templates: improved substantially. Function still has many literal newlines because source code naturally has them, but the descriptor-newline wrapper pattern was specifically reduced.
15. Correctness again: clean by final scans. The remaining concerns are distributional taste, not known semantic contamination: add more long messy artifacts later, keep watching list rows for drift back toward key-value singletons, and keep function from re-growing the "confused user explains colon" arc.

## Review Pass 2026-05-05 15:51

This pass responded to the stricter left-context constraint: when the colon appears, the preceding text should already make the colon's role semantically likely. I audited first-colon left contexts across labels and edited the weak cases rather than relying on the right side to disambiguate.

Edits in this continuation:

- `time_separator`: revised bare or weak timestamp starts such as `09:14`, SRT cue-number starts, alarm grids, radio grids, podcast chapters, bus inserts, race splits, and shift rows so the text before the first colon already cues time, timestamp, schedule, caption, flight, radio, calendar, or split semantics. Examples of added left context include `train text log`, `subtitle cue`, `phone alarm list`, `bread timer photo`, `TV grid`, `podcast chapters`, `flight card`, `official race time`, `feed chapters`, and `scene timing`.
- `introduces_a_list`: changed `bowl first:` to `dry ingredients first:` so the list semantics are already present before the colon.
- Rechecked `function_type_annotation`; its early first-colon cases already have code/type context before the colon, such as `function parseHeader(raw`, `val loader`, `type FoldStep = (event`, `from typing import Callable`, or `export declare function ...`.

Validation after this pass:

- Sample count: 300 total, exactly 100 per label.
- Samples starting with `:`: 0.
- Samples without `:`: 0.
- Exact duplicate samples: 0.
- Duplicate first-100-character starts: 0.
- Label-aware hazard scans: 0 hits for all three labels.
- Length distribution: `function_type_annotation` 0 very short, 21 short, 77 medium, 2 long; `introduces_a_list` 18 very short, 51 short, 30 medium, 1 long; `time_separator` 25 very short, 57 short, 17 medium, 1 long.
- First-colon placement after adding left context: `function_type_annotation` early under index 20 is 0; `introduces_a_list` early under index 20 is 3; `time_separator` early under index 20 is 21, down from 41 before the left-context-focused edits. The remaining early time cases have explicit left cues such as train/calendar/app/cam/flight/TV/grid/WEBVTT/train/stop/feed.

## Review Pass 2026-05-05 15:59

This pass tightened the left-context rule again after the user pointed out that even rows like `train text log 09:14` were still too weak. I treated every first time separator as needing an explicit time cue before the colon, not merely a plausible artifact noun.

Edits in this continuation:

- Reworked many `time_separator` openers so the pre-colon context contains clear words such as `time`, `timestamp`, `showtimes`, `depart time`, `timecode`, `timer`, `hours`, `split time`, `duration`, `schedule`, `timetable`, `ISO timestamp log`, or `times`.
- Examples: `train text log 09:14` became `train departure text log time 09:14`; `poster fragment ... matinee 14:30` became `cached showtimes page ... matinee time 14:30`; bare caption/SRT cues now say `timestamp` before the timestamp line; flight, call, race, bus, radio, feed, and clinic rows now state that the following numbers are times before the first colon.
- Left `livestream froze at 00:18`-style rows mostly intact where the pre-colon phrase already clearly establishes a time/event timestamp.

Validation after this pass:

- Sample count: 300 total, exactly 100 per label.
- Samples starting with `:`: 0.
- Samples without `:`: 0.
- Exact duplicate samples: 0.
- Duplicate first-100-character starts: 0.
- Label-aware hazard scans: 0 hits for all three labels.
- Length distribution: `function_type_annotation` 0 very short, 21 short, 77 medium, 2 long; `introduces_a_list` 18 very short, 51 short, 30 medium, 1 long; `time_separator` 17 very short, 62 short, 20 medium, 1 long.
- `time_separator` first-colon placement improved to only 1 sample under index 20, and that sample has `times` before the timestamp. Average first-colon position for `time_separator` rose to 35.4.

## Review Pass 2026-05-05 16:07

This pass corrected the overcorrection from 15:59. I had made the `time_separator` label too verbally explicit by inserting standalone `time`, `times`, and `timestamp` everywhere. That made the meaning clear, but in a fake, repetitive way.

Edits in this continuation:

- Removed the repeated literal scaffold from the affected `time_separator` rows: `start time`, `timestamp log`, `at time`, `finish time`, `grid time`, `depart time`, `opened time`, `burp times`, `caption block timestamp`, and similar phrases.
- Replaced those with natural artifact cues that still establish temporal meaning before the colon: `radio log ... starts`, `backup ISO log`, `subtitle cue`, `TV schedule grid`, `appointment board`, `flight card ... depart`, `WEBVTT cue track`, `train schedule`, `festival schedule ... opens`, `call log ... answered`, `race splits`, `late-night radio continuity`, and so on.
- Checked the early first-colon cases after the edit. The remaining under-index-20 rows are semantically clear before the colon because the left context includes calendar, meet-at text, alarm list, TV schedule, backup began, train schedule, bus insert, or feed chapters.

Validation after this pass:

- Standalone `time`, `times`, and `timestamp` in `time_separator`: 0. Natural related forms remain where appropriate, such as `timecode`, `showtimes`, and `timing`.
- Sample count: 300 total, exactly 100 per label.
- Samples starting with `:`: 0.
- Samples without `:`: 0.
- Exact duplicate samples: 0.
- Duplicate first-100-character starts: 0.
- Label-aware hazard scans: 0 hits for all three labels.
- Length distribution: `function_type_annotation` 0 very short, 21 short, 77 medium, 2 long; `introduces_a_list` 18 very short, 51 short, 30 medium, 1 long; `time_separator` 24 very short, 55 short, 20 medium, 1 long.
- `time_separator` first-colon placement is now 8 samples under index 20 and 86 under index 45. This is a distributional tradeoff I accept because the short, natural time mentions should exist; the early cases are still clear before the colon.

## Review Pass 2026-05-05 18:41

This pass addressed a broader distribution critique: the file had developed a recognizable authorial habit where list samples stacked multiple list sources, time samples often had a "something is covered or wrong" beat, and function/type samples still looked too much like bare declaration blocks.

Edits in this continuation:

- `introduces_a_list`: reworked well over 20 rows. The main change was removing the recurring "first list, second source adds another list, third source repeats/extends it" pattern. Many rows now contain one colon-introduced list followed by ordinary passage context. I also added/kept technical list contexts such as API docs and README setup requirements.
- `time_separator`: reworked 20+ rows that had the repeated damage/problem ending. Replaced subtitle/caption-heavy or broken-artifact rows with intact emails, clinic reminders, news prose, bus schedules, race rows, radio schedules, restore windows, flight cards, and recipe/blog timing. Some messy artifacts remain, but the section is no longer dominated by "ad covered/smudged/hidden/wrong" endings.
- `function_type_annotation`: reworked 30+ rows toward tutorials, Stack Overflow answers, compiler/mypy output, IDE hovers, PR review comments, API docs prose, test output, and inline annotated locals. Raw code remains represented, but it is no longer the only voice.
- After shortening too many list rows while removing stacked lists, I added longer single-list passages back in so list length did not collapse into only one-liners.

Validation after this pass:

- Timestamp: `2026-05-05 18:40:59 -04:00`.
- Sample count: 300 total, exactly 100 per label.
- Samples starting with `:`: 0.
- Samples without `:`: 0.
- Exact duplicate samples: 0.
- Duplicate first-100-character starts: 0.
- Label-aware hazard scans: 0 hits for all three labels.
- Length distribution: `function_type_annotation` 0 very short, 53 short, 45 medium, 2 long; `introduces_a_list` 5 very short, 80 short, 15 medium, 0 long; `time_separator` 37 very short, 49 short, 13 medium, 1 long.
- First-colon placement: `function_type_annotation` early under index 20 is 0 and under index 45 is 36; `introduces_a_list` early under index 20 is 3 and under index 45 is 36; `time_separator` early under index 20 is 8 and under index 45 is 84.
- Colon density: `introduces_a_list` now averages 1.1 colons per sample, which is intentional for the renamed list meaning and directly reduces the old stacking template. `time_separator` remains denser at 7.9 because schedules/logs are legitimate for this meaning. `function_type_annotation` averages 6.1 after replacing many declaration blocks with prose contexts.

Harsh residual notes:

- `introduces_a_list` is cleaner but now has fewer long samples than earlier; future passes could add a few long, messy, single-list passages without reintroducing multi-list stacking.
- `time_separator` still has some dense structured rows, because those are realistic for time separators; the important improvement is that many rows are now plain intact schedules/prose rather than broken-artifact drama.
- `function_type_annotation` still retains raw code blocks, but the surrounding-context distribution is much better after adding hovers, errors, review prose, tutorials, and forum-style explanation.

## Repeated Lessons To Preserve

Timestamp: `2026-05-05 18:52:56 -04:00`.

These are the main failure modes I had to fix repeatedly while building `dsv2/samples_colon.yaml`; future colon passes should check these directly, not wait for a review to catch them.

1. Broad explanatory-colon labels drift into other meanings. The original `introduces_what_follows` target was too broad and repeatedly admitted key-value, speaker-label, CSS/property, header-field, and generic elaboration colons. Renaming it to `introduces_a_list` helped, but only if every colon in that section clearly introduces multiple items, examples, steps, options, or requirements.
2. For `introduces_a_list`, the dominant bad template was "list one, then another source adds list two, then a footer/sidebar/comment adds list three." This made the section look artificial even when every colon was semantically correct. Prefer one colon-list embedded in normal surrounding text.
3. Removing stacked lists can overcorrect into very short samples. When trimming a multi-list row, extend the passage with ordinary non-list context rather than adding another colon-list. The target colon should feel incidental inside a real excerpt, not like the whole sample was built to demonstrate it.
4. For `time_separator`, semantic clarity before the colon matters, but literal words like `time`, `times`, and `timestamp` should not be sprayed everywhere. Better left-context cues are natural artifact words: `calendar`, `alarm`, `schedule`, `depart`, `arrival`, `duration`, `cue`, `showtimes`, `timecode`, `timer`, `race splits`, `call log`, `flight card`, `doors`, `opens`.
5. The opposite overcorrection is also possible: bare rows like `09:14 leaving now` or weak cues like `train text log 09:14` can be too ambiguous at the first colon. The phrase before the colon should already make the temporal interpretation likely.
6. The main `time_separator` template trap was "times plus a problem": ad covered it, paper smudged, dashboard froze, printer cut off, wrong row, hidden column, drift, missing cue. Some messy artifacts are realistic, but most time-containing data should be intact and mundane.
7. Subtitle/SRT/WebVTT blocks are useful but can quickly dominate because they are naturally colon-dense. Keep them as a minority and balance with emails, calendar invites, news prose, recipes, chat messages, appointment reminders, schedules, transit notices, sports/race timing, and ordinary sentences with one or two times.
8. For `function_type_annotation`, correctness is not enough. The repeated bad shape was a clean block of 3-6 annotated signatures or declarations. That is valid code but visually monotonous across 100 samples.
9. Function/type annotations need surrounding contexts: tutorials explaining syntax, Stack Overflow/forum questions, compiler/mypy/tsc output, IDE hover text, PR review comments, generated API docs, diffs, test failures, full-ish source files, and mid-function annotations buried among ordinary logic.
10. Confused-user voice can itself become a template. Earlier passes overused "beginner thinks the colon is a dict/key-value" and "reviewer asks why type changed." Keep those voices, but do not let them replace the old clean-docs monotony with a new confusion monotony.
11. Cross-label ambiguity is real. Strings like `cutoff: int = 24` can look like either a list/field label or a type annotation unless code context is already established before the colon. Avoid isolated ambiguous fragments.
12. Automated scans are necessary but insufficient. The label-aware hazard scan catches obvious wrong colons, duplicates, and token-position problems, but it does not catch authorial tics like list stacking, problem endings, or clean signature-block monotony. Always do a manual distribution read after scans pass.
13. Regex pattern counters are useful as smoke tests, not final judgments. Words like `footer`, `still`, `old`, or `covered` can be legitimate; use the counters to find clusters, then read samples rather than blindly deleting every hit.
14. Length distribution should be watched after every semantic cleanup. Fixing structure often changes length distribution unintentionally, especially when replacing dense stacked artifacts with single-list/prose samples.
15. The best final state is not maximally messy. C4/SFT-style text includes OCR junk, broken HTML, comments, and logs, but much web text is intact and boring. Preserve mundane samples deliberately.
