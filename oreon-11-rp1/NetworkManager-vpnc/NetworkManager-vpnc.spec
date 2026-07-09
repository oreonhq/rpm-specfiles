%global source0_hash e3b2a98880275a1b75154bc317a78643cfdf9ea7e70df4eed9648f29ea253730

Summary:   NetworkManager VPN plugin for vpnc
Name:      NetworkManager-vpnc
Epoch:     1
Version:   1.4.0
Release:   1%{?dist}
License:   GPL-2.0-or-later
URL:       https://wiki.gnome.org/Projects/NetworkManager/VPN

Source0:        https://download.gnome.org/sources/NetworkManager-vpnc/1.4/%{name}-%{version}.tar.xz

BuildRequires: make
BuildRequires: gcc
BuildRequires: gtk3-devel
BuildRequires: NetworkManager-libnm-devel >= 1:1.2.0
BuildRequires: glib2-devel
BuildRequires: libtool
BuildRequires: gettext
BuildRequires: libnma-devel >= 1.8.0
BuildRequires: libsecret-devel
BuildRequires: intltool
BuildRequires: /usr/bin/file

Requires: dbus
Requires: NetworkManager >= 1:1.2.0
Requires: vpnc

%global __provides_exclude ^libnm-.*\\.so

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
%{_libdir}/NetworkManager/libnm-vpn-plugin-vpnc.so
%{_prefix}/lib/NetworkManager/VPN/nm-vpnc-service.name
%{_libexecdir}/nm-vpnc-service
%{_libexecdir}/nm-vpnc-service-vpnc-helper
%{_datadir}/dbus-1/system.d/nm-vpnc-service.conf
%doc AUTHORS NEWS README
%license COPYING

%files -n NetworkManager-vpnc-gnome
%{_libexecdir}/nm-vpnc-auth-dialog
%{_libdir}/NetworkManager/libnm-vpn-plugin-vpnc-editor.so
%{_datadir}/metainfo/network-manager-vpnc.metainfo.xml

%changelog
%autochangelog
