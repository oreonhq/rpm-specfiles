%global source0_hash none

Name:           python-nihtest
Version:        1.11.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A testing tool for command line utilities.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/nih-at/nihtest
Source:         %{pypi_source nihtest}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'nihtest' generated automatically by pyp2spec.}

Patch:          run_tests_using_cmake_and_ctest.patch

%description %_description

%package -n     python3-nihtest
Summary:        %{summary}

%description -n python3-nihtest %_description


%prep
%autosetup -p1 -n nihtest-%{version}


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


%files -n python3-nihtest -f %{pyproject_files}
%{_bindir}/nihtest

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.9.1-1
- Prepare for Oreon 11 (RP1)
