%global source0_hash 0a06cc9656b10518c50f230ec8f7cf0218530823f6b2f28bf164899f8d569622
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libdnf
Version: 0.75.0
Release: 1%{?dist}
Summary: DNF library
License: LGPL-2.1-or-later
URL: https://github.com/rpm-software-management/libdnf
Source0: https://github.com/rpm-software-management/libdnf/archive/refs/tags/%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: pkgconf
BuildRequires: glib2-devel
BuildRequires: json-c-devel
BuildRequires: libmodulemd-devel
BuildRequires: librepo-devel
BuildRequires: libsolv-devel
BuildRequires: rpm-devel
BuildRequires: sqlite-devel
BuildRequires: libsmartcols-devel
BuildRequires: swig
BuildRequires: python3-devel
BuildRequires: patchelf
%endif

Provides: python3-libdnf = %{version}-%{release}
Provides: python3-hawkey = %{version}-%{release}

%description
libdnf is the library behind dnf 4.

%package devel
Summary: DNF library
Requires: libdnf%{?_isa} = %{version}-%{release}

%description devel
libdnf is the library behind dnf 4.

%prep
%oreon_sha256
%autosetup -p1

%build
%oreon_cmake \
  -DCMAKE_SKIP_RPATH=ON \
  -DWITH_ZCHUNK=OFF \
  -DWITH_GTKDOC=OFF \
  -DWITH_HTML=OFF \
  -DWITH_MAN=OFF \
  -DWITH_TESTS=OFF \
  -DWITH_BINDINGS=ON \
  -DENABLE_DNF5_CONF_DROP_IN=OFF \
  -DENABLE_DNF5_CONF_REPOS_OVERRIDE=OFF
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
