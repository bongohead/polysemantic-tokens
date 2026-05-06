# Plan: Polytok Token `" bar"`

## Objective

Create `dsv2/samples_bar.yaml` with 100 realistic samples for each meaning label:

- `establishment_serving_alcoholic_beverages`
- `long_rigid_material`
- `legal_profession_exam`

Every sample must contain the exact token `" bar"` at least once. Every occurrence of `" bar"` inside a sample must match that sample's `meaning_label`.

The old `ds/samples_bar.yaml` establishes the intended labels, but it is too clean, too travel-blog-like, and too explanatory for the v2 standard. It has 77 `establishment_serving_alcoholic_beverages` samples, 87 `long_rigid_material` samples, and 83 `legal_profession_exam` samples, so v2 must expand each label to 100 while replacing many polished narrator samples with messier C4/HPLT-like artifacts.

## Exact-String Notes

The target is a literal space followed by lowercase `bar`.

- ` bar`, ` bars`, ` bar's`, ` barroom`, ` barfly`, ` barback`, ` bartender`, ` barbell`, ` bar stock`, ` bar prep`, ` bar passers`, ` barista`, ` bargain`, ` barred`, ` barrier`, ` barrel`, ` bar code`, ` barcode`, ` barometer`, and indented fields like `  bar:` all contain the exact target visually or as a substring and must be handled deliberately.
- Uppercase `Bar`, line-initial `bar` with no preceding space, `_bar`, `.bar`, `/bar`, `-bar`, and `foobar` do not by themselves satisfy the exact lowercase leading-space target.
- A newline is not a space. A line beginning `bar: open until 2` does not contain the target unless it is indented or preceded by another character plus a space.
- Longer words are high risk. Do not rely on ` bartender`, ` barista`, ` barbecue`, ` barrier`, ` barrel`, ` bargain`, ` barren`, ` barcode`, ` barometer`, ` barred`, ` barring`, ` barley`, or ` barracks` as target-bearing text. Most are fail cases for all three labels and should simply be replaced.
- For all labels, avoid accidental unrelated senses in sidebars and ads. A venue sample with `search bar`, a metal sample with `bar chart`, or a legal sample with `hotel bar` is invalid even if the main text is correct.
- ` bars` is especially dangerous: it can mean taverns, physical rods, prison, music measures, phone signal, graphs, or legal membership depending on context. Classify every plural occurrence manually.
- Do not start any sample with the target. If a realistic artifact begins with lowercase `bar`, include preceding context from the same artifact or choose a different excerpt.
- Substring checks are not enough. Also verify a lowercase word-boundary occurrence such as ` bar\b` so samples do not pass only because of `bars`, `barista`, `barred`, or another longer form.
- Passing the start check is not enough. By the time the first target occurs, the meaning should already be clear from preceding context: `wine`, `beer`, `nightlife`, `attorney`, `state`, `law graduate`, `steel`, `brass`, `round`, `threaded`, dimensions, or a realistic artifact field that has already established the sense.

## Realism Standard

Samples should feel like mixed web data, not curated examples. Use raw excerpts directly where possible: nightlife listings, reservation pages, health-inspection blurbs, POS/menu snippets, construction invoices, steel-stock tables, repair tickets, gym equipment manuals, bar-exam forums, law-school emails, admissions dashboards, state-bar notices, OCR/PDF fragments, chats, forum replies, HTML, CSV, JSON, shipping rows, product listings, transcripts, and broken scraped pages.

Good data can be clipped, mundane, redundant, malformed, or surrounded by irrelevant page residue. Include plausible artifacts such as table headers, copied navigation, repeated footers, ad placeholders, cookie text, broken captions, stale sidebars, CSV rows, timestamps, mobile notification text, old quote markers, merged comments, and fields that wrap badly across lines.

Avoid source-intro wrappers such as `nightlife review:`, `blueprint excerpt:`, `law school note:`, `the page says`, `snippet from`, or `copied from` unless such labels are genuinely part of the artifact. The sample should be the artifact itself, not a description of the artifact.

During iteration, source labels repeatedly reappeared in subtler forms such as `curtain blog`, `garage sale note`, `basement gym setup`, `group text after results`, `TikTok caption draft`, and `FAQ for families`. Replace these with direct artifact text, realistic headers, timestamps, fields, or natural first lines. A real document can have a header like `FOOD ESTABLISHMENT INSPECTION` or `From:`, but a curator label naming the source type is usually a failure.

## Distribution Guidance

Use approximate distributions, not exact quotas.

