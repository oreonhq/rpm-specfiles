%global source0_hash e2ce13869a2df98b420adeaf7429b63796e8c000969d2dfe471854c0be3d9a54
Name:           python-arpy
Version:        2.4.0
Release:        1%{?dist}
Summary:        Library for accessing _ar_ files
License:        BSD-2-Clause
URL:            ...
Source0:        https://files.pythonhosted.org/packages/source/a/arpy/arpy-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.0
Requires:       python3-arpy = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-arpy
Summary:        Library for accessing _ar_ files
%description -n python3-arpy

%prep
%global oreon_srcdir arpy-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-arpy usr/lib/python3*/site-packages/arpy* usr/lib64/python3*/site-packages/arpy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/arpy* usr/lib64/python3*/site-packages/arpy* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-arpy -f %{oreon_filedir}/python3-arpy.list

%changelog

%autochangelog
