%global source0_hash none

Name:           python-colcon-core
Version:        0.21.3
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Command line tool to build sets of software packages.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/colcon/colcon-core/
Source:         %{pypi_source colcon_core}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'colcon-core' generated automatically by pyp2spec.}

Patch0:         %{name}-0.5.3-remove-pytest.patch
Patch1:         %{name}-0.19.0-pytest-compat.patch

%description %_description

%package -n     python3-colcon-core
Summary:        %{summary}

%description -n python3-colcon-core %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-colcon-core test


%prep
%autosetup -p1 -n colcon_core-%{version}


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


%files -n python3-colcon-core -f %{pyproject_files}
%{_bindir}/colcon

%changelog
%autochangelog
