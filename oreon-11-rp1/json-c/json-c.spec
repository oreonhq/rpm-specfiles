%global source0_hash 876ab046479166b869afc6896d288183bbc0e5843f141200c677b3e8dfb11724
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: json-c
Version: 0.18
Release: 1%{?dist}
Summary: JSON parser library
License: MIT
URL: https://github.com/json-c/json-c
Source0: https://s3.amazonaws.com/json-c_releases/releases/json-c-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: python3
BuildRequires: patchelf
%endif

%description
json-c is a JSON parser library.

%package devel
Summary: JSON parser library
Requires: json-c%{?_isa} = %{version}-%{release}

%description devel
json-c is a JSON parser library.

%prep
%oreon_sha256
%autosetup -p1

%build
%oreon_cmake \
  -DCMAKE_SKIP_RPATH=ON \
  -DBUILD_STATIC_LIBS=OFF \
  -DBUILD_TESTING=OFF \
  -DDISABLE_WERROR=ON
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