- Length: include a few very short fragments, many short and medium samples, and a meaningful minority of long or extra-long messy samples.
- Token placement: do not start any sample with `" bar"`. In longer samples, ensure target occurrences appear late sometimes, not only in the first sentence or first table row.
- Token density: use enough target tokens to make the meaning clear, but avoid stuffing. The physical-material label can naturally repeat `bar` in tables and inventory. The legal label often repeats `bar` in official pages. Venue samples often need only one or two occurrences.
- Source mix: include technical, commercial, legal/educational, workplace, informal, structured, crawled/OCR, social, and auto-generated styles.
- Voice and tone: vary between neutral machine output, terse notes, annoyed customers, polished listings, official notices, anxious students, rough maintenance text, marketing copy, forum advice, and raw logs.
- Completeness: not every sample should be self-contained. Some should start or end abruptly as if scraped from the middle of a page.
- Case: the target token is lowercase `" bar"`. Uppercase `Bar` can appear for realism, but it does not satisfy the target by itself.
- Surface form balance: avoid making any label mostly `the bar was...`, mostly `steel bar`, or mostly `bar exam`.
- After clarity edits, search for newly introduced verbal tics. The final pass had to reduce overuse of `cocktail bar` in the venue label and `lawyer licensing bar exam` in the legal label.
- Do not overcorrect into charm. Venue data should include some witty anecdotes and travel writing, but also flat business listings, insurance text, real-estate descriptions, inspection rows, map cards, clerk notes, and boring structured reviews.
- Do not overcorrect into insider expertise. Legal data should include fluent bar-administration material, but also parents, friends, basic questions, failed-retaker threads, pass-rate news, and search-like outsider language.
- Keep physical-material data from becoming all work orders and fabrication notes. Include consumer/DIY voices, confused hardware-store questions, household assembly, product reviews, school projects, stroller/cat/tree/gym/yard fixtures, and fiction or informal descriptions where the physical bar sense is clear.

Approximate source mix targets:

- `establishment_serving_alcoholic_beverages`: about one third reviews/listings/travel/nightlife pages, one fifth local event or social material, one fifth menus/reservations/POS/health-inspection/business operations, one sixth chats/forums/emails, and the remainder OCR, HTML, transcripts, odd scraped artifacts, and short fragments.
- `long_rigid_material`: about one quarter construction/structural/rebar/metal stock, one fifth manufacturing/machining/materials testing, one fifth household/repair/hardware/fixtures, one sixth vehicles/gym/stage/equipment/safety, and the remainder lab, art, museum, shipping, OCR, and messy inventory artifacts.
- `legal_profession_exam`: about one third bar exam/prep/results/student material, one quarter bar admission/licensure/character-and-fitness/state-bar administration, one fifth professional membership/discipline/dues/ethics, and the remainder recruiter/firm/clinic/legal-aid, forum/social, OCR/PDF, dashboards, and email artifacts.

## `establishment_serving_alcoholic_beverages`

Semantic rule: `" bar"` refers to an establishment, venue, room, business, or nightlife/social place that serves alcoholic drinks. This includes pubs, cocktail bars, wine bars, hotel bars, dive bars, sports bars, brewery taproom bars, speakeasies, karaoke bars, and venue-specific compounds where `bar` denotes the alcohol-serving establishment.

Good examples:

- `the rooftop bar closes at midnight`
- `walk past the taco stand and the wine bar is on the left`
- `review row: quiet bar, cheap lager, kitchen open late`
- `the hotel bar stayed open for delayed passengers`
- `event row: bar crawl stop, venue, cover, drink_special`
- `comments say the bar lost its patio permit`

Include:

- Nightlife and hospitality contexts: dive bar, sports bar, cocktail bar, wine bar, hotel/lobby/airport/poolside bar, pub-like neighborhood bar, tiki bar, jazz bar, karaoke bar, piano bar, listening bar, beach bar, rooftop bar, speakeasy, brewery bar, cider bar, and mezcal/sake/vermouth bars.
- Operational and business text: reservation systems, event calendars, happy-hour menus, staff schedules, POS tabs, liquor-license notices, health inspection pages, venue policies, closing times, lost cards, reviews, and noise complaints.
- Messy artifacts: Yelp-like reviews, Google snippets, scraped event pages, local-news blurbs, HTML menus, map results, Discord planning, SMS fragments, forwarded emails, OCR flyers, receipt text, venue calendars, and newsletter/sidebar collisions.
- Venue-adjacent compounds when they clearly refer to the establishment context, such as `bar menu`, `bar tab`, `bar crawl`, `bar staff`, `bar owner`, and `bar room`. Prefer also having at least one bare/plural `bar` occurrence in the same sample.

Exclude:

