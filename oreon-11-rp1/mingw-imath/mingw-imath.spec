%global source0_hash e10c12b3f21f45bf08e09d4215d9c7691368d747beebd840de0b6fefed2df9f8
%{?mingw_package_header}
%global pkgname imath
Name:          mingw-%{pkgname}
Version:       3.2.3
Release:        1%{?dist}
Summary:        MinGW Windows imath library
License:       BSD-3-Clause
URL:           http://www.openexr.com/
BuildArch:     noarch
Source0:        https://github.com/AcademySoftwareFoundation/Imath/archive/v%{version}/%{pkgname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
# /oreon:deps
%description
MinGW Windows %{pkgname} library.

%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library
%description -n mingw32-%{pkgname}
%{summary}.

%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library
%description -n mingw64-%{pkgname}
%{summary}.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Imath-%{version}
%oreon_prep
%build

%mingw_cmake -DIMATH_INSTALL_PKG_CONFIG=ON -DBUILD_TESTING=OFF
%mingw_make_build
%install
%mingw_make_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-imath -f %{oreon_filedir}/mingw32-imath.list
%files -n mingw64-imath -f %{oreon_filedir}/mingw64-imath.list

%changelog

%autochangelog
