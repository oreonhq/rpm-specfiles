%global source0_hash 7ab7e2266808716e26c39924ace1fb46da86c17ef39d989624c42314b32b5a76

%{?mingw_package_header}

# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-gtkmm30
Version:        3.24.10
Release:        3%{?dist}
Summary:        MinGW Windows C++ interface for the GTK+ library

License:        LGPL-2.0-or-later
URL:            http://www.gtkmm.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/gtkmm/%{release_version}/gtkmm-%{version}.tar.xz

BuildArch:      noarch

# For glib-compile-resources
BuildRequires:  glib2-devel
# For gdk-pixbuf-pixdata
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  meson

BuildRequires:  mingw32-atkmm
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-cairomm
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-glibmm24
BuildRequires:  mingw32-gtk3
BuildRequires:  mingw32-pangomm

BuildRequires:  mingw64-atkmm
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-cairomm
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-glibmm24
BuildRequires:  mingw64-gtk3
BuildRequires:  mingw64-pangomm

%description
gtkmm is the official C++ interface for the popular GUI library GTK+.
Highlights include type safe callbacks, and a comprehensive set of
widgets that are easily extensible via inheritance.

This package contains the MinGW Windows cross compiled gtkmm library,
API version 3.0.

%package -n mingw32-gtkmm30
Summary:        MinGW Windows C++ interface for the GTK+ library

%description -n mingw32-gtkmm30
gtkmm is the official C++ interface for the popular GUI library GTK+.
Highlights include type safe callbacks, and a comprehensive set of
widgets that are easily extensible via inheritance.

This package contains the MinGW Windows cross compiled gtkmm library,
API version 3.0.

%package -n mingw64-gtkmm30
Summary:        MinGW Windows C++ interface for the GTK+ library

%description -n mingw64-gtkmm30
gtkmm is the official C++ interface for the popular GUI library GTK+.
Highlights include type safe callbacks, and a comprehensive set of
widgets that are easily extensible via inheritance.

This package contains the MinGW Windows cross compiled gtkmm library,
API version 3.0.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n gtkmm-%{version}

%build
%mingw_meson -Dbuild-demos=false -Dbuild-tests=false
%mingw_ninja

%install
%mingw_ninja_install

%files -n mingw32-gtkmm30
%license COPYING
%{mingw32_bindir}/libgdkmm-3.0-1.dll
%{mingw32_bindir}/libgtkmm-3.0-1.dll
%{mingw32_libdir}/libgdkmm-3.0.dll.a
%{mingw32_libdir}/libgtkmm-3.0.dll.a
%{mingw32_includedir}/gdkmm-3.0/
%{mingw32_includedir}/gtkmm-3.0/
%{mingw32_libdir}/gdkmm-3.0/
%{mingw32_libdir}/gtkmm-3.0/
%{mingw32_libdir}/pkgconfig/gdkmm-3.0.pc
%{mingw32_libdir}/pkgconfig/gtkmm-3.0.pc

%files -n mingw64-gtkmm30
%license COPYING
%{mingw64_bindir}/libgdkmm-3.0-1.dll
%{mingw64_bindir}/libgtkmm-3.0-1.dll
%{mingw64_libdir}/libgdkmm-3.0.dll.a
%{mingw64_libdir}/libgtkmm-3.0.dll.a
%{mingw64_includedir}/gdkmm-3.0/
%{mingw64_includedir}/gtkmm-3.0/
%{mingw64_libdir}/gdkmm-3.0/
%{mingw64_libdir}/gtkmm-3.0/
%{mingw64_libdir}/pkgconfig/gdkmm-3.0.pc
%{mingw64_libdir}/pkgconfig/gtkmm-3.0.pc

%changelog
%autochangelog
