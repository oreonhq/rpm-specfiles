%global source0_hash none

Name:           python-catkin-lint
Version:        1.6.25
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Check catkin packages for common errors

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/fkie/catkin_lint
Source:         %{pypi_source catkin_lint}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'catkin-lint' generated automatically by pyp2spec.}

Patch:          0001-Handle-changed-ntpath.isabs-behaviour-in-Python-3.13.patch

%description %_description

%package -n     python3-catkin-lint
Summary:        %{summary}

%description -n python3-catkin-lint %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-catkin-lint ros


%prep
%autosetup -p1 -n catkin_lint-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x ros


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-catkin-lint -f %{pyproject_files}

%changelog
%autochangelog
