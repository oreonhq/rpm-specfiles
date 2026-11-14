# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 1a4fbe7589e814777ae76b64734ad80f4ecad22cd33a22682a2aaea4ae5375e7
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: libgit2
Version: 1.9.7
Release: 1%{?dist}
Summary: C implementation of the Git core methods as a library with a solid API
License: GPL-2.0-only WITH GCC-exception-2.0 AND MIT AND LicenseRef-Fedora-Public-Domain AND Apache-2.0 AND SSLeay-standalone AND BSD-2-Clause AND NCSA AND Unlicense
URL: https://libgit2.org/
Source0: https://github.com/libgit2/libgit2/archive/refs/tags/v%{version}.tar.gz#/libgit2-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: cmake >= 3.5.1
BuildRequires: ninja-build
BuildRequires: krb5-devel
BuildRequires: libcurl-devel
BuildRequires: libssh2-devel
BuildRequires: openssl-devel
BuildRequires: pcre2-devel
BuildRequires: python3
BuildRequires: zlib-devel

Provides: bundled(libxdiff)
Provides: bundled(llhttp) = 9.2.1
Provides: libgit2_1.9 = %{version}-%{release}
Provides: libgit2_1.9%{?_isa} = %{version}-%{release}
Obsoletes: libgit2_1.8 < 1.8.5-3

%description
libgit2 is a portable, pure C implementation of the Git core methods
provided as a re-entrant linkable library with a solid API, allowing
you to write native speed custom Git applications in any language
with bindings.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: pkgconfig(libgit2) = %{version}
Provides: libgit2_1.9-devel = %{version}-%{release}
Provides: libgit2_1.9-devel%{?_isa} = %{version}-%{release}
Obsoletes: libgit2_1.8-devel < 1.8.5-3

%description devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%oreon_sha256
%autosetup -p1 -n libgit2-%{version}

find examples -name ".gitignore" -delete -print

sed -i '/-sonline/s/^/#/' tests/libgit2/CMakeLists.txt

pushd deps
find . -maxdepth 1 -not -name . -not -name xdiff -not -name llhttp -exec rm -rf {} ';'
popd

%build
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DREGEX_BACKEND=pcre2 \
  -DBUILD_CLI=OFF \
  -DUSE_HTTP_PARSER=builtin \
  -DUSE_SHA1=HTTPS \
  -DUSE_HTTPS=OpenSSL \
  -DUSE_NTLMCLIENT=OFF \
  -DUSE_SSH=ON \
  %{nil}
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license COPYING
%{_libdir}/libgit2.so.1.9*

%files devel
%doc AUTHORS docs examples README.md
%{_libdir}/libgit2.so
%{_libdir}/cmake/libgit2/
%{_libdir}/pkgconfig/libgit2.pc
%{_includedir}/git2.h
%{_includedir}/git2/

%changelog
%autochangelog
