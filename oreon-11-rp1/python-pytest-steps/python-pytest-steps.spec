%global source0_hash none

Name:           python-pytest-steps
Version:        1.8.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Create step-wise / incremental tests in pytest.

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/smarie/python-pytest-steps
Source:         %{pypi_source pytest-steps}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pytest-steps' generated automatically by pyp2spec.}

Patch:          pytest-steps-1.7.2-no-pytest-runner.patch

%description %_description

%package -n     python3-pytest-steps
Summary:        %{summary}

%description -n python3-pytest-steps %_description


%prep
%autosetup -p1 -n pytest-steps-%{version}


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


%files -n python3-pytest-steps -f %{pyproject_files}

%changelog
%autochangelog
