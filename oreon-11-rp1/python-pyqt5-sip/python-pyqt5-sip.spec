%global source0_hash none

Name:           python-pyqt5-sip
Version:        12.19.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        The sip module support for PyQt5

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-2-Clause
URL:            https://github.com/Python-SIP/sip
Source:         %{pypi_source pyqt5_sip}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyqt5-sip' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-pyqt5-sip
Summary:        %{summary}

%description -n python3-pyqt5-sip %_description


%prep
%autosetup -p1 -n pyqt5_sip-%{version}


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


%files -n python3-pyqt5-sip -f %{pyproject_files}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 12.17.1-2
- Prepare for Oreon 11 (RP1)
