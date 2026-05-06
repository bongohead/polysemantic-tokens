# Plan: Polytok Token `" stock"`

## Objective

Create `dsv2/samples_stock.yaml` with 100 realistic samples for each meaning label:

- `financial_instrument`
- `inventory`
- `cooking_broth`

Every sample must contain the exact token `" stock"` at least once. Every occurrence of `" stock"` inside a sample must match that sample's `meaning_label`.

This token is new, so there is no old `ds/samples_stock.yaml` to preserve. The v2 file should be built from scratch with the same standard as `dsv2/samples_-.yaml`: semantically strict, realistically varied, messy enough to resemble C4/HPLT-style web text, and free of curator explanations that only describe the sample source.

## Exact-String Notes

The target is a literal space followed by lowercase `stock`.

- ` stock`, ` stocks`, ` stock's`, ` stocked`, ` stocking`, ` stockroom`, ` stocktake`, ` stockout`, ` stockpile`, ` stockholder`, ` stockbroker`, ` stock exchange`, ` stock market`, ` stock split`, ` stock option`, ` stock cube`, ` stockpot`, ` stock photo`, ` stock footage`, ` stock firmware`, ` stock ROM`, ` stock solution`, ` stock culture`, ` stock answer`, ` stock character`, and indented fields like `  stock:` all contain the exact target visually or as a substring and must be handled deliberately.
- Uppercase `Stock`, line-initial `stock` with no preceding space, `_stock`, `.stock`, `/stock`, `-stock`, and camelCase such as `currentStock` do not by themselves satisfy the exact lowercase leading-space target.
- Lookalikes such as `restock`, `restocking`, `overstock`, `backstock`, `livestock`, `out-of-stock`, and `no-stock` usually do not contain the exact target because `stock` is not preceded by a literal space inside the parsed sample. They can appear as surrounding context only if another exact `" stock"` occurrence satisfies the label.
- A newline is not a space. A line beginning `stock: 14` does not contain the target unless it is indented or preceded by another character plus a space.
- Longer words are high risk. Avoid relying on `stocky`, `stockade`, `stocking` as clothing, `stockholm`, `stockpot`, `stockyard`, `stockfish`, `stockinette`, `stockbroker`, `stockholder`, or `stockroom` unless the whole exact occurrence is valid for the active label. Even financial-domain longer words such as `stockbroker` and `stockholder` should not be the only target occurrence; the target should still appear as an equity/instrument term elsewhere in the sample.
- ` stocks` is especially dangerous because it can mean multiple financial securities, inventory reserves, cooking supplies, theater punishment devices, livestock/breeding lines, or raw material reserves. Classify every plural occurrence manually.
- Do not start any sample with the target. If a realistic artifact begins with lowercase `stock`, include a few preceding tokens from the same artifact or use a different excerpt.
- Watch adjacent sidebars. A brokerage sample with a recipe widget saying `chicken stock`, an inventory page with a `stock market` news ad, or a recipe page with `in stock` shopping text is invalid unless the unrelated exact occurrence is removed.

## Realism Standard

Samples should feel like mixed web data, not polished teaching examples. Use direct artifacts where possible: brokerage statements, SEC filing fragments, investor forums, earnings-call transcripts, portfolio exports, warehouse pick tickets, ecommerce pages, ERP logs, pharmacy shelf notes, library/vendor records, recipe cards, kitchen prep lists, food safety sheets, restaurant inventory, cooking blogs, OCR/PDF fragments, chats, emails, HTML, CSV, JSON, dashboards, product feeds, newsletters, and scraped pages with residue.

Good data can be clipped, mundane, redundant, malformed, or surrounded by irrelevant page residue. Include plausible artifacts such as table headers, copied navigation, cookie text, broken captions, ad placeholders, old footers, pagination, mobile notification text, forum quote markers, merged comments, OCR line breaks, fields that wrap badly, and repeated boilerplate.

Avoid source-intro wrappers such as `brokerage note:`, `warehouse record:`, `recipe excerpt:`, `the page says`, `copied from`, or `snippet from` unless such labels are genuinely part of the artifact. The sample should be the artifact itself, not a description of the artifact.

## Distribution Guidance

Use approximate distributions, not exact quotas.

- Length: include a few very short fragments, many short and medium samples, and a meaningful minority of long or extra-long messy samples.
- Rough length shape per label: around 5-10 tiny scraps, a large middle of short/medium samples, 20-30 longer artifacts, and several very long noisy scrapes or logs. Do not force exact counts if semantic quality would suffer.
- Token placement: do not start any sample with `" stock"`. In longer samples, ensure target occurrences appear late sometimes, not only in the first sentence or first table row.
- Token density: use enough target tokens to make the meaning clear, but avoid stuffing. Financial and inventory artifacts can naturally repeat `stock`; broth samples often need fewer repetitions unless they are recipe/prep pages.
- Source mix: include technical, commercial, workplace, educational, newsy, informal, structured, crawled/OCR, and auto-generated styles.
- Voice and tone: vary between neutral machine output, terse operations notes, anxious investors, annoyed shoppers, bland product feeds, excited cooks, confused forum replies, official filings, and raw logs.
- Completeness: not every sample should be self-contained. Some should start or end abruptly as if scraped from the middle of a page.
- Case: the target token is lowercase `" stock"`. Uppercase `Stock` can appear for realism, but it does not satisfy the target by itself.
- Surface form balance: avoid making the financial label mostly `stock price`, the inventory label mostly `out of stock`, or the broth label mostly `chicken stock`.
- Equal sample counts are for balanced training data, not a claim about real-world frequency. Inventory and financial uses are probably much more common than culinary broth in broad web text, so the broth label needs extra internal variety to avoid sounding artificially amplified.

