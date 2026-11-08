# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 0137fb05990d35f1275a587e9aee6d56da821fc83491a0fb838183be43f66d6d
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

%global py3_sitelib %(python3 -c 'import sysconfig; print(sysconfig.get_path("purelib", "posix_prefix", {"base": "/usr"}))')

Name: python3-jinja2
Version: 3.1.6
Release: 11%{?dist}
Summary: Template engine for Python
License: BSD-3-Clause
URL: https://github.com/pallets/jinja
Source0: https://files.pythonhosted.org/packages/source/j/jinja2/jinja2-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: python3
Requires: python3
Requires: python3-markupsafe

%description
Template engine for Python.

%prep
%oreon_sha256
%autosetup -n jinja2-%{version} -p1

%build

%install
mkdir -p %{buildroot}%{py3_sitelib}
cp -a src/jinja2 %{buildroot}%{py3_sitelib}/
find %{buildroot} -type f -exec grep -I -l -E '^#! */usr/bin/env python' {} + | while read -r f; do
  sed -i '1s|^#! */usr/bin/env python.*|#!/usr/bin/python3|' "$f"
done
%files
%license LICENSE.txt
%{py3_sitelib}/jinja2/
