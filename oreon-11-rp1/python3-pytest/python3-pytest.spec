# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 97c4f3b1f3c7414aa36465e09b8220f1d03627993bd51b1282e193753c80557b

Name: python3-pytest
Version: 9.2.0
Release: 1%{?dist}
Summary: pytest: simple powerful testing with Python
License: MIT
URL: https://pypi.org/project/pytest/
Source0: https://files.pythonhosted.org/packages/source/p/pytest/pytest-%{version}.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-setuptools_scm
BuildRequires: python3-iniconfig
BuildRequires: python3-packaging
BuildRequires: python3-pluggy
BuildRequires: python3-pygments
Requires: python3
Requires: python3-iniconfig
Requires: python3-packaging
Requires: python3-pluggy
Requires: python3-pygments

%description
pytest: simple powerful testing with Python

%prep
%oreon_sha256
%autosetup -n pytest-%{version}

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl

%check
python3 -c 'import pytest'

%files
%license LICENSE
%{_bindir}/pytest
%{_bindir}/py.test
%{python3_sitelib}/_pytest
%{python3_sitelib}/pytest
%{python3_sitelib}/pytest*.dist-info

%changelog
%autochangelog
