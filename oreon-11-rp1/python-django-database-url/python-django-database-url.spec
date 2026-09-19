%global source0_hash none

Name:           python-dj-database-url
Version:        3.1.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Use Database URLs in your Django Application.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://jazzband.co/projects/dj-database-url
Source:         %{pypi_source dj_database_url}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'dj-database-url' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-dj-database-url
Summary:        %{summary}

%description -n python3-dj-database-url %_description


%prep
%autosetup -p1 -n dj_database_url-%{version}


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


%files -n python3-dj-database-url -f %{pyproject_files}

%changelog
%autochangelog
