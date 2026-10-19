%global source0_hash 6404b8b82aef5ff0fd478934137128b99b12212ba35afdde5525ca4f8388ea58
Name:           python-pathable
Version:        0.6.0
Release:        1%{?dist}
Summary:        Object-oriented paths
License:        Apache-2.0
URL:            https://github.com/p1c2u/pathable
Source0:        https://files.pythonhosted.org/packages/source/p/pathable/pathable-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-pathable = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pathable
Summary:        Object-oriented paths
%description -n python3-pathable

%prep
%global oreon_srcdir pathable-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pathable usr/lib/python3*/site-packages/pathable* usr/lib64/python3*/site-packages/pathable* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pathable* usr/lib64/python3*/site-packages/pathable* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pathable -f %{oreon_filedir}/python3-pathable.list

%changelog

%autochangelog
