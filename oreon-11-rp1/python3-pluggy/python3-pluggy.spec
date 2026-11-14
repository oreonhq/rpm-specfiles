# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash d1eaa46ebb595891b860ab086b4d09c8588af65ebd4361b8e8f4bb8920b90ba8
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-pluggy
Version: 1.7.0
Release: 1%{?dist}
Summary: plugin and hook calling mechanisms for python
License: MIT
URL: https://pypi.org/project/pluggy/
Source0: https://files.pythonhosted.org/packages/bf/db/7fc19e6f2dc92a966727031389fc2e08b558f0f25eb7403c1119ad4713cd/pluggy-1.7.0.tar.gz
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
plugin and hook calling mechanisms for python

%prep
%oreon_sha256
%autosetup -n pluggy-1.7.0

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
PYTHONPATH=%{buildroot}%{python3_sitelib}:%{buildroot}%{python3_sitearch} python3 -c 'import pluggy'

%files -f %{_builddir}/%{name}.files

%changelog
%autochangelog
