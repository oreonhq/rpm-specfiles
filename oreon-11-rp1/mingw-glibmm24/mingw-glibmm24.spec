%global source0_hash 64f11d3b95a24e2a8d4166ecff518730f79ecc27222ef41faf7c7e0340fc9329
%{?mingw_package_header}
%global release_version %(echo %{version} | awk -F. '{print $1"."$2}')
Name:           mingw-glibmm24
Version:        2.66.8
Release:        1%{?dist}
Summary:        MinGW Windows C++ interface for GTK2 (a GUI library for X)
License:        LGPL-2.0-or-later
URL:            http://www.gtkmm.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/glibmm/%{release_version}/glibmm-%{version}.tar.xz
Patch0:         glibmm_export-symbols.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  meson
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-libsigc++20
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-libsigc++20
BuildRequires:  perl
BuildRequires:  perl-Getopt-Long
# /oreon:deps
%description
glibmm provides a C++ interface to the GTK+ GLib low-level core
library. Highlights include typesafe callbacks, widgets extensible via
inheritance and a comprehensive set of widget classes that can be
freely combined to quickly create complex user interfaces.

# Win32
%package -n mingw32-glibmm24
Summary:        MinGW Windows C++ interface for GTK2 (a GUI library for X)
%description -n mingw32-glibmm24
glibmm provides a C++ interface to the GTK+ GLib low-level core
library. Highlights include typesafe callbacks, widgets extensible via
inheritance and a comprehensive set of widget classes that can be
freely combined to quickly create complex user interfaces.

%package -n mingw32-glibmm24-static
Summary:        Static cross compiled version of the glibmm library
Requires:       mingw32-glibmm24 = %{version}-%{release}
%description -n mingw32-glibmm24-static
Static cross compiled version of the glibmm library.

# Win64
%package -n mingw64-glibmm24
Summary:        MinGW Windows C++ interface for GTK2 (a GUI library for X)
%description -n mingw64-glibmm24
glibmm provides a C++ interface to the GTK+ GLib low-level core
library. Highlights include typesafe callbacks, widgets extensible via
inheritance and a comprehensive set of widget classes that can be
freely combined to quickly create complex user interfaces.

%package -n mingw64-glibmm24-static
Summary:        Static cross compiled version of the glibmm library
Requires:       mingw64-glibmm24 = %{version}-%{release}
%description -n mingw64-glibmm24-static
Static cross compiled version of the glibmm library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir glibmm-%{version}
%oreon_prep
%build

%mingw_meson --default-library=both
%mingw_ninja
%install
%mingw_ninja_install
%oreon_autofiles mingw32-glibmm24 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-glibmm24-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-glibmm24 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-glibmm24-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-glibmm24 -f %{oreon_filedir}/mingw32-glibmm24.list
%files -n mingw32-glibmm24-static -f %{oreon_filedir}/mingw32-glibmm24-static.list
%files -n mingw64-glibmm24 -f %{oreon_filedir}/mingw64-glibmm24.list
%files -n mingw64-glibmm24-static -f %{oreon_filedir}/mingw64-glibmm24-static.list

%changelog

%autochangelog
