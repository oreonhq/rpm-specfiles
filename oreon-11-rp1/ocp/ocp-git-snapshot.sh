#!/bin/sh
# Since this project uses git submodules and Github's auto-archive
# feature doesn't archive the submodules, you need to create a git
# snapshot tarball manually with this ocp-git-snapshot.sh script.

if [ -e ocp ]; then
    echo "Not overwriting existing file: "
    ls -ld ocp
    exit 1
fi

set -x
git clone --recurse-submodules https://github.com/mywave82/opencubicplayer ocp
head=`git -C ocp rev-parse HEAD`
headdate=`git -C ocp log -1 --format=%cd --date='format:%Y%m%d'`
set +x

if [ -e ocp-${head} -o -e ocp-${head}.tar.bz2 ]; then
    echo "Not overwriting existing files: "
    ls -ld ocp-${head} ocp-${head}.tar.bz2
    exit 1
fi

set -x
mv ocp ocp-${head}
tar cjf ocp-${head}.tar.bz2 --exclude='.git*' ocp-${head}
rm -rf ocp-${head}
set +x

echo ""
echo "Define these globals at the top of the spec file:"
echo ""
echo "%global commit ${head}"
echo "%global commitdate ${headdate}"
