%global source0_hash none

Name:           python-ephem
Version:        4.2.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Compute positions of the planets and stars

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/brandon-rhodes/pyephem
Source:         %{pypi_source ephem}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'ephem' generated automatically by pyp2spec.}

Patch0:         ephem_bsymbolic.patch

%description %_description

%package -n     python3-ephem
Summary:        %{summary}

%description -n python3-ephem %_description


%prep
%autosetup -p1 -n ephem-%{version}


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


%files -n python3-ephem -f %{pyproject_files}

%changelog
%autochangelog
