---
name: jot
description: Save a jot about this session to the HQ repo (`/jot <text>`, `/jot --repo owner/x <text>`), or list current jots (`/jot`).
---

# Jot

A jot is a very short note the agent writes from what the user says mid-session. It lives in the HQ repo's `jots/` folder, one file per jot. A jot is **current** while its file-name date is at most 7 days before today. `productivity:brief`, `productivity:eod` and `human:human` show only current jots, and `productivity:eod` deletes the rest. There is no manual remove.

Follow the "Rules for every hq skill" section of `productivity:hq` (config, sync, gh). Find the HQ folder as in its **Find HQ** step.

Pick the branch from the argument:

- text (with or without `--repo owner/x`) → **Write**
- nothing → **List**

## Write

1. **Tag.** Pick the repo tag:
   - `--repo owner/x` given: use `owner/x`.
   - Else read the current folder's `git remote get-url origin` and turn it into `owner/name`. If `repos.txt` lists it (ignore case), use it.
   - Else use `General`.
2. **Branch.** If the tag is the current folder's repo, use `git branch --show-current`. Else `-`.
3. **Summary.** Write the shortest summary of what the user said that keeps its meaning. Use your own words, never theirs. One line is best; three at most.
4. **File.** Get the local time with `date '+%Y-%m-%d %H:%M'`. Write `jots/YYYY-MM-DD-HHMM-<id>.md` in the HQ folder, where `<id>` is 4 random lowercase letters and digits not already used by a file of that name:
   ```
   time: 2026-10-23 14:15
   session: ${CLAUDE_SESSION_ID}
   repo: owner/name
   branch: main

   <summary>
   ```
   The session line is already filled in with this session's id. Copy it as is.
5. Commit ("Jot for <tag>") and push (sync rule).
6. Say "Jotted for `<tag>`: <summary>"

Never write anything in the current project folder.

## List

Read every current jot in `jots/`. Show them oldest date first, and by time within a date:

```
- 2026-10-22
  - 09:40 — owner/a — <summary>
- 2026-10-23
  - 14:15 — General — <summary>
  - 16:02 — owner/b — <summary>
```

If there are none, say "No jots yet."
