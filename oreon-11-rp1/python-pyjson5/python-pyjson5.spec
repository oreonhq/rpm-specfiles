%global source0_hash a5b0e322e847b198a50d8a1ef16d6b2b19129644dc018d76773e81ef1487ca39
Name:           python-pyjson5
Version:        2.0.1
Release:        1%{?dist}
Summary:        JSON5 serializer and parser for Python 3 written in Cython.
License:        MIT OR Apache-2.0
URL:            https://github.com/Kijewski/pyjson5
Source0:        https://files.pythonhosted.org/packages/source/p/pyjson5/pyjson5-%{version}.tar.gz
Patch0:         flags.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) < 4
BuildRequires:  python3dist(cython) >= 3.1
BuildRequires:  python3dist(setuptools) >= 61
Requires:       python3-pyjson5 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyjson5
Summary:        JSON5 serializer and parser for Python 3 written in Cython.
%description -n python3-pyjson5

%prep
%global oreon_srcdir pyjson5-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyjson5 usr/lib/python3*/site-packages/pyjson5* usr/lib64/python3*/site-packages/pyjson5* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyjson5* usr/lib64/python3*/site-packages/pyjson5* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyjson5 -f %{oreon_filedir}/python3-pyjson5.list

%changelog

%autochangelog
