#!/bin/sh

requireCommand() {
  pkg="$2"
  [ -z "$pkg" ] && pkg="$1"
  cmd=$(command -v $1)
  if [ ! -x "$cmd" ]; then
    echo "$1 not found, install the $2 package"
    exit 1
  fi
}

requireCommand swift swift-lang
requireCommand jq
requireCommand awk

set -eu

version="$(awk '/Version:/ { print $2 }' swiftlint.spec)"
base="SwiftLint-${version}"
cache="${base}-bundled-deps.tar.gz"

if [ -e "$cache" ]; then
  echo "$cache already exists, aborting"
  exit 1
fi

srcdir="$PWD"
workdir="$(mktemp -d)"

tar xzf "${srcdir}/${base}.tar.gz" -C "$workdir"
(cd "${workdir}/${base}" && \
  swift package resolve && \
  rm -r .build/artifacts)
(cd "${workdir}" && tar czf "${srcdir}/${cache}" "${base}/.build/")

jq -r '.pins[] | [.identity, .state.version] | @tsv' \
  < "${workdir}/${base}/Package.resolved" \
  | awk '{print "Provides:       bundled(" $1 ") = " $2}' \
  > "${srcdir}/${base}-bundled-provides.txt"

exit 0
