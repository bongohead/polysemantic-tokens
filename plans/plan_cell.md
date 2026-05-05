# Plan: Polytok Token `" cell"`

## Objective

Create `dsv2/samples_cell.yaml` with 100 realistic samples for each meaning label:

- `biological_cell`
- `spreadsheet_cell`
- `cell_phone`

Every sample must contain the exact token `" cell"` at least once. Every occurrence of `" cell"` inside a sample must match that sample's `meaning_label`.

This token is high-risk because lowercase `cell` appears as a standalone word, inside plural and inflected forms, as a prefix in unrelated words, and in many excluded senses: prison cells, cell blocks, cellmates, battery cells, button cells, dry cells, fuel cells, solar cells, memory cells, Jupyter notebook cells, HTML table cells, terror cells, cellular automata, cellars, cellos, cellulose, cellophane, celluloid, cellulite, and cellulitis. Treat every lowercase exact occurrence seriously, including occurrences inside longer words.

## Exact-String Notes

The target is a literal space followed by lowercase `cell`.

- ` cell`, ` cell,`, ` cell.`, ` cell's`, ` cells`, ` cellular`, ` cell-free`, ` cell_line`, ` cellType`, ` cellPhone`, ` cellphone`, ` cellphones`, ` cell_id`, ` cell:` and ` cell.value` contain the exact token and must be semantically correct for the active label.
- `Cell` with uppercase C, `cell` at the beginning of a sample or line without a preceding space, `T-cell`, `B-cell`, `single-cell`, `.cell`, `_cell`, `/cell`, `mycell`, and `precellular` do not by themselves satisfy the exact token, though they may appear as surrounding context if another exact `" cell"` occurrence is present.
- Indented code or table fragments can create target occurrences, such as `  cell: A1` or `    cell.value`. Use these only when the meaning is clear.
- Avoid relying on target-adjacent punctuation unless the literal substring is present. `("cell")` does not contain the target, but `a cell)` does.
- Avoid line-initial examples such as `cell phone policy` or `cell A1` if there is no later exact target. They may look relevant to a human reader but do not satisfy the token requirement.
- If a non-target uppercase or hyphenated form appears in a sample, keep it sense-compatible where possible so the excerpt remains semantically coherent.

## Realism Standard

Samples should feel like mixed C4/HPLT-style web data rather than curated examples. Use raw excerpts when plausible: biology papers, lab protocols, pathology notes, sequencing outputs, school worksheets, spreadsheet help pages, Excel formulas, Google Sheets support threads, Apps Script/openpyxl snippets, phone repair listings, emergency forms, carrier support chats, tower outage notes, scraped HTML, OCR/PDF fragments, emails, chat logs, tables, and partial comments.

Good data can be clipped, mundane, redundant, malformed, or surrounded by adjacent page residue. Include plausible artifacts such as table headers, repeated footers, old nav text, ad placeholders, cookie text, broken captions, timestamps, CSV rows, JSON snippets, OCR line breaks, forum quote markers, copied email headers, hidden spreadsheet columns, product specs, and app UI strings.

Avoid source-intro wrappers such as `biology example:`, `spreadsheet note:`, `phone listing:`, `the page says`, or `snippet:` unless such labels are genuinely part of the artifact. The sample should be the artifact itself, not a description of it.

## Distribution Guidance

Use approximate distributions, not exact quotas.

- Length: include a few very short fragments, many short and medium samples, and a meaningful minority of long messy samples.
- Token placement: do not start any sample with `" cell"`. In longer samples, ensure the target token appears late sometimes, not only in the opening sentence, first table cell, or first support field.
- Token density: use enough target tokens to make the meaning clear, but avoid stuffing. Biology and spreadsheet samples can naturally repeat `cell`; phone samples often need fewer repetitions unless they are policy, support, or outage artifacts.
- Source mix: include technical, educational, workplace, commercial, medical, informal, structured, newsy, crawled/OCR, and auto-generated styles.
- Voice and tone: vary between neutral machine output, terse notes, confused users, polished documentation, academic prose, annoyed support text, regulatory language, personal notes, ads, and raw logs.
- Completeness: not every sample should be self-contained. Some should start or end abruptly as if scraped from the middle of a page.
- Case: the target token is lowercase `" cell"`. Uppercase `Cell` can appear for realism, but it does not satisfy the target by itself and should not be relied on.
- Near-miss control: avoid unrelated words beginning with the same letters unless they are the active phone form `cellphone` or a clearly sense-aligned biological/phone `cellular` use.

## Build Strategy

Create samples in batches of about 20 per label, then audit the entire label before adding more. Early batches should establish high-certainty core examples; later batches should deliberately fill gaps in source type, length, voice, messiness, token position, and surface form.

For each 20-sample batch:

- Verify every exact `" cell"` occurrence manually, especially `cells`, `cellular`, `cellphone`, `cell_id`, `cell.value`, and `cell:` in structured text.
- Check that at least several samples place the target token late, not only in the first sentence or first row.
- Add a few structured or non-prose artifacts: CSV, JSON, code/config, tables, forms, logs, OCR, or copied webpage residue.
- Add at least one longer messy sample per label if the current label is becoming too clean.
- Remove samples that need a curator explanation to disambiguate the sense.
- Track topic clusters so the labels do not collapse into only stem cells, only Excel formulas, or only school phone policies.

## Retrospective Learnings From Iteration

These are the recurring failure modes found while building this token. Treat them as required checks before considering the file done.

- Literal start scans are not enough. A sample can pass `^cell` checks while still placing exact `" cell"` in the first few characters through openings like `A cell`, `Every cell`, `Single cell`, `active cell`, or `A cell phone`. Run a stricter early-placement scan and rewrite the strongest offenders with plausible artifact context.
- Curator-style wrappers creep in even after cleanup. Phrases like `From the old...`, `local news draft`, `product review`, `worksheet export`, or `the page says` should be removed unless the label is clearly part of the scraped artifact. Prefer raw headings, rows, timestamps, or body text.
- `cell_phone` is the easiest label to overfit. Repeated clusters appeared around coverage complaints, outages, broken/lost phones, repair tickets, family anecdotes, school/work/court policies, contact-form administration, evidence/legal intake, asset management, marketplace listings, and delivery-driver workflows. These are valid in moderation but should not dominate.
- Strong `cell_phone` diversity came from adding domains that were initially missing: fiction excerpts, academic/methods prose, historical directory text, advertising copy, medical/health reminders, travel fragments, elderly/accessibility setup notes, raw HTML, event logistics, privacy writing, media production, and mundane incidental mentions.
- The phrase `cell phone` can sound mechanical if repeated every time. Once phone sense is established, natural variants such as `my cell`, `her cell`, `the cell`, `company cell`, `cell number`, `contact cell`, `spouse's cell`, and `cell phone photo` help. However, standalone `cell` must remain clearly phone-related through nearby calls, SMS, screen, contacts, charger, camera, carrier, or device context.
- Do not force long `cell_phone` samples just to match biology/spreadsheet. Earlier long phone samples tended to become support-chat sprawl or quirky anecdote chains. Medium structured artifacts often improve realism more than oversized narratives.
- `spreadsheet_cell` naturally gravitates toward `cell X has problem Y` troubleshooting. Keep some of that because it is realistic, but offset it with code/API snippets, tutorials, imports, accessibility notes, audit exports, mobile UI bugs, OCR, validation rules, and workflow prose where cells appear incidentally.
- `biological_cell` can sustain high token density naturally, but it still needs checks for wrapper openings, early token placement, and accidental non-biology `cellular` or `cell-free` ambiguity. Clinical, lab, educational, sequencing, pathology, and environmental-monitoring fragments make this label strongest when mixed.
- Raw headings are acceptable when they are artifact text (`macro replay`, `root tip lab`, `PSAP quality review`, `library note`) rather than descriptions of why the sample exists. The line between artifact heading and curator label should be judged harshly.
- Repeated final checks should include: length distribution; exact-token presence; literal sample-start scan; stricter early-placement scan; excluded-sense scan; wrapper-start scan; and targeted cluster scans for the label that received the most critique.

