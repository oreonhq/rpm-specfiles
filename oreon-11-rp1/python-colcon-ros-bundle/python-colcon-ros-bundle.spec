%global source0_hash none

Name:           python-colcon-ros-bundle
Version:        0.1.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Plugin for colcon to bundle ros applications

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/colcon/colcon-bundle/
Source:         %{pypi_source colcon-ros-bundle}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'colcon-ros-bundle' generated automatically by pyp2spec.}

Patch0:         %{name}-0.1.0-unittest-mock.patch

%description %_description

%package -n     python3-colcon-ros-bundle
Summary:        %{summary}

%description -n python3-colcon-ros-bundle %_description


%prep
%autosetup -p1 -n colcon-ros-bundle-%{version}


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


%files -n python3-colcon-ros-bundle -f %{pyproject_files}

%changelog
%autochangelog
