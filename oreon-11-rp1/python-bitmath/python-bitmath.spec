%global source0_hash 56f2cda86b1f0aa6470f4aaa90f82ef029f0e16c31b66f0fdd9d67613bc5e9f0
Name:           python-bitmath
Version:        2.1.1
Release:        1%{?dist}
Summary:        Pythonic module for representing and manipulating file sizes with different prefix notations _file size unit conversion_
License:        MIT
URL:            https://bitmath.readthedocs.io/en/latest/index.html
Source0:        https://files.pythonhosted.org/packages/source/b/bitmath/bitmath-%{version}.tar.gz
BuildArch:      noarch
Patch:  python-bitmath-rm-python-mock-usage.diff
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-bitmath = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-bitmath
Summary:        Pythonic module for representing and manipulating file sizes with different prefix notations _file size unit conversion_
%description -n python3-bitmath

%prep
%global oreon_srcdir bitmath-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-bitmath usr/lib/python3*/site-packages/bitmath* usr/lib64/python3*/site-packages/bitmath* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/bitmath* usr/lib64/python3*/site-packages/bitmath* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-bitmath -f %{oreon_filedir}/python3-bitmath.list

%changelog

%autochangelog