- Physical counters or furniture: `sat at the bar`, `bar stool`, `bar top`, `bar counter`, unless another exact occurrence clearly refers to the establishment and the furniture occurrence is removed or rewritten.
- People or roles as the only target: `bartender`, `barback`, `barista`, `barfly`. These are alcohol-service-adjacent or coffee-related, but the exact target is not the establishment itself. Avoid unless the sample also has unambiguous establishment occurrences and the longer-word occurrence cannot be misunderstood.
- Coffee/juice/salad/sushi/oxygen/dessert bars when alcohol service is absent or unclear. A dessert bar with cocktails is valid only if the alcohol-serving establishment sense is explicit.
- Candy, chocolate, granola, protein, soap, gold, steel, towel, pull-up, search, menu, progress, status, health, signal, chart, error, color, and space-bar senses.
- Legal bar/exam/profession uses.
- Prison `behind bars`, music `bars`, rap `bars`, phone reception `bars`, pressure unit `bar`, sand bar, barrier, barrel, bargain, barometer, barcode, barred/barring, and any `bar` verb meaning prohibit.

Guidance:

- Make alcohol service or nightlife unmistakable through drinks, beer, cocktails, liquor license, happy hour, tabs, last call, pub/lounge/nightlife, bouncers, cover charges, or bar-specific venue types.
- Be careful with `the bar` in a restaurant: it can mean the physical counter. Use venue nouns like `wine bar`, `cocktail bar`, `hotel bar`, or make it clear the whole establishment is being discussed.
- Do not make this label all travel writing. Add mundane local listings, angry noise complaints, stale event pages, liquor-board notices, POS receipts, staff chats, neighborhood Facebook-style posts, and health inspection rows.
- Avoid making every sample a pleasant night out. Include closed/empty bars, bad service, confusing hours, spilled drinks, ID checks, weird ads, business listings, and boring operational text.
- Use `cocktail bar` sparingly. Rotate through wine, beer, hotel, lobby, airport, poolside, neighborhood, rooftop, dive, sports, karaoke, jazz, beach, brewery, cider, and bare `the bar` only when prior context already makes the venue meaning clear.
- Avoid making every venue sample follow a venue-then-broken-listing/cache/page arc. Broken scraped artifacts are useful, but the section also needs ordinary complete pages, dull records, rage reviews, brief map data, insurance/lease text, and casual stories with nothing technically wrong.
- Avoid `bar service` when the meaning is alcohol service rather than the establishment itself. Rewrite to `alcohol service`, `liquor service`, or another phrase unless a different exact target in the same sample clearly carries the venue sense.
- Longer samples should sometimes have late target occurrences, such as a review sidebar or receipt footer mentioning the bar after unrelated menu or booking details.

Planned diversity dimensions:

- Venue type: dive, sports, hotel, airport, rooftop, cocktail, wine, jazz, karaoke, tiki, beach, pub, brewery taproom, speakeasy, cider, mezcal/sake, piano/listening.
- Setting: downtown nightlife district, hotel lobby, airport terminal, resort pool, small town, college area, ferry dock, theater district, ski lodge, beach boardwalk, basement venue, strip mall, music festival afterparty.
- Source type: review, map listing, reservation page, menu/POS receipt, event calendar, liquor-license notice, inspection report, complaint email, chat, forum reply, scraped HTML, OCR flyer, travel page, staff schedule.
- Tone: bored listing, excited tourist, annoyed neighbor, terse manager, spammy promotion, confused traveler, flat regulator, casual group text, bitter one-star review.
- Length: short map snippets, medium reviews or messages, long scraped pages with menus, hours, comments, ads, and footer duplication.

## `long_rigid_material`

Semantic rule: `" bar"` refers to a long, rigid physical piece or member made of material such as metal, wood, plastic, carbon fiber, ceramic, glass, or composite. The bar may be raw stock, a structural member, a rod/rail/brace, an installed fixture, a tool-like lever, a safety member, or a shaped ingot when the physical elongated/rigid object sense is clear.

Good examples:

- `the steel bar bent during the load test`
- `flat bar, 1/4 x 2 in, cut to 36 in`
- `slide the towel bar through the brackets`
- `the roll bar cracked near the weld`
- `bus bar copper, drilled 4 holes, wrapped separately`
- `guard bars failed inspection after the hinge repair`

Include:

