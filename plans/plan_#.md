# Plan: Polytok Token `" #"`

## Objective

Create `dsv2/samples_#.yaml` with 100 realistic samples for each meaning label:

- `comment_line_indicator`
- `hex_color_prefix`
- `numbered_item_rank`

Every sample must contain the exact token `" #"` at least once. Every occurrence of `" #"` inside a sample must match that sample's `meaning_label`.

Use the current dsv2 flat YAML schema, matching files such as `dsv2/samples_-.yaml`: one top-level item per meaning label, with `token`, `meaning_label`, and `text_samples` fields. Do not copy the old nested `meanings:` structure from `ds/samples_#.yaml`.

The old file is useful only as a rough taxonomy source. The `social_media_hashtag` label is retired and replaced with `hex_color_prefix`. The old `comment_line_indicator` samples are too clean, too explanatory, and too heavily made of toy comments. The old `numbered_item_rank` samples are mostly polished ranking prose and need more raw charts, scraped tables, ballots, reviews, sports/news fragments, search-result snippets, and messy list exports.

YAML hazard: unquoted ` #` starts a YAML comment. In the final dataset, keep `token: " #"` and serialize every text sample as a quoted string or block scalar that preserves literal ` #` text. Never leave sample text unquoted in a way that lets YAML treat target occurrences as comments.

## Exact-Token Notes

The target token is a leading ASCII space followed by an ASCII number sign: `" #"`.

- ` # comment`, `color: #f8fafc`, and `ranked #1` contain the target token.
- `# comment` at the beginning of a line does not contain the exact token unless there is a literal space before the `#`.
- `\t# comment` does not contain the exact token unless a normal space directly precedes the `#`.
- `"#fff"` does not contain the exact token; `color: #fff` does.
- Do not rely on bare `#` uses that lack the preceding space to satisfy the token requirement.
- Do not start any sample with the target token. For comment samples, put code or artifact text before the first indented comment. For hex and rank samples, avoid beginning with ` #...`.
- Avoid fullwidth or visually similar number signs.

Because bare `#` can appear in many unrelated roles, prefer samples where all visible hash marks are either the intended target sense or are absent. If a non-target bare hash is genuinely useful context, keep it only when it cannot be confused with an occurrence of the exact token, and manually inspect it. Bare hashes at line start generally should not be used to "help" a sample; they do not satisfy the token and can blur the semantics.

In this plan, shorthand forms such as `#fff`, `#1`, or `#include` are used to describe surface patterns. In the final dataset, the actual counted occurrence must include the preceding normal space, such as `color: #fff` or `ranked #1`.

## Realism Standard

Samples should feel like a mixed C4/HPLT-style slice, not curated demonstrations of `#`. Use raw excerpts directly when plausible: source files, configs, CI logs, docs, CSS/theme files, design tokens, scraped product pages, color palettes, rankings, charts, sports tables, ballots, reviews, wiki fragments, school worksheets, newsletters, forums, chat exports, OCR/PDF text, and partial web pages.

Good samples can be clipped, mundane, redundant, noisy, or surrounded by adjacent page residue. Include plausible artifacts such as broken indentation, copied terminal output, stale comments, generated docs, table rows, collapsed sidebars, repeated footers, OCR line wraps, cache fragments, HTML attributes, CSV exports, and support-ticket residue.

Avoid source-intro wrappers such as `snippet:`, `from a css file`, `ranking example`, `code comment:`, or `the page says`. A few labels are fine when they are naturally part of an artifact, but most samples should begin with the actual code, row, paragraph, table, chart, message, or page text.

## Lessons From The Old File

