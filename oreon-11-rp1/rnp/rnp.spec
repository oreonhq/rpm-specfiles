%global source0_hash 423c8e32e1e591462f759adf8441b1c44bca96d9f5daff13b82e81a79f18ecfd

# remirepo/fedora spec file for rnp
#
# SPDX-FileCopyrightText:  Copyright 2022-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%bcond_without      tests
%bcond_with         licensecheck
%bcond_without      libsexpp

%if 0%{?rhel} == 8
# use openssl by default as botan2 is too old
%bcond_without      openssl
%else
# use botan2 as openssl seems experimental/wip
%bcond_with         openssl
%endif

%global libname     librnp
%global soname      0

Name:          rnp
Summary:       OpenPGP (RFC4880) tools
Version:       0.18.1
Release:       3%{?dist}
# See rnp-files-by-license.txt and upstream LICENSE* files
License:       BSD-2-Clause AND Apache-2.0 AND MIT

URL:           https://github.com/rnpgp/rnp
Source0:       %{url}/releases/download/v%{version}/rnp-v%{version}.tar.gz
Source1:       %{url}/releases/download/v%{version}/rnp-v%{version}.tar.gz.asc
# See https://www.rnpgp.org/openpgp_keys/
Source2:       %{name}-keyring.gpg
# Use --with licensecheck to generate
Source3:       %{name}-files-by-license.txt

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake >= 3.14
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(bzip2)
%if %{with openssl}
BuildRequires:  openssl-devel >= 1.1.1
BuildRequires:  json-c-devel >= 0.11
BuildRequires:  gtest-devel
%else
BuildRequires:  pkgconfig(botan-2) >= 2.14
BuildRequires:  cmake(json-c) >= 0.11
BuildRequires:  cmake(GTest)
%endif
BuildRequires:  python3
BuildRequires:  gnupg2
BuildRequires:  rubygem-asciidoctor
%if %{with licensecheck}
BuildRequires:  licensecheck
%endif
%if %{with libsexpp}
%global libsexpp_version 0.8.7
BuildRequires:  pkgconfig(sexpp) >= %{libsexpp_version}
%endif

Requires:       %{libname}%{?_isa} = %{version}-%{release}

%description
RNP is a set of OpenPGP (RFC4880) tools.

%package -n %{libname}
Summary:    Library for all OpenPGP functions
%if %{without libsexpp}
%global libsexpp_version 0.9.0
Provides:   bundled(libsexpp) = %{libsexpp_version}
%endif

%description -n %{libname}
%{libname} is the library used by RNP for all OpenPGP functions,
useful for developers to build against, different from GPGME.

%package -n %{libname}-devel
Summary:    Header files and development libraries for %{libname}
Requires:   %{libname}%{?_isa} = %{version}-%{release}

%description -n %{libname}-devel
This package contains the header files and development libraries
for %{libname}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-v%{version}
%{?gpgverify:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}

%if %{with libsexpp}
rm -rf  src/libsexp
: check system version requirement
if ! grep -q 'sexpp>=%{libsexpp_version}' CMakeLists.txt; then
    echo fix %%libsexpp_version macro, defined %{libsexpp_version}, expected \
        $(grep 'sexpp>=' CMakeLists.txt | sed 's/.*sexp>=//;s/)//')
    exit 1
fi
%else
pushd src/libsexpp
: retrieve LICENSE
cp LICENSE.md ../../LICENSE-libsexp.md
: check bundled version
if ! grep -q %{libsexpp_version} version.txt; then
    echo fix %%libsexpp_version macro, defined %{libsexpp_version}, expected \
        $(cat version.txt)
    exit 1
fi
popd
%endif

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
   -DINSTALL_STATIC_LIBS:BOOL=OFF \
%if %{with openssl}
   -DCRYPTO_BACKEND:STRING=openssl \
%else
   -DCRYPTO_BACKEND:STRING=botan \
%endif
%if %{with libsexpp}
   -DSYSTEM_LIBSEXPP:BOOL=ON \
%else
   -DSYSTEM_LIBSEXPP:BOOL=OFF \
%endif
   -DENABLE_COVERAGE:BOOL=OFF \
   -DENABLE_SANITIZERS:BOOL=OFF \
   -DENABLE_SANITIZERS:BOOL=OFF \
   -DENABLE_FUZZERS:BOOL=OFF \
   -DDOWNLOAD_GTEST:BOOL=OFF \
   -DDOWNLOAD_RUBYRNP:BOOL=OFF

%cmake_build

%install
%cmake_install

%if %{with tests}
%check
# erratic results on koji
FILTER="s2k_iteration_tuning|test_key_add_userid|test_ffi_security_profile|EncryptElgamal|cli_tests"

%ctest --exclude-regex $FILTER
%endif

%files
%{_bindir}/rnp
%{_bindir}/rnpkeys
%{_mandir}/man1/rnp*

%files -n %{libname}
%license LICENSE*
%{_libdir}/%{libname}.so.%{soname}*

%files -n %{libname}-devel
%doc CHANGELOG.md
%{_includedir}/rnp
%{_libdir}/%{libname}.so
%{_libdir}/pkgconfig/%{libname}.pc
%{_libdir}/cmake/rnp
%{_mandir}/man3/librnp*

%changelog
%autochangelog
