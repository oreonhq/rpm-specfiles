%global source0_hash none

Name:           python-puzpy
Version:        0.6.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        python crossword puzzle library

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/alexdej/puzpy.git
Source:         %{pypi_source puzpy}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'puzpy' generated automatically by pyp2spec.}

Patch:          puzpy-drop-unneeded-deps.diff

%description %_description

%package -n     python3-puzpy
Summary:        %{summary}

%description -n python3-puzpy %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-puzpy dev,publish


%prep
%autosetup -p1 -n puzpy-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev,publish


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-puzpy -f %{pyproject_files}

%changelog
%autochangelog
