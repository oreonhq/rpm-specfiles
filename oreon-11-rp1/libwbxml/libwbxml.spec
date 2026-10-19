%global source0_hash 027b77ab7c06458b73cbcf1f06f9cf73b65acdbb2ac170b234c1d736069acae4
Name:           libwbxml
Version:        0.11.10
Release:        1%{?dist}
Summary:        Library and tools to parse, encode and handle WBXML documents
License:        LGPL-2.1-or-later
SourceLicense:  GPL-2.0-or-later AND LGPL-2.1-or-later AND BSD-4-Clause AND BSD-3-Clause AND MIT
URL:            https://github.com/%{name}/%{name}
Source0:        https://github.com/%{name}/%{name}/archive/%{name}-%{version}.tar.gz
Patch0:         libwbxml-0.11.10-Fix-installing-CMake-configuration-files.patch
Patch1:         libwbxml-0.11.10-Use-GNUInstallDirs-for-defining-installation-directo.patch
Obsoletes:      wbxml2 <= 0.9.3
# oreon:deps
BuildRequires:  bash
BuildRequires:  cmake
BuildRequires:  coreutils
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(English)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(check)
# /oreon:deps
%description
The WBXML Library (libwbxml) contains a library and its associated tools to
parse, encode and handle WBXML documents. The WBXML format is a binary
representation of XML, defined by the Wap Forum, and used to reduce
bandwidth in mobile communications.

%package devel
Summary:       Development files of %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      pkgconfig
Provides:      wbxml2-devel = %{version}-%{release}
Obsoletes:     wbxml2-devel <= 0.9.3
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{name}-%{version}
%oreon_prep
%build

%{cmake} \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DBUILD_STATIC_LIBS:BOOL=OFF \
    -DENABLE_INSTALL_DOC:BOOL=OFF \
    -DENABLE_UNIT_TEST:BOOL=ON \
    -DWBXML_ENCODER_USE_STRTBL:BOOL=ON \
    -DWBXML_INSTALL_FULL_HEADERS:BOOL=OFF \
    -DWBXML_LIB_VERBOSE:BOOL=OFF \
    -DWBXML_SUPPORT_AIRSYNC:BOOL=ON \
    -DWBXML_SUPPORT_CO:BOOL=ON \
    -DWBXML_SUPPORT_CONML=ON \
    -DWBXML_SUPPORT_DRMREL:BOOL=ON \
    -DWBXML_SUPPORT_EMN:BOOL=ON \
    -DWBXML_SUPPORT_OTA_SETTINGS:BOOL=ON \
    -DWBXML_SUPPORT_PROV:BOOL=ON \
    -DWBXML_SUPPORT_SI:BOOL=ON \
    -DWBXML_SUPPORT_SL:BOOL=ON \
    -DWBXML_SUPPORT_SYNCML:BOOL=ON \
    -DWBXML_SUPPORT_WML:BOOL=ON \
    -DWBXML_SUPPORT_WTA:BOOL=ON \
    -DWBXML_SUPPORT_WV:BOOL=ON
%{cmake_build}
%install
%{cmake_install}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%{ctest}
%files -f %{oreon_filedir}/main.list
%files -n libwbxml-devel -f %{oreon_filedir}/libwbxml-devel.list

%changelog

%autochangelog
