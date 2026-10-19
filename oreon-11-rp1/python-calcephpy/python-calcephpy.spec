%global source0_hash abf52b8d2898299ff837f90ed9824cc40d70745700b440374d6f375a86a5e831
Name:           python-calcephpy
Version:        5.0.0
Release:        1%{?dist}
Summary:        Python interface for the CALCEPH Library
License:        ...
URL:            https://calceph.imcce.fr/
Source0:        https://files.pythonhosted.org/packages/source/c/calcephpy/calcephpy-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-calcephpy = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-calcephpy
Summary:        Python interface for the CALCEPH Library
%description -n python3-calcephpy

%prep
%global oreon_srcdir calcephpy-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-calcephpy usr/lib/python3*/site-packages/calcephpy* usr/lib64/python3*/site-packages/calcephpy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/calcephpy* usr/lib64/python3*/site-packages/calcephpy* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-calcephpy -f %{oreon_filedir}/python3-calcephpy.list

%changelog

%autochangelog
