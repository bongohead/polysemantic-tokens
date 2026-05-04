# Plan: Polytok Token `" {"`

## Objective

Create `dsv2/samples_{.yaml` with 100 realistic samples for each meaning label:

- `set_notation`
- `programming_block_delimiter`
- `placeholder_token`

Every sample must contain the exact token `" {"` at least once. Every occurrence of `" {"` inside a sample must match that sample's `meaning_label`.

The old `ds/samples_{.yaml` has the right broad labels, with 42 `set_notation`, 40 `programming_block_delimiter`, and 41 `placeholder_token` samples. Its main problem is not label choice; it is that many samples sound like polished explanations of the token instead of raw C4/HPLT-style text. The v2 set should be rougher, more varied, less instructional, and more careful about not mixing curly-brace meanings.

## Realism Standard

Samples should feel like a mixed web-corpus slice, not like examples written for a dataset curator. Use raw excerpts when possible: math notes, proof fragments, worksheets, source files, code diffs, CSS and config blocks, stack traces, template emails, localization files, CMS exports, chat logs, forum posts, support macros, OCR text, copied tables, API docs, and half-broken scraped pages.

Good data can be clipped, mundane, oddly formatted, redundant, or surrounded by adjacent junk: footer text, cookie banners, page navigation, compiler warnings, copied comments, stale snippets, broken Markdown, duplicated headers, mobile scrape artifacts, and table rows merged into prose.

Avoid unnecessary wrappers such as `Here is a snippet`, `This example shows`, `In this dataset`, `A textbook says`, or `The page source contains`. A few natural labels are fine when they belong to the artifact, such as `invoice_template.html`, `err.log`, `worksheet 6`, or `strings.en.json`, but most samples should begin with the actual text, formula, code, or template.

## Exact-Token Hazard

The target token is a space followed by an opening curly brace: `" {"`. Other opening braces without a preceding space are not the exact token, but they can still confuse the sample visually. When possible, keep all visible brace use aligned with the target label, especially in short samples.

For tokenizer coverage, deliberately mix both after-brace spacing patterns in every meaning label:

- Space after the brace: `" { "`, as in `A = { 1, 2 }`, `if (ready) { run(); }`, or `Dear { first_name }`.
- No space after the brace: `" {a"`/`" {N"`/`" {0"`-style continuations, as in `A = {a,b}`, `function f() {return x;}`, or `Hello {Name}`.

Both forms are valid and useful. Do not let one spacing style dominate a label, especially `placeholder_token`, where no-space placeholders are common, or `set_notation`, where spaced set literals are common.

For this token, ambiguity is the biggest risk:

- `A = { 1, 2 }` is set notation.
- `if (ready) { run(); }` is a programming block delimiter.
- `Hello {first_name}` is a placeholder token.
- `const data = { id: 1 }` is an object literal, not a programming block delimiter.
- `\frac {a}{b}` is TeX grouping, not set notation.
- `grep {1..3}` or `file_{old,new}` is shell/filename brace expansion, not any of the three labels.

During sample writing, scan every `" {"` occurrence and ask what the opening brace is doing syntactically. If any occurrence has another meaning, rewrite or remove it.

## Distribution Guidance

Use approximate distributions, not exact quotas.

- Length: include a few tiny fragments, many short and medium samples, and a meaningful minority of long or extra-long messy samples.
- Token density: set notation and placeholders can naturally repeat; programming blocks often repeat in code. Longer samples should usually include `" {"` later in the text too, not only near the beginning.
- After-brace spacing: each label should include a noticeable mix of `" { "` and `" {x"`/`" {X"`/`" {0"` patterns, without forcing unnatural formatting.
- Source mix: each label needs raw, semi-structured, and messy material, not only explanatory prose.
- Voice and tone: vary between neutral machine output, terse notes, confused people, formal docs, student work, vendor templates, support replies, compiler output, and scraped web residue.
- Completeness: not every sample should be a complete thought. Some can start or end abruptly as if scraped from the middle of a page.
- Openings: avoid starting any sample with the target token. Also avoid starting with a bare `{` unless it is clearly a real artifact and the exact token still appears later.
- Formatting: multiline samples are useful for this token, especially code and templates, but keep YAML valid.

