# Plan: Polytok Token `" scale"`

## Objective

Create `dsv2/samples_scale.yaml` with 100 realistic samples for each meaning label:

- `climb`
- `weighing_instrument`
- `size_or_level`

Every sample must contain the exact token `" scale"` at least once. Every occurrence of `" scale"` inside a sample must match that sample's `meaning_label`.

This token is high-risk because lowercase `scale` appears as a standalone noun and verb, the start of inflected forms like `scaled` and `scales`, a field/key in code and configs, and in several unrelated meanings: fish/reptile scales, musical scales, limescale/deposits, map/rating/axis scales, weighing scales, climbing over walls or mountains, business/infra scaling, and idioms like `tip the scales`. Treat every lowercase exact occurrence seriously, including occurrences inside longer words.

## Exact-String Notes

The target is a literal space followed by lowercase `scale`.

- ` scale`, ` scale,`, ` scale.`, ` scaled`, ` scales`, ` scale-up`, ` scale-down`, ` scale-out`, ` scale_factor`, ` scaleFactor`, ` scale:` and ` scale(1.2)` contain the exact token and must be semantically correct for the active label.
- Indented keys such as `  scale: 0.75` contain the target because a space directly precedes `scale`.
- `Scale` with uppercase S, `scale` at the beginning of a sample or line without a preceding space, `.scale`, `/scale`, `_scale`, `rescale`, `upscale`, `downscale`, `limescale`, `scaling`, `scalable`, `scalability`, `scalar`, `scalene`, and `escalate` do not by themselves satisfy the exact token. They may appear as context only if another exact `" scale"` occurrence is present and all exact lowercase occurrences match the label.
- Avoid relying on token-adjacent punctuation unless the exact string is present. `("scale")` does not contain the target, but `a scale)` does.
- Do not start any sample with the target. Even if the sample begins with `scale` in the ordinary text, add realistic preceding context or choose a different excerpt.

## Realism Standard

Samples should feel like mixed C4/HPLT-style web data rather than curated examples. Use raw excerpts directly when plausible: hiking reports, climbing route notes, emergency manuals, police blotters, game text, product listings, calibration logs, lab SOPs, freight tickets, recipes, support tickets, survey exports, chart configs, CSS snippets, policy reports, forum replies, OCR/PDF text, tables, emails, and partial scraped pages.

Good data can be clipped, mundane, redundant, malformed, or surrounded by irrelevant web residue. Include plausible artifacts such as repeated headers, ad placeholders, cookie banners, broken captions, table fragments, JSON/CSV rows, timestamps, OCR line breaks, units, form labels, old nav text, moderation tags, missing context, and copied comments.

Avoid source-intro wrappers such as `climbing example:`, `scale listing:`, `the chart config says`, `snippet:`, or `weighing scale note:` unless such labels are genuinely part of the artifact. The sample should be the artifact itself, not a description of it.

## Distribution Guidance

Use approximate distributions, not exact quotas.

- Length: include a few very short fragments, many short and medium samples, and a meaningful minority of long or extra-long messy samples.
- Token placement: do not start any sample with `" scale"`. In longer samples, ensure target occurrences appear late in the sequence sometimes, not only in the first sentence or first table row.
- Token density: use enough target tokens to make the meaning clear, but avoid stuffing. Size/level and weighing-instrument samples can naturally repeat `scale`; climb samples often need fewer repetitions.
- Source mix: include technical, educational, commercial, workplace, outdoor, legal/regulatory, informal, structured, newsy, crawled/OCR, and auto-generated styles.
- Voice and tone: vary between neutral machine output, terse notes, confused humans, polished documentation, excited trip reports, frustrated support text, safety/legal boilerplate, mundane listings, and raw forms.
- Completeness: not every sample should be self-contained. Some should start or end abruptly as if scraped from the middle of a page.
- Case: the target token is lowercase `" scale"`. Uppercase `Scale` can appear for realism, but it does not satisfy the target by itself and should not be relied on.
- Near-miss control: avoid accidental fish/reptile, music, mineral-deposit, or idiomatic uses unless the active label explicitly allows them, which these three labels generally do not.

## Build Strategy

Create samples in batches of about 20 per label, then audit the entire label before adding more. Early batches should establish high-certainty core examples; later batches should deliberately fill gaps in source type, length, voice, and messiness.

For each 20-sample batch:

- Verify every exact `" scale"` occurrence by scanning manually, especially `scaled`, `scales`, and `scale:` keys.
- Check that at least several samples place the target token late, not only in the first sentence.
- Add a few structured or non-prose artifacts: CSV, JSON, code/config, tables, forms, logs, OCR, or copied webpage residue.
- Add at least one longer messy sample per label if the current label is becoming too clean.
- Remove samples that need a curator explanation to disambiguate the sense.
- Track topic clusters so the label does not collapse into only mountains, only kitchen scales, or only `large scale` business prose.

Approximate source mix targets:

- `climb`: roughly one third outdoor/mountaineering, one quarter barriers/security/incidents, one fifth games/fiction/training/obstacle courses, and the remainder animals/robots/unusual scraped artifacts.
- `weighing_instrument`: roughly one quarter household/consumer, one quarter freight/agriculture/warehouse, one quarter lab/medical/regulatory, and one quarter device/software/support/OCR/commercial miscellany.
- `size_or_level`: keep this especially spread out: no more than about one quarter `large scale`/`at scale` prose, with substantial representation from rating systems, map/model/chart/CSS scale, code/config transforms, research methods, pay/grading scales, and operational capacity.

## `climb`

Semantic rule: `" scale"` means to climb up, climb over, ascend, or get across a steep or difficult physical surface or barrier.

Good examples:

- `they had to scale the north wall before dawn`
- `the goats scale the cliff without slipping`
- `he scaled the fence behind the warehouse`
- `rescuers planned to scale the icy ridge`
- `players can scale the tower after unlocking the rope`

Include:

- Outdoor and mountaineering text: trip reports, route descriptions, accident reports, guidebook fragments, ridge/summit approaches, waterfall scrambles, quarry walls, canyon exits, glacier/ice notes, and park-service warnings.
- Barriers and built structures: fences, walls, gates, ladders, towers, scaffolding, fire escapes, border walls, stadium barriers, rooftops, prison/security reports, and obstacle-course instructions.
- Animals and robots when the sense is literal climbing: goats, lizards, insects, drones, rescue robots, climbing robots, and game NPCs that can scale walls or cliffs.
- Fiction/game/sports obstacle contexts where the physical ascent is clear: platformer walkthroughs, tabletop adventure notes, military scenarios, race obstacles, stunt reports, and training drills.
- Messy artifacts: forum posts, police blotter snippets, OCR from old climbing manuals, park PDFs, incident timelines, chat logs, field notes, product copy for crampons/rope where the target occurrence is a climb verb, and partial comments.
- Inflected exact-token forms such as `scaled` and `scales` only when they mean climbed/climbs. Example: `the team scaled the chimney`, `the runner scales the cargo net`.

Exclude:

- Size/level changes: `scale up`, `scale down`, `scaled the image`, `scale the service`, `scale factor`.
- Weighing instruments: `bathroom scale`, `truck scale`, `scale reading`.
- Fish/reptile skin plates or flakes: `fish scale`, `dragon scales`, `scale pattern`.
- Removing scales or deposits: `scale the fish`, `scale buildup`, `descale`.
- Musical scales, rating scales, map scales, pay scales, logarithmic scales, and any measurement-system sense.
- Idioms and figurative uses unless there is still physical climbing: `scale new heights` is too figurative and should be avoided for this label.

Guidance:

- Keep the label physically grounded. The reader should picture a body, animal, machine, or game character climbing a surface.
- Use both transitive forms (`scale the wall`) and past-tense forms (`scaled the cliff`), but avoid overusing heroic expedition prose.
- Long samples should not drift into `large scale` or `weighing scale` in sidebars, ads, gear specs, or page residue. Use neighboring text with words like `ascent`, `rope`, `ridge`, `fence`, `barrier`, `summit`, `cliff`, or `wall` to keep the target unambiguous.
- Avoid starting every sample with a person subject. Mix imperative instructions, incident reports, route tables, scraped comments, game code comments, transcript fragments, and terse logs.
- Be careful with `scales` as a plural noun. In this label, `scales` should be a verb meaning climbs, as in `the robot scales the wall`; avoid animal skin scales entirely.

Planned diversity dimensions:

- Surface/barrier: cliff, ridge, wall, fence, tower, cargo net, ravine exit, building facade, embankment, ship ladder, stadium barrier, ice step, canyon wall.
- Actor: hikers, rescuers, soldiers, firefighters, protesters, children, athletes, animals, robots, game avatars, fictional characters, maintenance workers.
- Source type: route notes, incident logs, news snippets, old manuals, game docs, forum posts, chats, police/security text, school obstacle-course handouts, OCR/PDF fragments, support/training materials.
- Tone: neutral report, excited trip note, confused complaint, terse instruction, dramatic fiction, safety warning, bug report, bored recap.
- Length: short clipped lines like `watched the goat scale the ledge`, medium field reports, and long scraped pages with route tables or incident timelines.

