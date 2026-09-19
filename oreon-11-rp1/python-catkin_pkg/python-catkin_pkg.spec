%global source0_hash none

Name:           python-catkin-pkg
Version:        1.1.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        catkin package library

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/ros-infrastructure/catkin_pkg
Source:         %{pypi_source catkin_pkg}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'catkin-pkg' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-catkin-pkg
Summary:        %{summary}

%description -n python3-catkin-pkg %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-catkin-pkg test


%prep
%autosetup -p1 -n catkin_pkg-%{version}


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


%files -n python3-catkin-pkg -f %{pyproject_files}
%{_bindir}/catkin_create_pkg
%{_bindir}/catkin_find_pkg
%{_bindir}/catkin_generate_changelog
%{_bindir}/catkin_package_version
%{_bindir}/catkin_prepare_release
%{_bindir}/catkin_tag_changelog
%{_bindir}/catkin_test_changelog

%changelog
%autochangelog
