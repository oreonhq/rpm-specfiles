%global source0_hash b055e26349b516b23585798ab3ef57b436b014800e92a8ac732cfc8e76c5dafa
%global ppp_version %(pkg-config --modversion pppd 2>/dev/null || echo 2.5.1)
Summary:        NetworkManager VPN plugin for Fortinet SSL VPN
Name:      NetworkManager-fortisslvpn
Epoch:     1
Version:   1.4.0
Release:        1%{?dist}
License:   GPL-2.0-or-later
URL:       https://wiki.gnome.org/Projects/NetworkManager/VPN
Source0:        https://download.gnome.org/sources/NetworkManager-fortisslvpn/1.4/%{name}-%{version}.tar.xz
Patch0:         networkmanager-fortisslvpn-1.4.0-ppp-2.5.0-1.patch
Patch1:         networkmanager-fortisslvpn-1.4.0-ppp-2.5.0-2.patch
Patch2:         networkmanager-fortisslvpn-1.4.0-ppp-2.5.0-3.patch
Requires: dbus
Requires: NetworkManager >= 1:1.2.0
Requires: ppp = %{ppp_version}
%global __provides_exclude ^libnm-.*\\.so
# oreon:deps
BuildRequires:  /usr/bin/file
BuildRequires:  NetworkManager-libnm-devel
BuildRequires:  autoconf
BuildRequires:  automake
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
%oreon_autofiles NetworkManager-fortisslvpn-gnome usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n NetworkManager-fortisslvpn-gnome -f %{oreon_filedir}/NetworkManager-fortisslvpn-gnome.list

%changelog

%autochangelog
