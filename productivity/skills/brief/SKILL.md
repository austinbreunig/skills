---
name: brief
description: Show where every connected repo stands, most recently active first. For each repo, where you left off, the last EOD, open PRs and tickets, and recent jots. Read-only. Use at the start of the day, or whenever you want the big picture.
---

# Brief

The brief is the one report of where every connected repo stands. `/brief` shows it on its own, and `/eod` shows it at the end of every run, built on the EOD compilation it just wrote.

Follow the "Rules for every hq skill" section of `productivity:hq` (config, gh, transcripts). Find the HQ folder as in its **Find HQ** step.

**Read-only.** The only change brief makes is `git pull` in the HQ folder. It never writes, commits or pushes anything, in the HQ repo or in any project repo.

## 1. Gather

Read `repos.txt`. If it lists no repos, say "No connected repos yet. Run /hq add <repo>." and stop.

**Last EOD.** The latest EOD compilation is the newest `eod/YYYY-MM-DD.md` by file name. **Since the last EOD** means from the start of the day after its date (local time) until now. If there is no compilation, it means the last 7 days.

For each connected repo, gather:

- **Left off.** Read transcripts by `productivity:hq`'s transcript rule:
  - Go through the files newest modified first. The first file with a record that maps to the repo is its newest session, even if it is after the last EOD.
  - From that file, use the newest `"subtype":"away_summary"` record (its `content`), else the newest `"type":"ai-title"` record (its `aiTitle`).
  - Keep the timestamp of that file's newest record.
  - Read only `type`, `subtype`, `uuid`, `cwd`, `timestamp`, `content` (of `away_summary` records) and `aiTitle`. Never the messages.
  - No subagent. Stop once every connected repo has a session.
- **Last time.** The repo's section in the latest compilation (its `## owner/name` heading through to the next `## ` heading), copied verbatim.
- **Open PRs.** `gh pr list -R <repo> --state open --json number,title,url,isDraft,reviewDecision,statusCheckRollup,updatedAt`.
- **Open tickets.** All open issues with their assignees, native blockers and last update, through `gh api graphql`:
  ```
  query($owner:String!,$name:String!){repository(owner:$owner,name:$name){
    issues(states:OPEN,first:100){nodes{number title url updatedAt
      assignees(first:5){nodes{login}}
      blockedBy(first:10){nodes{state}}}}}}
  ```
- **Closed since the last EOD.** Issues and PRs closed or merged in that window: `gh issue list -R <repo> --state closed --search "closed:>=<YYYY-MM-DD>" --json number,title,url,comments` and `gh pr list -R <repo> --state all --search "closed:>=<YYYY-MM-DD>" --json number,title,url,state,body,comments`. For each PR, also read its review comments: `gh api repos/<repo>/pulls/<number>/comments`.
- **Jots.** Current jots (see `productivity:jot`) whose `repo:` line is the repo (ignore case). Jots tagged `General` go to the General section.

## 2. Order

A repo's **last activity** is the newest of: its left-off session timestamp, its newest jot, the newest `updatedAt` on its open PRs and tickets, and its newest closed item.

A repo is **quiet** if it has no activity in the last 7 days and no section in the latest compilation. Quiet repos get one line, `owner/x — quiet`, after the active ones.

Show active repos most recent activity first.

## 3. Show

One section per active repo, in this shape:

```
## owner/name
Left off: <away_summary or ai-title>   (or: no session found)

### Last time
<the repo's section of the latest compilation, verbatim>   (or: No EOD yet.)

### Now
PRs
- [#31 Add tile cache](link) — waiting on review, checks failing
- [#29 Spike: new parser](link) — draft

Tickets
- [#12 Load config from env](link)
- [#14 Retry on 503](link) — @sam
- [#15 Cache tiles](link) (blocked)
- +3 more

Closed since the last EOD
- [#11 Parse headers](link) — closed
  - Fixed by #30; edge case for empty files noted.

### Jots
- 10-23 14:15 — <summary>
```

Rules for **Now**:

- **PRs.** Each PR's state, joined with ", ":
  - `draft` if `isDraft`.
  - Else `waiting on review` if `reviewDecision` is empty or `REVIEW_REQUIRED`; `approved` or `changes requested` otherwise.
  - Add `checks failing` if any check in `statusCheckRollup` ended as a failure, cancel or time-out.
- **Tickets.** Unblocked tickets first, by number. Then blocked tickets (any `blockedBy` issue still `OPEN`), by number, each marked `(blocked)`. Add `— @login` for each claimed (assigned) ticket. Show at most 10, then `+N more` for the rest.
- **Closed since the last EOD.** Each item in `productivity:eod`'s **Item shape** (step 3).
- Leave out a part (PRs, Tickets, Closed) with nothing in it. If all three are empty, write "Nothing open."

**Jots** part: `MM-DD HH:MM — <summary>`, oldest first. Leave the part out if there are none.

After the active repos, the quiet lines. Then, if there are any current General jots:

```
## General
- 10-24 09:40 — <summary>
```

End with this line on its own:

```
Want a deep-dive on any of these repos?
```

## 4. Deep-dive

If the user names one or more repos, hand the answer to `human:human` in **repo** mode, in chat. Any other answer ends the brief.
