---
name: hq
description: Home screen for the HQ repo. Sets it up on first run, shows connected repos and the hq skills, and adds or removes a connected repo (`/hq add <repo>`, `/hq remove <repo>`).
---

# HQ

The HQ repo is the user's private GitHub repo that holds the connected-repo list, EOD compilations, jots and saved repo pages. `/hq` does three things: setup, the home screen, and add/remove. It never shows live GitHub data; that is `/brief`'s job.

Pick the branch from the argument:

- `add [repo]` → **Add**
- `remove <repo>` → **Remove**
- `setup` → **Setup**
- nothing → **Home**

Every branch first runs **Find HQ**, except Setup itself.

## Rules for every hq skill

- **Config:** `~/.config/hq/config` holds one line, `path=<HQ folder>`. That folder is a clone of the HQ repo.
- **Sync:** run `git pull` in the HQ folder before reading it. Right after writing to it, commit and push, without asking. If a pull or push fails, say so in one line and keep going on the local copy.
- **gh:** if any `gh` call fails because `gh` is missing or logged out, stop and show the fix from Setup step 1.
- **Connected repo:** stored as `owner/name` only, one per line in `repos.txt`. Local paths are never stored.
- **Transcripts** (`productivity:brief`, `productivity:eod`, `human:human` repo mode). Each skill says which fields it reads; never more.
  - **Files:** the top-level `.jsonl` files under `~/.claude/projects/*/`.
  - Skip **subagent** files: anything in a `subagents/` folder.
  - Skip **orphaned** files: no `"type":"user"` or `"type":"assistant"` records.
  - Skip **superseded** records: a resumed or forked session repeats older records in a new file. Count each record `uuid` once.
  - **Repo:** map each distinct `cwd` once: `git -C <cwd> rev-parse --git-common-dir`, then that repo's `git remote get-url origin`, parsed as in **Add** step 1, gives `owner/name`. Worktrees count. Ignore records outside git, and git errors on deleted folders.
  - Ignore record types you don't know.

## Find HQ

1. Read `~/.config/hq/config`. If it is missing, run **Setup**, then carry on with the branch the user asked for.
2. If the folder it names is gone, say: "Your HQ folder `<path>` is gone." Offer to run setup again, and stop.
3. Pull (sync rule).

## Setup

1. Run `gh auth status`. If `gh` is missing, stop and show the install page, https://cli.github.com. If it is not logged in, stop and show the fix: `gh auth login`. Change nothing before this check passes.
2. Ask two questions in one message, and skip any the user already answered:
   - HQ repo name (default `hq`)
   - local folder (default `~/hq`)
3. Get the GitHub user with `gh api user --jq .login`. Then:
   - **Repo exists** (`gh repo view <user>/<name>` succeeds): clone it into the folder. If the folder is already a clone of that repo, pull instead.
   - **Repo missing:** create it with `gh repo create <user>/<name> --private`, then clone it into the folder.
4. Add any starter file that is missing (a new or empty repo has none of them):
   ```
   README.md       one short paragraph: this is the HQ repo for the productivity skills; lists what each file and folder holds
   repos.txt       empty; one owner/name per line
   eod/.gitkeep    EOD compilations
   jots/.gitkeep   jots
   human/.gitkeep  saved repo pages from /human
   ```
   If you added any, commit ("HQ starter files") and push with `git push -u origin HEAD`.
5. Write `~/.config/hq/config` as `path=<absolute folder path>`, creating `~/.config/hq/` if needed.
6. If the current folder is a git repo with a GitHub remote, offer to add it (**Add** with no argument).
7. Report in at most three lines: repo, folder, config written.

## Home

Show, in this order:

```
HQ: <owner>/<hq repo>  (<folder>)

Connected repos:
- owner/a
- owner/b
(or: none yet. Run /hq add <repo>.)

/brief                where every connected repo stands
/eod                  wrap up the day into an EOD compilation
/jot <text>           save a jot for this repo
/hq add|remove <repo> connect or drop a repo
```

## Add

1. Turn the argument into `owner/name`:
   - `owner/name`: use it as is.
   - GitHub URL (`https://github.com/owner/name/...`, `git@github.com:owner/name.git`): take owner and name, drop `.git`.
   - local folder: read `git -C <folder> remote get-url origin`, then parse it as a URL.
   - nothing: do the same for the current folder.
   If it can't be turned into `owner/name`, say why and stop.
2. Run `gh repo view <owner/name> --json nameWithOwner,hasIssuesEnabled`.
   - Fails: say "`<owner/name>` doesn't exist or you can't see it." Stop.
   - `hasIssuesEnabled` is false: say "`<owner/name>` has Issues turned off. Brief reads issues, so turn them on first." Stop.
   - Otherwise use the returned `nameWithOwner` from here on.
3. If `repos.txt` already lists it (ignore case), say "Already connected." and stop.
4. Append it to `repos.txt`. Commit ("Connect <owner/name>") and push (sync rule). Say "Connected `<owner/name>`."

`repos.txt` is untouched on every stop above.

## Remove

1. Turn the argument into `owner/name` as in **Add** step 1. No GitHub check.
2. If `repos.txt` doesn't list it (ignore case), say "Not connected." and stop.
3. Delete that line. Commit ("Disconnect <owner/name>") and push (sync rule).
4. Say "Removed `<owner/name>`. Past EOD compilations are kept." Leave `eod/`, `jots/` and `human/` as they are.
