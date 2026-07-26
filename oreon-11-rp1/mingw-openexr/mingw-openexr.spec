%global source0_hash none

%{?mingw_package_header}

%global pkgname openexr

Name:          mingw-%{pkgname}
Version:       3.4.7
Release:       1%{?dist}
Summary:       MinGW Windows %{pkgname} library

License:       BSD-3-Clause
URL:           http://www.openexr.com/
BuildArch:     noarch
Source0:       https://github.com/AcademySoftwareFoundation/%{pkgname}/archive/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: make

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-imath
BuildRequires: mingw32-libdeflate
BuildRequires: mingw32-libopenjph
BuildRequires: mingw32-zlib

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-imath
BuildRequires: mingw64-libdeflate
BuildRequires: mingw64-libopenjph
BuildRequires: mingw64-zlib

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

# Don't install doc
rm -rf %{buildroot}%{mingw32_docdir}/OpenEXR
rm -rf %{buildroot}%{mingw64_docdir}/OpenEXR

%files -n mingw32-%{pkgname}
%license LICENSE.md
%{mingw32_bindir}/libIex-3_4.dll
%{mingw32_bindir}/libIlmThread-3_4.dll
%{mingw32_bindir}/libOpenEXR-3_4.dll
%{mingw32_bindir}/libOpenEXRCore-3_4.dll
%{mingw32_bindir}/libOpenEXRUtil-3_4.dll
%{mingw32_includedir}/OpenEXR/
%{mingw32_libdir}/libIex-3_4.dll.a
%{mingw32_libdir}/libIlmThread-3_4.dll.a
%{mingw32_libdir}/libOpenEXR-3_4.dll.a
%{mingw32_libdir}/libOpenEXRCore-3_4.dll.a
%{mingw32_libdir}/libOpenEXRUtil-3_4.dll.a
%{mingw32_libdir}/cmake/OpenEXR/
%{mingw32_libdir}/pkgconfig/OpenEXR.pc

%files -n mingw32-%{pkgname}-tools
%{mingw32_bindir}/exr2aces.exe
%{mingw32_bindir}/exrenvmap.exe
%{mingw32_bindir}/exrheader.exe
%{mingw32_bindir}/exrinfo.exe
%{mingw32_bindir}/exrmakepreview.exe
%{mingw32_bindir}/exrmaketiled.exe
%{mingw32_bindir}/exrmanifest.exe
%{mingw32_bindir}/exrmetrics.exe
%{mingw32_bindir}/exrmultipart.exe
%{mingw32_bindir}/exrmultiview.exe
%{mingw32_bindir}/exrstdattr.exe

%files -n mingw64-%{pkgname}
%license LICENSE.md
%{mingw64_bindir}/libIex-3_4.dll
%{mingw64_bindir}/libIlmThread-3_4.dll
%{mingw64_bindir}/libOpenEXR-3_4.dll
%{mingw64_bindir}/libOpenEXRCore-3_4.dll
%{mingw64_bindir}/libOpenEXRUtil-3_4.dll
%{mingw64_includedir}/OpenEXR/
%{mingw64_libdir}/libIex-3_4.dll.a
%{mingw64_libdir}/libIlmThread-3_4.dll.a
%{mingw64_libdir}/libOpenEXR-3_4.dll.a
%{mingw64_libdir}/libOpenEXRCore-3_4.dll.a
%{mingw64_libdir}/libOpenEXRUtil-3_4.dll.a
%{mingw64_libdir}/cmake/OpenEXR/
%{mingw64_libdir}/pkgconfig/OpenEXR.pc

%files -n mingw64-%{pkgname}-tools
%{mingw64_bindir}/exr2aces.exe
%{mingw64_bindir}/exrenvmap.exe
%{mingw64_bindir}/exrheader.exe
%{mingw64_bindir}/exrinfo.exe
%{mingw64_bindir}/exrmakepreview.exe
%{mingw64_bindir}/exrmaketiled.exe
%{mingw64_bindir}/exrmanifest.exe
%{mingw64_bindir}/exrmetrics.exe
%{mingw64_bindir}/exrmultipart.exe
%{mingw64_bindir}/exrmultiview.exe
%{mingw64_bindir}/exrstdattr.exe

%changelog
%autochangelog
