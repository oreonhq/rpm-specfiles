%global source0_hash none

Name:           python-googleapis-common-protos
Version:        1.75.3
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Common protobufs used in Google APIs

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/googleapis/google-cloud-python/tree/main/packages/googleapis-common-protos
Source:         %{pypi_source googleapis_common_protos}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'googleapis-common-protos' generated automatically by pyp2spec.}

Patch:          %{url}/pull/212.patch

%description %_description

%package -n     python3-googleapis-common-protos
Summary:        %{summary}

%description -n python3-googleapis-common-protos %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-googleapis-common-protos grpc


%prep
%autosetup -p1 -n googleapis_common_protos-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x grpc


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-googleapis-common-protos -f %{pyproject_files}

%changelog
%autochangelog
