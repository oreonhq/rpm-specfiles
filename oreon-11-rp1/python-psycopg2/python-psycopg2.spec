%global source0_hash none

Name:           python-psycopg2
Version:        2.9.13
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        psycopg2 - Python-PostgreSQL Database Adapter

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://psycopg.org/
Source:         %{pypi_source psycopg2}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'psycopg2' generated automatically by pyp2spec.}

Patch0: test_types_extras-2.9.3-test_from_tables.patch

%description %_description

%package -n     python3-psycopg2
Summary:        %{summary}

%description -n python3-psycopg2 %_description


%prep
%autosetup -p1 -n psycopg2-%{version}


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


%files -n python3-psycopg2 -f %{pyproject_files}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.9.10-5
- Prepare for Oreon 11 (RP1)
