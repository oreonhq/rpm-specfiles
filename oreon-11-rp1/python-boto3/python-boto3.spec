%global source0_hash c11ad4c429a983493ba10014c7af9831a455c2c0eea91c1cefff74530e480277

Name:           python-boto3
Version:        1.43.106
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        The AWS SDK for Python _Boto3_

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/boto/boto3
Source:         %{pypi_source boto3}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'boto3' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-boto3
Summary:        %{summary}

%description -n python3-boto3 %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-boto3 crt


%prep
%autosetup -p1 -n boto3-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x crt


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-boto3 -f %{pyproject_files}

%changelog
%autochangelog