- Construction and structural material: steel bar, reinforcing bar, tie bar, tension bar, lintel/support bar, guard bar, cross bar, flat/round/square/hex bar, threaded bar, rebar only when accompanied by an exact ` bar` occurrence.
- Manufacturing and engineering: bar stock, extrusion, machining, lathe work, tensile tests, hardness tests, guide bars, calibration bars, bus bars, spreader bars, stabilizer bars, wear bars, reference bars, inventory manifests, and material certificates.
- Household and repair: towel bar, curtain bar, closet bar, door security bar, gate bar, stair handrail bar, shelving/mounting bar, cabinet brace, furniture footrest, playground cross bar, fence bar, and window support.
- Equipment and tools: lifting bar, pry bar, roll bar, pull-up bar, monkey bars, parallel bars, lighting bar, spreader bar, guide bar, magnetic bar, stirring bar, and lab/demo bars when they are physical rigid pieces.
- Messy artifacts: invoices, cut lists, warehouse pick tickets, CAD/BOM fragments, safety inspection forms, machine logs, product listings, shipping rows, repair tickets, lab data, OCR manuals, code/config naming physical parts.

Exclude:

- Alcohol-serving establishments.
- Legal bar/exam/profession uses.
- Digital/UI/graphical bars: search bar, menu bar, status bar, progress bar, scroll bar, health bar, signal bars, color bars, error bars, bar chart, bar graph, and histogram bars.
- Food/product bars: chocolate bar, candy bar, granola bar, protein bar, soap bar, shampoo bar, lotion bar.
- Music/poetry bars, prison `behind bars`, cell-signal bars, pressure unit `bar`, sand bar, island/bar geography, and barrier/prohibition uses.
- Barcode/bar code and printed visual bars. These are marks/encoding, not long rigid material, and should be removed even if another exact occurrence in the sample is physical.
- Longer unrelated words: `barrel`, `bargain`, `barley`, `barista`, `barbecue`, `barometer`, `barracks`, `barrier`, `barred`, and `barring`.
- Decorative or abstract names where `bar` is only branding, not the physical object.

Guidance:

- Make physicality unmistakable through material, dimensions, weight, bending, cutting, welding, drilling, fasteners, brackets, load ratings, corrosion, surface defects, placement, or inspection.
- The label should not be only steel construction. Include wood, aluminum, brass, copper, carbon fiber, ceramic, glass, acrylic, composite, gym equipment, lab apparatus, stage rigging, furniture, farm gates, boats, bikes, and machinery.
- The label should not be only industrial work-order voice. Deliberately include consumer and household contexts: assembling furniture, installing a towel or curtain bar, buying the wrong replacement part, confused hardware-store questions, product reviews, yard signs, gym gear at home, school projects, pet furniture, and informal fiction or anecdote where the long rigid object sense is still obvious.
- Fix label-ish starts here especially. `garage sale note`, `curtain blog`, `basement gym setup`, and similar source labels should become natural content such as a price tag, comment text, assembly instruction, message, or direct observation.
- `bar stock`, `flat bar`, `round bar`, and inventory rows are highly realistic. Use raw tables and cut lists instead of explaining them.
- `barbell` and `handlebar` are risky because the exact target may occur inside a lexicalized equipment word. Prefer `lifting bar`, `curl bar`, `pull-up bar`, or `handle bar` only when it clearly denotes a rigid physical bar.
- `rebar` does not contain the exact token by itself. If using construction reinforcement, include phrases such as `reinforcing bar`, `steel bar`, or `rebar bundle with one sample bar`.
- Watch long messy samples for accidental `bar chart`, `search bar`, `hotel bar`, or `bar exam` in sidebars.

Planned diversity dimensions:

- Material: steel, stainless, aluminum, brass, copper, iron, wood/oak/cedar/maple, carbon fiber, ceramic, glass, acrylic, composite, titanium, magnetic alloy.
- Shape/type: flat, round, square, hex, threaded, hollow, reinforcing, tie, cross, tension, guard, bus, guide, spreader, wear, calibration, towel, curtain, roll, lifting, pry, pull-up.
- Setting: construction site, machine shop, warehouse, lab, gym, stage grid, farm gate, boatyard, bike repair, home bathroom, classroom demo, museum, art studio, robotics lab, shipping dock.
- Source type: BOM/CAD note, invoice, product listing, cut ticket, safety inspection, repair log, machine transcript, lab worksheet, installation manual, forum reply, OCR form, CSV inventory, email chain.
- Tone: flat technical, rushed job note, frustrated repair thread, polished product copy, terse warehouse row, safety warning, student lab prose, casual DIY note.
- Length: one-line cut-list fragments, medium work orders, and long noisy artifacts with tables, dimensions, comments, and repeated footers.

## `legal_profession_exam`

Semantic rule: `" bar"` refers to attorney licensure, the legal profession as an admitted body, the bar exam, bar admission, bar prep, state-bar administration, professional discipline, or membership/eligibility to practice law.

