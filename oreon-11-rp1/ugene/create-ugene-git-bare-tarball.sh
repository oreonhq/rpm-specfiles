#!/bin/bash

set -x
set -e

REPONAME=ugene
GITURL=https://github.com/ugeneunipro/${REPONAME}.git

DATE=$(date '+%Y%m%d')
TIME=$(date '+%H%M')

TARNAME=${REPONAME}-free-${DATE}T${TIME}.tar.gz

PWDDIR=$(pwd)
TMPDIR=$(mktemp -d $(pwd)/tmp-${REPONAME}-XXXXXX)
pushd $TMPDIR

git clone --depth 30 --no-single-branch --mirror $GITURL

pushd ${REPONAME}.git

git log 2>&1 | head -n 5 > git-log-orig.txt
#grep version README.md

# remove non-free part
for NONFREE in \
	src/plugins_3rdparty/psipred
do
	env FILTER_BRANCH_SQUELCH_WARNING=1 \
		git filter-branch --index-filter "git rm -r --cached --ignore-unmatch $NONFREE" -- --all
done

# And again show git head info
git log 2>&1 | head -n 5
#grep version README.md
echo

# Here again show original git head infob
cat git-log-orig.txt
echo
rm -f git-log-orig.txt

popd

tar czf ${TARNAME} ${REPONAME}.git/

cp -p ${TARNAME} $PWDDIR
popd
rm -rf $TMPDIR
