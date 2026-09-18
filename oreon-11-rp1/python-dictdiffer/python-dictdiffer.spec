%global source0_hash none

Name:           python-dictdiffer
Version:        0.10.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Dictdiffer is a library that helps you to diff and patch dictionaries.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/inveniosoftware/dictdiffer
Source:         %{pypi_source dictdiffer}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'dictdiffer' generated automatically by pyp2spec.}

Patch:          0001-tests-remove-pytest-runner-setup.py-test-support.patch
Patch:          0002-Downstream-only-remove-linting-coverage-options-for-.patch

%description %_description

%package -n     python3-dictdiffer
Summary:        %{summary}

%description -n python3-dictdiffer %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-dictdiffer docs,numpy,tests


%prep
%autosetup -p1 -n dictdiffer-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x docs,numpy,tests


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-dictdiffer -f %{pyproject_files}

%changelog
%autochangelog
