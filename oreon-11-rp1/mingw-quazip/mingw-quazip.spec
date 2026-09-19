%global source0_hash 405b72b6e76c8987ff41a762523b8f64876ba406d8a831d268ee0b63f1369582

%{?mingw_package_header}

%global pkgname quazip

Name:          mingw-%{pkgname}
Version:       1.5
Release:       2%{?dist}
Summary:       MinGW Windows %{pkgname} library

BuildArch:     noarch
# Following files are zlib licensed:
#  - quazip/unzip.c
#  - quazip/unzip.h
#  - quazip/zip.c
#  - quazip/zip.h
# Rest is LGPLv2 with a static linking exception, see COPYING
License:       ( LGPL-2.1-or-later WITH Qwt-exception-1.0 ) AND Zlib
URL:           https://stachenov.github.io/quazip/
Source:        https://github.com/stachenov/quazip/archive/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires: make
BuildRequires: cmake

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-qt5-qtbase
BuildRequires: mingw32-qt6-qtbase
BuildRequires: mingw32-qt6-qt5compat
BuildRequires: mingw32-libzip

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-qt5-qtbase
BuildRequires: mingw64-qt6-qtbase
BuildRequires: mingw64-qt6-qt5compat
BuildRequires: mingw64-libzip

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

%files -n mingw32-%{pkgname}-qt5
%license COPYING
%{mingw32_bindir}/libquazip1-qt5.dll
%{mingw32_includedir}/QuaZip-Qt5-%{version}/
%{mingw32_libdir}/libquazip1-qt5.dll.a
%{mingw32_libdir}/pkgconfig/quazip1-qt5.pc
%{mingw32_libdir}/cmake/QuaZip-Qt5-%{version}/

%files -n mingw32-%{pkgname}-qt6
%license COPYING
%{mingw32_bindir}/libquazip1-qt6.dll
%{mingw32_includedir}/QuaZip-Qt6-%{version}/
%{mingw32_libdir}/libquazip1-qt6.dll.a
%{mingw32_libdir}/pkgconfig/quazip1-qt6.pc
%{mingw32_libdir}/cmake/QuaZip-Qt6-%{version}/

%files -n mingw64-%{pkgname}-qt5
%license COPYING
%{mingw64_bindir}/libquazip1-qt5.dll
%{mingw64_includedir}/QuaZip-Qt5-%{version}/
%{mingw64_libdir}/libquazip1-qt5.dll.a
%{mingw64_libdir}/pkgconfig/quazip1-qt5.pc
%{mingw64_libdir}/cmake/QuaZip-Qt5-%{version}/

%files -n mingw64-%{pkgname}-qt6
%license COPYING
%{mingw64_bindir}/libquazip1-qt6.dll
%{mingw64_includedir}/QuaZip-Qt6-%{version}/
%{mingw64_libdir}/libquazip1-qt6.dll.a
%{mingw64_libdir}/pkgconfig/quazip1-qt6.pc
%{mingw64_libdir}/cmake/QuaZip-Qt6-%{version}/

%changelog
%autochangelog
