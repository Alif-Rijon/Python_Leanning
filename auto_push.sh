#!/bin/bash

BRANCH="initial"
MAIN="main"

CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "$BRANCH" ]; then
  git checkout "$BRANCH"
fi 

echo "Adding changes"
git add .

#Get stated files
FILES=$(git diff --cached --name-only)

#If no changes then stop
if [ -z "$FILES" ]; then
  echo "No changes to commit"
  exit 0
fi

#Count files
COUNT=$(echo "$FILES" | wc -l)

#Create commit message
MSG="[$COUNT files] Daily Python Practice: $FILES ($(date +'%d-%m-%Y'))"

echo "Committing"
git commit -m "$MSG"

echo "Pushing $BRANCH"
git push origin "$BRANCH"

echo "Switching to $MAIN"
git checkout "$MAIN"

echo "Pull latest"
git pull origin "$MAIN"

echo "Merging $BRANCH to $MAIN"
git merge "$BRANCH"

#If merge fails
if [ $? -ne 0 ]; then
 echo "Merge conflict! Resolve manually."
 exit 1
fi 
echo "Pushing $MAIN"
git push origin "$MAIN"

echo "Done"
