%global source0_hash none

Name:           python-certifi
Version:        2026.7.22
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python package for providing Mozilla_s CA Bundle.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MPL-2.0
URL:            https://github.com/certifi/python-certifi
Source:         %{pypi_source certifi}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'certifi' generated automatically by pyp2spec.}

Patch:          certifi-2025.07.09-use-system-cert.patch

%description %_description

%package -n     python3-certifi
Summary:        %{summary}

%description -n python3-certifi %_description


%prep
%autosetup -p1 -n certifi-%{version}


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


%files -n python3-certifi -f %{pyproject_files}

%changelog
%autochangelog
