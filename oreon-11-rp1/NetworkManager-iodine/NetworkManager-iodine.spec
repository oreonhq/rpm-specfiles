%global source0_hash d0f3d59affaa032ed45e9232345bf808518ea2a3e8ea555d3551b638d58b4d5a
Summary:        NetworkManager VPN plugin for iodine
Name:      NetworkManager-iodine
Epoch:     1
Version:   1.2.0
Release:        1%{?dist}
License:   GPL-2.0-or-later
URL:       https://wiki.gnome.org/Projects/NetworkManager/VPN
Source0:        https://download.gnome.org/sources/NetworkManager-iodine/1.2/%{name}-%{version}.tar.xz
Patch0:         NetworkManager-iodine-1.2.0-g-add-private.patch
Patch1:         NetworkManager-iodine-1.2.0-vpnservicedir.patch
Patch2:         NetworkManager-iodine-1.2.0-name-properties.patch
Requires: dbus
Requires: NetworkManager >= 1:1.1.0
Requires: iodine
%global __provides_exclude ^libnm-.*\\.so
# oreon:deps
BuildRequires:  /usr/bin/file
BuildRequires:  NetworkManager-libnm-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  libnma-devel
BuildRequires:  libsecret-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
This package contains software for integrating VPN capabilities with the
iodine DNS tunnel with NetworkManager.

%package -n NetworkManager-iodine-gnome
Summary: NetworkManager VPN plugin for iodine - GNOME files
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires: shared-mime-info
%description -n NetworkManager-iodine-gnome
This package contains software for integrating VPN capabilities with
iodine with NetworkManager (GNOME/KDE authentication dialog files).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure \
        --disable-static \
        --without-libnm-glib \
        --with-dist-version=%{version}-%{release}
%make_build
%install
%make_install
mkdir -p %{buildroot}%{_prefix}/lib/NetworkManager/VPN
%{__cp} -p ./nm-iodine-service.name %{buildroot}%{_prefix}/lib/NetworkManager/VPN/
find %{buildroot} -name '*.la' -delete
if test -d %{buildroot}%{_sysconfdir}/dbus-1; then
    mv %{buildroot}%{_sysconfdir}/dbus-1 %{buildroot}%{_datadir}/
fi
%find_lang %{name}
%oreon_autofiles NetworkManager-iodine-gnome usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n NetworkManager-iodine-gnome -f %{oreon_filedir}/NetworkManager-iodine-gnome.list

%changelog

%autochangelog
