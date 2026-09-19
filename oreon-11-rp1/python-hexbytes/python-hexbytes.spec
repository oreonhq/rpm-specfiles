%global source0_hash a657eebebdfe27254336f98d8af6e2236f3f83aed164b87466b6cf6c5f5a4765

%global pypi_name hexbytes

Name:          python-%{pypi_name}
Version:       1.3.1
Release:       %autorelease
BuildArch:     noarch
Summary:       Python `bytes` subclass that decodes hex, with a readable console output
License:       MIT
URL:           https://github.com/ethereum/hexbytes
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
BuildRequires: python3-eth-utils
BuildRequires: python3-hypothesis
BuildRequires: python3-pytest
BuildSystem:   pyproject
BuildOption(install): -l %{pypi_name}

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%{summary}.

%check -a
%pytest -k 'not test_install_local_wheel'

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