Approximate source mix targets:

- `financial_instrument`: about one quarter brokerage/portfolio/account text, one quarter investor/news/market commentary, one fifth SEC/company-finance/compensation material, one sixth forums/social/newsletters, and the remainder tables, APIs, transcripts, tax material, education, and messy scraped artifacts.
- `inventory`: about one quarter ecommerce/product availability, one quarter warehouse/retail/ERP operations, one fifth internal procurement/manufacturing/service parts, one sixth customer support/pharmacy/library/field-service contexts, and the remainder CSV, JSON, OCR, labels, chat, and automated notifications.
- `cooking_broth`: about one quarter recipes and cooking instructions, one fifth restaurant/prep/food-service text, one fifth grocery/product/label material, one sixth home cooking/forum/chat material, and the remainder culinary education, food safety, OCR, menus, transcripts, and messy scraped pages.

## `financial_instrument`

Semantic rule: `" stock"` refers to an equity security or ownership share in a company, or to financial instruments and market contexts where the word denotes those securities collectively. This includes common stock, preferred stock, voting stock, capital stock, treasury stock, restricted stock, stock grants, stock options when the equity underlying is explicit, stock splits, dividends on stock, stock tickers, stock price, stock exchange listings, and stock market discussion when equities are the clear referent.

Good examples:

- `portfolio row: common stock, qty 42, cost basis 18.40`
- `the fund sold bank stocks and bought utility stocks`
- `Form 4 table says restricted stock vested on 06/01`
- `after the stock split, the option strike was adjusted`
- `chat says the stock was halted before the open`
- `ticker feed: stock price, bid, ask, volume`

Include:

- Brokerage and portfolio contexts: holdings, lots, cost basis, DRIP, dividends, share counts, ticker symbols, watchlists, stop orders, long or short stock positions, margin notices, stock loan, wash sales, stock quote rows, Form 1099-B rows, Schedule D notes, and taxable gains.
- Company finance and regulation: common stock, preferred stock, voting stock, capital stock, treasury stock, stock compensation, restricted stock units, employee stock purchase plans, stock option plans, stock warrants when equity-linked, stock grants, stock splits, buybacks, IPO/S-1/10-K/8-K language, cap tables, transfer agents, par value, authorized shares, and shareholder records.
- Market/news contexts: stock price, stock index only when individual equities are also present, stock exchange, stock market, sector stocks, halted stock, penny stock, meme stock, blue-chip stock, ADRs, volume, float, short interest, and earnings reaction.
- Education and advice: personal finance lessons, tax guides, retirement allocation, investor newsletters, analyst notes, classroom material, risk disclosures, and forum replies.
- Messy artifacts: CSV exports, JSON quote APIs, broker app notifications, SEC table OCR, earnings-call transcript fragments, email alerts, Reddit/forum posts, scraped finance pages, comment threads, calculator widgets, and stale ad/footer collisions.

Exclude:

- Inventory or availability: `in stock`, `out of stock`, `stock count`, `stock room`, `stock levels`, warehouse `stock_on_hand`.
- Cooking broth: `chicken stock`, `beef stock`, `vegetable stock`, `fish stock`, `stock cube`, `make stock`.
- Raw materials, paper, film, photos, or generic supply: `card stock`, `paper stock`, `film stock`, `stock photo`, `stock footage`, `bar stock`, `lumber stock`, `seed stock`.
- Livestock, breeding stock, plant stock/rootstock, family lineage, racial/ancestral stock, and stock animals.
- Gun stock, rifle stock, walking stick stock, theater punishment stocks, and `laughing stock`.
- Fixed expressions and default/template uses: `put stock in`, `take stock of`, `stock answer`, `stock phrase`, `stock character`, `stock image`, `stock music`, `stock sound`, `stock firmware`, `stock ROM`, `stock app`, `stock keyboard`, and `stock up` unless the exact occurrence is separately financial.
- Longer-word accidents such as `stocking` clothes, `stocky`, `stockade`, `stockholm`, and `stockpot`.

Guidance:

- Make the equity/security sense unmistakable through shares, tickers, brokers, exchange listings, SEC forms, dividends, vesting, split ratios, float, shareholder records, or trading language.
- Do not make this label all retail-investor chatter. Include official filings, compensation plans, tax statements, broker CSVs, APIs, transcripts, and dull financial tables.
- Be careful with `stock market` and `stock index`: they are valid only when the securities/equities sense is clearly active, not as a vague synonym for the economy.
- `stock option` and `restricted stock` are valid financial-instrument contexts, but avoid samples where `option` turns the target into a different derivative-only focus unless the equity share relationship is clear.
- `stockbroker`, `stockholder`, and `stock analyst` are useful surrounding context, but the target occurrence in those longer words is role/person/context rather than the instrument itself. Include them only alongside clearer instrument uses such as `common stock`, `stock price`, or `stock shares`.
- In long scraped samples, remove ecommerce sidebars saying `in stock`, recipe widgets saying `chicken stock`, and generic `stock photo` captions.

