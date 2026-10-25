%global source0_hash 0ba2a1a4b16afe7bceb2c07e9ce99a8c2c3508e5dec290dbb643384bd6beb7e2
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: dbus
Version: 1.16.2
Release: 1%{?dist}
Summary: D-Bus message bus
License: AFL-2.1 OR GPL-2.0-or-later
URL: https://www.freedesktop.org/wiki/Software/dbus/
Source0: https://dbus.freedesktop.org/releases/dbus/dbus-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: pkgconf
BuildRequires: expat-devel
BuildRequires: libselinux-devel
BuildRequires: audit-libs-devel
BuildRequires: libcap-ng-devel
BuildRequires: libX11-devel
BuildRequires: libxslt
BuildRequires: docbook-style-xsl
BuildRequires: docbook-dtds
BuildRequires: doxygen
BuildRequires: python3-mallard-ducktype
BuildRequires: yelp-tools
BuildRequires: qt-devel
BuildRequires: systemd-devel
BuildRequires: python3
BuildRequires: patchelf
%endif

%description
D-Bus is a message bus.

%package devel
Summary: D-Bus message bus
Requires: dbus%{?_isa} = %{version}-%{release}

%description devel
D-Bus is a message bus.

%prep
%oreon_sha256
%autosetup -p1

%build
%oreon_meson \
  -Dapparmor=disabled \
  -Dkqueue=disabled \
  -Dlaunchd=disabled \
  -Dlibaudit=enabled \
  -Dxml_docs=enabled \
  -Ddoxygen_docs=enabled \
  -Dducktype_docs=enabled \
  -Dqt_help=enabled \
  -Dx11_autolaunch=enabled \
  -Dselinux=enabled \
  -Dsystemd=enabled \
  -Dmessage_bus=true \
  -Dtools=true \
  -Dtraditional_activation=true
%oreon_meson_build

%install
%oreon_meson_install
find %{buildroot} -type f -exec grep -IlZ '^#!/usr/bin/env python$' {} + | while IFS= read -r -d '' f; do
  sed -i '1s|^#!/usr/bin/env python$|#!/usr/bin/python3|' "$f"
done
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
