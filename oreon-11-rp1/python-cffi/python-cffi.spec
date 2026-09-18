%global source0_hash none

Name:           python-cffi
Version:        2.1.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Foreign Function Interface for Python calling C code.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT-0
URL:            https://github.com/python-cffi/cffi
Source:         %{pypi_source cffi}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'cffi' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-cffi
Summary:        %{summary}

%description -n python3-cffi %_description


%prep
%autosetup -p1 -n cffi-%{version}


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


%files -n python3-cffi -f %{pyproject_files}
%{_bindir}/cffi-gen-src

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.0-1
- Prepare for Oreon 11 (RP1)
