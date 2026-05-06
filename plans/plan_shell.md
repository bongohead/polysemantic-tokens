# Plan: Polytok Token `" shell"`

## Objective

Create `dsv2/samples_shell.yaml` with 100 realistic samples for each meaning label:

- `sea_shell`
- `command_line_shell`
- `explosive_shell`

Every sample must contain the exact token `" shell"` at least once. Every occurrence of `" shell"` inside a sample must match that sample's `meaning_label`.

The old `ds/samples_shell.yaml` establishes the intended labels, but it is too polished and explanatory for the v2 standard. It has 40 `sea_shell` samples, 38 `command_line_shell` samples, and 40 `explosive_shell` samples. The v2 file should expand each label to 100 samples and should not merely rewrite the old paragraphs. It needs rawer artifacts, more varied voices, more clipped and partial text, more structured data, more realistic page residue, and stricter control of exact-token collisions.

## Exact-String Notes

The target is a literal space followed by lowercase `shell`.

- ` shell`, ` shell,`, ` shell.`, ` shells`, ` shell's`, ` shelled`, ` shelling`, ` shell_fire`, ` shell=True`, ` shell: bash`, ` shell_script`, ` shellfish`, and ` shellac` contain the exact token and must be semantically correct for the active label.
- `Shell` with uppercase S, `shell` at the beginning of a sample or line without a preceding space, `seashell`, `subshell`, `eggshell`, `nutshell`, `PowerShell`, `powershell`, `.shell`, `/shell`, `_shell`, `shell_script` preceded by a quote or underscore, and backticked `` `shell` `` without a preceding literal space do not by themselves satisfy the exact target.
- Indented structured text can create target occurrences: `  shell: bash`, `    shell_cmd: ./run.sh`, or `  shell_fragments: 12` contain `" shell"`.
- Quoted or code-delimited terms are easy to misread. `"shell"` in JSON does not contain the target if the character before `shell` is a quote, but `use shell=True` and `run shell: bash` do contain it.
- Longer words and fixed phrases are high risk. ` shellfish`, ` shellac`, ` shellcode`, ` shellshock`, ` sheller`, ` shelly`, ` shelling`, ` shelled`, ` shelling_out`, ` shell_game`, ` shell_company`, ` shell_model`, ` shell_theorem`, ` shell_method`, ` shell_extension`, ` shell_sort`, ` shell-script`, ` shell-shaped`, and ` shell_script` all contain the exact token. Use them only when the exact occurrence belongs to the active label, and otherwise avoid them.
- Hyphenated compounds need character-by-character checking. `oyster-shell` and `high-explosive-shell` do not contain `" shell"` at the `shell` part because the preceding character is a hyphen, not a space. But `shell-script`, `shell-shocked`, and `shell-like` do contain the target when preceded by a space because the compound begins with lowercase `shell`. Prefer spaced forms such as `oyster shell`, `shell script`, or `explosive shell` when clarity matters.
- Do not start any sample with the target. If a realistic artifact begins with lowercase `shell`, add preceding context from the same artifact or choose a different excerpt.

## Realism Standard

Samples should feel like mixed C4/HPLT-style web data, not curated examples. Use raw excerpts directly where plausible: beach cleanup notes, aquarium posts, shell craft listings, museum cards, marine biology tables, ecology reports, terminal sessions, CI logs, Dockerfiles, GitHub Actions snippets, `.bashrc` fragments, StackOverflow replies, command transcripts, support tickets, artillery incident reports, UXO forms, museum education pages, historical notes, OCR/PDF residue, chats, emails, forum comments, broken HTML, CSV rows, JSON-ish logs, and partial scraped pages.

Good data can be clipped, mundane, malformed, redundant, interrupted, or surrounded by irrelevant but safe page residue. Include plausible artifacts such as table headers, copied navigation, duplicate footers, ad placeholders, cookie text, timestamps, Markdown stripped by a renderer, OCR line breaks, mobile app paste artifacts, merged sidebar text, missing comments, and fields that wrap badly.

Avoid source-intro wrappers such as `excerpt:`, `snippet:`, `museum placard:`, `developer Q&A:`, `news clipping:`, `historical note:`, or `the page says` unless such labels genuinely belong to the artifact. The sample should be the artifact itself, not a description of the artifact.

Lessons from the completed iteration:

- Messiness must not become the house style. A few broken exports, missing images, repeated footers, OCR errors, and app/UI artifacts are useful, but dozens of samples ending with "the PDF hid...", "the app dropped...", or "the cached page repeated..." create a new artificial template.
- Prefer either normal unbroken text or inline embodied mess. Use the duplicated table row, misplaced `COOKIE SETTINGS`, repeated `MAIL TO`, or clipped transcript directly; do not narrate that "the blog footer drops related recipes" or "the queue sorted by uploader".
- First-use clarity matters more than eventual clarity. Do not rely on a later sentence to disambiguate the target. Borderline phrases such as `each shell`, `the shell`, `hollow shell`, `shell in the mud`, or `a shell struck...` should be tightened unless the preceding context already makes the meaning unmistakable.
- Curator-style labels are not a substitute for distributional variety. Strong fixes change the actual voice, setting, structure, and purpose of the sample, not just the heading.

