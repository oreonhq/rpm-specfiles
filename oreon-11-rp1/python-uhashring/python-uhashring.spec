%global source0_hash 4855ede3ea66e645eaee016bbeb004e20570ada7714ecb1947cd45ce85d0c08e
Name:           python-uhashring
Version:        2.5
Release:        1%{?dist}
Summary:        Full featured consistent hashing python library compatible with ketama.
License:        BSD-3-Clause
URL:            https://github.com/ultrabug/uhashring
Source0:        https://files.pythonhosted.org/packages/source/u/uhashring/uhashring-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.26.1
Requires:       python3-uhashring = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-uhashring
Summary:        Full featured consistent hashing python library compatible with ketama.
%description -n python3-uhashring

%prep
%global oreon_srcdir uhashring-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-uhashring usr/lib/python3*/site-packages/uhashring* usr/lib64/python3*/site-packages/uhashring* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/uhashring* usr/lib64/python3*/site-packages/uhashring* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-uhashring -f %{oreon_filedir}/python3-uhashring.list

%changelog

%autochangelog
