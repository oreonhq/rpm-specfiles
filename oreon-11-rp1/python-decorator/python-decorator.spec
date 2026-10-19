%global source0_hash 4cbcdd55a6efadb9dbea26b858f4fb3264567b52d69ca0d25b721b553f60ea82
Name:           python-decorator
Version:        5.3.1
Release:        1%{?dist}
Summary:        Decorators for Humans
License:        BSD-2-Clause
URL:            ...
Source0:        https://files.pythonhosted.org/packages/source/d/decorator/decorator-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.0
Requires:       python3-decorator = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-decorator
Summary:        Decorators for Humans
%description -n python3-decorator

%prep
%global oreon_srcdir decorator-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-decorator usr/lib/python3*/site-packages/decorator* usr/lib64/python3*/site-packages/decorator* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/decorator* usr/lib64/python3*/site-packages/decorator* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-decorator -f %{oreon_filedir}/python3-decorator.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.2.1-1
- Prepare for Oreon 11 (RP1)
