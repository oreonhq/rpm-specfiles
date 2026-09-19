%global source0_hash none

Name:           python-catkin-tools
Version:        0.9.5
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Command line tools for working with catkin.

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://catkin-tools.readthedocs.org/
Source:         %{pypi_source catkin_tools}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'catkin-tools' generated automatically by pyp2spec.}

Patch0:         %{srcname}-0.9.5-sphinx8.patch
Patch1:         %{name}-rm-python-mock-usage.patch

%description %_description

%package -n     python3-catkin-tools
Summary:        %{summary}

%description -n python3-catkin-tools %_description


%prep
%autosetup -p1 -n catkin_tools-%{version}


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


%files -n python3-catkin-tools -f %{pyproject_files}
%{_bindir}/catkin

%changelog
%autochangelog
