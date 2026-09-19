%global source0_hash none

Name:           python-ibm-cloud-sdk-core
Version:        3.26.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Core library used by SDKs for IBM Cloud Services

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/IBM/python-sdk-core
Source:         %{pypi_source ibm_cloud_sdk_core}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'ibm-cloud-sdk-core' generated automatically by pyp2spec.}

Patch0:         fix-deps.patch

%description %_description

%package -n     python3-ibm-cloud-sdk-core
Summary:        %{summary}

%description -n python3-ibm-cloud-sdk-core %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-ibm-cloud-sdk-core dev,publish


%prep
%autosetup -p1 -n ibm_cloud_sdk_core-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev,publish


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-ibm-cloud-sdk-core -f %{pyproject_files}

%changelog
%autochangelog
