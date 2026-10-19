%global source0_hash cc09a3ac41d60e6144e644bd3fcf97d47106d659c4a0b8965102581401e67c9c
%undefine __cmake_in_source_build
Summary:        Reference implementation of the iCalendar data type and serialization format
Name:		libical
Version:	4.0.5
Release:        1%{?dist}
License:	LGPL-2.1-only OR MPL-2.0
URL:		https://libical.github.io/libical/
Source0:        https://github.com/%{name}/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:	tzdata
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtk-doc
BuildRequires:  ninja-build
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(lib)
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  python3
BuildRequires:  python3-gobject
BuildRequires:  python3-pip
BuildRequires:  vala
# /oreon:deps
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
%oreon_prep
%build

%{cmake} \
  -DLIBICAL_GOBJECT_INTROSPECTION:BOOL=true \
  -DLIBICAL_GLIB:BOOL=true \
  -DLIBICAL_GLIB_VAPI:BOOL=true \
  -DLIBICAL_CXX_BINDINGS:BOOL=true
%cmake_build -j1
%install
%cmake_install
rm %{buildroot}/%{_libexecdir}/libical/ical-glib-src-generator
rm %{buildroot}/%{_libdir}/cmake/LibIcal/IcalGlibSrcGenerator.cmake
rm %{buildroot}/%{_libdir}/cmake/LibIcal/IcalGlibSrcGenerator-noconfig.cmake
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libical-devel -f %{oreon_filedir}/libical-devel.list
%files -n libical-glib -f %{oreon_filedir}/libical-glib.list
%files -n libical-glib-doc -f %{oreon_filedir}/libical-glib-doc.list
%files -n libical-glib-devel -f %{oreon_filedir}/libical-glib-devel.list

%changelog

%autochangelog
