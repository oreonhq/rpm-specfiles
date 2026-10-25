%global source0_hash 8c5957fb417823768d70e0faefa6f75f497f41289641256e4fdfecd1954fa16c
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libsolv
Version: 0.7.32
Release: 1%{?dist}
Summary: Package dependency solver
License: BSD-3-Clause
URL: https://github.com/openSUSE/libsolv
Source0: https://github.com/openSUSE/libsolv/archive/refs/tags/%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: pkgconf
BuildRequires: rpm-devel
BuildRequires: zlib-ng-compat-devel
BuildRequires: python3
BuildRequires: bzip2-devel
BuildRequires: xz-devel
BuildRequires: libzstd-devel
BuildRequires: libxml2-devel
BuildRequires: patchelf
%endif

%description
libsolv is a package dependency solver.

%package devel
Summary: Package dependency solver
Requires: libsolv%{?_isa} = %{version}-%{release}

%description devel
libsolv is a package dependency solver.

%prep
%oreon_sha256
%autosetup -p1

%build
%oreon_cmake \
  -DCMAKE_SKIP_RPATH=ON \
  -DFEDORA=1 \
  -DENABLE_STATIC=OFF \
  -DENABLE_RPMDB=ON \
  -DENABLE_RPMMD=ON \
  -DENABLE_RPMPKG=ON \
  -DENABLE_RPMPKG_LIBRPM=ON \
  -DENABLE_RPMDB_LIBRPM=ON \
  -DENABLE_COMPS=ON \
  -DENABLE_LZMA_COMPRESSION=ON \
  -DENABLE_BZIP2_COMPRESSION=ON \
  -DENABLE_ZSTD_COMPRESSION=ON \
  -DENABLE_ZCHUNK_COMPRESSION=OFF \
  -DWITH_LIBXML2=ON
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
%license LICENSE.BSD

%files devel -f %{_builddir}/%{name}-devel.files
