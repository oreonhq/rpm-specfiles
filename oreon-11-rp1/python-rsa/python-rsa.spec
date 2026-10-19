%global source0_hash e7bdbfdb5497da4c07dfd35530e1a902659db6ff241e39d9953cad06ebd0ae75
Name:           python-rsa
Version:        4.9.1
Release:        1%{?dist}
Summary:        Pure-Python RSA implementation
License:        Apache-2.0
URL:            https://stuvel.eu/rsa
Source0:        https://files.pythonhosted.org/packages/source/r/rsa/rsa-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-rsa = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-rsa
Summary:        Pure-Python RSA implementation
%description -n python3-rsa

%prep
%global oreon_srcdir rsa-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-rsa usr/lib/python3*/site-packages/rsa* usr/lib64/python3*/site-packages/rsa* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/rsa* usr/lib64/python3*/site-packages/rsa* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-rsa -f %{oreon_filedir}/python3-rsa.list

%changelog

%autochangelog
