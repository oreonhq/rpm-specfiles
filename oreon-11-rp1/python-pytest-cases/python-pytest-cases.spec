%global source0_hash none

Name:           python-pytest-cases
Version:        3.10.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Separate test code from test cases in pytest.

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/smarie/python-pytest-cases
Source:         %{pypi_source pytest_cases}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pytest-cases' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-pytest-cases
Summary:        %{summary}

%description -n python3-pytest-cases %_description


%prep
%autosetup -p1 -n pytest_cases-%{version}


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


%files -n python3-pytest-cases -f %{pyproject_files}

%changelog
%autochangelog
