%global source0_hash 435036128dd2715945c3c26f390439ecc3ae9d873ea2e69ac1f7982c88a02b87
Name:           python-mitogen
Version:        0.3.53
Release:        1%{?dist}
Summary:        Library for writing distributed self-replicating programs.
License:        BSD-3-Clause
URL:            https://github.com/mitogen-hq/mitogen/
Source0:        https://files.pythonhosted.org/packages/source/m/mitogen/mitogen-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mitogen = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-mitogen
Summary:        Library for writing distributed self-replicating programs.
%description -n python3-mitogen

%prep
%global oreon_srcdir mitogen-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mitogen usr/lib/python3*/site-packages/mitogen* usr/lib64/python3*/site-packages/mitogen* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mitogen* usr/lib64/python3*/site-packages/mitogen* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-mitogen -f %{oreon_filedir}/python3-mitogen.list

%changelog

%autochangelog
