%global source0_hash none

Name:           python-sqlalchemy-utils
Version:        0.42.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Various utility functions for SQLAlchemy.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/kvesteri/sqlalchemy-utils
Source:         %{pypi_source sqlalchemy_utils}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'sqlalchemy-utils' generated automatically by pyp2spec.}

Patch0:             no-psycopg2cffi.patch
Patch1:             python-sqlalchemy-utils-0.41.1-no-pyodbc-dep.patch
Patch2:             python-sqlalchemy-utils-0.41.1-nosqla2.patch

%description %_description

%package -n     python3-sqlalchemy-utils
Summary:        %{summary}

%description -n python3-sqlalchemy-utils %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-sqlalchemy-utils arrow,babel,color,encrypted,intervals,password,pendulum,phone,test,test-all,timezone,url


%prep
%autosetup -p1 -n sqlalchemy_utils-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x arrow,babel,color,encrypted,intervals,password,pendulum,phone,test,test-all,timezone,url


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-sqlalchemy-utils -f %{pyproject_files}

%changelog
%autochangelog
