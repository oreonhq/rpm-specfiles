%global source0_hash d36784fc2dae69523ba4b79c7d1d1b4d6e83e87836874f111262f4db940b16a6
Name:           python-psycopg2
Version:        2.9.13
Release:        1%{?dist}
Summary:        psycopg2 - Python-PostgreSQL Database Adapter
License:        ...
URL:            https://psycopg.org/
Source0:        https://files.pythonhosted.org/packages/source/p/psycopg2/psycopg2-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 70.1
Requires:       python3-psycopg2 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-psycopg2
Summary:        psycopg2 - Python-PostgreSQL Database Adapter
%description -n python3-psycopg2

%prep
%global oreon_srcdir psycopg2-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-psycopg2 usr/lib/python3*/site-packages/psycopg2* usr/lib64/python3*/site-packages/psycopg2* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/psycopg2* usr/lib64/python3*/site-packages/psycopg2* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-psycopg2 -f %{oreon_filedir}/python3-psycopg2.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.9.10-5
- Prepare for Oreon 11 (RP1)