## Distribution Guidance

Use approximate distributions, not exact quotas.

- Length: include a few very short fragments, many short and medium samples, and a meaningful minority of long or extra-long messy samples.
- Token placement: do not start any sample with `" shell"`. In longer samples, ensure target occurrences appear late sometimes, not only in the first sentence or first table row.
- Token density: use enough target tokens to make the meaning clear. `sea_shell` and `explosive_shell` can naturally repeat plural `shells`; `command_line_shell` can naturally repeat in code and logs. Avoid stuffing.
- Source mix: include technical, educational, commercial, workplace, informal, structured, newsy, crawled/OCR, auto-generated, and conversational text where appropriate for each label.
- Voice and tone: vary between neutral machine output, terse notes, confused humans, polished documentation, excited collectors, annoyed users, bureaucratic policy, historical prose, casual chat, and raw forms.
- Completeness: not every sample should be self-contained. Some should start or end abruptly as if scraped from the middle of a page.
- Case: the target token is lowercase `" shell"`. Uppercase `Shell` can appear for realism, but it does not satisfy the target by itself.
- Surface-form balance: avoid making `sea_shell` mostly dreamy beachcombing paragraphs, `command_line_shell` mostly tutorials about Bash, or `explosive_shell` mostly dramatic battlefield narration.
- Language mix: include a small number of non-English or code-mixed artifacts where lowercase English `shell` is plausible, especially technical command-line text, product listings, museum labels, and news/OCR fragments. Do not force translations that would normally use a local-language word instead of `shell`.

Approximate source mix targets:

- `sea_shell`: roughly one quarter beachcombing/coastal personal text, one fifth marine biology/ecology/conservation, one fifth craft/ecommerce/decor, one fifth aquarium/hermit-crab/museum/archaeology/education, and the remainder OCR, tables, forum posts, travel pages, and odd scraped artifacts.
- `command_line_shell`: roughly one third raw code/config/log/CI artifacts, one quarter troubleshooting/Q&A/support text, one fifth docs/tutorials/runbooks, one tenth chat/forum fragments, and the remainder security/admin/legacy-system material.
- `explosive_shell`: roughly one fifth historical/military reference, one fifth reports/news/UXO safety notices, one fifth fiction/film/education/casual artifacts, one sixth technical/forensic/manual/math fragments at a non-actionable level, and the remainder modern news, contemporary conflict service updates, casual history discussion, ammunition-collecting hobby text, veteran memoir fragments, chats, tables, museum records, legal/regulatory text, and archival mess. Do not let WWI/WWII-adjacent material dominate the whole label.

Post-iteration calibration:

- `sea_shell` needed explicit additions for food/cooking and reuse contexts: clambake cleanup, raw-bar oyster shell disposal, restaurant-to-garden shell pickup, crushed shell paths, shell mulch, conch shell horn/instrument use, and hobby collecting across species. Keep these in future revisions.
- `command_line_shell` was strongest when it used raw configs/logs and confused users, not when every sample was a competent maintainer explaining a Bash-vs-dash mismatch. Avoid making the central plot always "wrong shell chosen".
- `explosive_shell` repeatedly collapsed into old range discovery, authorities called, museum display, solemn war diary, and damage assessment. Counterbalance with modern news, current-conflict alerts, ballistics/math worksheets, collector forums, defense-industry/procurement notes, memoirs with varied emotional texture, and non-English/code-mixed fragments.

## Build Strategy

Create samples in batches of about 20 per label, then audit the entire label before adding more. Early batches should establish high-certainty core examples; later batches should deliberately fill gaps in source type, length, voice, and messiness.

For each 20-sample batch:

- Verify every exact `" shell"` occurrence by scanning manually, especially `shells`, `shelled`, `shelling`, `shell=True`, `shell_script`, `shellfish`, and indented `shell:` fields.
- Check that at least several samples place the target token late, not only near the opening.
- Add a few structured or non-prose artifacts: CSV, YAML, JSON, code/config, tables, logs, OCR, HTML, forms, receipts, or copied page residue.
- Add at least one longer messy sample per label if the current label is becoming too clean.
- Remove samples that need a curator explanation to disambiguate the sense.
- Track topic clusters so each label does not collapse into only beach finds, only Bash tutorials, or only artillery history.

During later revision rounds, explicitly count patterns as well as labels. If the same narrative skeleton appears more than a few times, rewrite even if every individual sample is semantically correct. The hardest recurring skeletons for this token were:

- `sea_shell`: beach find or product listing followed by a narrated app/export/page problem.
- `command_line_shell`: configured for one shell, actually ran in another shell, competent sysadmin explains the failure.
- `explosive_shell`: old ordnance found near range/ditch/field, authorities called, area closed; or shell impacts listed, then clearance/repair follows; or museum display and inert-status reassurance.

Do not "fix" diversity only by adding headings like `movie review`, `forum post`, `news brief`, or `profile page cached`. Those can become curator labels unless they plausibly belong to the copied source.

## `sea_shell`

