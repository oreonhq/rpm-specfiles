#!/bin/bash

tag=$(sed -n 's/^Version:\s\(.*\)$/\1/p' ./*.spec | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')
url=$(sed -n 's/^URL:\s\(.*\)$/\1/p' ./*.spec | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')
pkgdir=$(basename $url | sed -s 's/\.git$//')

echo "tag: $tag"
echo "URL: $url"
echo "pkgdir: $pkgdir"

set -e

tmp=$(mktemp -d)

trap cleanup EXIT
cleanup() {
    echo Cleaning up...
    set +e
    [ -z "$tmp" -o ! -d "$tmp" ] || rm -rf "$tmp"
}

unset CDPATH
pwd=$(pwd)

pushd "$tmp"
git clone $url
cd $pkgdir
echo Finding git tag
gittag=$(git show-ref --tags | cut -d' ' -f2 | grep "${tag}$" || git show-ref --tags | cut -d' ' -f2 | sort -Vr | head -n1)
if [ -z $gittag ]; then
	gittag=tags/$tag
fi
echo "Git Tag: $gittag"
if [ -d "test" ]; then
  git archive --prefix='test/' --format=tar ${gittag}:test/ \
      | bzip2 > "$pwd"/tests-${tag}.tar.bz2
elif [ -d "tests" ]; then
  git archive --prefix='tests/' --format=tar ${gittag}:tests/ \
      | bzip2 > "$pwd"/tests-${tag}.tar.bz2
elif [ -d "spec" ]; then
  git archive --prefix='spec/' --format=tar ${gittag}:spec/ \
      | bzip2 > "$pwd"/tests-${tag}.tar.bz2
else
  echo "No test directory found for tag ${gittag}"
fi
if [ -d "support" ]; then
  git archive --prefix='support/' --format=tar ${gittag}:support/ \
      | bzip2 > "$pwd"/support-${tag}.tar.bz2
fi
if [ -d "fixture" ]; then
  git archive --prefix='fixture/' --format=tar ${gittag}:fixture/ \
      | bzip2 > "$pwd"/fixture-${tag}.tar.bz2
fi
if [ -d "examples" ]; then
  git archive --prefix='examples/' --format=tar ${gittag}:examples/ \
      | bzip2 > "$pwd"/examples-${tag}.tar.bz2
elif [ -d "example" ]; then
  git archive --prefix='example/' --format=tar ${gittag}:example/ \
      | bzip2 > "$pwd"/examples-${tag}.tar.bz2
fi
if [ -d "tasks" ]; then
  git archive --prefix='tasks/' --format=tar ${gittag}:tasks/ \
      | bzip2 > "$pwd"/tasks-${tag}.tar.bz2
fi
if [ -d "docs" ]; then
  git archive --prefix='docs/' --format=tar ${gittag}:docs/ \
      | bzip2 > "$pwd"/docs-${tag}.tar.bz2
elif [ -d "doc" ]; then
  git archive --prefix='doc/' --format=tar ${gittag}:doc/ \
      | bzip2 > "$pwd"/docs-${tag}.tar.bz2
fi
if [ -d "src" ]; then
  git archive --prefix='src/' --format=tar ${gittag}:src/ \
      | bzip2 > "$pwd"/src-${tag}.tar.bz2
elif [ -d "source" ]; then
  git archive --prefix='source/' --format=tar ${gittag}:source/ \
      | bzip2 > "$pwd"/source-${tag}.tar.bz2
fi
if [ -d "tools" ]; then
  git archive --prefix='tools/' --format=tar ${gittag}:tools/ \
      | bzip2 > "$pwd"/tools-${tag}.tar.bz2
fi
if [ -d "scripts" ]; then
  git archive --prefix='scripts/' --format=tar ${gittag}:scripts/ \
      | bzip2 > "$pwd"/scripts-${tag}.tar.bz2
fi
if [ -d "modules" ]; then
  git archive --prefix='modules/' --format=tar ${gittag}:modules/ \
      | bzip2 > "$pwd"/modules-${tag}.tar.bz2
fi
if [ -d "ts" ]; then
  git archive --prefix='ts/' --format=tar ${gittag}:ts/ \
      | bzip2 > "$pwd"/ts-${tag}.tar.bz2
fi
if [ -d "build" ]; then
  git archive --prefix='build/' --format=tar ${gittag}:build/ \
      | bzip2 > "$pwd"/build-${tag}.tar.bz2
fi
if [ -d "fixtures" ]; then
  git archive --prefix='fixtures/' --format=tar ${gittag}:fixtures/ \
      | bzip2 > "$pwd"/fixtures-${tag}.tar.bz2
fi
if [ -d "mocks" ]; then
  git archive --prefix='mocks/' --format=tar ${gittag}:mocks/ \
      | bzip2 > "$pwd"/mocks-${tag}.tar.bz2
fi
if [ -d "typings" ]; then
  git archive --prefix='typings/' --format=tar ${gittag}:typings/ \
      | bzip2 > "$pwd"/typings-${tag}.tar.bz2
fi
if [ -d "templates" ]; then
  git archive --prefix='templates/' --format=tar ${gittag}:templates/ \
      | bzip2 > "$pwd"/templates-${tag}.tar.bz2
fi
if [ -d "benchmark" ]; then
  git archive --prefix='benchmark/' --format=tar ${gittag}:benchmark/ \
      | bzip2 > "$pwd"/benchmark-${tag}.tar.bz2
fi
if [ -d "vendor" ]; then
  git archive --prefix='vendor/' --format=tar ${gittag}:vendor/ \
      | bzip2 > "$pwd"/vendor-${tag}.tar.bz2
fi
if [ -d "packages" ]; then
  git archive --prefix='packages/' --format=tar ${gittag}:packages/ \
      | bzip2 > "$pwd"/packages-${tag}.tar.bz2
fi
popd
