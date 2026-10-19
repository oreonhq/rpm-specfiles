%global source0_hash 1f7a7c8164fac636382aa7b0d70279ad5581379748fc17a20bc0be8fe574c259
Name:           python-pykcs11
Version:        1.5.20
Release:        1%{?dist}
Summary:        A Full PKCS#11 wrapper for Python
License:        GPL-2.0-or-later
URL:            https://github.com/LudovicRousseau/PyKCS11
Source0:        https://files.pythonhosted.org/packages/source/p/pykcs11/pykcs11-%{version}.tar.gz
Patch:          %{url}/pull/113.patch#/Add-Fedora-PyKCS11-library-location-search-path.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pykcs11 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pykcs11
Summary:        A Full PKCS#11 wrapper for Python
%description -n python3-pykcs11

%prep
%global oreon_srcdir pykcs11-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pykcs11 usr/lib/python3*/site-packages/pykcs11* usr/lib64/python3*/site-packages/pykcs11* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pykcs11* usr/lib64/python3*/site-packages/pykcs11* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pykcs11 -f %{oreon_filedir}/python3-pykcs11.list

%changelog

%autochangelog
