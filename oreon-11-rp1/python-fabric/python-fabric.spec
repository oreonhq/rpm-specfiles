%global source0_hash none

Name:           python-fabric
Version:        3.2.3
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        High level SSH command execution

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/fabric/fabric
Source:         %{pypi_source fabric}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'fabric' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-fabric
Summary:        %{summary}

%description -n python3-fabric %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-fabric pytest,testing


%prep
%autosetup -p1 -n fabric-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x pytest,testing


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-fabric -f %{pyproject_files}
%{_bindir}/fab

%changelog
%autochangelog
