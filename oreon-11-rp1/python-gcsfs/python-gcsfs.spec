%global source0_hash none

Name:           python-gcsfs
Version:        2026.8.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Convenient Filesystem interface over GCS

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/fsspec/gcsfs
Source:         %{pypi_source gcsfs}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'gcsfs' generated automatically by pyp2spec.}

Patch0:         gcsfs-fsspec-pin.patch

%description %_description

%package -n     python3-gcsfs
Summary:        %{summary}

%description -n python3-gcsfs %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-gcsfs crc,dev,gcsfuse


%prep
%autosetup -p1 -n gcsfs-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x crc,dev,gcsfuse


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-gcsfs -f %{pyproject_files}

%changelog
%autochangelog
