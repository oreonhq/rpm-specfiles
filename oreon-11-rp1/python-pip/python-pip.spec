%global source0_hash none

Name:           python-pip
Version:        26.2.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        The PyPA recommended tool for installing Python packages.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://pip.pypa.io/
Source:         %{pypi_source pip}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pip' generated automatically by pyp2spec.}

Patch:        remove-existing-dist-only-if-path-conflicts.patch
Patch:        dummy-certifi.patch
Patch:        downstream-remove-pytest-subket.patch
Patch:          urllib3-CVE-2025-50181.patch

%description %_description

%package -n     python3-pip
Summary:        %{summary}

%description -n python3-pip %_description


%prep
%autosetup -p1 -n pip-%{version}


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


%files -n python3-pip -f %{pyproject_files}
%{_bindir}/pip
%{_bindir}/pip3

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 26.0.1-1
- Import
