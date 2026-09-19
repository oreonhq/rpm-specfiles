%global source0_hash e7bdf166c32de7aef5a626953f536ca4f1c6115f16795354c8c3f38f1da1fe10

# Upstream removed tests.
%bcond_with     tests

%global         srcname          azure-mgmt-eventhub
%global         tarball_name     azure_mgmt_eventhub

Name:           python-%{srcname}
Version:        12.0.0~b1
%global         pypi_version 12.0.0b1
Release:        %autorelease
Summary:        Microsoft Azure EventHub Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source %{tarball_name} %{pypi_version}}

BuildArch:      noarch

Epoch:          1

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(azure-devtools)
BuildRequires:  python3dist(azure-mgmt-authorization)
BuildRequires:  python3dist(azure-mgmt-keyvault)
BuildRequires:  python3dist(azure-mgmt-resource)
BuildRequires:  python3dist(azure-mgmt-storage)
BuildRequires:  python3dist(azure-mgmt-network)
BuildRequires:  python3dist(azure-sdk-tools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-aiohttp)
BuildRequires:  python3dist(python-dotenv)
%endif

%global _description %{expand:
Microsoft Azure EventHub Management Client Library for Python}

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
%pytest --disable-warnings
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
