%global source0_hash e1eadb6d2ccaa4b7a876a1c81b6ff0307fa7a08b56f7799862a50207c2e65a05
Name:           python-pandas-datareader
Version:        0.11.1
Release:        1%{?dist}
Summary:        Pandas-compatible data readers. Formerly a component of pandas.
License:        BSD-3-Clause
URL:            https://pandas.pydata.org
Source0:        https://files.pythonhosted.org/packages/source/p/pandas_datareader/pandas_datareader-%{version}.tar.gz
BuildArch:      noarch
Patch: pandas-datareader-python312.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64
BuildRequires:  python3dist(setuptools-scm) < 9
BuildRequires:  python3dist(setuptools-scm) >= 8
Requires:       python3-pandas-datareader = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pandas-datareader
Summary:        Pandas-compatible data readers. Formerly a component of pandas.
%description -n python3-pandas-datareader

%prep
%global oreon_srcdir pandas_datareader-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pandas-datareader usr/lib/python3*/site-packages/pandas_datareader* usr/lib64/python3*/site-packages/pandas_datareader* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pandas_datareader* usr/lib64/python3*/site-packages/pandas_datareader* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pandas-datareader -f %{oreon_filedir}/python3-pandas-datareader.list

%changelog

%autochangelog