Approximate source mix targets:

- `biological_cell`: roughly one quarter lab/protocol content, one quarter research/academic or clinical text, one fifth educational material, one fifth structured data/code/sequencing output, and the remainder forum, patient, product, or messy scraped fragments.
- `spreadsheet_cell`: roughly one quarter Excel/Google Sheets help or user support, one quarter formulas and worksheet artifacts, one quarter code/API/import/export snippets, and one quarter business/education/OCR/spreadsheet UI miscellany.
- `cell_phone`: mostly device, repair, contact-field, personal/chat, commercial, travel, form, and app/account artifacts. Carrier/network/data material is valid but should be a light minority, and coverage/tower/service complaints should remain sparse rather than forming a repeated narrative arc.

## `biological_cell`

Semantic rule: `" cell"` refers to a living biological cell or a directly cell-related biological concept. This includes whole cells, cell types, cell lines, cell culture, cell membranes, cell walls, cell cycle, stem cells, immune cells, blood cells, single cell measurements, cellular processes, and cell-free biological material when the term is used in a life-science context.

Good examples:

- `the stained cell showed a clear nucleus`
- `T cell activation increased after day 3`
- `red blood cells were counted manually`
- `day 3 cell culture medium changed at 09:00`
- `single cell RNA-seq reads failed QC`
- `worksheet page 2 covers cellular respiration`
- `the assay used cell-free DNA isolated from plasma`

Include:

- Lab and protocol text: cell culture, passaging, plating, viability assays, transfection, staining, microscopy, flow cytometry, Western blot setup, ELISA prep, CRISPR screens, organoids, and contamination checks.
- Research and academic prose: cell biology, microbiology, immunology, oncology, neuroscience, developmental biology, plant cell walls, bacterial cells, yeast cells, stem cells, apoptosis, mitosis, cell cycle, cell signaling, cell migration, and tissue sections.
- Clinical/pathology contexts: blood cell counts, sickle cell disease, tumor cells, epithelial cells, cervical smear notes, bone marrow reports, immune cell subsets, and specimen handling.
- Educational material: biology worksheets, flashcards, quiz questions, textbook fragments, lab reports, lecture notes, and student comments with mistakes.
- Structured and technical artifacts: scRNA-seq metadata, microscopy CSVs, assay plates, image-analysis logs, count tables, protocol checklists, dataset schemas, code using `cell_type` or `cell_id` for biological observations, and notebook outputs.
- Biological `cellular` forms when they mean cell-level or composed of cells: cellular respiration, cellular uptake, cellular morphology, cellular immunity, cellular debris, and cellular localization.

Exclude:

- Cell phones, cellular networks, cell towers, cell service, cell numbers used as phone contact fields, and `cellphone`.
- Spreadsheet cells, Excel/Sheets cells, HTML table cells, Jupyter notebook cells, UI grid cells, and generic table cells.
- Prison or jail cells, cell blocks, cellmates, monastery cells, sleeper/terror cells, battery cells, button cells, dry cells, fuel cells, solar cells, memory cells, storage cells, radio network cells, cellular automata, and game map cells.
- Unrelated prefix words: cellar, cello, cellulose, cellophane, celluloid, cellulite, cellulitis, and brand names that only happen to begin with `cell`.
- `cellular` when it means mobile-phone service, cellular automata, or telecom infrastructure.

Guidance:

- Keep the biology sense unmistakable by including organisms, tissues, assays, microscopes, plates, markers, stains, genes, specimens, culture conditions, or biological units.
- Use both singular and plural forms. `cells` will be common and valid only when it refers to biological cells.
- Do not make every sample an explanatory sentence about what a cell is. Raw protocols, count tables, comments, abstracts, code output, and OCR from lab sheets are better for diversity.
- Include different scales: molecular/cell process, whole-cell morphology, tissue sections, immune-cell populations, microbial cultures, plant cells, blood cells, and clinical specimens.
- Be careful with `cell line`: this is biological. Avoid nearby phrases like `cell line in spreadsheet` or `phone line` that could muddy the label.
- `cell-free` can be used sparingly for biological material such as cell-free DNA or cell-free extract, but the surrounding context must make the biology sense clear.

Planned diversity dimensions:

- Organism/source: human, mouse, zebrafish, plant, yeast, bacteria, algae, organoid, biopsy, blood, tissue culture, environmental sample.
- Cell type/process: T cell, B cell, stem cell, epithelial cell, red blood cell, neuron, macrophage, bacterial cell, plant cell wall, cell cycle, cell death, cell signaling, cell migration.
- Artifact type: protocol, lab notebook, paper abstract, peer review comment, microscopy caption, flow cytometry gate table, scRNA-seq metadata, CSV count export, code snippet, homework, clinical note, forum post, product/SDS fragment.
- Tone: neutral research prose, terse lab shorthand, confused student, clinical report, excited forum reply, warning label, broken OCR, automated analysis output.
- Length: short fragments like `count viable cells`, medium protocols or worksheets, and long messy excerpts with tables, repeated headers, and late target use.

## `spreadsheet_cell`

Semantic rule: `" cell"` refers to a cell in a spreadsheet worksheet: the row-column grid unit in Excel, Google Sheets, LibreOffice Calc, Numbers, or spreadsheet-like workbook files. It includes cell references, selected cells, formulas in cells, merged cells, cell formatting, cell ranges, protected cells, and spreadsheet APIs manipulating worksheet cells.

Good examples:

- `enter the tax rate in cell B4`
- `selected cells were merged before export`
- `row 1 cell A1 contains the invoice date`
- `copy the formula from cell D12`
- `openpyxl wrote cell.value as None`
- `Google Sheets protected the cell range by mistake`

Include:

