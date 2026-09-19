%global source0_hash none

Name:           python-paramiko
Version:        5.0.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        SSH2 protocol library

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        LGPL-2.1
URL:            https://github.com/paramiko/paramiko
Source:         %{pypi_source paramiko}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'paramiko' generated automatically by pyp2spec.}

Patch3:        0003-remove-pytest-relaxed-dep.patch
Patch4:        0004-remove-icecream-dep.patch
Patch5:        0005-remove-invoke-dep.patch

%description %_description

%package -n     python3-paramiko
Summary:        %{summary}

%description -n python3-paramiko %_description


%prep
%autosetup -p1 -n paramiko-%{version}


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


%files -n python3-paramiko -f %{pyproject_files}

%changelog
%autochangelog
