# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash cafe209d064a6efb88cb45a03e97981ff8832802b2b5d009dde0197a3b7b41c8
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global         pypi_name setproctitle

Name:           python-%{pypi_name}
Version:        1.3.8
Release:        %{autorelease}
Summary:        Python module to customize a process title

License:        BSD-3-Clause
URL:            https://github.com/dvarrazzo/py-setproctitle
Source0:        https://files.pythonhosted.org/packages/source/s/setproctitle/setproctitle-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires:  clang
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  procps-ng

%global _description %{expand:
Python module allowing a process to change its title as displayed by
system tool such as ps and top.

It's useful in multiprocess systems, allowing to identify tasks each forked
process is busy with. This technique has been used by PostgreSQL and OpenSSH.

It is based on PostgreSQL implementation which has proven to be portable.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Python module allowing a process to change its title as displayed by
system tool such as ps and top.

It's useful in multi-process systems, allowing to identify tasks each forked
process is busy with. This technique has been used by PostgreSQL and OpenSSH.

It's based on PostgreSQL implementation which has proven to be portable.

%prep
%oreon_sha256
%autosetup -p1 -n setproctitle-%{version}

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pyproject_check_import
%pytest -v tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
