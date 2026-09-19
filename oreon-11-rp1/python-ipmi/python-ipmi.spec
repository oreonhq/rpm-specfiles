%global source0_hash none

Name:           python-ipmi
Version:        1.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A ipmi python client used in NetXMS migrated from perl

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/zhao-ji/check_ipmi_sensor_v3
Source:         %{pypi_source ipmi}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'ipmi' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-ipmi
Summary:        %{summary}

%description -n python3-ipmi %_description


%prep
%autosetup -p1 -n ipmi-%{version}


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


%files -n python3-ipmi -f %{pyproject_files}

%changelog
%autochangelog
