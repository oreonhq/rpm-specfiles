%global source0_hash none

Name:           python-wheel
Version:        0.48.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Command line tool for manipulating wheel files

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/pypa/wheel
Source:         %{pypi_source wheel}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'wheel' generated automatically by pyp2spec.}

Patch:          https://github.com/pypa/wheel/commit/3028d3.patch
Patch:        https://github.com/pypa/wheel/commit/3028d3.patch
Patch:        https://github.com/pypa/wheel/commit/3028d3.patch

%description %_description

%package -n     python3-wheel
Summary:        %{summary}

%description -n python3-wheel %_description


%prep
%autosetup -p1 -n wheel-%{version}


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


%files -n python3-wheel -f %{pyproject_files}
%{_bindir}/wheel

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.45.1-1
- Prepare for Oreon 11 (RP1)
