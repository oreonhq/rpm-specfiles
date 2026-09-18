%global source0_hash none

Name:           python-hid-parser
Version:        0.1.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Typed pure Python library to parse HID report descriptors

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/usb-tools/python-hid-parser
Source:         %{pypi_source hid_parser}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'hid-parser' generated automatically by pyp2spec.}

Patch:          https://github.com/usb-tools/python-hid-parser/pull/23.patch#/%{name}-pytest-8.patch
Patch:          https://github.com/usb-tools/python-hid-parser/pull/18.patch#/%{name}-fix-GenericDesktopControls-Rz.patch
Patch:          %{name}-solaar.patch

%description %_description

%package -n     python3-hid-parser
Summary:        %{summary}

%description -n python3-hid-parser %_description


%prep
%autosetup -p1 -n hid_parser-%{version}


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


%files -n python3-hid-parser -f %{pyproject_files}

%changelog
%autochangelog
