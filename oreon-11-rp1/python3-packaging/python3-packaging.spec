# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 94edc256424af38762eb31306eed28beb9f0efc50a8837492c9d6fd6004aed79
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-packaging
Version: 26.3
Release: 2%{?dist}
Summary: Core utilities for Python packages
License: Apache-2.0 OR BSD-2-Clause
URL: https://github.com/pypa/packaging
Source0: https://files.pythonhosted.org/packages/7d/fa/3944b40b07da9ce895c0e6303a5ab7d53da063554f534556b134a54d6093/packaging-%{version}.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3
BuildRequires: python3-rpm-macros
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-flit-core
Requires: python3

%description
Core utilities for Python packages.

%prep
%oreon_sha256
%autosetup -n packaging-%{version}

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
cd /
PYTHONPATH=%{buildroot}%{python3_sitelib} python3 -c 'import packaging, importlib.metadata; assert importlib.metadata.version("packaging")'

%files -f %{_builddir}/%{name}.files

%changelog
%autochangelog
