# Plan: Polytok Token `" sink"`

## Objective

Create `dsv2/samples_sink.yaml` with 100 realistic samples for each meaning label:

- `plumbing_fixture`
- `descend_below_surface`
- `heat_absorber`

Every sample must contain the exact token `" sink"` at least once. Every occurrence of `" sink"` inside a sample must match that sample's `meaning_label`.

The `heat_absorber` label covers heat-sink hardware specifically: finned or otherwise thermally conductive parts, assemblies, and related thermal-interface hardware that absorb/spread/dissipate heat from electronics or other devices. It no longer covers carbon/current/data/hydraulic/model sinks.

This token is high-risk because lowercase `sink` appears as a noun, verb, inflected form, idiom, technical term, place/name fragment, and the beginning of unrelated compounds. Treat every lowercase exact occurrence seriously, including occurrences inside longer words such as `sinks`, `sinking`, `sinkhole`, `sinker`, and `sinkage`.

## Exact-String Notes

The target is a literal space followed by lowercase `sink`.

- ` sink`, ` sinks`, ` sinking`, ` sinkable`, ` sinkage`, ` sinkhole`, ` sinker`, ` sink_id`, ` sink:`, ` sink()`, ` sink-side`, and ` heat sink` contain the exact token and must be semantically correct for the active label.
- Indented keys such as `  sink: bathroom_2` contain the target because a space directly precedes `sink`.
- `Sink` with uppercase S, `sink` at the beginning of a sample or line without a preceding space, `.sink`, `/sink`, `_sink`, `unsinkable`, `backsplash_sink`, `under-sink`, `source-sink`, `heat-sink`, `carbon-sink`, and `heatsink` do not by themselves satisfy the exact token. They may appear as context only if another exact `" sink"` occurrence is present and all exact lowercase occurrences match the label.
- Do not start any sample with the target. If a natural artifact begins with `sink`, add realistic preceding context or choose a different excerpt.
- For code/config/table artifacts, include enough surrounding rows or parent keys before an indented ` sink:`/` sink_id` occurrence. Do not make the first visible content just the target key.
- Avoid relying on punctuation unless the exact string is present. `("sink")` does not contain the target, but `a sink)` does.
- `sank` and `sunk` are related words but do not contain the target and cannot satisfy the requirement alone.

## Realism Standard

Samples should feel like mixed C4/HPLT-style web data rather than curated examples. Use raw excerpts directly when plausible: plumbing forum posts, product listings, renovation checklists, apartment maintenance tickets, shipwreck reports, game logs, scientific papers, climate reports, hardware datasheets, code/config fragments, lab notes, OCR/PDF text, chat exports, support tickets, database rows, scraped tables, captions, newsletters, and partial comments.

Good data can be clipped, mundane, malformed, redundant, or surrounded by irrelevant web residue. Include plausible artifacts such as repeated headers, table fragments, stale navigation, cookie text, ad placeholders, OCR line breaks, warranty boilerplate, timestamps, JSON/CSV rows, unit labels, footnotes, sidebars, merged comments, and missing context.

Avoid source-intro wrappers such as `plumbing sample:`, `shipwreck note:`, `the climate page says`, `code snippet:`, or `example:` unless such labels are genuinely part of the artifact. The sample should be the text itself, not a description of the text.

## Distribution Guidance

Use approximate distributions, not exact quotas.

- Length: include a few very short fragments, many short and medium samples, and a meaningful minority of long or extra-long messy samples.
- Token placement: do not start any sample with `" sink"`. In longer samples, ensure target occurrences appear late sometimes, not only in the first sentence or first table row.
- Token density: use enough target tokens to make the meaning clear, but avoid stuffing. Plumbing and heat-absorber samples can naturally repeat `sink`; descend samples often need fewer repetitions and should not overuse dramatic sinking scenes.
- Source mix: include technical, educational, commercial, workplace, informal, structured, newsy, crawled/OCR, scientific, and auto-generated styles.
- Voice and tone: vary between neutral machine output, terse maintenance notes, confused homeowners, polished docs, academic prose, frightened incident reports, flat regulatory language, product marketing, forum sarcasm, and raw logs.
- Completeness: not every sample should be self-contained. Some should start or end abruptly as if scraped from the middle of a page.
- Case: the target token is lowercase `" sink"`. Uppercase `Sink` can appear for realism, but it does not satisfy the target by itself and should not be relied on.
- Language mix: mostly English, but include occasional bilingual or non-English artifacts where the lowercase English `sink` term naturally appears in product names, fixtures, configs, scientific terms, or technical documentation. Do not force translations that make the target unnatural.
- Rough length shape per label: a handful of very short clipped fragments, a large middle of one-paragraph or small-table samples, and a meaningful minority of long messy artifacts. Do not make every sample a complete explanatory paragraph.

