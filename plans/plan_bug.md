# Plan: Polytok Token `" bug"`

## Objective

Create `dsv2/samples_bug.yaml` with 100 realistic samples for each meaning label:

- `insect_bug`
- `software_defect_bug`
- `annoy_bother_bug`

Every sample must contain the exact token `" bug"` at least once. Every occurrence of `" bug"` inside a sample must match that sample's `meaning_label`, including occurrences inside compounds, identifiers, paths, headings, and quoted text.

The old `ds/samples_bug.yaml` established insect, software-defect, and covert-device senses, but the v2 target now swaps the covert-device sense for the annoyance/bother/pester sense. The dataset should feel like a mixed C4/HPLT/SFT-style scrape: issue trackers, field notes, classroom fragments, comments, raw logs, listings, chats, PDFs, emails, tables, code comments, news snippets, forum posts, OCR, and partial pages.

Use the v2 shape from `dsv2/samples_-.yaml`: one top-level entry per meaning label, each with `token: " bug"`, `meaning_label: ...`, and `text_samples:`. Do not preserve the old nested `meanings:` structure from `ds/samples_bug.yaml`.

## Old Dataset Read-Through Notes

The v1 file has 35 `insect_bug`, 33 `software_defect_bug`, and 32 `covert_device_bug` samples. It is useful for the label set, but not for distribution.

Problems to correct:

- Too many complete, polished paragraphs with a calm narrator explaining what happened.
- Too many repeated arcs: a person notices the bug, studies it, appreciates it; a team discovers the bug, diagnoses it, fixes it; an agent finds the bug, realizes secrets were recorded.
- Too much repeated phrasing around `the bug`, especially in long insect and covert samples.
- Too many source wrappers like `Title:`, `Chat transcript:`, `HTML snippet from old forum:`, `Meeting notes:`, and `Transcript snippet:`. Real artifacts can have headings, but the sample should usually begin with the artifact itself.
- Insect samples over-index on gardens, wonder, and field-journal prose.
- Software samples over-index on generic web/app/login/checkout problems and explanatory root-cause paragraphs.
- Annoyance samples are newly introduced and must not collapse into one repetitive pattern like `stop trying to bug me`.
- Very little raw tabular data, OCR, invoices, product pages, issue exports, logs, source code, legal snippets, or clipped messy context.

## General Realism Standard

Use samples as if they were scraped directly, not introduced or explained by a curator. Avoid openings such as `forum post:`, `biology note:`, `bug tracker says`, `spy novel excerpt`, or `example:` unless that label is visibly part of the source artifact itself.

The token should not appear as the first text in any sample. Usually include at least a few words, markup characters, log columns, or table fields before the first `" bug"`.

Vary source shape:

- Short scraps, medium paragraphs, and a meaningful minority of long messy extracts.
- Complete thoughts mixed with clipped middle-of-page fragments.
- Natural language mixed with raw structured material: YAML, JSON, Markdown tables, CSV, HTML, code comments, stack traces, changelog entries, OCR, email headers, chat logs, transcript lines, metadata rows, and UI copy.
- Neutral, flat, automated, confused, irritated, excited, joking, academic, corporate, instructional, and ad-like voices.
- Some clean samples are fine, but most should have realistic imperfection: duplicated footer text, stale sidebars, missing context, odd line breaks, comments merged into docs, mobile scrape residue, partial tables, tracking IDs, and inconsistent capitalization.
- A few multilingual or mixed-language snippets are useful when the English word `bug` is naturally used, such as software teams writing `el bug`, support pages mixing English field names, or pest-control pages preserving product names like `bed bug`.

Messy context must not introduce a second sense of `" bug"`. A software support page should not have an ad for `bug spray`; an annoyance complaint should not include software `bug report` language; an insect field note should not have a footer link to a software `bug tracker`.

Avoid overusing the pattern `the bug ... the bug ...`. It is especially stale in the old data. Mix definite, indefinite, plural, compound, and attributive forms such as `a bug`, `this bug`, `bed bug`, `stink bug`, `bug report`, `bug_id`, `will bug me`, `trying to bug him`, and `not the person to bug`, but only when the target sense is unambiguous.

The examples below are semantic examples, not required openings. When generating actual samples, add preceding context whenever an example phrase would otherwise begin with `bug` and fail to include the exact leading-space token.

## Exact Token Hazards

Because the target is `" bug"` rather than the standalone word `bug`, it can appear inside longer words and compounds. Treat every occurrence as active and check it.