## `weighing_instrument`

Semantic rule: `" scale"` refers to a physical instrument or system used to weigh something, including its display, platform, ticket, calibration, readings, and connected software.

Good examples:

- `put the bowl on the kitchen scale`
- `the truck scale printed a 42,180 lb gross ticket`
- `calibrate the scale before weighing the samples`
- `bathroom scales vary by several pounds`
- `lab scale drift exceeded 0.02 g after warmup`
- `scale_id, tare_weight, gross_weight, net_weight`

Include:

- Household and consumer contexts: kitchen scales, bathroom scales, postal scales, luggage scales, baby scales, bathroom-weight app sync, recipe measuring, product reviews, manuals, warranty text, and return complaints.
- Industrial and commercial weighing: truck scale, weighbridge, scale house, scale ticket, cattle/livestock scale, grain elevator scale, shipping dock scale, pallet scale, crane scale, forklift scale, retail deli scale, produce scale, jewelry scale, and counting scale.
- Lab/medical contexts: analytical balance, bench scale, gram scale, specimen weighing, pharmacy compounding, calibration weights, tare/zero functions, drift checks, NIST/NTEP/legal metrology notes, clinic/veterinary weights.
- Software and hardware around the instrument: serial ports, drivers, device IDs, RS-232 output, Bluetooth sync, scale head/display, indicator, calibration log, firmware, JSON events, database rows, and error codes.
- Raw artifacts: scale tickets, CSV exports, shipping labels, calibration certificates, lab notebooks, recipe fragments, product specs, StackOverflow/device threads, maintenance logs, OCR of weigh slips, invoices, emails, and support chats.
- Inflected exact-token forms when sense-aligned: `scales` as plural weighing instruments, `scaled weight` only if the context clearly refers to a value produced by the weighing device; otherwise avoid `scaled` here.

Exclude:

- Climbing: `scale the fence`, `scaled the ridge`.
- Size/level/extent: `large scale`, `at scale`, `scale up`, `scale factor`, `pain scale`, `map scale`, `log scale`.
- Fish/reptile scales, limescale, mineral scale, musical scales, pay scales, rating scales.
- Idioms like `tip the scales`, `the scales fell from his eyes`, or `balance the scales` unless the exact occurrence is a literal weighing device, which is uncommon.
- Pure arithmetic or proportional conversion named `scale` in code/config.

Guidance:

- Make the instrument unmistakable by including units, objects being weighed, tare/gross/net language, calibration, display/reading behavior, tickets, or weighing workflow.
- This label can be especially messy and structured. Real scale data often appears as receipts, calibration logs, product tables, serial output, CSV rows, shipping screens, and copied manuals.
- Do not make all samples about kitchen scales. Include freight, agriculture, lab, retail, medical, postal, and industrial weighing.
- Avoid contexts where `scale` means a measurement system rather than the device. `the scale reads 84.3 kg` is good; `the pain scale reads 8` is not an instrument.
- In long samples, watch for accidental `large scale` boilerplate in product marketing or shipping-policy sidebars. Remove or rewrite those sidebars if they introduce the size/level sense.
- `scale ticket`, `scale house`, and `scale operator` are valid when the weighing context is clear; otherwise they can read like workplace jargon and need supporting gross/tare/net or truck/freight terms.

Planned diversity dimensions:

- Device type: bathroom, kitchen, postal, luggage, baby, veterinary, truck/weighbridge, grain elevator, cattle, pallet, crane, counting, jewelry, lab analytical, pharmacy, retail deli/produce.
- Data features: tare, zero, calibration, drift, overload, gross/tare/net, units, serial output, ticket number, operator initials, scale ID, weighing timestamp, legal-for-trade status.
- Source type: product listing, review, manual, calibration certificate, support ticket, lab SOP, shipping email, freight ticket, database row, device log, forum post, OCR receipt, app screen, maintenance checklist.
- Tone: neutral machine output, annoyed customer, practical kitchen note, regulatory language, lab precision, warehouse shorthand, confused device-driver question.
- Length: short notes like `scale read 0.00 after tare`, medium support/product excerpts, and long messy logistics/lab artifacts with multiple readings.

## `size_or_level`

Current boundary after review: this label is for scope, magnitude, extent, operating size, capacity level, and spatial/aggregation level. It includes uses like `regional scale`, `enterprise scale`, `at scale`, `production scale`, `small scale`, `city scale`, `industrial scale`, `scale of the project`, `scale of the achievement`, `economies of scale`, and `large scale study`. It deliberately excludes the neighboring measurement-system senses that user feedback flagged as too heterogeneous: map/model ratio (`map scale`, `scale bar`, `1:87 scale`, `scale model`), ordered/rating systems (`on a scale of 1 to 10`, `Likert scale`, `pain scale`), CSS/chart/UI/logarithmic scale, and the verb sense `scale up/out/down` unless the exact target occurrence is clearly a noun phrase like `enterprise scale`. The file should not test those excluded senses unless the label set is split later.

Good examples:

- `the restoration happened on a regional scale`
- `teams could not run the service at scale`
- `the survey had enough scale for rare-event analysis`
- `production scale batch notes belong with the permit file`
- `industrial scale storage needs permits, staffing, and transport`
- `the scale of the archive is hidden in the linear-feet note`
- `economies of scale show up only after the towns share one spec`
- `large scale study, n=48,102, follow-up incomplete in table 3`

Include:

- Magnitude and extent: small scale, large scale, national/global/local scale, economy of scale, scale of impact, scale of operations, production scale, industrial scale, enterprise scale, large scale study, and ordinary phrases such as `the scale of the wedding`, `the scale of the collection`, or `the scale of attendance`.
- Static scope descriptions: public events, archives, manufacturing lines, social-science samples, civic projects, retail seasons, legal discovery, finance reports, school lessons, weather coverage, and scientific aggregation units where `scale` names how broad or large the thing is.
- Operational capacity as a noun phrase: `at scale`, `enterprise scale`, `production scale`, `service scale`, `chain scale`, and similar uses are fine when they name operating size. Avoid making this label mostly about a system breaking when it grows.
- Raw artifacts: policy PDFs, grant comments, budget tables, court/OCR text, classroom worksheets, scraped news pages, product Q&A, chat logs, transcript snippets, CSV/TSV rows, archival finding aids, economic notes, manufacturing records, and technical docs in limited balance.

Exclude:

- Weighing instruments: `bathroom scale`, `truck scale`, `calibrate the scale` when physical weighing is meant.
- Climbing: `scale the wall`, `scaled the cliff`.
- Fish/reptile flakes or plates: `fish scale`, `snake scales`, `scale pattern` on an animal.
- Mineral deposits or removal: `scale buildup`, `remove scale from the kettle`, `descale`.
- Musical scales: `major scale`, `minor scale`, `chromatic scale`, `scale practice`.
- Rating/ordered scoring systems: exclude `on a scale of 1 to 10`, `Likert scale`, `pain scale`, `severity scale`, `pay scale`, `grading scale`, `risk scale`, and `color scale` for this dataset. These are real senses, but they are not the narrowed target here.
- Physical ratio/proportion examples for this revised dataset: `map scale`, `scale bar`, `scale model`, `to scale`, `full scale` when it means print/model ratio rather than operating scope.
- Visual transform/config examples for this revised dataset: `transform: scale(...)`, `scale factor`, `display scale`, canvas/UI scale, chart axis scale, log scale.
- Weapon/armor/game-item names or brands where `scale` refers to fish/dragon plates or a proper noun unrelated to size/level.
- Idioms where the sense is not magnitude or a measurement system: `tip the scales`, `scales of justice`, `the scales fell from his eyes`.

Guidance:

- This label should test scope/magnitude/capacity/extent/aggregation level, not visual, physical-ratio, or rating-system scale. It must not become a single "small pilot worked, larger rollout broke" story.
- Prefer noun phrases and static descriptions. Use verb-growth forms only as non-target context or avoid them entirely; `scale up`, `scale out`, `scale down`, and `to scale` are especially risky.
- Avoid the repeated arc "one scale level vs another scale level, report mixed them up." Some scope contrasts are natural, but the batch needs neutral descriptions, raw data, journalism, classroom text, commercial copy, legal text, everyday chats, economic notes, and clipped artifacts.
- Add static magnitude uses: journalism about actual extent, academic sample-size claims, permit language about scale of operations, economic explanations of economies of scale, casual everyday descriptions of a party/job/archive/project being larger than expected, and big/small scale descriptions that are not about a process growing.
- Be careful with `scaled` in this label. It often means visual resizing or active growth, so avoid it unless the sense is unquestionably scope/capacity and not a neighboring label.

Planned diversity dimensions:

- Extent domain: journalism, archives, education, manufacturing, public events, commerce, economics, climate, ML/research, urban planning, legal discovery, household logistics, cultural projects, and a smaller amount of software operations.
- Static magnitude types: scale of attendance, collection, operation, renovation, production, sample, audience, turnout, archive, schedule, project, cost savings, and spatial aggregation.
- Source type: clean paragraphs, clipped news, OCR/PDF residue, CSV/TSV rows, product Q&A, text chats, SRT/transcript fragments, court snippets, classroom worksheets, economic notes, finding aids, forum posts, and technical docs.
- Tone: neutral report, bored spreadsheet, confused student, annoyed customer, practical family text, dry legal phrasing, academic caution, marketing copy, terse export, and occasional warm or impressed prose.
- Length: short fragments with the token late, medium docs and comments, and a few long messy reports with tables, sidebars, comments, or repeated headings.

Second-pass rewrite targets:

- Replace at least 50 `size_or_level` samples whose target token currently means rating/map/CSS/chart/model/visual ratio.
- Remove at least 25 context-intro starts across the full dataset. A heading can remain only if it plausibly belongs to the source text; avoid narrating the artifact as `support transcript`, `chart review comment`, `field rubric`, etc.
- Add at least 10 materially longer samples across the file, with real-world clutter rather than a single tidy explanatory paragraph.
- Recheck for the "scale mismatch" template and rewrite at least 15 samples that follow the arc "X at one scale, Y at another, system/report mixed them up."

Follow-up iteration notes:

- Treat `size_or_level` as scope/magnitude/capacity/level. Do not reintroduce map/model, CSS transform, chart-axis/logarithmic, musical, fish, mineral, weighing, or climbing senses. Limited 1-10 or plain rating-level examples are acceptable now, but they should not dominate.
- Watch the section for overuse of multi-row `local scale / regional scale / national scale` comparisons. Tables are useful, but too many of them make the label feel like one template.
- Watch for the "competent operations person explains the scaling bottleneck" voice. Add confused users, marketing overclaims, angry public comments, academic fragments, news snippets, executive demands, and raw autoscaling output.
- Context labels were a major weakness in the first draft. Prefer artifact content directly; if a line starts with `report`, `memo`, `transcript`, `ticket`, `review`, `post`, `OCR`, or similar, assume it needs to be challenged.
- Word-length distribution should stay near the improved balance: mostly short/medium, a small long tail, no cluster of tiny fragments, and no padded explanatory endings.

## Cross-Label Collision Rules

- If a sample contains more than one exact `" scale"` occurrence, every one must match the label. A good weighing sample cannot contain `large scale rollout`; a good size/level sample cannot contain `truck scale`; a good climb sample cannot contain `scaled image`.
- Avoid fish/reptile, mineral-deposit, and music senses entirely unless they appear without the exact lowercase target. They are not among the requested labels and will pollute the data.
- Be wary of `scales`:
  - `the runner scales the wall` is `climb`.
  - `the bathroom scales need batteries` is `weighing_instrument`.
  - `rating scales vary by survey` is excluded in this narrowed pass, even though it is a common measurement-system sense.
  - `fish scales` and `major scales` are excluded.
- Be wary of `scaled`:
  - `scaled the fence` is `climb`.
  - `scaled deployment` is `size_or_level`.
  - `scaled the image` is excluded in this narrowed pass because it is visual transformation/ratio, not operational scope.
  - `scaled weight` should usually be avoided unless explicitly produced by a weighing device and not a normalized value.
- Be wary of `scale:` in configs:
  - chart/CSS/game transform values are excluded in this narrowed pass.
  - device fields like `scale_id`, `scale_port`, or `scale_reading` can be `weighing_instrument` only with weight-device context.
  - a route or climbing-game config using `can scale wall` can be `climb`, but `scale:` as a numeric transform is not.
- Prefer replacing non-target hyphenated/compound near-misses instead of trying to explain them away.

## QA Checklist

Per sample:

- Contains exact token `" scale"`.
- Every exact occurrence has the target meaning.
- Does not start with the token, and usually does not place it extremely early.
- Avoids source-intro wrappers unless the wrapper is genuinely part of the raw text.
- Is plausible as web/SFT corpus text, not a meta-example about the label.
- Is valid YAML.

Per meaning:

- Exactly 100 samples.
- Lengths, token counts, source types, tones, and formats are visibly varied.
- No dominant opening pattern, topic cluster, or narrative template.
- Includes rough/partial/crawled material without making artifacts theatrical.
- Includes short, medium, and long samples, with some target occurrences late in long samples.
- Manually inspect high-risk cases: `scales`, `scaled`, `scale up/down`, `scale ticket`, `scale house`, `scale bar`, `log scale`, `pain scale`, `scale model`, `scale factor`, `scale:` config keys, `fish scales`, `major scale`, `scale buildup`, and `tip the scales`.

## Third-Pass `always_check.md` Answers

1. Correct, unambiguous meaning? Mostly yes after the third pass. The biggest risk is now allowed-but-rare level/rating usage like `on a scale of 1 to 10`; these must remain clearly in `size_or_level` and not drift into specialist survey-scale dominance.
2. Diversity and messiness? Better, but still not perfect. The reference `samples_-.yaml` is messier than this file, especially in raw HTML/code/table fragments and abrupt starts. Third pass added more of that, mainly to `size_or_level`.
3. Adequately dirty? Improved. Added article corrections, executive chat, app review, legal fragment, HPA output, alert email, HTML recall fragment, classroom board, insurance sheet, and more clipped climb/weighing artifacts. Still could tolerate even more malformed web residue.
4. Voice diversity? Much better in `size_or_level`: marketing, executives, angry residents, confused users, students, journalists, researchers, analysts, and raw automation now appear. Residual risk: some operations voice remains.
5. Introductory phrases avoided? Better. Some real-ish artifact starts remain (`app store review`, `grant portal title`, `airport launch checklist`), but they act like source text rather than curator narration. Continue challenging any start that only labels the artifact.
6. Length diversity? Acceptable but fragile. The messier rewrites shortened the size section, so later checks must watch short/medium balance.
7. Starts with token? Must be zero. One third-pass sample briefly started with `scale`; it was corrected to `insurance sheet column: scale of loss`.
8. Repetitive arcs? The old "small worked, big scale broke because staffing/manual approvals/freezer space" arc is substantially reduced. It is not gone, but no longer defines the whole size section.
9. Abrupt/mid-page starts? Improved with clipped HTML, logs, fragments, comments, and partial exports. More could still be added in future passes.
10. Not only natural language? Improved. Size now has Terraform, alerts, HPA output, CSV, HTML, dashboard cards, legal/OCR snippets, and classroom exports; weighing and climb already had structured artifacts.
11. Tone variation? Improved. There is now frustration, confusion, hype, bureaucratic flatness, academic caution, and terse automation.
12. Domain balance? Better. Size still leans civic/service/software, but academic, legal, media, economics, insurance, recall, airport, franchise, and public-comment examples reduce the old cluster.
13. Final meaning recheck? Required after every rewrite. Especially scan for map/model/CSS/log/chart scale, weighing scale, climbing scale, fish/music/mineral senses, and accidental `scale` at sample start.

## Fourth-Pass `always_check.md` Re-Answers

Latest audit after the extra rewrite pass: 300 samples total; 100 per label; zero case-sensitive missing lowercase `" scale"` occurrences; zero samples starting with `scale`; zero automated hits for excluded `size_or_level` senses. Word buckets are now close across labels: `size_or_level` has 45 short, 53 medium, 2 long; `climb` has 52 short, 45 medium, 3 long; `weighing_instrument` has 50 short, 48 medium, 2 long.

