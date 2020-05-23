#!/usr/bin/env bash
# Make paths static
set -e

BEFORE='#\/'
AFTER='\/'
PATTERN="s/${BEFORE}/${AFTER}/g; s/?id=/#/g"

# Add blank value as backup parameter if macOS otherwise leave out string completely.
# This assumes the gnu sed is not installed on macOS. Substituting didn't work so just to it
# literally. Also the find command could not be made DRY.

if [[ $OSTYPE == "darwin"* ]]; then
  echo 'Mac'
  sed -i '' "$PATTERN" $(find build -type f)
else
  echo 'Not a Mac'
  sed "$PATTERN" $(find build -type f)
fi
