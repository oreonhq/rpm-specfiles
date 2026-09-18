%global source0_hash none

Name:           python-idna
Version:        3.20
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Internationalized Domain Names in Applications _IDNA_

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/kjd/idna
Source:         %{pypi_source idna}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'idna' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-idna
Summary:        %{summary}

%description -n python3-idna %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-idna all


%prep
%autosetup -p1 -n idna-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x all


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-idna -f %{pyproject_files}
%{_bindir}/idna

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.11-1
- Prepare for Oreon 11 (RP1)
