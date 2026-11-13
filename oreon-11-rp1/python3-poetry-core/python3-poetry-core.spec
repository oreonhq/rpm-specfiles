# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 81d04c9253b19d0604718268d781867c8f7b2128e5b25bbf1e84141eec6b89c4
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-poetry-core
Version: 2.5.0
Release: 1%{?dist}
Summary: Poetry PEP 517 build backend
License: MIT
URL: https://pypi.org/project/poetry-core/
Source0: https://files.pythonhosted.org/packages/42/b5/50f1fda26c4fe5b1d6ce5cdf0391bdfa1ca12fdcb8ad68344d5cf678fc90/poetry_core-2.5.0.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-wheel
BuildRequires: python3-setuptools
Requires: python3

%description
Poetry PEP 517 build backend.

%prep
%oreon_sha256
%autosetup -n poetry_core-%{version}

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
PYTHONPATH=%{buildroot}%{python3_sitelib}:%{buildroot}%{python3_sitearch} python3 -c 'import poetry.core'

%files -f %{_builddir}/%{name}.files
