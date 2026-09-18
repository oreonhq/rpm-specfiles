%global source0_hash none

Name:           python-pyspike
Version:        0.9.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A Python library for the numerical analysis of spike train similarity

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-2-Clause
URL:            https://github.com/mariomulansky/PySpike
Source:         %{pypi_source pyspike}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pyspike' generated automatically by pyp2spec.}

Patch:          %{url}/pull/75.patch
Patch:          %{url}/pull/76.patch
Patch:          %{url}/pull/77.patch

%description %_description

%package -n     python3-pyspike
Summary:        %{summary}

%description -n python3-pyspike %_description


%prep
%autosetup -p1 -n pyspike-%{version}


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


%files -n python3-pyspike -f %{pyproject_files}

%changelog
%autochangelog