## Build Strategy

Create samples in batches of about 20 per label, then audit the entire label before adding more. Early batches should establish high-certainty core examples; later batches should deliberately fill gaps in source type, length, voice, and messiness.

For each 20-sample batch:

- Verify every exact `" sink"` occurrence by scanning manually, especially `sinks`, `sinking`, `sinkhole`, `sinker`, `sink:`, `sink_id`, and `heat sink`.
- Check that at least several samples place the target token late, not only in the first sentence.
- Add a few structured or non-prose artifacts: CSV, JSON, code/config, tables, forms, logs, OCR, calibration notes, or copied webpage residue.
- Add at least one longer messy sample per label if the current label is becoming too clean.
- Remove samples that need a curator explanation to disambiguate the sense.
- Track topic clusters so the dataset does not collapse into only kitchen remodels, only boats sinking, or only climate/heat-sink prose.
- Check for nearby false neighbors in scraped residue: ads for sink cabinets in a descent sample, climate sidebars in a plumbing article, shipwreck text in a heat sink datasheet, or `let that sink in` in a comment thread.

Approximate source mix targets:

- `plumbing_fixture`: roughly one quarter household repair/maintenance, one quarter product/commercial/remodel listings, one fifth rental/hotel/restaurant/public-facility text, one fifth structured/OCR/code-like artifacts, and the remainder odd but plausible contexts such as lab, classroom, insurance, cleaning, or accessibility docs.
- `descend_below_surface`: roughly one third water/boats/objects, one quarter ground/soil/snow/mud/subsidence, one fifth bodies/furniture/food/objects physically lowering into support or material, one tenth games/fiction/tutorials, and the remainder scientific, industrial, or scraped artifacts.
- `heat_absorber`: heat-sink hardware only. Keep this spread across product listings, reviews, datasheets, BOMs, installation manuals, thermal logs, QA/manufacturing notes, repair forums, ecommerce fragments, OCR/PDF artifacts, localization/config strings, and support tickets. Do not let it collapse into only dusty/misapplied sink repair arcs.

Common failure modes to catch during review:

- Too clean: every sample reads like a tidy sentence from a dictionary. Fix by adding real work orders, tables, OCR fragments, configs, comments, and partial pages.
- Too theatrical: every descent sample involves a shipwreck, quicksand, or disaster. Fix with mundane sinking: tires in mud, couch cushions, cake centers, fishing lures, sediment pellets, and sagging pavement.
- Too domestic: every plumbing sample is a kitchen or bathroom note. Fix with restaurant hand sinks, lab sinks, mop sinks, hotel tickets, CAD schedules, public restroom inspections, and product data.
- Too narrow technically: every heat sample is the same dusty sink / high temperature / cleaning helped story. Fix with catalog rows, ecommerce reviews, BOMs, install sheets, thermal drawings, compatibility questions, return notes, manufacturing inspections, teardown transcripts, translated product pages, and lab exports.
- Too idiomatic: samples sneak in `let that sink in`, `everything but the kitchen sink`, `sink or swim`, `time sink`, `sinking feeling`, or `sinking fund`. Replace rather than trying to contextualize.
- Too front-loaded: the target appears only in the opening phrase. Add longer samples with target occurrences in middle and late positions.

## `plumbing_fixture`

Semantic rule: `" sink"` refers to a basin fixture or related plumbing installation used for water, washing, draining, or disposal. This includes kitchen sinks, bathroom sinks, utility sinks, lab sinks, mop sinks, bar sinks, sink drains, sink traps, sink cabinets, and sink installation parts.

Good examples:

- `water was leaking under the kitchen sink`
- `the bathroom sink drains slowly after shaving`
- `install a new sink faucet before setting the countertop`
- `mop sink, floor drain, hand sink required by code`
- `fixture sink_id: exam_room_3`
- `stainless sinks with left-hand drainboards`

Include:

- Household plumbing: clogged drains, leaking traps, garbage disposals, faucets, strainers, P-traps, caulk, shutoff valves, under-sink cabinets, countertop cutouts, bathroom vanities, laundry/utility sinks, and kitchen remodel notes.
- Commercial/public contexts: restaurant hand sinks, bar sinks, mop sinks, school bathrooms, hotel maintenance tickets, hospital/lab sinks, code inspections, ADA lavatory notes, janitorial closets, campground wash stations, and apartment work orders.
- Product and commercial text: sink listings, countertop compatibility, undermount/drop-in/apron-front/vessel sinks, sink grids, mounting clips, drain assemblies, reviews, shipping damage, warranty pages, installation manuals, and ecommerce fragments.
- Raw artifacts: maintenance tickets, property inspection checklists, restaurant health reports, plumbing forum posts, real estate listings, product specs, OCR manuals, CSV fixture schedules, BIM/revit schedules, YAML/config fields for fixtures, chat logs, emails, invoices, and support threads.
- Inflected exact-token forms when sense-aligned: `sinks` as multiple fixtures, `sink-side` if the text means beside the fixture, and `sink cabinet`/`sink base` as fixture-adjacent cabinetry. Hyphenated `under-sink` is useful context but does not satisfy the exact target unless another exact occurrence appears.

