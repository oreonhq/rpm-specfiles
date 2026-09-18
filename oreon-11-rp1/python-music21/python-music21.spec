%global source0_hash none

Name:           python-music21
Version:        10.5.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A Toolkit for Computer-Aided Musical Analysis and Computational Musicology.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/cuthbertLab/music21
Source:         %{pypi_source music21}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'music21' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-music21
Summary:        %{summary}

%description -n python3-music21 %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-music21 extras


%prep
%autosetup -p1 -n music21-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x extras


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-music21 -f %{pyproject_files}

%changelog
%autochangelog
