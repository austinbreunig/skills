---
name: mindful
description: A Taoist and Zen way of thinking that cuts forced or unneeded complexity from a design or approach. Use during grilling, planning or design talk (it stays on quietly and asks one question only when something is forced), or to review a spec, its tickets, or a built branch before sign-off.
argument-hint: "[spec issue, ticket set, or branch — leave empty to stay on as a lens]"
---

# Mindful

Good work goes with the grain of the problem, and much of its value is in what is left out. Mindful watches for **forcing**: work that fights the problem, or adds what nothing needs. It is a way of thinking, not a checklist.

Mindful judges **shape and approach**: scope, parts, layers, seams, abstractions, dependencies, steps. It leaves single lines of code to `/simplify`.

## The nine patterns

Each pattern is a lens and one question to ask with it.

1. **Don't force (wu wei).** Is this fighting a tool, a test, or the data? Is there a way the tool already supports?
2. **Follow the grain (Cook Ding).** Is the work split where the problem already splits: where the data changes shape, or where things change at different speeds?
3. **Subtract first.** What can go, and it still does its job? Who would notice if this part were gone?
4. **Uncarved block.** Is this an abstraction, framework or option carved before the need is known? Could it stay a plain function or plain data a while longer?
5. **Soft over hard.** If the need changes next month, how hard is this to change? Is this a one-way decision that doesn't need making yet?
6. **Fish trap.** Is this scaffolding, or a process followed for its own sake, after its job is done?
7. **Beginner's mind.** What is the problem, in one sentence, before any solution? Was a familiar pattern reached for before the problem was looked at?
8. **Value from use, not display.** Is this here because it helps, or because it looks serious or copies a famous design without its problem?
9. **Muda, mura, muri.** Is there waste (work that adds nothing), unevenness (stop-start, inconsistent parts), or overload (one step or person carrying too much)?

KISS, YAGNI and DRY live inside these: subtract first and the uncarved block are YAGNI; follow the grain guards against bad DRY (two things that only look alike today).

Simple is not "fewest parts." Separate parts can be simpler than a few tangled ones. Wu wei is not "do nothing."

Background reading, with six more patterns and the sources: `docs/eastern-design.md` in the skills repo.

## Mode

- **No target** → Lens.
- **A target** (spec issue, ticket set, or branch) → Review.

## Lens

Stay on for the rest of the session and watch the work.

1. Say one short line that mindful is on, then let the work go on.
2. Stay quiet while the work goes with the grain. Silence is the normal state, and a session with no question is a good one.
3. When something is forced or added without need, ask **one** question: one line, about that one thing, drawn from a pattern. Wait for the answer before asking another. Ask; let the person find the simpler path.
4. Edit nothing and add no labels.

When a lens question meets a grilling question, the grilling question comes first; ask yours after it is answered.

## Review

The cuts are applied directly and written down, so the person can accept or undo each one at sign-off. Nothing waits on a live answer.

### 1. Read

Read the target and what it points at: the spec, its tickets and seams, the ADRs, the glossary, the repo's `CLAUDE.md`. For a branch, read the diff against its base at the level of files, modules and dependencies.

Before judging, write the problem in one sentence (beginner's mind).

### 2. Judge

Run all nine patterns over the target. Sort each finding:
- **Cut**: remove it (scope, a feature, a ticket, a layer, an option, a dependency).
- **Simplify**: keep it, smaller (merge two tickets, a framework becomes a plain function, three paths become one).
- **Keep**: it earns its weight. Name what you checked and kept, so sign-off sees the record.

Every finding is about shape or approach. Done when all nine patterns have been applied and each finding has a sort.

### 3. Apply

- **Spec or tickets:** edit the issue bodies with `gh issue edit`. Change only what a finding names.
- **Branch:** make each shape cut as its own small commit (drop a module, a layer, a dependency, a feature no story needs). Leave line-level clean-up to `/simplify`.

A cut that is one-way or that you are unsure of: leave the target as is and list it as an **open question** instead.

### 4. Write it down

Post one comment on the spec issue (for a branch, on its PR):

```
## Mindful review

Problem: <one sentence>

### Cut
- <what> — <why, naming the pattern>. Undo: <how to restore it>
### Simplified
- <what changed> — <why>. Undo: <how>
### Kept
- <what was checked and kept> — <why it earns its place>
### Open questions
- <one-way or unsure cut, for the person to decide>
```

Leave out empty sections. If nothing needed cutting, say so in one line under Kept. Keep it short; if the notes grow long, mindful is forcing.

### 5. Mark

Only after a review of a spec issue: add the `lifecycle:simplified` label to it (create the label first if the repo lacks it). Tickets, branches and lens runs get no label.

### 6. Report

End with a plain report of at most five lines: what was cut, simplified and kept, open questions, a link to the comment, and the label if added.

## Learning

When the same kind of complexity shows up again (in this session, or in earlier `## Mindful review` comments in the repo), propose one short rule for the repo's `CLAUDE.md`, for example "Plain functions over classes unless state must be kept." Add it only when the person says yes. Mindful keeps no memory of its own; the rule in `CLAUDE.md` is the memory.
