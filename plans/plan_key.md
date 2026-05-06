# Plan: Polytok Token `" key"`

## Objective

Create `dsv2/samples_key.yaml` with 100 realistic samples for each meaning label:

- `device_to_open_locks`
- `critical_important`
- `musical_tonal_framework`

Every sample must contain the exact token `" key"` at least once. Every occurrence of `" key"` inside a sample must match that sample's `meaning_label`.

The old `ds/samples_key.yaml` establishes the intended labels, but it is too clean and explanatory for the v2 standard. It overuses polished prose, quoted snippets, and curator labels such as `excerpt`, `snippet`, `message`, `transcript`, and `manual`, and it underuses raw tables, forms, logs, product rows, OCR, chats, scraped pages, and abrupt fragments. The v2 file should preserve the three meanings while making the data feel like a mixed C4/HPLT-style corpus.

The old file has only 36 `device_to_open_locks` samples, 36 `critical_important` samples, and 37 `musical_tonal_framework` samples. The v2 dataset should expand each label to 100 rather than merely polish the old set.

## Current Rework Overrides

These overrides reflect the final rework direction for `dsv2/samples_key.yaml` and supersede earlier broader examples in this plan:

- `critical_important`: use `key` only after the thing it describes, usually predicatively or postpositively. Valid shapes include `the timing is key`, `risks that are key`, `the requirement that is key is...`, and `the evidence is key`. Avoid premodifier adjective forms such as `key risks`, `key features`, `key witness`, `key metric`, `key evidence`, `key decision`, and similar `key [noun]` constructions.
- `critical_important`: avoid making the sample build theatrically toward a hidden punchline. The predicate use can appear in meeting notes, chats, tables, product copy, HTML, care notes, incident logs, job postings, recipes, sports, household planning, and other everyday text without the repeated `not X but Y` corrective frame.
- `critical_important`: include some multi-use samples, but every additional `" key"` must also be postpositive/predicate and semantically central/important. Good second occurrences look like `alert timing is key too`, `timestamp proof is key too`, `notes stay key`, or `urine output is key as the warning signal`; avoid adding premodifier cleanup debt while trying to increase token count.
- `musical_tonal_framework`: reduce `key of [note]`, `song key`, `concert key`, `written key`, `original key`, `listed key`, and transposition-negotiation templates. Use more varied structures: reviews, metadata rows, theory fragments, app UI, program notes, casual listener comments, historical notes, and harmonic-analysis prose.
- `musical_tonal_framework`: when `key` appears, the tonal meaning should already be clear from nearby musical context such as tonic, major/minor/modal terms, chord progressions, cadence, transposition, capo, rehearsal, score, or song metadata. Avoid physical piano keys, computer keyboards, and other longer `key...` words. Also avoid exact occurrences like `key field` or `key column` in music metadata; rewrite as `musical key`, `tonal key`, `recorded key`, or just remove `field/column`.
- `device_to_open_locks`: maintain broad context, but avoid overconcentrating on inventory/problem/resolution arcs. Include incidental mentions in manuals, receipts, product tables, lease clauses, game walkthroughs, historical records, travel reviews, and raw access logs.
- All labels: reduce curator-style starts and filename/category openers. Prefer the artifact text itself: rows, fragments, messages, HTML, tables, OCR, and abrupt scraped prose.
- All labels: include a meaningful minority of longer samples. The current target is not exact parity with `samples_-.yaml`, but the file should not collapse into uniformly medium snippets.

## Exact-String Notes

The target is a literal space followed by lowercase `key`.

- ` key`, ` keys`, ` keyed`, ` keying`, ` keyhole`, ` keyway`, ` keyring`, ` keychain`, ` keycard`, ` key fob`, ` key signature`, ` key of C`, ` key:`, and indented `  key:` contain the exact token and must be semantically correct for the active label. For the current `critical_important` version, avoid premodifier/field-name target forms such as ` key factor`, ` key point`, and ` key_result`; rewrite them as predicate/postpositive forms such as `factor is key` or `result marked key`.
- `Key` with uppercase K, `key` at the beginning of a sample or line without a preceding space, `_key`, `.key`, `/key`, `api_key`, `ssh_key`, `"key"` preceded only by a quote, and `-key` in compounds such as `low-key` do not by themselves satisfy the exact target.
- Indented structured text can create target occurrences: `  key: C minor` in music metadata, `  room key: returned` in a lock log, or `    spare key pouch` in a physical-access inventory all contain `" key"`. Avoid using indented critical field names such as `  key_factor:` or `  key_result:` in the current predicate-only version.
- Line-initial fields such as `key: C minor` or `key_findings:` do not contain the target unless they are indented or preceded by other text. When using structured artifacts, ensure at least one lowercase exact `" key"` occurrence is truly present.
- Longer words are high risk. ` keyboard`, ` keypad`, ` keypress`, ` keystroke`, ` keycode`, ` keyCode`, ` keyword`, ` keyphrase`, ` keynote`, ` keyframe`, ` keyless`, ` keystore`, ` keygen`, ` keychain`, ` keycard`, ` keyhole`, ` keyring`, and ` keystone` all contain the exact target. Use them only when the entire occurrence belongs to the active meaning, and otherwise avoid them.
- Bare structured fields such as ` key:` are usually data-structure fields, not one of the three requested meanings. They are valid only when the field itself clearly names a lock/access key or a musical key, such as `  key: C minor` in song metadata. For the current `critical_important` version, avoid ` key_findings:`, ` key_risks:`, and similar field-name target forms; use nearby prose or row values like `finding marked key` instead.
- Do not rely on uppercase-only section titles such as `KEY TAKEAWAYS` or `Key Signature`. They can appear for realism only if another lowercase exact `" key"` occurrence satisfies the target.
- Do not start any sample with the target. If a realistic artifact begins with lowercase `key`, add preceding context from the same artifact or choose a different excerpt.

