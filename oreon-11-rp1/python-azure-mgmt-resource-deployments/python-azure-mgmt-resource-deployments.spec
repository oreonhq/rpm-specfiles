%global source0_hash 7359b42658826e7e7ff13e6dbb0c490e95fcc95dbca224d2b85cf71ad7535f1d

Name:           python-azure-mgmt-resource-deployments
Version:        1.0.0~b1
%global         pypi_version %(echo '%{version}' | tr -d '~')
Release:        %autorelease
Summary:        Microsoft Azure Resource Deployments Management Client Library
License:        MIT
URL:            https://pypi.org/project/azure-mgmt-resource-deployments/
Source0:        %{pypi_source azure_mgmt_resource_deployments %{pypi_version}}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Microsoft Azure Resource Deployments Management Client Library}

%description %{_description}

%package -n python3-azure-mgmt-resource-deployments
Summary:        %{summary}

%description -n python3-azure-mgmt-resource-deployments %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n azure_mgmt_resource_deployments-%{pypi_version}

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

%files -n python3-azure-mgmt-resource-deployments -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
