%global source0_hash none

Name:           python-orjson
Version:        3.12.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Fast, correct Python JSON library supporting dataclasses, datetimes, and numpy

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MPL-2.0 AND (Apache-2.0 OR MIT)
URL:            https://github.com/ijl/orjson
Source:         %{pypi_source orjson}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'orjson' generated automatically by pyp2spec.}

Patch:          orjson-3.11.7-pyo3-0.27.patch

%description %_description

%package -n     python3-orjson
Summary:        %{summary}

%description -n python3-orjson %_description


%prep
%autosetup -p1 -n orjson-%{version}


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


%files -n python3-orjson -f %{pyproject_files}

%changelog
%autochangelog
