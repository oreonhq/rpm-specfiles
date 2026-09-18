%global source0_hash none

Name:           python-scp
Version:        0.16.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        scp module for paramiko

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        LGPL-2.1-or-later
URL:            https://github.com/jbardin/scp.py
Source:         %{pypi_source scp}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'scp' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-scp
Summary:        %{summary}

%description -n python3-scp %_description


%prep
%autosetup -p1 -n scp-%{version}


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


%files -n python3-scp -f %{pyproject_files}

%changelog
%autochangelog
