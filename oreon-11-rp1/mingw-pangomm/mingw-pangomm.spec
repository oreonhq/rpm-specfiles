%global source0_hash b92016661526424de4b9377f1512f59781f41fb16c9c0267d6133ba1cd68db22
%{?mingw_package_header}
%global apiver 1.4
%global release_version %(echo %{version} | awk -F. '{print $1"."$2}')
Name:           mingw-pangomm
Version:        2.46.4
Release:        1%{?dist}
Summary:        MinGW Windows C++ interface for Pango
License:        LGPL-2.0-or-later
URL:            http://gtkmm.sourceforge.net/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/pangomm/%{release_version}/pangomm-%{version}.tar.xz
BuildArch:      noarch
# oreon:deps
BuildRequires:  meson
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-cairomm
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-glibmm24
BuildRequires:  mingw32-pango
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-cairomm
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-glibmm24
BuildRequires:  mingw64-pango
# /oreon:deps
%description
pangomm provides a C++ interface to the Pango library. Highlights
include typesafe callbacks, widgets extensible via inheritance and a
comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

%package -n mingw32-pangomm
Summary:        MinGW Windows C++ interface for Pango
Obsoletes:      mingw32-pangomm-static < 2.28.4-3
Provides:       mingw32-pangomm-static = 2.28.4-3
%description -n mingw32-pangomm
pangomm provides a C++ interface to the Pango library. Highlights
include typesafe callbacks, widgets extensible via inheritance and a
comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

%package -n mingw64-pangomm
Summary:        MinGW Windows C++ interface for Pango
Obsoletes:      mingw64-pangomm-static < 2.28.4-3
Provides:       mingw64-pangomm-static = 2.28.4-3
%description -n mingw64-pangomm
pangomm provides a C++ interface to the Pango library. Highlights
include typesafe callbacks, widgets extensible via inheritance and a
comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pangomm-%{version}
%oreon_prep
%build

%mingw_meson
%mingw_ninja
%install
%mingw_ninja_install
%oreon_autofiles mingw32-pangomm usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-pangomm usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-pangomm -f %{oreon_filedir}/mingw32-pangomm.list
%files -n mingw64-pangomm -f %{oreon_filedir}/mingw64-pangomm.list

%changelog

%autochangelog
