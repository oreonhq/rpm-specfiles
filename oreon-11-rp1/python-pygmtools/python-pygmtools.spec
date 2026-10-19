%global source0_hash eac05393b8cf0cd19b61b9fa0bb0c494f25d0add709f60f891d1ab01bdd3a382
Name:           python-pygmtools
Version:        0.6.0
Release:        1%{?dist}
Summary:        pygmtools provides graph matching solvers in Python API and supports numpy and pytorch backends. pygmtools also provides dataset API for standard graph matching benchmarks.
License:        MulanPSL-2.0
URL:            https://pygmtools.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/p/pygmtools/pygmtools-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pygmtools = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pygmtools
Summary:        pygmtools provides graph matching solvers in Python API and supports numpy and pytorch backends. pygmtools also provides dataset API for standard graph matching benchmarks.
%description -n python3-pygmtools

%prep
%global oreon_srcdir pygmtools-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pygmtools usr/lib/python3*/site-packages/pygmtools* usr/lib64/python3*/site-packages/pygmtools* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pygmtools* usr/lib64/python3*/site-packages/pygmtools* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pygmtools -f %{oreon_filedir}/python3-pygmtools.list

%changelog

%autochangelog
