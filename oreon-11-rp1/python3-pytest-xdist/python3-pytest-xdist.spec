# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 7e578125ec9bc6050861aa93f2d59f1d8d085595d6551c2c90b6f4fad8d3a9f1
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-pytest-xdist
Version: 3.8.0
Release: 1%{?dist}
Summary: pytest xdist plugin for distributed testing, most importantly acros...
License: MIT
URL: https://pypi.org/project/pytest-xdist/
Source0: https://files.pythonhosted.org/packages/78/b4/439b179d1ff526791eb921115fca8e44e596a13efeda518b9d845a619450/pytest_xdist-3.8.0.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-setuptools_scm
BuildRequires: python3-execnet
BuildRequires: python3-pytest
Requires: python3
Requires: python3-execnet
Requires: python3-pytest

%description
pytest xdist plugin for distributed testing, most importantly acros...

%prep
%oreon_sha256
%autosetup -n pytest_xdist-3.8.0

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import xdist'

%files -f %{_builddir}/%{name}.files
