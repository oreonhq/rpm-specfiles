%global source0_hash 4a5b844789c10076da89320563600a7addf781e73ab315ae800521b3ec018509
Name:           python-flask-admin
Version:        2.2.0
Release:        1%{?dist}
Summary:        Simple and extensible admin interface framework for Flask
License:        ...
URL:            https://github.com/pallets-eco/flask-admin/
Source0:        https://files.pythonhosted.org/packages/source/f/flask_admin/flask_admin-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
Requires:       python3-flask-admin = %{version}-%{release}
# /oreon:deps
%package -n       python3-flask-admin+sqlalchemy
Summary:        Metapackage for python3-flask-admin sqlalchemy extras
Requires:       python3-flask-admin = %{version}-%{release}
Requires:       python3dist(flask-sqlalchemy) >= 3
Requires:       python3dist(sqlalchemy) >= 1.4
Provides:       python3dist(flask-admin[sqlalchemy]) = %{version}-%{release}

%description -n python3-flask-admin+sqlalchemy
Metapackage for python3-flask-admin sqlalchemy extras.

%package -n       python3-flask-admin+sqlalchemy-lite
Summary:        Metapackage for python3-flask-admin sqlalchemy-lite extras
Requires:       python3-flask-admin = %{version}-%{release}
Provides:       python3dist(flask-admin[sqlalchemy-lite]) = %{version}-%{release}

%description -n python3-flask-admin+sqlalchemy-lite
Metapackage for python3-flask-admin sqlalchemy-lite extras.

%package -n       python3-flask-admin+sqlalchemy-with-utils
Summary:        Metapackage for python3-flask-admin sqlalchemy-with-utils extras
Requires:       python3-flask-admin = %{version}-%{release}
Requires:       python3dist(sqlalchemy-utils) >= 0.38.0
Requires:       python3dist(sqlalchemy-citext) >= 1.8.0
Requires:       python3dist(colour) >= 0.1.5
Requires:       python3dist(email-validator) >= 2
Requires:       python3dist(arrow) >= 0.14.0
Provides:       python3dist(flask-admin[sqlalchemy-with-utils]) = %{version}-%{release}

%description -n python3-flask-admin+sqlalchemy-with-utils
Metapackage for python3-flask-admin sqlalchemy-with-utils extras.

%package -n       python3-flask-admin+geoalchemy
Summary:        Metapackage for python3-flask-admin geoalchemy extras
Requires:       python3-flask-admin = %{version}-%{release}
Requires:       python3dist(geoalchemy2) >= 0.14.0
Requires:       python3dist(shapely) >= 2
Provides:       python3dist(flask-admin[geoalchemy]) = %{version}-%{release}

%description -n python3-flask-admin+geoalchemy
Metapackage for python3-flask-admin geoalchemy extras.

%package -n       python3-flask-admin+pymongo
Summary:        Metapackage for python3-flask-admin pymongo extras
Requires:       python3-flask-admin = %{version}-%{release}
Requires:       python3dist(pymongo) >= 3.10.0
Provides:       python3dist(flask-admin[pymongo]) = %{version}-%{release}

%description -n python3-flask-admin+pymongo
Metapackage for python3-flask-admin pymongo extras.

%package -n       python3-flask-admin+mongoengine
Summary:        Metapackage for python3-flask-admin mongoengine extras
Requires:       python3-flask-admin = %{version}-%{release}
Requires:       python3dist(mongoengine) >= 0.29.0
Provides:       python3dist(flask-admin[mongoengine]) = %{version}-%{release}

%description -n python3-flask-admin+mongoengine
Metapackage for python3-flask-admin mongoengine extras.

%package -n       python3-flask-admin+peewee
Summary:        Metapackage for python3-flask-admin peewee extras
Requires:       python3-flask-admin = %{version}-%{release}
Requires:       python3dist(peewee) >= 3.14.0
Requires:       python3dist(wtf-peewee) >= 3.0.4
Provides:       python3dist(flask-admin[peewee]) = %{version}-%{release}

%description -n python3-flask-admin+peewee
Metapackage for python3-flask-admin peewee extras.

%package -n       python3-flask-admin+s3
Summary:        Metapackage for python3-flask-admin s3 extras
Requires:       python3-flask-admin = %{version}-%{release}
Requires:       python3dist(boto3) >= 1.33
Provides:       python3dist(flask-admin[s3]) = %{version}-%{release}

%description -n python3-flask-admin+s3
Metapackage for python3-flask-admin s3 extras.

%package -n       python3-flask-admin+azure-blob-storage
Summary:        Metapackage for python3-flask-admin azure-blob-storage extras
Requires:       python3-flask-admin = %{version}-%{release}
Requires:       python3dist(azure-storage-blob) >= 12.0.0
Provides:       python3dist(flask-admin[azure-blob-storage]) = %{version}-%{release}

%description -n python3-flask-admin+azure-blob-storage
Metapackage for python3-flask-admin azure-blob-storage extras.

%package -n       python3-flask-admin+images
Summary:        Metapackage for python3-flask-admin images extras
Requires:       python3-flask-admin = %{version}-%{release}
Requires:       python3dist(pillow) >= 10.0.0
Provides:       python3dist(flask-admin[images]) = %{version}-%{release}

%description -n python3-flask-admin+images
Metapackage for python3-flask-admin images extras.

%package -n       python3-flask-admin+export
Summary:        Metapackage for python3-flask-admin export extras
Requires:       python3-flask-admin = %{version}-%{release}
Requires:       python3dist(tablib) >= 3.0.0
Provides:       python3dist(flask-admin[export]) = %{version}-%{release}

%description -n python3-flask-admin+export
Metapackage for python3-flask-admin export extras.

%package -n       python3-flask-admin+rediscli
Summary:        Metapackage for python3-flask-admin rediscli extras
Requires:       python3-flask-admin = %{version}-%{release}
Requires:       python3dist(redis) >= 4.0.0
Provides:       python3dist(flask-admin[rediscli]) = %{version}-%{release}

%description -n python3-flask-admin+rediscli
Metapackage for python3-flask-admin rediscli extras.

%package -n       python3-flask-admin+translation
Summary:        Metapackage for python3-flask-admin translation extras
Requires:       python3-flask-admin = %{version}-%{release}
Requires:       python3dist(flask-babel) >= 3.0.1
Provides:       python3dist(flask-admin[translation]) = %{version}-%{release}

%description -n python3-flask-admin+translation
Metapackage for python3-flask-admin translation extras.

%package -n       python3-flask-admin+all
Summary:        Metapackage for python3-flask-admin all extras
Requires:       python3-flask-admin = %{version}-%{release}
Provides:       python3dist(flask-admin[all]) = %{version}-%{release}

%description -n python3-flask-admin+all
Metapackage for python3-flask-admin all extras.

%description

%package -n     python3-flask-admin
Summary:        Simple and extensible admin interface framework for Flask
# oreon:reqs
Requires:       python3dist(flask) >= 2.0
Requires:       python3dist(jinja2) >= 3.0
Requires:       python3dist(markupsafe) >= 2.0
Requires:       python3dist(werkzeug) >= 2.0
Requires:       python3dist(wtforms) >= 2.3
# /oreon:reqs
%description -n python3-flask-admin

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir flask_admin-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-flask-admin usr/lib/python3*/site-packages/flask_admin* usr/lib64/python3*/site-packages/flask_admin* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/flask_admin* usr/lib64/python3*/site-packages/flask_admin* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-flask-admin -f %{oreon_filedir}/python3-flask-admin.list

%changelog

%autochangelog
