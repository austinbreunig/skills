---
name: human
description: Explain, show and guide. Turns any context (a PR, ramp report, spec, Wayfinder map, connected repo, file, idea or the last message) into a plain-language, visual explanation at the reader's level, in chat or as a self-contained HTML page. Asks guiding questions; never recommends. Use when something didn't land or a person has to understand and decide.
---

# Human

Specs, tickets and code are written for machines. This skill writes the version for a person. It has three duties:

1. **Explain:** plain language at the reader's level, with the background they need first.
2. **Show:** anything complex gets a picture, and the text explains the picture. Complex means a process, a flow, a timeline, or more than two parts that affect each other.
3. **Guide:** questions that lead the reader to their own answer. **Never a recommendation**, anywhere. A reader who wants the agent's view can ask in chat.

Usable at any time: on an artifact, a repo, or whatever didn't land.

## Modes

Take the mode from the argument, or work it out from the input.

| mode | input | default output |
|---|---|---|
| pr | a pull request or integration branch: the diff, linked spec and tickets, test results, code-review output | HTML page |
| ramp | a `RAMP.md`: the break-it result, levels, checks, capacity statement, break list | HTML page |
| spec | a spec issue | HTML page |
| map | a Wayfinder map: decisions so far, the frontier, the fog | HTML page |
| repo | `owner/name`, or the current repo: where one connected repo stands (see **Repo mode**) | chat |
| explain | anything else: the last message, a file, an idea | chat |

Flags:

- `--html`: make an HTML page instead of a chat answer. No effect on modes that already default to HTML.
- `--level newbie|beginner|proficient|master`: the reader level for this call only. Default `beginner`.

## Reader level

| | newbie | beginner (default) | proficient | master |
|---|---|---|---|---|
| Reader | 5th grader | knows the basics, shaky on complex parts | knows the basics, needs steering on complex parts | handles jargon, needs help with fine points |
| Words | everyday words, an analogy for everything | plain words, terms defined | technical words, only domain terms defined | full jargon |
| Background | 3–4 cards, starting from zero | 2–4 cards on the complex parts | 0–2 cards | none |
| Visuals | a picture for every idea | a diagram for anything complex | diagrams for the complex parts | diagrams only for fine points |
| Guiding questions | big picture | cause and effect | trade-offs | edge cases and fine points |

## 1. Gather facts (from sources only)

Read the input and follow its pointers: linked tickets, ADRs, contracts, diff, test output. If the repo has a `GLOSSARY.md` or README, read it for its terms. Collect real facts: names, numbers, file paths, the decisions made and the reason given for each.

**Never invent numbers, results or reasons.** If a fact isn't in the sources, leave it out or mark it plainly as unknown. Every claim should trace to a source you can link.

## 2. Find the story

Answer in one sentence each before writing:

1. What is this, in words a newcomer would use?
2. Why does it exist? What problem or goal does it serve?
3. What is the single most important thing the reader must understand?
4. What question, if any, is in front of the reader?

## 3. Sections

In this order, for every mode. Leave out any section with nothing real in it.

1. **Think it through** (top, impossible to miss): one line naming the question from story step 4, then 2–4 guiding questions. Each guiding question points to the section that helps answer it, e.g. "What breaks if the cache is cold? → What could go wrong". Pick the question type from the reader level. If there is nothing to decide, the whole box is the one line "Nothing to decide, just read.", with no guiding questions.
2. **In one paragraph:** the story from step 2.
3. **Background:** concept cards, as many as the reader level says. Each card: a plain definition, an everyday example, a small visual, and one trusted source if you can find one. No quizzes or lessons.
4. **The picture:** at least one diagram of the real mechanism, not decoration.
   - pr: data or control flow through the parts touched, changed parts highlighted, before/after if behavior changed.
   - ramp: levels on a chart against the checks, the break point, and accuracy change.
   - spec: the parts and the seams between them.
   - map: decisions made, the frontier and the fog, drawn as a map.
   - repo: see **Repo mode**.
   - explain: whatever the input describes.
5. **What changed and why:** short cards, one per change or decision: what, why, link to the source.
6. **What could go wrong:** risks, edge cases, and anything a review or break-it pass flagged, with how each is handled or why it's accepted. Don't make it sound safer than it is.
7. **How we know it works:** test and break-it results, ramp numbers, and what is still untested.
8. **Glossary:** each term used, one plain line each.
9. **Go deeper:** short code excerpts, full tables, links.

The Think-it-through box must match the facts in the body. It names options only if the body does, and never ranks or favors one.

## Repo mode

