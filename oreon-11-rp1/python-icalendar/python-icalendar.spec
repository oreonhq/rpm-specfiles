%global source0_hash none

Name:           python-icalendar
Version:        7.3.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        RFC 5545 compatible parser and generator of iCalendar files

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-2-Clause
URL:            https://icalendar.readthedocs.io/en/stable/
Source:         %{pypi_source icalendar}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'icalendar' generated automatically by pyp2spec.}

Patch0:         hatch.patch
Patch1:         tzdata.patch

%description %_description

%package -n     python3-icalendar
Summary:        %{summary}

%description -n python3-icalendar %_description


%prep
%autosetup -p1 -n icalendar-%{version}


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


%files -n python3-icalendar -f %{pyproject_files}
%{_bindir}/icalendar

%changelog
%autochangelog
