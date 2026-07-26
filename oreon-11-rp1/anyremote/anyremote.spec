%global source0_hash c30f6ad0e03716d4d3dfd839cf429763aea272c34ef19b7653b45b2e67f690d9

Name: anyremote
Version: 6.7.3
Release: 18%{?dist}
Summary: Remote control through Wi-Fi or bluetooth connection
License: GPL-3.0-or-later
URL: https://anyremote.sourceforge.net/
Source0: https://downloads.sourceforge.net/anyremote/%{name}-%{version}.tar.gz
Patch0: fix_compile_error.patch

BuildRequires: gcc
BuildRequires: make
BuildRequires: bluez-libs-devel >= 5.0
BuildRequires: libX11-devel
BuildRequires: libXi-devel
BuildRequires: libXtst-devel
BuildRequires: xorg-x11-proto-devel
BuildRequires: glib2-devel >= 2.24.1
BuildRequires: dbus-devel >= 1.2.24
BuildRequires: dbus-glib-devel >= 0.86
BuildRequires: avahi-devel >= 0.6.25

Requires: bc
Requires: wmctrl
Requires: ImageMagick
Requires: anyremote-data >= 6.7.3

%description
Remote control software for applications using Wi-Fi or Bluetooth.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files 
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%package data
Summary: Configuration files for anyRemote
Group: Applications/System

%description data
Configuration files for anyRemote

%files data
%{_datadir}/%{name}

%package doc
Summary: Documentation for anyRemote
Group: Applications/System

%description doc
Documentation for anyRemote

%files doc
%doc %{_defaultdocdir}/%{name}

%changelog
%autochangelog
