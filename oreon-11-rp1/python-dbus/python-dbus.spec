%global source0_hash 57423cf87d09b7d084f420b55b737fe654c33339b06df77945620d97795c6ac4
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: python-dbus
Version: 1.5.1
Release: 1%{?dist}
Summary: Python bindings for D-Bus
License: MIT
URL: https://www.freedesktop.org/wiki/Software/DBusBindings/
Source0: https://files.pythonhosted.org/packages/f3/cc/23f24bc7cbfec3a0ab508b7e11bc98837d77a91445d5f666a8545353a147/dbus_python-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: pkgconf
BuildRequires: python3-devel
BuildRequires: dbus-devel
BuildRequires: glib2-devel
BuildRequires: patchelf
%endif

Provides: python3-dbus = %{version}-%{release}
Requires: python3
Requires: dbus

%description
python-dbus is the Python binding for D-Bus.

%prep
%oreon_sha256
%autosetup -n dbus_python-%{version} -p1

%build
%oreon_meson -Ddoc=disabled -Dtests=disabled
%oreon_meson_build

%install
%oreon_meson_install
find %{buildroot} -type f | while read -r f; do
  file -b "$f" | grep -q '^ELF' || continue
  r=$(patchelf --print-rpath "$f")
  if [ -n "$r" ]; then
    chmod u+w "$f"
    patchelf --remove-rpath "$f"
  fi
done
%oreon_filelist
python3 - %{_builddir}/%{name}.files << 'PY'
import os
import sys
from pathlib import Path
p = Path(sys.argv[1])
lines = p.read_text().splitlines()
seen = set(lines)
extra = []
for line in lines:
    path = line.strip().strip('"')
    if not path.endswith(".py"):
        continue
    if "/lib/python3." not in path and "/lib64/python3." not in path:
        continue
    glob = os.path.dirname(path) + "/__pycache__/*"
    if glob not in seen:
        seen.add(glob)
        extra.append(glob)
text = "\n".join(lines + extra)
p.write_text(text + ("\n" if text else ""))
PY

%files -f %{_builddir}/%{name}.files
%license COPYING
