%global source0_hash 49b876e45c0f5bab88ec47d7c56e8fb34fbdfcfe5b831a3a2a21e817f3d9732e

Name:           python-azure-mgmt-resource-deploymentstacks
Version:        1.0.0~b1
%global         pypi_version %(echo '%{version}' | tr -d '~')
Release:        %autorelease
Summary:        Microsoft Azure Resource Deploymentstacks Management Client Library
License:        MIT
URL:            https://pypi.org/project/azure-mgmt-resource-deploymentstacks/
Source:        %{pypi_source azure_mgmt_resource_deploymentstacks %{pypi_version}}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Microsoft Azure Resource Deploymentstacks Management Client Library}

%description %{_description}

%package -n python3-azure-mgmt-resource-deploymentstacks
Summary:        %{summary}

%description -n python3-azure-mgmt-resource-deploymentstacks %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n azure_mgmt_resource_deploymentstacks-%{pypi_version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l azure

# Like other Azure SDK packages, the tests expect Azure to be available
%check
%pyproject_check_import

%files -n python3-azure-mgmt-resource-deploymentstacks -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