- `comment_line_indicator` overuses tidy Python/shell comments that explain obvious toy code. V2 should include real-looking config/code fragments, Makefiles, YAML/TOML, Dockerfiles, R, Ruby, Perl, Julia, shell, Python, PowerShell, MySQL, CI scripts, notebooks, environment files, generated exports, and broken copied material.
- The old comment samples sometimes use hash at line start or shebangs. For V2, every sample still needs the exact `" #"` token, and any visible comment hash should be visually plausible as indented or inline source text. Avoid relying on bare line-start `#` comments because they are not the target token.
- `social_media_hashtag` is removed. Do not include social media tag clusters, campaign tags, or `#Topic` labels as a target meaning.
- `numbered_item_rank` old samples are mostly smooth paragraphs about `#1`, `#2`, and `#3`. V2 needs rankings in raw data: chart exports, poll widgets, sports standings, app-store review snippets, SEO pages, ballots, school results, product comparison tables, race results, ecommerce bestseller modules, and scraped "top N" fragments.
- The token is easy to cross-contaminate. A comment sample can accidentally include `color: #fff`; a color sample can accidentally include `issue #12`; a rank sample can accidentally include a hashtag or code comment. Treat every `" #"` as a classified occurrence.

## Iteration Learnings From `samples_#.yaml`

The completed dataset needed many review cycles. These are the failure modes that recurred and should be checked early if this file is regenerated:

- Semantic clarity must be established before or at the target token, not repaired afterward. For rank samples, `Ari sits #1 on the ladder` is understandable but weaker than `Ari sits ranked #1 on the ladder`; `result #1`, `list #1`, `slot #1`, `order #1`, `category #1`, and `poll #1` should usually become `result rank #1`, `ranking #1`, `placement #1`, `position #1`, `seed #1`, or another phrase that makes the ordinal meaning explicit before the hash.
- Do not "fix" rank clarity by making every sample say `rank #N`. The final set should use varied rank language such as `ranked #1`, `reached #5`, `climbed to #2`, `finished #1`, `placed #3`, `top seed #1`, `Best Seller #1`, `search position #8`, `leaderboard #1`, and raw table fields like `current_rank=#2`. The key is variety plus unambiguous pre-token context.
- `numbered_item_rank` is the easiest label to make repetitive. Avoid making most samples lists of entities plus ranks plus a wry reaction. Mix dry exports, raw tables, product/search widgets, headlines, captions, automated notifications, broadcast transcripts, emails, support messages, and short incidental mentions. Keep many samples emotionally flat.
- `hex_color_prefix` initially drifted into a single skeleton: named UI element plus color, repeated as a palette, followed by a note that the export/page/OCR broke. Keep some clean CSS/design-token material, but include incidental color mentions in larger documents, raw configs, minified CSS, GIS/map layers, game mod configs, slicer settings, print/OCR fragments, hardware notes, terminal themes, craft/paint ledgers, and support/chat text.
- Avoid unnatural leading spaces inside structured values just to force the token. Forms like `"hex":" #00d1ff"`, `fill=' #334155'`, `data-rank=" #1"`, and `"rank":" #1"` look synthetic. Prefer natural forms such as `style="color: #00d1ff"`, `fill: #334155`, `color, #00d1ff`, `badge_text="rank #1"`, `rank #1`, or prose where the value follows a color/rank cue.
- `comment_line_indicator` can become too much like a dotfiles dump. Keep scripts/configs as the core, but include tutorial prose, forum answers, README snippets, Stack Overflow-like replies, Jupyter exports, auto-generated boilerplate, confused beginners, stale/wrong comments, translated comments, game/frontend/mobile/scientific code, and clipped mid-file fragments.
- A recurring bad shape was `context label\nactual sample`, such as `booking support transcript\n...`, `paint ledger from...`, or `dog show catalog OCR: ...`. Most labels should be removed or converted into artifact text. If the first line exists only to tell the reader what the sample is, cut it.
- Another recurring bad shape was "then the page/export/scraper breaks" as a narrated ending. Messiness is better when embodied inline: repeated footer text, broken tags, cookie banner text, ad table cells, OCR fragments, merged rows, clipped XML, or stray newsletter boilerplate. Do not end too many samples by describing what went wrong.
- Avoid relying on topic diversity alone. A rank section can mention sports, pies, apps, schools, dogs, and hotels but still be structurally identical if every sample is `X rank #N, Y rank #M, comment`. Track syntax, voice, narrative arc, and source shape separately.
- The final semantic audit should inspect every exact `" #"` occurrence in context, not just the first one per sample. Extra target occurrences often introduce cross-label mistakes.

## Distribution Guidance

Use approximate distributions, not exact quotas.