## `set_notation`

Semantic rule: `" {"` opens mathematical set notation: finite set literals, set-builder notation, families/classes of sets, sample spaces, events, domains, alphabets, equivalence classes, solution sets, or similar set-denoting mathematical collections.

Good examples:

- `A = { 1, 3, 5 }`
- `S = { x : x > 0 }`
- `Omega = { HH, HT, TH, TT }`
- `F = { A subset X : A is finite }`
- `Sol(P) = { (x,y) : Ax = b }`
- `P(X) = { empty, {1}, {2}, {1,2} }`

Include:

- Raw math notes, proofs, set-builder definitions, topology, algebra, probability, logic, automata, graph theory, combinatorics, measure theory, and statistics.
- Worksheets, quizzes, answer keys, student scratchwork, lecture slides, theorem statements, dense research fragments, peer review notes, and LaTeX-ish text where the exact `" {"` occurrences are still set notation.
- Tables and structured rows listing domains, events, alphabets, states, constraints, solution sets, allowed values, or finite groups.
- Computational or documentation fragments where the braces are explicitly being used as sets, such as a Python set-operations tutorial. Use these sparingly, and avoid any mixed dict/object literal code.
- Messy/OCR math excerpts with page headers, broken captions, or adjacent navigation, as long as the brace meaning remains clear.

Exclude:

- Programming block delimiters: `if (x) {`, `class C {`, `.card {`.
- Object, dict, JSON, map, struct, or initializer literals: `const x = { id: 1 }`, `Point p = {0, 1}`.
- Placeholders and templates: `Hello {Name}`, `{API_KEY}`, `{{ user }}`.
- TeX command grouping or formatting arguments: `\frac {a}{b}`, `\textbf {word}`, `\section {Intro}`.
- Shell brace expansion, regex quantifiers, file globbing, or command syntax: `file_{old,new}`, `grep 'a\{2\}'`, `{1..5}`.
- Empty code blocks or CSS declarations, even if they look like `{ }`.

Guidance:

- This label should lean mathematical and technical, but not all samples should be polished textbook prose.
- Use a wide range of domains: finite sets, infinite sets, events, languages, automata states, graph neighborhoods, sigma-algebras, bases, ideals, varieties, equivalence classes, intervals expressed as sets, and solution spaces.
- Include mundane educational artifacts too: worksheet scans, LMS quiz exports, answer keys, tutoring notes, and student mistakes.
- Avoid overusing `Let A = ...` as the opening. Start some samples from table rows, proof middles, captions, or handwritten-note transcriptions.
- In nested-set samples, be extra careful that each exact `" {"` occurrence opens a set, not a template or code block.

## `programming_block_delimiter`

Semantic rule: `" {"` opens a code/config block, scope, rule body, function body, class body, branch body, loop body, closure body, handler body, or selector/configuration block.

Good examples:

- `if (ready) { start(); }`
- `function render() { return view; }`
- `class Parser {`
- `try { risky(); } catch (e) { recover(); }`
- `.notice { color: red; }`
- `server { listen 80; }`

Include:

- Raw source code in C, C++, Java, JavaScript, TypeScript, C#, Go, Rust, Kotlin, Swift, PHP, Perl, awk, and similar brace-delimited languages.
- CSS, SCSS, Sass-like blocks, media queries, keyframes, and HTML pages with embedded style/script blocks.
- Config formats that use braces as block delimiters, such as Nginx, Terraform/HCL, Gradle, Bison/Yacc fragments, firewall configs, and generated build rules.
- Diffs, code review comments, compiler errors, linter output, CI logs, stack traces, README snippets, tutorial scraps, forum posts, and IDE diagnostics.
- Minified or one-line code, partially copied code, missing-closing-brace complaints, and mixed prose/code pages.

Exclude:

