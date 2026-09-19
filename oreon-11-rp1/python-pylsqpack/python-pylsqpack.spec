%global source0_hash none

Name:           python-pylsqpack
Version:        0.3.24
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python wrapper for the ls-qpack QPACK library

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/aiortc/pylsqpack
Source:         %{pypi_source pylsqpack}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pylsqpack' generated automatically by pyp2spec.}

Patch0:         %{name}-unbundle_vendor_libs.patch

%description %_description

%package -n     python3-pylsqpack
Summary:        %{summary}

%description -n python3-pylsqpack %_description


%prep
%autosetup -p1 -n pylsqpack-%{version}


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


%files -n python3-pylsqpack -f %{pyproject_files}

%changelog
%autochangelog