- Spreadsheet UI and help text: Excel, Google Sheets, LibreOffice Calc, Numbers, fill handle, formula bar, selected cell, active cell, merged cells, protected cells, frozen rows, validation, conditional formatting, and named ranges.
- Worksheet artifacts: formulas, audits, budgets, gradebooks, timesheets, pivot table source ranges, hidden columns, cell references such as A1/B2/R1C1, pasted values, import cleanup, and formula errors.
- Code and APIs when worksheet context is explicit: Apps Script `getCell`, openpyxl `cell.value`, VBA `Range.Cells`, pandas-to-Excel export notes, xlsxwriter formats, Office scripts, CSV import mappers, and spreadsheet QA tests.
- Business and education contexts: invoices, inventory sheets, finance workbooks, class gradebooks, lab spreadsheets, schedules, data-entry forms, copied sheet comments, and LMS exports.
- Messy artifacts: copied spreadsheet rows, OCR from printed sheets, support tickets, forum posts, screenshot alt text, formula warnings, hidden worksheet notes, version comments, CSV/TSV fragments, and generated docs.
- Surface forms such as `cell`, `cells`, `cell A1`, `cell B12`, `active cell`, `merged cell`, `cell value`, `cell format`, `cell reference`, `cell range`, `cell formula`, `cell.value`, and `cell_id` when it denotes a worksheet coordinate.

Exclude:

- Biological cells, cell culture, cell lines, immune cells, blood cells, and biological `cellular` terms.
- Cell phones, cell numbers, cell service, cell towers, cell plans, `cellphone`, and cellular data.
- HTML table cells, Word table cells, PDF table cells, generic UI grid cells, calendar cells, game board cells, CSS `display: table-cell`, and Jupyter notebook cells unless the context is explicitly a spreadsheet worksheet.
- Prison/jail cells, cell blocks, cellmates, battery cells, button cells, dry cells, fuel cells, solar cells, memory/storage cells, cellular automata, and unrelated prefix words like cellar, cello, cellulose, and cellophane.
- Generic database rows/columns if there is no spreadsheet/workbook context.

Guidance:

- Make the spreadsheet sense clear with row/column language, cell coordinates, worksheet tabs, formulas, ranges, workbook apps, or spreadsheet APIs.
- Do not let this label become only polished Excel instructions. Mix support complaints, formula audits, copied workbook text, hidden columns, code snippets, printed sheets, teacher gradebooks, and financial workpapers.
- Use coordinates and formulas naturally, but avoid accidental arithmetic or other target-token issues only if they introduce unrelated `" cell"` forms.
- Code samples should include worksheet/workbook context. A generic variable named `cell` in an HTML parser or machine-learning grid is not enough.
- Avoid `table cell` unless the artifact is specifically a spreadsheet table inside Excel/Sheets. Plain HTML/Word/PDF table cells are off-label for this dataset version.
- Long samples should include some target tokens later in comments, error messages, or formula audit trails, not only in the first line.

Planned diversity dimensions:

- Spreadsheet app/source: Excel, Google Sheets, LibreOffice Calc, Numbers, Office Scripts, Apps Script, openpyxl, xlsxwriter, VBA, imported CSV opened as a worksheet.
- Feature area: formula reference, active selection, cell formatting, merged cells, protected ranges, data validation, conditional formatting, frozen panes, fill handle, pivot source, import/export, formula errors.
- Domain: finance, inventory, school grades, lab data, scheduling, payroll, fundraising, orders, CRM exports, sports stats, household budgets, compliance trackers.
- Artifact type: workbook notes, support ticket, formula bar text, code snippet, CSV/TSV row, OCR printout, screenshot alt text, QA checklist, auto-generated API docs, forum reply, email attachment thread.
- Tone: terse analyst note, confused user, automated warning, teacher instruction, developer debug output, finance audit comment, messy OCR, casual chat.
- Length: short fragments like `sheet note says cell C9 is locked`, medium support/forum excerpts, and long messy workbook audits with hidden rows and repeated footer text.

## `cell_phone`

Semantic rule: `" cell"` refers to a cellular/mobile phone, a cellphone, or directly related cellular telephone service and infrastructure. This includes cell phones, cellphone devices, cell numbers as contact phone numbers, cell service, cell signal, cell plans, cell carriers, cell towers, cell sites, cellular data, and cellular modems when the context is mobile telephony.

Good examples:

- `please list a cell phone number on the form`
- `my cellphone stopped charging after the update`
- `coverage notes say cell service drops near the ferry dock`
- `the cell tower behind the school is offline`
- `turn off cellular data before roaming`
- `staff may keep cell phones in lockers`

Include:

- Consumer and support contexts: cell phone repair, cracked screens, chargers, SIM cards, voicemail, contact forms, phone numbers, family plans, carrier bills, warranties, trade-ins, lost phones, device returns, and app permission complaints.
- Network/service material: cell service, cell signal, cellular data, cell tower, cell site, LTE/5G small cell, carrier outage, roaming, coverage maps, emergency calls, cellular modem, and mobile hotspot support.
- Policy and administrative text: school cell phone rules, workplace device policies, clinic intake forms, event waivers, emergency contact fields, travel checklists, rental agreements, and public notices.
- Commercial and product text: phone listings, repair shop ads, case/screen protector descriptions, prepaid plan pages, carrier emails, refurbished device specs, and app-store reviews.
- Messy artifacts: support chats, copied SMS/voicemail notes, outage dashboards, billing tables, contact exports, OCR forms, school handbooks, forum posts, repair tickets, scraped carrier pages, and newsletter fragments.
- Surface forms such as `cell phone`, `cell phones`, `cellphone`, `cellphones`, `cell number`, `cell service`, `cell signal`, `cell tower`, `cell site`, `cell plan`, `cell carrier`, `cell data`, `cellular data`, `cellular modem`, and `cellular network`.

Exclude:

- Biological cells, cellular respiration, cellular immunity, cell culture, cell lines, blood cells, and biological `cellular` uses.
- Spreadsheet cells, worksheet cells, Excel/Sheets cells, HTML table cells, and Jupyter notebook cells.
- Prison/jail cells, cell blocks, cellmates, battery cells, button cells, dry cells, fuel cells, solar cells, memory cells, storage cells, cellular automata, game map cells, terror cells, and monastery cells.
- `cell number` when it means the count or identifier of biological/spreadsheet/grid cells rather than a phone contact number.
- `cell site` or `cell tower` if the context is abstract geometry or a game grid rather than mobile telecom.
- Unrelated prefix words: cellar, cello, cellulose, cellophane, celluloid, cellulite, and cellulitis.

Guidance:

- Keep the mobile-phone sense explicit with words like phone, carrier, SIM, LTE, 5G, tower, signal, voicemail, charger, screen, roaming, contact number, data plan, or emergency call.
- Use `cellular` only for phone/network contexts in this label. If it could be biology, add telecom context or avoid it.
- Phone samples can be mundane and policy-heavy, so deliberately add repair tickets, carrier support, outage data, family messages, forms, classifieds, school handbooks, and device specs.
- `cell tower`, `cell site`, and `small cell` are valid when they refer to cellular phone infrastructure. For `small cell`, include carrier/5G/coverage context so it does not read as a biological or grid cell.
- `cell number` is valid in forms and contact records only when it clearly means a mobile phone number.
- Avoid letting sidebars introduce off-label biology or spreadsheet uses. A phone repair page with a finance table saying `cell B3` would be invalid.
- Second-pass correction: do not let `cell_phone` drift back into coverage complaints, dropped calls, tower permits, small-cell installations, or institutional `no cell phones` rules. Those are valid senses, but they should be occasional examples, not a dominant section identity.

