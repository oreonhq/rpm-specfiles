# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 99d7468c22f6cafd8c72aa53173a632f2ca29cb19aec913e8ed45b6102af322d
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: firewalld-filesystem
Version: 2.5.2
Release: 1%{?dist}
Summary: Firewalld directory layout and rpm macros
License: GPL-2.0-or-later
URL: https://firewalld.org
Source0: https://github.com/firewalld/firewalld/releases/download/v%{version}/firewalld-%{version}.tar.bz2
BuildArch: noarch

BuildRequires: oreon-rpm-macros
Requires: filesystem
Requires: rpm

%description
This package provides directories and rpm macros which
are used by packages that install firewalld services or zones.

%prep
%oreon_sha256
%autosetup -n firewalld-%{version}

%build
:

%install
mkdir -p %{buildroot}%{_prefix}/lib/firewalld/{helpers,icmptypes,ipsets,policies,services,zones,xmlschema}
mkdir -p %{buildroot}%{_datadir}/firewalld
mkdir -p %{buildroot}%{_rpmmacrodir}
install -p -m 644 config/macros.firewalld %{buildroot}%{_rpmmacrodir}/macros.firewalld

%files
%license COPYING
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/helpers
%dir %{_prefix}/lib/firewalld/icmptypes
%dir %{_prefix}/lib/firewalld/ipsets
%dir %{_prefix}/lib/firewalld/policies
%dir %{_prefix}/lib/firewalld/services
%dir %{_prefix}/lib/firewalld/zones
%dir %{_prefix}/lib/firewalld/xmlschema
%dir %{_datadir}/firewalld
%{_rpmmacrodir}/macros.firewalld

%changelog
%autochangelog
