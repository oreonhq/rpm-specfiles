%global source0_hash none

Name:           python-adafruit-platformdetect
Version:        3.89.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Platform detection for use by libraries like Adafruit-Blinka.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/adafruit/Adafruit_Python_PlatformDetect
Source:         %{pypi_source adafruit_platformdetect}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'adafruit-platformdetect' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-adafruit-platformdetect
Summary:        %{summary}

%description -n python3-adafruit-platformdetect %_description


%prep
%autosetup -p1 -n adafruit_platformdetect-%{version}


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


%files -n python3-adafruit-platformdetect -f %{pyproject_files}

%changelog
%autochangelog
