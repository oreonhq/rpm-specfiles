%global source0_hash none

Name:           python-unicodedata2
Version:        17.0.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Unicodedata backport updated to the latest Unicode version.

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            http://github.com/fonttools/unicodedata2
Source:         %{pypi_source unicodedata2}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'unicodedata2' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-unicodedata2
Summary:        %{summary}

%description -n python3-unicodedata2 %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-unicodedata2 testing


%prep
%autosetup -p1 -n unicodedata2-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x testing


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-unicodedata2 -f %{pyproject_files}

%changelog
%autochangelog
