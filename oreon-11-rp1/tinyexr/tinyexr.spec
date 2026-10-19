%global source0_hash df2bd61124a35d8138f8b0bc22418a1d4fe33622c818e0e022f5522afc0821b0
Name:           tinyexr
Version:        3.2.0
Release:        1%{?dist}
Summary:        Small library to load and save OpenEXR images
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/syoyo/%{name}
Source0:        https://github.com/syoyo/%{name}/archive/refs/tags/v%{version}.tar.gz
Source1:        LICENSE
Patch1:         0002-Explicitly-export-required-symbols.patch
Patch2:         0003-Fix-CMake-build-system.patch
Patch3:         0004-Add-test-executable-for-CTest.patch
Patch4:         %{name}-miniz.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  miniz-devel
BuildRequires:  sed
# /oreon:deps
%description
TinyEXR is a small library to load and save OpenEXR images. It supports
the version 1 format and version 2 multi-part images, and it has partial
support for version 2 deep images.
 
%package devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Summary:        Development files for %{name}
%description devel
%{summary}.

%prep

%autosetup -p1
cp %{SOURCE1} LICENSE

# Remove all thirdparty libraries
rm -rf deps

%build

%cmake
%cmake_build
sed -i '/^#ifdef TINYEXR_IMPLEMENTATION$/,/^#endif  \/\/ TINYEXR_IMPLEMENTATION$/d' tinyexr.h
%ifnarch s390x
%check

%ctest
%endif
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n tinyexr-devel -f %{oreon_filedir}/tinyexr-devel.list

%changelog

%autochangelog
