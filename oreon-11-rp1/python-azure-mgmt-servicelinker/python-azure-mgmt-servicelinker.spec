%global source0_hash c51c111fb76c59e58fceccfecfd119f8c83e4d64fdca77a46b62d81ec6a3ea29

# This SDK component has no tests upstream yet. 😭
%bcond_with     tests

%global         srcname      azure-mgmt-servicelinker
%global         tarball_name azure_mgmt_servicelinker

Name:           python-%{srcname}
Version:        1.2.0~b3
%global         pypi_version 1.2.0b3
Release:        %autorelease
Summary:        Microsoft Azure Servicelinker Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{tarball_name} %{pypi_version}}

# NOTE(mhayden): Set an epoch number because I used 1.0.0b1 as a version as a mistake
# and 1.0.0~b2 sorts poorly with it. 🤦🏻‍♂️
Epoch:          1

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(azure-devtools)
BuildRequires:  python3dist(azure-mgmt-keyvault)
BuildRequires:  python3dist(azure-mgmt-resource)
BuildRequires:  python3dist(azure-sdk-tools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-aiohttp)
%endif

%global _description %{expand:
Microsoft Azure Servicelinker Management Client Library for Python}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{tarball_name}-%{pypi_version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files azure

%check
%pyproject_check_import

%if %{with tests}
%pytest
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGELOG.md

%changelog
%autochangelog