1. Correct, unambiguous meaning? Yes on the automated and manual pass. `size_or_level` is now consistently scope/magnitude/capacity/level. I explicitly fixed the case-sensitive exact-token issue where lowercase `scale` appeared only at the start of an internal line or as uppercase headline text.
2. Diversity and messiness? Much better than the first and third passes. The section now has cached pages, FOIA/audit fragments, dashboards, board exports, court/legal snippets, config/alert output, CSV-ish artifacts, public comments, and article corrections. Still not as wildly varied as `samples_-.yaml`, but much closer.
3a. Adequately dirty / unique messy data? Improved materially. Added web footer bleed, cookie banners, hidden columns, OCR/page-order errors, broken attachments, mobile preview artifacts, copied speaker notes, missing fields, and stale cached copies. Harsh note: some mess is still a little designed; future passes could add more genuinely abrupt non-sequitur scraping.
3b. Voice diversity beyond competent explainer? Stronger. The weakest old voice was the calm operator explaining why growth failed. I replaced many of those with confused readers, public commenters, students, executives, reviewers, journalists, finance notes, automated alarms, and raw table fragments. Some competent-analysis voice remains where it is natural for the domain.
4. Token position and density? Acceptable. No sample starts with the token. Some short structured rows place `scale` early, but that is realistic for table fields and headings. Long samples still include late target occurrences, especially in climb/weighing and the longer `size_or_level` board/planning artifacts.
5. Introductory phrases avoided? Better, but not perfect. I challenged many source-label starts and left only those that plausibly occur in scraped artifacts (`CloudWatch alarm history`, `budget hearing p.18 OCR`, `newsletter export`). Harsh note: a few are still cleaner than raw web would be.
6. Length diversity? Acceptable after repair. The fourth pass briefly made `size_or_level` too short-heavy, then I lengthened selected artifacts. Long tail is modest but present; no very-short samples remain.
7. Starts with token? Verified zero. Also verified case-sensitive lowercase exact `" scale"` is present in every sample, not merely uppercase `Scale` or line-initial `scale`.
8. Repetitive arcs/templates? Much improved. The old "small worked, big broke because staffing/weekend/manual approvals" arc no longer dominates. Vocabulary audit dropped `queue` to 4, `support` to 3, `weekend` to 3, `manual` to 1, and `approvals` to 0 in `size_or_level`. Residual multi-scale tables remain, but they are no longer the only shape.
9. Abrupt/mid-page starts? Improved. Several samples now begin in the middle of exports, scraped pages, CSV rows, cached newsletters, and clipped transcripts. More abrupt endings could still be useful later.
10. Not only natural language? Pass. There is raw-ish Terraform/HPA/CloudWatch/load-test output, CSV, HTML, court/OCR text, table fragments, forms, dashboards, batch records, field notes, and chat/log text across labels.
11. Tone and emotional register? Better balanced: neutral bureaucratic prose remains common, with bursts of frustration, hype, confusion, dry reviewer language, student uncertainty, and terse automation. Harsh note: neutral still dominates, which is realistic but can make clusters feel flatter.
12. Topic/domain balance? Improved. `size_or_level` still leans civic/service/software because the requested sense naturally does, but now includes economics, research, journalism, legal discovery, disaster reporting, manufacturing, ML, airport, franchise, newsletter, libraries, planning, finance, and public health.
13. Final meaning recheck? Passed after the latest rewrite. I scanned especially for map/model/CSS/log/chart scale, weighing scale, climbing scale, music/fish/mineral senses, and exact-token casing. No automated excluded-sense hits remain.

## Fifth-Pass Opening Diversity Note

After the fourth-pass answers, I made one more general messiness pass outside `size_or_level`. The goal was not semantic change; it was to reduce polished sentence-openers and curator-like prose in `climb` and `weighing_instrument`.

- `climb` starts with `The` dropped from 30 to 20.
- `weighing_instrument` starts with `The` dropped from 26 to 15.
- `size_or_level` stayed stable at 100 samples with 45 short, 53 medium, 2 long after the final style pass.
- Rechecked YAML parse, label counts, case-sensitive exact lowercase `" scale"` presence, and no sample starts with `scale`.
- Added a stricter standalone-word check for `" scale\b"` after noticing that `scaled` can satisfy a loose substring check. One climb sample was repaired from `scaled the fence` to `had to scale the fence`.

Harsh residual note: the file is much less patterned now, but it is not maximally messy. Some artifact headers remain because they are plausible source text; future rounds could replace more of them with mid-page fragments if the dataset still feels too clean in review.

## Sixth-Pass `size_or_level` Rebalance

User feedback identified a new dominant pattern: "someone says X scale, someone else says the evidence does not support X scale." This was real. The fifth-pass version had overcorrected from operational-failure memos into scale-claim disputes, especially marketing/legal/comms/reviewer fragments.

Actions taken:

- Replaced many claim-vs-reality samples with neutral noun/level uses: geography worksheet, economics chapter review, construction permit, earth systems lecture, compost tonnage report, aquaculture manual, field experiment methods, history textbook, public health glossary, chemistry handout, ecology supplement, clinic 1-10 form, river basin paper, nursing textbook case, tenant support schedule, retail/portfolio guides, and model-card scale definitions.
- Removed most narrow autoscaler/Kubernetes context from `size_or_level`. Final scan for autoscaler/Kubernetes terms returned zero hits.
- Reduced verb "to scale" uses in `size_or_level`. Final scan for patterns such as `to scale`, `do not scale`, `scale up/out/down`, and `scaled from/to` returned zero hits.
- Repaired two case-sensitive exact-token failures caused by uppercase `Scale` or line-start `scale`.
- Rebalanced length after the rewrite: `size_or_level` ended at 49 short, 50 medium, 1 long by word buckets, with no very-short samples; by character buckets it retained a long tail.
- Follow-up cleanup removed remaining verb-like or ambiguous exact contexts: `scale-up`, `could not scale to regional`, `how to scale your CSA`, `scaled from`, and a noisy `remodel scale` near-miss that could be confused with `model scale`.
- Follow-up scans returned zero hits for `size_or_level` autoscaler/Kubernetes terms, zero hits for verb-scale patterns, zero starts-with-token, and zero missing standalone lowercase `" scale\b"` occurrences.

Harsh current assessment: this pass substantially fixes the user's main objection. The section is now much more about actual size, scope, level, spatial scale, measurement level, and scale-dependent behavior without constant accusation/overclaim dynamics. Residual risk is that `size_or_level` still has fewer very long messy examples than the other sections and still has some civic/service contexts, but it no longer reads like one workplace argument.

## Seventh-Pass Cleanup Note

After random sampling, I removed a few remaining borderline samples that still smelled like the old argument pattern or verb-resize sense:

- Replaced public-comment/wording-dispute wording with a truck-count appendix.
- Replaced recall wording conflict with a plain recall-scale HTML fragment.
- Removed `scale-up` compounds from manufacturing examples.
- Replaced `could not scale to regional resource requests` with a noun/scope comparison.
- Replaced `scale support carefully` with a refund-policy table where scale is volume/magnitude.
- Replaced an M&A scale-language caution with a neutral enterprise-scale integration inventory.
- Rewrote the industrial planning example to avoid "brochure says" argument framing.
- Removed explicit `chart-axis` wording from a math methods handout.
- Removed a slogan-like `we scale with care` occurrence from a kitchen/warehouse sample so every exact occurrence stays noun/scope rather than verb marketing copy.
- Repaired a corrupted OCR occurrence `scale nsk`, which was not semantically clean, while preserving a valid `main scale risk` target occurrence.

Post-cleanup scans:

- Zero missing standalone lowercase `" scale\b"`.
- Zero samples starting with `scale`.
- Zero `size_or_level` autoscaler/Kubernetes hits.
- Zero `size_or_level` verb-scale hits for the checked patterns.
- Zero excluded near-miss hits for map/model/CSS/log/chart-axis/scale-factor patterns.

Latest distribution after the seventh pass:

- Word buckets: `climb` 55 short / 42 medium / 3 long; `size_or_level` 49 short / 50 medium / 1 long; `weighing_instrument` 52 short / 46 medium / 2 long.
- Character buckets: `size_or_level` has 1 short / 96 medium / 3 long, so the section still has longer messy artifacts even though only one crosses the word-count long threshold.

## Eighth-Pass `size_or_level` Deep Rebalance

User feedback after the seventh pass identified a newer failure mode: the section was no longer mostly "small worked, big broke", but it had drifted into too many tiered scope lists, planning documents, and institutional-professional samples. I reread `always_check.md`, sampled `dsv2/samples_-.yaml` again for messiness, and then did another targeted pass.

Actions taken:

- Replaced 27 `size_or_level` samples, prioritizing tiered lists, economics/economies language, planning-packet prose, vendor-deck fragments, training dashboards, and institutional checklists.
- Removed the ambiguous phrase `commercial kitchen scale`, which could collide with weighing-instrument language, and changed it to `cafeteria scale`.
- Replaced the very long planning-packet appendix with a long messy live-blog disaster sample, keeping a long tail without another bureaucratic multi-scale planning artifact.
- Added more casual/non-institutional voices: group text, product Q&A, recipe comments, neighborhood comments, teacher comments, waiting-room whiteboard, coffee-shop review, public live blog, hobbyist post, and product/help-page fragments.
- Removed the remaining explicit `economies of scale` sample in this section to avoid the economics submeaning taking over.
- Reduced metalinguistic exact-token pollution by changing lines such as `word scale`, `scale joke`, `scale note`, and `skill instead of scale` so the only exact lowercase occurrences carry the active size/level meaning.
- Repaired an overcorrection in length: after the large replacement pass, `size_or_level` became 82 short / 16 medium / 2 long by word buckets. I lengthened selected samples with realistic residue, ending at 60 short / 38 medium / 2 long.
- Removed many source-intro first lines by starting samples inside the artifact: e.g. directly at counts, questions, table rows, or paragraphs rather than `worksheet scan`, `draft`, `transcript`, or `note`.
- Pushed early token placements later in several samples; a follow-up scan found no `size_or_level` first occurrence of `" scale"` within the first 12 characters.

Post-pass scans:

