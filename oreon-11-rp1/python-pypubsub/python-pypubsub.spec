%global source0_hash ec8b5cb147624958320e992602380cc5d0e4b36b1c59844d05e425a3003c09dc
Name:           python-pypubsub
Version:        4.0.7
Release:        1%{?dist}
Summary:        Python Publish-Subscribe Package
License:        BSD-2-Clause
URL:            https://github.com/schollii/pypubsub
Source0:        https://files.pythonhosted.org/packages/source/p/pypubsub/pypubsub-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) < 77
BuildRequires:  python3dist(setuptools) >= 68
BuildRequires:  python3dist(setuptools-scm) >= 7
Requires:       python3-pypubsub = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pypubsub
Summary:        Python Publish-Subscribe Package
%description -n python3-pypubsub

%prep
%global oreon_srcdir pypubsub-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pypubsub usr/lib/python3*/site-packages/pypubsub* usr/lib64/python3*/site-packages/pypubsub* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pypubsub* usr/lib64/python3*/site-packages/pypubsub* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pypubsub -f %{oreon_filedir}/python3-pypubsub.list

%changelog

%autochangelog
