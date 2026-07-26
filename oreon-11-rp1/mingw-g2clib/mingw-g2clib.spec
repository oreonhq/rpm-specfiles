%global source0_hash 8520a24c066500cfd0d07a05c6b7b0cb92383d1a4737cf6e79d9f4919c8e79ab

%{?mingw_package_header}

%global pkgname g2clib

Name:          mingw-%{pkgname}
Version:       2.3.0
Release:       2%{?dist}
Summary:       MinGW Windows g2clib library

BuildArch:     noarch
License:       LGPL-3.0-only
URL:           https://github.com/NOAA-EMC/NCEPLIBS-g2c
Source0:       https://github.com/NOAA-EMC/NCEPLIBS-g2c/archive/v%{version}/%{pkgname}-%{version}.tar.gz
# Add missing link libs
Patch0:        g2clib-linklibs-patch

BuildRequires: cmake

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-jasper
BuildRequires: mingw32-libpng
BuildRequires: mingw32-openjpeg

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-jasper
BuildRequires: mingw64-libpng
BuildRequires: mingw64-openjpeg

%description
MinGW Windows g2clib library.

%package -n mingw32-%{pkgname}
Summary:       MinGW Windows g2clib library

%description -n mingw32-%{pkgname}
MinGW Windows g2clib library.

%package -n mingw64-%{pkgname}
Summary:       MinGW Windows g2clib library

%description -n mingw64-%{pkgname}
MinGW Windows g2clib library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n NCEPLIBS-g2c-%{version}

%build
%mingw_cmake -DBUILD_STATIC_LIBS=OFF
%mingw_make_build

%install
%mingw_make_install

%files -n mingw32-%{pkgname}
%license LICENSE.md
%{mingw32_bindir}/g2c_compare.exe
%{mingw32_bindir}/g2c_degrib2.exe
%{mingw32_bindir}/g2c_index.exe
%{mingw32_bindir}/libg2c.dll
%{mingw32_libdir}/libg2c.dll.a
%{mingw32_libdir}/cmake/g2c/
%{mingw32_includedir}/grib2.h
%{mingw32_datadir}/g2c/

%files -n mingw64-%{pkgname}
%license LICENSE.md
%{mingw64_bindir}/g2c_compare.exe
%{mingw64_bindir}/g2c_degrib2.exe
%{mingw64_bindir}/g2c_index.exe
%{mingw64_bindir}/libg2c.dll
%{mingw64_libdir}/libg2c.dll.a
%{mingw64_libdir}/cmake/g2c/
%{mingw64_includedir}/grib2.h
%{mingw64_datadir}/g2c/

%changelog
%autochangelog
