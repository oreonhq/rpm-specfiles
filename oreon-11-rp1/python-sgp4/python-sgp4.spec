%global source0_hash 06d37247c6985739b707b8b39b6b83e06e8af783b2531e31965501ba983985f9
Name:           python-sgp4
Version:        2.27
Release:        1%{?dist}
Summary:        The C++ SGP4 routine that, given an Earth satellite TLE, computes its position.
License:        MIT
URL:            https://github.com/brandon-rhodes/python-sgp4
Source0:        https://files.pythonhosted.org/packages/source/s/sgp4/sgp4-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 38.6.0
BuildRequires:  python3dist(setuptools) >= 77.0.1
Requires:       python3-sgp4 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-sgp4
Summary:        The C++ SGP4 routine that, given an Earth satellite TLE, computes its position.
%description -n python3-sgp4

%prep
%global oreon_srcdir sgp4-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sgp4 usr/lib/python3*/site-packages/sgp4* usr/lib64/python3*/site-packages/sgp4* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sgp4* usr/lib64/python3*/site-packages/sgp4* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sgp4 -f %{oreon_filedir}/python3-sgp4.list

%changelog

%autochangelog