Planned diversity dimensions:

- Instrument/surface form: common stock, preferred stock, voting stock, capital stock, restricted stock, treasury stock, stock grant, stock option, stock warrant, stock split, stock dividend, stock certificate, stock quote, long stock, short stock, penny stock, blue-chip stock, meme stock, ADR stock, bank/utility/tech stocks.
- Setting: brokerage account, SEC filing, corporate equity plan, investor forum, tax worksheet, retirement plan, finance classroom, analyst note, earnings transcript, quote API, portfolio app.
- Source type: holdings CSV, Form 4/10-K/S-1 fragment, cap table, transfer-agent row, 1099-B statement, broker alert, news article, chat thread, newsletter, spreadsheet, JSON response, tax statement, app notification, slide text, OCR table.
- Tone: flat compliance, excited retail trader, anxious employee, skeptical analyst, terse broker export, confused tax filer, promotional newsletter, official disclosure.
- Length: short ticker fragments, medium posts or emails, and long messy pages with tables, comments, quote widgets, and footer residue.

## `inventory`

Semantic rule: `" stock"` refers to goods, materials, parts, products, supplies, or units held for sale, storage, use, replenishment, or distribution. This includes availability status, counts on hand, shelf stock, warehouse stock, back stock, safety stock, cycle stock, dead stock, stockroom text, stockouts, stocktaking language, stock keeping unit text when availability/inventory is the meaning, restocking language when the exact occurrence is `stock`, and stock records in ERP/ecommerce/retail systems.

Good examples:

- `site banner says only 3 left in stock`
- `cycle count: stock on hand 18, damaged 2`
- `pharmacy note says reorder when stock falls below 6`
- `sku,warehouse,available stock,reserved stock`
- `the blue size sold out but back stock is still in aisle 9`
- `ERP row: stock_status=low, stock_level=4`

Include:

- Retail and ecommerce: in stock, out of stock, low stock, stock status, stock alerts, back stock, shelf stock, product availability, variant counts, substitutions, store pickup, and replenishment.
- Warehouse and operations: stock count, stock on hand, stock levels, stock item, stock number, stock card, spares stock, stock adjustment, stock transfer, safety stock, buffer stock, cycle stock, dead stock, obsolete stock, stock ledger, stock control, stocktake/stocktaking, stockout, stockroom, bin locations, receiving, cycle counts, pick tickets, and inventory audits.
- Industry and institutional contexts: pharmacy, hospital supply, school cafeteria, library/cataloging when copies are inventory, service parts, manufacturing materials, maintenance stores, rental equipment, lab consumables, and field trucks.
- Structured artifacts: ERP exports, Shopify/WooCommerce feeds, CSV/TSV rows, JSON APIs, barcode scanner logs, POS reports, email alerts, procurement notes, shelf tags, invoices, and warehouse chat.
- Messy operational text: partial pick lists, damaged labels, automated reorder emails, support tickets, marketplace listings, stale product cards, mobile app errors, OCR forms, and low-context staff messages.

Exclude:

- Financial securities or market contexts.
- Cooking broth, soup base, bouillon, and recipe liquid.
- `stock up` as a phrasal verb unless the exact target means goods held in inventory and every occurrence fits.
- Raw material categories not framed as held inventory, such as `paper stock`, `card stock`, `film stock`, `bar stock`, `lumber stock`, or `rolling stock`.
- Lab/science fixed phrases such as `stock solution`, `stock culture`, `stock standard`, `cell stock`, and `viral stock` unless the exact occurrence is clearly an inventory count or availability status rather than the biological/chemical stock concept.
- Animals, livestock, breeding stock, seed stock, plant/rootstock, and genetic stock.
- `stock photo`, `stock image`, `stock footage`, `stock music`, `stock answer`, `stock character`, and generic template/default uses.
- Default configuration and generic product variants such as `stock firmware`, `stock ROM`, `stock launcher`, `stock keyboard`, `stock tires`, `stock exhaust`, and `stock car` racing unless inventory availability is explicitly the meaning.
- Gun stock, rifle stock, theater punishment stocks, `laughing stock`, and idioms like `take stock`.
- Employee/person terms such as `stocker` or `stock clerk` if the exact target refers to the worker rather than goods.

Guidance:

- Make inventory status unmistakable through SKUs, counts, quantities, warehouses, shelves, bins, availability, reorder points, reservations, sales channels, stockouts, transfers, or replenishment.
- Do not make this label only ecommerce product copy. Include warehouses, hospitals, pharmacies, school kitchens, libraries, repair vans, manufacturing, rental counters, and nonprofit supply closets.
- `stocked` is valid when it means goods are present on a shelf or in a store. Avoid `well-stocked with jokes` or other metaphorical extensions.
- `stockroom` is valid only when the room stores inventory; avoid using it as mere setting if no inventory sense is active.
- In long samples, remove finance widgets such as `stock market news`, recipe lines such as `vegetable stock`, and image captions such as `stock photo`.

Planned diversity dimensions:

- Item domain: electronics, apparel, groceries, medicine, lab supplies, spare parts, books, tools, janitorial supplies, restaurant ingredients, school supplies, emergency kits, rental gear.
- Inventory surface form: in stock, out of stock, low stock, available stock, back stock, safety stock, cycle stock, dead stock, spares stock, stock item, stock number, stock card, stock on hand, stock count, stock level, stock adjustment, stock transfer, stock ledger, stock control, stocktake, stockout, stockroom.
- Setting: warehouse, retail floor, ecommerce backend, pharmacy, hospital, school, library, repair shop, factory, restaurant, nonprofit pantry, field service truck, marketplace seller.
- Source type: product card, ERP CSV, scanner log, purchase order, support ticket, chat, shelf label, reorder email, API JSON, pick ticket, audit sheet, app error, OCR form.
- Tone: flat machine export, frustrated customer, rushed warehouse lead, polite support reply, terse buyer note, automated alert, confused small seller, regulatory or audit language.
- Length: tiny availability fragments, medium operational notes, and long messy records with product rows, comments, ads, headers, and duplicated footers.

## `cooking_broth`

Semantic rule: `" stock"` refers to cooking broth or liquid base made by simmering bones, meat, seafood, vegetables, aromatics, or similar ingredients, including concentrated or packaged forms used as broth. This includes chicken stock, beef stock, vegetable stock, fish stock, brown stock, white stock, shrimp stock, shellfish stock, veal stock, turkey stock, mushroom stock, master stock, dashi-style stock, stock reduction, and culinary instructions for making or using stock.

Good examples:

- `add 2 cups chicken stock and simmer uncovered`
- `the sauce broke after the stock reduced too far`
- `freezer label says turkey stock, 1 quart, 11/28`
- `prep list: roast bones for brown stock before lunch`
- `rice pilaf uses vegetable stock instead of water`
- `chef note says strain the stock through cheesecloth`

Include:

- Recipe and cooking instructions: soups, stews, sauces, gravy, risotto, braises, rice, ramen, pho, gumbo, demi-glace, pan sauces, reductions, and deglazing with stock.
- Stock types and technique: chicken, beef, veal, pork, fish, seafood, shrimp, shellfish, turkey, duck, ham, mushroom, vegetable, brown, white, master stock, ramen stock, dashi-style stock, court bouillon-adjacent text only when `stock` is the target, bones, mirepoix, aromatics, simmering, skimming, straining, chilling, defatting, reducing, freezing, and labeling.
- Food-service contexts: prep sheets, restaurant batch logs, HACCP/cooling records, culinary school handouts, catering notes, commissary production, freezer inventory when every exact `stock` means broth, and kitchen chat.
- Product/grocery contexts: boxed stock, canned stock, stock concentrate, stock cube, stock powder, low-sodium stock, store-brand stock, ingredient labels, substitutions, and shopper questions.
- Messy artifacts: recipe blogs with ads, OCR cookbooks, caption fragments, YouTube transcript, shopping lists, kitchen Slack/chat, menu prep rows, nutrition labels, product reviews, email chains, and broken HTML.

Exclude:

- Financial securities or stock market text.
- Inventory/availability, especially `in stock`, `out of stock`, `stock room`, `stock levels`, and freezer inventory where `stock` means supply rather than broth.
- `stockpot` when it means the pot itself, not the broth. A sample can mention a pot, but every exact `stock` occurrence must refer to broth.
- `livestock`, breeding stock, plant/rootstock, seed stock, paper/card stock, film stock, stock photo/footage/music, gun stock, theater stocks, and `laughing stock`.
- Generic `broth` without exact target does not satisfy the token.
- `vegetable stock` is valid as broth; `vegetable stock` as grocery inventory of vegetables is not. Keep nearby cooking verbs or ingredient measures.
- `stock cube` is valid only when it is a bouillon/broth concentrate, not a warehouse cube, SKU cube, or finance metaphor.

Guidance:

- Make the culinary liquid sense unmistakable through cups/quarts, simmering, bones, mirepoix, soup, sauce, risotto, gravy, stockpot contents, straining, reducing, cooling, freezing, or ingredient lists.
- Do not make this label only polished recipes. Include kitchen production logs, freezer labels, restaurant prep sheets, student culinary notes, grocery reviews, subtitles, OCR cookbooks, and chaotic recipe-blog pages.
- Balance common `chicken stock` with beef, vegetable, fish, shrimp, shellfish, turkey, veal, mushroom, brown, white, ham, duck, master, ramen, dashi-style, and concentrated stocks.
- Avoid cross-contamination with inventory by not writing `we have stock in stock`, `stock is out of stock`, or product availability sidebars.
- In long recipe samples, remove marketplace lines saying `in stock`, finance ads about `stock picks`, and caption text such as `stock photo`.

Planned diversity dimensions:

- Liquid type: chicken, beef, veal, pork, fish, shrimp, shellfish, seafood, turkey, duck, ham, mushroom, vegetable, brown, white, master, ramen, dashi-style, roasted, clear, concentrated, low-sodium.
- Use case: soup, sauce, gravy, risotto, braise, rice, ramen, pho, gumbo, pan sauce, stuffing, beans, stew, reduction, demi-glace, baby food, vegetarian substitute.
- Setting: home kitchen, restaurant prep, culinary school, catering kitchen, grocery shelf, food blog, old cookbook, meal kit, hospital kitchen, freezer label, family message thread.
- Source type: recipe card, prep list, HACCP cooling log, product label, OCR cookbook, subtitle transcript, forum comment, shopping list, nutrition table, Slack/chat, email, broken HTML page.
- Tone: calm instructional, harried chef, nostalgic family note, confused beginner, blunt product review, automated menu export, messy OCR, promotional recipe copy.
- Length: short ingredient fragments, medium recipe steps, and long messy pages with ads, comments, temperature logs, labels, and repeated recipe-card residue.

