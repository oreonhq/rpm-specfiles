%global source0_hash 900eaeaccffdcd01012b248a7d049008c92807b749edd1c9074ca9248554c17e

# No tests from upstream yet.
%bcond_with     tests

%global         srcname     azure-synapse-managedprivateendpoints

Name:           python-%{srcname}
Version:        0.4.0
Release:        %autorelease
Summary:        Microsoft Azure Synapse Managed Private Endpoints Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{srcname} %{version} zip}
# NOTE(mhayden): Still trying to get upstream to accept multiple PRs to add
# licenses to all PyPi packages, but they're moving slowly.
Source1:        https://github.com/Azure/azure-sdk-for-python/raw/%{srcname}_%{version}/LICENSE.txt

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(azure-devtools)
BuildRequires:  python3dist(azure-mgmt-keyvault)
BuildRequires:  python3dist(azure-mgmt-resource)
BuildRequires:  python3dist(azure-sdk-tools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-aiohttp)
BuildRequires:  python3dist(python-dotenv)
%endif

%global _description %{expand:
Microsoft Azure Synapse Managed Private Endpoints Client Library for Python}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
cp %SOURCE1 .

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
%license LICENSE.txt

%changelog
%autochangelog
