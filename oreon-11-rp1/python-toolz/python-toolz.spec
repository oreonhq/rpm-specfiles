%global source0_hash 27a5c770d068c110d9ed9323f24f1543e83b2f300a687b7891c1a6d56b697b5b
Name:           python-toolz
Version:        1.1.0
Release:        1%{?dist}
Summary:        List processing tools and functional utilities
License:        BSD-3-Clause
URL:            https://github.com/pytoolz/toolz
Source0:        https://files.pythonhosted.org/packages/source/t/toolz/toolz-%{version}.tar.gz
BuildArch:      noarch
Patch:          %{url}/pull/592.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
BuildRequires:  python3dist(setuptools-git-versioning) >= 2.0
Requires:       python3-toolz = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-toolz
Summary:        List processing tools and functional utilities
%description -n python3-toolz

%prep
%global oreon_srcdir toolz-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-toolz usr/lib/python3*/site-packages/toolz* usr/lib64/python3*/site-packages/toolz* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/toolz* usr/lib64/python3*/site-packages/toolz* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-toolz -f %{oreon_filedir}/python3-toolz.list

%changelog

%autochangelog
