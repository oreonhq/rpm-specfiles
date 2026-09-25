%global source0_hash 9e2ddadc609084b5f60affb8b87e77304fed64e271e2b2b7558186cf65d81e5a

Name:           python-awscrt
Version:        0.37.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A common runtime for AWS Python projects

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/awslabs/aws-crt-python
Source:         %{pypi_source awscrt}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'awscrt' generated automatically by pyp2spec.}

Patch0:         skip-tests-requiring-network.patch
Patch1:         skip-SHA1-in-test_crypto.patch
Patch2:         websockets.patch

%description %_description

%package -n     python3-awscrt
Summary:        %{summary}

%description -n python3-awscrt %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-awscrt dev


%prep
%autosetup -p1 -n awscrt-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-awscrt -f %{pyproject_files}

%changelog
%autochangelog
