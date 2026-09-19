%global source0_hash bbbc6db9c4bc067fb08271f8eda356129d6051c4538977a8f375120f4e63f79c

# Upstream has no tests.
%bcond_with     tests

%global         srcname     azure-mgmt-servicebus
%global         tarball_name     azure_mgmt_servicebus

Name:           python-%{srcname}
Version:        10.0.0~b1
%global         pypi_version 10.0.0b1
Release:        %autorelease
Summary:        Microsoft Azure Service Bus Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{tarball_name} %{pypi_version}}

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
Microsoft Azure Service Bus Management Client Library for Python}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{tarball_name}-%{pypi_version}

%generate_buildrequires
%pyproject_buildrequires -r

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
%doc README.md

%changelog
%autochangelog
