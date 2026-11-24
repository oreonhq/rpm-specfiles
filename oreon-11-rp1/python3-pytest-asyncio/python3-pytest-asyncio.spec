# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 92c8fa83ca419fd0d4bd6a34df6520dae435841d3733c319343249492adf37f7

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-pytest-asyncio
Version: 1.5.0
Release: 2%{?dist}
Summary: Pytest support for asyncio
License: Apache-2.0
URL: https://github.com/pytest-dev/pytest-asyncio
Source0: https://files.pythonhosted.org/packages/source/p/pytest-asyncio/pytest_asyncio-%{version}.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-setuptools_scm
BuildRequires: python3-wheel
BuildRequires: python3-pytest
BuildRequires: python3-hypothesis

Requires: python3-pytest >= 8.4

%description
pytest-asyncio is a pytest plugin. It facilitates testing of code that
uses the asyncio library.

%prep
%oreon_sha256
%autosetup -n pytest_asyncio-%{version}

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="%{buildroot}%{python3_sitelib}" python3 -m pytest -q

%files -f %{_builddir}/%{name}.files

%changelog
%autochangelog
