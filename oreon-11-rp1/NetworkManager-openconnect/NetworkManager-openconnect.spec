%global source0_hash 844b6bf64ecadb97b4a68c776db89aa5e6ee7e59bd24b0180228406863136464

Summary:   NetworkManager VPN plugin for OpenConnect
Name:      NetworkManager-openconnect
Epoch:     1
Version:   1.2.10
Release:   1%{?dist}
License:   GPL-2.0-or-later
URL:       https://wiki.gnome.org/Projects/NetworkManager/VPN

Source0:        https://download.gnome.org/sources/NetworkManager-openconnect/1.2/%{name}-%{version}.tar.xz

BuildRequires: make
BuildRequires: gcc
BuildRequires: gtk3-devel
BuildRequires: NetworkManager-libnm-devel >= 1:1.2.0
BuildRequires: glib2-devel
BuildRequires: libtool
BuildRequires: gettext
BuildRequires: libnma-devel >= 1.2.0
BuildRequires: libsecret-devel
BuildRequires: gcr-devel
BuildRequires: openconnect-devel >= 3.02
BuildRequires: intltool

Requires: dbus
Requires: NetworkManager >= 1:1.2.0
Requires: openconnect >= 3.02

%global __provides_exclude ^libnm-.*\\.so

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
%{_libdir}/NetworkManager/libnm-vpn-plugin-openconnect.so
%{_prefix}/lib/NetworkManager/VPN/nm-openconnect-service.name
%{_libexecdir}/nm-openconnect-service
%doc AUTHORS NEWS README
%license COPYING

%files -n NetworkManager-openconnect-gnome
%{_libexecdir}/nm-openconnect-auth-dialog
%{_libdir}/NetworkManager/libnm-vpn-plugin-openconnect-editor.so
%{_datadir}/metainfo/network-manager-openconnect.metainfo.xml

%changelog
%autochangelog
