%global source0_hash a250aef68509ed93419c9a1d90b0647cd5cbe26107ba94d3717ef5b6d595ffd9
Name:           python-sh
Version:        2.4.0
Release:        1%{?dist}
Summary:        Python subprocess replacement
License:        MIT
URL:            https://sh.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/s/sh/sh-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-sh = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-sh
Summary:        Python subprocess replacement
%description -n python3-sh

%prep
%global oreon_srcdir sh-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sh usr/lib/python3*/site-packages/sh* usr/lib64/python3*/site-packages/sh* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sh* usr/lib64/python3*/site-packages/sh* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sh -f %{oreon_filedir}/python3-sh.list

%changelog

%autochangelog
