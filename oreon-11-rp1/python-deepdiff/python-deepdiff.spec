%global source0_hash none

Name:           python-deepdiff
Version:        9.1.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Deep Difference and Search of any Python object/data. Recreate objects by adding adding deltas to each other.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://zepworks.com/deepdiff/
Source:         %{pypi_source deepdiff}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'deepdiff' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-deepdiff
Summary:        %{summary}

%description -n python3-deepdiff %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-deepdiff cli,coverage,dev,docs,optimize,static,test


%prep
%autosetup -p1 -n deepdiff-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x cli,coverage,dev,docs,optimize,static,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-deepdiff -f %{pyproject_files}
%{_bindir}/deep

%changelog
%autochangelog
