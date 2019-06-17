#!/bin/sh
echo Following diff must be empty:
./mergechangelogs.py test/Changelog_{1,2,3}.md > test/Changelog_test.md
diff test/Changelog_expect.md test/Changelog_test.md