## Cross-Meaning Hazards

Inspect these cases manually during dataset creation:

- ` stocks`: financial plural when equities/securities; inventory reserves when goods/supplies; cooking only if multiple broth batches/types are explicitly meant. Exclude old punishment-device or breeding-line senses.
- ` stock market`, `stock price`, `stock ticker`, `stock quote`, `stock split`, `common stock`, `preferred stock`, `voting stock`, `capital stock`, `restricted stock`, `treasury stock`, `stock grant`, `stock option`, `stock warrant`, `stock exchange`, `stock portfolio`: financial label when equity/security context is clear.
- ` in stock`, `out of stock`, `low stock`, `available stock`, `back stock`, `safety stock`, `cycle stock`, `dead stock`, `spares stock`, `stock item`, `stock number`, `stock card`, `stock on hand`, `stock count`, `stock level`, `stock transfer`, `stock ledger`, `stock control`, `stocktake`, `stockroom`, `stockout`: inventory label when goods/supplies are on hand or unavailable.
- ` chicken stock`, `beef stock`, `vegetable stock`, `fish stock`, `shrimp stock`, `shellfish stock`, `brown stock`, `white stock`, `master stock`, `dashi-style stock`, `stock concentrate`, `stock cube`, `stock powder`, `make stock`, `strain the stock`, `reduce the stock`: cooking broth label when culinary liquid is clear.
- ` stock photo`, `stock image`, `stock footage`, `stock music`, `stock sound`, `stock answer`, `stock phrase`, `stock character`, `stock firmware`, `stock ROM`, `stock app`, `stock launcher`: generic/template/default sense, excluded.
- ` paper stock`, `card stock`, `film stock`, `bar stock`, `lumber stock`, `rolling stock`: raw material or equipment category, excluded unless a future label covers it.
- ` stock solution`, `stock culture`, `stock standard`, `cell stock`, `viral stock`, and similar lab/science uses: excluded unless the exact occurrence separately refers to inventory availability/counts.
- ` livestock`, `breeding stock`, `seed stock`, `plant stock`, `rootstock`: animal/plant lineage or agricultural material, excluded. Note that `livestock` usually does not contain the exact target, but `breeding stock` and `seed stock` do.
- ` gun stock`, `rifle stock`, `shoulder stock`: firearm part, excluded.
- ` stock car`, `stock tank`, `stock saddle`, `stock dog`, and `stock horse`: racing, ranch, or animal-work senses, excluded unless the exact occurrence separately fits one of the three labels.
- `take stock`, `put stock in`, `laughing stock`, `stock-still`, `stock answer`, `stock up`: idiom or verb/phrase, excluded unless the exact occurrence separately fits one of the three labels.
- `stockpile`: inventory label only when goods/supplies are held for sale, storage, or distribution. Generic hoards, military reserves, nuclear stockpiles, and emergency reserves without inventory framing should usually be excluded.
- `stocked`: inventory label when shelves/goods are present. Avoid `stocked` in cooking-broth samples because phrases like `freezer stocked with chicken stock` mix an inventory occurrence with a broth occurrence and should be rewritten.
- `stocking`: inventory/restocking only when meaning adding goods; clothing `stocking` is excluded.
- `stockroom`: inventory label when the room stores goods; not valid for financial or broth labels.
- `stockpot`: normally pot object, excluded for broth label unless the exact target occurrence elsewhere in the sample is broth and the `stockpot` occurrence is removed or rewritten.
- `stockbroker`, `stockholder`, `stockholder equity`, and `stock analyst`: financial-domain context, but avoid using the longer word as the only target occurrence because it names a person/role/accounting category more than the instrument.
- Uppercase `Stock` in page titles or company names does not satisfy the exact target but can distract manual review.

## Dataset Creation Strategy

Build `dsv2/samples_stock.yaml` in rounds of about 20 samples per label, then review and revise before adding the next round.

For each `financial_instrument` round, deliberately cover several of:

- Brokerage holdings, SEC/company filings, stock-compensation documents, tax/cost-basis records, investor forums, news/commentary, quote APIs, earnings transcripts, classroom finance examples, and portfolio app snippets.
- Surface forms such as `common stock`, `preferred stock`, `voting stock`, `capital stock`, `restricted stock`, `treasury stock`, `stock grant`, `stock price`, `stock quote`, `stock split`, `stock option`, `stock warrant`, `stock market`, `stock exchange`, `stock ticker`, `stock portfolio`, `penny stock`, and `blue-chip stock`.

For each `inventory` round, deliberately cover several of:

- Ecommerce availability, warehouse counts, retail floor notes, pharmacy/hospital supplies, manufacturing parts, school/library/service stock, ERP exports, product cards, scanner logs, support tickets, procurement emails, and shelf labels.
- Surface forms such as `in stock`, `out of stock`, `low stock`, `available stock`, `stock on hand`, `stock count`, `stock level`, `stock transfer`, `safety stock`, `cycle stock`, `dead stock`, `spares stock`, `stock item`, `stock number`, `stock card`, `back stock`, `stock ledger`, `stock control`, `stocktake`, `stockout`, and `stockroom`.