## Realism Standard

Samples should feel like mixed web data, not hand-authored teaching examples. Use raw excerpts directly where possible: lock service tickets, hotel check-in messages, lost-and-found posts, key-control policies, product listings, locksmith invoices, building access forms, strategy decks, research abstracts, board minutes, software release notes, music theory handouts, chord charts, set lists, rehearsal chats, metadata rows, scraped HTML, OCR/PDF fragments, forum replies, email chains, and partial transcript text.

Good data can be clipped, mundane, redundant, malformed, or surrounded by irrelevant page residue. Include plausible artifacts such as table headers, copied navigation, repeated footers, ad placeholders, cookie text, broken captions, CSV/JSON rows, timestamps, mobile notification text, old forum quote markers, merged sidebar content, and fields that wrap badly across lines.

Avoid source-intro wrappers such as `lock note:`, `business memo:`, `music theory snippet:`, `the page says`, `excerpt from`, or `copied from` unless such labels are genuinely part of the artifact. The sample should be the artifact itself, not a description of the artifact.

## Distribution Guidance

Use approximate distributions, not exact quotas.

- Length: include a few very short fragments, many short and medium samples, and a meaningful minority of long or extra-long messy samples.
- Token placement: do not start any sample with `" key"`. In longer samples, ensure target occurrences appear late sometimes, not only in the first sentence or first table row.
- Token density: use enough target tokens to make the meaning clear, but avoid stuffing. Lock and music artifacts can naturally repeat `key`; `critical_important` samples usually need fewer repetitions.
- Source mix: include technical, educational, commercial, workplace, informal, structured, newsy, crawled/OCR, and auto-generated styles.
- Voice and tone: vary between neutral machine output, terse notes, confused humans, polished documentation, excited fans, frustrated support text, legal/security boilerplate, mundane listings, and raw forms.
- Completeness: not every sample should be self-contained. Some should start or end abruptly as if scraped from the middle of a page.
- Case: the target token is lowercase `" key"`. Uppercase `Key` can appear for realism, but it does not satisfy the target by itself.
- Surface form balance: avoid making any label mostly `the key to...`, mostly `spare key`, or mostly `key of C major`.

Approximate source mix targets:

- `device_to_open_locks`: about one quarter household/rental/lost-and-found, one quarter institutional access/key-control/hotel, one fifth vehicle/equipment access, one fifth locksmith/product/hardware commerce, and the remainder historical, legal, security, OCR, or odd scraped artifacts.
- `critical_important`: keep this deliberately broad. No more than about one third should be business/product/management prose. Include substantial research, policy, education, legal, health, civic, engineering, household advice, raw tables, and messy review/comment material.
- `musical_tonal_framework`: roughly one quarter theory/education, one quarter rehearsal/performance/set-list material, one fifth chord charts/metadata/app exports, one sixth forum/social/lesson Q&A, and the remainder musicology/program-note/OCR/page-scrape fragments.

## `device_to_open_locks`

Semantic rule: `" key"` refers to a physical or access-control device used to open, lock, unlock, start, or control a lock or keyed mechanism. This includes metal keys, car/ignition keys, safe keys, skeleton keys, mailbox keys, hotel keycards, access cards, key fobs, key blanks, and lock-cylinder keying when the lock-opening sense is explicit.

Good examples:

- `leave the spare key under the planter`
- `the mailbox key snapped inside the lock`
- `front desk printed a new keycard for room 418`
- `ignition key stuck in ACC position`
- `locks are keyed alike; one key opens the shed and gate`
- `checkout row key_code,door,issued_to,returned_at`

Include:

- Household and rental contexts: front door, apartment, mailbox, garage, storage locker, bike lock, padlock, shed, spare key, landlord handoff, lockout texts, move-in packets, and tenant forms.
- Vehicle and equipment contexts: car key, ignition key, motorcycle key, forklift key, equipment key, key fob, immobilizer programming, valet key, fleet checkout, mobile car key, and service-desk notes.
- Institutional access: hotel keycards, mobile room keys, office keys, master keys, key cabinets, key-control logs, badge/fob systems when described as keys, school/gym/church/community-center access, and return/issue policies.
- Locksmith and hardware text: key blank, duplicate key, key cutting, rekeying, keyed alike/different, keyway, keyhole, key code, bitting, lock cylinder, skeleton key, safe deposit key, and product/invoice rows.
- Messy artifacts: lost-and-found posts, product listings, shipping emails, work orders, police/security notes, hotel PMS logs, checkout tables, apartment inspection PDFs, forum advice, chat fragments, receipts, old manuals, and OCR of key-control sheets.
- Physical-access continuations such as ` keychain`, ` keyring`, ` keyhole`, ` keyway`, ` keycard`, and ` key fob` only when they are directly tied to opening or managing locks.
- Raw code/config/table text is valid when the exact occurrence is inside a physical-access value or field, such as `spare key`, ` key_id` for a key-control cabinet, or ` key_status=returned`. Avoid generic object fields where `key` only means dictionary key.

Exclude:

