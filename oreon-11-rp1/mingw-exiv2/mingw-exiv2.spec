%global source0_hash 700b76b97695b2fab4ef8c79619c68ae57d09e0c130724791cafbd39e0eb4aef
%{?mingw_package_header}
%global pkgname exiv2
Name:          mingw-%{pkgname}
Version:       0.28.9
Release:        1%{?dist}
Summary:        MinGW Windows exiv2 library
License:       GPL-2.0-or-later
BuildArch:     noarch
URL:           http://www.exiv2.org/
Source0:        https://github.com/Exiv2/%{pkgname}/archive/v%{version}/%{pkgname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  mingw32-brotli
BuildRequires:  mingw32-expat
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-inih
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-brotli
BuildRequires:  mingw64-expat
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-inih
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-zlib
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

%autosetup -p1 -n %{pkgname}-%{version}

%build

%mingw_cmake \
  -DEXIV2_ENABLE_NLS:BOOL=ON \
  -DEXIV2_BUILD_SAMPLES:BOOL=OFF \
  -DCMAKE_NO_SYSTEM_FROM_IMPORTED=ON \
  -DICONV_ACCEPTS_CONST_INPUT=1
%mingw_make_build
%install
%mingw_make_install
%mingw_find_lang exiv2
rm -f %{buildroot}%{mingw32_libdir}/pkgconfig/exiv2.lsm
rm -f %{buildroot}%{mingw32_datadir}/man/man1/exiv2.1
rm -f %{buildroot}%{mingw64_libdir}/pkgconfig/exiv2.lsm
rm -f %{buildroot}%{mingw64_datadir}/man/man1/exiv2.1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-exiv2 -f %{oreon_filedir}/mingw32-exiv2.list
%files -n mingw64-exiv2 -f %{oreon_filedir}/mingw64-exiv2.list

%changelog

%autochangelog
