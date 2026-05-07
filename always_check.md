First, create a `plan_[token].md` file for the token:
- Make sure you understand the meaning and what to include/exclude in terms of meaning for each meaning_label.
- Think carefully about realistic distribution in SFT-style text like C4/HPLT for each meaning_label.
- Write out a concrete set of dimensions you'll ensure diversity on and different types of text you'll include for each menaing_label. Iterate and improve on this several times.
- Consider length distributions, but don't overfixate on making these exact as long as they're approximately right.
- You can always refer to `dsv2/samples_-.yaml` as an example of one that has good diversity and meaning-label-appropriate token usage. You can see in this sample that distributions are diverse but also appropriate; 

Then go ahead and make the `dsv2/samples_[token].yaml` file and start to iteratively improve it. This will take a while; 10-20 iterative improvements and 50+ tool uses is normal.

In general, I recommend doing 20 per label at a time, going back then making sure all of them (including your new 20 and old sequences) follow below guidelines each time, and iterating until they do, then doing another 20 until you reach 100. Each time, make sure you analyze these questions genuinely and seriously, making changes as needed:

1. Is every usage of the token with the correct, unambiguous meaning? Avoid having the token of interest be placed in "unnatural" positions where its meaning is ambiguous - using realistic distributions will help with this.
2. Is there diversity in the type/messiness of the sequences? The amount of "messiness" should correspond to realistic distributions of the source in C4-style data, though you should keep in mind SFT-style data is generally messy:
3. Are the sequences adequately dirty, mixing in unique/messy data? For example of things that add diversity:
    - Raw code (perhaps cryptic), config, and build/error output. Source files, Dockerfiles, Makefiles, package.json, YAML configs, .env files, SQL dumps, JSON responses, stack traces, CI/CD logs, compiler warnings, raw CSV/TSV rows, etc.
    - Web scraping artifacts and raw HTML/XML. Partial HTML tags, breadcrumbs, cookie banners mid-text, footer boilerplate merged into body, ad placeholders, pagination artifacts, sidebar content merged into main column, RSS remnants, etc.
    - Academic and research text. LaTeX source, arXiv metadata, inline citations, peer review fragments, dense jargon-heavy prose, table captions separated from tables, raw math without natural language, chunks of proofs, etc.
    - Social media and forum posts. Nested replies, ">" quoting, vote counts inline, user signatures, edit notes ("Edit: nvm figured it out"), moderator tags, post metadata, hashtags, @mentions, poor formatting, etc.
    - Chat and messaging logs. Discord/IRC/Slack with timestamps and roles, interleaving speakers, emoji reactions as text, "(edited)" markers, bot responses mixed in, missing thread context, etc.
    - Email fragments and newsletters. Forwarding chains, partial headers, out-of-office replies, mailing list footers, newsletter boilerplate, corporate signatures with legal disclaimers, etc.
    - Ecommerce, listings, and commercial text. Product specs, star ratings as text, Craigslist ads, job postings with salary ranges and EEO boilerplate, pricing page fragments, app store descriptions, etc.
    - Auto-generated and templated text. Shipping notifications, CI summaries, Dependabot PRs, changelogs from commits, cron job emails, auto-generated API docs, README badges as text, GDPR boilerplate, etc.
    - Transcripts and subtitles. YouTube auto-captions without punctuation, SRT timestamp blocks, podcast transcripts with "[crosstalk]"/"[inaudible]", meeting diarization labels ("SPEAKER_02:"), etc.
    - News, journalism, and wiki/reference text. Datelines, correction notices, photo credits, Wikipedia citation markers, "[citation needed]", disambiguation notices, flattened infobox data, stub notices, etc.
    - Tabular and structured data as text. CSV rows, Markdown tables, spreadsheet exports with merged-cell artifacts, flattened headers, nutritional info blocks, box scores, etc.
    - UI strings, captions, and presentation fragments. Button labels, push notifications, error dialogs, image alt text, slide extracts with sparse bullets, slide numbers inline, speaker notes mixed in, etc.
    - Educational and instructional content. Quiz questions with options, rubrics, syllabus fragments, LMS exports, tutorial steps, textbook examples, student work with errors, etc.
    - Personal notes, informal docs, and miscellaneous. Stream-of-consciousness, to-do lists, half-finished drafts, recipe blog preambles, Usenet posts with nested quoting, government minutes, legal clause numbering, localization file entries, collaborative doc comments, etc.
3. Is there diversity in voices, not just a "competent explainer" voice? Ads, confused people, automated junk, terse messages without context, common human errors, and so on.
4. Did you use the token of interest enough, especially late in the sequences? Did you avoid stacking them frequently at or near the start of the sequence? Did you avoid starting any sequences with the token of interest — it should not occur until at least a few tokens in.
5. Did you avoid putting "introductory phrases" like "A textbook says:..", "The page source has..." at the start of sequences? Do not start samples with curator-style labels like "receipt:". Real scraped data just starts, it doesn't label itself. The sample should be the text, not a description of the text. the mess, don't describe it.
6. Is there enough diversity in the sequence length, especially longer sequences?
7. Did you avoid starting any sequences with the token of interest? For each sequence, the token of interest should not occur until at least a few tokens in.
8. Did you avoid repetitive narrative arcs and over-explaining? Did you avoid "templates" or overuse of the same patterns? Look carefully to identify such arcs.
9. Not every sample needs to be a complete, self-contained thought. Do some start and end abruptly, as if scraped from the middle of a page?
10. Did you avoid making everything only human text/natural language? For example, if a token is commonly used in math, there should be raw homework problems, proofs, code without extra text and without natural language. Similarly for code, avoid "narration" or "introductions".
11. Is there natural variation in tone and emotional register? Most sequences should be emotionally neutral or flat, since most web text is. But include some that are positive, excited, confused, frustrated, funny, or bored. Avoid making every sample sound like the same calm, competent person.
12. Ensure there's not a disproportionate amount of samples talking about the same topic, domain, or scenario.
13. When the token of interest is used, by that point, is it already semantically clear what the meaning is? For example "The shell is a clam" versus "The clam shell.." - the later is preferred if the token of itnerest is "shell", since the latter establishes meaning already by the time "shell" occurs.
14. Did you avoid adding contextual intros or repetitive intro->linebreak->text patterns? A common and bad pattern is stuff like "travel brochure\nthe hotels in the area..". The usage of "travel brochure" is bad here. This is a common pattern that you often generate on the first pass; you should repeatedly check for this until they are gone. In addition, always adding linebreaks in the same place is also a bad habit you should check for.
15. Again, is every usage of the token correct with the same unambiguous meaning? The unambiguity is very important. Read each sample and confirm the target meaning is clear.