- Computer keyboard keys or keypads: `press the enter key`, `keyboard shortcut`, `keycaps`.
- Other button/input-device senses: `keypress`, `keystroke`, `keybinding`, `keymap`, `hot key`, telegraph key, piano key, saxophone key, and any instrument-mechanism key.
- Cryptographic/software/license/API keys: `public key`, `API key`, `SSH key`, `license key`, `key exchange`.
- Database/map/dictionary/config keys: `primary key`, `foreign key`, `JSON key`, `object key`, `map key`, `legend key`.
- Answer keys, solution keys, identification keys, taxonomic keys, dichotomous keys.
- Musical keys or key signatures.
- Critical/important uses are excluded from this lock label, especially predicate/postpositive forms like `factor is key`, `takeaway marked key`, and `point remains key`; earlier drafts also used premodifier forms like `key factor`, but those are invalid in the current critical label.
- Florida Keys or island `key`, if lowercase appears.
- Key lime, keyhole surgery, keyhole neckline, mechanical shaft keys, Woodruff keys, and non-lock `keyway` uses.
- Vandalism uses such as `the car was keyed`; the object may be a physical key, but the exact occurrence means scratched/damaged, not a device to open a lock.
- Idioms where no lock-opening device is present: `the key to happiness`, `under lock and key` unless there is a literal lock device and all exact target occurrences are physical-access sense.
- Cryptographic or purely digital credentials are excluded even if they "open" an account. A `mobile key` for a hotel room or car is valid only when it unlocks physical access; an `API key`, `session key`, or `recovery key` is not.
- Software credential containers such as `keychain`, `keyring`, `keystore`, `key vault`, and `keygen` are excluded unless the text clearly describes physical keys on a ring or chain.

Guidance:

- Make the physical/access device unmistakable through locks, doors, ignition, keycards, fobs, cylinders, keyways, bitting, issue/return logs, or someone being locked out.
- Do not make all samples domestic. Balance house/apartment uses with hotels, vehicles, warehouses, schools, hospitals, locksmith shops, bike locks, safes, mailboxes, equipment yards, and access-control systems.
- `keyed` is allowed only when it means a lock is configured for a key, as in `keyed alike`, `keyed different`, or `keyed to master`. Avoid `keyed in` data-entry uses.
- Avoid `keyed` vandalism uses such as `someone keyed my car`; they are physical-key-adjacent but do not match the lock-opening label.
- `keychain` and `keyring` are accessories, not the device itself. They are acceptable only when the same sample clearly involves physical keys; avoid samples where the exact target is only a decorative keychain or a software credential store.
- `keyhole` and `keyway` are valid only in lock hardware. Exclude medical `keyhole surgery`, clothing/fashion `keyhole` cuts, and machinery keyways for shafts, gears, or pulleys.
- `digital key`, `phone key`, and `mobile key` need extra context: doors, rooms, vehicles, locks, Bluetooth fobs, or access readers. Without physical-access context they can look like software credential samples and should be replaced.
- In long scraped samples, watch for accidental `key features`, `keyboard`, `API key`, or `key signature` in sidebars and ads. Rewrite or remove those lines.

Planned diversity dimensions:

- Device/access type: house key, spare key, car/ignition key, mailbox key, padlock key, safe key, skeleton key, master key, keycard, fob, key blank, keyway, keyhole, key cabinet.
- Setting: home, apartment, hotel, office, warehouse, school, church, storage facility, car rental desk, locksmith shop, park gate, marina, gym, hospital, police property room.
- Source type: lost/found post, move-in email, key-control log, product listing, locksmith invoice, repair ticket, hotel chat, access policy, forum reply, OCR form, CSV checkout, work-order notes, manual excerpt.
- Tone: panicked lockout, flat policy, annoyed tenant, retail copy, terse security note, nostalgic antique listing, machine export, casual chat.
- Length: short fragments like `spare key missing again`, medium work orders, and long messy pages with key issue/return rows plus footer residue.

## `critical_important`

Semantic rule: `" key"` means important, central, crucial, essential, decisive, or a main factor/point/person/step in an argument, plan, process, or outcome.

Good examples under the current predicate/postpositive constraint:

- `retention is the metric that is key for this launch`
- `table 4 lists the finding reviewers marked key`
- `timing was key to the rescue`
- `three audit risks remain key before signoff`
- `meeting notes say the stakeholders who are key requested a shorter pilot`
- `incident row takeaway marked key: cache misses drove the latency spike`

Include:

- Business, policy, research, education, health, climate, engineering, nonprofit, product, operations, legal, and everyday advice contexts where `key` means central or important.
- Surface forms where the described item comes before `key`: `the factor is key`, `risks remain key`, `the metric marked key`, `the finding that is key`, `the evidence proved key`, `the question still key`, `the objective considered key`, and similar predicate/postpositive forms. Avoid all `key [noun]` target uses for this dataset version.
- Raw and semi-structured artifacts: meeting notes, slide text, board minutes, research abstracts, peer-review comments, executive summaries, strategy docs, grant rubrics, incident retrospectives, product requirement docs, LMS feedback, public-comment summaries, newsletter fragments, and dashboard exports.
- Messy web residue: headings, bullet fragments, copied table rows, comments under articles, OCR from reports, auto-generated summaries, stale sidebars, broken Markdown, and emails with legal footers.
- Some ordinary human advice: recipes, study habits, job search notes, parenting forums, repair threads, and fitness posts, as long as `key` clearly means important rather than answer/lock/music.

Exclude:

- Physical lock/access devices: `door key`, `spare key`, `keycard`, `key fob`.
- Musical tonal frameworks: `key of G`, `minor key`, `key signature`.
- Keyboard/button uses: `press any key`, `enter key`, `hotkey`, `keyboard`.
- Cryptographic, software, database, license, or identifier keys: `API key`, `public key`, `primary key`, `foreign key`, `license key`, `key-value`.
- Answer/solution/reference keys: `answer key`, `exam key`, `taxonomic key`, `map key`, `legend key`.
- `keyword`, `keyphrase`, `key term`, `key note`, `keynote`, `keyframe`, `keypad`, `keycap`, `keypress`, `keystroke`, `keycode`, `keyCode`, `keybinding`, `keymap`, `keystore`, `keygen`, `key error`, `KeyError`, and data-entry `key in`, `keying in`, or `keyed in`.
- Cinema/lighting/video terms such as `key light`, `key grip`, `key art`, `chroma key`, and compositing `keying`; they are separate technical fixed phrases and should not be used for this label.
- Food/geography/proper-name uses such as `key lime`, island `key`, and `Key West`.
- Idioms that drift away from importance or solution: `off key`, `low-key`, and `keyed up`.

Guidance:

- This label should not become only polished executive prose. Include blunt notes, raw meeting minutes, student comments, app reviews, support tickets, grant scoring, legal/public records, research tables, and messy automatic summaries.
- The phrase `the key to` is excluded for the current critical plan unless it clearly behaves like a predicate adjective after the described item; prefer `timing was key`, `benefits remain key`, `evidence reviewers marked key`, and similar forms.
- Avoid the repetitive moralizing arc `X is key to success`. Many samples can be mundane while still using predicate/postpositive syntax: `column choice is key`, `witness remained key`, `assumption marked key`.
- Avoid `key results`, `key_result`, and other premodifier/field-name forms for this version, even when they would normally mean important objective/result.
- Long samples should place `key` in multiple positions and avoid sidebars containing lock, music, or software-key senses.
- Be cautious with `key clue` and `key differentiator`; these are valid, but too many examples in that style make the label sound like a management explainer.
- Do not use `key accounts`, `key clients`, `key informants`, `key witnesses`, or `key personnel` as target forms in this version; rewrite as `accounts considered key`, `witnesses marked key`, etc.

Planned diversity dimensions:

- Domain: product, finance, law, public health, education, research methods, climate, construction, manufacturing, social services, sports analysis, workplace ops, nonprofit grants, household advice.
- Surface role: predicate/postpositive forms over factors, points, metrics, risks, findings, results, objectives, drivers, assumptions, steps, variables, details, stakeholders, witnesses, evidence, constraints, questions, and takeaways.
- Source type: board deck, meeting minutes, academic abstract, peer review, grant portal, issue tracker, incident review, article correction, study guide, app store response, email chain, OCR PDF, broken Markdown, table export.
- Tone: neutral report, tired manager, frustrated reviewer, casual advice, marketing copy, bureaucratic memo, student confusion, urgent incident note, terse spreadsheet row.
- Length: short fragments, ordinary medium notes, and long scraped reports with headings, tables, comments, and footer duplication.

## `musical_tonal_framework`

Semantic rule: `" key"` refers to the tonal center or tonal framework of a piece, passage, song, exercise, or improvisation. This includes major/minor/modal keys, key signatures, modulation from one key to another, transposition, relative keys, and phrases such as `in the key of F`.

Good examples:

- `play the verse in the key of D minor`
- `the bridge modulates to a new key`
- `staff line says the key signature shows three flats`
- `transpose the hymn down one key`
- `the solo sits better in a minor key`
- `setlist row: title, key, key_signature, capo`

Include:

- Music theory and performance contexts: key of C major, key of G major, key of D minor, major/minor keys, modal keys, relative major/minor, key signature, tonic, modulation, transposition, capo changes, concert key, written key, original key, target key, and enharmonic spellings.
- Genres and settings: classical analysis, jazz standards, church hymnals, choir rehearsal, guitar tabs, piano lessons, school band, orchestra, musical theater, folk sessions, DJ/remix notes, songwriting apps, DAW metadata, and set lists.
- Raw artifacts: chord charts, MusicXML-ish fragments, rehearsal chats, set-list spreadsheets, lyric/chord pages with ads, teacher comments, forum replies, exam questions, MIDI metadata, capo tables, program notes, OCR from theory PDFs, subtitle snippets, and copied comments.
- Surface forms such as `key of`, `major key`, `minor key`, `home key`, `target key`, `original key`, `concert key`, `written key`, `key center`, `key signature`, `key change`, `change key`, `different keys`, and `modulates from one key to another`.

Exclude:

- Physical piano/keyboard/instrument keys or button presses: `press the key`, `broken key`, `keyboard`, `keybed`, `keycap`, `sax key`, `MIDI key number`.
- Computer/music software license or API keys.
- Lock/access devices: `piano room key`, `studio keycard`, `case key`.
- Critical/important uses: `key performance`, `key theme`, `key objective`, unless the exact token is musical tonal only.
- `off-key` and `low-key` do not contain the exact target in typical hyphenated form and should not be used as target-bearing evidence. Avoid unhyphenated `off key` unless every exact occurrence clearly means pitch/intonation, not tonal framework; it is a separate pitch-accuracy sense and should usually be excluded.
- `keynote` or spaced `key note` as a speech, important note, or tonic note alone, unless the sample also contains a clear tonal-framework occurrence. Prefer `tonic` over `keynote` to avoid ambiguity.
- `keyboard`, `keytar`, `key switch`, `MIDI key number`, and piano/saxophone/instrument-key mechanics.

Guidance:

