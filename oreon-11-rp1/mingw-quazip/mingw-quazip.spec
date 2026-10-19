%global source0_hash 405b72b6e76c8987ff41a762523b8f64876ba406d8a831d268ee0b63f1369582
%{?mingw_package_header}
%global pkgname quazip
Name:          mingw-%{pkgname}
Version:       1.5
Release:        2%{?dist}
Summary:        MinGW Windows quazip library
BuildArch:     noarch
License:       ( LGPL-2.1-or-later WITH Qwt-exception-1.0 ) AND Zlib
URL:           https://stachenov.github.io/quazip/
Source0:        https://github.com/stachenov/%{pkgname}/archive/v%{version}/%{pkgname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-libzip
BuildRequires:  mingw32-qt5-qtbase
BuildRequires:  mingw32-qt6-qt5compat
BuildRequires:  mingw32-qt6-qtbase
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-libzip
BuildRequires:  mingw64-qt5-qtbase
BuildRequires:  mingw64-qt6-qt5compat
BuildRequires:  mingw64-qt6-qtbase
# /oreon:deps
%description
MinGW Windows %{pkgname} library.

%package -n mingw32-%{pkgname}-qt5
Summary:       MinGW Windows Qt5 %{pkgname} library
Obsoletes:     mingw32-%{pkgname}-qt5-static
%description -n mingw32-%{pkgname}-qt5
MinGW Windows Qt5 %{pkgname} library.

%package -n mingw32-%{pkgname}-qt6
Summary:       MinGW Windows Qt6 %{pkgname} library
%description -n mingw32-%{pkgname}-qt6
MinGW Windows Qt6 %{pkgname} library.

%package -n mingw64-%{pkgname}-qt5
Summary:       MinGW Windows Qt5 %{pkgname} library
Obsoletes:     mingw64-%{pkgname}-qt5-static
%description -n mingw64-%{pkgname}-qt5
MinGW Windows Qt5 %{pkgname} library.

%package -n mingw64-%{pkgname}-qt6
Summary:       MinGW Windows Qt6 %{pkgname} library
%description -n mingw64-%{pkgname}-qt6
MinGW Windows Qt6 %{pkgname} library.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}-%{version}

%build

export MINGW32_CXXFLAGS="%{mingw32_cflags} -msse2"
export MINGW64_CXXFLAGS="%{mingw64_cflags} -msse2"
mkdir build_qt5
pushd build_qt5
%mingw_cmake -DQUAZIP_QT_MAJOR_VERSION=5 -DQT_INCLUDE_DIRS_NO_SYSTEM=ON ../..
%mingw_make_build
popd
mkdir build_qt6
pushd build_qt6
%mingw_cmake -DQUAZIP_QT_MAJOR_VERSION=6 -DQT_INCLUDE_DIRS_NO_SYSTEM=ON ../..
%mingw_make_build
popd
%install
pushd build_qt5
%mingw_make_install
popd
pushd build_qt6
%mingw_make_install
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-quazip-qt5 -f %{oreon_filedir}/mingw32-quazip-qt5.list
%files -n mingw32-quazip-qt6 -f %{oreon_filedir}/mingw32-quazip-qt6.list
%files -n mingw64-quazip-qt5 -f %{oreon_filedir}/mingw64-quazip-qt5.list
%files -n mingw64-quazip-qt6 -f %{oreon_filedir}/mingw64-quazip-qt6.list

%changelog

%autochangelog
