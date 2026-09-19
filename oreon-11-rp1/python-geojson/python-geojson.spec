%global source0_hash none

Name:           python-geojson
Version:        3.3.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python bindings and utilities for GeoJSON

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/jazzband/geojson
Source:         %{pypi_source geojson}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'geojson' generated automatically by pyp2spec.}

Patch0:     remove-check.patch

%description %_description

%package -n     python3-geojson
Summary:        %{summary}

%description -n python3-geojson %_description


%prep
%autosetup -p1 -n geojson-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-geojson -f %{pyproject_files}

%changelog
%autochangelog
