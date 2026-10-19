%global source0_hash 658c93ef4f0d206586948dbcdc07742f9271ec3e78cda2ed3837d793424bcd2a
Name: anyremote
Version: 8.1.1
Release:        1%{?dist}
Summary:        Remote control through Wi-Fi or bluetooth connection
License: GPL-3.0-or-later
URL: https://anyremote.sourceforge.net/
Source0:        https://downloads.sourceforge.net/anyremote/%{name}-%{version}.tar.gz
Patch0: fix_compile_error.patch
Requires: bc
Requires: wmctrl
Requires: ImageMagick
Requires: anyremote-data >= 8.1.1
# oreon:deps
BuildRequires:  avahi-devel
BuildRequires:  bluez-libs-devel
BuildRequires:  dbus-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  libX11-devel
BuildRequires:  libXi-devel
BuildRequires:  libXtst-devel
BuildRequires:  make
BuildRequires:  xorg-x11-proto-devel
# /oreon:deps
%description
Remote control software for applications using Wi-Fi or Bluetooth.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
%oreon_autofiles anyremote-data usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles anyremote-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%package data
Summary: Configuration files for anyRemote
Group: Applications/System
%description data
Configuration files for anyRemote

%package doc
Summary: Documentation for anyRemote
Group: Applications/System
%description doc
Documentation for anyRemote

%files -f %{oreon_filedir}/main.list
%files -n anyremote-data -f %{oreon_filedir}/anyremote-data.list
%files -n anyremote-doc -f %{oreon_filedir}/anyremote-doc.list

%changelog

%autochangelog
