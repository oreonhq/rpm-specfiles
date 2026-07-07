%global source0_hash e5fa59fe46117f0ee86e9ca62c6943bc063884b04dd2396ccec38a2d1f414982

Summary:   NetworkManager VPN plugin for PPTP
Name:      NetworkManager-pptp
Epoch:     1
Version:   1.2.12
Release:   1%{?dist}
License:   GPL-2.0-or-later
URL:       https://wiki.gnome.org/Projects/NetworkManager/VPN

Source0:        https://download.gnome.org/sources/NetworkManager-pptp/1.2/%{name}-%{version}.tar.xz

BuildRequires: make
BuildRequires: gcc
BuildRequires: gtk3-devel
BuildRequires: NetworkManager-libnm-devel >= 1:1.2.0
BuildRequires: glib2-devel
BuildRequires: libtool
BuildRequires: gettext
BuildRequires: libnma-devel >= 1.2.0
BuildRequires: libsecret-devel
BuildRequires: intltool

Requires: dbus
Requires: NetworkManager >= 1:1.2.0
Requires: ppp
Requires: pptp

%global __provides_exclude ^libnm-.*\\.so

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
%{_libdir}/NetworkManager/libnm-vpn-plugin-pptp.so
%{_prefix}/lib/NetworkManager/VPN/nm-pptp-service.name
%{_libexecdir}/nm-pptp-service
%doc AUTHORS NEWS README
%license COPYING

%files -n NetworkManager-pptp-gnome
%{_libexecdir}/nm-pptp-auth-dialog
%{_libdir}/NetworkManager/libnm-vpn-plugin-pptp-editor.so
%{_datadir}/metainfo/network-manager-pptp.metainfo.xml

%changelog
%autochangelog
