%global source0_hash 119d1708ca022556d6d2989ee90ad1b82bd9c0d1667e066944a6d0020e2d5e57
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: glib2
Version: 2.86.1
Release: 1%{?dist}
Summary: GLib library
License: LGPL-2.1-or-later
URL: https://gitlab.gnome.org/GNOME/glib
Source0: https://download.gnome.org/sources/glib/2.86/glib-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: pkgconf
BuildRequires: python3
BuildRequires: libffi-devel
BuildRequires: pcre2-devel
BuildRequires: zlib-ng-compat-devel
BuildRequires: libattr-devel
BuildRequires: libmount-devel
BuildRequires: libselinux-devel
BuildRequires: gobject-introspection-devel
BuildRequires: python3-docutils
BuildRequires: systemtap-sdt-devel
BuildRequires: systemtap-sdt-dtrace
BuildRequires: sysprof-capture-devel
BuildRequires: gettext
BuildRequires: elfutils-libelf-devel
BuildRequires: patchelf
%endif

%description
GLib is the low level core library for GNOME.

%package devel
Summary: GLib library
Requires: glib2%{?_isa} = %{version}-%{release}

%description devel
GLib is the low level core library for GNOME.

%prep
%oreon_sha256
%autosetup -n glib-%{version} -p1

%build
%oreon_meson -Dglib_debug=disabled -Dintrospection=enabled -Dman-pages=enabled -Ddtrace=enabled -Dsystemtap=enabled -Dsysprof=enabled -Dnls=enabled -Dlibelf=enabled -Dselinux=enabled -Dlibmount=enabled
%oreon_meson_build

%install
%oreon_meson_install
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
