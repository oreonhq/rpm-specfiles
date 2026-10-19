%global source0_hash af40bd1a85f55db0b8b30715c858761306bd92d5590148636f75c3309e6e76bd
Name:           python-ijson
Version:        3.5.1
Release:        1%{?dist}
Summary:        Iterative JSON parser with standard Python iterator interfaces
License:        BSD-3-Clause AND ISC
URL:            https://github.com/ICRAR/ijson
Source0:        https://files.pythonhosted.org/packages/source/i/ijson/ijson-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0
Requires:       python3-ijson = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-ijson
Summary:        Iterative JSON parser with standard Python iterator interfaces
%description -n python3-ijson

%prep
%global oreon_srcdir ijson-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ijson usr/lib/python3*/site-packages/ijson* usr/lib64/python3*/site-packages/ijson* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ijson* usr/lib64/python3*/site-packages/ijson* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-ijson -f %{oreon_filedir}/python3-ijson.list

%changelog

%autochangelog
