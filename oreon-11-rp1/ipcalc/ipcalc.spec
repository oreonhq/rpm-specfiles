# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 321be92964228cf2ef876b2e91455ac6c69b9751bf2d54a00e8873f9caf86e8a
%global source1_hash 31e6f3d6808fc356e044681df9530a4cb1a042f7ccd0492c93ba24c2f248137f
%global source2_hash 5ca3e88cf1e2f4dbbebe8b3de120a6643b4e01c27fca2784e70c3bbc5bfc71a2
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: ipcalc
Version: 1.2.0
Release:        %{autorelease}
Summary: IP network address calculator
License: GPL-2.0-or-later
URL: https://gitlab.com/ipcalc/ipcalc
Source0: https://gitlab.com/api/v4/projects/ipcalc%%2Fipcalc/packages/generic/ipcalc/%{version}/ipcalc-%{version}.tar.xz
Source1: https://gitlab.com/api/v4/projects/ipcalc%%2Fipcalc/packages/generic/ipcalc/%{version}/ipcalc-%{version}.tar.xz.sig
Source2: gpgkey-1F42418905D8206AA754CCDC29EE58B996865171.gpg

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: libmaxminddb-devel
BuildRequires: meson
BuildRequires: rubygem-ronn-ng
BuildRequires: gnupg2
BuildRequires: jq
Recommends:    libmaxminddb, dbip-lite-city, dbip-lite-country, dbip-lite-asn

Conflicts: initscripts < 9.63
Obsoletes:  ipcalculator < 0.41-20

%description
ipcalc provides a simple way to calculate IP information for a host
or network. Depending on the options specified, it may be used to provide
IP network information in human readable format, in a format suitable for
parsing in scripts, generate random private addresses, resolve an IP address,
or check the validity of an address.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%meson -Duse_maxminddb=enabled -Duse_runtime_linking=enabled \
  -Dc_args="%{build_cflags} \
    -DMAXMINDDB_LOCATION_COUNTRY='\"%{_datadir}/GeoIP/dbip-country-lite.mmdb\"' \
    -DMAXMINDDB_LOCATION_CITY='\"%{_datadir}/GeoIP/dbip-city-lite.mmdb\"' \
    -DMAXMINDDB_LOCATION_ASN='\"%{_datadir}/GeoIP/dbip-asn-lite.mmdb\"'"
%meson_build

%install
%meson_install

%check
%meson_test

%files

%{_bindir}/ipcalc
%license COPYING
%doc README.md
%{_mandir}/man1/ipcalc.1*

%changelog
%autochangelog
