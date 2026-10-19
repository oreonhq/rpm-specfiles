%global source0_hash ce573bbea8e75b429f8c3d3e86498741ba3dc9628a1530d2f65268397ad059e8
%{?mingw_package_header}
%global pkgname cfitsio
Name:          mingw-%{pkgname}
Version:       4.7.0
Release:        1%{?dist}
Summary:        MinGW Windows CFITSIO library
License:       CFITSIO
BuildArch:     noarch
URL:           https://heasarc.gsfc.nasa.gov/fitsio/
Source0:        https://heasarc.gsfc.nasa.gov/FTP/software/fitsio/c/%{pkgname}-%{version}.tar.gz
Patch0:        cfitsio_cmake.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  mingw32-curl
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-curl
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-zlib
# /oreon:deps
%description
MinGW Windows CFITSIO library.

%package -n mingw32-%{pkgname}
Summary:       MinGW Windows CFITSIO library
%description -n mingw32-%{pkgname}
MinGW Windows CFITSIO library.

%package -n mingw32-%{pkgname}-tools
Summary:       MinGW Windows CFITSIO library
%description -n mingw32-%{pkgname}-tools
MinGW Windows CFITSIO library.

%package -n mingw64-%{pkgname}
Summary:       MinGW Windows CFITSIO library
%description -n mingw64-%{pkgname}
MinGW Windows CFITSIO library.

%package -n mingw64-%{pkgname}-tools
Summary:       MinGW Windows CFITSIO library
%description -n mingw64-%{pkgname}-tools
MinGW Windows CFITSIO library.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}-%{version}

%build

%mingw_cmake -DUTILS=ON -DCMAKE_DLL_NAME_WITH_SOVERSION=ON -DTESTS=OFF
%mingw_make_build
%install
%mingw_make_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-cfitsio -f %{oreon_filedir}/mingw32-cfitsio.list
%files -n mingw32-cfitsio-tools -f %{oreon_filedir}/mingw32-cfitsio-tools.list
%files -n mingw64-cfitsio -f %{oreon_filedir}/mingw64-cfitsio.list
%files -n mingw64-cfitsio-tools -f %{oreon_filedir}/mingw64-cfitsio-tools.list

%changelog

%autochangelog
