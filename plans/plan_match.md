# Plan: Polytok Token `" match"`

## Objective

Create `dsv2/samples_match.yaml` with 100 realistic samples for each meaning label:

- `fire_ignition_stick`
- `competitive_sporting_event`
- `pattern_correspondence`

Every sample must contain the exact token `" match"` at least once. Every occurrence of `" match"` inside a sample must match that sample's `meaning_label`.

This token is high-risk because lowercase `match` appears as a noun, verb, programming keyword, sports fixture term, dating/compatibility term, ignition object, and the beginning of unrelated words. Treat every lowercase exact occurrence seriously, including occurrences inside longer words.

## Exact-String Notes

The target is a literal space followed by lowercase `match`.

- ` match`, ` matches`, ` matched`, ` matching`, ` matchbox`, ` matchbook`, ` matchstick`, ` matchday`, ` matchup`, ` match_id`, ` matchScore`, ` matchmaker`, and ` matchmaking` contain the exact token and must be semantically correct for the active label. Other continuations such as ` match-funding` and ` match-3` also contain the exact token, but are excluded from this dataset version because they drift toward separate financial/game-mechanic senses.
- `Match` with uppercase M, `match` at the beginning of a sample or line without a preceding space, `pre-match`, `post-match`, `rematch`, `mismatch`, `unmatched`, and `no-match` do not by themselves satisfy the exact token, though they may appear as surrounding context if another exact `" match"` occurrence is present.
- Avoid unrelated continuations such as ` matcha`, ` matchless`, ` matchlock`, and brand/product names that only happen to begin with `match`, unless the occurrence is genuinely sense-aligned. ` matchlock` can be fire/weapon history, but it is not a modern ignition stick and should usually be avoided. ` match-3` is usually a puzzle-game/tile correspondence sense, not a sports event, and was kept out of this dataset version.
- Indented code can create target occurrences: `    match value:` or `  match x {` includes `" match"`. In this dataset version, Rust/Python-style control-flow `match` is treated as a gray-area keyword sense and should be avoided or replaced. Prefer regex, grep output, glob rules, router/path matching, CSS selectors, schema validators, nginx-style location matching, lexer/token expected-vs-observed tables, OCR/template matching, and other comparison APIs where the correspondence sense is explicit.
- Variable names and fields can be valid if the surrounding artifact makes the sense clear: sports `next match_id`, search `candidate match_score`, or fire-safety `stored match_count`. A header that starts with `match_id` does not satisfy the exact token unless another exact `" match"` appears elsewhere.
- Do not rely on target-adjacent punctuation unless the exact string is present. `("match")` does not contain the target, but `a match)` does.

## Realism Standard

Samples should feel like a mixed C4/HPLT-style slice rather than curated examples. Use raw excerpts directly when plausible: product listings, safety labels, campsite forum posts, tournament fixtures, live blogs, score tables, scraped sports pages, regex/code snippets, JSON responses, database dedupe logs, OCR/PDF fragments, support tickets, chat exports, emails, academic text, forms, and partial comments.

Good data can be clipped, mundane, redundant, or surrounded by irrelevant web residue. Include plausible artifacts such as table headers, repeated footers, old nav text, ad placeholders, cookie text, broken captions, collapsed comments, timestamps, JSON/CSV rows, OCR line breaks, odd casing, forum quote markers, and scraped sidebars.

Avoid source-intro wrappers such as `camping note:`, `sports article:`, `regex example:`, `the page says`, or `snippet:` unless such labels are genuinely part of the artifact. The sample should be the artifact itself, not a description of it.

## Distribution Guidance

Use approximate distributions, not exact quotas.

