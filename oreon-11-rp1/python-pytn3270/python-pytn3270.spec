%global source0_hash none

Name:           python-pytn3270
Version:        0.16.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        TN3270 library

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        ISC
URL:            https://github.com/lowobservable/pytn3270
Source:         %{pypi_source pytn3270}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pytn3270' generated automatically by pyp2spec.}

Patch:          %{url}/pull/3.patch

%description %_description

%package -n     python3-pytn3270
Summary:        %{summary}

%description -n python3-pytn3270 %_description


%prep
%autosetup -p1 -n pytn3270-%{version}


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


%files -n python3-pytn3270 -f %{pyproject_files}

%changelog
%autochangelog
