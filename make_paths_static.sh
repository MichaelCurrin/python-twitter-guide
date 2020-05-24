#!/usr/bin/env bash
# Make paths static
#
# See notes in deploy.md doc.
set -e

# Add
SEARCH_CONSOLE_VERIFICATION_TAG='<meta name="google-site-verification" content="9s-_R9brAtc1L8SUnsVIxgCB5WQQLGTMYciVr5zh8TA" />'

# Remove
DOCSIFY_TAG='<script src="//unpkg.com/docsify/lib/docsify.min.js"></script>'
SEARCH_TAG='<script src="//cdn.jsdelivr.net/npm/docsify/lib/plugins/search.min.js"></script>'

# Replace

OLD_PATH='#/'
NEW_PATH='/'

OLD_ID='?id='
NEW_ID='#'

# Hide the search bar it's inactive for non-JS prerendered solution.
# Warning: This only works because there is only ONE occurrence of flex.
# And multi-line solution targeting '.search .input-wrap' is too much effort.
OLD_SEARCH_CSS='display: flex;'
NEW_SEARCH_CSS='display: none;'

# This no longer works with JS disabled.
IMPROVE='Improve this page'

REPLACE="s|${OLD_PATH}|${NEW_PATH}|g
s|${OLD_ID}|${NEW_ID}|g
s|${OLD_SEARCH_CSS}|${NEW_SEARCH_CSS}|g
s|${DOCSIFY_TAG}|<!-- ${DOCSIFY_TAG} -->|g
s|${SEARCH_TAG}|<!-- ${SEARCH_TAG} -->|g
s|${IMPROVE}||g
s|</head>|${SEARCH_CONSOLE_VERIFICATION_TAG}</head>|g
"

# Add blank value as backup parameter if macOS otherwise leave out string completely.
# This assumes the gnu sed is not installed on macOS. Substituting didn't work so just to it
# literally. Also the find command could not be made DRY.

echo 'Making build files into static app'

if [[ $OSTYPE == "darwin"* ]]; then
  echo 'Using Mac sed'
  sed -i '' "$REPLACE" $(find build -type f)
else
  echo 'Using non-Mac sed'
  sed -i "$REPLACE" $(find build -type f)
fi