Planned diversity dimensions:

- Device/service area: phone device, charger, screen, SIM/eSIM, voicemail, texting, data, roaming, coverage, tower/site, small cell, hotspot, family plan, carrier billing, emergency calls.
- Source type: contact form, school policy, support ticket, repair invoice, carrier outage page, product listing, app review, chat log, emergency notice, travel checklist, legal/admin form, OCR waiver, scraped carrier FAQ.
- Domain: families, schools, workplaces, clinics, rentals, travel, events, emergency management, rural coverage, elder care, repair shops, prepaid plans, construction/tower permits.
- Tone: annoyed customer, neutral policy, automated carrier text, casual family note, terse dispatcher record, sales copy, confused forum user, OCR form residue.
- Length: short fragments like `status bar says cell signal weak`, medium support or policy excerpts, and long messy pages with contact fields, billing rows, and late target use.

## Cross-Meaning Hazards

Inspect these cases manually during dataset creation:

- `cells`: biological units in `biological_cell`, worksheet grid units in `spreadsheet_cell`, usually not useful for `cell_phone` except inside `cellphones`.
- `cellular`: biology when it means cell-level living material; phone label when it means mobile telephony; exclude cellular automata and vague metaphorical uses.
- `cell phone`, `cellphone`, `cellphones`: phone label only.
- `cell number`: phone label when it is a contact number; biological or spreadsheet labels only if it means an identifier/count and the context is unmistakable. Prefer avoiding this phrase outside phone samples.
- `cell line`: biological label, not a phone line or spreadsheet line.
- `cell range`, `cell reference`, `cell formula`, `active cell`, `merged cells`, and `cell.value`: spreadsheet label when worksheet context is clear.
- `single cell`, `T cell`, `B cell`, `stem cell`, `red blood cell`, `cell culture`, `cell cycle`, `cell membrane`, and `cell wall`: biological label.
- `cell tower`, `cell site`, `small cell`, `cell signal`, `cell service`, and `cell plan`: phone/network label when mobile telecom context is clear.
- `table cell`, `HTML cell`, `grid cell`, `calendar cell`, `game cell`, and `Jupyter cell`: exclude from all three labels unless rewritten into a spreadsheet worksheet context.
- `battery cell`, `button cell`, `dry cell`, `wet cell`, `fuel cell`, `solar cell`, `memory cell`, `storage cell`, `load cell`, and `electrochemical cell`: exclude from all three labels.
- `jail cell`, `prison cell`, `holding cell`, `cell block`, `cellmate`, `terror cell`, `sleeper cell`, and `monk's cell`: exclude from all three labels.
- `cellar`, `cello`, `cellulose`, `cellophane`, `celluloid`, `cellulite`, and `cellulitis`: contain the exact prefix after a space but are not any requested sense. Avoid unless there is another valid target occurrence and the word is removed or not exact lowercase, which is usually not worth the risk.
- `cell_id` and `cell:` fields can mean biology, spreadsheet coordinates, phone network sectors, game grids, or database internals. Use only with strong surrounding context.

## Dataset Creation Strategy

Build `dsv2/samples_cell.yaml` in rounds of about 20 samples per label, then review and revise before adding the next round.

For each `biological_cell` round, deliberately cover several of:

- Lab protocols, microscopy/image analysis, flow cytometry, cell culture logs, scRNA-seq metadata, clinical/pathology notes, educational worksheets, research abstracts, peer review fragments, product/SDS text, forum questions, and raw count tables.
- Surface forms such as ` cell`, ` cells`, ` cellular`, ` stem cell`, ` T cell`, ` red blood cell`, ` cell line`, ` cell culture`, ` cell cycle`, ` cell membrane`, ` cell viability`, ` single cell`, and ` cell-free`.

For each `spreadsheet_cell` round, deliberately cover several of:

- Excel/Sheets support, workbook audit notes, formulas and references, hidden rows/columns, conditional formatting, merged cells, protected ranges, imports/exports, gradebooks, finance sheets, openpyxl/VBA/Apps Script snippets, OCR printouts, and user forum posts.
- Surface forms such as ` cell`, ` cells`, ` cell A1`, ` cell B12`, ` active cell`, ` selected cell`, ` merged cells`, ` cell value`, ` cell format`, ` cell range`, ` cell reference`, ` cell formula`, ` cell.value`, and ` cell_id`.

For each `cell_phone` round, deliberately cover several of:

- Phone repair, device listings, school/work policies, contact forms, carrier support, outage notices, coverage maps, cell towers/sites, family plan billing, travel roaming notes, emergency call guidance, support chats, OCR waivers, and scraped product/review pages.
- Surface forms such as ` cell phone`, ` cell phones`, ` cellphone`, ` cellphones`, ` cell number`, ` cell service`, ` cell signal`, ` cell tower`, ` cell site`, ` cell plan`, ` cell carrier`, ` cellular data`, ` cellular modem`, and ` cellular network`.

After each round:

- Search every exact `" cell"` occurrence and classify it manually.
- Search high-risk continuations and off-label forms: ` cellular`, ` cells`, ` cellphone`, ` cellphones`, ` cellar`, ` cello`, ` cellulose`, ` cellophane`, ` celluloid`, ` cellulite`, ` cellulitis`, ` cell number`, ` cell line`, ` cell range`, ` cell tower`, ` prison cell`, ` jail cell`, ` cell block`, ` cellmate`, ` fuel cell`, ` solar cell`, ` battery cell`, ` button cell`, ` dry cell`, ` load cell`, ` table cell`, ` Jupyter cell`, and ` cell_id`.
- Check that no sample starts with the target and that first target positions vary.
- Check that long samples contain some late target occurrences.
- Rebalance if a label is becoming too tidy, too explanatory, too biology-paper-heavy, too Excel-help-heavy, too school-phone-policy-heavy, or too centered on one domain.
- Validate YAML structure before continuing.

## QA Checklist

Per sample:

- Contains exact lowercase token `" cell"` at least once.
- Every occurrence of `" cell"` has the target meaning, including occurrences inside longer lowercase forms such as `cells`, `cellular`, `cellphone`, `cellphones`, `cell_id`, `cell.value`, and `cell:`.
- Does not start with the token and usually delays the first target by several tokens.
- Avoids curator-style source introductions unless they are naturally part of the artifact.
- Is plausible as web/SFT corpus text, with realistic messiness and no theatrical over-explanation.
- Avoids unrelated prefix words and off-label senses such as prison, cell block, cellmate, battery, button, dry, fuel, solar, load, memory, notebook, table, terror, cellar, cello, cellulose, cellophane, cellulite, and cellulitis.
- Is valid YAML when inserted into `dsv2/samples_cell.yaml`.

Per meaning:

- Exactly 100 samples.
- Lengths, source types, voices, formats, emotional registers, and token counts are visibly varied.
- No dominant opening pattern, topic cluster, or narrative template.
- Includes rough/partial/crawled material without simply labeling the source type.
- Has target tokens distributed across early, middle, and late positions, especially in longer samples.
- Includes short fragments, medium artifacts, and some long messy samples.
- Manually inspect high-risk cases where biological cells, spreadsheet cells, and cell phones can appear near each other or inside the same support/page artifact.

