%global source0_hash 66a4998e020d7354a804fde83801a9d7157b20f5e08198f7fde69d3a0ab683fe
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: rpm
Version: 6.0.2
Release: 1%{?dist}
Summary: RPM package manager
License: GPL-2.0-or-later
URL: https://rpm.org/
Source0: https://github.com/rpm-software-management/rpm/releases/download/rpm-%{version}-release/rpm-%{version}.tar.bz2

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: pkgconf
BuildRequires: lua-devel
BuildRequires: zlib-ng-compat-devel
BuildRequires: bzip2-devel
BuildRequires: xz-devel
BuildRequires: libzstd-devel
BuildRequires: popt-devel
BuildRequires: readline-devel
BuildRequires: libarchive-devel
BuildRequires: file-devel
BuildRequires: sqlite-devel
BuildRequires: python3-devel
BuildRequires: libcap-devel
BuildRequires: libacl-devel
BuildRequires: libselinux-devel
BuildRequires: elfutils-libelf-devel
BuildRequires: elfutils-devel
BuildRequires: audit-libs-devel
BuildRequires: dbus-devel
BuildRequires: rpm-sequoia-devel
BuildRequires: gawk
BuildRequires: gettext
BuildRequires: fsverity-utils-devel
BuildRequires: ima-evm-utils-devel
BuildRequires: doxygen
BuildRequires: scdoc
BuildRequires: patchelf
%endif

Provides: python3-rpm = %{version}-%{release}

%description
RPM package manager libraries and tools.

%package devel
Summary: RPM package manager
Requires: rpm%{?_isa} = %{version}-%{release}

%description devel
RPM package manager libraries and tools.

%prep
%oreon_sha256
%autosetup -p1

%build
%oreon_cmake \
  -DCMAKE_SKIP_RPATH=ON \
  -DENABLE_TESTSUITE=OFF \
  -DENABLE_NLS=ON \
  -DENABLE_OPENMP=ON \
  -DENABLE_PYTHON=ON \
  -DWITH_SEQUOIA=ON \
  -DWITH_OPENSSL=OFF \
  -DWITH_LIBELF=ON \
  -DWITH_LIBDW=ON \
  -DWITH_AUDIT=ON \
  -DWITH_FSVERITY=ON \
  -DWITH_FAPOLICYD=ON \
  -DWITH_IMAEVM=ON \
  -DWITH_DOXYGEN=ON \
  -DWITH_CAP=ON \
  -DWITH_ACL=ON \
  -DWITH_SELINUX=ON \
  -DWITH_DBUS=ON \
  -DWITH_READLINE=ON \
  -DWITH_BZIP2=ON \
  -DWITH_ZSTD=ON \
  -DWITH_LIBLZMA=ON \
  -DENABLE_SQLITE=ON
%oreon_cmake_build

%install
%oreon_cmake_install
rm -f %{buildroot}%{_libdir}/*.a
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f")
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%oreon_filelist_devel
python3 - %{_builddir}/%{name}.files %{_builddir}/%{name}-devel.files << 'PY'
import os
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
def with_pyc(lines):
    extra = []
    seen = set(lines)
    for line in lines:
        path = line.split()[-1] if line.startswith("%") else line
        path = path.strip('"')
        if not path.endswith(".py"):
            continue
        if "/lib/python3." not in path and "/lib64/python3." not in path:
            continue
        glob = os.path.dirname(path) + "/__pycache__/*"
        if glob not in seen:
            seen.add(glob)
            extra.append(glob)
    return lines + extra
m = with_pyc(m + move)
keep = with_pyc(keep)
text = "\n".join(m)
main.write_text(text + ("\n" if text else ""))
text = "\n".join(keep)
devel.write_text(text + ("\n" if text else ""))
PY

%files -f %{_builddir}/%{name}.files
%license COPYING

%files devel -f %{_builddir}/%{name}-devel.files
