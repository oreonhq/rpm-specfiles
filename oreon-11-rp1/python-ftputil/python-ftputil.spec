%global source0_hash none

Name:           python-ftputil
Version:        5.2.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        High-level FTP client library _virtual file system and more_

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://ftputil.sschwarzer.net/
Source:         %{pypi_source ftputil}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'ftputil' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-ftputil
Summary:        %{summary}

%description -n python3-ftputil %_description


%prep
%autosetup -p1 -n ftputil-%{version}


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


%files -n python3-ftputil -f %{pyproject_files}

%changelog
%autochangelog
