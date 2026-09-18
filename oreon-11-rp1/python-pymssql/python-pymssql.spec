%global source0_hash none

Name:           python-pymssql
Version:        2.4.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        DB-API interface to Microsoft SQL Server for Python. _new Cython-based version_

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/pymssql/pymssql
Source:         %{pypi_source pymssql}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pymssql' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-pymssql
Summary:        %{summary}

%description -n python3-pymssql %_description


%prep
%autosetup -p1 -n pymssql-%{version}


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


%files -n python3-pymssql -f %{pyproject_files}

%changelog
%autochangelog
