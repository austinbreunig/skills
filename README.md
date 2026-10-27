# Skills

## What this is

A Claude Code marketplace with three plugins. `lifecycle` carries one product from idea to production, on top of Matt Pocock's skills. `productivity` keeps track of all your repos from one place, with a brief each morning and a wrap-up each evening. `human` explains anything in plain words and pictures; both plugins use it. Skills stop only for decisions that are yours to make.

## The plugins

| Plugin | What it's for | Needs |
|---|---|---|
| `lifecycle` | Carry one product through development cycles, across fresh sessions | `human`, `mattpocock-skills` |
| `productivity` | Keep track of many repos from one private HQ repo | `human` |
| `human` | Explain, show and guide, at the reader's level | nothing |

Needed plugins install for you.

## Prerequisites

A plugin can't install these, so set them up first:

- **git**
- **GitHub CLI**, logged in. Check with `gh auth status`. If it fails, run `gh auth login`. Get `gh` at https://cli.github.com.

## Install

In Claude Code:

```
/plugin marketplace add austinbreunig/skills
/plugin install lifecycle@austinbreunig-skills
/plugin install productivity@austinbreunig-skills
```

Install one plugin or both. `human` comes along with either. `lifecycle` also pulls in `mattpocock-skills` from the official marketplace.

Commands are bare: `/lifecycle`, `/hq`, `/human`. No plugin prefix needed.

For `productivity`, run `/hq` once to set up your HQ repo.

## Updating

Auto-update is **off** by default for third-party marketplaces like this one. To turn it on: run `/plugin`, open **Marketplaces**, pick `austinbreunig-skills`, and choose **Enable auto-update**.

To update by hand:

```
/plugin marketplace update austinbreunig-skills
```

Every merge to `main` is a release. There are no version numbers. To hold a known-good copy, pin a commit or branch with `#ref` when you add the marketplace:

```
/plugin marketplace add https://github.com/austinbreunig/skills.git#<commit-or-branch>
```

## Works with

Tested with **mattpocock-skills 1.3.1**. If a call to one of its skills breaks, suspect a newer version first.

`/lifecycle` runs `to-spec` and `to-tickets` for you. It publishes the spec and tickets as GitHub issues without asking, and you review them at spec sign-off. It never runs `wayfinder`, `grill-with-docs` or `implement-spec`; those are always yours to type.

## Skills

**lifecycle**

- [`/lifecycle`](lifecycle/skills/lifecycle/SKILL.md): says where the cycle stands, runs the next agent steps, and stops at your decisions with the exact next command.
- [`/mindful`](lifecycle/skills/mindful/SKILL.md): cuts forced or unneeded complexity. Stays on quietly during grilling, or reviews a spec, its tickets or a branch.
- [`/ramp`](lifecycle/skills/ramp/SKILL.md): plans how to pressure-test a built pipeline. Charts a map that ends in one spec for a ramp harness.
- [`/seam-lock`](lifecycle/skills/seam-lock/SKILL.md): commits contracts, stubs and fixtures before the build, then attacks the ticket split.
- [`/cycle-retro`](lifecycle/skills/cycle-retro/SKILL.md): looks back on a whole cycle and proposes edits so the next one needs fewer stops.

**productivity**

- [`/hq`](productivity/skills/hq/SKILL.md): sets up your HQ repo, shows the home screen, and adds or removes connected repos.
- [`/brief`](productivity/skills/brief/SKILL.md): where every connected repo stands: where you left off, the last EOD, open PRs and tickets, recent jots.
- [`/eod`](productivity/skills/eod/SKILL.md): wraps up the day into an EOD compilation, then shows the brief and your action items.
- [`/jot`](productivity/skills/jot/SKILL.md): saves a short note about this session, or lists current jots.

**human**

- [`/human`](human/skills/human/SKILL.md): explains a PR, spec, map, ramp report, repo or anything else, in chat or as an HTML page. Asks questions; never recommends.

How the lifecycle skills fit together: [docs/Lifecycle Skills.md](docs/Lifecycle%20Skills.md).

Words used across the skills: [GLOSSARY.md](GLOSSARY.md).

## Contributing

Changes land only by pull request. `main` is protected (see [docs/protect-main.md](docs/protect-main.md)).

Every PR runs `claude plugin validate .`, and it must pass. Run it yourself before you push. The PR description is the record of the change; there are no release notes.

If you change or add a term, update [GLOSSARY.md](GLOSSARY.md) in the same PR.
