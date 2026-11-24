# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 3ce821e78ca4dd0a1d5993186b2cb98ef473ef7910c92116294f8c5f26b6b5ad
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global modname hamcrest
%global origname PyHamcrest

Name:           python-%{modname}
Version:        2.1.0
Release:        1%{?dist}
Summary:        Hamcrest matchers for Python

License:        BSD-3-Clause
URL:            https://github.com/hamcrest/PyHamcrest
Source0:        %{url}/archive/V%{version}/%{name}-%{version}.tar.gz

Patch:          https://github.com/hamcrest/PyHamcrest/pull/248.patch

BuildArch:      noarch

BuildRequires: oreon-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-xdist

%global _description \
PyHamcrest is a framework for writing matcher objects, allowing you to\
declaratively define "match" rules. There are a number of situations where\
matchers are invaluable, such as UI validation, or data filtering, but it is\
in the area of writing flexible tests that matchers are most commonly used.

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%oreon_sha256
%autosetup -n %{origname}-%{version} -p1

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
%pytest -v --deselect tests/hamcrest_unit_test/core/future_test.py

%files -n python3-%{modname} -f %{pyproject_files}

%changelog
%autochangelog
