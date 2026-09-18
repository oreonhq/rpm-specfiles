%global source0_hash none

Name:           python-bitarray
Version:        3.11.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        efficient arrays of booleans -- C extension

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        PSF-2.0
URL:            https://github.com/ilanschnell/bitarray
Source:         %{pypi_source bitarray}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'bitarray' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-bitarray
Summary:        %{summary}

%description -n python3-bitarray %_description


%prep
%autosetup -p1 -n bitarray-%{version}


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


%files -n python3-bitarray -f %{pyproject_files}

%changelog
%autochangelog