The token is lowercase and includes the leading space. A sample that starts with `bug`, `bug_id`, `bug report`, or `Bug report` does not satisfy the exact token at that starting occurrence. Include preceding text, punctuation plus a space, a field label, or another later lowercase `" bug"` occurrence.

Do not satisfy the token requirement with an immediate opening like `- bug report`, `// bug`, or `> bug found` unless there is preceding source context in the same sample. Such lines are realistic inside artifacts, but bad as the first thing in a sample.

Structured data needs special care. `"bug_id"` in JSON, `<bug>` in XML, `(bug)` in notes, and start-of-line `bug_id` do not contain the exact leading-space token at that occurrence because the character before `bug` is not a space. Indented `  bug_id`, prose like `ticket bug_id`, or a later phrase like `known bug` does.

Allowed only when semantically correct for the label:

- ` bug`, ` bugs`, ` bug's`
- ` bug-report`, ` bug_report`, ` bug_id`, ` bugfix`, ` bugzilla`, ` bug_count` when they refer to software defects
- ` bed bug`, ` stink bug`, ` squash bug`, ` assassin bug`, ` water bug`, ` bug spray`, ` bug bite` when they refer to insects or similar crawling arthropods
- ` bug me`, ` bug him`, ` bug her`, ` bug them`, ` bug people`, ` bug someone`, and similar bare-verb annoyance constructions only when the meaning is annoy/bother/pester

Avoid across all labels unless deliberately assigned and unambiguous:

- Illness: `stomach bug`, `flu bug`, `winter bug`
- Covert surveillance: `bug detector`, `bug sweep`, `bugged room`, `bugging device`
- Enthusiasm: `travel bug`, `photography bug`
- Vehicle/adjective/gear: `VW bug`, `beach buggy`, `baby buggy`, `buggy behavior` unless the software-defect sense is explicit
- Programming words where `" bug"` is not the semantic unit, or would introduce ambiguity: `debug`, `debugging`, `debugger`
- Other unrelated strings beginning with the letters `bug`: `bug out`, `bug-out bag`, `bugle`, `bug-eyed`, `buggy` as a stroller/cart/car/adjective
- Mixed-sense puns where insect, defect, or surveillance readings are both plausible
- Negated uses are allowed only when the sense remains clear: `not a bug` in a software triage thread can be software-defect sense; `not a bug, a feature` in casual nontechnical banter should be avoided.

Final iteration lesson: for the annoyance label, prefer the exact bare token ` bug` over inflections. During drafting it is easy to drift into `bugs me`, `bugged her`, or `bugging them`; those can be semantically valid English but were too distributionally dominant and less aligned with the requested token. Rewrite most or all of them to bare forms such as `will bug me`, `trying to bug him`, `not the person to bug`, `how to bug people`, `enough to bug her`, or `the wrong time to bug me`.

## False-Friend Matrix

Use this matrix during review when a phrase could fit more than one area.

- `bed bug`, `stink bug`, `June bug`, `squash bug`: insect sense only.
- `bug spray`, `bug trap`, `bug bite`: insect sense only unless the text is explicitly metaphorical, in which case avoid it.
- `bug report`, `bug ticket`, `bug tracker`, `bug_id`, `bugfix`: software-defect sense by default; insect only if the report/ticket is plainly about insect sightings or pest inspection.
- `bug bounty`, `bug class`, `bug chain`: software/security defect sense only.
- `bugging him`, `bugged me`, `keeps bugging`, `stop bugging`: annoyance/bothering sense only, but avoid these in the final v2 file unless the user explicitly asks for inflections. Prefer bare ` bug` constructions.
- `bug detector`, `bug sweep`, `planted bug`, `bugged office`, `bugged room`, `bugged phone`, `bugged lamp`: excluded now because the covert-device sense is not a target label.
- `bugged release`, `bugged build`: avoid because it can drift between software defect and annoyance.
- `buggy behavior`, `bug out`, `bugle`, `bug-eyed`: avoid.
- `stomach bug`, `flu bug`, `travel bug`, `VW bug`: excluded senses.

## Distribution Guidance

Use approximate distributions, not quotas.

