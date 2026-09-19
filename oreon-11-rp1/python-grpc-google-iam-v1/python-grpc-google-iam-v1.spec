%global source0_hash none

Name:           python-grpc-google-iam-v1
Version:        0.14.5
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        IAM API client library

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/googleapis/google-cloud-python
Source:         %{pypi_source grpc_google_iam_v1}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'grpc-google-iam-v1' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-grpc-google-iam-v1
Summary:        %{summary}

%description -n python3-grpc-google-iam-v1 %_description


%prep
%autosetup -p1 -n grpc_google_iam_v1-%{version}


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


%files -n python3-grpc-google-iam-v1 -f %{pyproject_files}

%changelog
%autochangelog
