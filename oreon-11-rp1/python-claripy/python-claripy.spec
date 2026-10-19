%global source0_hash 6ec519ab39d851496c5a1f467b2d723c1f473eae6096df90cd567be6bcd646ca
Name:           python-claripy
Version:        9.3.5
Release:        1%{?dist}
Summary:        An abstraction layer for constraint solvers
License:        BSD-2-Clause
URL:            https://github.com/angr/claripy
Source0:        https://files.pythonhosted.org/packages/source/c/claripy/claripy-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.0
Requires:       python3-claripy = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-claripy
Summary:        An abstraction layer for constraint solvers
# oreon:reqs
Requires:       python3dist(z3-solver) == 4.13.0.0
# /oreon:reqs
%description -n python3-claripy

%prep
%global oreon_srcdir claripy-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-claripy usr/lib/python3*/site-packages/claripy* usr/lib64/python3*/site-packages/claripy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/claripy* usr/lib64/python3*/site-packages/claripy* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-claripy -f %{oreon_filedir}/python3-claripy.list

%changelog

%autochangelog
