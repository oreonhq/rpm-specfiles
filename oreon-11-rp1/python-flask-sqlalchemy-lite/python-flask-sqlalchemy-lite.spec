%global source0_hash 6de2f70c835a2c0a11264cbbc0cc33e7ed9732a52ee056781c5739e960213d2f
%global srcname flask_sqlalchemy_lite
Name:           python-flask-sqlalchemy-lite
Version:        0.2.1
Release:        2%{?dist}
Summary:        Adds SQLAlchemy support to Flask application
License:        MIT
URL:            https://github.com/pallets-eco/flask-sqlalchemy-lite
Source0:        https://files.pythonhosted.org/packages/source/f/flask_sqlalchemy_lite/flask_sqlalchemy_lite-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
Requires:       python3-flask-sqlalchemy-lite = %{version}-%{release}
# /oreon:deps
%description
Integrate SQLAlchemy with Flask. Use Flask's config to define SQLAlchemy
database engines. Create SQLAlchemy ORM sessions that are cleaned up
automatically after requests.

Intended to be a replacement for Flask-SQLAlchemy. Unlike the prior extension,
this one does not attempt to manage the model base class, tables, metadata, or
multiple binds for sessions. This makes the extension much simpler, letting the
developer use standard SQLAlchemy instead.

%package -n python3-flask-sqlalchemy-lite
Summary:        Adds SQLAlchemy support to Flask application
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%py_provides    python3-%{srcname}
# oreon:reqs
Requires:       python3dist(flask[async]) >= 3.0.0
Requires:       python3dist(sqlalchemy[asyncio]) >= 2.0.31
# /oreon:reqs
%description -n python3-flask-sqlalchemy-lite
Integrate SQLAlchemy with Flask. Use Flask's config to define SQLAlchemy
database engines. Create SQLAlchemy ORM sessions that are cleaned up
automatically after requests.

Intended to be a replacement for Flask-SQLAlchemy. Unlike the prior extension,
this one does not attempt to manage the model base class, tables, metadata, or
multiple binds for sessions. This makes the extension much simpler, letting the
developer use standard SQLAlchemy instead.

Python 3 version.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-flask-sqlalchemy-lite usr/lib/python3*/site-packages/flask_sqlalchemy_lite* usr/lib64/python3*/site-packages/flask_sqlalchemy_lite* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/flask_sqlalchemy_lite* usr/lib64/python3*/site-packages/flask_sqlalchemy_lite* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-flask-sqlalchemy-lite -f %{oreon_filedir}/python3-flask-sqlalchemy-lite.list

%changelog

%autochangelog