Exclude:

- Descending below a surface: `the boat began to sink`, `feet sinking into mud`.
- Heat-absorber terms: `heat sink`, `finned sink`, `sink clip`, `sink base`, `sink fins`, `sink pad`, `sink thermistor`.
- Idioms and figurative clutter: `everything but the kitchen sink`, `sink or swim`, `let that sink in`, `sunk cost`.
- `sinkhole`, `sinker`, `sinking fund`, `sink rate`, `sink a shot`, place names, unrelated brand names, and software sink endpoints. Brand/product text is fine only when the exact occurrence itself refers to a basin fixture.
- Musical, game, or tool names where `sink` is just a title/identifier.

Guidance:

- Keep the fixture physical and grounded by including water, drains, pipes, faucets, basins, cabinets, cleaning, fixtures, inspections, installation, or maintenance.
- Do not make the label only homeowner prose. Include commercial kitchens, public bathrooms, labs, rentals, CAD/BIM schedules, work orders, code snippets, inventory tables, and OCR manuals.
- Long scraped samples must not include unrelated `carbon sink`, `sink in`, `boat sink`, or plumbing `sink` text in sidebars or ads.
- Be careful with `sinks` as a verb in unrelated contexts. In this label, `sinks` should usually be plural basin fixtures.
- Avoid overusing "kitchen sink"; mix bathroom, utility, bar, handwash, mop, lab, laundry, outdoor, and accessibility contexts.

Planned diversity dimensions:

- Fixture type: kitchen, bathroom, laundry, utility, mop, bar, lab, handwash, prep, three-compartment, vessel, pedestal, undermount, farmhouse/apron, stainless commercial, portable camp wash.
- Adjacent parts: faucet, drain, trap, disposal, strainer, grid, clips, supply line, shutoff valve, vanity, base cabinet, countertop cutout, splash guard, caulk, overflow.
- Source type: work order, product listing, restaurant inspection, installation manual, apartment email, insurance report, design schedule, plumber forum, hotel housekeeping log, OCR PDF, HTML table, CSV export, chat transcript.
- Tone: annoyed tenant, neutral spec, terse maintenance log, excited remodel post, regulatory language, confused DIY thread, commercial copy, hotel staff note.
- Language/register: mostly English, with a few bilingual maintenance notes, product imports, or restaurant-inspection fragments where `hand sink`, `mop sink`, or `bar sink` appears as an untranslated fixture term.
- Length: short clipped notes like `leak under sink again`, medium tickets/listings, and long messy remodel or inspection artifacts with repeated fixture references.

## `descend_below_surface`

Semantic rule: `" sink"` means to go down, descend, drop, submerge, settle, or become lower relative to a surface, medium, level, or support. The motion can involve water, mud, snow, sand, soil, pavement, bedding, memory foam, ships, objects, bodies, buildings, or other physical surfaces.

Good examples:

- `the canoe started to sink near the dock`
- `the storm could sink the small boat at the mooring`
- `her boots kept sinking into the mud`
- `the old porch posts sink after heavy rain`
- `bread dough may sink in the center if underbaked`
- `the road surface is sinking near the culvert`
- `watch the marker sink below the foam line`

Include:

- Water/submersion: boats, toys, phones, bait, stones, nets, fishing gear, bath items, flood debris, swimming lessons, shipwrecks, submarines, ballast, and emergency reports. Transitive uses such as `sink the boat` are valid when they literally cause submersion.
- Ground/material settlement: feet sinking in mud/sand/snow, tires sinking, posts/foundations settling, pavement sinking, soil subsidence, mattresses/foam cushions dipping, dough/cakes sinking, and objects dropping through loose material.
- Physical downward motion in instruction or science contexts: density demonstrations, sedimentation, buoyancy worksheets, lab notes, particle settling, geology, civil engineering, ship stability, and oceanographic observations.
- Aviation, flight-simulation, and glider contexts when `sink` means literal vertical descent or downward velocity, such as `sink rate`, downdrafts, autorotation notes, and ballast/trim instructions.
- Game/fiction contexts where physical descent is literal: platforms sinking, characters sinking in quicksand, rooms sinking underwater, traps, terrain, and physics-engine logs.
- Raw artifacts: news snippets, safety instructions, repair forums, ship incident timelines, weather/flood reports, classroom worksheets, survival guides, game bug reports, construction logs, geotech PDFs, OCR captions, chat logs, and transcripts.
- Inflected exact-token forms when sense-aligned: `sinks`, `sinking`, and rare `sinkage` if they mean downward physical movement or settlement.

