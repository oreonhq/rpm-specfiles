%global source0_hash 027b77ab7c06458b73cbcf1f06f9cf73b65acdbb2ac170b234c1d736069acae4

Name:           libwbxml
Version:        0.11.10
Release:        6%{?dist}
Summary:        Library and tools to parse, encode and handle WBXML documents
## Used and installed:
# COPYING:                          LGPL-2.1-or-later
# GNU-LGPL:                         LGPL-2.1 text
# Other files:                      LGPL-2.1-or-later
## Not installed:
# cmake/modules/AddDocumentation.cmake:             "see the accompanying COPYING-CMAKE-SCRIPTS"
# cmake/modules/COPYING-CMAKE-SCRIPTS:              BSD-3-Clause text
# cmake/modules/MacroEnsureOutOfSourceBuild.cmake:  "see the accompanying COPYING-CMAKE-SCRIPTS"
# cmake/modules/ShowStatus.cmake:                   "see the accompanying COPYING-CMAKE-SCRIPTS"
## Not used:
# win32/leaktrack/COPYING.txt:      BSD-4-Clause
# win32/leaktrack/leaktrack.h:      GPL-2.0-or-later
# win32/leaktrack/lt_log.h:         GPL-2.0-or-later
# win32/expat/COPYING.txt:          MIT
# win32/expat/expat.h:              "See the file COPYING"
# win32/expat/README.txt:           "see COPYING, same as MIT/X Consortium license"
License:        LGPL-2.1-or-later
SourceLicense:  GPL-2.0-or-later AND LGPL-2.1-or-later AND BSD-4-Clause AND BSD-3-Clause AND MIT
URL:            https://github.com/%{name}/%{name}
Source:         %{url}/archive/%{name}-%{version}.tar.gz
# Fix installing CMake configuration files, in upstream after 0.11.10,
# <https://github.com/libwbxml/libwbxml/pull/95>.
Patch0:         libwbxml-0.11.10-Fix-installing-CMake-configuration-files.patch
# Fix building with nonstandard CMake variables, bug #2381269,
# in upstream after 0.11.10, <https://github.com/libwbxml/libwbxml/pull/104>
Patch1:         libwbxml-0.11.10-Use-GNUInstallDirs-for-defining-installation-directo.patch
BuildRequires:  cmake >= 3.5
BuildRequires:  coreutils
BuildRequires:  expat-devel
BuildRequires:  gcc
# cmake executes make, but does not declare the dependency
BuildRequires:  make
BuildRequires:  pkgconfig(check)
# Tests:
BuildRequires:  bash
BuildRequires:  perl-interpreter
BuildRequires:  perl(English)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Obsoletes:      wbxml2 <= 0.9.3

%description
The WBXML Library (libwbxml) contains a library and its associated tools to
parse, encode and handle WBXML documents. The WBXML format is a binary
representation of XML, defined by the Wap Forum, and used to reduce
bandwidth in mobile communications.

%package devel
Summary:       Development files of %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      pkgconfig
# ??? FIXME Deps for libwbxml2-config.cmake file
# <https://github.com/libwbxml/libwbxml/issues/96>
Provides:      wbxml2-devel = %{version}-%{release}
Obsoletes:     wbxml2-devel <= 0.9.3

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{name}-%{version}

%build
# Upstream does not support in-source-directory building
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

%check
%{ctest}

%files
%license COPYING GNU-LGPL
%doc BUGS ChangeLog README References THANKS TODO
%{_bindir}/wbxml2xml
%{_bindir}/xml2wbxml
%{_libdir}/libwbxml2.so.*

%files devel
%{_includedir}/libwbxml-1.1
%{_libdir}/cmake/libwbxml2
%{_libdir}/libwbxml2.so
%{_libdir}/pkgconfig/libwbxml2.pc

%changelog
%autochangelog
