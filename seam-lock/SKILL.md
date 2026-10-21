---
name: seam-lock
description: After to-tickets and before implement-spec: commit contracts, stubs and golden fixtures, amend the tickets to point at them, and run an adversarial review of the split.
---

# Seam Lock

Parallel implementer agents fail at the boundaries between them. to-spec has already sketched the test seams, and to-tickets has already sliced the work into a task graph. This skill makes those seams *real and committed* before anyone builds, then attacks the split.

It does not rewrite the spec or re-slice the tickets. It amends them.

Inputs: the spec issue, its implementation tickets, the repo's ADRs and domain glossary (wherever `setup-matt-pocock-skills` configured them), and `.lifecycle/STATE.md` if present.

## 1. Pre-flight (thin, usually silent)

1. Read the ADRs. Treat settled decisions as fixed.
2. List only the *new* decisions this step needs: exact interface shapes, schemas, conventions (units, CRS, IDs, nulls, time zones, error handling), and which golden fixtures to use.
3. Draft a default for each, drawing on the spec and the ADRs.
4. Flag any decision that is one-way or low-confidence.
5. If nothing is flagged, record the new decisions as ADRs and continue. If something is flagged, send one short decision sheet (decision, default, reason, each in at most two lines) and keep working on anything that doesn't depend on it.

## 2. Commit the seams

- **Contracts:** interfaces, data schemas and conventions for every seam the spec names. Each is stated once, as code where possible (types, schemas), with short prose only where code can't say it.
- **Stubs:** every interface implemented as a stub that type-checks and returns plausible placeholder output. This lets the pipeline (tracer) tickets and the algorithm (POC) tickets proceed in parallel against the same reality.
- **Golden fixtures:** a small, hand-checkable set of real inputs with known expected outputs. Deliberately include awkward cases. Add a harness that runs the fixtures against any implementation of the interface.

Commit all of this to the branch that implement-spec will integrate on, or to main if no branch exists yet.

## 3. Amend the tickets

For each implementation ticket, add a short **Seams** section containing:
- links to the contracts it consumes
- the files and modules it owns
- which golden fixtures must pass for it to count as done

Add pointers only. Don't restate contracts.

Then check the task graph:
- no two tickets own the same file
- every contract is consumed by at least one ticket
- every acceptance criterion can be run
- blocking edges cover every real dependency

Fix what you can. If a ticket really needs splitting or merging, flag it.

## 4. Adversarial review

Spawn one fresh subagent that has seen none of this session. Give it pointers only: the spec, the tickets, the contracts and the ADRs. Its brief:

> Attack this split, not just individual tickets. Find gaps (work no ticket covers), overlaps, mismatched assumptions across seams (units, CRS, ordering, nulls, errors), failure modes (what happens when one piece fails or returns empty), and acceptance criteria that would pass while the system is still wrong. Tag each finding one-way or two-way, and rate it high, medium or low. Report in at most 300 words.

Then:
- Fix every two-way finding yourself, in the contracts, fixtures or ticket amendments.
- Batch the one-way findings into a single decision sheet for the user.
- Allow at most two adversary rounds. After that, record what remains as ADRs and stop.

## 5. Hand-off

Update `.lifecycle/STATE.md`: add links to the contracts and fixtures and set the next step to Build. Report in at most five lines: seams locked, tickets amended, findings fixed, anything escalated. Finish with the next command:

```
/implement-spec <spec>
```
