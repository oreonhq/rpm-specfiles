%global source0_hash none

Name:           python-sphinx-notfound-page
Version:        1.1.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Sphinx extension to build a 404 page with absolute URLs

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/readthedocs/sphinx-notfound-page
Source:         %{pypi_source sphinx_notfound_page}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'sphinx-notfound-page' generated automatically by pyp2spec.}

Patch:         tox-no-dot-no-pdbpp.patch
Patch:         https://patch-diff.githubusercontent.com/raw/readthedocs/sphinx-notfound-page/pull/245.patch
Patch:         https://patch-diff.githubusercontent.com/raw/readthedocs/sphinx-notfound-page/pull/250.patch

%description %_description

%package -n     python3-sphinx-notfound-page
Summary:        %{summary}

%description -n python3-sphinx-notfound-page %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-sphinx-notfound-page doc,test


%prep
%autosetup -p1 -n sphinx_notfound_page-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x doc,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-sphinx-notfound-page -f %{pyproject_files}

%changelog
%autochangelog
