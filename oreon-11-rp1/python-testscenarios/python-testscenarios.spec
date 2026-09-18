%global source0_hash none

Name:           python-testscenarios
Version:        0.7.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Testscenarios, a unittest extension for dependency injection

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://github.com/testing-cabal/testscenarios
Source:         %{pypi_source testscenarios}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'testscenarios' generated automatically by pyp2spec.}

Patch:          https://github.com/testing-cabal/testscenarios/pull/1.patch

%description %_description

%package -n     python3-testscenarios
Summary:        %{summary}

%description -n python3-testscenarios %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-testscenarios dev,test


%prep
%autosetup -p1 -n testscenarios-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-testscenarios -f %{pyproject_files}

%changelog
%autochangelog
