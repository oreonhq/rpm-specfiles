# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 36b4462704450798197d090809a05f4e13649d9cba9acdc557ce9517da1fd847
%global source1_hash 49b00bf423506a1ac5c1c47df6b6458c01b5e785d9a91d4f57e78fe5d344f1b8
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global pypi_name pytest-expect

Name:           python-%{pypi_name}
Version:        1.1.0
Release:        %{autorelease}
Summary:        py.test plugin to store test expectations and mark tests based on them

License:        MIT
URL:            https://github.com/gsnedders/pytest-expect
Source0:        %pypi_source
Source1:        %{url}/raw/%{version}/LICENSE

Patch:          %{url}/pull/16.patch

BuildArch:      noarch

BuildRequires: oreon-rpm-macros
BuildRequires:  python3-devel

%description
A py.test plugin that stores test expectations by saving the set of failing
tests, allowing them to be marked as xfail when running them in future.
The tests expectations are stored such that they can be distributed alongside
the tests.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
A py.test plugin that stores test expectations by saving the set of failing
tests, allowing them to be marked as xfail when running them in future.
The tests expectations are stored such that they can be distributed alongside
the tests.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%autosetup -p1 -n %{pypi_name}-%{version}
cp -p %{SOURCE1} .

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pytest_expect

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
