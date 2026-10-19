%global source0_hash 799397b10d087d0147d6af117a5a473120f1369f0a3a3d68bf953abc0b749b75
Name:           advancecomp
Version:        2.6
Release:        1%{?dist}
Summary:        Recompression utilities for .png, .mng, .zip and .gz files
License:        GPL-3.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
SourceLicense:  %{license} AND Apache-2.0 AND MIT
URL:            https://www.advancemame.it/
%global forgeurl https://github.com/amadvance/advancecomp
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       libdeflate >= 1.19
Provides:      bundled(7zip)
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dos2unix
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(libdeflate)
BuildRequires:  zlib-devel
BuildRequires:  zopfli-devel
# /oreon:deps
%description
AdvanceCOMP contains recompression utilities for your .zip archives,
.png images, .mng video clips and .gz files.

The official site of AdvanceCOMP is:

  https://www.advancemame.it

This package contains:
  advzip - Recompression and test utility for zip files
  advpng - Recompression utility for png files
  advmng - Recompression utility for mng files
  advdef - Recompression utility for deflate streams in .png, .mng and .gz files

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

dos2unix --keepdate doc/*.txt

# Patch out bundled libdeflate
rm --recursive --verbose libdeflate
sed --regexp-extended --in-place '/libdeflate[\/_]/d' Makefile.am
# Fix up #include paths. The find-then-modify pattern keeps us from discarding
# mtimes on any sources that do not need modification.
find . -type f -exec gawk \
    '/^[[:blank:]]*#include.*libdeflate/ { print FILENAME; nextfile }' \
    '{}' '+' |
  xargs --no-run-if-empty --verbose sed --regexp-extended --in-place \
      's@^([[:blank:]]*#include.*)libdeflate/@\1@'

# Patch out bundled zopfli
rm --recursive --verbose zopfli
sed --regexp-extended --in-place \
    --expression '/zopfli[\/_]/d' \
    --expression 's/((\(7z_SOURCES\)|WindowOut\.h).*)[[:blank:]]*\\/\1/' \
    Makefile.am
# Fix up #include paths. The find-then-modify pattern keeps us from discarding
# mtimes on any sources that do not need modification.
find . -type f -exec gawk \
    '/^[[:blank:]]*#include.*zopfli/ { print FILENAME; nextfile }' \
    '{}' '+' |
  xargs --no-run-if-empty -t sed --regexp-extended --in-place \
      --expression 's@^([[:blank:]]*#include.*)zopfli/@\1@'

%conf
autoreconf --force --install --verbose

# Link against system libdeflate
export CFLAGS="$(pkgconf --cflags libdeflate) ${CFLAGS-}"
export CXXFLAGS="$(pkgconf --cflags libdeflate) ${CXXFLAGS-}"
export LDFLAGS="$(pkgconf --libs libdeflate) ${LDFLAGS-}"

# Link against system zopfli
export LDFLAGS="-lzopfli ${LDFLAGS-}"

%configure

%build

%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog

