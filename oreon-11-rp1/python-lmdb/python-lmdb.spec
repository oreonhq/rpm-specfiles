%global source0_hash 260f443640ee2da3cfd059a84258659319ff39ca912c16bf9748c324076b9d09
Name:           python-lmdb
Version:        2.3.0
Release:        1%{?dist}
Summary:        Universal Python binding for the LMDB _Lightning_ Database
License:        OLDAP-2.8
URL:            http://github.com/jnwatson/py-lmdb/
Source0:        https://files.pythonhosted.org/packages/source/l/lmdb/lmdb-%{version}.tar.gz
Patch:          https://github.com/jnwatson/py-lmdb/pull/368.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cffi) >= 0.8
Requires:       python3-lmdb = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-lmdb
Summary:        Universal Python binding for the LMDB _Lightning_ Database
%description -n python3-lmdb

%prep
%global oreon_srcdir lmdb-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-lmdb usr/lib/python3*/site-packages/lmdb* usr/lib64/python3*/site-packages/lmdb* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/lmdb* usr/lib64/python3*/site-packages/lmdb* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-lmdb -f %{oreon_filedir}/python3-lmdb.list

%changelog

%autochangelog