- Length: include a few very short fragments, many short and medium samples, and a meaningful minority of long messy samples.
- Token placement: do not start any sample with `" #"`. Avoid making the first target occurrence appear in the first few tokens in most samples. Longer samples should often contain a target occurrence late in the text.
- Token density: comments and color files can naturally have many target occurrences. Rank samples often need only one to four target occurrences, with dense chart/table samples mixed in.
- Source mix: include technical, commercial, educational, workplace, research-adjacent, news/wiki, informal, structured, crawled/OCR, and auto-generated styles where they fit each label.
- Voice and tone: vary between neutral machine output, terse human notes, confused user text, polished docs, bureaucratic forms, excited or annoyed reviews, and raw generated artifacts.
- Completeness: not every sample should be self-contained. Some can start or end abruptly as if scraped from the middle of a file, table, page, or thread.
- Cross-contamination: choose formats that do not accidentally introduce another `" #"` sense.

## Expected Corpus Shape

`comment_line_indicator` should be the most code/config-heavy label. It should include many snippets where comments are incidental maintenance notes, not the point of the sample. Think copied files, issue comments containing code blocks, notebook exports, package/build fragments, ops scripts, and config snippets with stale inline comments. A smaller share can be novice tutorials or classroom code.

`hex_color_prefix` should be design/web-heavy but not only CSS. The realistic core is theme code, style attributes, design tokens, email templates, palette tables, chart settings, CMS exports, and brand/accessibility docs. It should include some natural-language discussion of colors, but the ` #` occurrences still need to be color literals, not social tags or ids.

`numbered_item_rank` should be broad web ranking material. Music and sports are common, but do not let them dominate. Include rankings from product pages, search results, school results, app stores, polls, award ballots, racing, games, travel lists, media charts, leaderboards, and comparison articles. It should include middle and low ranks as well as `#1`.

Across all labels, include:

- Short scraps with one target occurrence.
- Medium snippets with two to five target occurrences.
- Long noisy artifacts with target occurrences spread across the whole sequence.
- A few extremely plain examples, because much real web text is boring.
- Some badly copied or partial examples, but not so many that the dataset feels theatrically dirty.

## Diversity Dimensions To Track

Track these dimensions during each 20-sample round:

- Source format: source code, config, shell output, CI/build snippets, README/docs, CSS/theme files, design-token exports, HTML inline styles, palette tables, chart/ranking tables, reviews, forums/chats, newsletters, OCR/PDF fragments, product modules, sports/results pages, and school/admin exports.
- Surface form: indented comment line, inline code comment, comment inside block-like config, ` #fff`, ` #ffffff`, ` #abcd`, ` #12345678`, ranked ` #1`, ordinal ` #2`, chart position ` #10`, option/rank slot ` #3`, and repeated rank lists.
- First-token position: early but not initial, mid-line after code or prose, table-body occurrence, late paragraph occurrence, late code comment, and repeated throughout long artifacts.
- Cleanliness: clean source/docs, rough copied rows, partial excerpts, OCR noise, page residue, broken formatting, ad/footer contamination, generated boilerplate, and stale cached widgets.
- Voice/register: machine output, terse developer notes, casual user review, confused support message, polished documentation, bureaucratic list, dry academic or technical prose, and excited entertainment/sports copy.
- Domain spread: software, data science, operations, education, design systems, ecommerce, media, music, sports, travel, civic/government, health/admin, hobbies, and household notes.
- Completeness and length: clipped fragments, short rows, medium artifacts, and long messy sequences with late target use.

## `comment_line_indicator`

Semantic rule: `" #"` marks a hash that begins or continues a comment in source code, shell/config syntax, notebooks, data files, command transcripts, or code-adjacent artifacts. The comment can be on its own indented line or at the end of a code/config line, but the hash must act as a comment delimiter.

Good examples:

- `value = clean(row)  # keep null rows out of export`
- `services:\n  api:\n    image: web\n    # staging uses the smaller queue`
- `Rscript build.R  # regenerate figures`
- `max_threads = 4 # old worker crashes above this`
- `SELECT id FROM users # temporary audit query`

Include:

- Python, shell, Bash, Makefile, Dockerfile comments, Ruby, R, Perl, Julia, PowerShell, YAML, TOML, INI, `.env`, MySQL, SQL-ish dumps, notebook exports, CI YAML, Terraform-like copied config when hash comments are plausible, and generated examples.
- Inline comments after code or config values, and indented full-line comments after surrounding source text.
- Raw source fragments with TODOs, commented-out commands, stale notes, copied stack traces with nearby comments, build scripts, data-cleaning notebooks, Docker/CI snippets, and deployment docs.
- Messy artifacts such as lost indentation, copied terminal prompts, comments in exported notebooks, partial diffs, commented CSV headers, stale config blocks, and docs where code fences have been flattened.
- A few non-English or bilingual comments when the syntax remains clear.

Exclude:

- Hex colors: `color: #fff`, `fill: #224466`.
- Social hashtags: ` #LaunchDay`, ` #coffee`.
- Ranked or numbered items: `ranked #1`, `option #2`.
- Markdown headings: ` # Title`, ` ## Section`.
- Issue, ticket, PR, invoice, room, case, and model numbers: `issue #42`, `room #210`, `PR #5`.
- URL fragments and anchors when they contain the target, such as `page.html #details` or `href=" #top"`. Bare forms like `href="#top"` do not satisfy the token, but still add distracting hash clutter.
- Shebangs and preprocessor directives: `#!/bin/bash`, ` #include`, ` #define`, because the hash is not a comment delimiter in those uses.
- Shell prompts or root prompts where `#` indicates privilege rather than comment.
- Data formats where `#` is part of an identifier, checksum, fragment, or literal string rather than a comment marker.

Guidance:

- This label should be code-heavy, but not just neat teaching snippets. Use real-looking fragments, partial files, and messy surrounding output.
- Avoid comments that merely narrate the obvious, such as `# print the result` after `print(result)`, unless the surrounding artifact is plausibly novice or generated material.
- Avoid having most samples start with comments. Start many with code/config/log text, then include comments later.
- Avoid letting a third or more of the section become complete scripts followed by a trailing forum/context note. Some samples should be just raw code, some should be prose with an embedded commented line, and some should start or end mid-function.
- Keep broad code-domain coverage. Include game loops, mobile/frontend snippets, academic/scientific code, generated UI files, config fragments, README/tutorial text, student mistakes, and chat/forum code pastes, not only ETL, deployment, ops, and data-cleaning scripts.
- Comment samples may contain other punctuation freely, but every exact `" #"` must be a comment delimiter. Do not include CSS colors, Markdown headings, or issue numbers with a preceding space.
- In longer samples, include target comments late in the file or output, not only near the top.

## `hex_color_prefix`

Semantic rule: `" #"` marks the hash prefix of a hexadecimal color literal. The token is followed by valid hex color characters, usually in CSS, SVG/HTML style attributes, design-token exports, palette tables, email templates, chart configs, or UI documentation.

Good examples:

- `color: #111827`
- `background-color: #f8fafc`
- `fill: #cc8844`
- `--brand-accent: #0ea5e9`
- `border, #d9e2ec, 1px`

Include:

- CSS and SCSS declarations, design tokens, Tailwind-like theme notes, HTML inline styles, SVG style attributes, chart/theme configs, palette CSV rows, brand guidelines, CMS color pickers, app settings exports, Figma/token exports rendered as text, email templates, and accessibility contrast notes.
- Three-, four-, six-, and eight-digit hex colors where plausible: `#fff`, `#0f0f`, `#334155`, `#112233cc`. Reject five-, seven-, nine-, or variable-length hash strings unless the surrounding standard explicitly supports them, which ordinary CSS colors do not.
- Color values in prose and tables: `primary #0057b8`, `warning border #f59e0b`, `old logo blue #173f5f`.
- Messy scraped artifacts: style tags flattened into text, repeated CSS blocks, theme tables with ad residue, OCR of brand guides, copied issue comments about colors, screenshots' alt text, and generated docs.
- Uppercase and lowercase hex, mixed-case where plausible, and repeated values across a theme file.

Exclude:

- Social hashtags: ` #Sale`, ` #DesignTok`.
- Comments: ` # TODO`, ` # keep this`.
- Ranked/numbered markers: ` #1`, ` #10`.
- Issue/ticket/PR/order identifiers: ` #1234`, `bug #88`, `order #A17`.
- URL anchors/fragments when they contain the target, such as ` #section`, `href=" #main"`, or `page #top`. Bare `href="#main"` does not satisfy the token but is still unwanted clutter.
- CSS ID selectors and DOM anchors: `.nav #main`, `button #icon`, `querySelector(" #modal")`.
- Markdown headings: ` # Overview`.
- Invalid or non-color hashes: ` #zzzzzz`, ` #primary`, ` #var(--x)`, ` #abcg`.
- Private channels, IRC/Slack rooms, shell prompts, checksums, commit hashes, anchors, and preprocessor directives.

Guidance:

- This label can be strongly technical/design-oriented, but it should not be a wall of pristine CSS. Mix raw CSS, design specs, ecommerce/theme snippets, chart configs, docs, comments from color-review threads, and scraped tables.
- Guard against the "palette plus defect" template. Do not make most samples a list of named colors followed by a note that the page/export/OCR/cache is broken. Balance lists with raw CSS/config, incidental one-color mentions, prose about color choices, hardware/print/game/science contexts, and clean artifacts with no drama.
- Make color semantics clear before the hash when the value could look numeric, especially for values such as `#1d4ed8` or `#2a6fdb`. Phrases like `sticker color is #2a6fdb`, `water color at #1d70a2`, or `fill color #073b4c` are safer than a bare `sticker #2a6fdb`.
- Be careful with comments inside CSS or config. `/* old #fff */` contains the exact `" #"` token before `#fff`; it is a color mention inside a comment, which may still be valid for `hex_color_prefix` if the context clearly discusses colors, but it is less clean than a declaration. Prefer uncommented declarations or comments without target occurrences unless the target is clearly still a color literal being discussed.
- Avoid object/JSON examples where the hex string is written as `"#fff"` with no preceding space, since it will not satisfy the exact token. Likewise, SVG attributes such as `fill="#fff"` are real colors but do not contain `" #"`. Use CSS declarations, inline `style="fill: #fff"`, CSV/table rows, prose, or config forms that naturally include ` #`.
- Avoid making structured data unnatural by inserting leading spaces inside quoted values. `fill=' #334155'`, `"hex":" #00d1ff"`, or `"color":" #fef3c7"` satisfy the token but look fake. Use nearby syntax that naturally puts a space before the color, such as `style='fill: #334155'`, `hex, #00d1ff`, `color is #fef3c7`, or `token= #fef3c7` only when that spacing is plausible for the artifact.
- Palette rows that begin with `#fff` or `#112233` do not contain the target token. Add realistic preceding context, such as `primary, #112233`, `brand blue #0057b8`, `--ink: #111827`, or a table cell with a space before the color.
- Include some accessibility, print, email, theme migration, charting, and brand-guideline contexts so the label is not only web CSS.
- In long samples, include colors throughout: palette tables, dark-mode overrides, print styles, or copied design-system tokens with late target values.

## `numbered_item_rank`

Semantic rule: `" #"` prefixes a number that marks rank, chart position, placement, seed, ordered option, poll result, top-N list entry, or ranked item position. The `#` means "number" in an ordinal/ranking/list-position sense, not merely an arbitrary identifier.

Good examples:

- `ranked #1 in the county results`
- `this week's chart: #4 last week, #2 this week`
- `option #3 had the lowest cost`
- `Seed #8 upset seed #1`
- `Result row says #12 Rivera, 48.31`

Include:

- Music/movie/book/game charts, product bestseller modules, search-result rankings, sports standings, tournament seeds, race placements, school competition results, poll summaries, review-site lists, award ballots, leaderboard exports, SEO "top 10" pages, recommendation widgets, bracket/seed notes, app-store rankings, and ecommerce category pages.
- Messy table rows, scraped chart widgets, cached standings, OCR result sheets, copied newsletters, forum arguments about rankings, liveblog fragments, and partial result exports.
- Both high and low positions: `#1`, `#2`, `#3`, `#10`, `#27`, `#100`, `#1 overall`, `#4 seed`, `#12 on the list`.
- Samples where ranks change over time: last week `#8`, now `#3`; preseason `#14`, final `#2`.
- Some option-number contexts where the number marks an ordered choice in a ranked list or assignment, such as `choice #1` and `preference #2`, but keep this less common than true ranking.
- Option-number contexts are valid only when the option is part of an ordered choice, preference, ballot, or ranked list. Plain arbitrary option IDs, form choices, bus numbers, product variants, or room numbers are identifiers and should be rejected.

Exclude:

- Issue, ticket, PR, bug, case, order, invoice, room, bus, flight, apartment, model, serial, form, and SKU numbers: `issue #42`, `order #991`, `room #204`.
- Social hashtags: ` #1Fan`, ` #BestDay`.
- Hex colors: ` #111827`, ` #2A5`.
- Code comments or config comments: ` # TODO`.
- Markdown headings: ` # Top Picks`.
- Phone extensions, legal sections, address units, citation markers, footnotes, anchors, and arbitrary identifiers.
- Probability/statistical notation or programming identifiers where `#` means count/cardinality/comment rather than rank.

Guidance:

- This label should feel like rankings as they occur on the web, not just paragraphs saying "I rank this #1." Use raw charts, tables, copied widgets, brackets, poll exports, school result sheets, product category pages, and forum snippets.
- Avoid overusing `#1` praise language. Include ordinary middle ranks, declining ranks, seeds, options, and boring table rows.
- Avoid the rigid `rank #N` template as the only syntax. Use `ranked #N`, `reached #N`, `climbed to #N`, `fell to #N`, `finished #N`, `placed #N`, `seed #N`, `Best Seller #N`, `search position #N`, `leaderboard #N`, and dry fields such as `current_rank=#N`. However, the rank sense still needs to be clear before or at the hash.
- Be skeptical of bare phrases like `result #1`, `list #2`, `slot #3`, `order #4`, `category #5`, and `target #1`. They can read as identifiers unless ranking language appears before the hash. Rewrite to `result rank #1`, `ranking #2`, `priority rank #3`, `price ranking #4`, `category rank #5`, or `ranked #1 among targets`.
- Keep the emotional register mixed. A few angry competitors, confused customers, excited fans, and sarcastic comments are useful, but most web ranking material is flat: exports, product badges, category pages, automated reports, neutral news briefs, and tables.
- Avoid unnatural structured values such as `"rank":" #1"` or `data-rank=" #1"`. Prefer valid structured data without the target plus adjacent visible text that contains the target naturally, such as `data-rank="#1"` with `sales rank #1`, or raw columns like `rank #1` / `current_rank=#1`.
- Ranking rows that start with `#1` do not contain the exact target token. Use natural preceding context such as `rank #1`, `pos #4`, `last week #12`, `seed #8`, or table rows where the rank appears after a column label or delimiter.
- First target occurrence should often be mid-sentence or in a table body, not always near the first words.
- Do not include `issue #`, `ticket #`, `case #`, or `PR #` examples; these are common but off-label for this meaning.
- If a sample uses `#1` as "number one fan" or slogan text, reject it unless it clearly functions as a rank.

## Cross-Meaning Hazards

Inspect these cases manually during dataset creation:

- `color: #fff  # old white` mixes a hex color and a comment indicator.
- `ranked #1  # final poll` mixes rank and comment.
- ` # TODO use #fff later` has a comment target and a bare color mention; the exact token before `TODO` is valid for comments, but the later color may also contain `" #"` if spaced.
- `issue #123` and `PR #44` are identifiers, not ranks.
- `room #2` is usually an identifier, not a rank, unless the surrounding text is explicitly ranking rooms.
- `seed #1` can be valid rank/seed; `bus #1` is an identifier.
- ` #include <stdio.h>` is a C preprocessor directive, not a comment.
- ` #!/usr/bin/env bash` is a shebang if at file start, not a comment target.
- ` # Heading` in Markdown is a heading marker, not a comment.
- `href=" #main"` or `go to #section` is an anchor, not a color, comment, or rank.
- `.article #sidebar { color: #333 }` mixes a CSS ID selector with a hex color. For `hex_color_prefix`, remove or rewrite selectors so every exact `" #"` is a color literal.
- `channel #general`, `IRC #help`, and Slack room names are channel identifiers, not social hashtags or ranks.
- `C#` and `F#` are language/music names and normally do not include the exact target token unless preceded by a space before the `#`; avoid them anyway to reduce ambiguity.
- ` #123456` could be a hex color or an identifier. Only use it for `hex_color_prefix` when the surrounding syntax clearly marks it as a color.
- ` #1a2b3c` could be a hex color but can look like an id/hash in non-design contexts. Use CSS/theme/color language around it.

