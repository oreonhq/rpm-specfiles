%global source0_hash f1303ef2eec81262a4b708c3e858afe58d7c75ad91c1c05266eda7673369859a
Name:           python-kiwisolver
Version:        1.5.1
Release:        1%{?dist}
Summary:        A fast implementation of the Cassowary constraint solver
License:        ...
URL:            https://github.com/nucleic/kiwi
Source0:        https://files.pythonhosted.org/packages/source/k/kiwisolver/kiwisolver-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cppy) >= 1.3.0
BuildRequires:  python3dist(setuptools) <= 72.1.0
BuildRequires:  python3dist(setuptools) >= 61.2
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.4.3
Requires:       python3-kiwisolver = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-kiwisolver
Summary:        A fast implementation of the Cassowary constraint solver
%description -n python3-kiwisolver

%prep
%global oreon_srcdir kiwisolver-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-kiwisolver usr/lib/python3*/site-packages/kiwisolver* usr/lib64/python3*/site-packages/kiwisolver* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/kiwisolver* usr/lib64/python3*/site-packages/kiwisolver* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-kiwisolver -f %{oreon_filedir}/python3-kiwisolver.list

%changelog

%autochangelog
