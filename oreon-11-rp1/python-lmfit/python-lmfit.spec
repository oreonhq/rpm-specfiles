%global source0_hash f40628814051140ac6a7a7c17ee075bb33fac0b00ccd32ff8bd73eebb35e0f40
Name:           python-lmfit
Version:        1.3.4
Release:        1%{?dist}
Summary:        Non-Linear Least Squares Minimization
License:        BSD-3-Clause
URL:            https://github.com/lmfit/lmfit-py
Source0:        https://github.com/lmfit/lmfit-py/archive/%{version}/lmfit-py-%{version}.tar.gz
BuildArch:      noarch
%ifnarch %{ix86}
%endif
%global common_description %{expand:
The lmfit Python library provides tools for non-linear least-squares
minimization and curve fitting. The goal is to make these optimization
algorithms more flexible, more comprehensible, and easier to use, with the key
feature of casting variables in minimization and fitting routines as named
parameters that can have many attributes beside just a current value.}
# oreon:deps
BuildRequires:  python3dist(emcee)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(pandas)
# /oreon:deps
%description %{common_description}

%package -n     python3-lmfit
Summary:        Non-Linear Least Squares Minimization
%description -n python3-lmfit %{common_description}

%build -p

export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%prep
%oreon_prep
%install
%pyproject_install
%oreon_autofiles python3-lmfit usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest -rs
%files -f %{oreon_filedir}/main.list
%files -n python3-lmfit -f %{oreon_filedir}/python3-lmfit.list

%changelog

%autochangelog