## Second-Pass Review: `cell_phone` Weaknesses

Date/time of this pass: 2026-05-04 evening, with final work held until after the requested 10:30 PM minimum.

Scope: addressed the weak `cell_phone` section after user review. The main failure modes were overrepresentation of coverage/signal/outage/tower material, repeated support-chat arcs, too many school/workplace no-phone policies, too-clean administrative voice, and long samples that only repeated the same coverage idea.

### Iteration Log

1. Re-read `always_check.md` and treated the checklist as the active standard, not background advice.
2. Re-read `dsv2/samples_-.yaml` for diversity calibration: raw math/code/OCR/thread fragments, not just polished examples.
3. Re-inspected the whole `cell_phone` block rather than only the complained-about lines.
4. Ran a length-distribution check and confirmed `cell_phone` was not wildly longer than other labels, but the content of long items was weak.
5. Ran coverage/service keyword scans and confirmed the user's complaint: coverage and telecom-infrastructure language was still visibly clustered.
6. Replaced an initial batch of 15 coverage, policy, and support samples with repair, lost-device, backup, product, insurance, travel, and family-message artifacts.
7. Re-ran distribution and coverage scans; coverage improved but still clustered.
8. Replaced another 21 samples, especially carrier outage, tower, small-cell, and repeated support-chat sequences.
9. Re-ran the scan and found the tail still had too many `cell service`, `cell signal`, `cell tower`, `small cell`, and outage arcs.
10. Replaced another 26 samples in the tail and policy cluster with trade-in, lost-and-found, permit-photo, app/login, maternity, jury, rental, and family-backup material.
11. Re-ran length distribution and found the cleanup had made `cell_phone` too compressed: p90 was too low and only one sample crossed the long threshold.
12. Expanded 6 short phone samples into longer messy non-coverage artifacts, including eSIM confusion, marketplace screenshots, recipe-comment derailment, volunteer QR chaos, and retail-return compatibility mess.
13. Re-ran extremes and found the long tail improved but the shortest phone samples were still too form-like.
14. Expanded 5 of the shortest phone samples into richer OCR/export/account artifacts without adding coverage complaints.
15. Audited openings and found too many genre labels like `repair ticket`, `Contact export`, and `billing page fragment`.
16. Removed or roughened 12 openings so more samples begin as raw rows, raw fields, or mid-artifact content rather than curator-style labels.
17. Ran off-label hazard scans for excluded senses such as cellar/cello/cellulose/prison/battery/fuel/table/Jupyter cells; no such hazards remained in this file from this pass.
18. Audited topic replacement patterns and caught a new duplicate: two soup-damaged phone samples.
19. Replaced one soup sample with a phone-language/screen-reader lock scenario.
20. Audited liquid-damage terms and found a secondary repair cluster around rain, lake, sink, leak, liquid, and corrosion.
21. Replaced 5 water/liquid-damage variants with cable spark, rideshare loss, battery swelling, stuck button, and train-platform damage scenarios.
22. Ran early-token-placement scans and nudged two phone samples whose first target occurrence was too abrupt.
23. Audited support/CSR phrasing after the main pass and converted one remaining support-chat sample into a raw car/Bluetooth note.
24. Audited lost/found replacements and changed one parent-group lost-phone sample into a birthday RSVP / wrong cell-number confirmation artifact.
25. Re-ran distribution and cluster scans after those changes; coverage/service/tower hits no longer appear in the phone section, while support and lost/found remain present but not dominant.

### Checklist Answers

1. Correct, unambiguous meaning: mostly yes after the pass. Every `cell_phone` exact lowercase occurrence I touched now points to phones, phone numbers, phone plans, phone data, phone repair, or phone-adjacent account/device contexts. I removed telecom-infrastructure cases that were valid but overdominant. Residual `cellular data` examples are phone-plan/app-settings contexts, not biology.

2. Diversity and messiness: much better. The section now includes contact exports, support snippets, app reviews, product Q&A, OCR intake forms, marketplace messages, repair forms, family chats, lost-and-found logs, trade-in audits, travel app failures, event volunteer SMS, and messy backup threads. It is still somewhat form/device-heavy, but no longer mostly carrier-service prose.

3. Voice diversity: improved sharply. There are annoyed reviewers, confused parents, casual chat participants, terse admins, clerks, automated portals, volunteers, support agents, and messy forum users. Harsh note: there are still many competent administrative notes; future passes could add more broken comments, short social posts, and malformed ecommerce text.

4. Token placement and density: acceptable. No sample starts with the exact target. I specifically scanned for early target placement and adjusted the worst phone cases. Some contact forms naturally put `cell` early, but longer samples also include later target occurrences.

5. Introductory phrases: improved but not perfect. I removed or roughened many opening labels. Some source-like headings remain because they are plausible artifact text, but the section no longer reads as uniformly curator-labeled.

6. Length diversity: acceptable after rebalancing. Current `cell_phone` distribution is roughly min 206, p25 256, median 277, p75 317, p90 471, max 792, average about 310.3; bucket mix is 17 short, 82 medium, 1 long. Harsh note: compared with the other two labels, `cell_phone` still has fewer very long examples, but that is preferable to recreating the old long carrier-outage problem.

7. No sample starts with target: yes. The start-target scan returned no samples beginning with lowercase `cell`, `cells`, `cellular`, or `cellphone`.

8. Repetitive arcs/templates: substantially improved. The old arc `cell phone exists -> service bad -> carrier/tower/fix` has been mostly removed. I also caught and fixed a new soup/liquid-damage repetition and reduced a water-damage repair cluster. Harsh note: repair/trade-in/contact-field material is now the main remaining cluster to watch.

9. Partial/incomplete artifacts: yes. Several samples start or end mid-artifact: raw CSV rows, OCR forms, collapsed replies, marketplace fragments, app reviews, lost-and-found logs, and exported chats.

10. Not only natural language: yes. The phone section now includes CSV-ish exports, contact tables, OCR forms, audit rows, photo logs, support macros, device setup checklists, and app/settings fragments.

11. Tone variation: improved. Neutral administrative text is still common, as it should be for web data, but there are also frustrated, confused, funny, informal, and all-caps-ish human moments. I specifically added messier parent/app/forum/marketplace cases to counter the calm-admin voice.

12. Domain balance: much better than before. Coverage/service/tower material no longer dominates; explicit coverage/service/tower keyword scans now mostly hit non-phone biology text or a small number of phone data-plan/settings examples. School/workplace no-phone policy is no longer a cluster; only a few policy-like phone settings remain.

13. Final semantic check: yes with residual caution. The remaining risky phone forms are `cell number`, `cell data`, `cellular data`, `cellphone`, and contact-export `cell` columns. I kept them in phone-number/phone-plan contexts. I did not find biology, spreadsheet, prison, battery, or unrelated-prefix contamination in the phone label during the final targeted scans.

### Residual Harsh Notes

