%global source0_hash dbfd6ab26c30ae710215ebabf590441d551bf0a8a6c95b33c3d0738062a56562
Name:           python-pyjwkest
Version:        1.4.4
Release:        1%{?dist}
Summary:        Python implementation of JWT, JWE, JWS and JWK
License:        ...
URL:            https://github.com/IdentityPython/pyjwkest
Source0:        https://files.pythonhosted.org/packages/source/p/pyjwkest/pyjwkest-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64
Requires:       python3-pyjwkest = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyjwkest
Summary:        Python implementation of JWT, JWE, JWS and JWK
%description -n python3-pyjwkest

%prep
%global oreon_srcdir pyjwkest-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyjwkest usr/lib/python3*/site-packages/pyjwkest* usr/lib64/python3*/site-packages/pyjwkest* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyjwkest* usr/lib64/python3*/site-packages/pyjwkest* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyjwkest -f %{oreon_filedir}/python3-pyjwkest.list

%changelog

%autochangelog
