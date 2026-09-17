%global source0_hash 6dbc80f6a09ba0cf6104a31784959780414dd77165e2963acd6657c28c2544c2

%if 0%{?fedora} < 28 && 0%{?rhel} < 8
%bcond_without libnm_glib
%else
# Disable the legacy version by default
%bcond_with libnm_glib
%endif

%if 0%{?fedora} < 36 && 0%{?rhel} < 10
%bcond_with gtk4
%else
# Use GTK4 for Fedora 36
%bcond_without gtk4
%endif

# Uses common git repository with strongswan:
# https://github.com/strongswan/strongswan/tree/master/src/frontends/gnome

Name:      NetworkManager-strongswan
Version:   1.6.0
Release:   12%{?dist}
Summary:   NetworkManager strongSwan IPSec VPN plug-in
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:   GPL-2.0-or-later
URL:       https://www.strongswan.org/
Source0:   https://download.strongswan.org/NetworkManager/%{name}-%{version}.tar.bz2
Source1:   https://download.strongswan.org/NetworkManager/%{name}-%{version}.tar.bz2.sig
Source2:   https://keys.openpgp.org/vks/v1/by-fingerprint/12538F8F689B5F1F15F07BE1765FE26C6B467584#/strongswan.asc

BuildRequires: make
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(libnm) >= 1.1.0
BuildRequires: pkgconfig(libnma) >= 1.1.0
BuildRequires: intltool
BuildRequires: libtool
%if 0%{?fedora}
BuildRequires: gnupg2
%endif

%if %{with gtk4}
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libnma-gtk4)
%endif

%if %{with libnm_glib}
BuildRequires: pkgconfig(dbus-glib-1) >= 0.30
BuildRequires: pkgconfig(NetworkManager) >= 1.1.0
BuildRequires: pkgconfig(libnm-util)
BuildRequires: pkgconfig(libnm-glib)
BuildRequires: pkgconfig(libnm-glib-vpn)
BuildRequires: pkgconfig(libnm-gtk)
%endif

Requires: NetworkManager
Requires: strongswan-charon-nm >= 5.8.3

%global __provides_exclude ^libnm-.*\\.so

%description
This package contains software for integrating the strongSwan IPSec VPN
with NetworkManager.

%package gnome
Summary: NetworkManager VPN plugin for strongswan - GNOME files

Requires: NetworkManager-strongswan = %{version}-%{release}

%description gnome
This package contains software for integrating the strongSwan IPSec VPN
with the graphical desktop.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?fedora}
%gpgverify -k 2 -d 0 -s 1
%endif
%autosetup -p1

%build
%configure \
        --disable-static \
%if %{with gtk4}
        --with-gtk4 \
%endif
%if %{without libnm_glib}
        --without-libnm-glib \
%endif
        --with-charon=%{_libexecdir}/strongswan/charon-nm \
        --enable-more-warnings=no
%make_build

%install
%make_install
%find_lang %{name}

rm -f %{buildroot}%{_libdir}/NetworkManager/libnm-*.la

%files -f %{name}.lang
%{_prefix}/lib/NetworkManager/VPN/nm-strongswan-service.name
%doc NEWS

%files gnome
%if %{with gtk4}
%{_libdir}/NetworkManager/libnm-gtk4-vpn-plugin-strongswan-editor.so
%endif
%{_prefix}/lib/NetworkManager/nm-strongswan-auth-dialog
%{_libdir}/NetworkManager/libnm-vpn-plugin-strongswan-editor.so
%{_libdir}/NetworkManager/libnm-vpn-plugin-strongswan.so
%{_datadir}/metainfo/NetworkManager-strongswan.metainfo.xml

%if %{with libnm_glib}
%{_libdir}/NetworkManager/libnm-*-properties.so
%{_sysconfdir}/NetworkManager/VPN/nm-strongswan-service.name
%endif

%changelog
%autochangelog