Semantic rule: `" shell"` refers to the hard external covering of a marine mollusk or the empty/remnant object left by one. This includes beach shells, conch/scallop/clam/oyster/cowrie/whelk/abalone/nautilus shells, marine fossil shells, shell fragments used in crafts or archaeology, oyster shell reef material, and empty mollusk shells used by hermit crabs.

Good examples:

- `the tide line was full of broken shell fragments`
- `a spiral conch shell sat in the gift-shop window`
- `oyster shell bags were stacked for reef restoration`
- `the hermit crab rejected the painted shell`
- `table row: species,cowrie shell,count,condition`
- `the midden layer contained clam shells and charcoal`

Include:

- Beach and coast contexts: beachcombing, tide lines, shell hash, shell fragments, drift rows, sand samples, shoreline cleanup, tourist stalls, shell collecting, guidebooks, and field notes.
- Marine species and natural history: clam, oyster, scallop, conch, cowrie, whelk, mussel, abalone, nautilus, murex, limpet, cockle, olive shell, junonia, chambered shell, fossil shell, and mollusk growth.
- Ecology and conservation: oyster shell reef restoration, shell bags, calcium carbonate, shell dissolution, ocean acidification, microplastics trapped in shells, protected species, collection rules, and beach cleanup logs.
- Human uses of marine shells: shell jewelry, shell buttons, shell inlay, shell mosaic, shell ornaments, shell planters, wind chimes, souvenir shops, aquarium decor, hermit crab spare shells, museum collections, archaeological shell middens, conch shell horns, shell mulch, crushed shell paths, raw-bar/clambake shell disposal, and restaurant oyster shell reuse for gardens or reef projects.
- Messy artifacts: product listings, craft instructions, shipping emails, aquarium forum posts, beach cleanup CSV rows, museum labels, OCR from field guides, HTML product tabs, travel blog comments, photo captions, school worksheets, and lab table fragments.
- Plural and inflected target forms such as `shells` or `shell's` only when each exact occurrence is a marine mollusk shell object.

Exclude:

- Command-line shells, shell scripts, shell sessions, shell variables, and software/API/code uses.
- Explosive shells, artillery shells, mortar shells, shell fire, shelling attacks, shell fragments from ordnance, and spent shell casings from weapons.
- Egg shells, turtle/tortoise shells, crab/lobster shells, insect shells, nut shells, taco shells, pasta shells, chocolate shells, capsule shells, phone cases, outer jackets, and generic protective covers.
- Shellfish as animals or food. `shellfish` contains the exact token but does not mean a shell object, so avoid it unless another exact target occurrence is clearly marine-shell and `shellfish` is removed or uppercase/non-target.
- Shellac, shell companies, shell games, shell accounts, shell theorem, shell method, electron/nuclear shell model, shell structures in architecture, car body shells, boat/racing shells, boiler shells, shell jackets, shell suits, shellac manicures, and idioms like `come out of her shell`.
- `shell-shaped`, `shell-like`, and decorative pattern uses are excluded when they are target-bearing, because they describe form rather than a shell object. Remove or uppercase them if a sample otherwise has a valid marine-shell occurrence.
- Lowercase `shelly` as a geology or texture adjective is high-risk. Use clearer noun phrases like `shell hash` or `clam shells` instead.
- Verbs such as `shelling peas`, `shelled walnuts`, `shell out money`, or `shelled a rower in a race`.
- `seashell` alone does not contain the exact target. It can appear as context only if another lowercase exact `" shell"` occurrence is present and semantically valid.
- Cowrie or wampum-style shell money is valid only when the exact target occurrence still refers to actual marine shells used as objects. Avoid vague economic phrases if they could drift toward `shell company` or `shell account`.

Guidance:

- Make the marine mollusk sense unmistakable through species names, beaches, tide lines, mollusks, reefs, aquariums, calcium carbonate, shell middens, or shell craft context.
- Do not make all samples sentimental beach narratives. Add dull collection logs, product tables, reef-restoration notes, archaeology rows, aquarium arguments, school worksheets, OCR captions, and messy ecommerce pages.
- Do not overuse the phrase `sea shell`. It is valid, but many realistic sources say `conch shell`, `clam shell`, `oyster shell`, `shell fragments`, `shell beads`, `shell midden`, or simply `shells` with coastal context.
- `shell fragments` and `broken shells` are valid only when the source makes them marine or mollusk-derived. In isolation, they risk ordnance or generic debris ambiguity.
- Hermit-crab samples are valid when the shell is an empty mollusk shell used by the crab. Avoid text where the exact token refers to the crab's own exoskeleton.
- Long scraped samples must not include sidebars with `shell command`, `shell company`, `shellfish allergy`, or `shotgun shell` because every exact target occurrence would then be polluted.
- If a phrase like `the shell`, `each shell`, `spare shell sizes`, or `little shell` appears, make sure a species or marine context already precedes it. Prefer `clam shell`, `oyster shell`, `whelk shell`, `conch shell`, or `beach shell` when there is any possible ambiguity.
- Cooking/food-adjacent samples should refer to shells as discarded physical shell objects, not `shellfish` as a food category. `raw bar closeout`, `empty oyster shell`, `clam shell halves`, and `shell bucket` are valid; `shellfish special` is not.

