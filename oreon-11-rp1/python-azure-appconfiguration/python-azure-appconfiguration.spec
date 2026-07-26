%global source0_hash cefd75b298b898a8ed9f73048f3f39f4e81059a58cd832d0523787fc1d912a06

# Enable tests everywhere except EPEL 9, where python-httpretty is not backported.
%if 0%{?el9} || 0%{?centos} >= 9
%bcond_with    tests
%else
# change back to bcond_without when the azure-sdk-tools/azure-devtools mess gets sorted out.
# It seems azure-devtools now lives inside azure-sdk-tools, as a separate package, and renamed.
%bcond_with     tests
%endif

%global         srcname     azure-appconfiguration

Name:           python-%{srcname}
Version:        1.7.2
Release:        %autorelease
Summary:        Microsoft App Configuration Data Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source azure_appconfiguration %{version}}

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(azure-devtools)
BuildRequires:  python3dist(azure-identity)
BuildRequires:  python3dist(azure-mgmt-keyvault)
BuildRequires:  python3dist(azure-mgmt-resource)
BuildRequires:  python3dist(azure-sdk-tools)
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
Microsoft App Configuration Data Library for Python}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n azure_appconfiguration-%{version}

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
# All of the configuration client tests require network access.
%pytest --ignore-glob=tests/test_azure_configuration_client*.py
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGELOG.md

%changelog
%autochangelog
