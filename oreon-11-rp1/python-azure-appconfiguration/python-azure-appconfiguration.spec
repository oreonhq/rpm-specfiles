%global source0_hash none

Name:           python-azure-appconfiguration
Version:        1.9.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Microsoft Corporation Azure App Configuration Data Client Library for Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/Azure/azure-sdk-for-python
Source:         %{pypi_source azure_appconfiguration}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'azure-appconfiguration' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-azure-appconfiguration
Summary:        %{summary}

%description -n python3-azure-appconfiguration %_description


%prep
%autosetup -p1 -n azure_appconfiguration-%{version}


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


%files -n python3-azure-appconfiguration -f %{pyproject_files}

%changelog
%autochangelog