- Make the tonal-framework meaning explicit through surrounding words such as `tonic`, `major`, `minor`, `mode`, `signature`, `modulate`, `transpose`, `capo`, `concert pitch`, `chord chart`, or `cadence`.
- Do not overuse `key of C major`. Rotate among keys, modes, genres, instruments, and artifacts. Include `minor key`, `major key`, `key signature`, `concert key`, `original key`, `target key`, and plural `keys`.
- Prefer ASCII spellings such as `Bb`, `Eb`, `C#`, and `A-flat` when generating new text, unless preserving a realistic copied source that already uses musical symbols.
- Be careful with `key signature`: valid and common, but if every sample says `key signature`, the label becomes too narrow. Use it as one surface form among many.
- Avoid `keyboard` entirely in this label unless the exact target occurrence is absent or separately satisfied. The word contains the target but means an instrument/interface, not the tonal framework.
- Chord charts often use hyphen separators or slash chords; those are fine as surrounding material, but every exact `" key"` occurrence must remain tonal.
- Long samples should include realistic music-page clutter without accidental `key features`, `API key`, `studio key`, or `press key` sidebars.

Planned diversity dimensions:

- Tonality: major, natural/harmonic/melodic minor, Dorian/Mixolydian/modal uses, relative keys, parallel keys, enharmonic keys, concert/written keys, original/target keys.
- Musical setting: choir, jazz combo, guitar lesson, piano exam, marching band, orchestra, worship set, theater rehearsal, DAW session, folk jam, remix pack, theory class, musicology paper.
- Source type: chord chart, set list, forum post, rehearsal chat, MusicXML/MIDI metadata, lesson handout, exam question, program note, lyric page scrape, YouTube caption, app export, review fragment.
- Tone: neutral theory prose, terse rehearsal instruction, confused beginner, excited songwriter, bored teacher note, academic analysis, raw metadata, messy chord-site comments.
- Length: short fragments like `chorus in key of A`, medium lesson notes, and long scraped music pages with ads, chord grids, comments, and repeated footer text.

## Cross-Meaning Hazards

Inspect these cases manually during dataset creation:

- ` keys`: physical lock devices in `device_to_open_locks`; tonal frameworks in `musical_tonal_framework`; important principles in phrases like `keys to retention`; keyboard buttons in excluded contexts.
- ` keycard`, ` key fob`, ` keychain`, ` keyring`, ` keyhole`, ` keyway`: lock/access label only when clearly tied to opening locks or access control.
- ` keyboard`, ` keypad`, ` keycap`, ` hotkey`, ` shortcut key`, `press any key`: excluded for all three labels unless a future label covers buttons/input devices.
- ` keypress`, ` keystroke`, ` keybinding`, ` keymap`, ` hot key`, ` keybed`, ` key switch`, and telegraph/music-instrument key mechanics: excluded input/button/mechanism senses.
- ` API key`, ` public key`, ` private key`, ` SSH key`, ` encryption key`, `license key`: excluded cryptographic/software/access-token sense.
- ` keychain`, ` keyring`, ` keystore`, ` key vault`, and ` keygen`: excluded software credential-store or generator senses unless clearly physical lock-key accessories.
- ` primary key`, ` foreign key`, `object key`, `JSON key`, `key-value`, `key:` in configs: excluded database/data-structure sense. Also avoid field names such as `key_findings` in the current predicate-only critical set.
- ` key error`, `missing key`, `KeyError`, and similar dictionary/config lookup failures: excluded data-structure sense.
- ` answer key`, `solution key`, `map key`, `legend key`, `taxonomic key`, `dichotomous key`: excluded reference/solution/classification senses.
- ` key light`, `key grip`, `key art`, `chroma key`, compositing `keying`, `key frame`, and `keyframe`: excluded film/animation/video/production senses.
- ` key lime`, island `key`, `Key West`, ` keyhole surgery`, ` keyless`, ` keystone`, and mechanical shaft/gear/pulley keys: excluded unrelated lexicalized senses.
- ` key signature`, `key of`, `major key`, `minor key`, `change key`: musical tonal framework.
- Predicate/postpositive forms such as `factor is key`, `finding marked key`, `risk remains key`, `stakeholder considered key`, and `evidence proved key`: critical/important if the centrality sense is unmistakable. Avoid premodifier `key [noun]` forms in the current dataset.
- ` key to`: lock/access label when followed by a lockable object such as `door`, `shed`, `bike lock`, `safe`, `room`, or `ignition`; critical/important when followed by an abstract outcome such as `retention`, `recovery`, `approval`, or `success`. Do not classify by the phrase alone.
- ` keyed`: lock label if `keyed alike/different/to master`; excluded for data entry (`keyed in`), cryptography, keyed hash, keyed notes, or emotional `keyed up`.
- ` keyed my car`, `car was keyed`, and similar vandalism text: excluded scratched/damaged sense.
- ` off key`: usually pitch accuracy, not tonal framework; avoid unless a future pitch-accuracy label is requested.
- ` low-key`/`high-key`: normally no exact target due to hyphen before `key`, but avoid unhyphenated variants that could confuse the label.
- Florida/island `key`, `Key West`, and proper names should not be used as target-bearing text.

## Dataset Creation Strategy

Build `dsv2/samples_key.yaml` in rounds of about 20 samples per label, then review and revise before adding the next round.

For each `device_to_open_locks` round, deliberately cover several of:

- Domestic keys, vehicle/ignition keys, institutional key control, hotel keycards/fobs, locksmith/hardware invoices, lost-and-found posts, policy/legal text, repair tickets, product listings, and OCR/access logs.
- Surface forms such as ` key`, ` keys`, ` spare key`, ` master key`, ` ignition key`, ` keycard`, ` key fob`, ` key blank`, ` keyhole`, ` keyway`, ` keyed alike`, and ` key cabinet`.

