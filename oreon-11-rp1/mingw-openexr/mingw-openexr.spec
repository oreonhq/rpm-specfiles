%global source0_hash 0dc41a9dd84c868ad89c892382f75f6835a73decbefab9366d6f168bf9322954
%{?mingw_package_header}
%global pkgname openexr
Name:          mingw-%{pkgname}
Version:       3.5.0
Release:        1%{?dist}
Summary:        MinGW Windows openexr library
License:       BSD-3-Clause
URL:           http://www.openexr.com/
BuildArch:     noarch
Source0:        https://github.com/AcademySoftwareFoundation/%{pkgname}/archive/v%{version}/%{pkgname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-imath
BuildRequires:  mingw32-libdeflate
BuildRequires:  mingw32-libopenjph
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-imath
BuildRequires:  mingw64-libdeflate
BuildRequires:  mingw64-libopenjph
BuildRequires:  mingw64-zlib
# /oreon:deps
%description
MinGW Windows %{pkgname} library.

%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library
%description -n mingw32-%{pkgname}
%{summary}.

%package -n mingw32-%{pkgname}-tools
Summary:       Tools for the MinGW Windows %{pkgname} library
Requires:      mingw32-%{pkgname} = %{version}-%{release}
%description -n mingw32-%{pkgname}-tools
%{summary}.

%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library
%description -n mingw64-%{pkgname}
%{summary}.

%package -n mingw64-%{pkgname}-tools
Summary:       Tools for the MinGW Windows %{pkgname} library
Requires:      mingw64-%{pkgname} = %{version}-%{release}
%description -n mingw64-%{pkgname}-tools
%{summary}.

%{?mingw_debug_package}

%prep

%autosetup -p1 -n %{pkgname}-%{version}

%build

%mingw_cmake -DOPENEXR_INSTALL_PKG_CONFIG=ON -DBUILD_TESTING=OFF
%mingw_make_build
%install
%mingw_make_install
rm -rf %{buildroot}%{mingw32_docdir}/OpenEXR
rm -rf %{buildroot}%{mingw64_docdir}/OpenEXR
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-openexr -f %{oreon_filedir}/mingw32-openexr.list
%files -n mingw32-openexr-tools -f %{oreon_filedir}/mingw32-openexr-tools.list
%files -n mingw64-openexr -f %{oreon_filedir}/mingw64-openexr.list
%files -n mingw64-openexr-tools -f %{oreon_filedir}/mingw64-openexr-tools.list

%changelog

%autochangelog
