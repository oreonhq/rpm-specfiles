%global source0_hash none

Name:           python-pytest-lazy-fixtures
Version:        1.4.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Allows you to use fixtures in @pytest.mark.parametrize.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/dev-petrov/pytest-lazy-fixtures
Source:         %{pypi_source pytest_lazy_fixtures}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pytest-lazy-fixtures' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-pytest-lazy-fixtures
Summary:        %{summary}

%description -n python3-pytest-lazy-fixtures %_description


%prep
%autosetup -p1 -n pytest_lazy_fixtures-%{version}


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


%files -n python3-pytest-lazy-fixtures -f %{pyproject_files}

%changelog
%autochangelog
