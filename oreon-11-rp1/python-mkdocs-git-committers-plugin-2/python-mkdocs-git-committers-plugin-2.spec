%global source0_hash none

Name:           python-mkdocs-git-committers-plugin-2
Version:        2.5.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        An MkDocs plugin to create a list of contributors on the page. The git-committers plugin will seed the template context with a list of GitHub or GitLab committers and other useful GIT info such as last modified date

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/ojacques/mkdocs-git-committers-plugin-2/
Source:         %{pypi_source mkdocs_git_committers_plugin_2}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'mkdocs-git-committers-plugin-2' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-mkdocs-git-committers-plugin-2
Summary:        %{summary}

%description -n python3-mkdocs-git-committers-plugin-2 %_description


%prep
%autosetup -p1 -n mkdocs_git_committers_plugin_2-%{version}


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


%files -n python3-mkdocs-git-committers-plugin-2 -f %{pyproject_files}

%changelog
%autochangelog
