%global source0_hash none

Name:           python-sphinx-tabs
Version:        3.5.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Tabbed views for Sphinx

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/executablebooks/sphinx-tabs
Source:         %{pypi_source sphinx_tabs}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'sphinx-tabs' generated automatically by pyp2spec.}

Patch0:         https://patch-diff.githubusercontent.com/raw/executablebooks/sphinx-tabs/pull/200.patch
Patch1:         https://github.com/executablebooks/sphinx-tabs/pull/207.patch

%description %_description

%package -n     python3-sphinx-tabs
Summary:        %{summary}

%description -n python3-sphinx-tabs %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-sphinx-tabs code-style,testing


%prep
%autosetup -p1 -n sphinx_tabs-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x code-style,testing


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-sphinx-tabs -f %{pyproject_files}

%changelog
%autochangelog
