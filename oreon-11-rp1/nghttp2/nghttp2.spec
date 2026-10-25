%global source0_hash 5511d3128850e01b5b26ec92bf39df15381c767a63441438b25ad6235def902c
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: nghttp2
Version: 1.68.0
Release: 1%{?dist}
Summary: HTTP/2 library
License: MIT
URL: https://nghttp2.org/
Source0: https://github.com/nghttp2/nghttp2/releases/download/v%{version}/nghttp2-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: pkgconf
BuildRequires: python3
BuildRequires: patchelf
%endif

%description
nghttp2 is an HTTP/2 library.

%package devel
Summary: HTTP/2 library
Requires: nghttp2%{?_isa} = %{version}-%{release}

%description devel
nghttp2 is an HTTP/2 library.

%prep
%oreon_sha256
%autosetup -p1

%build
%oreon_configure --disable-static --enable-lib-only
%oreon_make

%install
%oreon_make_install
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
