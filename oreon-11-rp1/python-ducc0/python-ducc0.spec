%global source0_hash bac084745bbdb243482a4aec3ecc857bdd46faec298c67e48bc0bb90350dbabd
Name:           python-ducc0
Version:        0.41.0
Release:        1%{?dist}
Summary:        Distinctly useful code collection: contains efficient algorithms for Fast Fourier _and related_ transforms, spherical harmonic transforms involving very general spherical grids, gridding/degridding tools for radio interferometry, 4pi spherical convolution operators and much more.
License:        GPL-2.0-or-later
URL:            ...
Source0:        https://files.pythonhosted.org/packages/source/d/ducc0/ducc0-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(nanobind) >= 2.5.0
BuildRequires:  python3dist(numpy) >= 1.17.0
BuildRequires:  python3dist(pybind11) >= 2.13.6
BuildRequires:  python3dist(scikit-build-core) > 0.5
Requires:       python3-ducc0 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-ducc0
Summary:        Distinctly useful code collection: contains efficient algorithms for Fast Fourier _and related_ transforms, spherical harmonic transforms involving very general spherical grids, gridding/degridding tools for radio interferometry, 4pi spherical convolution operators and much more.
# oreon:reqs
Requires:       python3dist(numpy) >= 1.17.0
# /oreon:reqs
%description -n python3-ducc0

%prep
%global oreon_srcdir ducc0-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ducc0 usr/lib/python3*/site-packages/ducc0* usr/lib64/python3*/site-packages/ducc0* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ducc0* usr/lib64/python3*/site-packages/ducc0* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-ducc0 -f %{oreon_filedir}/python3-ducc0.list

%changelog

%autochangelog
