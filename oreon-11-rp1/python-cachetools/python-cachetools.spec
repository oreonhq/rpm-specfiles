# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 30ac523adfc118b51d2b2e7bad8a0ddb31370dfe2700c7f10ca224f36ccf81e0
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           python-cachetools
Version:        8.0.2
Release:        %{autorelease}
Summary:        Extensible memoizing collections and decorators

License:        MIT
URL:            https://pypi.python.org/pypi/cachetools
Source0:        %{pypi_source cachetools}

BuildArch:      noarch
BuildRequires: oreon-rpm-macros
BuildRequires:  python3-devel

BuildRequires:  python3-pytest

%global _description\
This module provides various memoizing collections and decorators,\
including a variant of the Python 3 Standard Library @lru_cache\
function decorator.\
\
This module provides multiple cache implementations based on different\
cache algorithms, as well as decorators for easily memoizing function\
and method calls.\

%description %_description

%package -n python3-cachetools
Summary:        %{summary}

%description -n python3-cachetools %_description

%prep
%oreon_sha256
%autosetup -n cachetools-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l cachetools

%check
%pytest

%files -n python3-cachetools -f %{pyproject_files}
%doc CHANGELOG.rst README.rst

%changelog
%autochangelog