Good examples:

- `registration for the July bar closes Friday`
- `passed the bar and took the oath in November`
- `state bar number missing from the form`
- `calendar row: bar prep, Evidence, Torts, Property`
- `the bar complaint was dismissed after review`
- `clinic hiring contingent on bar admission`

Include:

- Exam and study contexts: bar exam, bar prep, bar review, bar results, bar passers, bar subjects, MBE/MEE/MPT, repeat takers, accommodations, exam-day rules, laptop registration, score transfer, and UBE/local components.
- Admission and licensing: bar application, bar admission, character and fitness, oath ceremony, certificate of admission, bar card, bar number, bar license, bar dues, bar status, and sworn-in/newly admitted attorneys.
- Professional body and regulation: state bar, bar association, bar committee, bar counsel, disciplinary board, ethics rules, pro bono panels, continuing legal education, attorney registration, and complaints.
- Career and institutional contexts: law-school advising, firm reimbursement policies, recruiters, clinics, legal aid fellowships, court notices, alumni panels, student forums, dashboards, newsletters, and social posts.
- Messy artifacts: admissions portal exports, bar-prep calendars, forum threads, email reminders, scanned forms, PDF footers, state-bar web pages, court ceremony programs, job posts, spreadsheet rows, and chat logs.

Exclude:

- Alcohol-serving establishments.
- Physical material bars, courtroom railings, jail bars, or `behind bars`.
- General legal verb/noun uses meaning prohibit or obstacle: `barred by statute`, `barred from entry`, `time barred claim`, `time-barred claim`, `bar to recovery`, unless another exact occurrence clearly refers to the legal profession/exam and the prohibited-sense occurrence is removed.
- `barred attorney` if it could mean prohibited rather than admitted. Use `admitted to the bar`, `licensed by the state bar`, or `bar admission` instead.
- Nonlegal exams, answer keys, bar charts, bar graphs, search/status/menu/progress bars, code `bar` variables, pressure unit `bar`, food bars, music bars, and tavern mentions in lawyer anecdotes.
- Uppercase-only `Bar` in organization names does not satisfy the exact lowercase target. If using `American Bar Association`, include another lowercase `state bar`, `bar association`, or `bar admission` occurrence.
- `barrister` is legal-adjacent but not the requested US-style bar exam/admission sense by itself. Avoid unless a clear target occurrence appears separately.

Guidance:

- This label can include both exam and profession/admission senses because the old label covers both; keep them balanced rather than making every sample `bar exam`.
- Make legal licensing explicit through law school, attorney admission, state bar, jurisdiction, oath, results, character and fitness, MBE/MEE, practice authorization, disciplinary rules, or bar number.
- Legal text should not be only insider administration. Include outsider and beginner perspectives: proud parents, family chats, basic Reddit-style questions, failed retakers asking what happens next, news pass-rate blurbs, search snippets, and people loosely saying `the bar` with enough preceding law-school or attorney context.
- `passed the bar` and `failed the bar` are natural, but they can be unclear at the target. Prefer preceding context such as `law graduate`, `state bar exam`, `attorney bar exam`, `bar exam for new lawyers`, or `after law school` before the target appears.
- Avoid repeated clarity crutches. During final edits, `lawyer licensing bar exam` became too recurrent after ambiguity fixes; rotate through state, attorney, jurisdiction, exam, admission, and family/social contexts instead.
- Avoid the old polished motivational arc. Add raw advising emails, deadline tables, portal status rows, anxious forum posts, reimbursement policies, complaint notices, ceremony programs, and dull official text.
- `bar` as a legal obstacle/prohibition is common but outside this label. Manually scan for `barred`, `barring`, `time-barred`, `bar to`, and `bar against`.
- In long messy samples, remove tavern or physical-bar sidebars. Law-school pages can easily have unrelated ads like `hotel bar` near conference content.
- Some samples can use terse fragments such as `July bar laptop fee paid`, but include enough context in most cases to distinguish exam/admission from other meanings.

Planned diversity dimensions:

- Stage: law school planning, application, character/fitness, exam registration, prep, exam day, results, retake, admission/oath, early practice, CLE/dues, discipline/complaints.
- Jurisdiction/admin surface: state bar, UBE, local component, bar number, bar card, admission certificate, bar counsel, bar committee, attorney registration, bar association.
- Source type: advising email, admissions portal, prep calendar, forum thread, social post, court program, recruiter note, firm policy, legal aid fellowship, scanned packet, FAQ, PDF notice, spreadsheet, chat, newsletter.
- Tone: anxious student, flat administrator, proud new lawyer, irritated repeat taker, official regulator, terse recruiter, supportive mentor, automated portal, messy email chain.
- Length: short deadline/status fragments, medium emails/posts, and long scraped state-bar pages with tables, footers, instructions, and comments.

