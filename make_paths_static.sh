#!/usr/bin/env bash
# Make paths static
#
# See notes in deploy.md doc.
set -e

OLD_PATH='#/'
NEW_PATH='/'

OLD_ID='?id='
NEW_ID='#'

DOCSIFY_TAG='<script src="//unpkg.com/docsify/lib/docsify.min.js"></script>'
SEARCH_TAG='<script src="//cdn.jsdelivr.net/npm/docsify/lib/plugins/search.min.js"></script>'

REPLACE="s|${OLD_PATH}|${NEW_PATH}|g
s|${OLD_ID}|${NEW_ID}|g
s|${DOCSIFY_TAG}|<!-- ${DOCSIFY_TAG} -->|g
s|${SEARCH_TAG}|<!-- ${SEARCH_TAG} -->|g"

# Add blank value as backup parameter if macOS otherwise leave out string completely.
# This assumes the gnu sed is not installed on macOS. Substituting didn't work so just to it
# literally. Also the find command could not be made DRY.

if [[ $OSTYPE == "darwin"* ]]; then
  echo 'Mac'
  sed -i '' "$REPLACE" $(find build -type f)
else
  echo 'Not a Mac'
  sed -i "$REPLACE" $(find build -type f)
fi
