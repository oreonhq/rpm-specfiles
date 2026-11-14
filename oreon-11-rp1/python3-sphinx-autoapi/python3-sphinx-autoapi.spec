# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: MIT

%global source0_hash 0b2a47beac401c5fe437fbcd41c650c6cdc072234e576f56ef04456805bddabf

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-sphinx-autoapi
Version: 3.9.0
Release: 1%{?dist}
Summary: Sphinx API documentation generator
License: MIT
URL: https://github.com/readthedocs/sphinx-autoapi
Source0: https://files.pythonhosted.org/packages/4b/e8/12412b8c25b7e22fc6677ce84aceb278e856a688478e0a3c6eb211281c75/sphinx_autoapi-%{version}.tar.gz
BuildArch: noarch
Provides: python3dist(sphinx-autoapi) = %{version}

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-wheel
BuildRequires: python3-sphinx
BuildRequires: python3-astroid
BuildRequires: python3-jinja2
BuildRequires: python3-pyyaml
Requires: python3
Requires: python3-sphinx
Requires: python3-astroid
Requires: python3-jinja2
Requires: python3-pyyaml

%description
Sphinx AutoAPI generates API docs by parsing source without importing it.

%prep
%oreon_sha256
%autosetup -n sphinx_autoapi-%{version}

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import autoapi'

%files -f %{_builddir}/%{name}.files

%changelog
%autochangelog