## Cross-Meaning Hazards

Inspect these cases manually during dataset creation:

- ` bars`: taverns for `establishment_serving_alcoholic_beverages`; physical rods for `long_rigid_material`; legal admission only in rare phrases like `members of the bar` if lowercase target exists. Exclude prison/music/phone/graph senses.
- ` bar exam`, `bar prep`, `bar review`, `bar admission`, `state bar`, `bar association`, `bar counsel`, `bar number`: legal label when not sample-initial and when legal licensing context is clear.
- ` wine bar`, `cocktail bar`, `sports bar`, `dive bar`, `hotel bar`, `bar crawl`, `bar tab`, `bar menu`: establishment label when not sample-initial and when alcohol-serving venue context is clear.
- ` steel bar`, `flat bar`, `round bar`, `towel bar`, `pull-up bar`, `roll bar`, `bus bar`, `guide bar`, `guard bar`, `spreader bar`, `cross bar`, `tie bar`: physical material label when not sample-initial and when the rigid object sense is clear.
- ` at the bar`: usually physical counter, not establishment. Avoid unless the sample also has clear establishment uses and this exact occurrence is not target-bearing or is rewritten.
- ` bar service`: risky because it often means alcohol service, not the establishment. Rewrite as `alcohol service` unless another exact target clearly carries the venue meaning.
- ` bar staff`, `bar manager`, `bar menu`, `bar safe`, `bar tab`, and `bar owner`: venue-adjacent and often valid, but they should not be the only evidence for the establishment label. Add or retain a clear venue occurrence nearby.
- ` bar chart`, `bar graph`, `error bars`, `color bars`: excluded graphical/statistical sense.
- ` search bar`, `menu bar`, `status bar`, `progress bar`, `scroll bar`, `navigation bar`, `space bar`, `health bar`, `signal bars`: excluded UI/game/keyboard senses.
- ` chocolate bar`, `candy bar`, `granola bar`, `protein bar`, `soap bar`, `gold bar` and `silver bar`: food/product/ingot senses. Gold/silver/metal ingots may be valid for `long_rigid_material` only if the physical elongated material object is the intended sense, not a finance/commodity price article.
- ` behind bars`, `jail bars`, `cell bars`: prison sense. Physical cell bars are rods, but the idiom `behind bars` means imprisonment and should be avoided unless describing actual metal bars.
- ` music bars`, `rap bars`, `measure bars`, `bar line`: music/poetry sense, excluded.
- ` bar` as pressure unit, legal obstacle/prohibition, or verb meaning prohibit: excluded.
- ` barrier`, `barrel`, `bargain`, `barley`, `barbecue`, `barista`, `barometer`, `barcode`, `barracks`, `barren`, `barred`, `barring`: longer-word hazards, usually excluded.
- Uppercase `Bar` in proper names does not satisfy the exact lowercase target but can introduce apparent false positives during visual review.

## Dataset Creation Strategy

Build `dsv2/samples_bar.yaml` in rounds of about 20 samples per label, then review and revise before adding the next round.

For each `establishment_serving_alcoholic_beverages` round, deliberately cover several of:

- Venue listings/reviews, event pages, menu/POS text, liquor-license or inspection records, neighborhood complaints, chats, social posts, reservation/hours snippets, staff notes, and crawled HTML.
- Surface forms such as `bar`, `bars`, `wine bar`, `cocktail bar`, `sports bar`, `dive bar`, `hotel bar`, `bar crawl`, `bar tab`, `bar menu`, `bar staff`, and `bar owner`.

For each `long_rigid_material` round, deliberately cover several of:

- Construction material, machine-shop stock, hardware fixtures, household repair, gym/sports equipment, lab apparatus, stage rigging, vehicle safety, shipping/inventory, and product listings.
- Surface forms such as `steel bar`, `metal bar`, `flat bar`, `round bar`, `cross bar`, `tie bar`, `towel bar`, `guard bar`, `bus bar`, `roll bar`, `pull-up bar`, `guide bar`, `spreader bar`, and `bar stock`.

For each `legal_profession_exam` round, deliberately cover several of:

- Bar prep/exam/result material, state-bar administration, admission/character-and-fitness, law-school advising, firm policies, recruiter notes, pro bono/legal-aid restrictions, discipline/ethics, and ceremony/social posts.
- Surface forms such as `bar exam`, `bar prep`, `bar review`, `bar results`, `bar application`, `bar admission`, `state bar`, `bar association`, `bar number`, `bar card`, `bar license`, `bar dues`, `bar counsel`, and `bar committee`.

