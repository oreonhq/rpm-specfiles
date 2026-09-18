%global source0_hash none

Name:           python-inquirer
Version:        3.4.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Collection of common interactive command line user interfaces, based on Inquirer.js

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/magmax/python-inquirer
Source:         %{pypi_source inquirer}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'inquirer' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-inquirer
Summary:        %{summary}

%description -n python3-inquirer %_description


%prep
%autosetup -p1 -n inquirer-%{version}


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


%files -n python3-inquirer -f %{pyproject_files}

%changelog
%autochangelog
