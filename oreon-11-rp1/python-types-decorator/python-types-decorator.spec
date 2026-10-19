%global source0_hash 2890f05fe3c65546baf5000fd5f1eed4d1c95bae5516e23e1735b7b5a4dd98c6
Name:           python-types-decorator
Version:        5.2.0.20260712
Release:        1%{?dist}
Summary:        Typing stubs for decorator
License:        Apache-2.0
URL:            https://github.com/python/typeshed
Source0:        https://files.pythonhosted.org/packages/source/t/types_decorator/types_decorator-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 82.0.1
Requires:       python3-types-decorator = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-types-decorator
Summary:        Typing stubs for decorator
%description -n python3-types-decorator

%prep
%global oreon_srcdir types_decorator-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-types-decorator usr/lib/python3*/site-packages/types_decorator* usr/lib64/python3*/site-packages/types_decorator* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/types_decorator* usr/lib64/python3*/site-packages/types_decorator* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-types-decorator -f %{oreon_filedir}/python3-types-decorator.list

%changelog

%autochangelog
