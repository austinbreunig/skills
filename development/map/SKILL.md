# Map

The user names the parts. Each part becomes a small ticket. Each ticket goes through /scope, then /bones. The map is done when every part stands on its own.

## Voice

Plain words. Short sentences. Answer first. No preamble, no recap, no praise.

## Where it lives

Use the repo's issue tracker if its docs name one. Labels: `map` for the map, `map:<type>` for tickets.

Otherwise, local markdown: `docs/map/<slug>/map.md`, plus one file per ticket in `docs/map/<slug>/tickets/`.

## 1. Get the parts

Ask the user to walk you from A to B and name the parts along the way, in their own words.

Ask follow-ups only by the /scope question rules: gap or assumption, max 3 per round, every question with its "Why" line.

Never add a part the user didn't name. If the path seems to skip something, ask it as an assumption: "This goes straight from A to C. Is there a step between?"

Only one part? You don't need a map. Run /scope.

More than 8 parts? Show the list and ask the user which to cut or merge.

## 2. Chart the map

One session. Chart only. Don't scope or build any ticket.

Ticket types:

- **component**: one part of the project. Goes through /scope, then /bones.
- **decision**: a choice that spans parts and only the user can make. Example: a shared data format.
- **research**: a fact you can look up.

**Small:** a component ticket goes from /scope to /bones in one session. If it can't, split it.

Ticket format:

```
## Part
<one line: what it does>

## In → Out
<what comes in> → <what goes out>

## Status
open | scoped | bones

## Source
<user | door | break>: <pointer>

## Blocked by
<tickets, or none>
```

"In → Out" is one line. It says how parts connect, not how they work. The shape tests from /bones hold it in place.

Create all tickets first, then wire the blocked-by links in a second pass. Tickets with nothing blocking them are the frontier.

Map format:

```
# <destination>

## Path
1. <part> → <ticket link>

## Decided
- <decision, one line> → <ticket link>

## Frontier
- <open ticket with nothing blocking it>

## Fog
- <unclear, but can't be phrased as a question yet>

## Out of scope
- <what the user ruled out>
```

The map is an index. Gist and link only. The detail lives in the ticket.

Stop.

## 3. Work the map

One ticket per session. Pick from the frontier. If there's more than one, let the user choose.

- **component**: run /scope on the ticket, then /bones. Status goes open → scoped → bones.
- **decision**: use the /scope question rules. Write the decision in the ticket, 3 lines max.
- **research**: send a subagent. Answer in 3 lines, with the source.

When a ticket closes, add one line to Decided if it decided something, and update the Frontier.

New tickets come only from:

- a one-way door the user chose to decide later in /bones
- something a skeleton broke on
- a question the user raised

Never from the envelope or your own scenarios.

## 4. Done

The map is done when every component ticket is at bones, the Frontier is empty, and every Fog line is resolved or moved to Out of scope.

Then growing starts. Hand off to /sprint.

## Never

- Add a part the user didn't name.
- Make a ticket for a scenario nobody raised.
- Make a ticket too big for one session.
- Scope or build in the charting session.
- Grow past bones. That's /sprint's job.
- Pad. If a sentence can go, cut it.