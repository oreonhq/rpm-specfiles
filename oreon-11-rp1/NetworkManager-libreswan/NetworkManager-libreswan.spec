%global source0_hash 6670af36d3bb4887e528f803babb689e42711e4ebbd29d8df6a178d3f17a11d3

%if 0%{?fedora} < 28 && 0%{?rhel} < 8
%bcond_without libnm_glib
%else
%bcond_with libnm_glib
%endif
%if 0%{?fedora} < 36 && 0%{?rhel} < 10
%bcond_with gtk4
%else
%bcond_without gtk4
%endif

%global nm_version       1:1.2.0
%global nma_version      1.2.0

Summary:   NetworkManager VPN plug-in for IPsec VPN
Name:      NetworkManager-libreswan
Version:   1.2.30
Release:   3%{?dist}
License:   GPL-2.0-or-later
URL:       https://gitlab.gnome.org/GNOME/NetworkManager-libreswan
Source0:        https://download.gnome.org/sources/NetworkManager-libreswan/1.2/%{name}-%{version}.tar.xz

#Patch1: 0001-some.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: gtk3-devel
BuildRequires: libnl3-devel
BuildRequires: NetworkManager-libnm-devel >= %{nm_version}
BuildRequires: libnma-devel >= %{nma_version}
BuildRequires: libsecret-devel
BuildRequires: intltool gettext

%if %with libnm_glib
BuildRequires: NetworkManager-devel >= %{nm_version}
BuildRequires: NetworkManager-glib-devel >= %{nm_version}
BuildRequires: libnm-gtk-devel >= %{nma_version}
%endif

%if %with gtk4
BuildRequires: libnma-gtk4-devel
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
%autosetup -p1


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

%files -f %{name}.lang
%{_libdir}/NetworkManager/libnm-vpn-plugin-libreswan.so
%{_datadir}/dbus-1/system.d/nm-libreswan-service.conf
%{_prefix}/lib/NetworkManager/VPN/nm-libreswan-service.name
%{_libexecdir}/nm-libreswan-service
%{_libexecdir}/nm-libreswan-service-helper
%{_mandir}/man5/nm-settings-libreswan.5.gz
%doc AUTHORS NEWS
%license COPYING


%files -n NetworkManager-libreswan-gnome
%{_libexecdir}/nm-libreswan-auth-dialog
%{_libdir}/NetworkManager/libnm-vpn-plugin-libreswan-editor.so
%{_metainfodir}/network-manager-libreswan.metainfo.xml

%if %with libnm_glib
%{_libdir}/NetworkManager/libnm-*-properties.so
%{_sysconfdir}/NetworkManager/VPN/nm-libreswan-service.name
%endif

%if %with gtk4
%{_libdir}/NetworkManager/libnm-gtk4-vpn-plugin-libreswan-editor.so
%endif


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.30-3
- Prepare for Oreon 11 (RP1)
