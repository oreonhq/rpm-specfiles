%global source0_hash 8d1a39bf6b192940cc5db5264eeefc1b20dd184f8b83b1303b078743744f5943
Name:           python-xyzservices
Version:        2026.9.1
Release:        1%{?dist}
Summary:        Source of XYZ tiles providers
License:        BSD-3-Clause
URL:            https://github.com/geopandas/xyzservices
Source0:        https://files.pythonhosted.org/packages/source/x/xyzservices/xyzservices-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.2
Requires:       python3-xyzservices = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-xyzservices
Summary:        Source of XYZ tiles providers
%description -n python3-xyzservices

%prep
%global oreon_srcdir xyzservices-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-xyzservices usr/lib/python3*/site-packages/xyzservices* usr/lib64/python3*/site-packages/xyzservices* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/xyzservices* usr/lib64/python3*/site-packages/xyzservices* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-xyzservices -f %{oreon_filedir}/python3-xyzservices.list

%changelog

%autochangelog
