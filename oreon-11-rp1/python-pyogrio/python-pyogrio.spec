%global source0_hash none

Name:           python-pyogrio
Version:        0.13.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Vectorized spatial vector file format I/O using GDAL/OGR

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/geopandas/pyogrio
Source:         %{pypi_source pyogrio}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyogrio' generated automatically by pyp2spec.}

Patch:          0001-Drop-extra-dependencies.patch

%description %_description

%package -n     python3-pyogrio
Summary:        %{summary}

%description -n python3-pyogrio %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-pyogrio benchmark,dev,geopandas,test


%prep
%autosetup -p1 -n pyogrio-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x benchmark,dev,geopandas,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-pyogrio -f %{pyproject_files}

%changelog
%autochangelog
