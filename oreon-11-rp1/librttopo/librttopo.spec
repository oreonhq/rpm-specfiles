%global source0_hash 60b49acb493c1ab545116fb0b0d223ee115166874902ad8165eb39e9fd98eaa9

%bcond mingw    %{defined fedora}

Name:           librttopo
Version:        1.1.0
Release:        20%{?dist}
Summary:        Create and manage SQL/MM topologies

License:        GPL-2.0-or-later
URL:            https://git.osgeo.org/gitea/rttopo/librttopo
Source0:        https://git.osgeo.org/gitea/rttopo/librttopo/archive/%{name}-%{version}.tar.gz
# Use pkgconfig to find geos
Patch0:        librttopo_geos.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}

%build
autoreconf -ifv

# Native build
mkdir build_native
pushd build_native
%global _configure ../configure
%configure --disable-static
%make_build
popd

%if %{with mingw}
# MinGW build
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
