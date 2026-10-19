%global source0_hash 8a9ff2e48582efe31118a354714e41946cc3c7f03713b640ce7c516e06468c57
Name:		expatpp
Version:	0
Release:        1%{?dist}
Summary:        C++ layer for expat
License:	MPL-1.1
URL:		http://sourceforge.net/projects/expatpp/
Source0:        expatpp.tar.bz2
Patch:		0001-Added-CMake-config-file.patch
Patch:		0002-Fix-case-of-required-arg.patch
Patch:		0003-Include-string-header.patch
Patch:		0004-Converted-to-lib-standalone-program-layout.patch
Patch:		0005-Added-test-code.patch
Patch:		0006-Build-testexpatpp1.patch
Patch:		0007-Fix-subdir-command.patch
Patch:		0008-Added-cPack.patch
Patch:		0009-Install-library.patch
Patch:		0010-Use-lib-or-lib64-automatically.patch
Patch:		0011-added-soname-info.patch
Patch:		0012-Fixed-missing-api-version.patch
Patch:		0013-Install-header-file.patch
Patch:		0014-Removed-windows-static-lib-header.patch
Patch:		0015-Reworked-documentation.patch
Patch:		0016-Quick-fix-for-FTBFS.patch
Patch:		0017-PATCH-Modernize-CMake-build-system-for-CMake-4-compa.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
# /oreon:deps
%description
Expatpp is a simple C++ layer to make using the open source expat XML parsing
library vastly easier for complex schemas. It has been used widely in industry
including the Valve Steam project.

%package	devel
Summary:	Headers and development libraries for expatpp
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
You should install this package if you would like to
develop code based on expatpp.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}
%oreon_prep
%build

%{cmake} -DCMAKE_VERBOSE_MAKEFILE=ON \
       -DBUILD_SHARED_LIBS:BOOL=ON \
       -DCMAKE_BUILD_TYPE:STRING="RelWithDebInfo" .
%{cmake_build}
%install
%{cmake_install}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%{ctest}
%files -f %{oreon_filedir}/main.list
%files -n expatpp-devel -f %{oreon_filedir}/expatpp-devel.list

%changelog

%autochangelog
