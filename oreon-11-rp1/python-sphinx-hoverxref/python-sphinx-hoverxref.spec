%global source0_hash none

Name:           python-sphinx-hoverxref
Version:        1.4.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Sphinx extension to show tooltips with content embedded when hover a reference.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/readthedocs/sphinx-hoverxref
Source:         %{pypi_source sphinx_hoverxref}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'sphinx-hoverxref' generated automatically by pyp2spec.}

Patch:          sphinx-hoverxref-fix_tox_ini.diff

%description %_description

%package -n     python3-sphinx-hoverxref
Summary:        %{summary}

%description -n python3-sphinx-hoverxref %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-sphinx-hoverxref doc,test


%prep
%autosetup -p1 -n sphinx_hoverxref-%{version}


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


%files -n python3-sphinx-hoverxref -f %{pyproject_files}

%changelog
%autochangelog
