%global source0_hash none

Name:           python-scikit-build-core
Version:        1.0.3
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Build backend for CMake based projects

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/scikit-build/scikit-build-core
Source:         %{pypi_source scikit_build_core}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'scikit-build-core' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-scikit-build-core
Summary:        %{summary}

%description -n python3-scikit-build-core %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-scikit-build-core hatchling,setuptools,wheel-free-setuptools,wheels


%prep
%autosetup -p1 -n scikit_build_core-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x hatchling,setuptools,wheel-free-setuptools,wheels


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-scikit-build-core -f %{pyproject_files}
%{_bindir}/scikit-build
%{_bindir}/scikit-build-core

%changelog
%autochangelog
