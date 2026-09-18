%global source0_hash none

Name:           python-portalocker
Version:        4.3.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Cross-platform file locking, with Redis, PID-file and bounded-semaphore locks

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/wolph/portalocker/
Source:         %{pypi_source portalocker}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'portalocker' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-portalocker
Summary:        %{summary}

%description -n python3-portalocker %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-portalocker docs,redis,tests,win32


%prep
%autosetup -p1 -n portalocker-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x docs,redis,tests,win32


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-portalocker -f %{pyproject_files}

%changelog
%autochangelog
