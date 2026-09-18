%global source0_hash none

Name:           python-flask-admin
Version:        2.2.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Simple and extensible admin interface framework for Flask

# No license information obtained, it's up to the packager to fill it in
License:        ...
URL:            https://github.com/pallets-eco/flask-admin/
Source:         %{pypi_source flask_admin}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'flask-admin' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-flask-admin
Summary:        %{summary}

%description -n python3-flask-admin %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-flask-admin all,azure-blob-storage,export,geoalchemy,images,mongoengine,peewee,pymongo,rediscli,s3,sqlalchemy,sqlalchemy-lite,sqlalchemy-with-utils,translation


%prep
%autosetup -p1 -n flask_admin-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x all,azure-blob-storage,export,geoalchemy,images,mongoengine,peewee,pymongo,rediscli,s3,sqlalchemy,sqlalchemy-lite,sqlalchemy-with-utils,translation


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-flask-admin -f %{pyproject_files}

%changelog
%autochangelog