For each `critical_important` round, deliberately cover several of:

- Business/ops strategy, public policy, research findings, education feedback, legal evidence, health guidance, engineering retrospectives, product docs, grant rubrics, meeting notes, news fragments, and ordinary advice.
- Surface forms where the described item precedes the token, such as `factor is key`, `point remains key`, `risk marked key`, `finding proved key`, `result stays key`, `metric considered key`, `objective that is key`, `detail still key`, `step was key`, `evidence reviewers called key`, `stakeholder considered key`, `question remains key`, and `takeaway marked key`.

For each `musical_tonal_framework` round, deliberately cover several of:

- Music theory handouts, chord charts, rehearsal notes, transposition/capo tables, set-list metadata, classical/jazz analysis, choir/band/orchestra contexts, songwriting app exports, forum questions, and lyric-page scrapes.
- Surface forms such as ` key of`, ` major key`, ` minor key`, ` key signature`, ` key change`, ` target key`, ` original key`, ` concert key`, ` written key`, ` home key`, ` related keys`, and ` different keys`.

After each round:

- Search every exact `" key"` occurrence and classify it manually, including occurrences inside `keyboard`, `keyword`, `keycard`, `keychain`, `key_signature`, and indented `key:` fields.
- Scan for high-risk phrases: ` keyboard`, ` keypad`, ` keypress`, ` keystroke`, ` keycode`, ` keyCode`, ` keybinding`, ` keymap`, ` keyword`, ` keyphrase`, ` key term`, ` key note`, ` keynote`, ` keyframe`, ` keyless`, ` keystone`, ` keychain access`, ` keyring daemon`, ` keystore`, ` key vault`, ` keygen`, ` key error`, ` KeyError`, ` keycap`, ` hotkey`, ` hot key`, ` shortcut key`, ` API key`, ` public key`, ` private key`, ` SSH key`, ` license key`, ` primary key`, ` foreign key`, ` JSON key`, ` key-value`, ` answer key`, ` map key`, ` legend key`, ` taxonomic key`, ` dichotomous key`, ` off key`, ` low key`, ` high key`, ` key lime`, ` keyhole surgery`, ` chroma key`, ` Florida key`, ` Key West`, ` key in`, ` keyed in`, ` keyed hash`, and ` keyed my car`.
- Check that no sample starts with the target and that the first exact target is not always near the beginning.
- Check that longer samples include late target occurrences.
- Rebalance if a label is becoming too tidy, too essay-like, too domestic-lock-heavy, too management-jargon-heavy, too `key of C`-heavy, or too dependent on one source type.
- Search for repeated openings and templates such as `During the`, `In a`, `The key`, `remember that`, `practice in the key of`, `lost my key`, and overused critical predicates such as `X is key`.
- Compute or manually inspect first-target positions late in the process. Aim for zero samples where the first exact lowercase `" key"` appears before character index 8 unless a raw table row makes that unavoidable.
- In final QA, parse the YAML and inspect the parsed text strings, not only the raw file. Escaped newlines, indentation, and quoted code blocks can change whether a visible `key` has a literal preceding space in the actual sample text.
- Validate YAML structure before continuing.

## First-Pass Improvement Targets From `ds/samples_key.yaml`

- Replace most polished narrator wrappers (`snippet`, `excerpt`, `message`, `transcript`, `manual`, `blog entry`) with direct artifact text.
- The old file has many curator words in sample text: `snippet` appears 15 times, `excerpt` 5 times, `message` 5 times, and `transcript` once. The v2 file should use those only when they are natural source text, not framing.
- Add much more raw structure: CSV rows, key-control logs, hotel PMS notes, locksmith invoices, research tables, strategy deck fragments, meeting minutes, MusicXML-like rows, chord-site scraps, forum quote chains, and OCR/PDF fragments.
- Reduce the single-sentence advice pattern in `critical_important`, especially `X is key to Y`; the old file has 18 ` key to ` occurrences.
- Reduce domestic-house-key dominance in `device_to_open_locks`; add hotels, cars, institutional access, master-key systems, safes, equipment yards, and locksmith commerce.
- Add missing lock-access forms from the old file: it has no `keycard` or `key fob` samples, even though those are common in hotel, vehicle, office, and institutional access data.
- Reduce `key of C major`/textbook dominance in `musical_tonal_framework`; the old file has 43 ` key of ` occurrences. Add set lists, capo charts, concert vs written key, jazz/theater/choir contexts, modal keys, DAW metadata, and messy chord pages.
- Increase abrupt starts and endings. Not every sample should explain itself or close with a lesson.
- Keep all non-target exact occurrences out of sidebars. In particular, a music sample cannot have a `studio keycard` line, a lock sample cannot have a `key features` product sidebar, and an important sample cannot have `API key` or `primary key` table text.

## Plan Audit Notes

Latest self-review of the plan:

