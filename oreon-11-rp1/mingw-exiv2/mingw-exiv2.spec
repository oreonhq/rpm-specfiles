%global source0_hash none

%{?mingw_package_header}

%global pkgname exiv2

Name:          mingw-%{pkgname}
Version:       0.28.7
Release:       2%{?dist}
Summary:       MinGW Windows %{pkgname} library
License:       GPL-2.0-or-later
BuildArch:     noarch
URL:           http://www.exiv2.org/
Source0:       https://github.com/Exiv2/%{pkgname}/archive/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires: make
BuildRequires: cmake
BuildRequires: gettext

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-brotli
BuildRequires: mingw32-expat
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-gettext
BuildRequires: mingw32-inih
BuildRequires: mingw32-win-iconv
BuildRequires: mingw32-zlib

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-brotli
BuildRequires: mingw64-expat
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-gettext
BuildRequires: mingw64-inih
BuildRequires: mingw64-win-iconv
BuildRequires: mingw64-zlib

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
%autosetup -p1 -n %{pkgname}-%{version}

%build
%mingw_cmake \
  -DEXIV2_ENABLE_NLS:BOOL=ON \
  -DEXIV2_BUILD_SAMPLES:BOOL=OFF \
  -DCMAKE_NO_SYSTEM_FROM_IMPORTED=ON \
  -DICONV_ACCEPTS_CONST_INPUT=1

# Hack around double slashes install paths in generated po/cmake_install.cmake
# sed -i 's|//|/|g' build_win32/po/cmake_install.cmake
# sed -i 's|//|/|g' build_win64/po/cmake_install.cmake

%mingw_make_build

%install
%mingw_make_install
%mingw_find_lang exiv2

rm -f %{buildroot}%{mingw32_libdir}/pkgconfig/exiv2.lsm
rm -f %{buildroot}%{mingw32_datadir}/man/man1/exiv2.1
rm -f %{buildroot}%{mingw64_libdir}/pkgconfig/exiv2.lsm
rm -f %{buildroot}%{mingw64_datadir}/man/man1/exiv2.1

%files -n mingw32-%{pkgname} -f mingw32-%{pkgname}.lang
%license COPYING
%{mingw32_bindir}/exiv2.exe
%{mingw32_bindir}/libexiv2.dll
%{mingw32_libdir}/libexiv2.dll.a
%{mingw32_libdir}/cmake/exiv2/
%{mingw32_libdir}/pkgconfig/exiv2.pc
%{mingw32_includedir}/exiv2/

%files -n mingw64-%{pkgname} -f mingw64-%{pkgname}.lang
%license COPYING
%{mingw64_bindir}/exiv2.exe
%{mingw64_bindir}/libexiv2.dll
%{mingw64_libdir}/libexiv2.dll.a
%{mingw64_libdir}/cmake/exiv2/
%{mingw64_libdir}/pkgconfig/exiv2.pc
%{mingw64_includedir}/exiv2/

%changelog
%autochangelog
