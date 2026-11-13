# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 67f4b9c50da0dedf52af349e7749a80a9057a5031199791b906c3bb3ae878960
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-iniconfig
Version: 2.3.1
Release: 1%{?dist}
Summary: brain-dead simple config-ini parsing
License: MIT
URL: https://pypi.org/project/iniconfig/
Source0: https://files.pythonhosted.org/packages/01/e1/2069291243c926a2ff1cd706c7f3eeb9b62144bf60f77c9fb9ff2fb26bd3/iniconfig-2.3.1.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-wheel
BuildRequires: python3-setuptools
BuildRequires: python3-setuptools_scm
Requires: python3

%description
brain-dead simple config-ini parsing

%prep
%oreon_sha256
%autosetup -n iniconfig-2.3.1

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
PYTHONPATH=%{buildroot}%{python3_sitelib}:%{buildroot}%{python3_sitearch} python3 -c 'import iniconfig'

%files -f %{_builddir}/%{name}.files
