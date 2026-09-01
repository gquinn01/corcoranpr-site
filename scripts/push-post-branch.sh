#!/usr/bin/env bash
#
# Pushes a blog post branch, and refuses to push anything else.
#
# WHY THIS EXISTS. The Content Writer agent needs to push exactly one
# kind of branch and nothing else. That restriction used to live in the
# workflow's tool allowlist as:
#
#     Bash(git push -u origin post/:*)
#
# which reads as "any push to a ref starting post/". It is not. Claude
# Code on the runner matches an allowlist entry token by token, so that
# pattern requires the fifth token to be exactly "post/", and a real
# branch name never is. On 2026-09-01 the agent wrote a complete post,
# passed both gates, committed it, and then could not push: two refusals
# of "This command requires approval", and the run ended with a
# content-blocked issue instead of a pull request.
#
# A permission pattern is a fragile place to keep a rule. This is the
# same rule as code, which can be read and tested. The allowlist entry
# is now a whole-token command, `bash scripts/push-post-branch.sh`, and
# the policy lives here.
#
# Branch protection on main is still the second lock and stays. This is
# the first: the agent never holds a general `git push`.
#
# Usage:  bash scripts/push-post-branch.sh post/<slug>

set -euo pipefail

BRANCH="${1:-}"

if [ -z "$BRANCH" ]; then
  echo "usage: bash scripts/push-post-branch.sh post/<slug>" >&2
  exit 2
fi

# Only post/ branches. Not main, not a tag, not a ref with a path trick
# in it. `case` is a literal glob match, not a regex, so post/../main
# would fail the checkout test below even if it got this far.
case "$BRANCH" in
  post/?*) ;;
  *)
    echo "refused: '$BRANCH' is not a post/ branch. This script pushes nothing else." >&2
    exit 3
    ;;
esac

# And it must be the branch actually checked out, so this cannot be used
# to push some other ref that happens to be named correctly.
CURRENT="$(git rev-parse --abbrev-ref HEAD)"
if [ "$CURRENT" != "$BRANCH" ]; then
  echo "refused: HEAD is on '$CURRENT', not '$BRANCH'. Check out the branch you mean to push." >&2
  exit 4
fi

echo "pushing $BRANCH"
exec git push -u origin "$BRANCH"
