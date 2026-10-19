%global source0_hash 2d8440d2be8a5577137fb2313ee211b5b35f36c4c922f274192d34f401616e83
%global pypi_name solcx
Name:          python-%{pypi_name}
Version:       2.0.5
Release:        1%{?dist}
BuildArch:     noarch
Summary:        Python wrapper and version management tool for the Solidity compiler
License:       MIT
URL:           https://github.com/ApeWorX/py-solc-x
VCS:           git:%{url}.git
Source0:        https://files.pythonhosted.org/packages/source/p/py_solc_x/py_solc_x-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 51.1.1
BuildRequires:  python3dist(setuptools-scm[toml]) >= 5.0
Requires:       python3-solcx = %{version}-%{release}
# /oreon:deps
%description
%{summary}.

%package -n python3-%{pypi_name}
Summary:        Python wrapper and version management tool for the Solidity compiler
%description -n python3-%{pypi_name}
%{summary}.

%prep
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/solcx* usr/lib64/python3*/site-packages/solcx* usr/bin/*

%check

%files
%files -n python3-solcx -f %{oreon_filedir}/python3-solcx.list

%changelog

%autochangelog