Planned diversity dimensions:

- Species/object: conch, scallop, clam, oyster, cowrie, whelk, abalone, nautilus, murex, mussel, limpet, fossil shell, broken shell, shell beads, shell inlay, oyster shell bags.
- Setting: beach, tide pool, reef project, aquarium, museum, classroom, craft fair, souvenir stall, archaeology trench, lab, shipping warehouse, coastal cleanup, travel blog, raw bar, clambake, restaurant compost/reuse pickup, garden path, landscaping quote, music room/conch horn.
- Source type: field note, product listing, HTML tab, forum post, cleanup log, museum label, recipe/craft page residue, school handout, OCR field guide, photo caption, chat, email, CSV table.
- Tone: excited collector, flat lab log, annoyed buyer, conservation bulletin, parent note, tourist page, academic fragment, casual comment, machine export.
- Length: short fragments like `bucket had two intact shells`, medium notes, and long messy pages with product specs, comments, and duplicated footer text.

## `command_line_shell`

Semantic rule: `" shell"` refers to a command-line interpreter, command execution environment, or script language/context used to run commands. This includes Unix shells such as `sh`, `bash`, `zsh`, `fish`, `dash`, `ksh`, `csh`, and `tcsh`; named shells such as Bourne shell, C shell, Korn shell, and Almquist shell when lowercase ` shell` is present; Windows command shells when explicitly command-line; login/interactive shells; shell scripts; shell prompts; shell builtins; shell expansion; environment `SHELL`; CI `shell:` settings; and subprocess command execution through a shell.

Good examples:

- `open a shell and run npm test`
- `the login shell is /bin/zsh`
- `GitHub Actions row: shell: bash`
- `subprocess.run(cmd, shell=True) failed in CI`
- `the shell script exits before sourcing .env`
- `operators used a remote shell to restart the service`

Include:

- Raw command artifacts: terminal transcripts, prompts, history snippets, Makefiles, shell scripts, `.bashrc`, `.zshrc`, `.profile`, `Dockerfile` commands, cron entries, systemd units, `package.json` scripts, CI logs, YAML workflow `shell:` fields, and build output.
- Troubleshooting contexts: `command not found`, PATH issues, permissions, shebang lines, quoting, globbing, pipes, redirects, process substitution, shell expansion, shell builtins, login shell changes, Windows line endings, and Bash-vs-dash compatibility.
- Programming interfaces that explicitly invoke a shell: Python `subprocess(..., shell=True)`, Node `child_process.exec`, Ruby/Perl system calls, Make recipes, `/bin/sh -c`, SSH/secure shell sessions when command access is explicit, container entrypoints, and deployment runners.
- Admin/security contexts when the command interpreter is clear: restricted shell, remote shell, web shell, reverse shell, chroot shell, shell access, rescue shell, root shell, UEFI shell, database shell, language REPL shell, and audit logs. Keep these at diagnostic or incident-report level, not exploit instructions.
- Messy artifacts: StackOverflow answers, support tickets, Slack exports, CI annotations, docs pages with copied nav, package README fragments, ShellCheck reports, and OCR of terminal handouts.
- Surface forms such as `shells`, `shell's`, `shell_script`, `shell_cmd`, `shell=True`, `shell: bash`, `shell session`, `shell prompt`, `shell command`, `shell builtin`, `shell variable`, and `shell environment` when they clearly mean command-line shell.

Exclude:

- Sea shells, shell fragments, shell collecting, shell jewelry, shell middens, oyster shells, and mollusk biology.
- Explosive shells, shell fire, shelling, shell casings, mortar/artillery/tank/naval shells, and UXO.
- Desktop/GUI operating-system shells such as Windows Explorer shell, GNOME Shell, shell extensions, shell namespace, and shell folders unless the text is explicitly about command-line command execution.
- `shellcode` as exploit payload bytes, even when it opens a shell; it is a separate security term and can create confusing exact-token occurrences.
- Software proper names or tools where the target occurrence is not the command interpreter itself: lowercase `shellcheck`, `shelljs`, `shellwords`, and package names contain the target if preceded by a space, so avoid them. Uppercase `ShellCheck` can appear as context if another exact occurrence clearly refers to the command-line shell.
- Shell companies, shell accounts in finance, shell games, shellac, shell suits, nutshell, eggshell, shell theorem, electron/nuclear shell model, and shell structures.
- Keyboard buttons or UI controls named `shell` in an app when no command interpreter is involved.
- `shell account` is valid only in explicit Unix/hosting contexts where it means an account with command-line shell access. Financial or corporate `shell account` uses are excluded.
- Lowercase brand/proper-name uses such as `shell oil`, `shell station`, or `shell plc` are excluded unless they are uppercase/non-target context and another occurrence carries the active label.
- `PowerShell` or `powershell` alone does not contain the exact target. It can provide context, but at least one lowercase exact `" shell"` occurrence such as `PowerShell shell session` must carry the label if used.

