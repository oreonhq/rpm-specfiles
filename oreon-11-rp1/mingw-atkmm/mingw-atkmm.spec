%global source0_hash ae449192a582a2582a95e0602b15d792bbd639e836339b81ef916aa87540ac5c
%{?mingw_package_header}
Name:           mingw-atkmm
Version:        2.28.5
Release:        1%{?dist}
Summary:        MinGW Windows C++ interface for the ATK library
License:        LGPL-2.0-or-later
URL:            http://www.gtkmm.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/atkmm/2.28/atkmm-%{version}.tar.xz
BuildArch:      noarch
# oreon:deps
BuildRequires:  meson
BuildRequires:  mingw32-atk
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-glibmm24
BuildRequires:  mingw32-libsigc++20
BuildRequires:  mingw64-atk
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-glibmm24
BuildRequires:  mingw64-libsigc++20
# /oreon:deps
%description
atkmm provides a C++ interface for the ATK library. Highlights
include type-safe callbacks, widgets extensible via inheritance and a
comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

%package -n mingw32-atkmm
Summary:        MinGW Windows C++ interface for the ATK library
Conflicts:      mingw32-gtkmm24 < 2.21.1
Obsoletes:      mingw32-atkmm-static < 2.22.6-3
Provides:       mingw32-atkmm-static = 2.22.6-3
%description -n mingw32-atkmm
atkmm provides a C++ interface for the ATK library. Highlights
include type-safe callbacks, widgets extensible via inheritance and a
comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

%package -n mingw64-atkmm
Summary:        MinGW Windows C++ interface for the ATK library
Obsoletes:      mingw64-atkmm-static < 2.22.6-3
Provides:       mingw64-atkmm-static = 2.22.6-3
%description -n mingw64-atkmm
atkmm provides a C++ interface for the ATK library. Highlights
include type-safe callbacks, widgets extensible via inheritance and a
comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir atkmm-%{version}
%oreon_prep
%build

%mingw_meson
%mingw_ninja
%install
%mingw_ninja_install
%oreon_autofiles mingw32-atkmm usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-atkmm usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-atkmm -f %{oreon_filedir}/mingw32-atkmm.list
%files -n mingw64-atkmm -f %{oreon_filedir}/mingw64-atkmm.list

%changelog

%autochangelog
