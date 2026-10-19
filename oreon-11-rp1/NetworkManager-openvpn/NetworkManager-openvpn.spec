%global source0_hash ce32e38b0500eddf2fc8072ca17679817fc2d35eb91f6ff7b9904209c14b5afd
%if 0%{?fedora} < 36 && 0%{?rhel} < 9 && 0%{?oreon} < 11
%bcond_with gtk4
%else
%bcond_without gtk4
%endif
Summary:        NetworkManager VPN plugin for OpenVPN
Name:      NetworkManager-openvpn
Epoch:     1
Version:   1.12.5
Release:        1%{?dist}
License:   GPL-2.0-or-later
URL:       http://www.gnome.org/projects/NetworkManager/
Source0:        https://download.gnome.org/sources/NetworkManager-openvpn/1.12/%{name}-%{version}.tar.xz
Patch0:    https://gitlab.gnome.org/GNOME/NetworkManager-openvpn/-/merge_requests/104.patch
%if %with gtk4
%endif
Requires: dbus
Requires: NetworkManager >= 1:1.46.2
Requires: openvpn
Obsoletes: NetworkManager-openvpn < 1:0.9.8.2-3
%global __provides_exclude ^libnm-.*\\.so
# oreon:deps
BuildRequires:  NetworkManager-libnm-devel
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  libnma-devel
BuildRequires:  libnma-gtk4-devel
BuildRequires:  libsecret-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
This package contains software for integrating VPN capabilities with
the OpenVPN server with NetworkManager.

%package -n NetworkManager-openvpn-gnome
Summary: NetworkManager VPN plugin for OpenVPN - GNOME files
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires: gtk3
Requires: shared-mime-info
Obsoletes: NetworkManager-openvpn < 1:0.9.8.2-3
%description -n NetworkManager-openvpn-gnome
This package contains software for integrating VPN capabilities with
the OpenVPN server with NetworkManager (GNOME files).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

if [ ! -f configure ]; then
  ./autogen.sh
fi
%configure \
        --disable-static \
%if %with gtk4
        --with-gtk4 \
%endif
        --enable-more-warnings=yes \
        --with-dist-version=%{version}-%{release}
make %{?_smp_mflags}
%check

make check
%install
make install DESTDIR=%{buildroot} INSTALL="%{__install} -p"
rm -f %{buildroot}%{_libdir}/NetworkManager/lib*.la
%find_lang %{name}
%oreon_autofiles NetworkManager-openvpn-gnome usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n NetworkManager-openvpn-gnome -f %{oreon_filedir}/NetworkManager-openvpn-gnome.list

%changelog

* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:1.12.5-1
- Import Fedora rawhide NetworkManager-openvpn 1.12.5-4 as 1.12.5-1

