# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash c158c7a71ced2a77471ae851089b4ea15c15fce968d3f0105a15819666cd641a
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global srcname constantly

%global common_description %{expand:
A library that provides symbolic constant support. It includes collections and
constants with text, numeric, and bit flag values. Originally
twisted.python.constants from the Twisted project.}

%bcond bootstrap 0

Name:           python-%{srcname}
Version:        23.10.4
Release:        %{autorelease}
Summary:        Symbolic constants in Python

License:        MIT
URL:            https://github.com/twisted/constantly
Source0:        %url/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: oreon-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(sphinx-rtd-theme)

%if %{without bootstrap}
BuildRequires:  python3dist(twisted)
%endif

Patch:          fix-build-sphinx-8.patch

%description %{common_description}

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{common_description}

%package doc
Summary:        Documentation for %{name}

%description doc
%{common_description}

This is the documentation package for %{name}.

%prep
%oreon_sha256
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

sphinx-build docs html
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pyproject_check_import -e constantly.test*
%if %{without bootstrap}
%{py3_test_envvars} trial %{srcname}
%endif

%files -n python3-%{srcname} -f %{pyproject_files}

%files -n python-%{srcname}-doc
%doc html
%license LICENSE

%changelog
%autochangelog
