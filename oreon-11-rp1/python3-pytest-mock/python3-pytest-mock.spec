# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 1849a238f6f396da19762269de72cb1814ab44416fa73a8686deac10b0d87a0f

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-pytest-mock
Version: 3.15.1
Release: 1%{?dist}
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
python3 -m pytest -q

%files -f %{_builddir}/%{name}.files

%changelog
%autochangelog