- Length: include a few very short fragments, many short and medium samples, and a real long tail per label. The old `bug` file has no long samples, so do not repeat that flat distribution.
- Token position: include many samples where `" bug"` appears later in the sequence, not only in the first sentence or first line.
- Token density: insect and annoyance samples often work with one or two uses; software samples can naturally include repeated `bug` references in tickets, changelogs, and code comments.
- Source mix: each label should include everyday web text, technical/professional text where appropriate, messy crawled artifacts, structured data, social/forum/chat material, and educational/reference fragments.
- Tone: most samples should be neutral or flat, with some irritated users, excited nature watchers, bored workers, sibling/family friction, dry official prose, kids' worksheets, and auto-generated text.
- Topic diversity: avoid making insect samples mostly gardens, software samples mostly checkout/login bugs, or annoyance samples mostly sibling complaints or generic `stop trying to bug me` lines.

Final iteration distribution lessons:

- Stage-label openings were the most persistent artifact smell. Lines like `Museum catalog card`, `Triage export`, `customer transcript`, `campground review`, `Postmortem draft`, or `Garden newsletter bottom half` usually needed to be removed or turned into actual source text, headers, rows, or dialogue. The sample should be the document, not a description of the document.
- `insect_bug` repeatedly drifted toward expert/naturalist/agriculture voices. Counterbalance with squeamish tenants, confused parents, blurry phone-photo posters, kids with misspellings, irritated guests, product reviewers, and people who lack insect vocabulary.
- `software_defect_bug` repeatedly drifted toward professional QA/engineering summaries. Counterbalance with angry or confused users, managers, forum posters, app-store reviews, sales/support fragments, and bare artifacts where the defect is visible without a polished impact/action summary.
- `annoy_bother_bug` repeatedly drifted toward notification/message complaints and the syntax `X bugs me`. Counterbalance with physical pestering, hallway interruptions, kids poking siblings, door-to-door sales, pets demanding food, chores, in-person nagging, sports/ref boundaries, family photo requests, and institutional rules.
- Avoid the repeated arc `problem -> administrative follow-up` across labels. A realistic scrape can be a raw row, a fragment, a joke, a policy line, a child worksheet, a support reply, or a complaint with no tidy resolution.
- Avoid the old cross-label habit where the medium is also broken: scanner clipped the page, export shifted columns, footer repeated, template pasted wrong. Use messy artifacts when they are genuinely present, but do not narrate formatting failure in most samples.

Approximate source mix by label:

- `insect_bug`: household/pest-control and commercial pages; gardening/agriculture/extension-office text; field/science/classroom material; informal photos, reviews, and forum posts; structured/OCR/listing fragments.
- `software_defect_bug`: raw developer artifacts; issue/support systems; release docs and known issues; user/app-store complaints; security/vulnerability material; workplace chat/postmortem fragments.
- `annoy_bother_bug`: casual chats, social posts, complaint forms, etiquette advice, HR/school notes, customer-service tone complaints, workplace reminders, family texts, moderation logs, therapy/journal fragments, and scraped comment threads where `bug` means pester/annoy.

Length and placement targets:

- Very short samples: a small handful per label, often rows, comments, captions, or chat lines.
- Short/medium samples: the bulk of each label, with enough surrounding context to make the sense unambiguous.
- Long samples: aim for a modest but visible long tail, especially crawled pages, support threads, issue exports, invoices, inspection reports, transcripts, and OCR fragments. Do not force long samples when the artifact would naturally be short.
- First occurrence: avoid having most samples place `" bug"` in the first five words. A few early occurrences are natural; many should appear after setup, table fields, quoted replies, or appended notes.
- Late occurrence: include samples where the first or clearest `" bug"` appears past the midpoint, especially in long artifacts with sidebars, logs, or forwarded text.

## `insect_bug`

Semantic rule: `" bug"` means an insect or colloquial small crawling arthropod, including named true bugs and common household/garden pests. The sample may be scientific, casual, commercial, educational, or fictional, but every `" bug"` must refer to a living or dead creature, its body, traces, or insect-related products.

Good examples:

- `washed one tiny bug off the lettuce before packing lunches`
- `brown marmorated stink bug nymph, stage III`
- `bed bug inspection found casings near the headboard`
- `kids counted each bug under the rotting log`
- `camp store said bug spray was sold out after the lake weekend`

Include:

- Field notes, nature guides, pest-control pages, extension office bulletins, garden forums, hiking/camping posts, classroom worksheets, children's activities, product reviews for traps/sprays, recipe scraps with accidental insects, specimen labels, museum exhibits, lab notebooks, agricultural reports, OCR from PDFs, and casual household complaints.
- Named insects and near-insect colloquial uses: bed bug, stink bug, squash bug, water bug, June bug, pill bug/roly-poly if context makes the colloquial creature sense clear.
- Life stages, anatomy, behavior, habitat, bites, traps, infestations, shells/casings, specimens, images, and identification keys.
- Messy artifacts: species tables, pesticide labels, comment threads, image alt text, inspection invoices, school worksheets, two-column PDF merges, forum quotes, and product Q&A.

Exclude:

- Software defects, issue trackers, code comments, `bug report` unless it is about an insect sighting report.
- Listening devices or rooms being bugged.
- Illness (`stomach bug`), annoyance (`bugging me`), enthusiasm (`caught the travel bug`), and vehicles (`VW bug`).
- Samples where `ladybug` is the only occurrence, because it does not contain the exact token `" bug"` as a separate leading-space token. `lady bug` can be used only if the phrase appears naturally as a split or error and clearly refers to the insect.

Guidance:

- The old insect set leans dreamy and polished. V2 should be more mundane and scraped: pest invoices, extension-office copy, garden comments, classroom pages, campground reviews, pet food listings, inspection notes, OCR, and casual phone photos.
- Do not make every insect sample reverent or whimsical. Most bug text on the web is practical, annoyed, observational, or commercial.
- Include some non-human structured samples where the word is in a field, tag, product title, species row, or caption.
- Watch compounds carefully. `bug bite` and `bug spray` are insect-related; `bug report` is not unless the report is about insects.
- Final semantic-clarity lesson: if the first occurrence is a bare ` bug`, put an insect cue before it when possible: `insect`, `specimen`, `pest`, `six legs`, a taxon/family name, an inspection context, a species name, or a visible product context such as trap/spray/net. `The bug is small` is weaker than `The insect is small. The bug...`.
- Keep bed bug samples scarce. Five-ish is enough; too many hotel/apartment/heat-treatment examples make the section feel narrower than real insect web text.

## `software_defect_bug`

Semantic rule: `" bug"` means a software or digital-system defect, error, vulnerability, regression, issue, or flaw. It can appear in human prose, code comments, ticket metadata, identifiers, changelogs, logs, release notes, forum answers, support transcripts, tests, or security reports.

Good examples:

- `opened a bug after the export button returned a blank CSV`
- `ticket row bug_id: PAY-4821`
- `// bug: cache key ignores tenant_id`
- `known bug in 2.4.1 breaks Safari upload`
- `triage moved the bug to P1 after two duplicate charges`

Include:

- Issue trackers, bug reports, QA notes, Jira/GitHub/GitLab exports, Stack Overflow fragments, changelogs, release notes, failing tests, code comments, commit messages, CI logs, crash dumps, telemetry dashboards, support tickets, app reviews, forum posts, security advisories, postmortems, TODO comments, and documentation known-issues pages.
- Bugs in web apps, mobile apps, games, firmware, drivers, data pipelines, ML systems, spreadsheets/macros, APIs, auth, payments, rendering, localization, date/time handling, concurrency, memory, caching, accessibility, and deployment tooling.
- Security defects where `bug` refers to a software vulnerability. `bug bounty`, `bug class`, and `bug chain` are acceptable if the sense is vulnerability/defect.
- Natural developer shorthand: `bug_id`, `bugCount`, `bugfix`, `bug_report.md`, `bugzilla`, `known-bug`, and `bug bash`, as long as every `" bug"` occurrence has the software-defect sense.

Exclude:

- Insects in code examples, games, images, CSS class names, or sample data unless the exact token does not occur.
- Covert listening devices, `bugged room`, `bug detector`, surveillance sweep.
- `debug`, `debugging`, or `debugger` as target evidence. These do not necessarily contain the target sense and can pull the sample toward tool/process language rather than the defect itself.
- Generic annoyance or illness: `this is bugging me`, `stomach bug`.

Guidance:

- This label can be the most technical and structurally messy. Use raw artifacts heavily: stack traces, diffs, config, test output, ticket tables, CI summaries, JSON API responses, and issue templates.
- Avoid making every sample say `we found a bug in...`. Include terse metadata, unresolved duplicate tickets, logs with one comment line, raw Markdown lists, customer complaints, and automated dependency PR notes.
- Include realistic severity variation: tiny UI nits, serious data loss, security bugs, flaky race conditions, platform-specific regressions, old known issues, reopened tickets, and "not a bug" discussions where every target occurrence still refers to a suspected software defect.
- Put ` bug` late in some samples via comments, footer links, duplicate ticket references, appended release-note sections, or copied support replies.
- Final semantic-clarity lesson: before a vague phrase like `this bug`, `the bug`, or `visible bug`, establish the failure mode: `export failure`, `invoice bug`, `duplicate-tap bug`, `checkout total doubles`, `Safari file chooser`, etc. This avoids relying on post-token explanation.
- Watch for the meta-confusion pattern. Not every defect sample should also have stale docs, misrouted tickets, confusing dashboards, cached pages, or contradictory status text. Those are useful sometimes, but not as a default second beat.

## `annoy_bother_bug`

Semantic rule: `" bug"` means to annoy, bother, pester, nag, irritate, or keep pressing someone. The sample can be casual, workplace, instructional, social, parental, customer-service, therapeutic, or fictional, but every `" bug"` occurrence must mean bothering/annoying rather than insect, software defect, surveillance device, illness, enthusiasm, or vehicle.

Good examples:

- `the third reminder will bug me`
- `trying to bug him for answers after redirection`
- `not the person to bug about the spreadsheet`
- `daily calls will bug the clinic manager`
- `the wrong time to bug me with repeated questions`

Include:

- Direct requests to stop pestering, nagging, interrupting, reminding, asking, texting, calling, hovering, or pushing.
- Complaints about sounds, manners, habits, chores, sales follow-ups, meeting reminders, forms, ads, notifications, jokes, spoiler requests, and social pressure.
- Messy artifacts: SMS/Slack/Discord logs, forum replies, advice columns, classroom notes, HR tickets, moderation excerpts, personal journals, survey comments, transcript fragments, comment threads, email chains, UI notification feedback, and policy snippets.
- Prefer bare ` bug` forms where context before the token already establishes annoyance: `will bug me`, `trying to bug`, `safe time to bug`, `not the person to bug`, `how to bug`, `enough to bug her`, `wrong time to bug me`, `pester or bug`.

Exclude:

- Software defects, issue trackers, bug reports, bug bounties, debug/debugging/debugger, and `buggy` as software adjective.
- Insects, bug spray, bed bugs, true bugs, household pests, and `bug bite`.
- Covert listening devices, RF sweep, bug detector, bugged room/phone/lamp.
- Illness (`stomach bug`, `flu bug`), enthusiasm (`travel bug`), vehicles (`VW bug`), and `bug out`.
- Bare uses like `it will bug me` when nothing before `" bug"` establishes annoyance. Prefer pre-token cues such as `annoyance`, `nagging`, `pester`, `quit`, `stop`, `reminder`, or `noise`.

Guidance:

- This label should feel common and mundane, not a dictionary exercise. Most uses are conversational or complaint-shaped.
- The strongest semantic-clarity pattern is `stop/quit/keep/pester/nag/bother/annoy` before the exact `" bug"` token.
- Do not overuse direct first-person `bug me`; include institutional text, advice, logs, partial chats, structured feedback, and third-person boundaries.
- Be careful with `bugged` and `bugging`: in this label they must mean annoyed, not surveilled or broken, but final drafts should usually rewrite them to bare ` bug`.
- Final iteration lesson: this was the weakest and most repetitive label until it moved away from the single syntactic pattern `[repeated X] bug(s) me/him/her`. Review the whole section specifically for syntax, not just topics.

## Per-Label Diversity Targets

For `insect_bug`, include:

- Pest-control and household infestation documents.
- Garden/agriculture/extension-office material.
- Field biology, museum, specimen, and classroom material.
- Reviews and product listings for sprays, traps, nets, habitats, and reptile feeder insects.
- Informal posts, captions, chats, and kid/school fragments.
- At least a few tables, invoice rows, OCR scraps, and image alt/caption fragments.
- Rotate topics: bed bug hotel/apartment inspections, garden pests, field ID, specimen labels, school worksheets, reptile feeder insects, lake/campground mosquitoes or biting insects, farm crop scouting, product reviews, museum displays, and casual phone-photo posts.

For `software_defect_bug`, include:

- Issue tracker metadata and support tickets.
- Raw code comments, diffs, test failures, stack traces, CI logs, config, and JSON/CSV exports.
- Release notes, known issues, app store reviews, customer complaints, and developer chat.
- Security/vulnerability references where `bug` is a defect.
- Platform-specific and domain-diverse cases: mobile, web, backend, firmware, game, database, analytics, ML, localization, accessibility, payments, auth, and date/time.
- Rotate topics: login, checkout, export/import, rendering, permissions, data loss, scheduler/date bugs, memory leaks, race conditions, flaky tests, firmware, game saves, accessibility, localization, security reports, ML/data pipeline drift, and dependency regressions.