- 300 total samples; 100 per label.
- Zero missing exact lowercase `" scale"` substring.
- Zero missing standalone lowercase `" scale\b"` occurrence.
- Zero samples starting with `scale`.
- Zero `size_or_level` excluded-sense hits for map/model/CSS/log/chart-axis/weighing/climbing/fish/music/mineral patterns.
- Zero `size_or_level` verb/autoscaler hits for checked `scale up/out/down`, `to scale`, Kubernetes/HPA/Terraform/CloudWatch patterns.
- Word buckets: `climb` 55 short / 41 medium / 4 long; `weighing_instrument` 52 short / 45 medium / 3 long; `size_or_level` 60 short / 38 medium / 2 long.
- Character buckets from `scripts/check_length_distribution.py`: `size_or_level` 27 short / 71 medium / 2 long, close to `climb` and `weighing_instrument`.

Harsh residual assessment: `size_or_level` is much better, but still naturally has more institutional residue than the other labels because scope/magnitude language often appears in reports, studies, public notices, and dashboards. The current section is no longer one workplace argument or one tiered-list template, but some artifact labels remain because the reference sample itself includes real headers and scraped labels. The weakest remaining cluster is civic/public-service magnitude: disaster, clinic, housing, transit, tenant, county, school, and utility examples still appear often. I think that cluster is acceptable now because the voices and source shapes vary, but it is the first place I would trim in a future pass.

## Eighth-Pass `always_check.md` Answers

1. Correct, unambiguous meaning? Yes on the current pass. I specifically removed ambiguous weighing-adjacent `kitchen scale`, autoscaling/verb-growth hits, and metalinguistic exact-token leftovers.
2. Diversity/messiness? Much improved. The section now includes casual chats, live blogs, product Q&A, comments, whiteboards, classroom scraps, HTML, CSV-like rows, legal text, research fragments, and newsy excerpts.
3. Adequately dirty? Better, though not perfect. There are cookie banners, broken mobile pages, OCR issues, duplicate attachments, missing fields, stale screenshots, hidden table rows, ad insertions, and cropped images. Harsh note: some dirt is still authored rather than truly chaotic.
4. Voice diversity? Improved. More confused users, parents, students, public commenters, shoppers, teachers, moderators, patients, and casual reviewers; fewer calm operations explainers.
5. Introductory phrases avoided? Better after removing many explicit source labels, but not zero. Some starts like `seller forum cached page` and `product page Q&A` remain because they are plausible scraped headers. This is still a residual weakness.
6. Length diversity? Good after repair. `size_or_level` was over-shortened, then rebalanced to 60/38/2 by word buckets and 27/71/2 by character buckets.
7. Starts with token? Verified zero. Also checked early placement; no `size_or_level` first occurrence appears in the first 12 characters.
8. Repetitive arcs/templates? Much reduced. The old "worked small, broke big", "scale claim vs reality check", and tiered `local/regional/national scale` list patterns are no longer dominant. Some contrast samples remain because the meaning often needs scope contrast.
9. Abrupt/mid-page starts? Improved. Several samples now start at timestamps, table rows, whiteboard entries, questions, fragments, or copied paragraphs.
10. Not only natural language? Pass. The file includes code/config-like rows, CSV-ish exports, HTML, forms, logs, OCR, calibration data, route/status records, and tables across labels.
11. Tone variation? Better. Neutral still dominates, but there is frustration, sarcasm, classroom confusion, customer irritation, emergency reporting, dry legal phrasing, casual texting, and product-copy flatness.
12. Topic/domain balance? Better but not flawless. Civic/service contexts are still the main residual cluster; however, size now also includes science, education, ecommerce, food, consumer products, legal, ML, retail, astronomy, history, and personal messages.
13. Final meaning recheck? Passed in the latest scans. Remaining high-risk exact forms were manually challenged: `scale of`, `at scale`, `on a scale`, `large scale`, `spatial scale`, `scale_bucket`, and table/config-adjacent uses.

## Ninth-Pass Neutral-Magnitude Rework

User feedback identified two remaining issues:

- The `size_or_level` section still had too many samples with the narrative arc "something looked manageable at small scope, but at this scale it becomes a problem, then a web artifact interrupts."
- The `on a scale of 1 to 10` / rating-scale samples were probably not the intended sense for this label and should be replaced.

Actions taken:

- Removed all `on a scale`, `scale from 1`, `scale of 1`, and `1 to 10` usages from `size_or_level`.
- Replaced the rating-scale samples with neutral scope/magnitude artifacts: basement inspection extent, watershed project scope, exhibition size, concert exit scale, clinic study scale, and discharge-translation tracker scale.
- Reworked roughly two dozen "surprise, this gets worse at scale" samples into neutral counts, summaries, tables, logs, or descriptions: route cards, contact-tracing coverage, festival traffic totals, subscription-box station counts, warehouse rate/count table, industrial storage description, app inventory, campaign totals, clinic whiteboard counts, state tablet deployment, library hold counts, refund-desk forecast, paratransit daily log, portfolio view, crew map layers, and benchmark size.
- Replaced `bench scale run` with `small scale run` to avoid weighing-instrument ambiguity.
- Reduced repeated `At this scale` / `at that scale` phrasing where it was easy to rewrite neutrally.

Post-pass scans:

- YAML parses; 3 labels with 100 samples each.
- Zero missing exact lowercase `" scale"` substring.
- Zero missing standalone lowercase `" scale\b"` occurrence.
- Zero samples starting with `scale`.
- Zero `size_or_level` rating-scale hits for `on a scale`, `scale from 1`, `scale of 1`, or `1 to 10`.
- Zero `size_or_level` excluded-sense hits for map/model/CSS/log/chart-axis/weighing/climbing/fish/music/mineral patterns.
- Zero `size_or_level` verb/autoscaler hits for checked `scale up/out/down`, `to scale`, Kubernetes/HPA/Terraform/CloudWatch patterns.
- Word buckets after the pass: `climb` 55 short / 41 medium / 4 long; `weighing_instrument` 52 short / 45 medium / 3 long; `size_or_level` 69 short / 29 medium / 2 long.
- Character buckets after the pass: `size_or_level` 22 short / 76 medium / 2 long, with average character length close to the other labels.

Harsh `always_check.md` re-answer:

1. Correct meaning? Better. Rating-scale usages are gone. Exact lowercase occurrences in `size_or_level` now consistently express scope, magnitude, extent, operational size, or spatial/aggregation scale.
2. Diversity/messiness? Improved again. The replacements add more neutral tables, logs, posters, trackers, chat snippets, product/review snippets, and static count summaries.
3. Dirty data? Pass but not maximal. There are still plausible artifacts, footers, stale screenshots, shifted tables, wrong figure numbers, missing rows, and OCR/page-order issues.
4. Voice diversity? Better. More neutral descriptive fragments and fewer frustrated "this broke at scale" explainers.
5. Intro phrases? Still not perfect. Some artifact headings remain, but fewer samples begin by narrating the source rather than being the source.
6. Length diversity? Acceptable. Word buckets skew short after replacing long complaint arcs, but character buckets remain balanced and the section still has a long tail.
7. Starts with token? Verified zero.
8. Repetitive arcs? Much improved. The "looks manageable, but at scale it is bad" arc is now present only in isolated natural cases, not as a dominant section skeleton.
9. Abrupt/mid-page starts? Maintained with table rows, log fragments, copied chats, cached pages, and clipped pages.
10. Non-natural language? Pass. There are CSV-like fields, HTML, tables, logs, trackers, notebook output, and scraped-page fragments.
11. Tone variation? Better balanced toward neutral web text, with some casual, annoyed, bureaucratic, and academic voices.
12. Topic/domain balance? Improved, but civic/service examples still remain a visible cluster. The section now has more consumer, education, science, retail, product, concert, and benchmark contexts.
13. Final semantic recheck? Passed scans for rating-scale, excluded senses, verb/autoscaler uses, starts-with-token, and exact-token presence.

## Tenth-Pass Natural-Use And Clean-Paragraph Rework

User feedback identified three remaining problems in `size_or_level`:

- Too many first-half samples had the unnatural `[modifier] scale [noun/count]` feel.
- The "scale of a bad thing" subtype was still too visible.
- Artifacts were too omnipresent; the clean paragraph ratio needed to be higher.

Targeted sequence sets:

- Structural monotony: reworked samples 7, 9, 12, 16, 22, 24-27, 30-39, 41, 44, 48, 50, 53-55, 57-62, 64-65, 67-71, 74-75, 79-80, 83, 85-88, 90, 94-97, 99-100. These removed or softened many `At X scale`, `X scale count`, `X scale summary`, and `X scale: numbers` shapes.
- Bad-event/magnitude subtype: replaced or reframed samples 16, 22, 25, 44, 67, 70, 74-75, 80, 90, and several nearby samples so the section now includes more school musical, exhibition, trade, birthday, warehouse, soup, bakery, solar co-op, terminal, museum, fair, pricing, and restoration uses.
- Artifact saturation: converted many source-labeled fragments into clean paragraphs, especially samples 22, 24-27, 30-39, 44, 48, 50, 53-55, 57-62, 64-65, 67-71, 74-75, 79-80, 83, 85-88, 90, 95, 99-100. A small amount of artifact/source texture remains intentionally.
- Follow-up fixes removed one `factory floor scale` false neighbor, one awkward `returning to scale` phrase, the remaining `scale:` colon in the long restoration sample, and several leftover `state/route/county/portfolio/benchmark scale` starts.

