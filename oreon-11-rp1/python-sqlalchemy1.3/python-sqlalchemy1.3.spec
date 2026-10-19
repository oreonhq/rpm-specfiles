%global source0_hash baa8521e8ee9f24e75dfc7aaabc08020e551ef0d48d7c3e3536f5cddf277586b
Name:           python-sqlalchemy
Version:        2.0.54
Release:        1%{?dist}
Summary:        Database Abstraction Library
License:        MIT
URL:            https://docs.sqlalchemy.org
Source0:        https://files.pythonhosted.org/packages/source/s/sqlalchemy/sqlalchemy-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 0.29.24
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-sqlalchemy = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-sqlalchemy
Summary:        Database Abstraction Library
%description -n python3-sqlalchemy

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir sqlalchemy-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sqlalchemy usr/lib/python3*/site-packages/sqlalchemy* usr/lib64/python3*/site-packages/sqlalchemy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sqlalchemy* usr/lib64/python3*/site-packages/sqlalchemy* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sqlalchemy -f %{oreon_filedir}/python3-sqlalchemy.list

%changelog

%autochangelog
