%global source0_hash e71ab7cd6aee6683aa94342eb26e61433bffdf2da69782eca6d1c299dcc3a76f
%bcond_with libnm_glib
%if 0%{?fedora} < 36 && 0%{?rhel} < 10 && 0%{?oreon} < 11
%bcond_with gtk4
%else
%bcond_without gtk4
%endif
%global nm_version       1:1.2.0
%global nma_version      1.2.0
Summary:        NetworkManager VPN plug-in for IPsec VPN
Name:      NetworkManager-libreswan
Version:   1.2.31
Release:        1%{?dist}
License:   GPL-2.0-or-later
URL:       https://gitlab.gnome.org/GNOME/NetworkManager-libreswan
Source0:        https://download.gnome.org/sources/NetworkManager-libreswan/1.2/%{name}-%{version}.tar.xz
%if %with libnm_glib
%endif
%if %with gtk4
%endif
Requires: NetworkManager >= %{nm_version}
Requires: dbus-common
Requires: /usr/sbin/ipsec
Provides: NetworkManager-openswan = %{version}-%{release}
Obsoletes: NetworkManager-openswan < %{version}-%{release}
Recommends: (NetworkManager-libreswan-gnome%{?_isa} = %{version}-%{release} if libnma%{?_isa})
%if %with gtk4
Recommends: (NetworkManager-libreswan-gnome%{?_isa} = %{version}-%{release} if libnma-gtk4%{?_isa})
%endif
%global _privatelibs libnm-libreswan-properties[.]so.*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$
# oreon:deps
BuildRequires:  NetworkManager-libnm-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  libnl3-devel
BuildRequires:  libnma-devel
BuildRequires:  libnma-gtk4-devel
BuildRequires:  libsecret-devel
BuildRequires:  make
# /oreon:deps
%description
This package contains software for integrating the libreswan VPN software
with NetworkManager and the GNOME desktop

%package -n NetworkManager-libreswan-gnome
Summary: NetworkManager VPN plugin for libreswan - GNOME files
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: shared-mime-info
Provides: NetworkManager-openswan-gnome = %{version}-%{release}
Obsoletes: NetworkManager-openswan-gnome < %{version}-%{release}
%description -n NetworkManager-libreswan-gnome
This package contains software for integrating VPN capabilities with
the libreswan server with NetworkManager (GNOME files).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure \
        --disable-static \
%if %with gtk4
        --with-gtk4 \
%endif
%if %without libnm_glib
        --without-libnm-glib \
%endif
        --enable-more-warnings=yes \
        --with-dist-version=%{version}-%{release}
%make_build
%check

make check
%install
%make_install
rm -f %{buildroot}%{_libdir}/NetworkManager/lib*.la
mv %{buildroot}%{_sysconfdir}/dbus-1 %{buildroot}%{_datadir}/
%find_lang %{name}
%oreon_autofiles NetworkManager-libreswan-gnome usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n NetworkManager-libreswan-gnome -f %{oreon_filedir}/NetworkManager-libreswan-gnome.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.30-3
- Prepare for Oreon 11 (RP1)