Post-pass checks:

- YAML parses; 3 labels with 100 samples each.
- Zero missing exact lowercase `" scale"` substring.
- Zero missing standalone lowercase `" scale\b"` occurrence.
- Zero samples starting with `scale`.
- Zero `size_or_level` rating-scale hits for `on a scale`, `scale from 1`, `scale of 1`, or `1 to 10`.
- Zero `size_or_level` excluded-sense hits for map/model/CSS/log/chart-axis/weighing/climbing/fish/music/mineral patterns.
- Zero `size_or_level` verb/autoscaler hits for checked `scale up/out/down`, `to scale`, Kubernetes/HPA/Terraform/CloudWatch patterns.
- Zero hits for the checked bad-event cluster: disaster, damage, flood, mold, contamination, layoff, outage, hunger, wildfire, fault, absences, duplicate records, mess, storm, crisis.
- Zero `size_or_level` `scale:` colon hits.
- Remaining explicit source-intro artifact starts in `size_or_level`: 6. This is now a minority rather than the dominant texture.
- Character buckets from `scripts/check_length_distribution.py`: `size_or_level` 0 very short / 30 short / 69 medium / 1 long, avg 292.9 chars. This is now closer to the other labels.
- Word buckets: `size_or_level` 58 short / 42 medium / 0 long, avg 48.0 words. Harsh note: word-count long tail is still weaker than character-length long tail.

Harsh `always_check.md` re-answer:

1. Correct meaning? Yes. The section now stays on scope, magnitude, extent, operational size, or spatial/aggregation scale. I removed the remaining `factory floor scale` false neighbor and the `to scale` scan hit.
2. Diversity/messiness? Better balanced. Clean paragraph prose is now much more common, with a smaller residue of chats, listings, orders, wiki/search results, and cached help pages.
3. Adequately dirty? Adequate but deliberately less dirty than before. The earlier file overdid broken artifacts; now the dirty samples stand out more naturally.
4. Voice diversity? Improved. The pass added or strengthened school, museum, recipe, concert, textbook, warehouse, bakery, co-op, dispatch, retail, finance, pricing, and planning voices.
5. Introductory phrases avoided? Much improved, but not perfect. Six `size_or_level` samples still start with source-ish text; I kept these because a fully clean section would be unrealistic too.
6. Length diversity? Acceptable by character distribution; weaker by word buckets. I lengthened many clean paragraphs after noticing the first rewrite got too short-heavy.
7. Starts with token? Verified zero.
8. Repetitive arcs/templates? Much improved. The old `modifier scale: counts` skeleton no longer appears in `size_or_level` scan results, and `scale of a bad thing` is no longer a visible cluster.
9. Abrupt/mid-page starts? Still present, but less dominant. This is now closer to the reference file's balance.
10. Not only natural language? Pass. There are still structured/legal/app/research/listing/chat fragments across the label, while clean paragraphs now have a healthier share.
11. Tone variation? Better. Neutral prose dominates, with some amused, practical, promotional, academic, procedural, and casual samples.
12. Topic/domain balance? Better than before. Civic/service contexts remain, but positive and neutral domains now include music, archives, murals, travel, exhibitions, trade, parties, warehouses, recipes, bakeries, solar purchasing, terminals, museums, fairs, pricing, portfolios, and restoration.
13. Final semantic recheck? Passed all current scans: exact token presence, standalone token presence, no token starts, no rating-scale patterns, no excluded senses, no verb/autoscaler patterns, no bad-event keyword cluster, no `scale:` colon residue.

## Eleventh-Pass Technical/Register And Token-Placement Rework

User feedback identified four newer issues in `size_or_level`:

- The target word appeared extremely early in many samples, often in `The scale...` starts.
- Register had collapsed into warm narrative prose about local programs, community events, and institutional growth.
- Technical/code/data contexts were underrepresented relative to real uses of size/scope `scale`.
- Emotional register was too admiring and too often followed the arc "project/event grows, concrete details, human observation."

Actions taken:

- Reread `always_check.md` before editing, especially questions 1, 4, 5, 8, 10, 11, and 12.
- Reworked more than 60 `size_or_level` sequences across multiple passes.
- Token-placement pass:
  - Initial audit found 54 `size_or_level` samples with first `" scale"` before character 35, 89 before character 60, and 10 samples starting `The scale`.
  - Final audit has 0 before character 35, 0 before character 60, 8 before character 80, median first-token position 118, and 0 `The scale` starts.
- Register/diversity pass:
  - Replaced much of the warm civic/community prose with SQL, warehouse jobs, README/perf notes, API docs, cloud invoices, RF survey notes, postmortems, search docs, privacy queues, ticketing exports, pricing Slack, object-store inventory, dashboard copy, lab notebooks, trial registry edits, court orders, CDN migration notes, query-planner comments, model-card review, and incident appendices.
  - Reduced the old local-program cluster to a small residue, with a rough keyword scan returning 0 hits for the previous warm-local cluster terms.
  - Added more frustrated, bored, procedural, clinical, legal, and annoyed commercial voices.
- Structural pass:
  - Removed remaining `reached a scale` growth arcs except false-positive wording like `not app growth`.
  - Replaced `platform scale` because it is a software phrase here but too close to the weighing-instrument submeaning.
  - Rewrote several `The X says/explains...` narrator phrases into direct fragments.
- Length repair:
  - The first technical rewrite made the section too clipped, so I lengthened roughly thirty technical/dry samples with realistic residue: comments, bad captions, reviewer notes, stale screenshots, missing metadata, status fields, and failed imports.
  - Added long-tail weight to the messy research appendix and batch-scoring incident appendix.

Post-pass checks:

- YAML parses; 3 labels with 100 samples each.
- Zero missing exact lowercase `" scale"` substring.
- Zero missing standalone lowercase `" scale\b"` occurrence.
- Zero samples starting with `scale`.
- Zero `The scale` starts in `size_or_level`.
- First `" scale"` position in `size_or_level`: 0 before char 35, 0 before char 60, 8 before char 80, median 118.
- Zero `size_or_level` rating-scale hits for `on a scale`, `scale from 1`, `scale of 1`, or `1 to 10`.
- Zero `size_or_level` excluded-sense hits for map/model/CSS/log/chart-axis/weighing/climbing/fish/music/mineral patterns and the old false-neighbor patterns.
- Zero `size_or_level` verb/autoscaler hits for checked `scale up/out/down`, `to scale`, Kubernetes/HPA/Terraform/CloudWatch patterns.
- Zero `size_or_level` `scale:` colon hits.
- Character buckets from `scripts/check_length_distribution.py`: `size_or_level` 0 very short / 26 short / 73 medium / 1 long, avg 293.3 chars.
- Word buckets: `size_or_level` 80 short / 18 medium / 2 long, avg 45.2 words.
- Rough overlapping context scan after edits: code/log/data 47, casual/forum/review 33, business/legal 30, academic/science 27, civic/ops 17.

Harsh `always_check.md` re-answer:

1. Correct meaning? Yes. The exact token in `size_or_level` now consistently means scope, magnitude, extent, operational size, aggregation level, or spatial scale. I removed `platform scale` as a risky false neighbor.
2. Diversity/messiness? Much better. The section now has logs, SQL, configs, docs, invoices, dashboards, court/OCR, scientific methods, Slack/forum fragments, product reviews, and support pages.
3. Adequately dirty? Better than the warm clean pass. Dirt now comes from realistic technical and scraped residue rather than constant broken-page decoration.
4. Voice diversity? Stronger. There are annoyed customers, finance reviewers, legal/court text, clinical/statistical caution, support macros, bug reports, terse logs, forum crankiness, and neutral documentation.
5. Intro phrases? Improved but not perfect. File/log headers remain, which is natural for technical/data contexts; I removed several curator-like narrative phrases.
6. Length diversity? Acceptable by character distribution and improved long-tail; still harshly weak by word buckets because many logs/config fragments are compact.
7. Starts with token? Verified zero.
8. Repetitive arcs/templates? Much improved. The old warm growth arc and `The scale of...` starts are gone as dominant structures.
9. Abrupt/mid-page starts? Yes. Many samples now start in logs, exports, comments, OCR, config, or copied support text.
10. Not only natural language? Pass. Technical/code/data contexts are now strongly represented; perhaps slightly high, but this corrects the prior underrepresentation.
11. Tone variation? Much better: bored, clinical, annoyed, dry, procedural, skeptical, and only lightly warm in a few places.
12. Topic/domain balance? Much better. There is no longer a dominant community-program register, though code/log/data may now be the largest single family.
13. Final semantic recheck? Passed exact-token, standalone-token, token-start, rating-scale, excluded-sense, verb/autoscaler, and `scale:` scans.

## Twelfth-Pass Active Cooldown Cleanup

After the eleventh pass, I continued active review rather than stopping at the first clean metrics. This pass targeted smaller patterns introduced by the technical rewrite:

- Reduced the `scale is` / `at this scale` / `at that scale` wording cluster.
- Removed one accidental `scale:` colon introduced in an event-rental sample.
- Repaired one sample that briefly lost a standalone lowercase `" scale"` after a rewrite.
- Replaced awkward coined compounds:
  - `travel-day scale`
  - `bulk-service scale`
  - `plant-opening scale`
  - `recreation-center scale`
  - `multi-million-object scale`
  - risky `full scale`
  - odd `world scale`
- Reduced `enterprise scale` from 6 occurrences to 4.
- Lengthened additional clipped samples while preserving terse/log-like register.

Latest checks after the active cleanup:

- Zero missing exact lowercase `" scale"` substring.
- Zero missing standalone lowercase `" scale\b"` occurrence.
- Zero samples starting with `scale`.
- Zero first `" scale"` positions before character 60; only 5 before character 80; median first-token position 126.
- Zero `at this scale`, zero `at that scale`, zero `scale is`, zero `scale:` in `size_or_level`.
- Zero rating-scale hits, zero excluded-sense hits, zero verb/autoscaler hits.
- Character buckets from `scripts/check_length_distribution.py`: `size_or_level` 0 very short / 10 short / 88 medium / 2 long, avg 308.3 chars.
- Word buckets: `size_or_level` 70 short / 28 medium / 2 long.

Harsh residual note:

The `size_or_level` section is much less warm and much less front-loaded than before. The remaining weakness is that the technical/log/data family is now the largest family; however, this is a deliberate correction to the prior underrepresentation, and the section still includes academic, legal, commercial, support, civic, educational, review, and forum contexts. I would not push further toward warm prose again.

## Thirteenth-Pass Boundary And Register Rework

Latest user feedback said `size_or_level` was still dominated by a calm technical narrator, organizational/operational memos, and the recurring "small/test scale is fine, real scale breaks it" arc. It also raised the label-boundary question around map/model ratios and Likert/rating systems.

Boundary decision:

- Keep `size_or_level` narrowed to scope, magnitude, extent, operating size, capacity level, and spatial/aggregation level.
- Exclude map/model ratio, rating/Likert/pain/pay/severity scales, CSS/chart/log/UI transforms, weighing instruments, climbing, and active verb-growth phrases like `scale up/out/down` for this dataset. These are real meanings, but earlier review found that including them makes the label internally heterogeneous.

Actions taken:

- Updated the plan's `size_or_level` semantic boundary so it no longer permits `on a scale of 1 to 10`, map/model ratio, CSS/chart/log scale, or verb-growth examples as target uses.
- Reworked roughly fifty `size_or_level` samples, replacing many technical narrator and ops-memo entries with everyday texts, journalism, classroom fragments, product Q&A, economics notes, OCR/legal text, chat logs, archive/finding-aid language, event copy, SRT transcript, survey/table snippets, and clean paragraphs.
- Removed new `scale:` punctuation leaks introduced during the pass.
- Reduced the remaining enterprise/production-doc cluster by replacing several pricing/new-hire/support-style entries with arts, publishing, event, and property-listing contexts.
- Rebalanced from highly technical/log-heavy toward a broader mix while preserving some technical, academic, legal, and data artifacts.

Latest checks:

- YAML parses; 3 labels with 100 samples each.
- Zero missing exact lowercase `" scale"` substring.
- Zero missing standalone lowercase `" scale\b"` occurrence.
- Zero samples starting with `scale`.
- `size_or_level` first-token placement: 3 samples before character 60, 12 before character 80, median first occurrence at character 120.
- Zero `size_or_level` hits for rating-scale patterns: `on a scale`, `scale from 1`, `scale of 1`, `1 to 10`, `Likert`, `pain scale`, `severity scale`, `pay scale`, `grading scale`, `risk scale`, or `color scale`.
- Zero `size_or_level` hits for excluded map/model/CSS/chart/log/weighing/climbing/verb-growth scan terms checked: `map scale`, `scale bar`, `scale model`, `model scale`, `scale factor`, `transform: scale`, `scale(`, `log scale`, `chart axis`, `kitchen scale`, `truck scale`, `scale up`, `scale down`, `scale out`, `to scale`, and `scaled`.
- Zero `scale:` hits in `size_or_level`.
- Character buckets from `scripts/check_length_distribution.py`: `size_or_level` 0 very short / 40 short / 58 medium / 2 long, avg 278.5 chars.

Harsh `always_check.md` re-answer:

1. Correct, unambiguous meaning? Pass. The target occurrences now stay within scope/magnitude/extent/operating size/aggregation level. The plan and samples now agree that rating and ratio senses are excluded.
2. Diversity/messiness? Better than the previous pass. The section now has clean prose, OCR, CSV-ish tables, Q&A, chats, SRT, legal transcript, economics notes, finding-aid style text, product/review snippets, and a smaller technical residue.
3. Adequately dirty? Better. The dirt is no longer almost entirely file headers and engineering notes; it includes mobile scrape residue, merged comments, OCR, repeated footers, table fragments, and messy human notes.
4. Voice diversity? Much better. There are parents, annoyed customers, clerks, students, reviewers, reporters, vendors, teachers, forum posters, legal witnesses, and plain descriptive paragraphs. The calm technical narrator is no longer the dominant voice.
5. Introductory phrases avoided? Mixed but acceptable. Some artifact headers remain because raw web/text data often has them, but many samples now begin directly in the middle of messages, paragraphs, tables, or scraped text.
6. Length diversity? Acceptable but now slightly short-heavy. This is a deliberate correction from the earlier long ops-memo problem; shortest entries are still over 200 characters, and two long messy samples remain.
7. Starts with token? Verified zero.
8. Repetitive arcs/templates? Much improved. The old "small/test works, real scale breaks" and "marketing claimed scale, reviewer objects" arcs are now isolated rather than structural.
9. Abrupt/mid-page starts? Pass. Several entries start as cached pages, clipped tables, OCR, group texts, transcript fragments, forum posts, and partial emails.
10. Not only natural language? Pass. The section still has structured data and artifact-like text, but no longer mostly technical operations prose.
11. Tone variation? Better. Neutral remains common, but there is frustration, boredom, family logistics, academic caution, news flatness, mild excitement, and dry legal language.
12. Topic/domain balance? Better. Remaining domains include education, archives, journalism, events, retail, economics, public records, scientific methods, arts/culture, weather, food, property, ML/research, and a smaller amount of software/business.
13. Final semantic recheck? Passed the latest exact-token, standalone-token, token-start, excluded-sense, rating-scale, verb-growth, and `scale:` scans.

Harsh residual note:

The section is now less polished and less ops-memo dominated. The main residual weakness is that `size_or_level` has become shorter on average than the other two labels after removing many long explanatory samples. I am accepting that tradeoff for now because the shorter entries are not tiny, and padding them would risk recreating the same explanatory voice.

## Fourteenth-Pass Direct-Use And Voice Rework

Latest user feedback found four remaining weaknesses in `size_or_level`:

- Too many samples narrated what `scale` means instead of simply using it.
- Too many samples followed a hidden-bigness reveal arc: modest framing, then true scale revealed.
- Some spatial/methodological samples blurred toward level-of-analysis rather than size/magnitude.
- Voice still leaned toward calm analytical observer.

Actions taken:

- Reworked 30+ `size_or_level` samples across the issue clusters.
- Replaced meta-commentary phrasing such as `describe the scale`, `scale is the point`, `effect of scale`, `depends on scale`, and `the scale ... easier to see` with direct artifact uses.
- Reduced the hidden-bigness pattern in samples about garage sale, archive, mural, studio, press, depot, property, and similar contexts.
- Replaced or sharpened fuzzy spatial-method samples: hydrology, climate, geology, reef, dashboard, worksheet, and planning examples now use clearer magnitude/coverage/operating-size wording.
- Added rougher voices and formats: school sale setup notes, complaint thread, recall notice comments, permit email, radio/export-ish tables, mobile chat, labor report excerpt, and OCR/catalog fragments.
- Nudged several front-loaded `X scale` occurrences later after checking token placement.

Latest checks:

- YAML parses; 3 labels with 100 samples each.
- Zero missing exact lowercase `" scale"` substring.
- Zero missing standalone lowercase `" scale\b"` occurrence.
- Zero samples starting with `scale`.
- `size_or_level` first-token placement: 4 samples before character 60, 12 before character 80, median first occurrence at character 114.
- Zero `size_or_level` hits for excluded rating/map/model/CSS/chart/log/weighing/climbing/verb-growth scan terms.
- Zero `scale:` hits in `size_or_level`.
- Zero hits for the checked meta/reveal phrases: `surprises`, `finally hits`, `easy to miss`, `looks tiny`, `not just`, `describe the scale`, `asked for the scale`, `effect of scale`, `depends on scale`, `relevant scale`, `Identify the scale`, `moved the scale`, `scale is the point`, `The scale changed`, `scale of the .* easier`, `scale of the project in acres`, `Students should notice`, and `explains why`.
- Character buckets from `scripts/check_length_distribution.py`: `size_or_level` 0 very short / 41 short / 58 medium / 1 long, avg 268.6 chars.

