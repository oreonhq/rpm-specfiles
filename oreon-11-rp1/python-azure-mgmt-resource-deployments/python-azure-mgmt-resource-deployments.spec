%global source0_hash none

Name:           python-azure-mgmt-resource-deployments
Version:        2.0.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Microsoft Azure Deployments Management Client Library for Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         %{pypi_source azure_mgmt_resource_deployments}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'azure-mgmt-resource-deployments' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-azure-mgmt-resource-deployments
Summary:        %{summary}

%description -n python3-azure-mgmt-resource-deployments %_description


%prep
%autosetup -p1 -n azure_mgmt_resource_deployments-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-azure-mgmt-resource-deployments -f %{pyproject_files}

%changelog
%autochangelog