For each `cooking_broth` round, deliberately cover several of:

- Recipes, kitchen prep sheets, restaurant batch logs, grocery/product labels, culinary school notes, home cooking chats, recipe blog pages, OCR cookbook fragments, subtitles, product reviews, and HACCP/cooling records.
- Surface forms such as `chicken stock`, `beef stock`, `vegetable stock`, `fish stock`, `shrimp stock`, `shellfish stock`, `brown stock`, `white stock`, `master stock`, `dashi-style stock`, `stock concentrate`, `stock cube`, `stock powder`, `make stock`, `strain the stock`, `reduce the stock`, and `stock reduction`.

Suggested batch rotation:

- Batch 1: high-signal core examples with some raw structure, making sure each label boundary is clean before adding mess.
- Batch 2: structured artifacts: finance CSV/API/filing tables, inventory ERP/pick/scanner rows, and broth prep/HACCP/product-label rows.
- Batch 3: informal and social sources: investor forums, support chats, store complaints, kitchen texts, recipe comments, newsletters, and rough email chains.
- Batch 4: long messy pages with late target occurrences, sidebars carefully scrubbed of cross-label `stock` senses, and abrupt starts/ends.
- Batch 5: gap filling for underused domains, short fragments, unusual but valid surface forms, and final distribution repair.

After each round:

- Search every exact `" stock"` occurrence and classify it manually, including occurrences inside longer lowercase words or compounds such as `stocks`, `stocked`, `stocking`, `stockroom`, `stockout`, `stockholder`, `stockbroker`, `stockpot`, and indented `stock:` fields.
- Scan for high-risk excluded strings: `stock photo`, `stock image`, `stock footage`, `stock music`, `stock answer`, `stock phrase`, `stock character`, `stock firmware`, `stock ROM`, `stock launcher`, `stock keyboard`, `stock solution`, `stock culture`, `stock standard`, `stock car`, `stock tank`, `stock saddle`, `card stock`, `paper stock`, `film stock`, `bar stock`, `lumber stock`, `rolling stock`, `breeding stock`, `seed stock`, `plant stock`, `rootstock`, `gun stock`, `rifle stock`, `take stock`, `put stock in`, `laughing stock`, `stock-still`, `stocky`, `stockade`, `stockholm`, `stockfish`, `stockinette`, and `stockpot`.
- Check that no sample starts with the target and that the first exact target is not always near the beginning. A sample that starts with line-initial lowercase `stock` is also suspicious even though it does not contain the exact leading-space token at character 0.
- Check that longer samples include late target occurrences.
- Rebalance if a label is becoming too tidy, too essay-like, too retail-investor-heavy, too ecommerce-availability-heavy, too `chicken stock`-heavy, or too dependent on one source type.
- Search for repeated openings and templates such as `The stock`, `I bought`, `The warehouse`, `This recipe`, `Add chicken stock`, `According to`, `The investor`, `The product page`, and `In the`.
- Validate YAML structure before continuing.
- In final QA, parse the YAML and inspect parsed text strings, not only the raw file. Escaped newlines and indentation can change whether a visible `stock` has a literal preceding space.

## First-Pass Generation Red Flags

Because this token is new, the first generated batches should be reviewed especially hard for these failure modes:

- Too many clean explanatory sentences. Replace a large fraction with raw rows, tables, comments, clipped pages, partial logs, and abruptly cut artifacts.
- Too many source labels at the front. `brokerage note`, `warehouse record`, `recipe card`, and similar labels are acceptable only when the surrounding text plausibly contains them; otherwise start directly in the table, message, recipe, page body, or row.
- Too many samples where the first target appears in the opening phrase. Later target placement matters, especially in long finance pages, product feeds, and recipe/blog scrapes.
- Financial samples collapse into `the stock went up/down`. Add ownership/share structure: quantities, lots, vesting, voting rights, transfer agents, dividends, cap tables, tax rows, and SEC boilerplate.
- Financial samples use `stock market` as a generic mood word. Keep shares/equities close by through tickers, portfolios, common/preferred stock, exchange listings, or trading fields.
- Inventory samples collapse into customer-facing `out of stock` notices. Add receiving, cycle counts, low-stock alerts, damaged/reserved quantities, stock ledgers, pharmacy or hospital supplies, and internal stockroom text.
- Inventory samples accidentally become raw-material or template/default senses. `paper stock`, `bar stock`, `stock firmware`, and `stock photo` are not the requested inventory meaning unless the exact occurrence is separately an availability/count term.
- Broth samples collapse into `add chicken stock`. Add stock reductions, brown/white stock technique, freezer labels, HACCP cooling logs, grocery product labels, master stock, seafood stock, and messy recipe comments.
- Broth samples accidentally mix with availability. Product pages often say boxed chicken stock is `in stock`; that exact `in stock` occurrence is inventory and invalid for the broth label.
- Longer samples include sidebars from a different label. Finance articles can have stock-photo captions; ecommerce pages can have market-news modules; recipe pages can have `in stock` purchase buttons.
- Do not rescue mixed-sense samples by making the main sentence correct. `the stock rose, image via stock photo`, `chicken stock is back in stock`, and `stock count includes boxed vegetable stock` are all invalid because at least one exact occurrence belongs to another label.
- Too many human voices sound competent and calm. Force dull machine exports, anxious retail traders, annoyed shoppers, harried cooks, support agents, official forms, confused beginners, and abrupt no-context fragments.
- Too many complete stories. Some samples should start mid-table, end after a broken line, include footer junk, or omit the resolution.

