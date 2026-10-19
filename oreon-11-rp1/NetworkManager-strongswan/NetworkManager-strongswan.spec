%global source2_hash 09fbb94ae613a0b44940573e194fd22c75aa3bb5b187ff1e3754751c3c73d51b
%global source1_hash b4816b4bf7f19f9e899eddbb184d0935d94c92f51b250a7aa2a059925cc35dc4
%global source0_hash 6fe095802629c741f44fe6241115dc0e86b917ccf05ee59c72ec8441e64fe58a
%if 0%{?fedora} < 28 && 0%{?rhel} < 8 && 0%{?oreon} < 11
%bcond_without libnm_glib
%else
%bcond_with libnm_glib
%endif
%if 0%{?fedora} < 36 && 0%{?rhel} < 10 && 0%{?oreon} < 11
%bcond_with gtk4
%else
%bcond_without gtk4
%endif
Name:      NetworkManager-strongswan
Version:   1.6.6
Release:        1%{?dist}
Summary:        NetworkManager strongSwan IPSec VPN plug-in
License:   GPL-2.0-or-later
URL:       https://www.strongswan.org/
Source0:        https://download.strongswan.org/NetworkManager/%{name}-%{version}.tar.bz2
Source1:   https://download.strongswan.org/NetworkManager/%{name}-%{version}.tar.bz2.sig
Source2:   https://keys.openpgp.org/vks/v1/by-fingerprint/12538F8F689B5F1F15F07BE1765FE26C6B467584#/strongswan.asc
%if %{with gtk4}
%endif
%if %{with libnm_glib}
%endif
Requires: NetworkManager
Requires: strongswan-charon-nm >= 5.8.3
%global __provides_exclude ^libnm-.*\\.so
# oreon:deps
BuildRequires:  gnupg2
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libnma)
BuildRequires:  pkgconfig(libnma-gtk4)
BuildRequires:  pkgconfig(libsecret-1)
# /oreon:deps
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
%oreon_prep
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
%oreon_autofiles NetworkManager-strongswan-gnome usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n NetworkManager-strongswan-gnome -f %{oreon_filedir}/NetworkManager-strongswan-gnome.list

%changelog

%autochangelog
