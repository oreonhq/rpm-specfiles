%global source0_hash cda115a841142d4646e3f05818cbb08e2ca3daafc740646fa5888f9b8db08f97
Name:           python-eth-stdlib
Version:        0.2.8
Release:        1%{?dist}
Summary:        Ethereum Standard Library for Python
License:        LGPL-3.0-only
URL:            https://github.com/skellet0r/eth-stdlib
Source0:        https://files.pythonhosted.org/packages/source/e/eth_stdlib/eth_stdlib-%{version}.tar.gz
BuildArch:      noarch
Patch:         python-eth-stdlib-0001-Switch-to-cryptodomex.patch
Patch:         python-eth-stdlib-0002-Clarify-licensing-terms.patch
Patch:         python-eth-stdlib-0003-Disable-pytest-coverage.patch
Patch:         python-eth-stdlib-0004-Fix-for-modern-poetry.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-eth-stdlib = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-eth-stdlib
Summary:        Ethereum Standard Library for Python
%description -n python3-eth-stdlib

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir eth_stdlib-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-eth-stdlib usr/lib/python3*/site-packages/eth_stdlib* usr/lib64/python3*/site-packages/eth_stdlib* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/eth_stdlib* usr/lib64/python3*/site-packages/eth_stdlib* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-eth-stdlib -f %{oreon_filedir}/python3-eth-stdlib.list

%changelog

%autochangelog
