%global source0_hash none

Name:           python-w3lib
Version:        2.4.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Library of web-related functions

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/scrapy/w3lib
Source:         %{pypi_source w3lib}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'w3lib' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-w3lib
Summary:        %{summary}

%description -n python3-w3lib %_description


%prep
%autosetup -p1 -n w3lib-%{version}


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


%files -n python3-w3lib -f %{pyproject_files}

%changelog
%autochangelog