Exclude:

- Plumbing fixtures: `kitchen sink`, `sink drain`, `bathroom sinks`.
- Heat-absorber terms: `heat sink`, `finned sink`, `sink clip`, `sink base`, `sink fins`, `sink temperature`, `sink-to-ambient`.
- Figurative comprehension, emotional, or cognitive idioms: `let it sink in`, `that needs to sink in`, `sinking feeling`, `sinking suspicion`, `the news sank in`, `my heart sank`, `sink into despair`.
- Financial or institutional terms: `sinking fund`, `bond sinking account`, `sink cost`, `sunk cost`.
- Non-physical decline: `prices sink`, `morale sinks`, `approval sinks`, `rankings sink`, `temperatures sink`, and similar level-change prose. These are not the requested physical descent/below-surface sense.
- Sports/scoring verbs: `sink a putt`, `sink the free throw`, `sink a shot`. These are a separate "successfully make" sense.
- Causation metaphors: `sink the deal`, `sink the bill`, `sink the campaign`, `sink the project`. These mean ruin/defeat, not physical submersion.
- `sinkhole` as a noun unless the exact occurrence is part of a sample whose target occurrence also clearly means physical descending; safer to avoid entirely because the word names a feature rather than the act of descending.
- `sinker` as a fishing weight or baseball pitch unless the sample explicitly uses another exact `sink` occurrence for physical downward motion and all exact occurrences fit. Usually avoid.

Guidance:

- Keep the sense physical. The reader should see something moving or settling downward, not merely understand something or feel sad.
- Apparent physical descent can be valid when spatial: `the sun sinks below the ridge`, `the balloon starts to sink`, or `the glider's sink rate increases`. Avoid abstract charts, prices, temperatures, moods, or rankings.
- Balance tense and aspect deliberately. Use simple present facts (`heavy objects sink`, `cold brine sinks`), completed simple past (`the boat sank`, with another exact ` sink` occurrence if needed), instructions (`if the block sinks, remove it`), and only some progressive/inchoative forms (`starts to sink`, `keeps sinking`, `the slab is sinking`, `watch it sink`).
- Include both intransitive and transitive physical uses: `the raft begins to sink`, `heavy rain can sink the forms`, `ice can sink the float`, as long as the target occurrence itself contains exact lowercase ` sink`.
- Avoid making the label all boats. Balance water submersion with mud/sand/snow, construction settlement, food/craft failures, classroom density examples, game terrain, and industrial observations.
- In long samples, watch for accidental plumbing sidebars (`under sink storage`), climate `carbon sink` references, or electronics `current sink` references.
- The word `sinking` is often figurative. Reject samples where `sinking feeling`, `sinking suspicion`, or `sinking realization` is the exact target occurrence.
- `sink below` is useful but do not over-template it; vary syntax with `sink into`, `sinks under`, `sink through`, `sank into`, `did sink`, and `sink toward`. Avoid letting the whole section sound like ongoing narration.

Planned diversity dimensions:

- Medium/surface: water, mud, sand, snow, foam, wet concrete, loose soil, peat, pavement, mattress, cake batter, dough, ballast tank, sediment column, quicksand, marsh, carpet padding.
- Object/actor: boat, kayak, phone, stone, bait, tire, boot, fence post, porch pier, slab, building corner, child, platform, game avatar, cake center, marker bead, sample pellet.
- Source type: accident report, repair forum, classroom lab, recipe comment, construction log, geotechnical report, game bug ticket, flood alert, fishing thread, OCR textbook, chat transcript, news article, table export.
- Tone: calm instruction, worried owner, terse incident log, excited child/science demo, frustrated baker, dry engineering prose, dramatic fiction, messy forum reply.
- Language/register: mostly English, with occasional bilingual game, repair, or classroom text only if the `sink` occurrence is natural and physical.
- Length: short fragments like `watch the cork sink`, medium repair posts, and long messy reports with timelines or measurement rows.

## `heat_absorber`

Semantic rule: `" sink"` refers specifically to heat-sink hardware or directly adjacent heat-sink interface/measurement terms. The target occurrence should name a physical heat absorber/spreader/dissipater used to remove heat from electronics, LEDs, processors, regulators, amplifiers, motors, enclosures, or similar devices. Core examples are aluminum/copper heat sinks, finned sinks, passive heat sinks, GPU/CPU/LED heat sinks, heat sink compounds/pads/clips/brackets/bases/fins, chassis used as a heat sink, and thermal test references to sink temperature or sink-to-ambient resistance. Exclude all non-thermal uses, including carbon/current/hydraulic/data/model sinks.

Good examples:

- `the aluminum heat sink keeps the regulator below 70 C`
- `the sink fins align with the fan duct`
- `apply heat sink compound before clipping the module`
- `record sink temperature after five minutes`
- `the chassis acts as a heat sink for the power stage`
- `this passive sink is too tall for the router cover`

Include:

- Thermal/electronics hardware: heat sinks, passive/finned/skived/pin-fin heat sinks, cold plates only when called a sink or directly paired with one, heat spreaders when contrasted with a heat sink, CPU/GPU/LED/regulator/MOSFET/amplifier cooling, thermal paste/compound/pads, clips, springs, brackets, fins, fans, ducts, junction temperature, and hardware manuals.
- Product/commercial contexts: ecommerce listings, Q&A pages, star reviews, return forms, compatibility tables, warehouse notes, line cards, catalog rows, imported spreadsheet rows, and product descriptions for heat sink kits or parts.
- Engineering/manufacturing contexts: BOMs, ECAD notes, vendor drawings, receiving reports, assembly travelers, QA inspections, torque errata, thermal simulations, compliance reports, fixture logs, and design-review comments.
- Repair/service contexts: teardown transcripts, service manuals, RMA notes, forum posts, support chats, laptop/mini-PC/router/amplifier repairs, replacement screws, missing clips, and wrong-height returns.
- Raw artifacts: HTML fragments, OCR/PDF extraction, CSV/TSV/JSON-ish exports, localization strings, mobile-page residue, captions, comments, email fragments, screenshot notes, and mixed-language product text.
- Inflected exact-token forms when sense-aligned: `sinks` as plural heat-sink parts, `sink` as short form after heat-sink context, `sink fins`, `sink base`, `sink clip`, `sink temp`, `sink-to-ambient`, and `sink thermistor`.

Exclude:

- Plumbing fixtures: `kitchen sink`, `lab sink`, `sink drain`.
- Physical descending: `boat sink`, `sinking into mud`, `the floor sinks`.
- Any non-thermal absorber/reservoir: `carbon sink`, `methane sink`, `nitrogen sink`, `phosphorus sink`, `sediment sink`, `energy sink`, `vibration sink`, `current sink`, `sink current`, `sink rating`, `sink mode`, and other physical-but-not-heat labels.
- Figurative drains: `time sink`, `money sink`, casual `energy sink`, and similar resource-drain prose.
- Idioms: `everything but the kitchen sink`, `sink or swim`, `let that sink in`, `sunk cost`.
- `sinkhole`, `sinker`, `sink a shot`, and proper names unless the exact occurrence is a heat-sink hardware term.
- Software/data/audio abstractions: data sink, log sink, event sink, metrics sink, trace sink, Kafka sink connector, OpenTelemetry exporter sink, S3/archive sink, audio sink, video sink, null sink, HTTP/file sink, table/queue/webhook sink, and similar endpoints.
- Graph/mathematical abstractions: graph sink nodes, source/sink vertices, super sink constructions, Markov absorbing sink states, queueing sink nodes, population sink habitats, and generic source/sink equation terms when the exact occurrence names an abstract model element rather than a physical absorbing system.

Guidance:

- Make the heat role explicit with nearby words like `thermal`, `heat`, `finned`, `aluminum`, `copper`, `pad`, `compound`, `paste`, `clip`, `fin`, `fan`, `junction`, `ambient`, `Rth`, `C/W`, `extrusion`, `anodize`, `chassis`, `module`, `regulator`, `GPU`, `CPU`, or `LED`.
- Do not let this label become only repair arcs where a dusty or misapplied sink caused high temperature and cleaning/fixing helped. Those are realistic but should be a minority.
- Balance product/commercial snippets with datasheets, install manuals, engineering notes, lab/test logs, BOMs, support chats, reviews, OCR tables, localization files, and manufacturing artifacts.
- Long samples are valuable here because real technical text often includes tables, comments, footers, mobile-page residue, or repeated part references. Keep every exact `sink` occurrence within heat-sink hardware or direct thermal measurement context.

Planned diversity dimensions:

- Domain: electronics thermal management, computer/SSD/router cooling, LED fixtures, regulators, MOSFETs, amplifiers, appliance boards, fanless enclosures, thermal simulations, manufacturing QA, repair/service, and ecommerce parts.
- Quantity handled: heat, junction temperature, sink temperature, sink-to-ambient delta, thermal resistance, airflow, pad compression, fin area, sink mass, and contact resistance.
- Source type: datasheet, thermal benchmark, lab notebook, product listing, Q&A, review, BOM, line card, installation manual, ECAD review, vendor drawing, RMA ticket, service manual, teardown transcript, localization file, CSV/TSV/JSON-ish export, forum answer.
- Tone: dry engineering prose, terse hardware config, annoyed support thread, product copy, confused buyer, sarcastic reviewer, lab precision, manufacturing checklist, copied table, regulatory boilerplate.
- Language/register: mostly English, with occasional multilingual technical/product pages where `heat sink` remains in English as a term of art.
- Length: short lines like `attach heat sink before power`, medium product/support/lab snippets, and long messy technical artifacts with multiple heat-sink references.

