Hi GPT! Let's name this chat, "Reworking samples x".

--

The goal of this repo is to create *polysemantic token datasets* for LLM training. This means given a single token, we take multiple (3) meanings of that token, then create sequences where for each sequence, that token is used at least once, and every usage of the token in that sequence corresponds to that meaning_label.

We have some old, not-very good examples in ds/, and we're filling out dsv2/ with improved, better versions. This will be an iterative improvement procedure, and you should generally iterate without asking me for guidance every time.

We've already done one such example, taking `ds/samples_-.yaml` and converting it to `dsv2/samples_-.yaml`. Before creating it, you created `plan/plan_-.md`; while iteratively creating it over 20+ review/improvement cycles, you followed the guidance in `always_check.md`, asking yourself those questions and improving the distribution and semantic accuracy each time. That `always_check.md` instruction file is very important - make sure you read it and understand it fully. Do you understand the objective?

--

Perfect. Let's go ahead! Let's start by making our plan for the bracket token (" {"). You can read our existing ds/ version, then iterately work on improving and creating the plan file until fully satisfied.

--

Good work. Let's go ahead and get started on your iterative improvement creation + process. Remember to regularly go back and compare against those questions and your plan. Always "take a step back" and look for distributional issues regularly. Please use the same YAML format as in the `samples_-.yaml`.

Do not write code or install anything. Be self-critical and notice distributional issues.

The time is now 6:40pm (you can use `Get-Date` on PS to check). You should not finish your next round of edits until at least 30 minutes after this starting point, though later is fine (this is just a minimum!) - there is always more to edit, and you did not take the time to actually ask yourself those questions one by one. When you finish, you need to report back on every single question and you need to be HARSH, assuming by default you tend to fixate on pattern repetition. By default, you need to be harsh and continue to iterate further - you have a strong tendency to fall into patterns, and your default assumption should be that there are still too many patterns and that `always_check.md` has not yet been satisfied.

I've also added a `python scripts/check_length_distribution.py dsv2/samples_-.yaml` you can use to help with length distribution.

--

Keep going, I just wanted to add a brief note. I've also added a python scripts/check_length_distribution.py dsv2/samples_-.yaml you can use to help with length distribution.

Make a plan and continue to iterate and improve until 2:50 this time. Be harsh again and keep going until you can be harsh on all those questions and still say it's good to go.

---


This is a decent first draft, needs continued reowrk and diversity. I suggest the strategy you emploiy going forward is that for each problem, think about how many sequences need to be fixed, pick some out (5-50 for each problem typically), and modify them. Add much more diversity. Reread samples_-.yaml for good examples of real world messiness. Please continue to iterate; keep going until at least 8pm.

- In general, there's too much use of "context intros", there's no need to narrate the source of everything but this is constant through this entire dataset.
- The messiness is still not there but needs to be much more messy! I suggest updating your plan and executing.
- Length diversity is also not great.