A deep-dive on one connected repo: what's open, why, and what could be next. Starts from `/human repo owner/x` (no repo: use the current folder's GitHub `origin`), or from the "Want a deep-dive on any of these repos?" offer at the end of brief and eod. Several repos named there: one deep-dive each. A level named with a repo ("owner/x, proficient") is that repo's `--level`.

**Needs hq.** If `~/.config/hq/config` is missing, say "repo mode needs hq. Run /hq to set it up." and stop. Otherwise find the HQ folder and pull, as in hq's "Rules for every hq skill".

**Reads, for that repo only.** These replace step 1's sources:

- HQ folder: the repo's `## owner/name` section of each `eod/YYYY-MM-DD.md` from the last 7 days; the jots in `jots/` dated (by file name) in the last 7 days whose `repo:` line is `owner/name`.
- Left off: the newest session under `~/.claude/projects/` with any record whose `cwd` maps to the repo (`git -C <cwd> rev-parse --git-common-dir`, then that repo's `origin` is `owner/name`, so worktrees count). Use that session's newest `away_summary` record, else its `ai-title`.
- Live `gh`: open PRs (draft, review state, check status, linked tickets); open tickets with body and latest comments, assignee, blocked-by, last update; tickets closed in the last 7 days; any open `wayfinder:map` issue. The repo's `GLOSSARY.md` and README, via `gh api` if it isn't the current folder.

No raw transcripts: from session files read only the `cwd`, `away_summary` and `ai-title` fields, never the messages.

**Sections**, in this order (they replace section 3's list):

1. **Think it through:** "What should you work on next?" plus guiding questions.
2. **In one paragraph:** what the repo is and where it stands.
3. **Background:** what the repo is for, and key terms from its GLOSSARY or README.
4. **The picture:** open tickets as a map, grouped done (closed in 7 days) / next up (unblocked) / blocked (by which ticket). Each PR sits on the ticket it closes; a PR with no ticket stands alone.
5. **Recent work:** cards from the last 7 days of EOD sections, and the left-off line.
6. **Open tickets:** one card each: what it is, why it's still open (from its body and latest comments), who claimed it.
7. **What could go wrong:** stale or stuck work: failing checks, PRs waiting on review, tickets not updated in 7+ days.
8. **Next steps:** facts only, each linked, not ranked: the unblocked tickets, open EOD action items, and the stuck items. The guiding questions make the reader weigh them.
9. **Jots, Glossary, Go deeper.**

No "What changed and why" and no "How we know it works".

## 4. Writing rules

- Words as the reader level says. Define each repo glossary term the first time it appears, using the repo's own definition; the level decides how much else gets defined.
- Short sentences. One idea per sentence.
- A concrete example for every abstract idea.
- Lead with what matters. No preamble.
- Numbers keep their units and context: "4.2 s per tile (was 9.8 s)", not "faster".
- No "I recommend", "you should", "the best option" or similar. Ask instead.

## 5. Output

### Chat (a human explanation)

- Same section order. Think it through comes first.
- Diagrams are plain-text box-and-arrow drawings in code blocks.
- Background is short bullets: term, plain definition, everyday example.
- Go deeper is a list of source links.
- About one screen: 50 lines or fewer, code blocks included. Keep only the most important card, risk and glossary items to fit. Cut detail before cutting the box or the picture.
- Not saved anywhere.

### HTML page (a human page)

- **One self-contained HTML file.** Inline CSS and inline SVG. Nothing loaded from the network, so it opens offline.
- Readable on a phone: one column, 16px side margin, no horizontal scrolling.
- Light and dark mode: colors as CSS variables on `:root`, redefined under `prefers-color-scheme: dark`.
- A restrained palette with one highlight color for "changed" or "needs attention". Color carries meaning, not decoration.
- Every diagram gets a one-line caption saying what to notice. Charts get labeled axes, units, and the checks and break point marked on them.
- Go deeper uses collapsible `<details>` sections.
- Save to `.lifecycle/human/<cycle>-<mode>-<short-name>.html` if `.lifecycle/` exists, else `docs/human/<mode>-<short-name>.html`.
- **repo mode:** save instead in the HQ folder at `human/YYYY-MM-DD-owner-name.html` (today's date; overwrite a same-day page, keep older ones). Then commit and push under hq's sync rule.
- **pr mode:** link the page from the PR description.
- **ramp mode:** link the page from `RAMP.md` and `.lifecycle/STATE.md`.

## 6. Check before finishing

- Every number appears in a source.
- The Think-it-through box matches the body, and nothing recommends.
- HTML only: well-formed; no external URLs in `src` or `href` except links to sources; if a headless browser is available, look at it at phone and desktop widths.
- Report: for a page, two lines (where it is, and the question it asks). For chat, the explanation is the report.