- Length: include a few very short fragments, many short and medium samples, and a meaningful minority of long messy samples.
- Token placement: do not start any sample with `" match"`. In longer samples, ensure the target token appears late sometimes, not only in the opening sentence or first row.
- Token placement QA should use the literal exact target, not only word-boundary matching. Check that every sample contains lowercase `" match"` after interpreting escaped newlines, that no sample starts with it, and that the first exact target is usually delayed by several characters. During final cleanup, aim for zero samples with the first exact target in the first 8 characters unless there is a strong raw-format reason.
- Token density: use enough target tokens to make the meaning clear, but avoid stuffing. Sports and search/code samples can naturally repeat ` match`; ignition-stick samples often need fewer repetitions. If a sample has 7+ exact-target occurrences, inspect it manually and replace some repetitions with natural pronouns, `bout`, `fixture`, `row`, `candidate`, `segment`, or other domain terms.
- Source mix: include technical, educational, commercial, outdoor, workplace, informal, structured, newsy, crawled/OCR, and auto-generated styles.
- Voice and tone: vary between neutral machine output, terse notes, confused users, polished docs, excited fans, frustrated support text, safety/legal boilerplate, mundane listings, and raw logs.
- Completeness: not every sample should be self-contained. Some should start or end abruptly as if scraped from the middle of a page.
- Case: the target token is lowercase `" match"`. Uppercase `Match` can appear for realism, but it does not satisfy the target by itself and should not be relied on.

## `fire_ignition_stick`

Semantic rule: `" match"` refers to a physical match used to create flame, or a container/object directly for such matches.

Good examples:

- `strike a match before opening the gas valve`
- `waterproof matches in the side pocket`
- `one match left in the matchbox`
- `safety match heads must stay dry`
- `the matchbook cover was singed`
- `a matchstick bridge` only if the sticks are literal matchsticks, not the puzzle/game sense

Include:

- Camping, hiking, survival kits, emergency-preparedness lists, cabin/fireplace use, candles, stoves, grills, fire pits, power outages, religious/ceremonial candles, old household manuals, and fire-safety warnings.
- Product and commercial text: strike-anywhere matches, waterproof matches, matchbooks, matchboxes, match safes, bulk cartons, shipping warnings, product reviews, auction listings, vintage packaging, safety data, and retail specs.
- Messy artifacts: product tables, OCR from safety manuals, forum troubleshooting, chat requests for a light, insurance/fire-department handouts, customs/shipping restrictions, recipe/camping page residue, and old classified listings.
- Physical details: match head, match tip, wooden match, paper match, spent match, damp match, broken match, sulfur smell, striker strip, matchbook, matchbox, match safe, matchstick, and match count.
- Some historical/chemistry context when the occurrence still refers to the object: safety match chemistry, old lucifer matches, phosphorus tips, factory/transport warnings.

Exclude:

- Sports contests: `soccer match`, `tennis match`, `match highlights`.
- Correspondence/equality/search/compatibility: `exact match`, `match the color`, `regex match`, `good match for the role`.
- Dating and matchmaking unless the exact occurrence is not target text or is removed.
- ` matchlock` unless the sample explicitly centers a match as a burning cord, which is a separate historical weapon mechanism and easy to confuse.
- ` matcha`, ` matchless`, `matching` when it means similarity rather than physical matches.
- Figurative idioms such as `met his match`, `match made in heaven`, or `match for anyone`.

Guidance:

- Keep this label physical and concrete. The reader should picture a small ignitable object, not a general act of matching.
- Use plural ` matches` naturally; fire-related web text often discusses boxes, packs, waterproof tins, or safety instructions rather than one single match.
- Avoid making every sample a cozy campfire paragraph. Mix warnings, commerce, damaged packaging, old manuals, messy chats, product metadata, and fire investigation notes.
- Do not let a fire sample rely only on compounds like `matchbook`, `matchbox`, `matchstick`, or `match heads` if the standalone sense could be debated. Include at least one clear physical ` match` or ` matches` occurrence whenever possible.
- Be careful with `matching`: in fire-stick samples it is almost always a false sense. Prefer `match head`, `match box`, `matchbook`, `matchstick`, or `matches`.
- If a sample contains `matchbox`, make clear it is a box for matches, not a toy car, music venue, software package, or brand.
- Some samples may include non-target words like `lighter`, `flint`, `tinder`, and `candle`, but every exact `" match"` occurrence must remain the ignition-object sense.

## `competitive_sporting_event`

Semantic rule: `" match"` refers to a competitive sporting fixture, game, bout, contest, set of play, or recorded event between players/teams.

Good examples:

- `tonight's match kicks off at 7:30`
- `the tennis match went to a fifth set`
- `archived match report: United 2, City 1`
- `rain delayed the cricket match`
- `man of the match voting closes at midnight`
- `fixture match_id,home_team,away_team,score`

Include:

- Football/soccer, cricket, tennis, rugby, volleyball, hockey, basketball where local usage says match, badminton, table tennis, chess/esports when framed as an organized competitive fixture, wrestling/boxing/MMA where `match` is natural in the source.
- Fixture lists, live blogs, scoreboards, match reports, ticket pages, fan forums, chat logs, league tables, tournament brackets, betting/odds pages, referee reports, club newsletters, postponement notices, TV listings, and scraped sports pages.
- Raw artifacts: sports feed `match_id` JSON, CSV fixture exports, HTML score widgets, commentary timestamps, box-score fragments, mobile-app push text, SRT/subtitle snippets, OCR from programs, forum quote chains, and post-match press quotes if another exact target occurrence is present.
- Sports-adjacent compounds: matchday, matchweek, match report, match official, match ball, match fitness, match highlights, match stats, match thread, match preview, and match result, when they refer to the sporting event.
- Different emotional registers: flat schedule data, ecstatic fan reactions, bored local recaps, angry officiating complaints, automated postponement notices, and messy ticketing/support text.

Exclude:

- Pattern/search/correspondence: `records match`, `exact match`, `DNA match`, `match requirements`.
- Fire ignition objects: `light a match`, `matchbox`, `matches in the drawer`.
- Non-sport competitive comparisons where `match` means "equal" or "rival": `can't match their speed`, `no match for the champion` unless the occurrence clearly names a formal sporting event.
- Dating/compatibility: `your top match`, `match profile`.
- General command/programming `match` unless the code is clearly sports fixture code and every occurrence refers to a sport match.
- Hyphenated `post-match`/`pre-match` alone as the only target, because these do not contain the exact `" match"` token.

Guidance:

- This label should not become only polished soccer prose. Include many sports and formats, including structured feeds and mundane local recreation pages.
- The safest uses are nouns with fixture context: `the match`, `this match`, `next match`, `match report`, `match stats`, `match result`.
- Avoid `matched`, `matching`, and `matchup` unless the sporting-event sense is unmistakable. `matched up well` often means correspondence/equality, not the event.
- Include some long samples where ` match` appears in the middle or near the end: live-blog tails, fixture tables with ads, ticketing emails, local club newsletters, and app notification dumps.
- Do not rely on sports brands or terms that are not lowercase exact target occurrences. Ensure at least one literal lowercase `" match"` appears.
- Watch `man of the match`: it is event-related and valid, but do not overuse it.
- Watch sport-type balance. Soccer/football terms like `pitch`, `header`, `keeper`, `kickoff`, `halftime`, and `touchline` can dominate quickly; keep them as a minority by deliberately adding cricket, tennis, chess, hockey, volleyball, wrestling, boxing/MMA, badminton, judo, snooker, curling, archery, swimming, water polo, netball, rugby, esports, bowls, squash, and other local/community contexts.
- Avoid a uniform comic-ending rhythm. A few complaints, jokes, and angry fan rants are useful, but many samples should be flat fixture data, ordinary notices, clean reports, or raw tables.

## `pattern_correspondence`

Semantic rule: `" match"` refers to correspondence, equality, similarity, fitting, pairing, search hits, pattern matching, compatibility, or the act/result of comparing one thing to another.

Good examples:

- `the regex found a match on line 42`
- `records match after trimming the ZIP code`
- `the user id produced a weak match candidate`
- `candidate match score: 0.82`
- `colors do not match under warm light`
- `ajv error /email must match format email`

Include:

- Search and code: regex, parser/tokenizer expected-vs-observed tables, glob filters, query engines, grep results, validation rules, router/path matching, CSS selectors, schema validators, nginx-style location matching, config options, and error messages. Avoid Rust/Python `match` keyword examples for this version, even though they are technically pattern matching, because they blur toward a separate control-flow-keyword label.
- Data/entity resolution: address matching, dedupe pipelines, CRM/contact merges, invoice/receipt matching, bank reconciliation, product catalog matching, identity/session matching, fingerprint/DNA/face match, schema matching, and lookup tables.
- Compatibility, fit, and equality: job/candidate match, HLA/transplant compatibility match, dating/app match, roommate match, mentor match, product recommendation match, color/fabric/paint match, size/part-number match, schedule match, requirement matching, and other cases where one item, pattern, feature, or candidate corresponds to another. Avoid bare `donor match` phrasing unless the medical HLA/ABO/crossmatch context is explicit, because it can read like a fundraising contribution sense.
- Academic/research text: sequence alignment, approximate matching, edit distance, bipartite matching, matching estimators, propensity score matching, graph matching, template matching, and information retrieval.
- Raw artifacts: JSON API responses, CSV match scores, stack traces, config files, code snippets, bug reports, forum Q&A, help-center text, UI strings, search-result pages, OCR forms, support tickets, research tables, color/font tools, product-fit outputs, and validator logs.
- Surface forms: exact match, partial match, fuzzy match, match score, match rate, match threshold, match group, match object, matched rows, matching rules, pattern matching, match_id only when it is a comparison identifier rather than sports fixture id. Do not let the phrase `no match` become a repeated fingerprint; use it rarely or avoid it entirely in the final set.

