#!/bin/sh

# Usage: ./mono-reflection-make-git-snapshot.sh [COMMIT] [DATE]
#
# to make a snapshot of the given tag/branch.  Defaults to HEAD.
# Point env var REF to a local banshee repo to reduce clone time.

if [ -z $2 ]; then
  DATE=`date +%Y%m%d`
else
  DATE=$2
fi

export DIRNAME="mono-reflection-${DATE}"

echo REF ${REF:+--reference $REF}
echo DIRNAME ${DIRNAME}
echo HEAD ${1:-HEAD}

rm -rf ${DIRNAME}

git clone ${REF:+--reference $REF} \
        https://github.com/jbevain/mono.reflection.git ${DIRNAME}

GITREV=`GIT_DIR=$DIRNAME/.git git rev-parse HEAD| cut -c1-6`

FILENAME=${DIRNAME}git${GITREV}

GIT_DIR=${DIRNAME}/.git git archive --format=tar --prefix=${DIRNAME}/ ${1:-HEAD} \
        | bzip2 > ${FILENAME}.tar.bz2

rm -rf ${DIRNAME}

echo Generated ${FILENAME}.tar.bz2

