%global source0_hash none

Name:           python-libpysal
Version:        4.15.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Core components of PySAL - A library of spatial analysis functions

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/pysal/libpysal
Source:         %{pypi_source libpysal}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'libpysal' generated automatically by pyp2spec.}

Patch:          0001-Remove-unused-build-requirements.patch

%description %_description

%package -n     python3-libpysal
Summary:        %{summary}

%description -n python3-libpysal %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-libpysal dev,docs,plus,tests


%prep
%autosetup -p1 -n libpysal-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev,docs,plus,tests


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-libpysal -f %{pyproject_files}

%changelog
%autochangelog
