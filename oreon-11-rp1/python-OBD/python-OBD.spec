%global source0_hash none

Name:           python-obd
Version:        0.7.3
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Serial module for handling live sensor data from a vehicle_s OBD-II port

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        GPL-2.0-only
URL:            https://github.com/brendan-w/python-OBD
Source:         %{pypi_source obd}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'obd' generated automatically by pyp2spec.}

Patch0:        %{name}-dep-ver.patch

%description %_description

%package -n     python3-obd
Summary:        %{summary}

%description -n python3-obd %_description


%prep
%autosetup -p1 -n obd-%{version}


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


%files -n python3-obd -f %{pyproject_files}

%changelog
%autochangelog
