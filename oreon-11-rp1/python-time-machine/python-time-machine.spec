%global source0_hash none

Name:           python-time-machine
Version:        3.5.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Travel through time in your tests.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/adamchainz/time-machine
Source:         %{pypi_source time_machine}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'time-machine' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-time-machine
Summary:        %{summary}

%description -n python3-time-machine %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-time-machine cli,dateutil


%prep
%autosetup -p1 -n time_machine-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x cli,dateutil


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-time-machine -f %{pyproject_files}

%changelog
%autochangelog
