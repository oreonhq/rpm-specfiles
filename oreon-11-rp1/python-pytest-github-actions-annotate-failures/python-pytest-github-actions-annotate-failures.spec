%global source0_hash none

Name:           python-pytest-github-actions-annotate-failures
Version:        0.4.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        pytest plugin to annotate failed tests with a workflow command for GitHub Actions

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/pytest-dev/pytest-github-actions-annotate-failures
Source:         %{pypi_source pytest_github_actions_annotate_failures}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pytest-github-actions-annotate-failures' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-pytest-github-actions-annotate-failures
Summary:        %{summary}

%description -n python3-pytest-github-actions-annotate-failures %_description


%prep
%autosetup -p1 -n pytest_github_actions_annotate_failures-%{version}


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


%files -n python3-pytest-github-actions-annotate-failures -f %{pyproject_files}

%changelog
%autochangelog
