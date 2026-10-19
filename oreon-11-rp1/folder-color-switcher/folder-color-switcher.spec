%global source0_hash 5b8b3e6a3450257e86b4025b26145bf21d18b97856ad755200089dd61815b8ee
Name:           folder-color-switcher
Version:        1.7.1
Release:        1%{?dist}
Summary:        Change a folder colour
License:        GPL-3.0-only
URL:            https://github.com/linuxmint/folder-color-switcher
Source0:        http://packages.linuxmint.com/pool/main/f/%{name}/%{name}_%{version}.tar.xz
BuildArch:      noarch
Requires:       python3
# oreon:deps
BuildRequires:  gettext
BuildRequires:  make
# /oreon:deps
%description
Change a folder colour

%package nemo
Summary:        Nemo folder colour
Requires:       %{name} = %{version}-%{release}
Requires:       nemo-python
%description nemo
Support for Nemo folder colour

%package caja
Summary:        Caja folder colour
Requires:       %{name} = %{version}-%{release}
Requires:       python-caja
%description caja
Support for Caja folder colour

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}
chmod 644 COPYING.GPL3

%build

%make_build
%install
cp -Rp usr/ %{buildroot}/
for lib in %{buildroot}%{_datadir}/*-python/extensions/*.py; do
 sed '1{\@^#!/usr/bin/python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n folder-color-switcher-nemo -f %{oreon_filedir}/folder-color-switcher-nemo.list
%files -n folder-color-switcher-caja -f %{oreon_filedir}/folder-color-switcher-caja.list

%changelog

%autochangelog
