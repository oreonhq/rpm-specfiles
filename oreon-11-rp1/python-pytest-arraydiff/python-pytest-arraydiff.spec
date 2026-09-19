%global source0_hash none

Name:           python-pytest-arraydiff
Version:        0.7.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        pytest plugin to help with comparing array output from tests

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/astropy/pytest-arraydiff
Source:         %{pypi_source pytest_arraydiff}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pytest-arraydiff' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-pytest-arraydiff
Summary:        %{summary}

%description -n python3-pytest-arraydiff %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-pytest-arraydiff test,test-hdf5


%prep
%autosetup -p1 -n pytest_arraydiff-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x test,test-hdf5


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-pytest-arraydiff -f %{pyproject_files}

%changelog
%autochangelog
