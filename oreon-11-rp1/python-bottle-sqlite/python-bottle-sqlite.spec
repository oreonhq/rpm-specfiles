%global source0_hash e61b9c4b2240d5abb635ce79fb5d5f4e6e6216f68c0d1670add2df0d5d5db618

%global srcname bottle-sqlite
Name:           python-%{srcname}
Version:        0.2.0
Release:        15%{?dist}
Summary:        SQLite3 integration for Bottle WSGI framework

License:        MIT
URL:            http://bottlepy.org
Source0:        https://files.pythonhosted.org/packages/source/b/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
Bottle-sqlite is a plugin that integrates SQLite3 with your Bottle application.
It automatically connects to a database at the beginning of a request, passes
the database handle to the route callback and closes the connection afterwards.

To automatically detect routes that need a database connection, the plugin
searches for route callbacks that require a db keyword argument (configurable)
and skips routes that do not. This removes any overhead for routes that don't
need a database connection.

%package -n python3-%{srcname}
Summary: SQLite3 integration for Bottle WSGI framework

BuildRequires:  python3-devel

Requires:       python3-bottle

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Bottle-sqlite is a plugin that integrates SQLite3 with your Bottle application.
It automatically connects to a database at the beginning of a request, passes
the database handle to the route callback and closes the connection afterwards.

To automatically detect routes that need a database connection, the plugin
searches for route callbacks that require a db keyword argument (configurable)
and skips routes that do not. This removes any overhead for routes that don't
need a database connection.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{srcname}
%doc PKG-INFO README.rst
%{python3_sitelib}/bottle_sqlite.py*
%{python3_sitelib}/__pycache__/bottle_sqlite*
%{python3_sitelib}/bottle_sqlite*.dist-info

%changelog
%autochangelog