Harsh `always_check.md` re-answer:

1. Correct, unambiguous meaning? Pass. The target is consistently scope/magnitude/extent/operating size/coverage, with rating/ratio/visual/weighing/climbing senses excluded.
2. Diversity/messiness? Improved. More raw artifacts and fewer polished explanations.
3. Adequately dirty? Better. The recall notice, OCR/catalog text, chats, tables, and copied worksheet/forum fragments add realistic mess without becoming decorative.
4. Voice diversity? Improved. Still not as naturally dramatic as `climb`, but less dominated by calm explanatory prose.
5. Intro phrases? Some artifact headers remain; acceptable, but still a place to watch.
6. Length diversity? Slightly short-heavy, but restored one long messy sample and kept most samples above 200 chars.
7. Starts with token? Verified zero.
8. Repetitive arcs/templates? Better. The hidden-bigness reveal and meta-scale explanation arcs are no longer dominant.
9. Abrupt/mid-page starts? Pass.
10. Not only natural language? Pass.
11. Tone variation? Better: annoyed customer, parent chat, permit/admin flatness, school setup notes, public complaint, terse tables, and legal/recall text.
12. Topic/domain balance? Better, though civic/institutional contexts remain visible.
13. Final semantic recheck? Passed current scans.

Harsh residual note:

The section is now much more direct, but it still has a higher share of institutional/civic material than the climb and weighing sections. Further work should add more consumer, entertainment, classifieds, casual forum, and auto-generated commercial text without returning to hidden-scale reveal prose.

## Fifteenth-Pass Format Diversity Rework

Latest user feedback found that `size_or_level` still had too few non-prose artifact formats compared with `climb` and `weighing_instrument`.

Actions taken:

- Replaced eight prose/chat-heavy samples with format-native artifacts.
- Added JSONC-like device benchmark config, YAML survey manifest, slide/speaker notes, LMS CSV export, Markdown issue notes with HTML comment, NetCDF-style metadata dump, Python code comments, and housing-model CSV inputs.
- Kept all target uses in the narrowed size/scope/magnitude sense: travel-day scale, survey scale, port scale, sidewalk scale, planetary scale, corpus scale, and neighborhood scale.

Latest checks:

- YAML parses; 3 labels with 100 samples each.
- Zero missing exact lowercase `" scale"` substring.
- Zero missing standalone lowercase `" scale\b"` occurrence.
- Zero samples starting with `scale`.
- `size_or_level` first-token placement: 7 samples before character 60, 15 before character 80, median first occurrence at character 112.
- Zero `size_or_level` hits for excluded rating/map/model/CSS/chart/log/weighing/climbing/verb-growth scan terms.
- Character buckets from `scripts/check_length_distribution.py`: `size_or_level` 0 very short / 44 short / 55 medium / 1 long, avg 265.7 chars.

Harsh residual note:

Format diversity is noticeably better, but the section is still shorter on average than the other labels. Future additions should prefer artifact-rich medium/long samples over more compact prose.

## Final Sweep

Final user request asked whether the `always_check.md` questions could now all be answered, and whether any last diversity or semantic-clarity improvements were worth making.

Last edits:

- Cleaned a few synthetic compounds in `size_or_level`: `school scale resale`, `Holiday-return scale`, `travel-day scale`, `Plant-opening scale`, and `neighborhood scale lot`.
- Rephrased them into more ordinary uses while preserving the target scope/magnitude sense.

Final checks:

- YAML parses; 3 labels with 100 samples each.
- Zero missing exact lowercase `" scale"` substring.
- Zero missing standalone lowercase `" scale\b"` occurrence.
- Zero samples starting with `scale`.
- `size_or_level` first-token placement: 7 samples before character 60, 15 before character 80, median first occurrence at character 113.
- `size_or_level` excluded-sense scan is clean for rating/map/model/CSS/chart/log/weighing/climbing/verb-growth terms.
- Character buckets from `scripts/check_length_distribution.py`: `size_or_level` 0 very short / 43 short / 56 medium / 1 long, avg 266.0 chars.

Final `always_check.md` answers:

1. Correct, unambiguous meaning? Yes. Every checked exact target use fits its label; cross-label scan hits in climb/weighing were false positives from nearby non-target words or literal weighing-device contexts.
2. Diversity/messiness? Yes. The file now includes logs, chats, OCR, HTML, YAML, JSONC-like config, SQL, Python comments, CSV/TSV rows, SRT transcript, slide notes, product/listing/review text, academic fragments, legal/court text, and ordinary prose.
3. Adequately dirty? Yes. There is realistic web/text residue without making every sample artificially corrupted.
4. Voice diversity? Mostly yes. `climb` and `weighing_instrument` are stronger, but `size_or_level` now has annoyed customers, parents, teachers, clerks, forum posters, reporters, legal witnesses, code comments, and raw exports.
5. Introductory phrases avoided? Mostly. Some artifact headers remain because they are part of realistic scraped/exported text; curator-style framing is no longer dominant.
6. Length diversity? Acceptable, with a residual weakness: `size_or_level` is shorter on average and has only one long sample.
7. Starts with token? Verified zero.
8. Repetitive arcs/templates? Strongly improved. The old "small thing reveals huge scale" and "scale as concept explanation" arcs are no longer dominant.
9. Abrupt/mid-page starts? Yes, especially in logs, exports, OCR, chats, code comments, and page fragments.
10. Not only natural language? Yes, after the final format-diversity pass.
11. Tone variation? Yes, though `size_or_level` remains naturally flatter than `climb`.
12. Topic/domain balance? Good enough. Civic/institutional contexts are still visible in `size_or_level`, but now balanced by consumer, commercial, technical, educational, legal, research, event, and casual contexts.
13. Final semantic recheck? Passed.

Final residual note:

I would stop here. The remaining weakness is not semantic clarity or format diversity; it is only that `size_or_level` has a slightly shorter length profile than the other labels. Forcing more length now would likely reintroduce the polished explanatory voice we spent several passes removing.

## Consolidated Learnings For Future Tokens

Repeated failure modes found while iterating on `" scale"`:

- Abstract labels attract over-explanation. `size_or_level` repeatedly drifted into samples that explained what scale means, rather than simply using `scale` in ordinary artifacts. Future abstract labels need direct-use scans for phrases like `describe the meaning`, `the point is`, `the effect of`, `depends on`, or curator-like explanation.
- Narrow the semantic boundary early and keep it in the plan. For `size_or_level`, map/model ratio, rating systems, CSS/chart/log scale, and verb-growth uses were tempting but made the label too heterogeneous. The final label is scope/magnitude/extent/operating size/coverage only.
- Do not let a correction become the new dominant register. The section moved from warm community-program vignettes, to technical/ops memos, to clean explanatory prose, before settling into a broader artifact mix. Every rebalancing pass should include a fresh scan for the new largest family.
- Beware repeated narrative arcs, not just repeated words. The worst recurring arcs were `small/test works, larger scale breaks`, `marketing claims scale and reviewer objects`, `modest surface, hidden true scale`, and `someone explains which scale is relevant`. Topic variety did not fix these until the underlying story shape changed.
- Format diversity must be native, not decorative. Adding a header above a paragraph is not the same as adding JSONC, YAML, CSV, code comments, slide notes, SRT, OCR, or raw exports. The final improvement came from replacing prose with actual artifact structures.
- Token placement can improve one pass and regress the next. `size_or_level` needed repeated first-occurrence checks because patches introduced early `X scale` starts. Final placement is acceptable, but future passes should check positions after every major rewrite.
- Synthetic compounds are a subtle realism problem. Phrases like `travel-day scale`, `school scale resale`, and `Plant-opening scale` technically had the right sense but sounded generated. Prefer ordinary phrasing such as `at regional scale`, `at evaluation scale`, `at this scale`, or domain-native forms already found in real text.
- Length should be balanced against voice risk. `size_or_level` remains shorter than the other labels because lengthening often reintroduced polished explanatory narration. For future final passes, prefer one or two long messy artifacts instead of padding many medium samples.
- Cross-label regex scans overreport but are still useful. The climb/weighing scans produced false positives from nearby words like `weight` or `scale for`, but they were good reminders to manually challenge every exact lowercase occurrence and side-context.
- `always_check.md` should be answered after edits, not only before them. The biggest improvements happened when the answers were harsh and specific enough to name exact templates, registers, source types, and semantic boundary leaks.

Reusable final audit pattern:

- Parse YAML and verify label/sample counts.
- Verify exact `" scale"` and standalone ` scale\b` in every sample.
- Verify no sample starts with `scale`.
- Check first-token position distribution by label.
- Run excluded-sense scans per label, then manually judge false positives.
- Scan for repeated narrative arcs and meta-commentary phrases, not just keywords.
- Run length distribution and decide whether length repair would improve realism or merely add padded prose.
