# Lifecycle Skills

A thin layer around Matt Pocock's skills that carries a product from idea to production, one fresh session at a time. `/lifecycle` navigates. The other skills do the work Pocock's skills don't cover. Every step leaves a marker that `/lifecycle` can check.

Each skill's `SKILL.md` is the source of truth. This page shows how they fit; it doesn't restate them.

| Skill | Job |
|---|---|
| [lifecycle](../lifecycle/skills/lifecycle/SKILL.md) | Navigator. Run it at the start of every fresh session. |
| [mindful](../lifecycle/skills/mindful/SKILL.md) | Cuts forced or unneeded complexity from the shape of the work. |
| [seam-lock](../lifecycle/skills/seam-lock/SKILL.md) | Commits contracts, stubs and fixtures, then attacks the split. |
| [ramp](../lifecycle/skills/ramp/SKILL.md) | Plans how to pressure-test a built pipeline. |
| [cycle-retro](../lifecycle/skills/cycle-retro/SKILL.md) | Measures the cycle and proposes workflow edits. |
| [human](../human/skills/human/SKILL.md) | Turns specs, PRs, maps and ramp reports into pages a person can decide from. |

## One cycle

Clear the session, run `/lifecycle`, do what it asks. Repeat.

A **human step** is a decision only you can make. Everything else is an **agent step**: `/lifecycle` runs those back to back, each in its own subagent, and stops at the next human step.

```
Start -> Route (map or grill) -> Spec chain -> Build chain -> Ramp tail (ramp: yes) -> Verdict -> Retro
```

You set the start, walk the route, sign off each spec and PR, and make the Verdict. The Retro runs in your session and asks which edits to apply.

To push back on a spec, comment on the spec issue; the chain reruns from the first step your change affects. To ask for PR changes, each change becomes a ticket and you run `/implement-spec` again.

After the Verdict, Continue starts the next cycle with a more demanding destination. Re-shape keeps the goal and tries a new approach.

The full step tables, gates and markers are in [lifecycle's SKILL.md](../lifecycle/skills/lifecycle/SKILL.md).
