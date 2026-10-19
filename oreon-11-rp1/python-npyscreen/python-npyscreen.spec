%global source0_hash 3d6c7207cccd08d9269804eeed960b40678e99e891880a2fd936f23c66d5c156
Name:           python-npyscreen
Version:        5.0.4
Release:        1%{?dist}
Summary:        Writing user interfaces without all that ugly mucking about in hyperspace
License:        BSD-3-Clause
URL:            https://github.com/npcole/npyscreen
Source0:        https://files.pythonhosted.org/packages/source/n/npyscreen/npyscreen-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
Requires:       python3-npyscreen = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-npyscreen
Summary:        Writing user interfaces without all that ugly mucking about in hyperspace
%description -n python3-npyscreen

%prep
%global oreon_srcdir npyscreen-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-npyscreen usr/lib/python3*/site-packages/npyscreen* usr/lib64/python3*/site-packages/npyscreen* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/npyscreen* usr/lib64/python3*/site-packages/npyscreen* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-npyscreen -f %{oreon_filedir}/python3-npyscreen.list

%changelog

%autochangelog
