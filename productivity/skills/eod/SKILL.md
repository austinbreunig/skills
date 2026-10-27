---
name: eod
description: Wrap up the day. Writes an EOD compilation to the HQ repo (per connected repo, what the sessions covered, issue activity and action items), prunes old jots, then shows the brief and the action items. Use at the end of the day.
---

# EOD

`/eod` writes the day's **EOD compilation**, `eod/YYYY-MM-DD.md` in the HQ repo, then shows the brief built on it. It reads your session transcripts and GitHub; it never creates issues and never writes in a project repo.

Follow the "Rules for every hq skill" section of `productivity:hq` (config, sync, gh, transcripts). Find the HQ folder as in its **Find HQ** step.

Read `repos.txt`. If it lists no repos, say "No connected repos yet. Run /hq add <repo>." and stop.

## 1. Window

Get today's local date with `date +%F`.

- **Start:** the day after the newest `eod/YYYY-MM-DD.md` dated before today (by file name), at 00:00 local time. Skipped days fold in this way. If there is none, start at today 00:00.
- **End:** now.

The file is always `eod/<today>.md`. A rerun on the same day rebuilds it from scratch over the same window.

Turn the start into UTC once, `date -u -d '<start date> 00:00' +%Y-%m-%dT%H:%M:%SZ`. Transcript and `gh` timestamps are UTC, so compare them to that.

## 2. Sessions

Find which records belong to which repo, by `productivity:hq`'s transcript rule:

- Only files modified since the start.
- Keep records whose `timestamp` is at or after the start.
- Here read only `type`, `uuid`, `cwd` and `timestamp`. The subagents below read the messages.

Each record counts toward its own repo, so one session can count toward several repos.

A mapped repo that `repos.txt` doesn't list (ignore case) is **unconnected**. Note its name for the closing line and nothing else.

For each connected repo with records, start one subagent (all in parallel). Give it the window, the file paths, and the `cwd` values that map to the repo. Tell it:

> Read only records whose `cwd` is one of these and whose `timestamp` is in the window. From `"type":"user"` records read the prompt text (skip `tool_result` blocks and `isMeta` records). From `"type":"assistant"` records read only `text` blocks (skip `tool_use` and `thinking`). Ignore every other record type. Return:
> 1. **Sessions:** 2–6 short bullets on what was done and decided, in plain words.
> 2. **Loose ends:** things said to be left to do, unfinished or worth a ticket. One line each.

## 3. Issue activity

For each connected repo, list every issue and PR opened, commented on, closed or merged in the window. Comments from anyone count.

```
gh issue list -R <repo> --state all --search "updated:>=<start date>" --json number,title,url,state,createdAt,closedAt,comments
gh pr list -R <repo> --state all --search "updated:>=<start date>" --json number,title,url,state,createdAt,closedAt,mergedAt,body,comments,reviews
```

Keep an item only if its `createdAt`, `closedAt`, `mergedAt`, or a comment or review `createdAt` is at or after the start. For a kept PR, also read its review comments: `gh api repos/<repo>/pulls/<number>/comments`.

**Item shape.** Write each kept item like this (`productivity:brief` uses the same shape):

```
- [#31 Add tile cache](link) — merged
  - Adds a disk cache for tiles; review asked for a size limit, added.
```

- State: `open` or `closed` for issues; `open`, `merged` or `closed unmerged` for PRs.
- Then one or two bullets summarizing the comments in the window. For PRs: the description, comments and review comments.
- No bullets if there's nothing to say.

## 4. Action items

From each repo's loose ends, drop any already covered by an open issue (`gh issue list -R <repo> --state open --json number,title`). The rest are its action items, one line each. **Never create an issue.** Listing them is all eod does.

## 5. Write

A repo is **active** if it has any session bullets, issue activity or action items. Quiet repos are left out. Write `eod/<today>.md`, overwriting it if it exists:

```
# EOD 2026-10-27
Covers 2026-10-25 to 2026-10-27.

## owner/name

**Sessions**
- Added a tile cache and tuned its size limit.

**Issue activity**
- [#31 Add tile cache](link) — merged
  - Review asked for a size limit; added.

**Action items**
- Document the cache folder in the README.
```

- One `## owner/name` section per active repo. Brief reads a repo's section by exactly this heading, so use the `owner/name` from `repos.txt`.
- Inside a section use only bold part names, never `#` headings.
- Leave out a part with nothing in it. If no repo is active, write "No activity." under the `Covers` line.
- Never copy jots in. Never mention unconnected repos in the file.

## 6. Prune jots

Delete every jot that isn't current (see `productivity:jot`). Leave the rest.

Commit the compilation and the deletions ("EOD <today>") and push (sync rule).

## 7. Show

In chat, in this order:

1. **The brief.** Run `productivity:brief` steps 1–3 (Gather, Order, Show). Its **Last time** now reads the compilation just written. Leave out its closing deep-dive line; it comes last here.
2. **Action items**, grouped by repo:
   ```
   ## Action items
   owner/name
   - Document the cache folder in the README.
   ```
   Or "No action items."
3. If there were unconnected repos, one line: "Also worked in: `owner/x`, `owner/y` (not connected). Run `/hq add owner/x`."
4. This line on its own:
   ```
   Want a deep-dive on any of these repos?
   ```

Then handle the answer as in `productivity:brief` step 4 (**Deep-dive**).