## Cross-Label Collision Rules

- If a sample contains more than one exact `" sink"` occurrence, every one must match the label. A good plumbing sample cannot mention `carbon sink`; a good descend sample cannot mention `kitchen sink`; a good heat-absorber sample cannot mention a boat starting to sink, a current sink, or a plumbing sink.
- Be wary of `sinks`:
  - `two bathroom sinks` is `plumbing_fixture`.
  - `the canoe sinks slowly` is `descend_below_surface`.
  - `heat sinks vary by fin area` is `heat_absorber`.
- Be wary of `sinking`:
  - `the slab is sinking` is `descend_below_surface`.
  - Literal `sinking ship` text can be valid for `descend_below_surface` when the ship is physically going down.
  - `sinking feeling`, `sinking suspicion`, `sinking fund`, and `sinking ship` as metaphor are excluded.
- Be wary of `sink:` in configs:
  - fixture schedules can use `sink:` for `plumbing_fixture`.
  - thermal-test or heat-sink hardware configs can use `sink:` for `heat_absorber` only when the sink is a heat sink component or direct thermal measurement field.
  - physics/game configs can use `sink_rate` or `sink:` for descent only if it clearly controls downward motion or submersion.
- Be wary of rare or technical continuations:
  - `sinkage` is usually `descend_below_surface` when it means settlement/subsidence; avoid if it is jargon without context.
  - `sink_id`, `sink_name`, and `sink()` can be `plumbing_fixture` in fixture schedules or `heat_absorber` in thermal test/config contexts; surrounding fields must disambiguate.
  - `sinkable` can be `descend_below_surface` when it means capable of sinking, but use sparingly because it is uncommon.
  - `sinker` is usually a fishing weight, lure, pitch, or surname and should almost always be avoided.
- Avoid `sinkhole`, `sinker`, `sinkerball`, `sinking fund`, `bond sinking account`, `sink cost`, `sunk cost`, `sync`, and proper names. They create unnecessary ambiguity and are not among the requested labels.
- Avoid the idiom `everything but the kitchen sink` even in the plumbing label, because the actual exact occurrence functions idiomatically rather than as a fixture.
- Avoid `let that sink in` and `news began to sink in`; these are comprehension/realization meanings, not descent.
- Avoid `sink a shot`, `sink a putt`, and `sink money into` because they are scoring/investment senses outside the requested labels.
- Avoid `sink the bill`, `sink the deal`, and `sink the project`; these are defeat/ruin senses, not physical descent.
- Avoid casual `time sink`, `money sink`, current sinks, carbon sinks, hydraulic energy sinks, and data/log sinks. The third label is heat-sink hardware only.

## Dataset Creation Strategy

Build `dsv2/samples_sink.yaml` in rounds of about 20 samples per label, then review and revise before adding the next round.

First-round priority: establish unambiguous core uses before adding edge forms. Start plumbing with obvious basin fixtures, descent with literal submersion/settlement, and heat_absorber with obvious heat sink hardware, sink fins, sink clips, sink bases, thermal pads, and sink-temperature contexts. Save `sinkage`, `sink_id`, `sink()`, bilingual fragments, and very messy OCR for later rounds after the label boundaries are already stable.

For each `plumbing_fixture` round, deliberately cover several of:

- Residential kitchen/bath/laundry repair, commercial hand/mop/bar sinks, lab/clinic fixtures, apartment/hotel tickets, restaurant inspection, product listings, installation manuals, design schedules, cleaning notes, insurance reports, and messy forum/chat text.
- Surface forms such as ` sink`, ` sinks`, ` sink drain`, ` sink trap`, ` sink base`, ` sink cabinet`, ` sink faucet`, ` under sink`, ` hand sink`, ` mop sink`, ` lab sink`, and `counter sink-side`.
- Messier formats such as itemized repair invoices, fixture schedules, tenant text messages, HTML product grids, hotel housekeeping sheets, health-inspection checklists, OCR installation pages, and warranty-return emails.

For each `descend_below_surface` round, deliberately cover several of:

- Boats and floating objects, mud/snow/sand movement, subsiding pavement/foundations, mattress/cushion compression, baking/craft failures, classroom density demos, game/platform terrain, flood/debris reports, geotechnical notes, and accident/repair forums.
- Surface forms such as ` sink`, ` sinks`, ` sinking`, ` sink below`, ` sink into`, ` sink under`, ` sink rate`, ` keep sinking`, ` began sinking`, and `sinkage` where natural.
- Messier formats such as flood bulletin fragments, repair-thread replies, recipe comments, game physics bug reports, lab worksheet tables, construction punch lists, geotech boring logs, and transcript snippets.

