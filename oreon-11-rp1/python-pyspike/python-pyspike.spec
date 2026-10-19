%global source0_hash b74008d88723a7781a6b7265621fe4555197d724156a6905ee5328c3e31e1fad
Name:           python-pyspike
Version:        0.9.0
Release:        1%{?dist}
Summary:        A Python library for the numerical analysis of spike train similarity
License:        BSD-2-Clause
URL:            https://github.com/mariomulansky/PySpike
Source0:        https://files.pythonhosted.org/packages/source/p/pyspike/pyspike-%{version}.tar.gz
Patch:          %{url}/pull/75.patch
Patch:          %{url}/pull/76.patch
Patch:          %{url}/pull/77.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 3.0
BuildRequires:  python3dist(numpy) >= 1.25
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-pyspike = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyspike
Summary:        A Python library for the numerical analysis of spike train similarity
%description -n python3-pyspike

%prep
%global oreon_srcdir pyspike-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyspike usr/lib/python3*/site-packages/pyspike* usr/lib64/python3*/site-packages/pyspike* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyspike* usr/lib64/python3*/site-packages/pyspike* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyspike -f %{oreon_filedir}/python3-pyspike.list

%changelog

%autochangelog
