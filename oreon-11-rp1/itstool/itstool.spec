# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 119a221f71067353d219af80ec2247ac964a8c6b29fe87e8808f95d698b0cafc
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: itstool
Version: 2.0.7
Release: 1%{?dist}
Summary: Translate XML with ITS rules
License: GPL-3.0-or-later
URL: http://itstool.org/
Source0: https://files.pythonhosted.org/packages/23/58/04c2595475db382175f4185d2faafcbe82772e5e6131cb49dfc0933db095/itstool-%{version}.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3
BuildRequires: python3-libxml2
Requires: python3-libxml2

%description
itstool extracts translatable strings from XML and merges translations back.

%prep
%oreon_sha256
%autosetup -n itstool-%{version}
sed -i '1s|#!/usr/bin/python.*|#!/usr/bin/python3|' itstool

%build

%install
install -D -p -m 0755 itstool %{buildroot}%{_bindir}/itstool
mkdir -p %{buildroot}%{_datadir}/itstool/its
install -p -m 0644 its/* %{buildroot}%{_datadir}/itstool/its/

%check
python3 -c 'import libxml2'

%files
%license COPYING
%{_bindir}/itstool
%{_datadir}/itstool/
