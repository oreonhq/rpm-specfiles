#!/bin/bash

set -ex

SNAPSHOT_BUILD=${SNAPSHOT_BUILD:-0}

tmpdir=`mktemp -d`
currentdir=`pwd`
version="$1"

if [ -n "$version" ]; then
  gpghome=`mktemp -d`
  original_sources="test-suite-$version.src.tar.xz"
  download_url="https://github.com/llvm/llvm-project/releases/download/llvmorg-$version/$original_sources"
  curl -O -L $download_url
  curl -O -L $download_url.sig
  gpg --homedir=$gpghome --yes --output=keyring.gpg --dearmor release-keys.asc
  gpg --verify --homedir=$gpghome --keyring=./keyring.gpg $original_sources.sig $original_sources
  rm -Rf $gpghome
else
  if [[ "${SNAPSHOT_BUILD}" == "1" ]]; then
    spectool \
      --define 'original_sources 1' \
      --define "_sourcedir ${PWD}" \
      --define "with_snapshot_build 1" \
      -g \
      -C . \
      llvm-test-suite.spec \
      | tee dl.log
  else
    spectool \
      --define 'original_sources 1' \
      -g \
      -C . \
      llvm-test-suite.spec \
      | tee dl.log
  fi
  original_sources=`head -1 dl.log | sed 's/.*\///'`
  rm dl.log
fi


tar -C $tmpdir -xvf $original_sources > $tmpdir/tar_output
test_suite_src=`head -1 $tmpdir/tar_output | sed -e 's/\/.*//'`
pushd $tmpdir
test -d $test_suite_src


UNKNOWN="\
	MultiSource/Benchmarks/mediabench/ \
	MultiSource/Applications/JM/"

#MallocBench/{espresso,cfrac} might be OK
BAD="\
	MultiSource/Benchmarks/MallocBench/ \
	MultiSource/Benchmarks/7zip/"

POSSIBLY_BAD="\
	MultiSource/Benchmarks/Olden/ \
	MultiSource/Benchmarks/Fhourstones/ \
	MultiSource/Benchmarks/ASCI_Purple/SMG2000/ \
	MultiSource/Benchmarks/Fhourstones-3.1/ \
	MultiSource/Benchmarks/McCat/ \
	MultiSource/Applications/spiff/ \
	MultiSource/Applications/Burg/ \
	MultiSource/Benchmarks/MiBench/telecomm-FFT/"

VIRUSES="\
	MultiSource/Applications/ClamAV/"

#siod: llvm.org/PR38648
BUGGY="\
	MultiSource/Applications/siod"

for f in $UNKNOWN $BAD $POSSIBLY_BAD $BUGGY $VIRUSES; do
	test -d $test_suite_src/$f
	rm -Rf $test_suite_src/$f
	basedir=`dirname $f`
	dir=`basename $f`
	cmake_file=$test_suite_src/$basedir/CMakeLists.txt
	test -f $cmake_file
	sed -i s/add_subdirectory\($dir\)//g $cmake_file
done

# The llvm-test-suite now contains broken symlinks because
# the link target was removed above, e.g.
#
#   /usr/share/llvm-test-suite/CTMark/7zip -> ../MultiSource/Benchmarks/7zip
#   /usr/share/llvm-test-suite/CTMark/lencod -> ../MultiSource/Applications/JM/lencod
#
# To fix these algorithmically, we have to find all broken
# symlinks and remove the add_subdirectory entry in the
# CMakeLists.txt in their parent directory.
broken_symlinks=$(find $test_suite_src -type l ! -exec test -e {} \; -print)
for f in $broken_symlinks; do
	test -L $f
	rm -fv $f
	basedir=`dirname $f`
	dir=`basename $f`
	cmake_file=$basedir/CMakeLists.txt
	test -f $cmake_file
	sed -i s/add_subdirectory\($dir\)//g $cmake_file
done

tar --transform=s/$test_suite_src/$test_suite_src.fedora/ --show-transformed-names -cJf $currentdir/$test_suite_src.fedora.tar.xz $test_suite_src
popd
rm -Rf $tmpdir
