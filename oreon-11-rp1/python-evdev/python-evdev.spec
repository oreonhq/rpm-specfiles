%global source0_hash none

Name:           python-evdev
Version:        2.0.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Bindings to the Linux input handling subsystem

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/gvalkov/python-evdev
Source:         %{pypi_source evdev}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'evdev' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-evdev
Summary:        %{summary}

%description -n python3-evdev %_description


%prep
%autosetup -p1 -n evdev-%{version}


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


%files -n python3-evdev -f %{pyproject_files}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.9.3-1
- Prepare for Oreon 11 (RP1)
