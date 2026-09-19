%global source0_hash 64f11d3b95a24e2a8d4166ecff518730f79ecc27222ef41faf7c7e0340fc9329

%{?mingw_package_header}

# first two digits of version
%global release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-glibmm24
Version:        2.66.8
Release:        3%{?dist}
Summary:        MinGW Windows C++ interface for GTK2 (a GUI library for X)

License:        LGPL-2.0-or-later
URL:            http://www.gtkmm.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/glibmm/%{release_version}/glibmm-%{version}.tar.xz
# Export Glib::Threads::wrap symbols (#2017676)
Patch0:         glibmm_export-symbols.patch

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  mingw32-libsigc++20 >= 2.0.0
BuildRequires:  mingw64-libsigc++20 >= 2.0.0
BuildRequires:  mingw32-glib2 >= 2.48.0
BuildRequires:  mingw64-glib2 >= 2.48.0

BuildRequires:  meson
BuildRequires:  perl
BuildRequires:  perl-Getopt-Long

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

%autosetup -p1 -n glibmm-%{version}

%build
%mingw_meson --default-library=both
%mingw_ninja

%install
%mingw_ninja_install

# Win32
%files -n mingw32-glibmm24
%license COPYING COPYING.tools
%{mingw32_bindir}/libgiomm-2.4-1.dll
%{mingw32_bindir}/libglibmm-2.4-1.dll
%{mingw32_bindir}/libglibmm_generate_extra_defs-2.4-1.dll
%{mingw32_libdir}/libgiomm-2.4.dll.a
%{mingw32_libdir}/libglibmm-2.4.dll.a
%{mingw32_libdir}/libglibmm_generate_extra_defs-2.4.dll.a
%{mingw32_libdir}/giomm-2.4
%{mingw32_libdir}/glibmm-2.4
%{mingw32_includedir}/giomm-2.4
%{mingw32_includedir}/glibmm-2.4
%{mingw32_libdir}/pkgconfig/giomm-2.4.pc
%{mingw32_libdir}/pkgconfig/glibmm-2.4.pc

%files -n mingw32-glibmm24-static
%{mingw32_libdir}/libgiomm-2.4.a
%{mingw32_libdir}/libglibmm-2.4.a
%{mingw32_libdir}/libglibmm_generate_extra_defs-2.4.a

# Win64
%files -n mingw64-glibmm24
%license COPYING COPYING.tools
%{mingw64_bindir}/libgiomm-2.4-1.dll
%{mingw64_bindir}/libglibmm-2.4-1.dll
%{mingw64_bindir}/libglibmm_generate_extra_defs-2.4-1.dll
%{mingw64_libdir}/libgiomm-2.4.dll.a
%{mingw64_libdir}/libglibmm-2.4.dll.a
%{mingw64_libdir}/libglibmm_generate_extra_defs-2.4.dll.a
%{mingw64_libdir}/giomm-2.4
%{mingw64_libdir}/glibmm-2.4
%{mingw64_includedir}/giomm-2.4
%{mingw64_includedir}/glibmm-2.4
%{mingw64_libdir}/pkgconfig/giomm-2.4.pc
%{mingw64_libdir}/pkgconfig/glibmm-2.4.pc

%files -n mingw64-glibmm24-static
%{mingw64_libdir}/libgiomm-2.4.a
%{mingw64_libdir}/libglibmm-2.4.a
%{mingw64_libdir}/libglibmm_generate_extra_defs-2.4.a

%changelog
%autochangelog
