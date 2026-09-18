%global source0_hash none

Name:           python-sqlparse
Version:        0.6.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A non-validating SQL parser.

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/andialbrecht/sqlparse
Source:         %{pypi_source sqlparse}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'sqlparse' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-sqlparse
Summary:        %{summary}

%description -n python3-sqlparse %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-sqlparse dev,doc


%prep
%autosetup -p1 -n sqlparse-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev,doc


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-sqlparse -f %{pyproject_files}
%{_bindir}/sqlformat

%changelog
%autochangelog
