%global source0_hash d55bf4ef10eb09b8b6866790e083d26d087d84caa3cc0946ba87c3ca7ecaf7b7
Name:           python-xxhash
Version:        4.0.1
Release:        1%{?dist}
Summary:        Python binding for xxHash
License:        BSD-2-Clause
URL:            https://github.com/ifduyue/python-xxhash
Source0:        https://files.pythonhosted.org/packages/source/x/xxhash/xxhash-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 45
Requires:       python3-xxhash = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-xxhash
Summary:        Python binding for xxHash
%description -n python3-xxhash

%prep
%global oreon_srcdir xxhash-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-xxhash usr/lib/python3*/site-packages/xxhash* usr/lib64/python3*/site-packages/xxhash* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/xxhash* usr/lib64/python3*/site-packages/xxhash* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-xxhash -f %{oreon_filedir}/python3-xxhash.list

%changelog

%autochangelog
