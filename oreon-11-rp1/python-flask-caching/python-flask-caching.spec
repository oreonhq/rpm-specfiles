%global source0_hash none

Name:           python-flask-caching
Version:        2.5.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Adds caching support to Flask applications.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/pallets-eco/flask-caching
Source:         %{pypi_source flask_caching}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'flask-caching' generated automatically by pyp2spec.}

Patch:          https://github.com/pallets-eco/flask-caching/pull/599/commits/3c8df1714292549d2fe27fa4a03110657fd647a3.patch

%description %_description

%package -n     python3-flask-caching
Summary:        %{summary}

%description -n python3-flask-caching %_description


%prep
%autosetup -p1 -n flask_caching-%{version}


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


%files -n python3-flask-caching -f %{pyproject_files}

%changelog
%autochangelog
