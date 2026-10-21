---
name: ramp
description: Pressure-test a built pipeline: an adversarial break-it pass first, then real data at rising volume and variety, to find where it breaks, revalidate the algorithm, and produce a capacity statement and break list.
---

# Ramp

The pipeline already works. The question now is where it breaks. Attack it in order of cost:
- **Level 0** finds cheap bugs with synthetic attacks.
- **Volume** finds performance limits with real data.
- **Variety** finds edge cases with real data.

Re-check the algorithm at every level, because accuracy can drift as scale grows.

`/code-review` (run inside implement-spec) checks conformance: does the code match the standards and the spec? This skill is the adversarial side: how can the code be broken?

How far a ramp goes depends on the cycle's destination in `.lifecycle/STATE.md`. A POC cycle might ramp to one county; a production cycle ramps to the full target load, with headroom.

Inputs: the integration branch or merged code, the contracts, the golden fixtures, the ADRs, `.lifecycle/STATE.md`.

Safety: treat source data as read-only. Write outputs to a scratch location. Never touch production systems unless an ADR explicitly allows it.

## 1. Instrument first

Confirm or add, before any ramp run:
- timing and peak memory for each stage
- record counts in and out of each stage
- a **quarantine** output: records that fail go there with a reason, instead of crashing the run
- cost tracking, if the pipeline runs on paid compute

## 2. Level 0: break-it pass (synthetic, cheap)

Spawn one fresh subagent that has seen neither the implementation sessions nor this one. Give it pointers only: the contracts, the code, the golden fixtures and the ADRs. Its brief:

> Your job is to make this code fail. Write tests that you expect to fail, against the contracts:
> - property-based tests (e.g. Hypothesis) over the contract's input space
> - boundary cases: empty, single-element, maximum-size and degenerate inputs
> - malformed inputs: invalid, null and wrongly typed values
> - domain edge cases. For geospatial work, for example: invalid or self-intersecting geometries, empty geometries, mixed or missing CRS, antimeridian and poles, precision at tile boundaries
> - operational failures: idempotency (running the same job twice), retries, partial failure mid-run, re-ordering of inputs
>
> Commit the tests to a `break-it` branch. Report each failing test in at most 300 words: the test, what failed, and your guess at the cause.

Then, for each failure:
- **Classify** it as performance, data edge case, or algorithm (see section 4).
- If the fix is small and reversible, call the Skill tool with "tdd" to fix it, keeping the failing test as the red test.
- Otherwise, log it to the break list.

Keep the passing break-it tests as a permanent regression suite. Volume levels start only once level 0 has no unclassified failures.

## 3. Baseline, then pre-flight

Run the smallest real-data level (about 1% of the destination's target) to get baseline timings and accuracy. Then do the pre-flight, now based on real numbers:

1. Read the ADRs, including any earlier cycle's ramp plan.
2. Draft the ramp plan:
   - **Levels:** default 1% → 10% → 50% → 100% of the destination's target load. Production destinations add a headroom level, e.g. 150%.
   - **Exit criteria for each level:** throughput, peak memory, cost, quarantine rate, and the algorithm accuracy metric on the golden fixtures and on a spot-check sample. Base the thresholds on the baseline and the destination.
   - **Variety strata** to sample at every level, taken from the domain. For geospatial data, for example: dense versus sparse areas, each geometry type, each CRS present, invalid or empty geometries, antimeridian and poles, nulls, very large features.
3. Flag any criterion that is one-way or low-confidence, e.g. a hard SLA. If anything is flagged, send one short decision sheet; otherwise record the ramp plan as an ADR and continue.

## 4. Run the levels

At each level:
1. Run the pipeline on a sample stratified across the variety list.
2. Run the golden fixtures and the break-it suite as regression checks.
3. Compare the results with the exit criteria.
4. If every criterion passes, go to the next level.

If a criterion fails:
- **Classify** the failure as one of:
  - **performance:** slow, out of memory, too costly
  - **data edge case:** crash or quarantine spike tied to a stratum
  - **algorithm:** accuracy drifts or fixtures fail
- **Fix only what blocks the next level.** If the fix is small and reversible, make it on a branch, call the Skill tool with "tdd" for it, re-run the level and continue. Otherwise stop the ramp at this level.
- Log every failure, fixed or not, in the break list.

Don't optimize anything that isn't blocking.

## 5. Report

Write `RAMP.md` for this cycle, and link it from STATE. It contains:
- **Level 0 result:** the number of break-it tests, the failures found, fixed and logged, and a link to the suite.
- **Capacity statement:** "Holds to X, slows at Y, breaks at Z because W."
- A table of levels against criteria.
- Accuracy drift across the levels.
- **Break list:** each entry has its class, the evidence, and the open question it raises, written so it can seed the next cycle (as Wayfinder input if the breaks are foggy, or grill-with-docs or to-spec input if they're clear).
- The fixes applied during the ramp, with links.

Then invoke `human` in ramp mode on `RAMP.md`, to produce the visual page used at Verdict.

## 6. Hand-off

Update `.lifecycle/STATE.md`: link `RAMP.md` and the ramp page, record appetite spent, and set the next step to Verdict. Report in at most five lines: the level 0 result, the capacity statement, the top three breaks, and appetite spent. Finish with: run `/conductor` for the Verdict.