- Object/dict/JSON/map literals: `return { ok: true }`, `const opts = { cache: false }`.
- Array/struct/composite initializers: `Point p = { 0, 1 }`, `int xs[] = { 1, 2 }`.
- Mathematical sets, even inside code comments.
- Template placeholders: `Hello {name}`, `{{ user }}`, `{API_KEY}`.
- JSX interpolation or framework template expressions when the brace is not delimiting a code block.
- Shell brace expansion, parameter expansion, command grouping that is too ambiguous, and regex quantifiers.
- Rust/JS/C macros or DSLs where the brace is best read as a data literal rather than a block; use only if clearly block-like.

Guidance:

- Prefer samples that are mostly actual code or raw developer artifacts, not explanations of braces.
- It is fine if a sample contains closing braces, semicolons, comments, warnings, or unrelated text, but every exact `" {"` must open a block.
- Avoid `return { ... }`, `= { ... }`, and JSON-like snippets unless there is no exact `" {"` in those literals. These are the easiest accidental wrong-label cases.
- Include both tidy and broken code: missing braces, indentation loss, copied Stack Overflow answers, pastebin scraps, generated code, CI failures, and code review fragments.
- In CSS/config samples, make sure selectors or directives precede the brace so the block role is obvious.

## `placeholder_token`

Semantic rule: `" {"` opens a placeholder, merge field, template variable, substitution slot, route/documentation variable, localization variable, or unresolved dynamic field in text intended to be filled later.

Good examples:

- `Hello {first_name}`
- `Order {order_id} is ready`
- `Dear { recipient },`
- `Subject: Reset code {CODE}`
- `greeting: "Hi {{ user_name }}"` when used by a template engine
- `endpoint {baseURL}/v1/users`

Include:

- Mail merge, CRM, transactional email, SMS, push notification, calendar invite, ticket macros, support canned replies, and form-letter templates.
- Localization and i18n files, game dialogue strings, CMS snippets, newsletter templates, landing-page copy, survey invitations, event reminders, and ecommerce messages.
- Developer docs, README templates, environment/config examples, code generation templates, API route docs, CLI scaffold output, f-strings/format strings, and generated issue/PR templates.
- Debug logs showing unresolved placeholders, template-rendering errors, replacement maps, test fixtures, screenshots OCR, and CMS preview text.
- Messy real-world fragments: forwarded drafts, half-filled forms, spammy marketing copy, duplicated footers, stale placeholders left in production, bot transcripts, and translated strings.

Exclude:

- Programming block delimiters: `if (ok) {`, `function x() {`, `.class {`.
- Object/dict/JSON/map literals unless the exact `" {"` occurrences are only inside quoted placeholder strings.
- Mathematical sets or set-builder notation.
- TeX grouping, regex quantifiers, shell brace expansion, or file glob patterns.
- Literal examples where `{` is being discussed as punctuation rather than used as a placeholder.
- Samples that begin with `{Name}` or `{CODE}` and never contain the exact `" {"` token later.

Guidance:

- The placeholder should feel like unresolved templated text, not an explanation of what placeholders are.
- Use many template syntaxes inside realistic surrounding text: `Dear {Name}`, `value: { user_name }`, `code {ORDER_ID}`, `Hi {{ customer.first_name }}`, `slot {0}`, `items {count}`, `host {base_url}`, and product-specific merge fields.
- Double-brace templates are allowed if the exact `" {"` occurrence clearly opens a placeholder delimiter.
- ICU/message-format snippets are allowed only when each exact `" {"` is a substitution field. Avoid plural/select syntax if nested braces would make the role hard to classify.
- Include realistic unreplaced-placeholder failures: emails sent with `{FirstName}`, logs saying missing value for `{account_id}`, preview pages with `{hero_copy}`, or support macros leaking `{case_link}`.
- Avoid starting most samples with formal salutations. Mix in raw localization rows, config comments, CSV exports, app strings, OCR snippets, chat transcripts, and ticket notes.

## Iterative Build Strategy

