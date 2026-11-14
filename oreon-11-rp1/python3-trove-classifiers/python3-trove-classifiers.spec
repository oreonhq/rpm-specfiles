# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 0a9ebc8d4e2f3e8a22848c5258033035bec17a3012ac3fea16dbaa764489eb71
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-trove-classifiers
Version: 2026.9.21.13
Release: 1%{?dist}
Summary: Canonical source for classifiers on PyPI (pypi.org).
License: Apache Software License
URL: https://pypi.org/project/trove-classifiers/
Source0: https://files.pythonhosted.org/packages/bf/93/af436dfaa845cab5d96f0adbc1e4f3730532d37fa249e4eb796fb1d7fc82/trove_classifiers-2026.9.21.13.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-calver
Requires: python3

%description
Canonical source for classifiers on PyPI (pypi.org).

%prep
%oreon_sha256
%autosetup -n trove_classifiers-2026.9.21.13

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
PYTHONPATH=%{buildroot}%{python3_sitelib}:%{buildroot}%{python3_sitearch} python3 -c 'import trove_classifiers'

%files -f %{_builddir}/%{name}.files
