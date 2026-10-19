%global source0_hash c59932395e98896038d59199f2e2453595df6d730ffbe09d69df2a661bcb619b
%{?mingw_package_header}
%global pkgname spatialindex
Name:          mingw-%{pkgname}
Version:       2.1.0
Release:        1%{?dist}
Summary:        MinGW Windows spatialindex library
BuildArch:     noarch
License:       MIT
URL:           http://libspatialindex.org
Source0:        https://github.com/libspatialindex/libspatialindex/releases/download/%{version}/spatialindex-src-%{version}.tar.bz2
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
MinGW Windows %{pkgname} library.

%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library
%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname} library.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}-src-%{version}

%build

%mingw_cmake -DSIDX_BIN_SUBDIR=bin .
%mingw_make_build
%install
%mingw_make_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-spatialindex -f %{oreon_filedir}/mingw32-spatialindex.list
%files -n mingw64-spatialindex -f %{oreon_filedir}/mingw64-spatialindex.list

%changelog

%autochangelog
