%global source0_hash ed4f80c4106a8abaab09e4094ed8d712dedd376699815bc4957c5cf690cdc53d
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libcomps
Version: 0.1.22
Release: 1%{?dist}
Summary: Comps XML library
License: GPL-2.0-or-later
URL: https://github.com/rpm-software-management/libcomps
Source0: https://github.com/rpm-software-management/libcomps/archive/refs/tags/%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: pkgconf
BuildRequires: expat-devel
BuildRequires: libxml2-devel
BuildRequires: zlib-devel
BuildRequires: python3-devel
BuildRequires: patchelf
%endif

Provides: python3-libcomps = %{version}-%{release}

%description
libcomps reads and writes comps XML.

%package devel
Summary: Comps XML library
Requires: libcomps%{?_isa} = %{version}-%{release}

%description devel
libcomps reads and writes comps XML.

%prep
%oreon_sha256
%autosetup -p1

%build
cd libcomps
%oreon_cmake \
  -DCMAKE_SKIP_RPATH=ON \
  -DENABLE_TESTS=OFF \
  -DENABLE_DOCS=OFF \
  -DBUILD_LIBCOMPS_SHARED=ON
%oreon_cmake_build

%install
cd libcomps
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
