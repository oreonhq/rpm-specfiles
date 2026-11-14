# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ac7742a6cc6c25a2c35e9292dfd554b897b517d2dec26891a2e8debf205cb94a
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-freezegun
Version: 1.5.5
Release: 1%{?dist}
Summary: Let your Python tests travel through time
License: Apache-2.0
URL: https://pypi.org/project/freezegun/
Source0: https://files.pythonhosted.org/packages/95/dd/23e2f4e357f8fd3bdff613c1fe4466d21bfb00a6177f238079b17f7b1c84/freezegun-1.5.5.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-wheel
BuildRequires: python3-setuptools
BuildRequires: python3-dateutil
Requires: python3
Requires: python3-dateutil

%description
Let your Python tests travel through time

%prep
%oreon_sha256
%autosetup -n freezegun-1.5.5

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
PYTHONPATH=%{buildroot}%{python3_sitelib}:%{buildroot}%{python3_sitearch} python3 -c 'import freezegun'

%files -f %{_builddir}/%{name}.files