## Plan Audit Notes

Latest self-review of the plan:

- The three labels are meaning-bounded enough to support strict review: equity/security, goods/supply inventory, and culinary broth.
- The exact-string section covers the main token-specific danger: `stock` often appears inside longer words and fixed phrases whose meaning is outside all three labels.
- The plan excludes several attractive but wrong senses: stock photo/media, stock character/template, default firmware/ROM/app uses, lab stock-solution/culture uses, paper/card/film/bar stock, livestock/breeding/seed/rootstock, ranch/racing stock-car uses, gun stock, idioms, stockpot-as-pot, and "take stock" reflection.
- Source-mix targets should prevent the next phase from collapsing into three obvious defaults: retail trading chat, ecommerce `out of stock` notices, and polished chicken-stock recipes.
- The biggest future sample audit is side contamination. Recipe and ecommerce pages commonly include availability widgets; finance pages commonly include `stock photo` captions; product pages can include market-news or recipe-ad sidebars.
- The second biggest audit is exact-target presence. Line-initial `stock:` and uppercase `Stock` look convincing but do not satisfy the literal leading-space lowercase token.
- Residual risk: `financial_instrument` can become too market-commentary-like. Force official filings, portfolio exports, tax rows, compensation docs, and APIs.
- Residual risk: `inventory` can become too product-card-like. Force dull operational records, institutional supply contexts, and raw count tables.
- Residual risk: `cooking_broth` can become too recipe-polished. Force restaurant prep, food safety, product labels, OCR cookbooks, grocery reviews, and kitchen chats.
- Later review tightened line-initial `stock` handling, lookalikes that do not contain the exact token, default/template senses such as `stock firmware`, lab/science fixed phrases such as `stock solution`, and the mixed-sense trap in `freezer stocked with chicken stock`.
- The next phase should treat any sample with two different `stock` senses as invalid even if one occurrence is strongly correct. The labels are per-sample, not majority vote.

Dataset-build audit notes after iterative creation:

- The completed draft has 100 samples per label and passed parsed-YAML length checks, exact-target presence checks, no-start-with-target checks, and ASCII checks.
- Manual semantic fixes removed metalinguistic broth occurrences such as `not stock` / `says stock` when they were talking about spelling rather than the liquid, removed the inventory wrong-sense phrase `stock clerk`, and replaced ambiguous catalog-code uses such as `stock number` where the intended inventory meaning was weak.
- Surface-form concentration is much lower than the first full draft. `preferred stock`, `chicken stock`, and `stock on hand` were specifically reduced; `common stock` and `in stock` remain common because they are realistic, but they no longer dominate the same structural template.
- Length distribution is now close across labels: medians are in the same narrow band, and each label has a mix of short, medium, and a few long samples. A few very-short scraps remain intentionally for abrupt scrape realism; there is still no extra-long bucket.
- Source-wrapper openings were aggressively reduced by starting directly with rows, chat lines, HTML, timestamps, instructions, or page body text. Remaining apparent wrapper starts are mostly raw table/log openings or plausible artifact titles, not universal `intro\ntext` scaffolding.
- Cross-label scans found no actual broth phrases inside financial/inventory samples and no real inventory availability phrases inside broth samples. Apparent high-risk hits are either valid target-sense occurrences or have been rewritten.
- A later left-context audit rewrote weak first occurrences so the meaning is usually established before the target: `this stock` became domain-specific forms like `airline stock` or `bank stock`, bare `stock grant/options/sale` gained employee/company cues, inventory `no stock` cases gained item cues such as `pump-seal stock`, and broth cases like `hot stock`, `shop's stock`, and `add stock` gained culinary cues such as `vegetable stock` or `ramen stock`.
- A final ambiguity pass removed text-reference uses such as `stock mention`, `stock line`, `stock rows`, `stock page`, and `uses stock as`, then tightened weak first occurrences such as `stockroom`, `stock_status`, `ending stock`, `stock cube`, `make stock`, `the stock`, `brown stock`, `white stock`, and `master stock` so the left context establishes the requested sense before the exact token.
- A later distribution pass replaced dozens of repetitive correction-arc samples. Finance lost several dense stock-type stacks and gained raw quote/API/code fragments plus more incidental one-stock mentions. Inventory lost many `item/status/quantity/discrepancy` rows and gained Liquid/PHP/JSON/config snippets, reviews, news, and neutral supply descriptions. Cooking lost a large batch of repeated `warm/dilute/taste/salt/reduce` advice and gained more labels, menus, comments, family logistics, transcripts, and non-instructional mentions.
- A follow-up cooking-broth pass targeted the remaining cozy/narrator problem directly. Roughly three dozen warm domestic, family/comment, and intro-labeled samples were replaced or hardened into cafeteria production logs, HACCP cooling records, food-service purchase orders, clinical diet orders, product-spec records, R&D trial rows, food-science lab notes, procurement templates, menu costing sheets, CSV/JSON/ASR artifacts, and angry product reviews. The `stalk` autocaption motif was removed.
- Final sweep tightened residual checklist issues: source-label openings in cooking were converted to raw rows where easy, `term: stock` was changed so culinary meaning is clear before the exact target, and inventory `stock card` phrases were rewritten to avoid the `stock car` substring hazard while preserving the inventory meaning.
- Final length-parity repair checked `python scripts/check_length_distribution.py dsv2/samples_stock.yaml`, then lengthened targeted short cooking-broth rows with cold fields such as lot IDs, allergen columns, validation rows, and lab/status snippets. Final bucket counts are now close: cooking 65 short / 35 medium, financial 64 short / 33 medium / 1 long, and inventory 60 short / 38 medium.
- A last left-context sweep caught `def stock_weight(...)`, where the first exact target appeared inside a bare identifier before the financial sense was established. Rewriting it as a company-stock allocation snippet confirmed that code-heavy samples need the same left-context audit as prose.
- A subsequent strict first-occurrence pass tightened a few remaining term-dependent cases: employee-stock options gained equity-comp context, a bare ticker quote gained `equity quote`, restricted/deferred stock rows gained broker or compensation context, inventory `stock_qty` rows gained sellable/inventory cues, and `safety stock` gained imported-valve inventory context.
- That strict pass briefly reintroduced a few label-ish openings while fixing clarity. The final version smoothed those into in-artifact cues such as hashtag text, broker-message prose, compensation-ledger wording, and inventory-target wording rather than curator prefixes.
- The remaining biggest risks are subtler: finance still has many formal equity-plan/company-finance contexts, inventory still has a visible operations/dashboard flavor, and broth still has recipe/cooking-instruction pressure despite added product labels, family messages, diet boards, old print, grocery reviews, forum posts, captions, and incidental household contexts.

