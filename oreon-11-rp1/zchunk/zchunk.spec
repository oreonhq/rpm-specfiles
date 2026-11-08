# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 2ab8ef54475aa2b2c0120fc6ae6d0788e0c3d4d4b671985edc6a19c8096a02cc

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
Name:           zchunk
Version:        1.5.5
Release:        1%{?dist}
Summary:        Compressed file format that allows easy deltas
License:        BSD-2-Clause AND MIT
URL:            https://github.com/zchunk/zchunk
Source0:        https://github.com/zchunk/zchunk/archive/%{version}/zchunk-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  meson
BuildRequires:  oreon-rpm-macros
Requires:       %{name}-libs%{_isa} = %{version}-%{release}
Provides:       bundled(buzhash-urlblock) = 0.1

%description
zchunk is a compressed file format that splits the file into independent
chunks.  This allows you to only download the differences when downloading a
new version of the file, and also makes zchunk files efficient over rsync.
zchunk files are protected with strong checksums to verify that the file you
downloaded is in fact the file you wanted.

%package libs
Summary: Zchunk library

%description libs
zchunk is a compressed file format that splits the file into independent
chunks.  This allows you to only download the differences when downloading a
new version of the file, and also makes zchunk files efficient over rsync.
zchunk files are protected with strong checksums to verify that the file you
downloaded is in fact the file you wanted.

This package contains the zchunk library, libzck.

%package devel
Summary: Headers for building against zchunk
Requires: %{name}-libs%{_isa} = %{version}-%{release}

%description devel
zchunk is a compressed file format that splits the file into independent
chunks.  This allows you to only download the differences when downloading a
new version of the file, and also makes zchunk files efficient over rsync.
zchunk files are protected with strong checksums to verify that the file you
downloaded is in fact the file you wanted.

This package contains the headers necessary for building against the zchunk
library, libzck.

%prep
%oreon_sha256

%autosetup
# Remove bundled sha libraries
rm -rf src/lib/hash/sha*

%build
%meson -Dwith-openssl=enabled -Dwith-zstd=enabled
%meson_build

%install
%meson_install
mkdir -p %{buildroot}%{_libexecdir}
install contrib/gen_xml_dictionary %{buildroot}%{_libexecdir}/zck_gen_xml_dictionary

%check
%meson_test

%ldconfig_scriptlets libs

%files
%doc README.md contrib
%{_bindir}/zck*
%{_bindir}/unzck
%{_libexecdir}/zck_gen_xml_dictionary
%{_mandir}/man1/*.gz

%files libs
%license LICENSE
%doc README.md
%{_libdir}/libzck.so.*

%files devel
%doc zchunk_format.txt
%{_libdir}/libzck.so
%{_libdir}/pkgconfig/zck.pc
%{_includedir}/zck.h