- The section is now much less coverage-heavy, but it may have swung slightly toward repair/device/admin-contact artifacts. That is acceptable for this pass because the user specifically called out coverage and no-phone-policy dominance, but it is the next thing to watch.
- The long tail is cleaner than before but conservative: only one phone sample exceeds 750 characters. The p90 is now close to the spreadsheet label, so I am not forcing more length just to satisfy a bucket.
- The plan's original source-mix target overallocated network/tower material. The second-pass rule above supersedes that: phone network material is valid, but it should stay sparse.

## Third-Pass Review: 1 AM Diversity Pass

Date/time: 2026-05-05, continued until after the requested 1:00 AM floor.

Focus:

- Left `biological_cell` untouched because review found it excellent.
- Reduced `spreadsheet_cell`'s repeated troubleshooting shape by replacing several `cell X has problem Y` examples with tutorials, setup notes, teaching material, seed-list workflow, onboarding, and import-class material.
- Reduced `cell_phone`'s phone-in-distress and family-chaos flavor by replacing many lost/broken/repair/trade-in/family-drama samples with shorter incidental mentions in rosters, public notices, intake forms, event logistics, travel instructions, permit notices, alerts, and contact CSVs.

Harsh notes after this pass:

- `cell_phone` now has many more short incidental samples and no longer reads primarily like a support-anecdote anthology.
- Final post-1 AM distribution: `cell_phone` min 139, p25 187, median 244, p75 276, p90 316, max 508, avg about 246.0; bucket mix is 54 short and 46 medium, with no long samples. This is short-heavy compared with the other labels, but it is an intentional correction from the previous long/dramatic skew.
- Some device/problem contexts remain because they are natural for the meaning, but they are no longer the dominant organizing principle.
- `spreadsheet_cell` still has many real spreadsheet references and support artifacts, but the added incidental/tutorial samples soften the earlier IT-ticket feel.

## Fourth-Pass Review: `cell_phone` Distributional Diversity

Focus: addressed a remaining `cell_phone` pattern where too many samples still followed the institutional contact-management skeleton: field or checklist item, contextual note, footer/export glitch. Replaced a broad batch with non-form contexts while preserving the phone meaning for every exact ` cell` occurrence.

Added/rebalanced toward:

- News and civic text: distracted-driving ordinance, school-board liveblog, city council comment, public-comment transcript.
- Narrative and fiction-like prose: detective scene, airport delay note, dorm hallway transcript, middle-grade bus scene, movie-review notebook.
- Reviews and commercial text: tripod clamp review, budget cell phone review, power bank review, restaurant review.
- Emotionally varied user text: angry app-store review, privacy forum reply, group chat, repair counter conversation, repair-shop voicemail.
- Casual/incidentally phone-related contexts: movie theater recording, recipe phone-in-dough mishap, drone complaint with cell phone video, festival flashlights, infrared remote DIY tip.

Final check after this pass:

- `cell_phone` distribution: min 157, p25 194, median 226, p75 263, p90 307, max 476, avg about 240.7; 63 short and 37 medium.
- Exact-token presence check passed for all samples.
- Start-token scan passed; no samples begin with lowercase `cell`, `cells`, `cellular`, or `cellphone`.
- Excluded-sense scan passed.
- Coverage/service scan has only one phone-section hit, a story scene with `one bar`, not a repeated coverage-support topic.

Residual harsh note: `cell_phone` is now deliberately short-heavy and has no long samples. That is acceptable for this correction because the problem being fixed was repetitive, over-institutional contact management, but a future pass could add 2-3 genuinely different long phone samples, such as a news article, forum fight, or privacy essay, without returning to support-chat or contact-form structure.

## Fifth-Pass Review: Intro Removal and Phone Anti-Anecdote Pass

Date/time: 2026-05-05, continued through the requested 1:30 AM floor and final checks after 1:30 AM.

Focus:

- Removed or rewrote a large set of source-announcing openings across all three labels. Many samples now begin directly with rows, timestamps, protocol steps, comments, or prose instead of `draft`, `review`, `transcript`, `export`, `notes`, `text layer`, or similar wrapper text.
- Replaced many `cell_phone` samples whose main action was inconvenience, breakage, loss, quirky mishap, or family anecdote. Added flatter real-world phone uses: ticket scanning, product pages, evidence procedure, museum rules, privacy guidance, restaurant mobile pages, staff tables, SIM advice, event logistics, driver workflow, and orientation material.
- After the first phone rewrite made `cell_phone` too short-heavy, expanded several neutral samples into medium-length scraped artifacts without returning to support-chat or device-disaster arcs.

Checks run:

- `python scripts/check_length_distribution.py dsv2/samples_cell.yaml`
- exact-token presence scan for every YAML sample
- start-token scan for lowercase/uppercase `cell`, `cells`, `cellular`, and `cellphone`
- excluded-sense scan for prison, battery, fuel, solar, table, Jupyter, and unrelated-prefix senses
- targeted scan for removed phone-mishap terms such as storm drain, freezer, applesauce, bread dough, rideshare, and screen-stays-black

Final distribution after this pass:

- `biological_cell`: 100 samples; min 97, p25 238, median 274, p75 322, p90 488, max 978, avg 314.2; 1 very short, 34 short, 61 medium, 4 long.
- `spreadsheet_cell`: 100 samples; min 70, p25 224, median 274, p75 308, p90 461, max 809, avg 302.9; 1 very short, 32 short, 64 medium, 3 long.
- `cell_phone`: 100 samples; min 136, p25 178, median 205, p75 238, p90 363, max 528, avg 230.6; 81 short, 19 medium, 0 long.

### Checklist Answers

1. Correct, unambiguous meaning: yes by mechanical scan and manual spot check. The risky exact tokens in this pass are `cell-free`, `cellular`, `cell.value`, `cell number`, `cell data`, and `cellphone`; each is in the intended biology, spreadsheet, or phone sense. I did not find off-label prison, battery, table, Jupyter, or unrelated-prefix usage.

2. Diversity and messiness: improved, especially on starts. Samples now more often begin in medias res: rows, logs, raw code, timestamped chat, instructions, and body text. Harsh note: some first-line artifact headings remain because they are plausible text, but the earlier curator-label density was too high and has been cut substantially.

3. Voice diversity: improved in `cell_phone` because I removed some over-stylized anecdotes and added flatter institutional, commercial, privacy, ticketing, and workflow voices. Harsh note: neutral/procedural tone is now dominant in phone, which is realistic but risks blandness if pushed further.

4. Token placement and density: acceptable. No sample starts with the target form according to the start-token scan. Some short phone samples naturally place `cell phone` early, but longer samples include later occurrences in footers, notes, and policy text.

5. Introductory phrases: much better. This was the main defect. I removed dozens of explicit wrappers such as `local news draft`, `product review`, `forum thread`, `transcript cleanup`, `worksheet export`, `student lab report excerpt`, and similar labels. Harsh note: not every heading disappeared; raw scraped data can include headings, but I should assume future review will still catch more.

6. Length diversity: acceptable overall, but phone remains short-heavy. I intentionally recovered some medium phone samples after noticing the first pass overcorrected. Harsh note: `cell_phone` still has no long samples and 81 short samples; that is not ideal, but better than recreating long quirky/support anecdotes.

