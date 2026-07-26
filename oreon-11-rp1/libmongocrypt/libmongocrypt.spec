%global source0_hash fe60fc4943a73d93cb29b8b20b026b7da634614ef4b4f92d9c2f98d166594bf4

# remirepo/fedora spec file for libmongocrypt
#
# SPDX-FileCopyrightText:  Copyright 2020-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#
%global gh_owner     mongodb
%global gh_project   libmongocrypt
%global libname      %{gh_project}
%global libver       1.0
%global soname       0

Name:      %{libname}
Summary:   The companion C library for client side encryption in drivers
Version:   1.15.2
Release:   2%{?dist}

# see kms-message/THIRD_PARTY_NOTICES
# kms-message/src/kms_b64.c is ISC
# IntelRDFPMathLib is BSD-3-Clause
# everything else is ASL 2.0
License:   Apache-2.0 AND ISC AND BSD-3-Clause
URL:       https://github.com/%{gh_owner}/%{gh_project}

Source0:   https://github.com/%{gh_owner}/%{gh_project}/archive/%{version}.tar.gz

# drop all reference to static libraries
Patch0:    %{libname}-static.patch
# fix FTBFS -Werror=discarded-qualifiers
# https://jira.mongodb.org/browse/MONGOCRYPT-873
Patch1:    %{libname}-build.patch

BuildRequires: cmake >= 3.12
BuildRequires: gcc
BuildRequires: gcc-c++
# pkg-config may pull compat-openssl10
BuildRequires: openssl-devel
BuildRequires: cmake(bson-1.0) >= 1.11
# for documentation
BuildRequires: doxygen
BuildRequires: make
# for IntelRDFPMathLib
BuildRequires: git
Provides:      bundled(IntelRDFPMathLib) = 2.2

%description
%{summary}.

%package devel
Summary:    Header files and development libraries for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   pkgconfig
Requires:   cmake-filesystem

%description devel
This package contains the header files and development libraries
for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gh_project}-%{version}%{?prever:-dev} -p1

# Gather license files
tar xf third-party/IntelRDFPMathLib*.tar.xz --strip-components=1 */eula.txt
mv eula.txt                        LICENSE.intelrdfpmathlib
cp kms-message/THIRD_PARTY_NOTICES LICENSE.kms_b64
cp kms-message/COPYING             LICENSE.kms-message

%build
%cmake \
    -DBUILD_VERSION=%{version} \
    -DENABLE_PIC:BOOL=ON \
    -DUSE_SHARED_LIBBSON:BOOL=ON \
    -DMONGOCRYPT_MONGOC_DIR:STRING=USE-SYSTEM \
    -DENABLE_ONLINE_TESTS:BOOL=OFF \
    -DENABLE_STATIC:BOOL=OFF

%cmake_build

doxygen ./doc/Doxygen

%install
%cmake_install

%check
%ctest

if grep -r static %{buildroot}%{_libdir}/cmake; then
  : cmake configuration file contain reference to static library
  exit 1
fi

%files
%license LICENSE*
%{_libdir}/libkms_message.so.%{soname}*
%{_libdir}/libmongocrypt.so.%{soname}*

%files devel
%doc *.md
%doc doc/html
%{_includedir}/kms_message
%{_includedir}/mongocrypt
%{_libdir}/libkms_message.so
%{_libdir}/libmongocrypt.so
%{_libdir}/cmake/kms_message
%{_libdir}/cmake/mongocrypt
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
