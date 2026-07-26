%global source0_hash 0a142a8128f83c001efb8014ee463e9a766054ef84686af953135e04d28fdab3

%{?mingw_package_header}

Name:           mingw-atkmm
Version:        2.28.4
Release:        5%{?dist}
Summary:        MinGW Windows C++ interface for the ATK library

License:        LGPL-2.0-or-later
URL:            http://www.gtkmm.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/atkmm/2.28/atkmm-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  meson

BuildRequires:  mingw32-atk
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-glibmm24 >= 2.24
BuildRequires:  mingw32-libsigc++20

BuildRequires:  mingw64-atk
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-glibmm24 >= 2.24
BuildRequires:  mingw64-libsigc++20

%description
atkmm provides a C++ interface for the ATK library. Highlights
include type-safe callbacks, widgets extensible via inheritance and a
comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

%package -n mingw32-atkmm
Summary:        MinGW Windows C++ interface for the ATK library
# mingw32-atkmm files used to be part of mingw32-gtkmm24
Conflicts:      mingw32-gtkmm24 < 2.21.1

# Fix upgrade path for people who are upgrading from the mingw-w64 testing repo
Obsoletes:      mingw32-atkmm-static < 2.22.6-3
Provides:       mingw32-atkmm-static = 2.22.6-3

%description -n mingw32-atkmm
atkmm provides a C++ interface for the ATK library. Highlights
include type-safe callbacks, widgets extensible via inheritance and a
comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

%package -n mingw64-atkmm
Summary:        MinGW Windows C++ interface for the ATK library

# Fix upgrade path for people who are upgrading from the mingw-w64 testing repo
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

%autosetup -p1 -n atkmm-%{version}

%build
%mingw_meson
%mingw_ninja

%install
%mingw_ninja_install

%files -n mingw32-atkmm
%license COPYING
%{mingw32_includedir}/atkmm-1.6
%{mingw32_libdir}/atkmm-1.6
%{mingw32_libdir}/pkgconfig/atkmm-1.6.pc
%{mingw32_libdir}/libatkmm-1.6.dll.a
%{mingw32_bindir}/libatkmm-1.6-1.dll

%files -n mingw64-atkmm
%license COPYING
%{mingw64_includedir}/atkmm-1.6
%{mingw64_libdir}/atkmm-1.6
%{mingw64_libdir}/pkgconfig/atkmm-1.6.pc
%{mingw64_libdir}/libatkmm-1.6.dll.a
%{mingw64_bindir}/libatkmm-1.6-1.dll

%changelog
%autochangelog
