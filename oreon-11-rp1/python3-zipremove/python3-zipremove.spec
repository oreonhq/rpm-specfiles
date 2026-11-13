# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 3c5957c115447b54299d3a23128764b59c4558fc98c4b878ff2dbc5db8a62021
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-zipremove
Version: 0.10.0
Release: 1%{?dist}
Summary: Extend zipfile with remove helpers
License: MIT
URL: https://pypi.org/project/zipremove/
Source0: https://files.pythonhosted.org/packages/92/30/47d65b9213f52df8a51f603cb0a2e5ef02c22172a8a17805e46c3beabb0d/zipremove-0.10.0.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-wheel
Requires: python3

%description
Extend zipfile with remove helpers

%prep
%oreon_sha256
%autosetup -n zipremove-0.10.0

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
PYTHONPATH=%{buildroot}%{python3_sitelib}:%{buildroot}%{python3_sitearch} python3 -c 'import zipremove'

%files -f %{_builddir}/%{name}.files
