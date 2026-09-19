%global source0_hash none

Name:           python-google-api-core
Version:        2.38.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Google API client core library

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/googleapis/google-cloud-python/tree/main/packages/google-api-core
Source:         %{pypi_source google_api_core}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'google-api-core' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-google-api-core
Summary:        %{summary}

%description -n python3-google-api-core %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-google-api-core async-rest,grpc,testing,tracing


%prep
%autosetup -p1 -n google_api_core-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x async-rest,grpc,testing,tracing


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-google-api-core -f %{pyproject_files}

%changelog
%autochangelog
