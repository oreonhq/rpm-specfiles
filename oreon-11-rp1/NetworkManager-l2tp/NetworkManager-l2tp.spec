%global source0_hash 7a951d81dfbcbe4044fb88114f7a4e91d4e8f3d55bde148c743d3ee4700df3d9

Summary:   NetworkManager VPN plugin for L2TP and L2TP/IPsec
Name:      NetworkManager-l2tp
Epoch:     1
Version:   1.52.0
Release:   1%{?dist}
License:   GPL-2.0-or-later
URL:       https://github.com/nm-l2tp/NetworkManager-l2tp

Source0:        https://github.com/nm-l2tp/NetworkManager-l2tp/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires: make
BuildRequires: gcc
BuildRequires: gtk3-devel
BuildRequires: NetworkManager-libnm-devel >= 1.56.0
BuildRequires: glib2-devel
BuildRequires: libtool
BuildRequires: gettext
BuildRequires: libnma-devel >= 1.8.0
BuildRequires: libsecret-devel
BuildRequires: openssl-devel
BuildRequires: nss-devel
BuildRequires: intltool

Requires: dbus
Requires: NetworkManager >= 1:1.56.0
Requires: xl2tpd
Requires: ppp
Recommends: strongswan

%global __provides_exclude ^libnm-.*\\.so

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
%autosetup -p1

%build
%configure \
        --disable-static \
        --with-dist-version=%{version}-%{release}
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete

%find_lang %{name}

%files -f %{name}.lang
%{_libdir}/NetworkManager/libnm-vpn-plugin-l2tp.so
%{_prefix}/lib/NetworkManager/VPN/nm-l2tp-service.name
%{_libexecdir}/nm-l2tp-service
%doc README.md NEWS
%license COPYING

%files -n NetworkManager-l2tp-gnome
%{_libexecdir}/nm-l2tp-auth-dialog
%{_libdir}/NetworkManager/libnm-vpn-plugin-l2tp-editor.so
%{_datadir}/metainfo/network-manager-l2tp.metainfo.xml

%changelog
%autochangelog
