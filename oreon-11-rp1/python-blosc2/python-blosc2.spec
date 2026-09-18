%global source0_hash none

Name:           python-blosc2
Version:        4.13.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A fast _ compressed ndarray library with a flexible compute engine.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/Blosc/python-blosc2
Source:         %{pypi_source blosc2}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'blosc2' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-blosc2
Summary:        %{summary}

%description -n python3-blosc2 %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-blosc2 fsspec,hdf5,hires,parquet,tui,zarr


%prep
%autosetup -p1 -n blosc2-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x fsspec,hdf5,hires,parquet,tui,zarr


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-blosc2 -f %{pyproject_files}
%{_bindir}/b2nd-to-zarr
%{_bindir}/b2view
%{_bindir}/blosc2-to-zarr
%{_bindir}/parquet-to-blosc2

%changelog
%autochangelog
