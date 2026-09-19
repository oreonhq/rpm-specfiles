%global source0_hash none

Name:           python-dependency-groups
Version:        1.3.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A tool for resolving PEP 735 Dependency Group data

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/pypa/dependency-groups
Source:         %{pypi_source dependency_groups}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'dependency-groups' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-dependency-groups
Summary:        %{summary}

%description -n python3-dependency-groups %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-dependency-groups cli


%prep
%autosetup -p1 -n dependency_groups-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x cli


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-dependency-groups -f %{pyproject_files}
%{_bindir}/dependency-groups
%{_bindir}/lint-dependency-groups
%{_bindir}/pip-install-dependency-groups

%changelog
%autochangelog
