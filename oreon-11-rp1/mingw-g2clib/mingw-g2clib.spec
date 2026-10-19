%global source0_hash 8520a24c066500cfd0d07a05c6b7b0cb92383d1a4737cf6e79d9f4919c8e79ab
%{?mingw_package_header}
%global pkgname g2clib
Name:          mingw-%{pkgname}
Version:       2.3.0
Release:        1%{?dist}
Summary:        MinGW Windows g2clib library
BuildArch:     noarch
License:       LGPL-3.0-only
URL:           https://github.com/NOAA-EMC/NCEPLIBS-g2c
Source0:        https://github.com/NOAA-EMC/NCEPLIBS-g2c/archive/v%{version}/%{pkgname}-%{version}.tar.gz
Patch0:        g2clib-linklibs-patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-jasper
BuildRequires:  mingw32-libpng
BuildRequires:  mingw32-openjpeg
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-jasper
BuildRequires:  mingw64-libpng
BuildRequires:  mingw64-openjpeg
# /oreon:deps
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
%global oreon_srcdir NCEPLIBS-g2c-%{version}
%oreon_prep
%build

%mingw_cmake -DBUILD_STATIC_LIBS=OFF
%mingw_make_build
%install
%mingw_make_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-g2clib -f %{oreon_filedir}/mingw32-g2clib.list
%files -n mingw64-g2clib -f %{oreon_filedir}/mingw64-g2clib.list

%changelog

%autochangelog
