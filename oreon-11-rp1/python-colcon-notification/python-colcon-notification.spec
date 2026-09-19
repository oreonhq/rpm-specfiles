%global source0_hash none

Name:           python-colcon-notification
Version:        0.3.3
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Extension for colcon to provide status notifications.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/colcon/colcon-notification/
Source:         %{pypi_source colcon_notification}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'colcon-notification' generated automatically by pyp2spec.}

Patch0:         %{name}-0.2.8-data-files.patch

%description %_description

%package -n     python3-colcon-notification
Summary:        %{summary}

%description -n python3-colcon-notification %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-colcon-notification test


%prep
%autosetup -p1 -n colcon_notification-%{version}


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


%files -n python3-colcon-notification -f %{pyproject_files}

%changelog
%autochangelog
