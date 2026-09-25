%global source0_hash none

Name:           python-platformdirs
Version:        4.11.13
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A small Python package for determining appropriate platform-specific dirs, e.g. a _user data dir_.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/tox-dev/platformdirs
Source:         %{pypi_source platformdirs}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'platformdirs' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-platformdirs
Summary:        %{summary}

%description -n python3-platformdirs %_description


%prep
%autosetup -p1 -n platformdirs-%{version}


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


%files -n python3-platformdirs -f %{pyproject_files}

%changelog
%autochangelog
