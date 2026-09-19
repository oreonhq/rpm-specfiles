%global source0_hash none

Name:           python-gsw
Version:        3.6.23
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Gibbs Seawater Oceanographic Package of TEOS-10

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://www.teos-10.org/
Source:         %{pypi_source gsw}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'gsw' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-gsw
Summary:        %{summary}

%description -n python3-gsw %_description


%prep
%autosetup -p1 -n gsw-%{version}


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


%files -n python3-gsw -f %{pyproject_files}

%changelog
%autochangelog
