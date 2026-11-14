# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash d76623373421df22fb4cf8817020cbb7ef15c725b9d5e45f17e189bfc384190f
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-pyyaml
Version: 6.0.3
Release: 1%{?dist}
Summary: YAML parser and emitter for Python
License: MIT
URL: https://pypi.org/project/pyyaml/
Source0: https://files.pythonhosted.org/packages/05/8e/961c0007c59b8dd7729d542c61a4d537767a59645b82a0b521206e1e25c2/pyyaml-6.0.3.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-cython
BuildRequires: gcc
BuildRequires: libyaml-devel
Requires: python3
Requires: libyaml

%description
YAML parser and emitter for Python

%prep
%oreon_sha256
%autosetup -n pyyaml-6.0.3

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
PYTHONPATH=%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib} python3 -c 'import yaml'

%files -f %{_builddir}/%{name}.files

%changelog
%autochangelog
