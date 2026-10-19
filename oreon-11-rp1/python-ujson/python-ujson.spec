%global source0_hash 80e23393feb707582e0ad495c397a4477b646d08094d2df64f7316f9fafd8aae
Name:           python-ujson
Version:        6.0.0
Release:        1%{?dist}
Summary:        Ultra fast JSON encoder and decoder for Python
License:        BSD-3-Clause AND TCL
URL:            https://github.com/ultrajson/ultrajson
Source0:        https://files.pythonhosted.org/packages/source/u/ujson/ujson-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 80
BuildRequires:  python3dist(setuptools-scm[simple]) >= 9.2
Requires:       python3-ujson = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-ujson
Summary:        Ultra fast JSON encoder and decoder for Python
%description -n python3-ujson

%prep
%global oreon_srcdir ujson-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ujson usr/lib/python3*/site-packages/ujson* usr/lib64/python3*/site-packages/ujson* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ujson* usr/lib64/python3*/site-packages/ujson* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-ujson -f %{oreon_filedir}/python3-ujson.list

%changelog

%autochangelog
