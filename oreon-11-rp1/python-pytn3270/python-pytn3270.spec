%global source0_hash d20e194f5d0bee61b149e0dc319c718c97f76b38173171e9b074177500a3c05d
Name:           python-pytn3270
Version:        0.16.0
Release:        1%{?dist}
Summary:        TN3270 library
License:        ISC
URL:            https://github.com/lowobservable/pytn3270
Source0:        https://files.pythonhosted.org/packages/source/p/pytn3270/pytn3270-%{version}.tar.gz
BuildArch:      noarch
Patch:          %{url}/pull/3.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pytn3270 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pytn3270
Summary:        TN3270 library
%description -n python3-pytn3270

%prep
%global oreon_srcdir pytn3270-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pytn3270 usr/lib/python3*/site-packages/pytn3270* usr/lib64/python3*/site-packages/pytn3270* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pytn3270* usr/lib64/python3*/site-packages/pytn3270* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pytn3270 -f %{oreon_filedir}/python3-pytn3270.list

%changelog

%autochangelog
