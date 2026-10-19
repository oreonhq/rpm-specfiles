%global source0_hash e3b2a98880275a1b75154bc317a78643cfdf9ea7e70df4eed9648f29ea253730
Summary:        NetworkManager VPN plugin for vpnc
Name:      NetworkManager-vpnc
Epoch:     1
Version:   1.4.0
Release:        1%{?dist}
License:   GPL-2.0-or-later
URL:       https://wiki.gnome.org/Projects/NetworkManager/VPN
Source0:        https://download.gnome.org/sources/NetworkManager-vpnc/1.4/%{name}-%{version}.tar.xz
Requires: dbus
Requires: NetworkManager >= 1:1.2.0
Requires: vpnc
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
# /oreon:deps
%description
This package contains software for integrating VPN capabilities with
Cisco3000-compatible VPN concentrators (via vpnc) with NetworkManager.

%package -n NetworkManager-vpnc-gnome
Summary: NetworkManager VPN plugin for vpnc - GNOME files
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires: shared-mime-info
%description -n NetworkManager-vpnc-gnome
This package contains software for integrating VPN capabilities with
vpnc with NetworkManager (GNOME/KDE authentication dialog files).

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
%oreon_autofiles NetworkManager-vpnc-gnome usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n NetworkManager-vpnc-gnome -f %{oreon_filedir}/NetworkManager-vpnc-gnome.list

%changelog

%autochangelog
