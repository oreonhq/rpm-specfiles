%global source0_hash none

Name:           python-sphinx-last-updated-by-git
Version:        0.3.8
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Get the _last updated_ time for each Sphinx page from Git

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-2-Clause
URL:            https://github.com/mgeier/sphinx-last-updated-by-git/
Source:         %{pypi_source sphinx_last_updated_by_git}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'sphinx-last-updated-by-git' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-sphinx-last-updated-by-git
Summary:        %{summary}

%description -n python3-sphinx-last-updated-by-git %_description


%prep
%autosetup -p1 -n sphinx_last_updated_by_git-%{version}


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


%files -n python3-sphinx-last-updated-by-git -f %{pyproject_files}

%changelog
%autochangelog
