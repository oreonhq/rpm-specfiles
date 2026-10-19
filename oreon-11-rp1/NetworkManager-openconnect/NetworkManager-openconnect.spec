%global source0_hash 844b6bf64ecadb97b4a68c776db89aa5e6ee7e59bd24b0180228406863136464
Summary:        NetworkManager VPN plugin for OpenConnect
Name:      NetworkManager-openconnect
Epoch:     1
Version:   1.2.10
Release:        1%{?dist}
License:   GPL-2.0-or-later
URL:       https://wiki.gnome.org/Projects/NetworkManager/VPN
Source0:        https://download.gnome.org/sources/NetworkManager-openconnect/1.2/%{name}-%{version}.tar.xz
Requires: dbus
Requires: NetworkManager >= 1:1.2.0
Requires: openconnect >= 3.02
%global __provides_exclude ^libnm-.*\\.so
# oreon:deps
BuildRequires:  /usr/bin/file
BuildRequires:  NetworkManager-libnm-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  libnma-devel
BuildRequires:  libsecret-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openconnect-devel
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  webkit2gtk4.1-devel
# /oreon:deps
%description
This package contains software for integrating VPN capabilities with
Cisco AnyConnect, Juniper/Pulse, GlobalProtect, Fortinet and other SSL
VPNs (via openconnect) with NetworkManager.

%package -n NetworkManager-openconnect-gnome
Summary: NetworkManager VPN plugin for OpenConnect - GNOME files
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires: shared-mime-info
%description -n NetworkManager-openconnect-gnome
This package contains software for integrating VPN capabilities with
OpenConnect with NetworkManager (GNOME/KDE authentication dialog files).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure \
        --disable-static \
        --with-dist-version=%{version}-%{release}
%make_build
%install
%make_install
find %{buildroot} -name '*.la' -delete
%find_lang %{name}
%oreon_autofiles NetworkManager-openconnect-gnome usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n NetworkManager-openconnect-gnome -f %{oreon_filedir}/NetworkManager-openconnect-gnome.list

%changelog

%autochangelog
