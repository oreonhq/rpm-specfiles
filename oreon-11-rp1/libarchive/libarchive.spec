%global source0_hash 19f917d42d530f98815ac824d90c7eaf648e9d9a50e4f309c812457ffa5496b5
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libarchive
Version: 3.8.1
Release: 1%{?dist}
Summary: Archive reading library
License: BSD-2-Clause
URL: https://www.libarchive.org/
Source0: https://github.com/libarchive/libarchive/releases/download/v%{version}/libarchive-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: pkgconf
BuildRequires: zlib-devel
BuildRequires: bzip2-devel
BuildRequires: xz-devel
BuildRequires: libzstd-devel
BuildRequires: lz4-devel
BuildRequires: openssl-devel
BuildRequires: libxml2-devel
BuildRequires: libattr-devel
BuildRequires: libacl-devel
BuildRequires: patchelf
%endif

%description
libarchive reads and writes archive formats.

%package devel
Summary: Archive reading library
Requires: libarchive%{?_isa} = %{version}-%{release}

%description devel
libarchive reads and writes archive formats.

%prep
%oreon_sha256
%autosetup -p1

%build
%oreon_cmake \
  -DCMAKE_SKIP_RPATH=ON \
  -DENABLE_TEST=OFF \
  -DENABLE_WERROR=OFF \
  -DENABLE_LIBB2=OFF \
  -DENABLE_LZO=OFF \
  -DENABLE_PCREPOSIX=OFF \
  -DENABLE_PCRE2POSIX=OFF \
  -DENABLE_EXPAT=OFF \
  -DENABLE_OPENSSL=ON \
  -DENABLE_LIBXML2=ON \
  -DENABLE_ZLIB=ON \
  -DENABLE_BZip2=ON \
  -DENABLE_LZMA=ON \
  -DENABLE_ZSTD=ON \
  -DENABLE_LZ4=ON \
  -DENABLE_ACL=ON \
  -DENABLE_XATTR=ON
%oreon_cmake_build

%install
%oreon_cmake_install
rm -f %{buildroot}%{_libdir}/*.a
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f")
  if [ -n "$r" ]; then
    patchelf --remove-rpath "$f"
  fi
done
%oreon_filelist_devel
python3 - %{_builddir}/%{name}.files %{_builddir}/%{name}-devel.files << 'PY'
import sys
from pathlib import Path
main, devel = Path(sys.argv[1]), Path(sys.argv[2])
m = main.read_text().splitlines()
d = devel.read_text().splitlines()
keep, move = [], []
for line in d:
    path = line.split()[-1] if line.startswith("%") else line
    if path.endswith(".so") and path.count("/") > 3:
        move.append(line)
    else:
        keep.append(line)
text = "\n".join(m + move)
main.write_text(text + ("\n" if text else ""))
text = "\n".join(keep)
devel.write_text(text + ("\n" if text else ""))
PY

%files -f %{_builddir}/%{name}.files
%license COPYING

%files devel -f %{_builddir}/%{name}-devel.files
