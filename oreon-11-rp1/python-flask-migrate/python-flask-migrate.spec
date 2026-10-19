%global source0_hash 253b7f6d27c9da82246507456d5e4eea0d6ae0b88f2b27a6748a2cb3e11e1ee5
Name:               python-flask-migrate
Version:            4.1.0
Release:        1%{?dist}
Summary:        SQLAlchemy database migrations for Flask applications using Alembic
License:            MIT
URL:                https://github.com/miguelgrinberg/Flask-Migrate
Source0:        https://github.com/miguelgrinberg/Flask-Migrate/archive/v%{version}/Flask-Migrate-%{version}.tar.gz
BuildArch:          noarch
%global common_description %{expand:
SQLAlchemy database migrations for Flask applications using Alembic.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.2
Requires:       python3-flask-migrate = %{version}-%{release}
# /oreon:deps
%package -n       python3-flask-migrate+dev
Summary:        Metapackage for python3-flask-migrate dev extras
Requires:       python3-flask-migrate = %{version}-%{release}
Provides:       python3dist(flask-migrate[dev]) = %{version}-%{release}

%description -n python3-flask-migrate+dev
Metapackage for python3-flask-migrate dev extras.

%package -n       python3-flask-migrate+docs
Summary:        Metapackage for python3-flask-migrate docs extras
Requires:       python3-flask-migrate = %{version}-%{release}
Provides:       python3dist(flask-migrate[docs]) = %{version}-%{release}

%description -n python3-flask-migrate+docs
Metapackage for python3-flask-migrate docs extras.

%description %{common_description}

%package -n python3-flask-migrate
Summary:        SQLAlchemy database migrations for Flask applications using Alembic
Obsoletes:          python-flask-migrate-doc < 4.1.0-3
# oreon:reqs
Requires:       python3dist(alembic) >= 1.9.0
Requires:       python3dist(flask) >= 0.9
Requires:       python3dist(flask-sqlalchemy) >= 1.0
# /oreon:reqs
%description -n python3-flask-migrate %{common_description}

%prep

%autosetup -p1
# Fix shebangs that use /bin/env and unversioned Python
%py3_shebang_fix tests/app.py tests/app_multidb.py

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-flask-migrate usr/lib/python3*/site-packages/flask_migrate* usr/lib64/python3*/site-packages/flask_migrate* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/flask_migrate* usr/lib64/python3*/site-packages/flask_migrate* usr/bin/*

%check

%pytest -p no:logging
%files
%files -n python3-flask-migrate -f %{oreon_filedir}/python3-flask-migrate.list

%changelog

%autochangelog