Exclude:

- Fire ignition objects: `strike a match`, `matchbox`, `matches`.
- Sports contests: `tennis match`, `match report`, `matchday`.
- Financial contribution and price/equality idioms such as `price match`, `employer match`, `donation match`, `matching gift`, `grant match`, and `match-funding` for this dataset version; these are close enough to a separate financial-contribution sense to risk label contamination.
- ` matcha`, ` matchless`, and decorative wordplay unrelated to correspondence.
- `matchlock` and historical weapons.
- Idioms that mean opposition rather than correspondence, such as `met his match`, unless the sample explicitly frames a compatibility/pairing result and avoids sports/fire senses.
- Sports `matchup` data, fixture IDs, or tournament brackets.

Guidance:

- This label can be broad, but every exact occurrence must stay in the compare/correspond/fit family.
- Do not let it become only regex tutorials or only entity-resolution/deduplication. Balance code/search with messy business data, forms, biology, recommendations, HR, support, color/size matching, translation memory, accessibility/UI tests, template matching, route matching, biometrics, audio/image fingerprints, and statistical matching.
- Programming language `match` constructs are good raw material, but include surrounding `case`, pattern, or branch syntax so the pattern-matching sense is unambiguous.
- `matching` can mean visual coordination, equality, or the statistical method. It is valid when the context is clear, but avoid fashion prose where `matching` could drift into style fluff unless it explicitly means colors/items correspond.
- Do not include price-match, donation-match, employer-match, or matching-gift samples in this dataset version. Even though they involve equality, they read like a distinct financial contribution or commercial policy sense.
- Avoid finance-adjacent support examples when they are not needed, because words like `billing`, `refund`, `credit`, `donor`, and `contribution` can make the reader look for the excluded financial matching sense even if the local `match` token is technically correspondence.
- For dating and recommendations, avoid romantic cliches; use app UI strings, exports, moderation notes, and algorithmic match scores.
- In research samples, distinguish `matching` as a method from sports matching or physical pairing. Include terms like `treated`, `control`, `propensity`, `caliper`, or `bipartite` when helpful.
- Avoid repeated micro-templates such as `field X should match Y`, `X match confirmed, Y match confirmed`, `selector match failed`, or parallel tables where every row is just `match/reject`. If a domain needs this idea, vary the surface form with raw code, error output, prose bug reports, logs, UI strings, or partial terminal output.

## Cross-Meaning Hazards

Inspect these cases manually during dataset creation:

- ` matches`: fire label if physical sticks; sports label if plural fixtures; pattern label if records/strings correspond.
- ` matching`: usually pattern/correspondence, but can appear in fire-related `matching box` or sports `matching uniforms`; avoid unless sense is clear and target label matches.
- ` matchbox`: fire label only if it is a box for matches. Avoid toy cars, venues, and package names.
- ` matchbook`: fire label if it is a paper folder of matches; can be a brand/software name in web text, so avoid unless physical.
- ` matchday`, ` matchweek`, ` match report`, ` match official`, ` match stats`: sports label.
- ` match score`: sports if score of a sporting event; pattern label if similarity/recommendation score. Surrounding fields must disambiguate.
- ` match_id`: sports fixture ID or pattern/entity match ID depending on schema. Use clear field names around it.
- ` matchmaker`, ` matchmaking`: pattern/compatibility only if explicitly about pairing people/items; otherwise avoid.
- ` price match`, ` employer match`, ` donation match`, ` matching gift`, ` grant match`, ` match-funding`: exclude for this dataset version because they risk a distinct financial/commercial sense, not the intended pattern-correspondence distribution.
- ` match-3`, ` match three`, ` matching tiles`: avoid in this dataset version because it tends to read like a distinct game-mechanic sense; never use under sports because it is a puzzle mechanic rather than a sporting fixture.
- ` matcha`: tea, not any label. Exclude.
- ` matchless`: means incomparable or a brand adjective, not any target sense. Exclude.
- ` matchlock`: historical firearm mechanism; avoid because it is not a match stick and can muddy the fire label.
- `met his match`, `no match for`, `match made in heaven`: usually idiomatic opposition/compatibility; avoid in this dataset version unless a future label explicitly wants idioms. Literal `no match` also became a repeated fingerprint during iteration, so treat it as a search-and-remove phrase.
- `rematch`, `mismatch`, `unmatched`, `matched` without preceding exact space: some forms may not contain the target; still avoid sense conflicts in the same sample when possible.
- Code `match`: prefer comparison APIs, regex/glob/router/schema examples, and fixture variables over language keyword/control-flow examples. Never use in fire label unless variable names explicitly count physical matches.

