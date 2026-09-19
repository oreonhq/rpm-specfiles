%global source0_hash none

Name:           python-pykcs11
Version:        1.5.20
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A Full PKCS#11 wrapper for Python

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        GPL-2.0-or-later
URL:            https://github.com/LudovicRousseau/PyKCS11
Source:         %{pypi_source pykcs11}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pykcs11' generated automatically by pyp2spec.}

Patch:          %{url}/pull/113.patch#/Add-Fedora-PyKCS11-library-location-search-path.patch

%description %_description

%package -n     python3-pykcs11
Summary:        %{summary}

%description -n python3-pykcs11 %_description


%prep
%autosetup -p1 -n pykcs11-%{version}


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


%files -n python3-pykcs11 -f %{pyproject_files}

%changelog
%autochangelog