Reusable learnings from this token:

- Exact-substring hazard scans are necessary but need judgment. Valid phrases such as `stock card`, `stock carton`, and `stock containers` can trip broader excluded strings like `stock car`; if an easy rewrite preserves meaning, rewrite to reduce review noise.
- The first exact `" stock"` occurrence deserves a separate left-context audit. A later disambiguating phrase does not rescue a weak first occurrence such as `term: stock`; prefer `culinary stock`, `company stock`, `formula stock`, or another left cue before the target.
- Removing cozy narration can accidentally make a label too terse. When hardening a section into institutional or machine-like text, length should be restored with realistic fields, measurements, timestamps, lot codes, allergen statements, and validation rows rather than explanatory prose.
- Source-label openings tend to creep back in under new names. `HACCP cooling record`, `rice_cooker_program.csv`, `support transcript`, and similar starts should be converted to raw rows when the artifact still reads naturally without the label.
- Left-context fixes should not default to labels like `equity comp thread:` or `broker alert:`. Prefer cues that are naturally part of the text itself: hashtags, UI copy, ledger wording, field names, item categories, ticker/quote context, or ingredient/allergen fields.
- Repetition can hide under semantic correctness. Cooking samples were correct for the broth sense but still repeated `warm/dilute/taste/salt/reduce` advice; finance was correct but stacked stock types; inventory was correct but repeated item/status/discrepancy rows. Audit content arcs, not only labels.
- Metalinguistic uses are risky even when they mention the right domain. Prefer actual object uses over phrases like `stock mention`, `stock line`, `stock reference`, or `word stock`.
- A cold/institutional rewrite should not erase all human tone. Keep a few reviews, chats, and messy personal artifacts per label, but make sure they do not become the dominant emotional register.

## QA Checklist

Per sample:

- Contains exact lowercase token `" stock"` at least once.
- Every occurrence of `" stock"` has the target meaning, including occurrences inside longer lowercase words such as `stocks`, `stocked`, `stocking`, `stockroom`, `stockholder`, `stockbroker`, `stockpot`, and `stock_status`.
- Does not start with the token and usually delays the first exact occurrence by several tokens; aim for the first exact target after character index 8 unless a raw artifact has an unusually good reason.
- Does not visually start with lowercase `stock` either. Line-initial `stock:` may be realistic in a table, but it cannot be the only apparent target and should usually be preceded by context from the same artifact.
- Is checked as parsed sample text, so line-initial `stock:` and uppercase `Stock` are not mistaken for successful target occurrences.
- Avoids curator-style source introductions unless they are naturally part of the artifact.
- Is plausible as web/SFT corpus text, with realistic messiness and no theatrical over-explanation.
- Avoids unrelated financial/inventory/broth cross-contamination and excluded media, raw-material, animal, plant, firearm, idiom, clothing, and place-name senses.
- Is valid YAML when inserted into `dsv2/samples_stock.yaml`.

Per meaning:

- Exactly 100 samples.
- Lengths, source types, voices, formats, emotional registers, and token counts are visibly varied.
- No dominant opening pattern, topic cluster, or narrative template.
- Includes rough/partial/crawled material without simply labeling the source type.
- Has target tokens distributed across early, middle, and late positions, especially in longer samples.
- Includes short fragments, medium artifacts, and some long messy samples.
- Manually inspect high-risk cases where financial securities, inventory availability, cooking broth, stock media, raw materials, livestock/agriculture, idioms, and longer-word hazards can appear near each other.
