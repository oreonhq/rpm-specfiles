%global source0_hash 0f9e739ab43db2ad870eae5df1b5c4bfa0500bbea1c6e58aa5e2e9c385facbc5

%global         srcname     azure-mgmt-resource-templatespecs
%global         tarball_name     azure_mgmt_resource_templatespecs

Name:           python-azure-mgmt-resource-templatespecs
Version:        1.0.0~b1
%global         pypi_version %(echo '%{version}' | tr -d '~')
Release:        %autorelease
Summary:        Microsoft Azure Resource Templatespecs Management Client Library
License:        MIT
URL:            https://pypi.org/project/azure-mgmt-resource-templatespecs/
Source:        %{pypi_source azure_mgmt_resource_templatespecs %{pypi_version}}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Microsoft Azure Resource Templatespecs Management Client Library}

%description %{_description}

%package -n python3-azure-mgmt-resource-templatespecs
Summary:        %{summary}

%description -n python3-azure-mgmt-resource-templatespecs %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n azure_mgmt_resource_templatespecs-%{pypi_version}

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

%files -n python3-azure-mgmt-resource-templatespecs -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
