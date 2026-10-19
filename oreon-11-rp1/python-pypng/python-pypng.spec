%global source0_hash 739c433ba96f078315de54c0db975aee537cbc3e1d0ae4ed9aab0ca1e427e2c1
Name:           python-pypng
Version:        0.20220715.0
Release:        1%{?dist}
Summary:        Pure Python library for saving and loading PNG images
License:        MIT
URL:            https://gitlab.com/drj11/pypng
Source0:        https://files.pythonhosted.org/packages/source/p/pypng/pypng-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 35.0.2
Requires:       python3-pypng = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pypng
Summary:        Pure Python library for saving and loading PNG images
%description -n python3-pypng

%prep
%global oreon_srcdir pypng-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pypng usr/lib/python3*/site-packages/pypng* usr/lib64/python3*/site-packages/pypng* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pypng* usr/lib64/python3*/site-packages/pypng* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pypng -f %{oreon_filedir}/python3-pypng.list

%changelog

%autochangelog
