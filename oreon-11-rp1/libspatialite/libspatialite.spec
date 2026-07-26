%global source0_hash 43be2dd349daffe016dd1400c5d11285828c22fea35ca5109f21f3ed50605080

%if 0%{?rhel} >= 9
%bcond_with mingw
%else
%bcond_without mingw
%endif

Name:          libspatialite
Version:       5.1.0
Release:       12%{?dist}
Summary:       Enables SQLite to support spatial data

License:       MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.0-or-later
URL:           https://www.gaia-gis.it/fossil/libspatialite
Source0:       http://www.gaia-gis.it/gaia-sins/libspatialite-sources/libspatialite-%{version}.tar.gz

# Move private libs to Libs.private in pkg-config file (#1926868)
Patch0:        libspatialite_pkgconfig.patch
# Fix mingw detection in configure.ac
Patch1:        libspatialite_mingw.patch
# Use pkgconfig to find geos
Patch2:        libspatialite_geos.patch
# Fix incompatibile pointer types
Patch3:        libspatialite_incompat-ptrs.patch

BuildRequires: autoconf automake libtool
BuildRequires: freexl-devel
BuildRequires: gcc
BuildRequires: geos-devel >= 3.7.1
BuildRequires: librttopo-devel
BuildRequires: libxml2-devel
BuildRequires: make
BuildRequires: minizip-ng-compat-devel
BuildRequires: proj-devel >= 6.2.0
BuildRequires: sqlite-devel
BuildRequires: zlib-devel

%if %{with mingw}
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-freexl
BuildRequires: mingw32-gcc
BuildRequires: mingw32-geos
BuildRequires: mingw32-libcharset
BuildRequires: mingw32-librttopo
BuildRequires: mingw32-libxml2
BuildRequires: mingw32-minizip
BuildRequires: mingw32-proj
BuildRequires: mingw32-sqlite
BuildRequires: mingw32-zlib

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-freexl
BuildRequires: mingw64-gcc
BuildRequires: mingw64-geos
BuildRequires: mingw64-libcharset
BuildRequires: mingw64-librttopo
BuildRequires: mingw64-libxml2
BuildRequires: mingw64-minizip
BuildRequires: mingw64-proj
BuildRequires: mingw64-sqlite
BuildRequires: mingw64-zlib
%endif

%description
SpatiaLite is a a library extending the basic SQLite core in order to
get a full fledged Spatial DBMS, really simple and lightweight, but
mostly OGC-SFS compliant.

%package devel
Summary:	Development libraries and headers for SpatiaLite
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if %{with mingw}
%package -n mingw32-%{name}
Summary:       MinGW Windows libspatialite library
BuildArch:     noarch

%description -n mingw32-%{name}
MinGW Windows libspatialite library.

%package -n mingw64-%{name}
Summary:       MinGW Windows libspatialite library
BuildArch:     noarch

%description -n mingw64-%{name}
MinGW Windows libspatialite library.

%{?mingw_debug_package}
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}
autoreconf -ifv

# Need to copy testdata into builddir
mkdir build_native
cp -a test build_native

%build
# Native build
pushd build_native
%global _configure ../configure
%configure \
    --disable-static \
    --enable-geocallbacks   \
    --enable-rttopo \
    --enable-gcp
%make_build
popd

%if %{with mingw}
# MinGW build
%mingw_configure --disable-static
%mingw_make_build
%endif

%install
%make_install -C build_native
%if %{with mingw}
%mingw_make_install
%endif

find %{buildroot} -type f -name "*.la" -delete

%if %{with mingw}
%mingw_debug_install_post
%endif

%check
make check  -C build_native %{?_smp_mflags} || :

%files
%doc AUTHORS
%license COPYING
%{_libdir}/%{name}.so.8*
%{_libdir}/mod_spatialite.so.8*
# The symlink must be present to allow loading the extension
# https://groups.google.com/forum/#!topic/spatialite-users/zkGP-gPByXk
%{_libdir}/mod_spatialite.so

%files devel
%doc examples/*.c
%{_includedir}/spatialite.h
%{_includedir}/spatialite
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/spatialite.pc

%if %{with mingw}
%files -n mingw32-%{name}
%license COPYING
%{mingw32_bindir}/libspatialite-5.dll
%{mingw32_includedir}/spatialite.h
%{mingw32_includedir}/spatialite/
%{mingw32_libdir}/libspatialite.dll.a
%{mingw32_libdir}/mod_spatialite.dll*
%{mingw32_libdir}/pkgconfig/spatialite.pc

%files -n mingw64-%{name}
%license COPYING
%{mingw64_bindir}/libspatialite-5.dll
%{mingw64_includedir}/spatialite.h
%{mingw64_includedir}/spatialite/
%{mingw64_libdir}/libspatialite.dll.a
%{mingw64_libdir}/mod_spatialite.dll*
%{mingw64_libdir}/pkgconfig/spatialite.pc
%endif

%changelog
%autochangelog
