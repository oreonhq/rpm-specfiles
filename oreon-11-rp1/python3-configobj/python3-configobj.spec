# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 03c881bbf23aa07bccf1b837005975993c4ab4427ba57f959afdd9d1a2386848
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-configobj
Version: 5.0.9
Release: 1%{?dist}
Summary: Config file reading, writing and validation.
License: BSD-3-Clause
URL: https://pypi.org/project/configobj/
Source0: https://files.pythonhosted.org/packages/f5/c4/c7f9e41bc2e5f8eeae4a08a01c91b2aea3dfab40a3e14b25e87e7db8d501/configobj-5.0.9.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-wheel
BuildRequires: python3-setuptools
Requires: python3

%description
Config file reading, writing and validation.

%prep
%oreon_sha256
%autosetup -n configobj-5.0.9

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
PYTHONPATH=%{buildroot}%{python3_sitelib}:%{buildroot}%{python3_sitearch} python3 -c 'import configobj'

%files -f %{_builddir}/%{name}.files