Guidance:

- Make the command-interpreter sense explicit through commands, prompts, paths, shebangs, `$SHELL`, `/bin/sh`, `/bin/bash`, `zsh`, `fish`, CI runner settings, process execution, or terminal behavior.
- Raw artifacts are especially valuable here. Do not wrap every sample in a tutorial voice. Use logs, configs, errors, snippets, stack traces, support pastebins, comments, and broken Markdown.
- Be careful with `shell script`: it is valid, but overusing tidy beginner tutorials will make the label weak. Include compatibility failures, CI defaults, quoting bugs, runner configs, container entrypoints, and admin sessions.
- Do not let `shell=True` become the main structured form. Mix it with `shell: bash`, `login shell`, `interactive shell`, `/bin/sh -c`, `remote shell`, `shell prompt`, profile files, and raw terminal output.
- `remote shell`, `web shell`, and `reverse shell` are valid only when the text clearly means command access. Avoid procedural exploit details and payload construction.
- Avoid accidental sidebars that mention beach shells, artillery shell, shell company, or `shellfish`.
- Structured fields such as `shell:` are valid when they select a command interpreter. Generic fields named `shell` in unrelated schemas should be replaced.
- `shell` in Python, Node, or CI config is valid only when it means commands are being executed by a command interpreter. It is not valid for generic UI tabs, browser shells, desktop shells, or package names.
- Avoid overusing the "wrong shell chosen" arc. Bash-vs-dash, cmd-vs-Git-Bash, npm `script-shell`, and CI `shell:` mismatches are all realistic, but they should not be most of the label. Balance them with tutorials that work, admin policy, login-shell inventory, historical shell design, REPL/database shells, UEFI/BusyBox/router shells, and basic confused-user questions.
- Vary competence and emotional register. Include automated output with no explainer, beginners who misunderstand terminal vs shell, terse runbooks, angry users, old vendor notes, and normal documentation where nothing fails.

Planned diversity dimensions:

- Shell family: sh, bash, zsh, fish, dash, ksh, csh/tcsh, BusyBox ash, Bourne shell, C shell, Korn shell, Windows cmd, secure shell/SSH context, database or language REPL shells, PowerShell as context with a lowercase target occurrence.
- Task: setup, CI build, deployment, cron, Docker entrypoint, SSH, quoting, environment variables, permissions, shebangs, aliases, profile startup, subprocess execution, test harness.
- Source type: terminal paste, workflow YAML, Dockerfile, README, issue comment, StackOverflow answer, support ticket, Slack/Discord chat, log output, stack trace, package docs, runbook, config table.
- Tone: terse machine output, confused beginner, annoyed maintainer, calm docs, security incident note, legacy-admin warning, quick chat, release checklist.
- Length: short fragments like `default shell was dash`, medium bug reports, and long messy CI/runbook pages with repeated command output and footer residue.

## `explosive_shell`

Semantic rule: `" shell"` refers to an explosive or military projectile, usually fired by artillery, mortar, tank, naval gun, or similar weapon, including its firing, impact, casing, fragments, fuse/fuze, crater, unexploded state, or shelling action. `shelled` and `shelling` are valid only when they mean bombardment by such shells.

Good examples:

- `an artillery shell landed near the roadblock`
- `UXO team marked the unexploded mortar shell`
- `the shell fragments were logged as evidence`
- `records mention heavy shelling before dawn`
- `range table: high-explosive shell, smoke shell, armor-piercing shell`
- `villagers reported shell fire north of the bridge`

Include:

- Military and historical contexts: artillery shells, mortar shells, tank shells, naval shells, high-explosive shells, shrapnel shells, smoke shells, armor-piercing shells when described as ordnance, shell fire, shell bursts, shell craters, shell fragments, shell casings from artillery-size ordnance, and unexploded shells.
- Reports and safety notices: UXO warnings, bomb squad logs, demining records, range-control notices, museum labels, battlefield archaeology, incident timelines, news fragments, contemporary conflict updates, city-service alerts, insurance/damage assessments, and evacuation notices.
- Technical/forensic context at a non-actionable level: fuse/fuze type, caliber, casing fragments, residue analysis, trajectory estimates, blast radius references, ordnance identification, storage records, and training-range cleanup logs. Avoid procedural construction details.
- Fiction, film, memoir, and education: novel excerpts, movie reviews, classroom worksheets, math/ballistics problems, museum activity text, children asking questions, veteran memoir fragments, and fictional battle scenes, as long as the projectile sense is explicit.
- Casual and hobby contexts: history-buff forum discussion, ammunition-collecting checklists, demilled shell casing ID posts, collector safety reminders, and casual chat about war films or news, as long as the ordnance sense is already clear and there are no actionable weapon-construction details.
- Messy artifacts: OCR war diaries, old newspaper snippets, CSV damage assessments, museum tables, demining spreadsheets, incident reports with redactions, forum posts about found ordnance, captions, and transcript fragments.
- Inflected target forms such as `shells`, `shelled`, `shelling`, and `shell_fire` when every exact occurrence clearly relates to explosive projectile use.

Exclude:

- Sea shells, beach shells, oyster/clam/conch shells, shell fragments from mollusks, shell jewelry, and shell middens.
- Command-line shells, shell scripts, shell commands, remote shells, and software execution environments.
- Shotgun shells, spent bullet shell casings, blank cartridges, fireworks shells, model-rocket shells, and small-arms cartridge cases unless the text explicitly treats them as explosive artillery-like shells. Prefer excluding them to keep the label narrow.
- Shell shock as a psychological condition, shell-shocked as an emotional state, and `shellshock` as a vulnerability or idiom. These contain the target but do not directly mean the projectile object/action.
- Nuclear/electron shell model, shell theorem, shell company, shell game, turtle shell, egg shell, taco shell, shell suit, shell jacket, shellac, shelling peas/corn, and `shell out money`.
- `shell sort` or Shellsort is an algorithm/proper-name sense, not one of the three target meanings. Exclude lowercase `shell sort` if it appears in code/tutorial sidebars.
- Detailed instructions for making, filling, arming, or modifying explosive shells. General historical or forensic descriptions are fine; operational construction detail is not needed for this dataset.

Guidance:

- Make the munition sense unmistakable through artillery, mortar, tank, naval gun, battlefield, UXO, crater, shrapnel, fuse/fuze, barrage, impact, range, ordnance, demining, or blast context.
- Do not make every sample a dramatic war paragraph. Add dry range logs, museum accession rows, news updates, damage-assessment tables, classroom material, pure math/ballistics exercises, legal clauses, archival residue, forum safety replies, collector posts, current-conflict service notices, and non-actionable technical tables.
- Do not overuse the exact phrase `explosive shell`. Many realistic sources say `artillery shell`, `mortar shell`, `tank shell`, `naval shell`, `shell fire`, `shelling`, `shell crater`, or `unexploded shell`.
- `shell casing` is valid only when the casing belongs to an explosive artillery/mortar/tank/naval shell. Avoid ambiguous `spent shell casing` without weapon scale because it may read as small-arms ammunition.
- `shelling` and `shelled` are valid bombardment actions, but long samples must not also include non-military `shelling peas` or `shell shock` target occurrences.
- Because this label touches weaponry, favor observation, reporting, history, safety, education, and fictional aftermath contexts over actionable weapon construction.
- In long scraped samples, watch for sidebars containing `shell command`, `sea shell`, `shell company`, or `shellfish` and remove or rewrite them.
- Watch the time-period distribution. The first drafts skewed heavily WWI/WWII or vaguely historical. Include current or recent contexts, contemporary news language, 2020s defense-industry procurement, modern city-service alerts after shelling, and non-English/code-mixed fragments where `shell` plausibly appears.
- Watch tone. The first drafts skewed solemn, official, and educational. Add casual history-buff discussion, annoyed or frightened civilians, clipped emergency updates, purely mathematical exercises, collector hobby posts, and memoir fragments with varied emotion.
- Do not over-rely on `artillery shell` as a prefix in every sample. It is useful for clarity, but stronger samples also establish meaning through `battery`, `guns`, `mortar`, `naval`, `fuzes`, `breech`, `ballistics`, `shell crater`, or `shell burst` before or around the first target.

Planned diversity dimensions:

- Munition type: artillery shell, mortar shell, naval shell, high-explosive shell, smoke shell, shrapnel shell, armor-piercing shell, unexploded shell, shell casing, shell fragment.
- Setting: battlefield history, training range, border village, contemporary conflict city, museum, bomb squad callout, demining operation, classroom, math worksheet, forensic lab, archive, insurance claim, emergency notice, court hearing, collector forum, defense-industry newsletter.
- Source type: news wire, UXO form, range log, war diary OCR, museum card, classroom handout, ballistics problem, chat, forum safety thread, history forum comment, collector checklist, incident timeline, CSV damage table, field manual fragment, transcript.
- Tone: neutral report, urgent warning, dry archive, frightened witness, casual history-buff reply, hobbyist collector, film review, veteran memoir, safety bureaucracy, academic/museum prose, terse machine export.
- Length: short fragments like `mortar shell found by shed`, medium reports, and long messy pages with timelines, tables, captions, and duplicated navigation.

## Cross-Meaning Hazards

Inspect these cases manually during dataset creation:

- ` shells`: sea-shell plural, command-interpreter plural, or explosive-projectile plural depending on context. It is never safe by itself.
- ` shelling` and ` shelled`: bombardment for `explosive_shell`; removing shells from food/peas/nuts or general covering removal is excluded; not valid for `sea_shell` unless the exact target occurrence still means a shell object, which is unlikely.
- ` shell fragments`: marine debris for `sea_shell` when coastal/mollusk context is clear; ordnance debris for `explosive_shell` when blast/munition context is clear; ambiguous otherwise.
- ` shell casing`: usually explosive/artillery only when ordnance scale is explicit. Avoid small-arms or shotgun ambiguity.
- ` shell script`, ` shell-script`, ` shell command`, ` shell prompt`, ` shell session`, ` shell=True`, ` shell: bash`, ` shell_cmd`, ` shell_exec`: `command_line_shell`.
- ` remote shell`, ` web shell`, ` reverse shell`, ` root shell`: `command_line_shell` when command-access context is explicit; avoid exploit payload details.
- ` shell account`: command-line only when explicit Unix/hosting shell access is meant; financial/corporate `shell account` is excluded.
- ` shellfish`, ` shellac`, ` shell company`, ` shell game`, ` shell corporation`, ` shell out`, ` shelly`, `shelling peas`, `shelled walnuts`, ` shell-shaped`, ` shell-like`, ` shell suit`, ` shell jacket`, ` shell theorem`, ` shell method`, ` cylindrical shell`, ` body shell`, ` boat shell`, ` racing shell`, ` boiler shell`, ` pressure vessel shell`, ` shell model`, ` shell sort`, ` shell structure`, ` shell extension`, ` shell namespace`, ` shell oil`, and ` shell station`: excluded unless a different exact target occurrence carries the active label and these target-bearing forms are removed.
- ` egg shell`, ` turtle shell`, ` crab shell`, ` lobster shell`, ` nut shell`, ` taco shell`, ` pasta shell`, ` chocolate shell`: excluded for this three-label dataset.
- ` shell shock`, ` shell-shocked`, and `shellshock`: excluded because they are trauma/vulnerability/idiom senses, not the projectile itself, even though they are adjacent to explosive-shell history.
- ` PowerShell` and `powershell`: do not contain the lowercase target as a standalone exact token. They can appear for context only; use `PowerShell shell session` or another lowercase target occurrence if the sample needs to satisfy `command_line_shell`.
- ` seashell`, `subshell`, `eggshell`, `nutshell`: do not contain the target. They can be context only, but do not count as target-bearing.
- Line-start `shell` inside a quoted sample does not contain `" shell"` unless the line is indented with a literal space before `shell`. Do not rely on headings like `shell: bash` at true line start unless another target occurrence exists.
- If a sample contains more than one exact `" shell"` occurrence, every one must match the label. A good Bash sample cannot contain `sea shell` in a copied ad; a good beach sample cannot contain `shell script` in page boilerplate; a good ordnance sample cannot contain `shellfish` in unrelated sidebar text.

## Dataset Creation Strategy

Build `dsv2/samples_shell.yaml` in rounds of about 20 samples per label, then review and revise before adding the next round.

For each `sea_shell` round, deliberately cover several of:

- Beach finds, reef restoration, marine biology, aquarium/hermit-crab care, shell crafts, ecommerce listings, archaeology/middens, museum labels, school worksheets, cleanup tables, and messy travel/forum artifacts.
- Surface forms such as ` shell`, ` shells`, ` shell's`, ` clam shell`, ` conch shell`, ` oyster shell`, ` shell fragments`, ` shell beads`, ` shell inlay`, and ` shell midden` only if the exact target occurrence is still valid. Hyphenated `oyster-shell` can be context but does not satisfy the target by itself.

For each `command_line_shell` round, deliberately cover several of:

- Terminal transcripts, CI workflow YAML, Docker/container startup, login shell settings, shell scripts, shell quoting bugs, `$SHELL` environment issues, PATH errors, subprocess `shell=True`, Make/cron/systemd contexts, SSH sessions, and support/Q&A fragments.
- Surface forms such as ` shell`, ` shells`, ` shell script`, ` shell command`, ` shell prompt`, ` shell session`, ` shell builtin`, ` shell expansion`, ` login shell`, ` interactive shell`, ` remote shell`, ` shell=True`, ` shell: bash`, and ` shell_cmd`.

For each `explosive_shell` round, deliberately cover several of:

- Artillery/mortar/naval shells, UXO notices, shell fire, shelling reports, shell fragments, craters, range logs, museum/archive text, damage assessments, demining records, classroom records, court material, and safe high-level forensic descriptions.
- Modern news, city-service updates after shelling, pure ballistics/math exercises, casual history forum replies, ammunition-collector checklists, demilled shell casing ID posts, veteran memoir fragments, and non-English/code-mixed current-conflict snippets.
- Surface forms such as ` shell`, ` shells`, ` shelled`, ` shelling`, ` shell fire`, ` shell burst`, ` shell crater`, ` shell casing`, ` shell fragment`, ` mortar shell`, ` artillery shell`, ` tank shell`, ` HE shell`, and ` unexploded shell`.

After each round:

- Search every exact `" shell"` occurrence and classify it manually, including occurrences inside longer words such as `shellfish`, `shelling`, `shell=True`, `shell_exec`, and `shellshock`.
- Scan for high-risk phrases: ` shellfish`, ` shellac`, ` shell company`, ` shell game`, ` shell account`, ` shell out`, ` shelly`, ` shelling peas`, ` shelled walnuts`, ` shell shock`, ` shell-shocked`, ` shellcode`, ` shellcheck`, ` shell sort`, ` shell-shaped`, ` shell-like`, ` shell oil`, ` shell station`, ` shell extension`, ` shell theorem`, ` shell method`, ` cylindrical shell`, ` body shell`, ` boat shell`, ` racing shell`, ` boiler shell`, ` pressure vessel shell`, ` shell model`, ` egg shell`, ` turtle shell`, ` crab shell`, ` taco shell`, ` pasta shell`, ` shotgun shell`, ` fireworks shell`, ` shell casing`, ` shell command`, ` shell script`, ` shell-script`, ` sea shell`, ` oyster shell`, ` artillery shell`, ` shell fragments`, ` shell=True`, and ` shell:`.
- Check opening patterns. Remove curator intros unless they are realistic artifact headings.
- Check source/voice diversity. Add dirty artifacts if a label is mostly clean prose.
- Check length distribution and make sure longer samples include late target occurrences.