For `annoy_bother_bug`, include:

- Family and roommate texts, workplace chat, school/classroom behavior notes, retail/service complaints, advice columns, forum/social posts, moderation logs, transcript scraps, survey feedback, personal notes, and email chains.
- Structured artifacts such as CSV complaint exports, LMS comments, HR tickets, moderation queues, chat logs, support macros about harassment, notification feedback rows, and task lists.
- Rotate topics: chores, reminders, sales follow-ups, repeated questions, unsolicited advice, noisy habits, meetings, forms, spoilers, kids/siblings, coworkers, neighbors, customer service, dating/friendship boundaries, ads/notifications, and petty irritations.

## Build And Review Procedure

When generating `dsv2/samples_bug.yaml`, work in batches of about 20 per label.

After each batch:

- Scan every sample for all `" bug"` occurrences, not just standalone `bug`.
- Mark any sample with illness, covert-device, enthusiasm, vehicle, insect, software-defect, or ambiguous `bugging/bugged` usage for rewrite.
- Check that the newest batch does not lean too heavily on one opening shape such as `I found`, `The bug`, `Known bug`, or `Security found`.
- Check whether the meaning is already clear before each target occurrence. Prefer `clam shell`-style construction over `The shell is a clam`: for this token, use pre-token cues like `insect specimen`, `invoice failure`, `duplicate-tap`, `pestering`, `annoying`, `not the person to`, or `will`.
- Search for curator-style openings and rewrite them into actual source text. Bad recurring openings include `Museum catalog card`, `Triage export`, `customer transcript`, `Postmortem draft`, `campground review`, `Garden newsletter`, `Farm chat`, `QA export`, and similar stage directions.
- Add rougher artifacts if the batch is mostly polished paragraphs.
- Add longer samples if the batch is mostly one-sentence snippets.
- Move or rewrite samples where `" bug"` appears only in the first few tokens too often.
- Check that software samples include enough code/log/ticket material, insect samples include enough pest/science/commercial material, and annoyance samples include enough chats, complaints, advice, workplace, school, structured, and partial artifacts.
- Re-read the full label after each 20-sample addition, because older samples can become redundant once new ones are added.
- Run `python scripts/check_length_distribution.py dsv2/samples_bug.yaml --metric words` after substantial drafts and compare against the plan. The goal is a varied distribution, not exact bucket matching.
- For final annoyance review, search for ` bugs`, ` bugged`, and ` bugging`. In this dataset they should generally be zero in the annoyance label; use bare ` bug` instead.
- For final insect review, count `bed bug` and reduce if it rises far above about five samples.
- For final software review, scan for the repeated arc `bug -> impact -> finder -> next step`, and replace some with raw logs, customer complaints, code comments, bare changelog lists, bot output, or unresolved forum fragments.

## QA Checklist

Per sample:

- Contains exact token `" bug"` at least once.
- Contains a lowercase target occurrence; uppercase ` Bug` is not enough.
- Does not start with `" bug"` or place the first occurrence immediately at the start via a bullet, quote marker, code comment, or field prefix.
- Every occurrence of `" bug"` has the sample's target meaning, including inside longer strings.
- The local meaning is established before the target token whenever practical, not only after it.
- Avoids non-target illness, covert-device, enthusiasm, vehicle, and mixed pun senses.
- Avoids curator-style intro wrappers unless they are part of the artifact.
- Feels plausible as scraped corpus text, not a textbook example written for the dataset.
- Uses the repo's one-line quoted sample style with escaped newlines, and has valid YAML escaping and formatting.

Per meaning:

- Exactly 100 samples.
- Source types, tones, lengths, and structures are visibly varied.
- No dominant opening phrase, topic cluster, or narrative template.
- A reasonable minority of samples are messy, partial, structured, or non-prose.
- Long samples often place `" bug"` late or multiple times throughout.
- Manually inspect high-risk strings: `bed bug`, `stomach bug`, `bugging`, `bugged`, `bug report`, `bug detector`, `bug bounty`, `debug`, `ladybug`, `buggy`, `bug out`, and `travel bug`.
- Run a false-friend scan by label, plus an exact-token/missing-token scan, before calling the file final.