After each round:

- Search every exact `" bar"` occurrence and classify it manually, including occurrences inside longer lowercase words.
- Run both substring and word-boundary checks. The final dataset should have exact target coverage and at least one lowercase ` bar\b` occurrence per sample unless a specific plural/possessive case has been manually justified.
- Scan for high-risk excluded strings: `barista`, `barbecue`, `barley`, `barrel`, `bargain`, `barometer`, `bar code`, `barcode`, `barrier`, `barracks`, `barren`, `barred`, `barring`, `bar chart`, `bar graph`, `error bars`, `search bar`, `menu bar`, `status bar`, `progress bar`, `scroll bar`, `space bar`, `health bar`, `signal bars`, `chocolate bar`, `candy bar`, `granola bar`, `protein bar`, `soap bar`, `behind bars`, `music bars`, `rap bars`, `pressure bar`, `time barred`, `time-barred`, `barred from`, and `bar to recovery`.
- Check that no sample starts with the target, that the first exact target is not always near the beginning, and that the meaning is already clear by the first target occurrence.
- Check that longer samples include late target occurrences.
- Rebalance if a label is becoming too tidy, too essay-like, too travel-review-heavy, too steel-construction-heavy, too `bar exam`-heavy, or too dependent on one source type.
- Search for repeated openings, source labels, modifiers, and templates such as `I read`, `A friend`, `The bar`, `In the`, `During a`, `The law school`, `A state bar`, `The steel bar`, `cocktail bar`, `lawyer licensing bar exam`, `post from`, `note from`, and `excerpt`.
- Validate YAML structure before continuing.
- In final QA, parse the YAML and inspect parsed text strings, not only the raw file. Escaped newlines and indentation can change whether a visible `bar` has a literal preceding space.

## First-Pass Improvement Targets From `ds/samples_bar.yaml`

- Replace most polished narrator openings such as `I read`, `I saw`, `A friend`, `During`, `Scrolling through`, and bracketed labels like `[Snippet...]` or `[Blueprint Extract]` with direct artifacts.
- Old-file pattern counts to beat: `In the` appears 35 times, `the bar was` 33 times, `steel bar` 21 times, `During` 18 times, `at the bar` 15 times, `bar prep` 14 times, `bar exam` 12 times, `I saw` 10 times, and `A friend` 7 times. The v2 file should not preserve those cadences or surface-form concentrations.
- Add substantially more raw structure: POS/menu rows, liquor-license notices, health-inspection fragments, steel cut lists, BOM/CAD rows, shipping manifests, machine logs, bar-prep calendars, state-bar dashboards, scanned admission packets, and court ceremony programs.
- Expand each label to exactly 100 samples rather than polishing the old 77/87/83 samples.
- Reduce travel-and-nightlife-review dominance in the establishment label. Add local operations, regulatory text, bad reviews, map snippets, complaints, staff chats, and business pages.
- Reduce steel/construction dominance in the material label. Add household fixtures, stage/gym/lab/vehicle equipment, wood/plastic/composite materials, inventory rows, and repair tickets.
- Reduce `bar exam` dominance in the legal label. Add state-bar admission, attorney registration, bar dues, discipline, bar counsel, pro bono eligibility, firm policy, court appearance authorization, and oath ceremony material.
- Reduce `the bar was...` as a sentence skeleton across all labels. It is sometimes natural, but the old file uses it enough that it has become a template.
- Add more abrupt starts and endings. Not every sample should explain what happened or close with a lesson.
- Increase length diversity with more very short fragments and more long messy scraped samples.
- Watch for old-file ambiguous patterns: `at the bar` and `the bar itself` in venue samples can drift to counter/furniture; `bar` in legal samples can drift to professional threshold vs exam; `gold bar` in material samples can drift to finance/commodity if not physically described.

## Iteration Learnings From Final dsv2 Pass

These are the issues that repeatedly required repair while creating `dsv2/samples_bar.yaml`; keep them in the plan for future review rounds.

