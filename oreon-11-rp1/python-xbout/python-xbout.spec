%global source0_hash none

Name:           python-xbout
Version:        0.4.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Collect data from BOUT++ runs in python using xarray

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/boutproject/xBOUT
Source:         %{pypi_source xbout}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'xbout' generated automatically by pyp2spec.}

Patch:          sphinx-theme.patch
Patch:          engine-h5netcdf.patch

%description %_description

%package -n     python3-xbout
Summary:        %{summary}

%description -n python3-xbout %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-xbout 3d-plot,adios2,calc,cherab,docs,tests


%prep
%autosetup -p1 -n xbout-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x 3d-plot,adios2,calc,cherab,docs,tests


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-xbout -f %{pyproject_files}

%changelog
%autochangelog
