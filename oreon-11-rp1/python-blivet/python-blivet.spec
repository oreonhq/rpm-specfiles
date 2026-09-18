%global source0_hash none

Name:           python-blivet
Version:        3.14.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python module for system storage configuration

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        GPL-2.0-or-later
URL:            https://github.com/storaged-project/blivet
Source:         %{pypi_source blivet}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'blivet' generated automatically by pyp2spec.}

Patch0:        0001-remove-btrfs-plugin.patch
Patch1:        0002-Ignore-btrfs-mount-errors-during-storage-scan.patch

%description %_description

%package -n     python3-blivet
Summary:        %{summary}

%description -n python3-blivet %_description


%prep
%autosetup -p1 -n blivet-%{version}


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


%files -n python3-blivet -f %{pyproject_files}

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:3.13.2-2
- Import
