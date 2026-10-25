%global source0_hash 7395b34af0d7a3fa13d2db1ad0ca0d8cbcae6695c2ecd62c6204606184bfd92b
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: librepo
Version: 1.19.0
Release: 1%{?dist}
Summary: Repodata download library
License: LGPL-2.1-or-later
URL: https://github.com/rpm-software-management/librepo
Source0: https://github.com/rpm-software-management/librepo/archive/refs/tags/%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: pkgconf
BuildRequires: glib2-devel
BuildRequires: openssl-devel
BuildRequires: libxml2-devel
BuildRequires: libcurl-devel
BuildRequires: gpgme-devel
BuildRequires: libselinux-devel
BuildRequires: zchunk-devel
BuildRequires: python3-devel
BuildRequires: patchelf
%endif

Provides: python3-librepo = %{version}-%{release}

%description
librepo downloads repodata and packages.

%package devel
Summary: Repodata download library
Requires: librepo%{?_isa} = %{version}-%{release}

%description devel
librepo downloads repodata and packages.

%prep
%oreon_sha256
%autosetup -p1

%build
%oreon_cmake \
  -DCMAKE_SKIP_RPATH=ON \
  -DENABLE_TESTS=OFF \
  -DENABLE_DOCS=OFF \
  -DENABLE_EXAMPLES=OFF \
  -DWITH_ZCHUNK=ON \
  -DUSE_GPGME=ON \
  -DENABLE_SELINUX=ON \
  -DENABLE_PYTHON=ON
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
%license COPYING

%files devel -f %{_builddir}/%{name}-devel.files
