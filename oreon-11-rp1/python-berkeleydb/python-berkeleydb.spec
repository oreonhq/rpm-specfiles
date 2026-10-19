%global source0_hash 7afa53143d754c6bb2c85656c1325ebae518adcfcd1b59e13cc2abb88ddf758e
Name:           python-berkeleydb
Version:        18.1.15
Release:        1%{?dist}
Summary:        Python bindings for Oracle Berkeley DB
License:        BSD-3-Clause
URL:            https://www.jcea.es/programacion/pybsddb.htm
Source0:        https://files.pythonhosted.org/packages/source/b/berkeleydb/berkeleydb-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 80.9.0
Requires:       python3-berkeleydb = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-berkeleydb
Summary:        Python bindings for Oracle Berkeley DB
%description -n python3-berkeleydb

%prep
%global oreon_srcdir berkeleydb-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-berkeleydb usr/lib/python3*/site-packages/berkeleydb* usr/lib64/python3*/site-packages/berkeleydb* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/berkeleydb* usr/lib64/python3*/site-packages/berkeleydb* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-berkeleydb -f %{oreon_filedir}/python3-berkeleydb.list

%changelog

%autochangelog
