%global source0_hash 7557300dbf02a93c70fa44af352b5c4a58f94e997a0fd6797fb7d1c29d9538ee

%global pypi_name eth_typing

Name:          python-eth-typing
Version:       5.2.1
Release:       %autorelease
BuildArch:     noarch
Summary:       Python types for type hinting commonly used Ethereum types
License:       MIT
URL:           https://github.com/ethereum/eth-typing
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
BuildRequires: python3-pytest

%description
%{summary}.

%package -n python3-eth-typing
Summary: %{summary}

%description -n python3-eth-typing
%{summary}.

%prep
%autosetup -p1

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest -k 'not test_install_local_wheel'

%files -n python3-eth-typing -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
