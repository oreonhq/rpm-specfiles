# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash bc11ac297b3cb010be904c72789695543ee3fdf3d75cdc8225fd371385af4e61
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%if 0%{?oreon}
%bcond_with ecore
%else
%bcond_without ecore
%endif

Name:          dbus-c++
Version:       0.9.0
Release:       1%{?dist}
Summary:       Native C++ bindings for D-Bus

License:       LicenseRef-Callaway-LGPLv2+
URL:           http://sourceforge.net/projects/dbus-cplusplus/
Source0:       http://downloads.sourceforge.net/dbus-cplusplus/lib%{name}-%{version}.tar.gz

Patch1: dbus-c++-gcc4.7.patch
Patch2: dbus-c++-linkfix.patch
Patch3: dbus-c++-macro_collision.patch
Patch4: dbus-c++-threading.patch
Patch5: dbus-c++-writechar.patch
Patch6: dbus-c++-template-operators.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: dbus-devel
BuildRequires: glib2-devel
BuildRequires: gtkmm24-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: expat-devel
%if %{with ecore}
BuildRequires: ecore-devel
%endif
BuildRequires: make

%description
dbus-c++ attempts to provide a C++ API for D-Bus.
Subpackages are provided with mainloop integration.

%if %{with ecore}
%package       ecore
Summary:       Ecore library for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description   ecore
This package contains the ecore mainloop library for %{name}
%endif

%package       glib
Summary:       GLib library for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description   glib
This package contains the GLib mainloop library for %{name}

%package       devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      pkgconfig
%description   devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%oreon_sha256
%setup -q -n lib%{name}-%{version}
sed -i 's/\r//' AUTHORS
sed -i 's/libtoolize --force --copy/libtoolize -if --copy/' bootstrap
%patch -P1 -p1 -b .gcc47
%patch -P2 -p1 -b .linkfix
%patch -P3 -p1 -b .collision
%patch -P4 -p1 -b .threading
%patch -P5 -p1 -b .writechar
%patch -P6 -p1 -b .template-operators

%build
autoreconf -vfi
export CPPFLAGS='%{optflags}' CXXFLAGS='--std=gnu++11 %{optflags}'
%configure --disable-static --disable-tests \
%if %{without ecore}
           --disable-ecore
%else
  ;
%endif
%make_build

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -print -delete

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS
%{_bindir}/dbusxx-introspect
%{_bindir}/dbusxx-xml2cpp
%{_libdir}/libdbus-c++-1.so.0*

%if %{with ecore}
%files ecore
%{_libdir}/libdbus-c++-ecore-1.so.0*
%endif

%files glib
%{_libdir}/libdbus-c++-glib-1.so.0*

%files devel
%doc TODO
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%changelog
%autochangelog