For each `heat_absorber` round, deliberately cover several of:

- Heat sinks for CPUs, GPUs, SSDs, routers, LED modules, regulators, MOSFETs, amplifiers, appliance boards, fanless enclosures, and chassis-as-sink designs.
- Surface forms such as ` heat sink`, ` finned sink`, ` passive sink`, ` sink fins`, ` sink base`, ` sink clip`, ` sink pad`, ` sink thermistor`, ` sink temp`, ` sink-to-ambient`, and ` sinks` as plural heat-sink parts.
- Messier formats such as thermal benchmark logs, PCB datasheet excerpts, product listings, Q&A pages, reviews, BOMs, ECAD notes, installation manuals, service tickets, teardown transcripts, warehouse returns, localization files, CSV/TSV/JSON-ish thermal exports, and OCR/manual fragments.

After each round:

- Search every exact `" sink"` occurrence and classify it manually.
- Search for high-risk continuations: ` sinks`, ` sinking`, ` sinkhole`, ` sinker`, ` sinkage`, ` sink:`, ` sink_id`, ` heat sink`, ` carbon sink`, ` current sink`, ` kitchen sink`, ` sink in`, ` sinking fund`, ` time sink`, and ` money sink`.
- Check that no sample starts with the target and that first target positions vary.
- Check that long samples contain some late target occurrences.
- Rebalance if a label is becoming too tidy, too explanatory, too remodel-heavy, too shipwreck-heavy, too heat-sink-heavy, or too cloud-config-heavy.
- Validate YAML structure before continuing.

## QA Checklist

Per sample:

- Contains exact lowercase token `" sink"` at least once.
- Every occurrence of `" sink"` has the target meaning, including occurrences inside longer lowercase strings such as `sinks`, `sinking`, `sinkhole`, `sinker`, `sink_id`, and `sink:`.
- By the time each exact `" sink"` occurrence is reached, the prior text has already anchored the sense. Prefer `kitchen sink`, `lab sink`, `heat sink`, `vertical sink rate`, or an already-established local context over bare first uses such as `the sink`, `sink base`, `sink temp`, or `sink rate` that only become clear after the token.
- Does not rely on uppercase, line-start, underscore-prefixed, slash-prefixed, or hyphenated lookalikes such as `Sink`, `sink` at line start, `_sink`, `/sink`, `under-sink`, `heat-sink`, or `source-sink`.
- Does not start with the token and usually delays the first target by several tokens.
- Avoids curator-style source introductions unless they are naturally part of the artifact.
- Is plausible as web/SFT corpus text, with realistic messiness and no theatrical over-explanation.
- Avoids unrelated idioms, comprehension uses, financial uses, sinkholes/sinkers, uppercase-only target reliance, and cross-label contamination.
- Is valid YAML when inserted into `dsv2/samples_sink.yaml`.

Per meaning:

- Exactly 100 samples.
- Lengths, source types, voices, formats, emotional registers, and token counts are visibly varied.
- No dominant opening pattern, topic cluster, or narrative template.
- Includes rough/partial/crawled material without simply labeling the source type.
- Has target tokens distributed across early, middle, and late positions, especially in longer samples.
- Includes short fragments, medium artifacts, and some long messy samples.
- Manually inspect high-risk cases where `sink` could mean a fixture, physical descent, heat-sink hardware, an idiom, or an unrelated compound in nearby text.

## Final Iteration Learnings

- The third label changed scope twice: broad absorber/reservoir -> physical-only absorber -> `heat_absorber`. Future passes should not reintroduce carbon/current/hydraulic/data/model sinks into this file. The final label is heat-sink hardware only.
- The most important semantic audit is not just "does the main occurrence fit?" but "does every exact ` sink` occurrence fit?" A final heat sample had a correct `heat sink` occurrence but an unrelated `kitchen sink` category in the same row; that had to be rewritten. Similar cross-label sidebars should be treated as failures, not harmless noise.
- `heat_absorber` initially became too short-heavy and too repetitive around the same arc: dusty/misapplied sink -> high temperature -> cleaning/fixing helped. The fix was to expand and diversify with product pages, catalog rows, BOMs, install sheets, thermal drawings, compatibility Q&A, return notes, manufacturing inspections, teardown transcripts, translated product pages, localization files, and lab exports. Keep the dusty/fix arc as a minority only.
- `descend_below_surface` initially overused progressive/inchoative aspect (`started sinking`, `keeps sinking`). It now needs deliberate simple present and simple past coverage: `sinks`, `sank`, `did sink`, factual physics/instructions, and completed incident reports.
- Long samples should be checked for late target occurrences. Two long descent rows were semantically valid but had the last exact target too early; adding natural late occurrences improved token placement without changing the label distribution.
- Narrator framing can creep in when writing review artifacts. Prefer embedded artifacts (`REVIEWER:`, comments, tables, thread snippets) over descriptions like "Reviewer asks whether...".
- The pre-token semantic-clarity check caught many rows that were correct only after reading past the target: `Set the sink...`, `sink base`, `sink temp`, `stock sink`, `captive sink screws`, `junction to sink`, and similar bare uses. Fix by adding a natural cue before the target token itself (`kitchen sink`, `lab sink`, `heat sink`, `vertical sink rate`, `basin sink drain`) rather than relying on following words or later explanation.
- A later ambiguity pass found that excluded senses can still leak in as contrast or metadata, not just as the main target use. In `heat_absorber`, phrases like `software sink`, `the word sink`, or nearby kitchen/plumbing category chatter should be removed or rewritten even when surrounded by valid `heat sink` text. Clearer local wording such as `heat sink clip`, `heat sink temp`, `heat sink body`, and `heat sink line` is better than compact shorthand when ambiguity is possible.