## Dataset Creation Strategy

Build `dsv2/samples_match.yaml` in rounds of about 20 samples per label, then review and revise before adding the next round.

For each `fire_ignition_stick` round, deliberately cover several of:

- Camping/emergency use, home candles/stoves, fire-safety warnings, product listings, vintage packaging, shipping/legal restrictions, matchbook/matchbox artifacts, chemistry/history notes, forum/chat troubleshooting, and OCR/manual fragments.
- Surface forms such as ` match`, ` matches`, ` safety match`, ` waterproof match`, ` strike-anywhere match`, ` match head`, ` match tip`, ` matchbox`, ` matchbook`, and ` matchstick`.

For each `competitive_sporting_event` round, deliberately cover several of:

- Fixture feeds, live commentary, fan forums, local club notices, ticketing pages, news recaps, sports app notifications, tournament brackets, referee reports, postponed/canceled fixtures, betting odds, school/community sports, and scraped HTML score widgets.
- Surface forms such as ` match`, ` matches`, ` matchday`, ` matchweek`, ` match report`, ` match preview`, ` match stats`, ` match result`, ` match thread`, ` match official`, and ` man of the match`.

For each `pattern_correspondence` round, deliberately cover several of:

- Regex/search/code, database/entity matching, biological/DNA/fingerprint matching, HR/recruiting, dating/recommendation apps, color/size/part matching, academic matching methods, game/tile matching, UI/support text, visual/template matching, translation memory, font matching, and matchmaking queues.
- Surface forms such as ` match`, ` matches`, ` matched`, ` matching`, ` exact match`, ` partial match`, ` fuzzy match`, ` match score`, ` match rate`, ` match threshold`, ` pattern matching`, and ` propensity score matching`. Treat literal `no match` as a high-risk repeated phrase, not a target surface form to include by default.

After each round:

- Search every exact `" match"` occurrence and classify it manually.
- Search for high-risk continuations and phrases: ` matcha`, ` matchless`, ` matchlock`, ` matchbox`, ` matchbook`, ` matchday`, ` match score`, ` matching`, ` matches`, ` matched`, ` matchmaking`, ` match_id`, ` match-3`, ` match three`, ` price match`, ` employer match`, ` donation match`, ` matching gift`, ` grant match`, ` no match`, ` no match for`, ` met his match`, and language-keyword patterns such as `let result = match`, `Kind::`, or `case _`.
- Check that no sample starts with the target and that first target positions vary. For final QA, compute exact `" match"` positions after unescaping `\n`; try to make `first_exact_under_8=0`.
- Check that long samples contain some late target occurrences.
- Check target density. Inspect any sample with 7+ exact-target occurrences and reduce forced repetition when a natural replacement exists.
- Rebalance if a label is becoming too tidy, too explanatory, too sports-news-heavy, too soccer/football-heavy, too regex-heavy, too entity-resolution-heavy, too camping-heavy, or too commercial.
- Search for near-duplicate anchors that can quietly recur across samples, such as repeated font-weight examples, the same paint/color name, repeated template coordinates like `x=442`, duplicate checkbox-template setups, repeated `Harbor Fog`-style named colors, or repeated `field should match field` skeletons.
- Validate YAML structure before continuing.

## Iteration Learnings From Final Cleanup

