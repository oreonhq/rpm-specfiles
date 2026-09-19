%global source0_hash none

Name:           python-mysqlclient
Version:        2.3.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python interface to MySQL

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        GPL-2.0-or-later
URL:            https://github.com/PyMySQL/mysqlclient
Source:         %{pypi_source mysqlclient}

BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'mysqlclient' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-mysqlclient
Summary:        %{summary}

%description -n python3-mysqlclient %_description


%prep
%autosetup -p1 -n mysqlclient-%{version}


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


%files -n python3-mysqlclient -f %{pyproject_files}

%changelog
%autochangelog
