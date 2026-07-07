%global source0_hash cddfa0f3a7192f289b2e160b6a5e97cd46fdc05bbb90744ea742b344cf794278

Summary:   NetworkManager VPN plugin for SSTP
Name:      NetworkManager-sstp
Epoch:     1
Version:   1.3.2
Release:   1%{?dist}
License:   GPL-2.0-or-later
URL:       https://wiki.gnome.org/Projects/NetworkManager/VPN

Source0:        https://download.gnome.org/sources/NetworkManager-sstp/1.3/%{name}-%{version}.tar.xz

BuildRequires: make
BuildRequires: gcc
BuildRequires: gtk3-devel
BuildRequires: NetworkManager-libnm-devel >= 1.7.0
BuildRequires: glib2-devel
BuildRequires: libtool
BuildRequires: gettext
BuildRequires: libnma-devel >= 1.8.0
BuildRequires: libsecret-devel
BuildRequires: gnutls-devel
BuildRequires: sstp-client-devel >= 1.0.10
BuildRequires: intltool

Requires: dbus
Requires: NetworkManager >= 1:1.7.0
Requires: sstp-client >= 1.0.10
Requires: ppp

%global __provides_exclude ^libnm-.*\\.so

%description
This package contains software for integrating VPN capabilities with the
Secure Socket Tunneling Protocol (SSTP), via sstp-client, with
NetworkManager.

%package -n NetworkManager-sstp-gnome
Summary: NetworkManager VPN plugin for SSTP - GNOME files

Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires: shared-mime-info

%description -n NetworkManager-sstp-gnome
This package contains software for integrating VPN capabilities with SSTP
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
%{_libdir}/NetworkManager/libnm-vpn-plugin-sstp.so
%{_prefix}/lib/NetworkManager/VPN/nm-sstp-service.name
%{_libexecdir}/nm-sstp-service
%doc AUTHORS README
%license COPYING

%files -n NetworkManager-sstp-gnome
%{_libexecdir}/nm-sstp-auth-dialog
%{_libdir}/NetworkManager/libnm-vpn-plugin-sstp-editor.so
%{_datadir}/metainfo/network-manager-sstp.metainfo.xml

%changelog
%autochangelog
