%global source0_hash c008bac08fd5c7b4a87f7b8a71f283fa581d80d80ff8d2efd3b26224c39bc54c
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libxml2
Version: 2.15.1
Release: 1%{?dist}
Summary: XML parser library
License: MIT
URL: https://gitlab.gnome.org/GNOME/libxml2
Source0: https://download.gnome.org/sources/libxml2/2.15/libxml2-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: pkgconf
BuildRequires: zlib-ng-compat-devel
BuildRequires: python3
BuildRequires: patchelf
%endif

%description
libxml2 is an XML parser library.

%package devel
Summary: XML parser library
Requires: libxml2%{?_isa} = %{version}-%{release}

%description devel
libxml2 is an XML parser library.

%prep
%oreon_sha256
%autosetup -p1

%build
%oreon_configure --disable-static --without-python --with-zlib
%oreon_make

%install
%oreon_make_install
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
%license Copyright

%files devel -f %{_builddir}/%{name}-devel.files
