%global source0_hash 16720f33d7dcfc7ef906cad8d182f05ba7e5d2c35c6be6a5bc17ce5edfc428b2
Name:           python-pymssql
Version:        2.4.1
Release:        1%{?dist}
Summary:        DB-API interface to Microsoft SQL Server for Python. _new Cython-based version_
License:        ...
URL:            https://github.com/pymssql/pymssql
Source0:        https://files.pythonhosted.org/packages/source/p/pymssql/pymssql-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 3.1.0
BuildRequires:  python3dist(packaging) >= 24.2
BuildRequires:  python3dist(setuptools) > 80.0
BuildRequires:  python3dist(setuptools-scm[toml]) >= 8.0
BuildRequires:  python3dist(wheel) >= 0.36.2
Requires:       python3-pymssql = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pymssql
Summary:        DB-API interface to Microsoft SQL Server for Python. _new Cython-based version_
%description -n python3-pymssql

%prep
%global oreon_srcdir pymssql-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pymssql usr/lib/python3*/site-packages/pymssql* usr/lib64/python3*/site-packages/pymssql* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pymssql* usr/lib64/python3*/site-packages/pymssql* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pymssql -f %{oreon_filedir}/python3-pymssql.list

%changelog

%autochangelog
