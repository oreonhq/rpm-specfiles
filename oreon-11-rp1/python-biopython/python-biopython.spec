%global source0_hash none

Name:           python-biopython
Version:        1.88
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Freely available tools for computational molecular biology.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        LicenseRef-Biopython-License-Agreement
URL:            https://biopython.org/
Source:         %{pypi_source biopython}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'biopython' generated automatically by pyp2spec.}

Patch0:           %{pypi_name}-CVE_2025_68463_1.patch
Patch1:           %{pypi_name}-fix_numpy-2.4_compatibility.patch

%description %_description

%package -n     python3-biopython
Summary:        %{summary}

%description -n python3-biopython %_description


%prep
%autosetup -p1 -n biopython-%{version}


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


%files -n python3-biopython -f %{pyproject_files}

%changelog
%autochangelog
