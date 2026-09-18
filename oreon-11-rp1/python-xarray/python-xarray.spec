%global source0_hash none

Name:           python-xarray
Version:        2026.7.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        N-D labeled arrays and datasets in Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://xarray.dev/
Source:         %{pypi_source xarray}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'xarray' generated automatically by pyp2spec.}

Patch:          0001-Drop-pydap-from-dependencies.patch
Patch:          0002-Ensure-netcdf4-is-locked-while-closing.patch
Patch:          0003-numpy-2.4-curvefit-concat-periods.patch

%description %_description

%package -n     python3-xarray
Summary:        %{summary}

%description -n python3-xarray %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-xarray accel,complete,etc,io,parallel,types,viz


%prep
%autosetup -p1 -n xarray-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x accel,complete,etc,io,parallel,types,viz


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-xarray -f %{pyproject_files}

%changelog
%autochangelog
