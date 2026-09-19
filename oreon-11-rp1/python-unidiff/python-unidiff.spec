%global source0_hash none

Name:           python-unidiff
Version:        1.0.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Unified diff parsing/metadata extraction library.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/matiasb/python-unidiff
Source:         %{pypi_source unidiff}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'unidiff' generated automatically by pyp2spec.}

Patch1: 0001-use-setuptools-console_scripts-for-usr-bin-unidiff.patch

%description %_description

%package -n     python3-unidiff
Summary:        %{summary}

%description -n python3-unidiff %_description


%prep
%autosetup -p1 -n unidiff-%{version}


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


%files -n python3-unidiff -f %{pyproject_files}
%{_bindir}/unidiff

%changelog
%autochangelog
