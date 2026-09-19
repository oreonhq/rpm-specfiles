%global source0_hash 566d855953e949bb2b34cb43e1e73054aaa79281c74613b745ffddb82c802375

Name:           python-azure-mgmt-resource-deploymentscripts
Version:        1.0.0~b1
%global         pypi_version %(echo '%{version}' | tr -d '~')
Release:        %autorelease
Summary:        Microsoft Azure Resource Deploymentscripts Management Client Library
License:        MIT
URL:            https://pypi.org/project/azure-mgmt-resource-deploymentscripts/
Source0:        %{pypi_source azure_mgmt_resource_deploymentscripts %{pypi_version}}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Microsoft Azure Resource Deploymentscripts Management Client Library}

%description %{_description}

%package -n python3-azure-mgmt-resource-deploymentscripts
Summary:        %{summary}

%description -n python3-azure-mgmt-resource-deploymentscripts %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n azure_mgmt_resource_deploymentscripts-%{pypi_version}

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

%files -n python3-azure-mgmt-resource-deploymentscripts -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
