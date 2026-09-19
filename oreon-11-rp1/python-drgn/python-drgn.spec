%global source0_hash none

Name:           python-drgn
Version:        1.1.99
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Programmable debugger

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        LGPL-2.1-or-later
URL:            https://github.com/osandov/drgn/issues
Source:         %{pypi_source drgn}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'drgn' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-drgn
Summary:        %{summary}

%description -n python3-drgn %_description


%prep
%autosetup -p1 -n drgn-%{version}


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


%files -n python3-drgn -f %{pyproject_files}
%{_bindir}/drgn
%{_bindir}/drgn-crash

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1.0-1
- Prepare for Oreon 11 (RP1)
