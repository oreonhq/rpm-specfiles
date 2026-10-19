%global source0_hash ba0d2089de75ea0310e2dde03160e6ca10009947fb95a182f9b54021bb272e34
Name:           python-click
Version:        8.5.0
Release:        1%{?dist}
Summary:        Composable command line interface toolkit
License:        BSD-3-Clause
URL:            https://github.com/pallets/click/
Source0:        https://files.pythonhosted.org/packages/source/c/click/click-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.11
Requires:       python3-click = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-click
Summary:        Composable command line interface toolkit
%description -n python3-click

%prep
%global oreon_srcdir click-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-click usr/lib/python3*/site-packages/click* usr/lib64/python3*/site-packages/click* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/click* usr/lib64/python3*/site-packages/click* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-click -f %{oreon_filedir}/python3-click.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 8.3.1-1
- Prepare for Oreon 11 (RP1)
