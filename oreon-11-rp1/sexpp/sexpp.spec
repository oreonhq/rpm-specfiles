%global source0_hash 00c47b56a4dd5e80aba6b15df4e86d276a2a369737c6b467be1f51a9c29af31e

# remirepo/fedora spec file for sexpp
#
# SPDX-FileCopyrightText:  Copyright 2023-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%bcond_without      tests
%bcond_with         licensecheck

%global libname     libsexpp
%global soname      0

Name:          sexpp
Summary:       S-expressions parser and generator tools
Version:       0.9.2
Release:       3%{?dist}
License:       MIT

URL:           https://github.com/rnpgp/%{name}
Source0:       %{url}/archive/refs/tags/v%{version}.tar.gz
# Use --with licensecheck to generate
Source3:       %{name}-files-by-license.txt

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake >= 3.14
BuildRequires:  gcc
BuildRequires:  gcc-c++
%if 0%{?rhel} == 8
BuildRequires:  gtest-devel
%else
BuildRequires:  cmake(GTest)
%endif
%if %{with licensecheck}
BuildRequires:  licensecheck
%endif

Requires:       %{libname}%{?_isa} = %{version}-%{release}

%description
S-expressions parser and generator tools.

%package -n %{libname}
Summary:    S-expressions parser and generator library

%description -n %{libname}
%{libname} is a C++ library for working with S-expressions.

This implementation is derived from the reference SEXP C library developed by
Professors Ronald Rivest and Butler Lampson of MIT LCS (now CSAIL).

%package -n %{libname}-devel
Summary:    Header files and development libraries for %{libname}
Requires:   %{libname}%{?_isa} = %{version}-%{release}

%description -n %{libname}-devel
This package contains the header files and development libraries
for %{libname}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%if %{with licensecheck}
LST=$(mktemp)

licensecheck -r . | sed -e 's:^./::' >$LST
grep -v UNKNOWN $LST | sed -e 's/.*: //' | sort -u | while read lic
do
    echo -e "\n$lic\n------------"
    grep ": $lic\$" $LST | sed -e "s/: $lic//"
done  | tee %{SOURCE3}
rm $LST
%endif

%build
%cmake . \
%if %{with tests}
   -DWITH_SEXP_TESTS:BOOL=ON \
%else
   -DWITH_SEXP_TESTS:BOOL=OFF \
%endif
   -DDOWNLOAD_GTEST:BOOL=OFF \
   -DWITH_SEXP_CLI:BOOL=ON \
   -DWITH_SANITIZERS:BOOL=OFF \
   -DWITH_COVERAGE:BOOL=OFF \
   -DBUILD_SHARED_LIBS:BOOL=ON \
   -DDOWNLOAD_GTEST:BOOL=OFF

%cmake_build

%install
%cmake_install

%if %{with tests}
%check
%ctest
%endif

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%files -n %{libname}
%license LICENSE*
%{_libdir}/%{libname}.so.%{soname}*

%files -n %{libname}-devel
%{_includedir}/%{name}
%{_libdir}/%{libname}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