## Second-Pass Always-Check Answers

Timestamp context: this review began during the post-8pm cleanup pass and was updated after the final `heat_absorber` rewrite, length balancing, and strict false-neighbor sweep.

1. Correct, unambiguous meaning: yes after the latest rewrite. The third label is now `heat_absorber` only: heat sink hardware, sink fins, sink clips, sink bases, sink pads, sink thermistors, sink-to-ambient measurements, and adjacent thermal-interface language. Carbon/current/hydraulic/data/model sinks are excluded.
2. Diversity and messiness: improved. The first completed file still leaned too much toward neat tickets, notes, and reports. The second pass rewrote 30+ rows into messier scraped artifacts: clipped forum replies, support chats, crooked scans, RFI fragments, ad-interrupted pages, incident snippets, OCR-like worksheets, and broken exports. Later cleanup passes rewrote another 30+ rows that still had too-obvious source wrappers or slightly fuzzy `sink` phrasing.
3. Adequately dirty data: better, but still not maximal. There is meaningful raw-ish material across all labels, with HTML, CSV-like rows, config, chat, OCR, support tickets, forum posts, worksheets, and damaged exports. Weakness: the file still has a strong "operational note" backbone because `sink` is common in maintenance and technical contexts.
3. Voice diversity: improved in `plumbing_fixture` and `heat_absorber`. The first pass made descent more emotionally alive than the other labels. Later passes added angry customers, confused forum posters, annoyed support agents, student confusion, sarcastic electronics replies, and worried hardware/manufacturing notes.
4. Token usage and placement: acceptable. No sample starts with the target. Many longer rows still introduce the first exact token early, but late repetitions are common enough that the token is not only front-loaded.
5. Introductory phrases: improved. Some natural artifact labels remain, but curator-style wrappers were removed or rewritten as direct artifact text. Rows should read more like the scraped content itself, not descriptions of examples.
6. Length diversity: acceptable after the latest balancing pass. Current shape is intentionally mixed, with `heat_absorber` now close to the other labels by median and average rather than short-heavy. Remaining weakness: plumbing still has the heaviest long tail.
   Current post-cleanup distribution: 4 very short, 60 short, 220 medium, 16 long, 0 extra-long across 300 samples. Medians are now close by label: plumbing 308, descent 312, heat_absorber 309.
7. No starting with the token: yes. This is checked mechanically.
8. Repetitive arcs/templates: improved but not perfect. Maintenance-ticket, support-thread, and technical-note rhythms still recur. The later cleanup pass removed several visible artifact wrappers and converted them into raw starts, but this remains the harshest style risk after topic clustering.
9. Partial/non-self-contained samples: yes. The second pass added more mid-page starts and clipped fragments such as `...dry fit before silicone`, cached page fragments, cropped handouts, and broken forum/export text.
10. Not only natural language: yes. The dataset includes configs, CSV-ish schedules, tables, logs, HTML, worksheets, formulas, and raw UI/help fragments.
11. Tone and emotional register: improved. Neutral remains the majority, correctly for web/SFT data, but there are now annoyed, confused, funny, worried, bored, and urgent samples in all labels.
12. Topic/domain dominance: improved but still worth watching. `descend_below_surface` still has a large ground/soil/snow/road cluster; `heat_absorber` is intentionally all heat-sink hardware but now spreads across product pages, BOMs, manuals, reviews, manufacturing, testing, repair, localization, and OCR/HTML artifacts; `plumbing_fixture` still has commercial fixture and kitchen/bath maintenance clusters.
13. Correct and unambiguous again: yes. High-risk idiom/finance/sports/comprehension forms are intentionally absent. Final strict false-neighbor scans found zero remaining cross-label hits after fixing the heat row with an unrelated kitchen-fixture category and tightening one loose `whole lamp a sink` phrase to `whole lamp a heat sink`.
