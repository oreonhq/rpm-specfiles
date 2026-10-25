%global source0_hash 931b44eabdd5f7d170803f3476397c8e9dea07209589e1194ff8379429991ccb
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libmodulemd
Version: 2.15.3
Release: 1%{?dist}
Summary: Module metadata library
License: MIT
URL: https://github.com/fedora-modularity/libmodulemd
Source0: https://github.com/fedora-modularity/libmodulemd/releases/download/%{version}/modulemd-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: pkgconf
BuildRequires: glib2-devel
BuildRequires: libyaml-devel
BuildRequires: rpm-devel
BuildRequires: gobject-introspection-devel
BuildRequires: python3-devel
BuildRequires: python3-gobject-devel
BuildRequires: gtk-doc
BuildRequires: glib2-doc
BuildRequires: patchelf
%endif

%description
libmodulemd reads modulemd documents.

%package devel
Summary: Module metadata library
Requires: libmodulemd%{?_isa} = %{version}-%{release}

%description devel
libmodulemd reads modulemd documents.

%prep
%oreon_sha256
%autosetup -n modulemd-%{version} -p1

%build
%oreon_meson \
  -Dwith_py3=true \
  -Dwith_py2=false \
  -Dskip_introspection=false \
  -Dwith_manpages=enabled \
  -Drpmio=enabled
%oreon_meson_build

%install
%oreon_meson_install
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
