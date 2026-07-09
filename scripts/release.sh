#!/bin/sh
set -e

git add -A

if ! git diff --cached --quiet; then
  git commit -m "${RELEASE_COMMIT_MESSAGE:-Update package}"
fi

yarn test
yarn publish --patch
git push
git push --tags
