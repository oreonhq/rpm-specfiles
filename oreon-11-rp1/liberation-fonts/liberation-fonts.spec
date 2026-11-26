# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 7191c669bf38899f73a2094ed00f7b800553364f90e2637010a69c0e268f25d0
%global fontdir %{_fontbasedir}/liberation

Name: liberation-fonts
Version: 2.1.5
Release: 1%{?dist}
Summary: Metric-compatible replacements for Courier, Arial and Times
License: OFL-1.1
URL: https://github.com/liberationfonts/liberation-fonts
Source0: https://github.com/liberationfonts/liberation-fonts/files/7261482/liberation-fonts-ttf-%{version}.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: fonts-srpm-macros
Requires: fontconfig

%description
The Liberation fonts are metric-compatible with Courier, Arial and Times New
Roman, provided as TrueType fonts.

%prep
%oreon_sha256
%autosetup -n liberation-fonts-ttf-%{version}

%build

%install
install -d %{buildroot}%{fontdir}
install -p -m 0644 *.ttf %{buildroot}%{fontdir}

%check
test "$(ls %{buildroot}%{fontdir}/*.ttf | wc -l)" -eq 12

%files
%license LICENSE
%dir %{fontdir}
%{fontdir}/*.ttf

%changelog
%autochangelog
