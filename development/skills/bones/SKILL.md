---
name: bones
description: Build the thinnest working skeleton of one component from a confirmed /scope card, with simple, test-first code, so it stands on its own. Use for /bones.
---

# Bones

Build exactly what the scope card says, as thin as possible, test first, so it stands. No growing. Your ideas wait until asked.

## Voice

Plain words. Short sentences. Answer first. No preamble, no recap, no praise.

## Input

A confirmed card at `docs/scope/<slug>/scope.md`. No card, or not confirmed → run /scope first.

## Files

Next to the card:

- `bones.md`: one line per step, saying how it was built.
- `envelope.md`: your withheld ideas. Sealed.
- `risks-accepted.md`: one-way doors the user chose to leave open.

Don't edit `scope.md`. If the build shows the card is wrong, stop and tell the user. They fix it with /scope.

## Code rules

Keep it simple. The plain way wins.

- **Functions first.** Use a class only when state must live between calls and passing it around gets messy. Say why in `bones.md`.
- **Plain data:** dicts, lists, simple records.
- **No abstraction** until the same code shows up 3 times.
- **Standard library first.** No new dependency unless the user named it.
- **One file** until it gets hard to read.
- Small functions, clear names. No comments that repeat the code.

## Test first, every step

For each step:

1. Write one small test for what the step should output. Run it. It fails.
2. Write the least code that makes it pass.
3. Run all tests.

For a stub, test the shape of the output, not the values. That test stays when the stub is filled in later.

Keep tests thin: one per step, one per "Done when" check. No mocks unless the step calls something outside, like a network or an external service.

## 1. Build

Build the thinnest thing that meets "Done when" along the Path. Hardcode values, skip error handling, use test data. It must run end to end.

If a step is too big to build now, stub it: fake its output.

For each step, add one plain line to `bones.md`:

```
<step #>: <what it does, how> | built | STUB | agent's choice
```

Add nothing outside the card. When you want to (a retry, a config layer, an abstraction, a different approach), add one line to `envelope.md` instead:

```
<step #>: <what you'd do> | <why> | source: code, data or hypothetical
```

## 2. Check

Run the "Done when" checks. Report pass or fail in 3 lines or less.

## 3. Door check

Raise at most 3. Only one-way doors: choices that get baked in and cost a lot to change later. Examples: data model, storage format, coordinate system, anything that can't be undone. Retries, caching, config and abstractions are two-way doors. They go in the envelope.

Format:

**Door 1: <name>**
Breaks if: <what happens>. Source: code, data or hypothetical.
Fix now: <cost>. Fix later: <cost>.
What do you want to do?

If the source is hypothetical, also ask: "Is this likely for you?"

Wait for the user's answer. Then give your pick in one line, if you have one.

The user picks:

- **Fix now.** Do it, test first.
- **Accept.** One line in `risks-accepted.md`: door, what could break, date, the user's reason.
- **Decide later.** It becomes a /map decision ticket.

## 4. Ship

All tests pass → commit, with a one-line message.

## 5. Close

Ask the user to say in one or two sentences what got built. Correct only what's wrong.

Then trace: every piece of the code should map to a step on the card. List anything that doesn't. If the repo has an over-engineering review skill, run it with `scope.md` as the baseline instead.

Stop. Growing is a separate job.

## The envelope

Stays sealed. Open it only when the user asks. Show it grouped by step. Don't argue for any item.

When something breaks later, check the envelope first. Tell the user if the problem was in there.

## Never

- Build anything not on the card.
- Write code before its test.
- Add a class, abstraction or dependency the code rules don't allow.
- Grow past the card.
- Raise two-way doors as risks.
- Edit the scope card.
- Pad. If a sentence can go, cut it.