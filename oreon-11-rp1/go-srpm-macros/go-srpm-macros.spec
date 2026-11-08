# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 3f28f41e9d26564d494cd713fdba3f8797c31865307de282d5ec0f76f710f2c1
%global debug_package %{nil}

Name: go-srpm-macros
Version: 3.8.0
Release: 2%{?dist}
Summary: SRPM macros for Go packages
License: GPL-3.0-or-later
URL: https://gitlab.com/fedora/sigs/go/go-rpm-macros
BuildArch: noarch
Source0: https://gitlab.com/fedora/sigs/go/go-rpm-macros/-/archive/3.8.0/go-rpm-macros-3.8.0.tar.gz
Requires: oreon-rpm-config
Requires: forge-srpm-macros

BuildRequires: oreon-rpm-macros

%description
SRPM macros for Go source packages. The Go compiler is not part of this package.

%prep
%autosetup -n go-rpm-macros-%{version} -p1
%oreon_sha256
sed -i 's/"fedora\./"oreon./g' rpm/macros.d/macros.go-srpm rpm/lua/srpm/go.lua

%build

%install
mkdir -p %{buildroot}%{_rpmmacrodir}
mkdir -p %{buildroot}%{_rpmluadir}/oreon/srpm
install -m 644 rpm/macros.d/macros.go-srpm %{buildroot}%{_rpmmacrodir}/macros.go-srpm
install -m 644 rpm/lua/srpm/go.lua %{buildroot}%{_rpmluadir}/oreon/srpm/go.lua

%files
%license LICENSE.txt
%{_rpmmacrodir}/macros.go-srpm
%{_rpmluadir}/oreon/srpm/go.lua