## Anti-Template Checks

Before calling any batch good, look for these grooves and rewrite away from them:

- `sea_shell`: not mostly first-person beach walks, magical mementos, pastel shells, parent-child identification scenes, or souvenir-shop paragraphs. Add workmanlike reef logs, product rows, aquarium disputes, school/OCR scraps, archaeology tables, and messy cleanup data.
- `command_line_shell`: not mostly beginner tutorials that say "open your shell" and explain `cd`, `PATH`, or `chmod`. Add raw CI failures, YAML runner settings, terminal output, subprocess bugs, odd legacy shells, pasted Slack support, security/admin logs, and terse config fragments.
- `explosive_shell`: not mostly cinematic battlefield prose, old soldier letters, or high-level manual paragraphs beginning with `explosive shell`. Add dry UXO forms, damage tables, range notices, museum rows, classroom material, news fragments, archival OCR, legal/regulatory text, and safety-focused reports.
- `explosive_shell`: not mostly old-range discovery, cordon, EOD, civilians react; not mostly museum/inert-display reassurance; not mostly war diary dispatch; not mostly damage assessment tables. Replace overrepresented instances with modern news, service disruption notices, mathematical ballistics, collector posts, defense-industry text, memoirs, and non-English snippets.
- `explosive_shell`: avoid samples whose main value is how to build, fill, arm, modify, or source components for shells. Prefer reporting, identification, history, safety handling by authorities, fiction/film response, or aftermath records.
- All labels: avoid repeating `Subject:`, `Excerpt`, `Snippet`, `According to`, `In a ... context`, `Random snippet`, and similar curator labels. If a heading remains, it should plausibly be copied from the source itself.
- All labels: include some samples that are not complete thoughts. Clipped beginnings, cut-off endings, duplicated footer text, malformed rows, and missing context are useful when the target meaning remains unambiguous. But do not make "something is broken" the default ending.
- All labels: messiness should be embodied, not narrated. Prefer raw rows, copied nav, duplicate lines, clipped transcripts, and inline cookie text over sentences explaining that an app hid, dropped, sorted, cached, or misplaced something.
- All labels: check that long samples have the target later in the text, not just once near the start followed by unrelated padding.
- All labels: after semantic QA, run a house-style scan for repeated endings about broken PDFs, cached pages, failed images, hidden rows, dropped captions, and app/export problems. Keep only a small realistic minority.

## Mechanical QA Aids

Use these only as aids; the final decision is still manual semantic inspection.

- `rg -n " shell" dsv2/samples_shell.yaml` to enumerate every exact target occurrence.
- `rg -n ' shellfish| shellac| shell company| shell game| shell account| shell out| shelly| shell shock| shell-shocked| shellcode| shellcheck| shell sort| shell-shaped| shell-like| shell oil| shell station| egg shell| turtle shell| crab shell| taco shell| pasta shell| shotgun shell| fireworks shell| shell extension| shell theorem| shell method| cylindrical shell| body shell| boat shell| racing shell| boiler shell| pressure vessel shell| shell model' dsv2/samples_shell.yaml` to catch common non-target senses.
- `rg -n '^\s*-\s*" shell|^\s*shell' dsv2/samples_shell.yaml` to catch samples or embedded lines that may start with the target or fail to contain it due to line-start placement.
- Search weak first-use forms and inspect them manually: `rg -n '\bthe shell\b|\ba shell\b|\bone shell\b|\beach shell\b|\bhollow shell\b|\bshell in the mud\b|\bsound of each shell\b' dsv2/samples_shell.yaml`. These are not automatically wrong, but they often need a stronger preceding cue.
- Search the narrated-mess house style: `rg -n 'cached|PDF|footer|dropped|hidden|failed thumbnail|image link is broken|iframe is broken|loading under|browser|viewer|preview|truncat|collapsed|template|widget|queue sorted|caption service|modal|thumbnail|screenshot|clipped|stripped|wedged|sync failed|DUP grid|app ' dsv2/samples_shell.yaml`. Treat hits as review candidates, not automatic failures.
- For long samples, inspect the whole text around every target occurrence; a single copied sidebar can invalidate an otherwise good sample.

## QA Checklist

Per sample:

- Contains exact token `" shell"`.
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
- Manually inspect high-risk cases: sea-shell vs explosive-shell fragments, shell scripts vs GUI shells, shelling as bombardment vs food prep, shellfish, shell shock, shellcode, and any longer word beginning with `shell`.
