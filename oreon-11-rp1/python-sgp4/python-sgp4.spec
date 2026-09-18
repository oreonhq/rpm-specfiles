%global source0_hash none

Name:           python-sgp4
Version:        2.27
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        The C++ SGP4 routine that, given an Earth satellite TLE, computes its position.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/brandon-rhodes/python-sgp4
Source:         %{pypi_source sgp4}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'sgp4' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-sgp4
Summary:        %{summary}

%description -n python3-sgp4 %_description


%prep
%autosetup -p1 -n sgp4-%{version}


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


%files -n python3-sgp4 -f %{pyproject_files}

%changelog
%autochangelog
