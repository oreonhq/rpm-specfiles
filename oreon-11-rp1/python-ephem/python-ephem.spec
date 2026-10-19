%global source0_hash 920cb30369c79fde1088c2060d555ea5f8a50fdc80a9265832fd5bf195cf147f
Name:           python-ephem
Version:        4.2.1
Release:        1%{?dist}
Summary:        Compute positions of the planets and stars
License:        MIT
URL:            https://github.com/brandon-rhodes/pyephem
Source0:        https://files.pythonhosted.org/packages/source/e/ephem/ephem-%{version}.tar.gz
Patch0:         ephem_bsymbolic.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ephem = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-ephem
Summary:        Compute positions of the planets and stars
%description -n python3-ephem

%prep
%global oreon_srcdir ephem-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ephem usr/lib/python3*/site-packages/ephem* usr/lib64/python3*/site-packages/ephem* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ephem* usr/lib64/python3*/site-packages/ephem* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-ephem -f %{oreon_filedir}/python3-ephem.list

%changelog

%autochangelog