- The three labels are now meaning-bounded enough to support strict sample review: lock/access device, critical/central importance, and musical tonal framework.
- The exact-string section explicitly covers the most dangerous issue for this token: target occurrences inside longer words, indented fields, and line-initial non-matches.
- The plan deliberately excludes common but unlabeled senses: keyboard/buttons, cryptographic/software keys, database/config keys, answer keys, map/legend/taxonomic keys, film/animation fixed phrases, food/geography names, keyless access wording, keyhole surgery, and mechanical shaft keys.
- The source-mix targets should prevent the next phase from collapsing into the old dominant patterns: house keys, polished `key to success` advice, and textbook `key of C` music prose.
- The most important future sample audit is cross-contamination in messy sidebars. A single `key features`, `API key`, `keyboard`, `answer key`, or `studio keycard` line can invalidate an otherwise good sample.
- The second most important future sample audit is target presence. Line-initial `key:` and uppercase `Key` look convincing but do not satisfy the exact lowercase leading-space token.
- Residual risk: `critical_important` is broad and can become bland. During generation, force raw tables, legal/research/education/public-comment fragments, and terse operational text instead of mostly motivational or strategy prose.
- Residual risk: `musical_tonal_framework` can accidentally drift into physical piano keys or software metadata. Keep words like `tonic`, `major`, `minor`, `mode`, `signature`, `modulate`, `transpose`, and `capo` close to target occurrences.
- Residual risk: `device_to_open_locks` can drift into decorative keychains or software/mobile credentials. Require lock, door, ignition, room, fob reader, cylinder, bitting, key cabinet, or issued/returned physical-access context.
- Later review fixes tightened examples that visually began with `key` but lacked the leading-space token, added old-file pattern counts, added parsed-YAML QA, and widened the hazard list for `keyless`, `keystone`, `keypress`, `keycode`, `key error`, `keystore`, `keygen`, `chroma key`, `keyhole surgery`, `key lime`, vandalism `keyed`, and mechanical keyway senses.

## Second-Pass Rework Plan

User critique after the first dataset draft:

- Too many samples begin with context-intro framing such as `tenant portal note`, `teacher feedback`, `program note OCR`, `musicxml export`, `setlist export`, or `memo`. Some of these can be realistic artifacts, but their frequency makes the dataset feel narrated instead of scraped.
- Messiness is still too weak. The next pass should replace polished notes with more raw C4/HPLT-like material: table fragments, broken markup, forwarded headers, ad/footer collisions, OCR repeats, partial chat logs, clipped rows, old mobile page residue, and abrupt starts/ends.
- Length diversity is only acceptable, not strong. Add more long messy samples and also preserve very short scraps, while reducing the central pile of similarly sized medium notes.
- `critical_important` is semantically solid but syntactically monotonous. Earlier drafts overused both `X is key` and invalid premodifier forms such as `key findings` or `key metrics`. Rework critical samples toward varied post-noun/predicate structures such as `timing proved key`, `benefits remain key`, `the evidence reviewers marked key`, `the requirement that is key is...`, table/list rows, and sentence-final complement uses. Avoid making `key among` a fingerprint.
- `critical_important` is too professional/analytical. Rework 15-30 samples toward everyday material: parenting, cooking, home repair, sports, school, travel, hobbies, gardening, shopping, neighborhood posts, personal finance, and casual advice.
- Cross-section ambiguity needs another pass. In lock samples, reduce or clarify terms like `key cabinet`, `key_tag`, and `key-control` when they could momentarily look like important/adjective `key`. In critical samples, avoid phrases like `key contact` where physical key-management readings are plausible.

Batch strategy for the next edits:

- Batch A, critical syntax/domain: modify about 35 samples, prioritizing lines 109-206. Replace professional memo cadence with more varied structures and everyday sources while preserving exactly 100 samples.
- Batch B, context-intro reduction: modify about 40 samples across all labels. Remove or naturalize opening labels where possible by starting inside the artifact, table, message, or raw page rather than naming the source.
- Batch C, messiness/length: expand roughly 15-25 samples into longer messy artifacts with pasted sidebars, footer residue, OCR/table collisions, email/thread fragments, or raw rows; shorten or leave abrupt several others so the length distribution has more tails.
- Batch D, ambiguity cleanup: specifically inspect `key cabinet`, `key_tag`, `key control`, `key contact`, `key column`, `key field`, `key evidence`, `key decision`, and all high-risk excluded senses. Rewrite any sample where a target occurrence could plausibly be taken outside its label. In the final dataset, `key column` and `key field` proved especially risky in music samples because they pull the occurrence toward data-schema meaning even when nearby rows are tonal.
- Batch E, final validation: rerun length distribution, exact-target presence, start-position checks, source-wrapper scans, high-risk excluded-sense scans, ASCII scan, and a harsh manual review against every `always_check.md` question.

Acceptance standard for the second pass:

- Fewer context-intro openings; more samples should simply be the text itself.
- Critical label should visibly include everyday forum/chat/list/post material, not mostly workplace analysis.
- Critical label should no longer be dominated by `X is key`; simple `key [noun]` attributive forms are invalid for the current file and should be rewritten as predicate/postpositive forms.
- More long samples should resemble `samples_-.yaml`: raw rows, footer pollution, broken extraction, unrelated sidebars, and abrupt continuations.
- Any exact `" key"` occurrence in longer words or fields must remain label-correct after the added mess.

## QA Checklist

Per sample:

- Contains exact lowercase token `" key"` at least once.
- Every occurrence of `" key"` has the target meaning, including occurrences inside longer lowercase words such as `keys`, `keyed`, `keycard`, `keychain`, `keyboard`, `keyword`, or `key_signature`.
- Does not start with the token and usually delays the first occurrence by several tokens.
- Is checked as parsed sample text, so line-initial `key:` and uppercase `Key` are not mistaken for successful target occurrences.
- Avoids curator-style source introductions unless they are naturally part of the artifact.
- Is plausible as web/SFT corpus text, with realistic messiness and no theatrical over-explanation.
- Avoids unrelated keyboard/button, cryptographic/API, database/config, answer-key, map-key, taxonomy-key, island/proper-name, and pitch-accuracy senses.
- Is valid YAML when inserted into `dsv2/samples_key.yaml`.

