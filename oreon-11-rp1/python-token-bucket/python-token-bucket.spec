%global source0_hash none

Name:           python-token-bucket
Version:        0.4.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Very fast implementation of the token bucket algorithm.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/falconry/token-bucket
Source:         %{pypi_source token_bucket}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'token-bucket' generated automatically by pyp2spec.}

Patch0:         0000-py312-imp.patch
Patch1:         0001-Drop-pytest-runner-and-setup.py-test-support.patch

%description %_description

%package -n     python3-token-bucket
Summary:        %{summary}

%description -n python3-token-bucket %_description


%prep
%autosetup -p1 -n token_bucket-%{version}


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


%files -n python3-token-bucket -f %{pyproject_files}

%changelog
%autochangelog