7. Avoid starting with token: yes. The scan for samples beginning with `cell`, `cells`, `cellular`, `cellphone`, and uppercase variants returned no hits after fixes.

8. Repetitive arcs/templates: improved. The phone section has fewer arcs based on lost/broken/dead phones, quirky mishaps, and form-field-plus-footer scaffolds. Harsh note: phone still has clusters around policies, scanning/tickets, and contact numbers, but none dominates as aggressively as the old inconvenience/anecdote cluster.

9. Partial/incomplete artifacts: yes. The file still includes clipped rows, raw tables, code fragments, OCR fragments, chat lines, footer contamination, duplicated fields, and samples that end without neat explanation.

10. Not only natural language: yes. Biology and spreadsheet already had strong structured variety; this pass preserved raw rows, code, CSV-like artifacts, app settings, staff tables, and checklists while removing explanatory wrappers.

11. Tone variation: more realistic after removing too much phone quirk. Most text is flat or procedural, with some annoyed, casual, nostalgic, confused, and policy-debate voices left in moderation. Harsh note: a little warmth remains in phone, but the previous sitcom-ish bits are mostly gone.

12. Topic/domain balance: better. `cell_phone` no longer centers on inconvenience, device distress, family chaos, or contact-form administration. Remaining domains include tickets, privacy, travel, commerce, civic policy, school procedure, event staff, driver workflow, repair accessories, and media creation.

13. Final semantic check: passed. All samples contain exact lowercase `" cell"` somewhere; start-token and excluded-sense scans passed; the phone-mishap scan no longer finds the specific quirky patterns called out in the review.

### Residual Harsh Notes

- `cell_phone` is still the weakest label by length distribution: no long samples, many short samples. The safer next improvement would be 5-8 genuinely medium/long neutral phone artifacts, not stories and not support chats.
- Some headings remain where they read like real artifact text. This is acceptable for now, but I should keep assuming there are still removable wrapper starts.
- Spreadsheet still has many troubleshooting references to specific cells because that is a realistic dominant usage. The incidental/tutorial additions help, but it is not as broad as biology.

## Sixth-Pass Review: `cell_phone` Format Extremes

Focus: addressed the remaining weakness that `cell_phone` was solid but too uniformly casual/everyday. Replaced 18 lighter short samples with heavier institutional, structured, academic, journalistic, and deeply scraped artifacts.

Added/rebalanced toward:

- Raw structured data: company cell phone asset CSV, MDM JSON records, library locker CSV, school device-status CSV, substitute emergency export.
- Dense institutional/legal text: evidence chain-of-custody, property release, device-search training language, school board minutes, public-safety PSAP quality review, FOIA dispatch log.
- Academic/journalistic prose: survey-methods paragraph, classroom cell phone restriction abstract, state audit reporting, article-style technology policy analysis.
- Messy web/scrape artifacts: HTML privacy page with footer/script residue, staff table/PDF split, OCR-like emergency and registration fragments retained.

Final distribution after this pass:

- `cell_phone`: 100 samples; min 136, p25 194, median 230, p75 355, p90 426, max 528, avg 269.9; 63 short, 37 medium, 0 long.
- Overall file still has 300 samples and the other two labels are unchanged in count and shape.

Checks run:

- `python scripts/check_length_distribution.py dsv2/samples_cell.yaml`
- exact-token presence scan for every sample
- start-token scan for lowercase/uppercase `cell`, `cells`, `cellular`, `cellphone`
- excluded-sense scan including prison/jail/holding, battery, fuel, solar, storage, table, Jupyter, and unrelated-prefix senses

Harsh note: the excluded-sense scan caught one self-inflicted error: a phone FOIA sample said `holding cell` while explaining a column name. I rewrote that to `custody location`; the follow-up excluded-sense scan was clean. `cell_phone` still has no long samples, but the medium bucket is now much stronger and more comparable in seriousness to the biology/spreadsheet labels without returning to support-chat or quirky-anecdote sprawl.

## Seventh-Pass Review: Policy Cluster and Surface Form

Focus: addressed two minor remaining `cell_phone` distribution issues: policy/restriction contexts were overrepresented, and the phrase `cell phone` appeared mechanically in places where natural text would switch to `cell`, `my cell`, `her cell`, or `company cell` after the phone sense was clear.

Changes:

- Replaced a broad set of school/court/camp/work restriction samples with incidental uses: directions, flower photos, oral-history archive text, market vendors using a phone for checkout, photo kiosk receipts, museum audio-guide comments, baggage updates, bus hotspot use, legal extraction timeline, student film demo, camp photo log, laundry-room timer confusion, volunteer contact exports, route checkout, and campus-paper filming.
- Preserved some institutional/legal structure where it adds format diversity, but shifted it away from rules and toward evidence handling, extraction timelines, contact exports, FOIA logs, and operational records.
- Added more natural standalone phone uses: `call my cell`, `from her cell`, `one cell`, `the cell`, `her cell went to sleep`, `counselor cell`, `cell pictures`, `Mina's cell rang`, `call cell after 3pm`, `company cell`, and `on her cell`.

Final distribution after this pass:

- `cell_phone`: 100 samples; min 136, p25 203, median 236, p75 346, p90 407, max 528, avg 268.1; 57 short, 43 medium, 0 long.

Checks run:

- `python scripts/check_length_distribution.py dsv2/samples_cell.yaml`
- exact-token presence scan for every sample
- start-token scan for lowercase/uppercase `cell`, `cells`, `cellular`, and `cellphone`
- excluded-sense scan including prison/jail/holding, battery, fuel, solar, storage, table, Jupyter, and unrelated-prefix senses
- targeted policy/restriction keyword scan to verify the old school/court/camp/work rule cluster was reduced

Harsh note: some phone-governance and safety language remains because real corpora do include evidence forms, contact fields, emergency instructions, and app-permission text. The section no longer feels dominated by school bans/courtroom rules/camp baskets/work policies, and the exact token now appears with a less monotonous surface form.

## Eighth-Pass Review: `cell_phone` Domain Breadth

Focus: addressed the remaining imbalance that the final label still leaned too much on evidence/legal, asset management, marketplace, school/parent communication, and delivery-driver contexts.

Changes:

- Replaced 8 overrepresented `cell_phone` sequences with formats and domains that were lighter in the section: advertising/raw HTML, fiction excerpts, medical reminder exports, historical directory prose, travel itinerary text, elderly/accessibility setup notes, and academic/travel survey methods.
- Kept the exact-token constraint by using natural phone-sense forms such as `cell phone`, `the cell`, `her cell`, `kitchen cell`, `cell number`, and `spouse's cell`.
- Avoided turning the additions into another inconvenience cluster. The new examples are mostly incidental or documentary rather than lost/broken/problem-phone anecdotes.

Final distribution after this pass:

- `cell_phone`: 100 samples; min 136, p25 203, median 236, p75 316, p90 407, max 528, avg 265.9; 56 short, 44 medium, 0 long.
- Overall file remains 300 samples with balanced label counts.

Checks run:

- `python scripts/check_length_distribution.py dsv2/samples_cell.yaml`
- exact-token presence scan for every sample
- start-token scan for lowercase/uppercase `cell`, `cells`, `cellular`, and `cellphone`
- excluded-sense scan including prison/jail/holding, battery, fuel, solar, storage, table, Jupyter, and unrelated-prefix senses

Harsh note: `cell_phone` is still less extreme than `biological_cell`; that is partly natural because the token appears in everyday prose more often than in lab-style artifacts. This pass specifically reduced domain sameness without bloating the section or reintroducing overly curated openings.

## Ninth-Pass Final Sweep: Checklist Closure

Focus: reread `always_check.md` and did a final pass across all labels for remaining checklist failures, especially wrapper starts, semantic ambiguity, and overrepresented `cell_phone` domains.

Final edits:

- Removed a remaining biology wrapper start (`From the old immunology handout`) and rewrote it as a raw handout/scan fragment.
- Replaced 4 more `cell_phone` samples from legal/driver-heavy contexts with medical pre-op instructions, vacation-rental raw HTML, fiction reading notes, and academic poster methods.
- Tightened one self-created ambiguous phrase from `cell memory question` to `memory B cell question`.

Final distribution after this pass:

- `biological_cell`: 100 samples; min 97, p25 238, median 274, p75 322, p90 488, max 978, avg 314.4; 1 very short, 33 short, 62 medium, 4 long.
- `spreadsheet_cell`: 100 samples; min 70, p25 224, median 274, p75 308, p90 461, max 809, avg 302.9; 1 very short, 32 short, 64 medium, 3 long.
- `cell_phone`: 100 samples; min 136, p25 204, median 237, p75 311, p90 407, max 528, avg 266.0; 56 short, 44 medium.
- Overall: 300 samples; 2 very short, 121 short, 170 medium, 7 long.

Final checklist answers:

1. Correct, unambiguous meaning: yes. Exact-token and excluded-sense scans passed, and the final manual spot check found no prison, battery, spreadsheet-in-phone, or phone-in-biology leakage.
2. Diversity and messiness: yes. The file includes lab notes, CSVs, chat logs, OCR, HTML, code, methods prose, forum fragments, tickets, instructions, exports, and incomplete artifacts.
3. Adequately dirty data: yes. There are raw structured rows, broken previews, copied footers, merged columns, scan artifacts, comments, thread residue, and partial pages. Harsh note: phone is still cleaner than biology, but no longer too uniformly anecdotal.
4. Token placement and density: acceptable. Every sample contains lowercase exact ` cell`, and the start-token scan passed. Many samples place the token after context rather than as the first word.
5. Introductory phrases: acceptable now. A targeted scan for obvious wrapper starts returned no hits. Some real headings remain (`Methods`, `Abstract`, status lines), but they function as artifact text rather than sample descriptions.
6. Length diversity: acceptable. Biology and spreadsheet have several long samples; phone has no long samples but a healthier medium bucket and avoids returning to bloated support-chat stories.
7. Avoid starting with token: yes. The scan for samples beginning with lowercase/uppercase `cell`, `cells`, `cellular`, and `cellphone` returned no hits.
8. Repetitive arcs/templates: much better. Spreadsheet still naturally contains many specific cell-reference troubleshooting cases, but it also has code, imports, instructions, OCR, accessibility, and API-like text. Phone no longer centers on policies, legal evidence, driver workflows, marketplace listings, or family anecdotes.
9. Incomplete artifacts: yes. Many samples start or end as fragments rather than polished explanations.
10. Not only natural language: yes. All labels include structured/non-prose examples appropriate to their meaning.
11. Tone variation: yes. The mix is mostly neutral/procedural with some confused users, terse logs, annoyed comments, academic prose, ad copy, fiction-like narration, and casual chat.
12. Topic/domain balance: acceptable. Final phone residual clusters exist, but none is large enough to dominate; the added medical, travel, fiction, raw HTML, advertising, elderly/accessibility, academic, and historical contexts improve the spread.
13. Final semantic check: passed. All exact ` cell` usages are meaning-label appropriate after the final wording fix.

Checks run:

- `python scripts/check_length_distribution.py dsv2/samples_cell.yaml`
- exact-token presence scan for every sample
- start-token scan for lowercase/uppercase `cell`, `cells`, `cellular`, and `cellphone`
- excluded-sense scan including prison/jail/holding, battery, fuel, solar, storage, table, Jupyter, and unrelated-prefix senses
- targeted wrapper-start scan
- targeted overrepresented-domain scan for remaining phone clusters

Harsh final note: the one residual weakness is that `cell_phone` still has no truly long samples, while the other two labels do. I am choosing not to force one in at the end because earlier long phone samples tended to become support-chat or anecdote sprawl, and the current medium examples carry the phone sense cleanly without overfitting to a new template.

## Tenth-Pass Final Sweep: Early Token Placement

Focus: reran the checklist with harsher attention to the instruction that the target should not appear immediately at the start of a sample. The earlier start-token scan only caught samples beginning literally with `cell`; this pass also checked for exact `" cell"` appearing within the first few text characters.

Final edits:

- Delayed early biological starts such as `A cell is`, `Every cell`, `Single cell`, `The cell-free`, `B cell`, `Stem cell`, `Sickle cell`, `Count cells`, `yeast cells`, and `blast cells` by adding plausible artifact context or rewriting the opening sentence.
- Delayed early spreadsheet starts such as `merged cells`, `Selected cell`, `active cell`, `expected cell`, `click cell`, `select cell`, and `Old file: cell`.
- Delayed early phone starts such as `A cheap cell phone`, `A cell phone camera`, `The reporter's cell`, `The budget cell phone`, `Your cell phone location history`, and `Take a cell phone photo`.
- Removed one wrapper-ish wording introduced during the previous pass (`Clinic handout notes`) by making the sentence itself carry the content.

Final distribution after this pass:

- `biological_cell`: 100 samples; min 97, p25 238, median 274, p75 324, p90 488, max 978, avg 315.3; 1 very short, 33 short, 62 medium, 4 long.
- `spreadsheet_cell`: 100 samples; min 84, p25 227, median 276, p75 308, p90 461, max 809, avg 304.3; 1 very short, 30 short, 66 medium, 3 long.
- `cell_phone`: 100 samples; min 136, p25 204, median 237, p75 316, p90 407, max 528, avg 266.2; 56 short, 44 medium.
- Overall: 300 samples; 2 very short, 119 short, 172 medium, 7 long.

Checks run:

- `python scripts/check_length_distribution.py dsv2/samples_cell.yaml`
- exact-token presence scan for every sample
- literal start-token scan for lowercase/uppercase `cell`, `cells`, `cellular`, and `cellphone`
- excluded-sense scan including prison/jail/holding, battery, fuel, solar, storage, table, Jupyter, and unrelated-prefix senses
- wrapper-start scan
- stricter early-placement scan for exact `" cell"` near the beginning of sample text

Final harsh note: the remaining early-ish occurrences are mostly realistic raw fragments (`field 1 cells counted`, `Panel A: cell spreading`, `Section 2: cell C9`) where delaying the token further would make the artifact less natural. The stronger constraint failures have been fixed.
