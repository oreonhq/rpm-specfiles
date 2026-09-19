%global source0_hash none

Name:           python-mkdocs-git-revision-date-localized-plugin
Version:        1.6.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Mkdocs plugin that enables displaying the localized date of the last git modification of a markdown file.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/timvink/mkdocs-git-revision-date-localized-plugin
Source:         %{pypi_source mkdocs_git_revision_date_localized_plugin}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'mkdocs-git-revision-date-localized-plugin' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-mkdocs-git-revision-date-localized-plugin
Summary:        %{summary}

%description -n python3-mkdocs-git-revision-date-localized-plugin %_description


%prep
%autosetup -p1 -n mkdocs_git_revision_date_localized_plugin-%{version}


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


%files -n python3-mkdocs-git-revision-date-localized-plugin -f %{pyproject_files}

%changelog
%autochangelog
