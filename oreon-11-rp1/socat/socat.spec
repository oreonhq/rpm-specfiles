# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash a9f9eb6cfb9aa6b1b4b8fe260edbac3f2c743f294db1e362b932eb3feca37ba4

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: socat
Version: 1.8.0.3
Release: 1%{?dist}
Summary: Multipurpose relay for bidirectional data transfer
License: GPL-2.0-or-later
URL: http://www.dest-unreach.org/socat/
Source0: http://www.dest-unreach.org/socat/download/socat-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: readline-devel

%description
socat is a command line based utility that establishes two bidirectional
byte streams and transfers data between them.

%prep
%oreon_sha256
%autosetup -p1

%build
%configure --disable-libwrap
%make_build

%install
%make_install

%check
make test

%files
%license COPYING
%doc CHANGES README
%{_bindir}/socat
%{_bindir}/socat1
%{_bindir}/procan
%{_bindir}/filan
%{_mandir}/man1/socat.1*
%{_mandir}/man1/socat1.1*
%{_mandir}/man1/procan.1*
%{_mandir}/man1/filan.1*

%changelog
%autochangelog
