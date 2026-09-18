%global source0_hash none

Name:           python-xxhash
Version:        4.0.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python binding for xxHash

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-2-Clause
URL:            https://github.com/ifduyue/python-xxhash
Source:         %{pypi_source xxhash}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'xxhash' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-xxhash
Summary:        %{summary}

%description -n python3-xxhash %_description


%prep
%autosetup -p1 -n xxhash-%{version}


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


%files -n python3-xxhash -f %{pyproject_files}

%changelog
%autochangelog
