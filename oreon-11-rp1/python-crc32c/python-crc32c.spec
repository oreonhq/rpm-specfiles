%global source0_hash none

Name:           python-crc32c
Version:        2.9^post0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A python package implementing the crc32c algorithm in hardware and software

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        LGPL-2.1-or-later
URL:            https://github.com/ICRAR/crc32c
Source:         %{pypi_source crc32c 2.9.post0}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'crc32c' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-crc32c
Summary:        %{summary}

%description -n python3-crc32c %_description


%prep
%autosetup -p1 -n crc32c-2.9.post0


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


%files -n python3-crc32c -f %{pyproject_files}
%{_bindir}/crc32c

%changelog
%autochangelog