Use the old `ds/samples_{.yaml` only as a weak seed. Many old samples can inspire topics, but most v2 samples should be rewritten or replaced to improve realism.

Track diversity across these dimensions while building:

- All labels: source type, length, token position, token count, cleanliness/messiness, voice, emotional register, whether the sample is complete or clipped, and whether surrounding junk appears naturally.
- `set_notation`: math domain, notation form, finite vs infinite collections, set-builder vs enumerated sets, educational vs research vs computational source, student/corrected vs polished proof voice, and whether the set appears in prose, a table, a formula block, or a proof fragment.
- `programming_block_delimiter`: language/config family, block type, artifact type, indentation state, complete vs broken code, one-line vs multiline blocks, source vs diff vs log vs forum context, and whether the brace occurs in ordinary code, CSS/config, generated code, or diagnostics.
- `placeholder_token`: channel, template syntax, product/domain, placeholder naming style, filled/unfilled/error state, human vs automated voice, and whether the text appears as raw template, localization row, log, form letter, CMS export, codegen stub, or support macro.

Build in batches of roughly 20 per label:

- After each batch, scan all samples created so far for the exact token and manually classify every occurrence.
- Check that openings, source types, lengths, and topics are not becoming repetitive.
- Add longer, messier samples early enough that the final file is not dominated by compact examples.
- Keep a running mix of raw artifacts and human prose; do not leave "messy" examples until the last batch.
- When adding a new sample, deliberately decide whether the target token appears early, middle, or late.

Suggested source mix by label:

- `set_notation`: math/research proof fragments; worksheets and answer keys; probability/statistics tables; automata/language theory; algebra/topology/analysis; computational notebooks; OCR/PDF math artifacts.
- `programming_block_delimiter`: raw source files; CSS/config blocks; diffs and PR reviews; stack traces and linter/compiler output; forum/debug posts; tutorials/docs; generated code and broken paste fragments.
- `placeholder_token`: email/SMS/push templates; localization files; support macros; CMS/newsletter templates; API/config docs; codegen scaffolds; debug logs with unresolved fields; ecommerce/CRM/event forms.

## QA Checklist

Per sample:

- Contains exact token `" {"`.
- Every exact `" {"` occurrence has the target meaning.
- Across the label, contributes to a healthy mix of spaced-after-brace and unspaced-after-brace forms.
- Does not start with the target token, and usually avoids placing it extremely early.
- Avoids curator-style introductions unless they are genuinely part of the raw artifact.
- Is plausible as web/SFT corpus text rather than a meta-example about the label.
- Has enough context to disambiguate the brace role.
- Does not accidentally include a wrong-label exact `" {"` in a quote, code comment, template string, formula, or pasted footer.
- Is valid YAML.

Per meaning:

- Exactly 100 samples.
- Lengths, token counts, source types, tones, and formats are visibly varied.
- No dominant opening pattern, topic cluster, or narrative template.
- Includes rough/partial/crawled material without making artifacts theatrical.
- Includes a realistic amount of mundane text, not just clever or dense examples.
- Manually inspect high-risk patterns:
  - `= {` in programming samples, often an object or initializer rather than a block.
  - `if (...) {` or `.class {` in set or placeholder samples.
  - `Hello {Name}` or `{API_KEY}` in set or programming samples.
  - `\frac {`, `\section {`, and other TeX grouping in set samples.
  - `{{ ... }}` in non-placeholder samples.
  - ` { }` empty braces, which may be set notation only in a clearly mathematical context.
  - ` {1..5}`, `{old,new}`, regex quantifiers, and shell brace expansion.

Final review:

- Run a token occurrence scan and inspect all lines around `" {"`.
- Confirm each label has 100 samples.
- Confirm the final distribution includes code/config, math/proofs, templates, messy scraped artifacts, educational text, logs, tables, forum/chat/email fragments, and longer sequences where appropriate.
- Read for repeated "competent explainer" voice and replace those with rawer artifacts.
- Recheck YAML validity after any multiline edits.
