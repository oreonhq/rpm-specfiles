%global source0_hash b80e2874157cd55071f1b6710fa0b911d5ac5de106a9ee2a4c9c7bee61782f8e
%{?mingw_package_header}
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')
Name:           mingw-glib-networking
Version:        2.80.1
Release:        1%{?dist}
Summary:        MinGW Windows glib-networking library
License:        LGPL-2.1-or-later
URL:            http://www.gnome.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/glib-networking/%{release_version}/glib-networking-%{version}.tar.xz
BuildArch:      noarch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gsettings-desktop-schemas-devel
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-gnutls
BuildRequires:  mingw32-gsettings-desktop-schemas
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-gnutls
BuildRequires:  mingw64-gsettings-desktop-schemas
BuildRequires:  pkgconfig
# /oreon:deps
%description
This package contains modules that extend the networking support in GIO.

%package -n mingw32-glib-networking
Summary:        MinGW Windows glib-networking library
Requires:       mingw32-gsettings-desktop-schemas
%description -n mingw32-glib-networking
This package contains modules that extend the networking support in GIO.

%package -n mingw64-glib-networking
Summary:        MinGW Windows glib-networking library
Requires:       mingw64-gsettings-desktop-schemas
%description -n mingw64-glib-networking
This package contains modules that extend the networking support in GIO.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir glib-networking-%{version}
%oreon_prep
%build

%mingw_meson -Dlibproxy=disabled -Denvironment_proxy=enabled
%mingw_ninja
%install
%mingw_ninja_install
rm -f %{buildroot}%{mingw32_libdir}/gio/modules/*.dll.a
rm -f %{buildroot}%{mingw64_libdir}/gio/modules/*.dll.a
rm -f %{buildroot}%{mingw32_libdir}/gio/modules/*.la
rm -f %{buildroot}%{mingw64_libdir}/gio/modules/*.la
%mingw_find_lang glib-networking
%oreon_autofiles mingw32-glib-networking usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-glib-networking usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-glib-networking -f %{oreon_filedir}/mingw32-glib-networking.list
%files -n mingw64-glib-networking -f %{oreon_filedir}/mingw64-glib-networking.list

%changelog

%autochangelog
