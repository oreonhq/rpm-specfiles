%global source0_hash none

Name:           python-fastpurge
Version:        1.0.6
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A client for the Akamai Fast Purge API

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        GPL-3.0-or-later
URL:            https://release-engineering.github.io/python-fastpurge/
Source:         %{pypi_source fastpurge}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'fastpurge' generated automatically by pyp2spec.}

Patch: 0001-Use-unittest.mock-on-Python-3.3.patch

%description %_description

%package -n     python3-fastpurge
Summary:        %{summary}

%description -n python3-fastpurge %_description


%prep
%autosetup -p1 -n fastpurge-%{version}


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


%files -n python3-fastpurge -f %{pyproject_files}

%changelog
%autochangelog
