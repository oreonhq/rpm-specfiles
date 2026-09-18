%global source0_hash none

Name:           python-sqlite-migrate
Version:        0.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Compatibility package for sqlite-utils migrations

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            https://github.com/simonw/sqlite-migrate
Source:         %{pypi_source sqlite_migrate}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'sqlite-migrate' generated automatically by pyp2spec.}

Patch:          python-sqlite-migrate-0.1b0-toml.patch

%description %_description

%package -n     python3-sqlite-migrate
Summary:        %{summary}

%description -n python3-sqlite-migrate %_description


%prep
%autosetup -p1 -n sqlite_migrate-%{version}


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


%files -n python3-sqlite-migrate -f %{pyproject_files}

%changelog
%autochangelog
