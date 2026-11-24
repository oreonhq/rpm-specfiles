# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 2e2fcabb48193a712a6c76ac9a9be2a53f82e32f91a2bc834d9f1b4fa9cd879f
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond mingw    %{defined fedora}

Name:           librttopo
Version:        1.1.0
Release:        1%{?dist}
Summary:        Create and manage SQL/MM topologies

License:        GPL-2.0-or-later
URL:            https://git.osgeo.org/gitea/rttopo/librttopo
Source0:        https://git.osgeo.org/gitea/rttopo/librttopo/archive/%{name}-%{version}.tar.gz
Patch0:        librttopo_geos.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: geos-devel
BuildRequires: libtool
BuildRequires: make

%if %{with mingw}
BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc
BuildRequires: mingw32-geos

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc
BuildRequires: mingw64-geos
%endif

%description
The RT Topology Library exposes an API to create and manage standard
(ISO 13249 aka SQL/MM) topologies using user-provided data stores.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if %{with mingw}
%package -n mingw32-%{name}
Summary:       MinGW Windows Leptonica library
BuildArch:     noarch

%description -n mingw32-%{name}
MinGW Windows %{name} library.

%package -n mingw64-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw64-%{name}
MinGW Windows %{name} library.

%{?mingw_debug_package}
%endif

%prep
%oreon_sha256
%autosetup -p1 -n %{name}

%build
autoreconf -ifv

mkdir build_native
pushd build_native
%global _configure ../configure
%configure --disable-static
%make_build
popd

%if %{with mingw}
MINGW32_CONFIGURE_ARGS="PKGCONFIG=%{mingw32_target}-pkg-config" \
MINGW64_CONFIGURE_ARGS="PKGCONFIG=%{mingw64_target}-pkg-config" \
%mingw_configure  --disable-static
%mingw_make_build
%endif

%install
%make_install -C build_native

%if %{with mingw}
%mingw_make_install
%endif

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%if %{with mingw}
%mingw_debug_install_post
%endif

%files
%license COPYING
%doc CREDITS NEWS.md README.md TODO
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/%{name}.h
%{_includedir}/%{name}_geom.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/rttopo.pc

%if %{with mingw}
%files -n mingw32-%{name}
%license COPYING
%{mingw32_bindir}/%{name}-1.dll
%{mingw32_includedir}/%{name}.h
%{mingw32_includedir}/%{name}_geom.h
%{mingw32_libdir}/%{name}.dll.a
%{mingw32_libdir}/pkgconfig/rttopo.pc

%files -n mingw64-%{name}
%license COPYING
%{mingw64_bindir}/%{name}-1.dll
%{mingw64_includedir}/%{name}.h
%{mingw64_includedir}/%{name}_geom.h
%{mingw64_libdir}/%{name}.dll.a
%{mingw64_libdir}/pkgconfig/rttopo.pc
%endif

%changelog
%autochangelog
