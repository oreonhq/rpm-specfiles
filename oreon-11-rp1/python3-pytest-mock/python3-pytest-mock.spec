# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash e36576e0985e01027e999891e7a966c67822d40c89ef1b4c8b6e22737e3590b4

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-pytest-mock
Version: 3.17.0
Release: 3%{?dist}
Summary: Thin-wrapper around mock for easier use with pytest
License: MIT
URL: https://github.com/pytest-dev/pytest-mock/
Source0: https://files.pythonhosted.org/packages/source/p/pytest-mock/pytest_mock-%{version}.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-setuptools_scm
BuildRequires: python3-wheel
BuildRequires: python3-pytest
BuildRequires: python3-pytest-asyncio >= 1.5.0-3

Requires: python3-pytest

%description
This plugin provides a mocker fixture which is a thin-wrapper around the
patching API provided by the mock package.

%prep
%oreon_sha256
%autosetup -n pytest_mock-%{version}

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
PYTHONPATH="%{buildroot}%{python3_sitelib}" python3 -m pytest -q
%oreon_filelist

%files -f %{_builddir}/%{name}.files

%changelog
%autochangelog
