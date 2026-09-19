%global source0_hash 6344a69fc1ed847d4ed3e272e0da5998948c6b828cb7af39c6321aba6cf88126

%define __cmake_in_source_build 1
#
# spec file for package innoextract
#
# Copyright (c) 2012-2015 Daniel Scharrer <daniel@constexpr.org>
#               2015 Alexandre Detiste <alexandre@detiste.be>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name:           innoextract
Version:        1.9
Release:        19%{?dist}
License:        zlib
Summary:        Tool to extract installers created by Inno Setup
Url:            https://constexpr.org/innoextract/
Source:         %{url}/files/%{name}-%{version}.tar.gz
Patch0:         innoextract-boost190.patch
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  boost-devel
BuildRequires:  xz-devel
BuildRequires: make

%description
Inno Setup is a tool to create installers for Microsoft Windows
applications. innoextract allows to extract such installers under
non-windows systems without running the actual installer using wine.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch 0 -p1

%build
%cmake \
    -DCMAKE_INSTALL_DATAROOTDIR="%{_datadir}" \
    -DCMAKE_INSTALL_MANDIR="%{_mandir}" \
    -DCMAKE_INSTALL_BINDIR="%{_bindir}" \
    -DUSE_LDGOLD=FALSE \
    .
make %{?_smp_mflags}

%install
%make_install

%files
%license LICENSE
%doc README.md CHANGELOG VERSION
%{_bindir}/innoextract
%{_mandir}/man1/innoextract.1*

%changelog
%autochangelog
