%global source0_hash 814cf7872c816a7fb8abe96d98b243b815da9e898056dfdbbdb68063daee6496
Name:           python-myhdl
Version:        0.11.52
Release:        1%{?dist}
Summary:        Python as a Hardware Description Language
License:        ...
URL:            http://www.myhdl.org
Source0:        https://files.pythonhosted.org/packages/source/m/myhdl/myhdl-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-myhdl = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-myhdl
Summary:        Python as a Hardware Description Language
%description -n python3-myhdl

%prep
%global oreon_srcdir myhdl-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-myhdl usr/lib/python3*/site-packages/myhdl* usr/lib64/python3*/site-packages/myhdl* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/myhdl* usr/lib64/python3*/site-packages/myhdl* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-myhdl -f %{oreon_filedir}/python3-myhdl.list

%changelog

%autochangelog
