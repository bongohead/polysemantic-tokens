Hi GPT! Let's name this chat, "Reworking samples x".

--

The goal of this repo is to create *polysemantic token datasets* for LLM training. This means given a single token, we take multiple (3) meanings of that token, then create sequences where for each sequence, that token is used at least once, and every usage of the token in that sequence corresponds to that meaning_label.

We have some old, not-very good examples in ds/, and we're filling out dsv2/ with improved, better versions. This will be an iterative improvement procedure, and you should generally iterate without asking me for guidance every time.

We've already done one such example, taking `ds/samples_-.yaml` and converting it to `dsv2/samples_-.yaml`. Before creating it, you created `plans/plan_-.md`; while iteratively creating it over 20+ review/improvement cycles, you followed the guidance in `always_check.md`, asking yourself those questions and improving the distribution and semantic accuracy each time. That `always_check.md` instruction file is very important - make sure you read it and understand it fully. Do you understand the objective?

--

Perfect. Let's go ahead! Let's start by making our plan for the " bar" token (leading space included). You can read our existing ds/ version, then iterately work on improving and creating the plan file until fully satisfied.

Iterate until 10:20pm (later is fine, just not earlier) until you get this plan right.  You can use PS Get-Date to check the time.

--

Good work. Let's go ahead and get started on your iterative improvement creation + process. Remember to regularly go back and compare against those questions and your plan. Always "take a step back" and look for distributional issues regularly. Please use the same YAML format as in the `samples_-.yaml`.

Do not write code or install anything. Be self-critical and notice distributional issues.

The time is now 6:40pm (you can use `Get-Date` on PS to check). You should not finish your next round of edits until at least 30 minutes after this starting point, though later is fine (this is just a minimum!) - there is always more to edit, and you did not take the time to actually ask yourself those questions one by one. Don't pause, keep adding diversity and better semantic meaning correctness. When you finish, you need to report back on every single question and you need to be HARSH, assuming by default you tend to fixate on pattern repetition. By default, you need to be harsh and continue to iterate further - you have a strong tendency to fall into patterns, and your default assumption should be that there are still too many patterns and that `always_check.md` has not yet been satisfied.

I've also added a `python scripts/check_length_distribution.py dsv2/samples_-.yaml` you can use to help with length distribution.

--

Still too many contextual intros and not enoguh diversity in gheneral. Review samples_-.yaml for good examples of distributional diversity. I recommend pulling ~20 sequences per meaning label and adding more diversity appropriately.

In addition, there is still too much contextual intros, e.g. "traveler review, 3 stars\n..". This formula of intro followed by actual text (seperated by a linebreak) is way too frequent! This is a serious issue and you should at least fix at least half of these instances to fix these. Remember, no "intro descriptor" is needed at all!

Please continue to iterate and improve on distributional diversity. Check samples_-.yaml for good examples if necessary. Review the questions and continue to iterate until they are correct. You should go until at least 2:30pm without pausing.

---


This is a decent first draft, needs continued reowrk and diversity. I suggest the strategy you emploiy going forward is that for each problem, think about how many sequences need to be fixed, pick some out (5-50 for each problem typically), and modify them. Add much more diversity. Reread samples_-.yaml for good examples of real world messiness. Please continue to iterate; keep going until at least 8pm.

- In general, there's too much use of "context intros", there's no need to narrate the source of everything but this is constant through this entire dataset.
- The messiness is still not there but needs to be much more messy! I suggest updating your plan and executing.
- Length diversity is also not great.

----

Getting close. Please address the below issues. Remember, you can re-read the samples_-.yaml file to get a good grasp on diversity; also answer those questions in the .md file. In general unless not appropriate, you should fix problems by sampling out 5-30 sequences for each problem (depending on scope of the problem), and modify them appropriately.

- Make these messier, some can start in the middle without "narrating". Pick out at least 30 sequences which have this issue and fix them. In general too, add more messiness and diversity throughout - these are too clean and don't resemble the messiness of real SFT data. Reread samples_-.yaml if you need to.
- 

As always, reread the questions at the end and iterate more if needed. You should iterate at least X times, and continue to search for improvements to distribution or semantic meaning clarity/accuracy until at least X:XXpm. Do not pause or stop until then; there are always places to keep looking for improvements.

---
Mostly good, make sure all sequences satisfy this constraint:

When the token of interest is used, by that point, is it already semantically clear what the meaning is? For example "The shell is a clam" versus "The clam shell.." - the later is preferred if the token of itnerest is "shell", since the latter establishes meaning already by the time "shell" occurs.
---
Do one final run through and make sure there's no contextual ambiguity and resolve any you see. Clearer is better.
---



Excellent work. Do one last sweep and make sure those questions could all be answered now. Any last improvements you want to make for either diversity or to resolve this questions or to improve semantic clarity?


---

Great work. Make sure you plan file is up to date with any learnings you have or things you had to fix/iterate on repeatedly.