%global source0_hash a5758ad00f0e1bbd60dc5a579a50259bff2e267e8e925d485351bf2bc683a329
Name:           python-pycdlib
Version:        1.21.0
Release:        1%{?dist}
Summary:        Pure python ISO manipulation library
License:        LGPL-2.1-only
URL:            http://github.com/clalancette/pycdlib
Source0:        https://files.pythonhosted.org/packages/source/p/pycdlib/pycdlib-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pycdlib = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pycdlib
Summary:        Pure python ISO manipulation library
%description -n python3-pycdlib

%prep
%global oreon_srcdir pycdlib-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pycdlib usr/lib/python3*/site-packages/pycdlib* usr/lib64/python3*/site-packages/pycdlib* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pycdlib* usr/lib64/python3*/site-packages/pycdlib* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pycdlib -f %{oreon_filedir}/python3-pycdlib.list

%changelog

%autochangelog
