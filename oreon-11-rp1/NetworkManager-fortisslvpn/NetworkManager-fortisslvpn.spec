%global source0_hash b055e26349b516b23585798ab3ef57b436b014800e92a8ac732cfc8e76c5dafa
%global ppp_version %(pkg-config --modversion pppd 2>/dev/null || echo 2.5.1)

Summary:   NetworkManager VPN plugin for Fortinet SSL VPN
Name:      NetworkManager-fortisslvpn
Epoch:     1
Version:   1.4.0
Release:   2%{?dist}
License:   GPL-2.0-or-later
URL:       https://wiki.gnome.org/Projects/NetworkManager/VPN

Source0:        https://download.gnome.org/sources/NetworkManager-fortisslvpn/1.4/%{name}-%{version}.tar.xz
Patch0:         networkmanager-fortisslvpn-1.4.0-ppp-2.5.0-1.patch
Patch1:         networkmanager-fortisslvpn-1.4.0-ppp-2.5.0-2.patch
Patch2:         networkmanager-fortisslvpn-1.4.0-ppp-2.5.0-3.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: gtk3-devel
BuildRequires: NetworkManager-libnm-devel >= 1.2.0
BuildRequires: glib2-devel
BuildRequires: libtool
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gettext
BuildRequires: libnma-devel >= 1.8.33
BuildRequires: libsecret-devel
BuildRequires: ppp-devel
BuildRequires: pkgconfig(pppd)
BuildRequires: intltool
BuildRequires: /usr/bin/file

Requires: dbus
Requires: NetworkManager >= 1:1.2.0
Requires: ppp = %{ppp_version}

%global __provides_exclude ^libnm-.*\\.so

%description
This package contains software for integrating VPN capabilities with the
Fortinet SSL VPN with NetworkManager. The SSL VPN client itself is
implemented in the plugin (via ppp and OpenSSL/GnuTLS), no external
openfortivpn binary is required.

%package -n NetworkManager-fortisslvpn-gnome
Summary: NetworkManager VPN plugin for Fortinet SSL VPN - GNOME files

Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires: shared-mime-info

%description -n NetworkManager-fortisslvpn-gnome
This package contains software for integrating VPN capabilities with the
Fortinet SSL VPN with NetworkManager (GNOME/KDE authentication dialog
files).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
[ -f src/nm-ppp-status.h ] && [ ! -f src/nm-fortisslvpn-pppd-status.h ] && mv src/nm-ppp-status.h src/nm-fortisslvpn-pppd-status.h
autoreconf -fvi

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

%files -f %{name}.lang
%{_libdir}/NetworkManager/libnm-vpn-plugin-fortisslvpn.so
%{_libdir}/pppd/%{ppp_version}/nm-fortisslvpn-pppd-plugin.so
%{_prefix}/lib/NetworkManager/VPN/nm-fortisslvpn-service.name
%{_libexecdir}/nm-fortisslvpn-service
%{_libexecdir}/nm-fortisslvpn-pinentry
%{_sysconfdir}/dbus-1/system.d/nm-fortisslvpn-service.conf
%doc AUTHORS NEWS README
%license COPYING

%files -n NetworkManager-fortisslvpn-gnome
%{_libexecdir}/nm-fortisslvpn-auth-dialog
%{_libdir}/NetworkManager/libnm-vpn-plugin-fortisslvpn-editor.so
%{_datadir}/appdata/network-manager-fortisslvpn.metainfo.xml

%changelog
%autochangelog
