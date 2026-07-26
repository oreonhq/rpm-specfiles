%global source0_hash b1ae225ef87ada85f29c02e406140ab5895285ca64de2bcfe50b631c4818a337

# All tests are skipped by upstream. Skip installing test requirements.
%bcond_with     tests

%global         srcname     azure-mgmt-storage
%global         tarball_name     azure_mgmt_storage

Name:           python-azure-mgmt-storage
Version:        24.0.0
Release:        %autorelease
Summary:        Microsoft Azure Storage Management Client Library for Python
License:        MIT
URL:            https://pypi.org/project/azure-mgmt-storage/
Source:         %{pypi_source azure_mgmt_storage %{version}}

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3-azure-sdk-tools
BuildRequires:  python3dist(azure-devtools)
BuildRequires:  python3dist(azure-mgmt-keyvault)
BuildRequires:  python3dist(azure-mgmt-resource)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-aiohttp)
BuildRequires:  python3dist(python-dotenv)
%endif

%global _description %{expand:
Microsoft Azure Storage Management Client Library for Python}

%description %{_description}

%package -n python3-azure-mgmt-storage
Summary:        %{summary}

%description -n python3-azure-mgmt-storage %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n azure_mgmt_storage-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l azure

%check
%pyproject_check_import

%if %{with tests}
%pytest
%endif

%files -n python3-azure-mgmt-storage -f %{pyproject_files}
%doc README.md CHANGELOG.md

%changelog
%autochangelog