- The biggest synthetic fingerprint was not one bad sample but repeated tiny habits: final artifact sentences, curator labels, `no match`, `field X should match Y`, and neat match/fail tables. Future passes should search for skeletons, not just words.
- Messiness works best when it is embedded as the text itself: raw HTML, CSV, chat, terminal output, SRT timestamps, odd casing, cropped table rows, and partial logs. Avoid saying that an OCR/export/footer is broken unless that statement would naturally appear in the artifact.
- `pattern_correspondence` is especially prone to over-indexing on entity matching and deduplication. When that happens, replace some rows with regex/glob/router/schema/CSS selector/validator examples, biological or biometric matching, translation memory, color/font matching, audio/image hashes, statistical matching, or queue matching.
- `pattern_correspondence` is also prone to a repeated "system matched wrong / match failed" narrative beat. Keep some negative and diagnostic cases, but include plenty of routine successful matches: accepted regex hits, clean schema validation, product/part matches that just work, successful accessibility/title matches, accepted biometric candidates, and ordinary match-score outputs.
- Queue matching is valid for `pattern_correspondence`, but avoid game-lobby vocabulary that could pull toward sporting/esports events: `mmr`, `tank/support/dps`, `party size`, `ranked queue`, map IDs, or match servers. Prefer non-game queues such as interpreters, care shifts, support routing, drivers/riders, certification matching, or scheduling.
- `competitive_sporting_event` is especially prone to soccer/football gravity and to a repeated jokey complaint ending. Counterbalance with many sports, neutral data feeds, clean schedule fragments, and ordinary club notices.
- `competitive_sporting_event` and `fire_ignition_stick` can become too clean compared with `pattern_correspondence`. Add a few raw artifacts in each: scraped HTML widgets, cached score tables, OCR-ish manual rows, broken print/export text, ad placeholders, copied app tables, product rows, and clipped safety/manual fragments.
- `fire_ignition_stick` is strongest when physical details make the sense concrete. Watch samples that only contain `matchbook`, `matchbox`, `matchstick`, or `match heads`; add a standalone physical `match`/`matches` where needed.
- Some valid-looking pattern examples were cut or rewritten because they leaned into separate senses: Rust/Python control-flow keyword `match`, employer/donor/grant/price matching, and puzzle `match-3` mechanics. Keep these out unless a future label explicitly covers them. Lexer/parser samples are safer when phrased as expected-vs-observed token correspondence rather than keyword dispatch.
- Run both semantic and mechanical checks. Useful final metrics include: total samples, per-label counts, length distribution, exact-target missing count, starts-with-target count, first exact target under 8 characters, literal `no match` count, 7+ exact-target density, high-risk phrase scan, and intro-label scan.

## QA Checklist

Per sample:

- Contains exact lowercase token `" match"` at least once.
- Every occurrence of `" match"` has the target meaning, including occurrences inside longer lowercase words such as `matches`, `matched`, `matching`, `matchbox`, `matchbook`, `matchday`, or `matchmaking`.
- Does not start with the token and usually delays the first exact target by several characters. Final version should have zero samples with the first exact `" match"` before character index 8 unless a deliberate raw-format exception is documented.
- Avoids curator-style source introductions unless they are naturally part of the artifact.
- Is plausible as web/SFT corpus text, with realistic messiness and no theatrical over-explanation.
- Avoids unrelated `matcha`, `matchless`, `matchlock`, sports/fire/correspondence cross-contamination, and uppercase-only target reliance.
- Avoids financial/contribution/commercial policy senses such as `price match`, `employer match`, `donation match`, `matching gift`, and `grant match`.
- Avoids overused local fingerprints: literal `no match`, repeated coordinates, repeated named colors, repeated font-weight examples, and repetitive `match/reject` or `should match` tables.
- Is valid YAML when inserted into `dsv2/samples_match.yaml`.

Per meaning:

- Exactly 100 samples.
- Lengths, source types, voices, formats, emotional registers, and token counts are visibly varied.
- No dominant opening pattern, topic cluster, or narrative template.
- Includes rough/partial/crawled material without simply labeling the source type.
- Has target tokens distributed across early, middle, and late positions, especially in longer samples.
- Has natural target density; repeated `match` tokens should feel like the source genre, not like dataset construction.
- Includes short fragments, medium artifacts, and some long messy samples.
- Manually inspect high-risk cases where `match` could mean a fire object, a sports event, or a correspondence relation in nearby text.
