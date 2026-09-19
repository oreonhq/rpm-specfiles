%global source0_hash c5d0cb3f5b6e81e8e35da5754388ddcc6d0d14b6c6a132cb93d69ed580a7278c

%global pypi_name base58
%global common_description %{expand:
Base58 and Base58Check implementation compatible with what is used by the
bitcoin network.}

Name:          python-%{pypi_name}
Version:       2.1.1
Release:       %autorelease
BuildArch:     noarch
Summary:       Base58 and Base58Check implementation
License:       MIT
URL:           https://github.com/keis/%{pypi_name}
VCS:           git:%{url}.git
Source0:       %{pypi_source %{pypi_name}}
BuildRequires: python3-hamcrest
BuildRequires: python3-pytest
BuildRequires: python3-pytest-benchmark
BuildSystem:   pyproject
BuildOption(install): -l %{pypi_name}

%description  %{common_description}

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name} %{common_description}

%check -a
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%{_bindir}/base58

%changelog
%autochangelog
