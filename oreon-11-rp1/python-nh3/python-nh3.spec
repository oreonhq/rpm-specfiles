%global source0_hash 71860d01c16f4d8c72e334e0674beb2b0899dbd0bf760de18932ef4390303848
Name:           python-nh3
Version:        0.3.7
Release:        1%{?dist}
Summary:        Python binding to Ammonia HTML sanitizer Rust crate
License:        MIT
URL:            https://github.com/messense/nh3
Source0:        https://files.pythonhosted.org/packages/source/n/nh3/nh3-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(maturin) < 2.0
BuildRequires:  python3dist(maturin) >= 1.0
Requires:       python3-nh3 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-nh3
Summary:        Python binding to Ammonia HTML sanitizer Rust crate
%description -n python3-nh3

%prep
%global oreon_srcdir nh3-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-nh3 usr/lib/python3*/site-packages/nh3* usr/lib64/python3*/site-packages/nh3* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/nh3* usr/lib64/python3*/site-packages/nh3* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-nh3 -f %{oreon_filedir}/python3-nh3.list

%changelog

%autochangelog
