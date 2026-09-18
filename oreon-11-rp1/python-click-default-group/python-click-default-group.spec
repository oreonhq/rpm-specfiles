%global source0_hash none

Name:           python-click-default-group
Version:        1.2.4
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        click_default_group

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        LicenseRef-Fedora-Public-Domain
URL:            https://github.com/click-contrib/click-default-group
Source:         %{pypi_source click_default_group}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'click-default-group' generated automatically by pyp2spec.}

Patch0:         https://patch-diff.githubusercontent.com/raw/click-contrib/click-default-group/pull/18.patch#/0001-Fix-detection-of-error-message.patch

%description %_description

%package -n     python3-click-default-group
Summary:        %{summary}

%description -n python3-click-default-group %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-click-default-group test


%prep
%autosetup -p1 -n click_default_group-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-click-default-group -f %{pyproject_files}

%changelog
%autochangelog
