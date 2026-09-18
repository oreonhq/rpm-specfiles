%global source0_hash none

Name:           python-mkdocs-static-i18n
Version:        1.3.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        MkDocs i18n plugin using static translation markdown files

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/ultrabug/mkdocs-static-i18n
Source:         %{pypi_source mkdocs_static_i18n}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'mkdocs-static-i18n' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-mkdocs-static-i18n
Summary:        %{summary}

%description -n python3-mkdocs-static-i18n %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-mkdocs-static-i18n material


%prep
%autosetup -p1 -n mkdocs_static_i18n-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x material


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-mkdocs-static-i18n -f %{pyproject_files}

%changelog
%autochangelog