- The establishment label first leaned too administrative, then too charming. The stable target is a mixture: casual stories, rage reviews, flat business listings, insurance/lease snippets, zoning and inspection fragments, map cards, travel writing, party recaps, and boring structured data.
- `cocktail bar` became a verbal tic. Even correct modifiers can become distributional bugs, so search exact repeated modifiers after each clarity pass.
- Broken scraped-page artifacts are useful, but they became a narrative template. Samples should sometimes be simply complete, boring, or emotionally flat, without stale widgets, broken caches, or crawler-junk explanations.
- The physical label drifted toward competent fabrication and maintenance voices. Deliberately add consumer-facing and confused contexts, while keeping the physical object sense clear before `bar` appears.
- The legal label drifted toward insider fluency. Keep CLE, discipline, trust accounts, pro hac vice, and admissions administration, but balance them with outsider voices such as family texts, basic forum questions, news pass-rate reporting, and retaker anxiety.
- Clarity fixes can create new repetition. `lawyer licensing bar exam` solved ambiguity but became a pattern; prefer varied local context over one repeated clarifying phrase.
- Curator-style starts are the most persistent realism failure. A realistic artifact can start with a header, form field, timestamp, sender line, or sentence fragment, but not with a curator telling us the source type.
- Do not narrate mess from outside. Replace `crawler inserted`, `footer repeats`, or `old widget says` with the actual embedded artifact text when possible.
- Semantic clarity must be established before the token, not merely after it. Final fixes changed starts like bare venue names, bare `July bar`, and bare physical-object mentions into lines with preceding nightlife, legal, or material context.
- The final QA needs both text-level judgment and mechanical checks: parsed YAML, sample counts, duplicates, length distribution, exact-substring target presence, word-boundary target presence, start-position checks, and high-risk hazard scans.

## Plan Audit Notes

Latest self-review of the plan:

- The three labels are now meaning-bounded enough to support strict sample review: alcohol-serving venue, long rigid physical material/object, and legal exam/admission/profession.
- The exact-string section explicitly covers the most dangerous issue for this token: target occurrences inside longer words and line-initial non-matches.
- The plan deliberately excludes many common but unlabeled senses: UI bars, charts, food bars, music bars, prison bars, pressure unit, prohibition/legal-obstacle uses, coffee/salad/sushi bars, and longer-word accidents.
- Source-mix targets should prevent the next phase from collapsing into the old dominant patterns: polished nightlife reviews, steel-bar explainers, and bar-exam motivation prose.
- The biggest future sample audit is side contamination. A single `search bar`, `bar chart`, `hotel bar`, `bar exam`, or `steel bar` line in the wrong label can invalidate a long sample.
- The second biggest audit is counter ambiguity in the establishment label. `At the bar` often means furniture, not the venue; avoid that phrase unless another occurrence carries the target meaning and the counter phrase is removed.
- The plan now records the final dsv2 iteration failures directly: curator labels, narrated mess, over-charming venue prose, industrial physical-material voice, insider legal voice, and clarity phrases becoming new repetition.
- Residual risk: distributional self-similarity can appear after local semantic fixes. Search repeated exact phrases and re-audit source/voice balance after every concentrated edit pass.
- Residual risk: `long_rigid_material` is broad enough to include many object types. During generation, keep physical dimensions/material/installation context close to every target occurrence.
- Residual risk: `legal_profession_exam` combines exam and profession. Keep both, but avoid unrelated legal `barred from` and `time-barred` senses.
- Residual risk: venue samples can accidentally use `bar staff`, `bar menu`, or `bartender` more than actual establishment references. Prefer clear venue names and bare/plural `bar` occurrences.

## QA Checklist

Per sample:

- Contains exact lowercase token `" bar"` at least once.
- Contains at least one lowercase word-boundary occurrence like ` bar\b` unless a plural/possessive case has been consciously accepted.
- Every occurrence of `" bar"` is target-correct or removed, including occurrences inside longer lowercase words or compounds such as `bars`, `barroom`, `bar stock`, `bar prep`, `barista`, `barred`, `bar code`, and `barcode`.
- Does not start with the token, usually delays the first occurrence by several tokens, and is semantically clear by the time the first target occurs.
- Is checked as parsed sample text, so line-initial `bar:` and uppercase `Bar` are not mistaken for successful target occurrences.
- Avoids curator-style source introductions unless they are naturally part of the artifact.
- Is plausible as web/SFT corpus text, with realistic messiness and no theatrical over-explanation.
- Avoids unrelated UI, graph, food, music, prison, pressure, prohibition, coffee-service, and longer-word accident senses.
- Is valid YAML when inserted into `dsv2/samples_bar.yaml`.

Per meaning:

- Exactly 100 samples.
- Lengths, source types, voices, formats, emotional registers, and token counts are visibly varied.
- No dominant opening pattern, topic cluster, or narrative template.
- Includes rough/partial/crawled material without simply labeling the source type.
- Has target tokens distributed across early, middle, and late positions, especially in longer samples.
- Includes short fragments, medium artifacts, and some long messy samples.
- Manually inspect high-risk cases where venue, physical material, legal admission/exam, UI/chart, food, prison, music, and longer-word senses can appear near each other.
