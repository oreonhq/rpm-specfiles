# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 35f1008184c13de55793fa292b62a0c10739f1294f401a3b6a772edc145a4b3b
%global source1_hash a871d912b8ec3d7bfe8908278e1b2c85ce7d773c027a484231dc1cce15eafddd
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global forgeurl https://github.com/adah1972/libunibreak

Name:           libunibreak
Version:        8.0
Release:        %{autorelease}
Summary:        A Unicode line-breaking library
%global tag %{name}_%{lua: v = string.gsub(rpm.expand('%{version}'), '%.', '_'); print(v) }
%forgemeta
License:        Zlib
URL:            %forgeurl
Source0:        %forgesource
Source1:        libunibreak-test-data.tar.gz

Patch0:         0000-offline-files.patch
Patch1:         0001-remove-unused-variable.patch

ExcludeArch:    %{ix86}

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  make
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool

%description
Libunibreak is an implementation of the line breaking and word
breaking algorithms as described in Unicode Standard Annex 14 and
Unicode Standard Annex 29. It is designed to be used in a generic text
renderer.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%forgeautosetup -p1

tar xzf %{SOURCE1}

sed -r -i 's|^(#!/usr/bin/)env (python)|\1\23|' src/*.py
chmod a+x src/*.py

%build
./autogen.sh
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%check
%make_build check

%ldconfig_scriptlets

%files
%doc AUTHORS NEWS README.md
%license LICENCE
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
