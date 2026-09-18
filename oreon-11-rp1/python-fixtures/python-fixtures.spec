%global source0_hash none

Name:           python-fixtures
Version:        4.3.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Fixtures, reusable state for writing clean tests and more.

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/testing-cabal/fixtures
Source:         %{pypi_source fixtures}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'fixtures' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-fixtures
Summary:        %{summary}

%description -n python3-fixtures %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-fixtures docs,streams,test


%prep
%autosetup -p1 -n fixtures-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x docs,streams,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-fixtures -f %{pyproject_files}

%changelog
%autochangelog