Per meaning:

- Exactly 100 samples.
- Lengths, source types, voices, formats, emotional registers, and token counts are visibly varied.
- No dominant opening pattern, topic cluster, or narrative template.
- Includes rough/partial/crawled material without simply labeling the source type.
- Has target tokens distributed across early, middle, and late positions, especially in longer samples.
- Includes short fragments, medium artifacts, and some long messy samples.
- Manually inspect high-risk cases where lock devices, important/central uses, musical tonal frameworks, keyboard buttons, software keys, answer keys, and data keys can appear near each other.

## Third-Pass Rework Notes

User critique after further review:

- Physical/access samples are strong in scope and format but still had too much `missing/stuck/wrong/lost -> action -> resolution`. Rework roughly 35-45 toward routine non-problem contexts: handoff logs, manuals, catalog rows, children's/fictional text, product copy, lease exhibits, neutral inventories, and historical descriptions.
- `critical_important` had a new fingerprint: corrective reveal framing such as `not X but Y`, `the key failure was not...`, and especially repeated `Key among...`. Rework roughly 25-35 into plain declarations, tables, lists, findings/metrics described before the token, agenda rows, care notes, recipe comments, sports possessions, and everyday decisions.
- `musical_tonal_framework` was too often a negotiation about transposition or someone using the wrong key. Rework roughly 20-30 into descriptive/analytical text: liner notes, catalog records, theory handouts, app rows, program notes, archive cards, and musicology fragments. Metadata fields are useful, but avoid `key field` and `key column` wording unless the occurrence still plainly means tonal framework rather than data schema.
- Equal per-label counts are inherited from `samples_-.yaml` and useful for balanced label training, but the real-world prior should be acknowledged: musical `key` is rarer in natural web corpora than lock/access and critical/important uses. Since the file format uses 100 samples per label, reduce the music label's internal overrepresentation of one rehearsal-negotiation situation rather than changing label counts mid-file.
- Context-intro overuse remains a dataset-wide risk. More samples should look like the artifact itself, with raw rows or clutter, rather than sentences explaining that a scan/export/footer/comment exists.

Current acceptance additions:

- `Key among` should be zero or near-zero; if it appears, it must look natural and isolated.
- Corrective `not X but Y` frames should be occasional, not the main rhetorical engine of `critical_important`.
- Music can include transposition, but it must not mostly be range negotiation by singers, worship teams, or conductors.
- Physical/access can include lost/stuck/wrong-key incidents, but routine possession, inventory, instruction, commerce, and description must be comparably visible.
- Source labels such as `export`, `scan`, `thread`, `note`, and `footer` should appear only where the surrounding artifact warrants them; otherwise convert them into the raw content they were describing.

## Final-Pass Learnings

These notes capture issues that required repeated fixes during the final rounds and should be treated as active guidance for future maintenance:

- Every exact `" key"` occurrence matters, not only the first one. Physical/access samples naturally repeat the token many times; scan all occurrences so a sidebar or row note does not drift into `key features`, `key rows`, `API key`, `answer key`, or another excluded sense.
- `critical_important` is intentionally narrower than ordinary English here. The final dataset uses postpositive/predicate adjective forms only. Valid multi-use samples can say `features that are key`, `alert timing is key too`, `notes stay key`, or `evidence reviewers marked key`; invalid cleanup targets include `key risks`, `key witness`, `key feature`, `key metric`, `key finding`, `key_result`, and similar field-name/premodifier forms.
- Adding more `critical_important` target density is useful, but do it by adding a second already-established important item after the first occurrence. Do not bolt on an isolated `key point` or `key takeaway` just to increase counts.
- Music samples need the tonal framework established before the target where possible. Strong disambiguators include `major`, `minor`, `tonic`, `cadence`, `chord`, `mode`, `modulation`, `capo`, `score`, `sounding`, `home`, `recorded`, `recital`, and named notes near the target.
- In music metadata, `key field`, `key column`, and similar phrases were a subtle failure mode: they make the exact token feel like a database/config key. Prefer `musical key`, `tonal key`, `recorded key`, `recital key`, or rewrite the row so `key` modifies the tonal value directly.
- Context-intro cleanup took several passes. Openings like `parenting thread export`, `wedding DJ request form`, `Pop review:`, `Field note:`, `hardware ticket says`, or `cold-weather paragraph before donation ask` often sound like curator labels even when plausible. Usually remove the source label and start with the artifact content itself.
- Web artifacts are strongest when embodied rather than narrated. Prefer actual rows, broken HTML, duplicate footer text, clipped chats, and pasted sidebars over prose such as `the scan says`, `the export shows`, or `the footer repeats`.
- The physical/access label became strongest after reducing the repeated arc `key missing/stuck/wrong/lost -> action -> resolution`. Preserve routine and incidental mentions: manuals, lease clauses, product rows, invoices, child/fiction text, travel reviews, evidence/property logs, game hints, and simple handoff text.
- The music label became strongest after reducing the repeated arc `what key is this in / can we transpose it`. Preserve non-specialist voices, reviews, program notes, streaming/app metadata, ear-training rows, historical notes, and harmonic-analysis prose.
- Mechanical checks that proved useful: parsed-YAML exact-token count, first-position statistics, suffix scan for ` key\w+`, critical premodifier regex, header/source-label scan, abstract-next contamination scan for non-critical labels, and length distribution.
