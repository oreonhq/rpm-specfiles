%global source0_hash 0b48f17296f869db89221c3bde463fdff35152a4cb99ae4aaa42b0b64333fc6c
Name:           python-gssapi
Version:        1.12.0
Release:        1%{?dist}
Summary:        Python GSSAPI Wrapper
License:        ISC
URL:            https://github.com/pythongssapi/python-gssapi
Source0:        https://files.pythonhosted.org/packages/source/g/gssapi/gssapi-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) == 3.3.0
BuildRequires:  python3dist(setuptools) >= 40.6.0
Requires:       python3-gssapi = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-gssapi
Summary:        Python GSSAPI Wrapper
%description -n python3-gssapi

%prep
%global oreon_srcdir gssapi-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-gssapi usr/lib/python3*/site-packages/gssapi* usr/lib64/python3*/site-packages/gssapi* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/gssapi* usr/lib64/python3*/site-packages/gssapi* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-gssapi -f %{oreon_filedir}/python3-gssapi.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.7.3-16
- Import
