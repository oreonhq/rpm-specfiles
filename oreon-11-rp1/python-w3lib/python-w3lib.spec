%global source0_hash 8dd69ee39ff6398d708c793abc779c334a69bac7cee1cdf71736c669ed6be864
Name:           python-w3lib
Version:        2.4.1
Release:        1%{?dist}
Summary:        Library of web-related functions
License:        BSD-3-Clause
URL:            https://github.com/scrapy/w3lib
Source0:        https://files.pythonhosted.org/packages/source/w/w3lib/w3lib-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.27.0
Requires:       python3-w3lib = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-w3lib
Summary:        Library of web-related functions
%description -n python3-w3lib

%prep
%global oreon_srcdir w3lib-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-w3lib usr/lib/python3*/site-packages/w3lib* usr/lib64/python3*/site-packages/w3lib* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/w3lib* usr/lib64/python3*/site-packages/w3lib* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-w3lib -f %{oreon_filedir}/python3-w3lib.list

%changelog

%autochangelog
