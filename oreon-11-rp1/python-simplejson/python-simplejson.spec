%global source0_hash 6ae4186f90362e9c03c80a1cd5062a20f3a11ac9d391f7ee0ef0701a0e2b7394
Name:           python-simplejson
Version:        4.1.2
Release:        1%{?dist}
Summary:        Simple, fast, extensible JSON encoder/decoder for Python
License:        MIT OR AFL-2.1
URL:            https://github.com/simplejson/simplejson
Source0:        https://files.pythonhosted.org/packages/source/s/simplejson/simplejson-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 42
Requires:       python3-simplejson = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-simplejson
Summary:        Simple, fast, extensible JSON encoder/decoder for Python
%description -n python3-simplejson

%prep
%global oreon_srcdir simplejson-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-simplejson usr/lib/python3*/site-packages/simplejson* usr/lib64/python3*/site-packages/simplejson* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/simplejson* usr/lib64/python3*/site-packages/simplejson* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-simplejson -f %{oreon_filedir}/python3-simplejson.list

%changelog

%autochangelog