## Dataset Creation Strategy

Build `dsv2/samples_#.yaml` in rounds of about 20 samples per label, then review and revise before adding the next round.

For each `comment_line_indicator` round, deliberately cover several of:

- Python, Bash/shell, Makefile, Dockerfile, YAML/CI, TOML/INI/env, R, Ruby, Perl, Julia, PowerShell, MySQL, notebook exports, generated config, deployment scripts, data-cleaning fragments, and copied terminal/code docs.
- Surface forms such as inline `code  # comment`, indented full-line `  # comment`, config comments after a value, stale TODOs, commented-out commands, and comments late in long files.

For each `hex_color_prefix` round, deliberately cover several of:

- CSS/SCSS, design tokens, theme tables, email templates, HTML style attributes, SVG/CMS style text, chart configs, brand guides, accessibility contrast reports, app settings exports, color-review comments, product theme snippets, and scraped palette pages.
- Surface forms such as ` #fff`, ` #000000`, ` #0ea5e9`, ` #F5A623`, ` #112233cc`, and table/prose forms like `brand blue #0057b8`.

For each `numbered_item_rank` round, deliberately cover several of:

- Music charts, sports standings, tournament seeds, race results, product bestseller pages, search-result rankings, app-store rankings, school competition sheets, poll summaries, award ballots, review-site lists, SEO pages, leaderboard exports, and forum arguments.
- Surface forms such as ` #1`, ` #2`, ` #10`, ` #27`, `seed #8`, `rank #4`, `choice #3`, `last week #12`, and `overall #1`.

## 20-Sample Round Review Prompts

After adding each batch of about 20 samples per label, pause and ask these directly:

- Did any exact `" #"` occurrence slip into a different meaning than the label?
- Are there samples whose first target token appears too early or at the very start?
- Are too many samples shaped like clean educational examples instead of raw corpus text?
- Did the `comment_line_indicator` batch overuse Python, obvious comments, or `# End of file` endings?
- Did the `hex_color_prefix` batch overuse pristine CSS declarations without tables, docs, scraped text, or design-system artifacts?
- Did the `numbered_item_rank` batch overuse `#1`, music charts, sports standings, or personal "my top picks" prose?
- Are there enough messy, partial, or structurally weird artifacts without making the mess feel forced?
- Is the mess embedded as text, tags, repeated rows, OCR fragments, or boilerplate rather than described from outside?
- Are longer samples using `" #"` late in the sequence, not only in the opening lines?
- Are voices varied: machine output, terse workplace notes, confused users, polished docs, reviews, bureaucratic forms, and plain flat web text?
- Is any domain appearing disproportionately across the whole file?
- For every target occurrence, is the meaning clear by the time the reader reaches the hash?
- Are there still curator-style openings or `intro line\nactual sample` patterns that can be removed?

If a round fails one of these prompts, revise existing samples before adding the next round. Do not "fix" diversity only by appending better examples at the end; rebalance the current set.

After each round:

- Search every exact `" #"` occurrence and classify it manually.
- For `comment_line_indicator`, search for color-looking patterns, ` #\d`, ` #include`, ` #define`, ` #!`, Markdown heading patterns, `issue #`, `PR #`, `ticket #`, `order #`, `room #`, and channel names.
- For `hex_color_prefix`, search for invalid hex digits, identifier contexts such as `issue #`, rank contexts such as `#1`, comments such as ` # TODO`, Markdown headings, anchors, channels, and social hashtags.
- For `numbered_item_rank`, search for identifier contexts such as issue/ticket/order/room/model numbers, hex-looking values, comments, Markdown headings, hashtags, and anchors.
- Search for unnatural structured values such as `" #`, `' #`, `"rank":" #`, `data-rank=" #`, `fill=" #`, and `fill=' #`.
- Search for curator labels and repeated context intros such as `transcript`, `text export`, `OCR:`, `pasted into ticket`, `copied from`, `reader test`, `practice room`, `traveler review`, and `the page says`.
- Check that no sample starts with the target token and that first-target positions vary.
- Check that long samples contain some late target uses, not only an early mention.
- Rebalance if a label becomes too tidy, too CSS-heavy, too Python-heavy, too sports-heavy, too music-chart-heavy, too ecommerce-heavy, too explanatory, or too centered on one topic.
- Validate YAML structure before continuing.

## Useful Final Validation Commands

Run these after major edits:

```powershell
python scripts/check_length_distribution.py 'dsv2/samples_#.yaml'
```

Count labels and token placement:

```powershell
$label=''; $counts=@{}; $missing=@(); $starts=@(); $ln=0; Get-Content 'dsv2/samples_#.yaml' | ForEach-Object { $ln++; if ($_ -match 'meaning_label: "([^"]+)"') { $label=$matches[1]; if (-not $counts.ContainsKey($label)) { $counts[$label]=0 } }; if ($_ -match '^\s*-\s*"') { $counts[$label]++; if ($_ -notmatch ' #') { $missing += "${ln} [$label] $_" }; if ($_ -match '^\s*-\s*"#') { $starts += "${ln} [$label] $_" } } }; $counts; "missing=$($missing.Count)"; "starts=$($starts.Count)"
```

Check high-risk semantic drift:

```powershell
Select-String -Path 'dsv2/samples_#.yaml' -Pattern 'result #[0-9]|list #[0-9]|slot #[0-9]|target #[0-9]|item #[0-9]|issue #[0-9]|ticket #[0-9]|room #[0-9]|lot #[0-9]|sticker #[0-9]|label #[0-9]|tag #[0-9]|category #[0-9]|poll #[0-9]|order #[0-9]|" #|'' #|rank":" #|data-rank=" #|fill=" #|fill='' #'
```

Check label-specific stray hashes:

```powershell
$label=''; $ln=0; Get-Content 'dsv2/samples_#.yaml' | ForEach-Object { $ln++; if ($_ -match 'meaning_label: "([^"]+)"') { $label=$matches[1] }; if ($_ -match '^\s*-\s*"' -and $label -eq 'hex_color_prefix' -and $_ -match '#[^0-9a-fA-F{]') { "${ln}: $_" }; if ($_ -match '^\s*-\s*"' -and $label -eq 'numbered_item_rank' -and $_ -match '#[^0-9]') { "${ln}: $_" } }
```

## QA Checklist

Per sample:

- Contains at least one exact `" #"` token.
- Every exact `" #"` occurrence has the target meaning for the active label.
- Does not start with `" #"` and usually avoids placing the first target occurrence in the first few tokens.
- Avoids curator-style source introductions unless the introduction is naturally part of the artifact.
- Is plausible as web/SFT corpus text, with realistic messiness and no theatrical over-explanation.
- Avoids off-label target uses such as hashtags, identifiers, CSS colors in comment/rank labels, comments in color/rank labels, issue numbers, anchors, Markdown headings, channels, and preprocessor directives.
- Is valid YAML when inserted into `dsv2/samples_#.yaml`, with ` #` preserved inside the loaded string rather than swallowed as a YAML comment.

Per meaning:

- Exactly 100 samples.
- Lengths, source types, voices, formats, emotional registers, and token counts are visibly varied.
- No dominant opening pattern, topic cluster, or narrative template.
- Includes rough/partial/crawled material without simply labeling the source type.
- Has target tokens distributed across early, middle, and late positions, especially in longer samples.
- Includes short fragments, medium artifacts, and some long messy samples.
- Manually inspect high-risk mixed-context cases where comment markers, hex colors, ranks, hashtags, issue numbers, Markdown headings, and anchors can appear near each other.
