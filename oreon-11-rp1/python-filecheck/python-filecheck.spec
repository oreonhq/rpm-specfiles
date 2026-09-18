%global source0_hash none

Name:           python-filecheck
Version:        1.0.6
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        A Python-native clone of LLVMs FileCheck tool

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            ...
Source:         %{pypi_source filecheck}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'filecheck' generated automatically by pyp2spec.}

Patch0: %{name}-tests-x86_64.patch
Patch1: %{name}-no-coverage.patch

%description %_description

%package -n     python3-filecheck
Summary:        %{summary}

%description -n python3-filecheck %_description


%prep
%autosetup -p1 -n filecheck-%{version}


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


%files -n python3-filecheck -f %{pyproject_files}
%{_bindir}/filecheck

%changelog
%autochangelog
