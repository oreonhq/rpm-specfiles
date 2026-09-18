%global source0_hash none

Name:           python-llvmlite
Version:        0.49.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        lightweight wrapper around basic LLVM functionality

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-2-Clause AND Apache-2.0 WITH LLVM-exception
URL:            https://github.com/numba/llvmlite
Source:         %{pypi_source llvmlite}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'llvmlite' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-llvmlite
Summary:        %{summary}

%description -n python3-llvmlite %_description


%prep
%autosetup -p1 -n llvmlite-%{version}


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


%files -n python3-llvmlite -f %{pyproject_files}

%changelog
%autochangelog
