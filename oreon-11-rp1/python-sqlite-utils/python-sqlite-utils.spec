%global source0_hash none

Name:           python-sqlite-utils
Version:        4.2.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        CLI tool and Python library for manipulating SQLite databases

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/simonw/sqlite-utils
Source:         %{pypi_source sqlite_utils}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'sqlite-utils' generated automatically by pyp2spec.}

Patch:          python-sqlite-utils-3.38-click.patch

%description %_description

%package -n     python3-sqlite-utils
Summary:        %{summary}

%description -n python3-sqlite-utils %_description


%prep
%autosetup -p1 -n sqlite_utils-%{version}


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


%files -n python3-sqlite-utils -f %{pyproject_files}
%{_bindir}/sqlite-utils

%changelog
%autochangelog
