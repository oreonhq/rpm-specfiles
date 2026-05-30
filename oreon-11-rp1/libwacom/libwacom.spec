%global source0_hash 7dbb9ab37df9df47ae2fdbb644916c986728291749bcd5ad8bcaa26f1e15f002

Name:           libwacom
Version:        2.18.0
Release:        1%{?dist}
Summary:        Tablet Information Client Library
Requires:       %{name}-data

License:        HPND
URL:            https://github.com/linuxwacom/libwacom

Source0:        https://github.com/linuxwacom/libwacom/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz

BuildRequires:  meson gcc
BuildRequires:  glib2-devel libgudev1-devel libevdev-devel
BuildRequires:  systemd systemd-devel
BuildRequires:  git-core
BuildRequires:  libxml2-devel

Requires:       %{name}-data = %{version}-%{release}

%description
%{name} is a library that provides information about Wacom tablets and
tools. This information can then be used by drivers or applications to tweak
the UI or general settings to match the physical tablet.

%package devel
Summary:        Tablet Information Client Library Development Package
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
Tablet information client library development package.

%package data
Summary:        Tablet Information Client Library Data Files
BuildArch:      noarch

%description data
Tablet information client library data files.

%package utils
Summary:        Tablet Information Client Library Utilities Package
Requires:       %{name} = %{version}-%{release}
Requires:       python3-libevdev python3-pyudev

%description utils
Utilities to handle and/or debug libwacom devices.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -S git

%build
%meson -Dtests=disabled -Ddocumentation=disabled
%meson_build

%install
%meson_install
install -d ${RPM_BUILD_ROOT}/%{_udevrulesdir}

%check
%meson_test

%ldconfig_scriptlets

%files
%license COPYING
%doc README.md
%{_libdir}/libwacom.so.*
%{_bindir}/libwacom-list-local-devices
%{_bindir}/libwacom-update-db

%{_mandir}/man1/libwacom-list-local-devices.1*

%files devel
%dir %{_includedir}/libwacom-1.0/
%dir %{_includedir}/libwacom-1.0/libwacom
%{_includedir}/libwacom-1.0/libwacom/libwacom.h
%{_libdir}/libwacom.so
%{_libdir}/pkgconfig/libwacom.pc

%files data
%doc COPYING
%{_udevrulesdir}/65-libwacom.rules
%{_udevhwdbdir}/65-libwacom.hwdb
%dir %{_datadir}/libwacom
%{_datadir}/libwacom/*.tablet
%{_datadir}/libwacom/*.stylus
%dir %{_datadir}/libwacom/layouts
%{_datadir}/libwacom/layouts/*.svg

%files utils
%{_bindir}/libwacom-list-devices
%{_bindir}/libwacom-show-stylus
%{_mandir}/man1/libwacom-list-devices.1*
%{_mandir}/man1/libwacom-show-stylus.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.18.0-1
- Prepare for Oreon 11 (RP1)
