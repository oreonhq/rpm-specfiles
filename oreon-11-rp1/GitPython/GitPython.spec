# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 0f1229ec5c057bdabdeeda8bda4f17bda679ab33dbccc00f24e6a480553c8613
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global srcname GitPython

Name:           %{srcname}
Version:        3.2.1
Release:        1%{?dist}
Summary:        Python Git Library

License:        BSD-3-Clause
URL:            https://github.com/gitpython-developers/GitPython
Source:         %{pypi_source gitpython}

BuildArch:      noarch

%global _description %{expand:
GitPython is a python library used to interact with git repositories,
high-level like git-porcelain, or low-level like git-plumbing.

It provides abstractions of git objects for easy access of repository data, and
additionally allows you to access the git repository more directly using either
a pure python implementation, or the faster, but more resource intensive git
command implementation.

The object database implementation is optimized for handling large quantities
of objects and large datasets, which is achieved by using low-level structures
and data streaming.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires: oreon-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  git-core
Requires:       git-core

%description -n python3-%{srcname} %{_description}

%prep
%oreon_sha256
%autosetup -n gitpython-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l git

%check
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%doc CHANGES AUTHORS

%changelog
%autochangelog
