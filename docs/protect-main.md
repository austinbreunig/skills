# Protect `main`

Every merge to `main` is a release, so `main` is protected. Nothing lands without a PR and a passing `validate` check.

## The ruleset

Name it `protect-main`. It applies to the default branch and has no bypass list.

- Restrict deletions
- Block force pushes
- Require a pull request before merging, with 0 approvals (GitHub won't let you approve your own PR; raise it to 1 when a collaborator joins)
- Require status checks to pass: `validate`

## Steps

1. Settings → Rules → Rulesets → New ruleset → New branch ruleset.
2. Name `protect-main`. Enforcement `Active`.
3. Target branches → Add target → Include default branch.
4. Check Restrict deletions, Block force pushes, and Require a pull request before merging (Required approvals 0).
5. Create.

## Add the status check later

You can only pick the `validate` check after the Action has run once. So:

1. Set up everything above first.
2. Open any PR. The `validate` Action runs on it.
3. Edit `protect-main` → check Require status checks to pass → add `validate` → Save.

After that, every change lands through a PR, docs and glossary edits included.
