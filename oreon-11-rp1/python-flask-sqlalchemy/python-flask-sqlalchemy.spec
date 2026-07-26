%global source0_hash c5765e58ca145401b52106c0f46178569243c5da25556be2c231ecc60867c5b1

%global srcname flask_sqlalchemy

Name:           python-flask-sqlalchemy
Version:        3.0.5
Release:        %autorelease
Summary:        Adds SQLAlchemy support to Flask application

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/pallets/flask-sqlalchemy
Source0:        %{pypi_source}

BuildArch:      noarch

%description
Flask-SQLAlchemy is an extension for Flask that adds support for
SQLAlchemy to your application. It aims to simplify using SQLAlchemy with
Flask by providing useful defaults and extra helpers that make it easier
to accomplish common tasks.

%package -n python3-flask-sqlalchemy
Summary:        Adds SQLAlchemy support to Flask application
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%py_provides    python3-%{srcname}
# Provide also the legacy name (Flask-SQLAlchemy)
%py_provides    python3-Flask-SQLAlchemy

%description -n python3-flask-sqlalchemy
Flask-SQLAlchemy is an extension for Flask that adds support for
SQLAlchemy to your application. It aims to simplify using SQLAlchemy with
Flask by providing useful defaults and extra helpers that make it easier
to accomplish common tasks.

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files flask_sqlalchemy

%check
%pytest -Wdefault

%files -n python3-flask-sqlalchemy -f %{pyproject_files}
%license LICENSE.rst
%doc docs/ README.rst CHANGES.rst PKG-INFO

%changelog
%autochangelog
