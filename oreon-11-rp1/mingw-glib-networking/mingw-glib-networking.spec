%global source0_hash b80e2874157cd55071f1b6710fa0b911d5ac5de106a9ee2a4c9c7bee61782f8e

%{?mingw_package_header}

# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-glib-networking
Version:        2.80.1
Release:        4%{?dist}
Summary:        MinGW Windows glib-networking library

License:        LGPL-2.1-or-later
URL:            http://www.gnome.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/glib-networking/%{release_version}/glib-networking-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gsettings-desktop-schemas-devel
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pkgconfig

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-gnutls >= 2.10
BuildRequires:  mingw32-gsettings-desktop-schemas

BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-gnutls >= 2.10
BuildRequires:  mingw64-gsettings-desktop-schemas

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

%autosetup -p1 -n glib-networking-%{version}

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

%files -n mingw32-glib-networking -f mingw32-glib-networking.lang
%license COPYING
%{mingw32_libdir}/gio/modules/libgiognutls.dll
%{mingw32_libdir}/gio/modules/libgioenvironmentproxy.dll
%{mingw32_libdir}/gio/modules/libgiognomeproxy.dll

%files -n mingw64-glib-networking -f mingw64-glib-networking.lang
%license COPYING
%{mingw64_libdir}/gio/modules/libgiognutls.dll
%{mingw64_libdir}/gio/modules/libgioenvironmentproxy.dll
%{mingw64_libdir}/gio/modules/libgiognomeproxy.dll

%changelog
%autochangelog
