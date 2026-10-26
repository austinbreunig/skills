---
name: human
description: Turn a machine artifact (PR, ramp report, spec, or Wayfinder map) into a beginner-friendly, highly visual, self-contained HTML page a person can understand and decide from.
---

# Human

Specs, tickets and ADRs are written for machines. This skill writes the version for the person who has to **understand the change and make a decision about it**. The reader is smart but new to this code. They should finish the page in about five minutes, knowing what changed, why, what could go wrong, and what they need to decide.

## Modes

Work out which mode applies from the input, or take it from the argument:

- **pr:** a pull request or integration branch. Reads the diff, the linked spec and tickets, test results, and the code-review output.
- **ramp:** a `RAMP.md`. Reads the level 0 result, the levels, metrics, capacity statement and break list.
- **spec:** a spec issue, before slicing or after wu-wei.
- **map:** a Wayfinder map: the decisions so far, the frontier, and the fog.

## 1. Gather facts (from sources only)

Read the artifact and follow its pointers: the linked tickets, ADRs, contracts, diff and test output. Collect real facts:
- names, numbers, file paths, metrics
- the decisions made, and the reason given for each

**Never invent numbers, results or reasons.** If a fact isn't in the sources, leave it out or mark it plainly as unknown. Every claim on the page should be traceable to a source you can link.

## 2. Find the story

Before writing anything, answer in one sentence each:
1. What is this, in words a newcomer would use?
2. Why does it exist? What problem or goal does it serve?
3. What is the single most important thing the reader must understand?
4. What decision, if any, does the reader need to make, and what's the recommended answer?

The page is built around these four answers.

## 3. Page structure

In order. Leave out any section that has nothing real in it.

1. **Decision box** (top, impossible to miss): what the reader needs to decide, the recommended choice, and why, in at most three lines. If no decision is needed, say "Nothing to decide, just review."
2. **In one paragraph:** the story from step 2, in plain language.
3. **The picture:** at least one diagram showing the real mechanism, not decoration.
   - pr: data or control flow through the components touched, with changed parts highlighted, and a before/after view if behavior changed.
   - ramp: levels on a chart against the exit criteria, the point where it breaks, and accuracy drift.
   - spec: components and the seams between them.
   - map: decisions made, the frontier, and the fog, shown as a map.
4. **What changed and why:** a few short cards, one per meaningful change or decision. Each says what it is, why, and links to the source (file, ticket or ADR).
5. **What could go wrong:** risks, edge cases, and anything the adversary, break-it pass or code review flagged, with how each is handled or why it's accepted. Be honest; don't make it sound safer than it is.
6. **How we know it works:** test, fixture and break-it results, ramp numbers, and what is still untested.
7. **Glossary:** each domain or technical term used on the page, in one plain line.
8. **Go deeper:** collapsible `<details>` sections for anyone who wants detail: key code excerpts (short), full metric tables, links.

## 4. Writing rules

- Plain words. Define each term the first time it appears, or use a simpler one.
- Short sentences. One idea per sentence.
- A concrete example or analogy for every abstract idea.
- Lead with what matters. No preamble.
- Numbers keep their units and context: "4.2 s per tile (was 9.8 s)", not "faster".

## 5. Visual rules

- **One self-contained HTML file.** Inline CSS and inline SVG. Nothing loaded from the network, so it opens offline and renders the same everywhere.
- Readable on a phone: a single column, a 16px side margin, and no horizontal scrolling.
- Works in light and dark mode: define colors as CSS variables on `:root` and redefine them under `prefers-color-scheme: dark`.
- Use a restrained palette and one highlight color for "changed" or "needs attention". Use color for meaning, not decoration.
- Every diagram gets a one-line caption saying what to notice.
- Charts get labeled axes and units. Mark the thresholds and the break point directly on the chart.

## 6. Output and check

- Save to `.lifecycle/human/<cycle>-<mode>-<short-name>.html`. If `.lifecycle/` doesn't exist, use `docs/human/`.
- **pr mode:** add a link to the page in the PR description.
- **ramp mode:** link it from `RAMP.md` and from `.lifecycle/STATE.md`.
- Before finishing, check:
  - the file has no external URLs in `src` or `href` except links to sources
  - the HTML is well-formed
  - every number on the page appears in a source
  - the decision box matches the recommendation in the body
  - if a headless browser is available, render the page at phone and desktop widths and look at it
- Report in two lines: where the page is, and the decision it asks for.
