%global source0_hash 0ba2a1a4b16afe7bceb2c07e9ce99a8c2c3508e5dec290dbb643384bd6beb7e2
%{?mingw_package_header}
Name:           mingw-dbus
Version:        1.16.2
Release:        1%{?dist}
Summary:        MinGW Windows port of D-Bus
License: (AFL-2.1 OR GPL-2.0-or-later) AND GPL-2.0-or-later
URL:            http://www.freedesktop.org/wiki/Software/dbus
Source0:        http://dbus.freedesktop.org/releases/dbus/dbus-%{version}.tar.xz
Patch0:         dbus-static-libs.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  mingw32-expat
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-glib2
BuildRequires:  mingw64-expat
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-glib2
# /oreon:deps
%description
D-BUS is a system for sending messages between applications. It is
used both for the system wide message bus service, and as a
per-user-login-session messaging facility.

# Win32
%package -n mingw32-dbus
Summary:        MinGW Windows port of D-Bus
Requires:       pkgconfig
%description -n mingw32-dbus
D-BUS is a system for sending messages between applications. It is
used both for the system wide message bus service, and as a
per-user-login-session messaging facility.

%package -n mingw32-dbus-static
Summary:        Static version of MinGW Windows port of DBus library
Requires:       mingw32-dbus = %{version}-%{release}
%description -n mingw32-dbus-static
D-BUS is a system for sending messages between applications. It is
used both for the system wide message bus service, and as a
per-user-login-session messaging facility.

Static version of MinGW Windows port of DBus library

# Win64
%package -n mingw64-dbus
Summary:        MinGW Windows port of D-Bus
Requires:       pkgconfig
%description -n mingw64-dbus
D-BUS is a system for sending messages between applications. It is
used both for the system wide message bus service, and as a
per-user-login-session messaging facility.

%package -n mingw64-dbus-static
Summary:        Static version of MinGW Windows port of DBus library
Requires:       mingw64-dbus = %{version}-%{release}
%description -n mingw64-dbus-static
D-BUS is a system for sending messages between applications. It is
used both for the system wide message bus service, and as a
per-user-login-session messaging facility.

Static version of MinGW Windows port of DBus library

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir dbus-%{version}
%oreon_prep
%build

MINGW_BUILDDIR_SUFFIX=static %mingw_cmake -DDBUS_ENABLE_DOXYGEN_DOCS=OFF -DENABLE_QT_HELP=OFF -DBUILD_SHARED_LIBS=OFF
MINGW_BUILDDIR_SUFFIX=static %mingw_make_build
MINGW_BUILDDIR_SUFFIX=shared %mingw_cmake -DDBUS_ENABLE_DOXYGEN_DOCS=OFF -DENABLE_QT_HELP=OFF
MINGW_BUILDDIR_SUFFIX=shared %mingw_make_build
%install
MINGW_BUILDDIR_SUFFIX=static %mingw_make_install
MINGW_BUILDDIR_SUFFIX=shared %mingw_make_install
rm -rf %{buildroot}%{mingw32_datadir}/doc
rm -rf %{buildroot}%{mingw64_datadir}/doc
rm -rf %{buildroot}%{mingw32_datadir}/xml
rm -rf %{buildroot}%{mingw64_datadir}/xml
%oreon_autofiles mingw32-dbus usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-dbus-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-dbus usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-dbus-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-dbus -f %{oreon_filedir}/mingw32-dbus.list
%files -n mingw32-dbus-static -f %{oreon_filedir}/mingw32-dbus-static.list
%files -n mingw64-dbus -f %{oreon_filedir}/mingw64-dbus.list
%files -n mingw64-dbus-static -f %{oreon_filedir}/mingw64-dbus-static.list

%changelog

%autochangelog
