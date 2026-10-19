%global source0_hash f63cc794029759aeee5bcef10f9821659e623ccc0f11b22a19e06ebb256340e0
%global ppp_version %(pkg-config --modversion pppd 2>/dev/null || echo 2.5.1)
Summary:        NetworkManager VPN plugin for L2TP and L2TP/IPsec
Name:      NetworkManager-l2tp
Epoch:     1
Version:   1.52.6
Release:        1%{?dist}
License:   GPL-2.0-or-later
URL:       https://github.com/nm-l2tp/NetworkManager-l2tp
Source0:        https://github.com/nm-l2tp/NetworkManager-l2tp/releases/download/%{version}/%{name}-%{version}.tar.xz
Requires: dbus
Requires: NetworkManager >= 1:1.56.0
Requires: xl2tpd
Requires: ppp = %{ppp_version}
Recommends: strongswan
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
BuildRequires:  nss-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(pppd)
BuildRequires:  ppp-devel
# /oreon:deps
%description
This package contains software for integrating VPN capabilities with
L2TP and L2TP/IPsec (L2TP over IPsec) connections with NetworkManager,
using xl2tpd for the L2TP tunnel and strongSwan or Libreswan for the
IPsec layer.

%package -n NetworkManager-l2tp-gnome
Summary: NetworkManager VPN plugin for L2TP - GNOME files
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires: shared-mime-info
%description -n NetworkManager-l2tp-gnome
This package contains software for integrating VPN capabilities with L2TP
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
%oreon_autofiles NetworkManager-l2tp-gnome usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n NetworkManager-l2tp-gnome -f %{oreon_filedir}/NetworkManager-l2tp-gnome.list

%changelog

%autochangelog
