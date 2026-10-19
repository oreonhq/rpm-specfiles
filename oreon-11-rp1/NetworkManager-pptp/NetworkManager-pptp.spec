%global source0_hash e5fa59fe46117f0ee86e9ca62c6943bc063884b04dd2396ccec38a2d1f414982
%global ppp_version %(pkg-config --modversion pppd 2>/dev/null || echo 2.5.1)
Summary:        NetworkManager VPN plugin for PPTP
Name:      NetworkManager-pptp
Epoch:     1
Version:   1.2.12
Release:        1%{?dist}
License:   GPL-2.0-or-later
URL:       https://wiki.gnome.org/Projects/NetworkManager/VPN
Source0:        https://download.gnome.org/sources/NetworkManager-pptp/1.2/%{name}-%{version}.tar.xz
Requires: dbus
Requires: NetworkManager >= 1:1.2.0
Requires: ppp = %{ppp_version}
Requires: pptp
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
BuildRequires:  pkgconfig(pppd)
BuildRequires:  ppp-devel
# /oreon:deps
%description
This package contains software for integrating VPN capabilities with the
Point-to-Point Tunneling Protocol (PPTP) with NetworkManager.

%package -n NetworkManager-pptp-gnome
Summary: NetworkManager VPN plugin for PPTP - GNOME files
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires: shared-mime-info
%description -n NetworkManager-pptp-gnome
This package contains software for integrating VPN capabilities with PPTP
with NetworkManager (GNOME/KDE authentication dialog files).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure \
        --disable-static \
        --with-dist-version=%{version}-%{release} \
        --with-pppd-plugin-dir=%{_libdir}/pppd/%{ppp_version}
%make_build
%install
%make_install
find %{buildroot} -name '*.la' -delete
%find_lang %{name}
%oreon_autofiles NetworkManager-pptp-gnome usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n NetworkManager-pptp-gnome -f %{oreon_filedir}/NetworkManager-pptp-gnome.list

%changelog

%autochangelog
