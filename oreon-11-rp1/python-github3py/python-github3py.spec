%global source0_hash none

%global modname github3py
%global srcname github3.py
%global altname github3

# Tests require internet connection to github.com
%bcond_with tests

Name:           python-%{modname}
Version:        4.0.1
Release:        14%{?dist}
Summary:        Python wrapper for the GitHub API

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github3py.readthedocs.org
Source0:        https://github.com/sigmavirus24/%{srcname}/archive/%{version}%{?rctag:%{rctag}}/%{modname}-%{version}%{?rctag:%{rctag}}.tar.gz

BuildArch:      noarch

%global _description \
github3.py is a comprehensive, actively developed and extraordinarily stable\
wrapper around the GitHub API (v3).

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
%{?python_provide:%python_provide python3-%{srcname}}
%{?python_provide:%python_provide python3-%{altname}}
BuildRequires:  python3-devel
BuildRequires: pyproject-rpm-macros
BuildRequires: python3dist(hatchling)

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}%{?rctag:%{rctag}}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{altname}

%if %{with tests}
%check
%tox
%endif

%files -n python3-%{modname} -f %{pyproject_files}
%license LICENSE
%doc AUTHORS.rst README.rst

%changelog
%autochangelog
