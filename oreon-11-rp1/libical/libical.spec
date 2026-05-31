%global source0_hash e73de92f5a6ce84c1b00306446b290a2b08cdf0a80988eca0a2c9d5c3510b4c2

%undefine __cmake_in_source_build

Summary:	Reference implementation of the iCalendar data type and serialization format
Name:		libical
Version:	3.0.20
Release:	%{autorelease}
License:	LGPL-2.1-only OR MPL-2.0
URL:		https://libical.github.io/libical/
Source:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	gtk-doc
BuildRequires:	ninja-build
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(icu-i18n)
BuildRequires:	pkgconfig(icu-uc)
BuildRequires:	perl(Getopt::Std)
BuildRequires:	perl(lib)
BuildRequires:	python3
BuildRequires:	python3-pip
BuildRequires:	python3-gobject
BuildRequires:	vala
Requires:	tzdata

%description
Reference implementation of the iCalendar data type and serialization format
used in dozens of calendaring and scheduling products.

%package devel
Summary:	Development files for libical
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The libical-devel package contains libraries and header files for developing
applications that use libical.

%package glib
Summary:	GObject wrapper for libical library
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description glib
This package provides a GObject wrapper for libical library with support
of GObject Introspection.

%package glib-doc
Summary:	Documentation files for %{name}-glib
BuildArch:	noarch

%description glib-doc
This package contains developer documentation for %{name}-glib.

%package glib-devel
Summary:	Development files for building against %{name}-glib
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}
Requires:	%{name}-glib%{?_isa} = %{version}-%{release}

%description glib-devel
Development files needed for building things which link against %{name}-glib.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -S gendiff

%build
%{cmake} \
  -DUSE_INTEROPERABLE_VTIMEZONES:BOOL=true \
  -DICAL_ALLOW_EMPTY_PROPERTIES:BOOL=true \
  -DGOBJECT_INTROSPECTION:BOOL=true \
  -DICAL_GLIB:BOOL=true \
  -DICAL_GLIB_VAPI:BOOL=true \
  -DSHARED_ONLY:BOOL=true

# avoid parallel-builds, gir generatation fails on slower archs
%cmake_build -j1

%install
%cmake_install

# This is just a private build tool, not meant to be installed
rm %{buildroot}/%{_libexecdir}/libical/ical-glib-src-generator
rm %{buildroot}/%{_libdir}/cmake/LibIcal/IcalGlibSrcGenerator.cmake
rm %{buildroot}/%{_libdir}/cmake/LibIcal/IcalGlibSrcGenerator-noconfig.cmake

%check
%ctest

%ldconfig_scriptlets

%files
%doc README.md ReleaseNotes.txt THANKS
%license LICENSE
%{_libdir}/libical.so.3
%{_libdir}/libical.so.%{version}
%{_libdir}/libical_cxx.so.3
%{_libdir}/libical_cxx.so.%{version}
%{_libdir}/libicalss.so.3
%{_libdir}/libicalss.so.%{version}
%{_libdir}/libicalss_cxx.so.3
%{_libdir}/libicalss_cxx.so.%{version}
%{_libdir}/libicalvcal.so.3
%{_libdir}/libicalvcal.so.%{version}
%{_libdir}/girepository-1.0/ICal-3.0.typelib

%files devel
%doc doc/UsingLibical.md
%{_libdir}/libical.so
%{_libdir}/libical_cxx.so
%{_libdir}/libicalss.so
%{_libdir}/libicalss_cxx.so
%{_libdir}/libicalvcal.so
%{_libdir}/pkgconfig/libical.pc
%{_libdir}/cmake/LibIcal/
%{_includedir}/libical/
%{_datadir}/gir-1.0/ICal-3.0.gir

%ldconfig_scriptlets glib

%files glib
%{_libdir}/libical-glib.so.3
%{_libdir}/libical-glib.so.%{version}
%{_libdir}/girepository-1.0/ICalGLib-3.0.typelib

%files glib-devel
%{_libdir}/libical-glib.so
%{_libdir}/pkgconfig/libical-glib.pc
%{_includedir}/libical-glib/
%{_datadir}/gir-1.0/ICalGLib-3.0.gir
%{_datadir}/vala/vapi/libical-glib.vapi

%files glib-doc
%{_datadir}/gtk-doc/html/%{name}-glib

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.20-1
- Prepare for Oreon 11 (RP1)
