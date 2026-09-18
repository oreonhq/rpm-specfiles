%global source0_hash none

Name:           python-numpy-stl
Version:        4.0.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Library to make reading, writing and modifying both binary and ascii STL files easy.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/WoLpH/numpy-stl/
Source:         %{pypi_source numpy_stl}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'numpy-stl' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-numpy-stl
Summary:        %{summary}

%description -n python3-numpy-stl %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-numpy-stl dev,docs,fast,tests,tox


%prep
%autosetup -p1 -n numpy_stl-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev,docs,fast,tests,tox


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-numpy-stl -f %{pyproject_files}
%{_bindir}/stl
%{_bindir}/stl2ascii
%{_bindir}/stl2bin

%changelog
%autochangelog
