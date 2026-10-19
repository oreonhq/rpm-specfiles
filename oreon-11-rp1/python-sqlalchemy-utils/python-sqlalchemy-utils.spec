%global source0_hash 881f9cd9e5044dc8f827bccb0425ce2e55490ce44fc0bb848c55cc8ee44cc02e
Name:           python-sqlalchemy-utils
Version:        0.42.1
Release:        1%{?dist}
Summary:        Various utility functions for SQLAlchemy.
License:        BSD-3-Clause
URL:            https://github.com/kvesteri/sqlalchemy-utils
Source0:        https://files.pythonhosted.org/packages/source/s/sqlalchemy_utils/sqlalchemy_utils-%{version}.tar.gz
BuildArch:      noarch
Patch0:             no-psycopg2cffi.patch
Patch1:             python-sqlalchemy-utils-0.41.1-no-pyodbc-dep.patch
Patch2:             python-sqlalchemy-utils-0.41.1-nosqla2.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77.0.0
Requires:       python3-sqlalchemy-utils = %{version}-%{release}
# /oreon:deps
%package -n       python3-sqlalchemy-utils+test
Summary:        Metapackage for python3-sqlalchemy-utils test extras
Requires:       python3-sqlalchemy-utils = %{version}-%{release}
Requires:       python3dist(pytest) == 7.4.4
Requires:       python3dist(pygments) >= 1.2
Requires:       python3dist(jinja2) >= 2.3
Requires:       python3dist(docutils) >= 0.10
Requires:       python3dist(flexmock) >= 0.9.7
Requires:       python3dist(psycopg) >= 3.1.8
Requires:       python3dist(psycopg2) >= 2.5.1
Requires:       python3dist(psycopg2cffi) >= 2.8.1
Requires:       python3dist(pg8000) >= 1.12.4
Requires:       python3dist(pytz) >= 2014.2
Requires:       python3dist(python-dateutil) >= 2.6
Requires:       python3dist(flake8) >= 2.4.0
Requires:       python3dist(isort) >= 4.2.2
Provides:       python3dist(sqlalchemy-utils[test]) = %{version}-%{release}

%description -n python3-sqlalchemy-utils+test
Metapackage for python3-sqlalchemy-utils test extras.

%package -n       python3-sqlalchemy-utils+babel
Summary:        Metapackage for python3-sqlalchemy-utils babel extras
Requires:       python3-sqlalchemy-utils = %{version}-%{release}
Requires:       python3dist(babel) >= 1.3
Provides:       python3dist(sqlalchemy-utils[babel]) = %{version}-%{release}

%description -n python3-sqlalchemy-utils+babel
Metapackage for python3-sqlalchemy-utils babel extras.

%package -n       python3-sqlalchemy-utils+arrow
Summary:        Metapackage for python3-sqlalchemy-utils arrow extras
Requires:       python3-sqlalchemy-utils = %{version}-%{release}
Requires:       python3dist(arrow) >= 0.3.4
Provides:       python3dist(sqlalchemy-utils[arrow]) = %{version}-%{release}

%description -n python3-sqlalchemy-utils+arrow
Metapackage for python3-sqlalchemy-utils arrow extras.

%package -n       python3-sqlalchemy-utils+pendulum
Summary:        Metapackage for python3-sqlalchemy-utils pendulum extras
Requires:       python3-sqlalchemy-utils = %{version}-%{release}
Requires:       python3dist(pendulum) >= 2.0.5
Provides:       python3dist(sqlalchemy-utils[pendulum]) = %{version}-%{release}

%description -n python3-sqlalchemy-utils+pendulum
Metapackage for python3-sqlalchemy-utils pendulum extras.

%package -n       python3-sqlalchemy-utils+intervals
Summary:        Metapackage for python3-sqlalchemy-utils intervals extras
Requires:       python3-sqlalchemy-utils = %{version}-%{release}
Requires:       python3dist(intervals) >= 0.7.1
Provides:       python3dist(sqlalchemy-utils[intervals]) = %{version}-%{release}

%description -n python3-sqlalchemy-utils+intervals
Metapackage for python3-sqlalchemy-utils intervals extras.

%package -n       python3-sqlalchemy-utils+phone
Summary:        Metapackage for python3-sqlalchemy-utils phone extras
Requires:       python3-sqlalchemy-utils = %{version}-%{release}
Requires:       python3dist(phonenumbers) >= 5.9.2
Provides:       python3dist(sqlalchemy-utils[phone]) = %{version}-%{release}

%description -n python3-sqlalchemy-utils+phone
Metapackage for python3-sqlalchemy-utils phone extras.

%package -n       python3-sqlalchemy-utils+password
Summary:        Metapackage for python3-sqlalchemy-utils password extras
Requires:       python3-sqlalchemy-utils = %{version}-%{release}
Requires:       python3dist(passlib) >= 1.6
Requires:       python3dist(passlib) < 2.0
Provides:       python3dist(sqlalchemy-utils[password]) = %{version}-%{release}

%description -n python3-sqlalchemy-utils+password
Metapackage for python3-sqlalchemy-utils password extras.

%package -n       python3-sqlalchemy-utils+color
Summary:        Metapackage for python3-sqlalchemy-utils color extras
Requires:       python3-sqlalchemy-utils = %{version}-%{release}
Requires:       python3dist(colour) >= 0.0.4
Provides:       python3dist(sqlalchemy-utils[color]) = %{version}-%{release}

%description -n python3-sqlalchemy-utils+color
Metapackage for python3-sqlalchemy-utils color extras.

%package -n       python3-sqlalchemy-utils+timezone
Summary:        Metapackage for python3-sqlalchemy-utils timezone extras
Requires:       python3-sqlalchemy-utils = %{version}-%{release}
Provides:       python3dist(sqlalchemy-utils[timezone]) = %{version}-%{release}

%description -n python3-sqlalchemy-utils+timezone
Metapackage for python3-sqlalchemy-utils timezone extras.

%package -n       python3-sqlalchemy-utils+url
Summary:        Metapackage for python3-sqlalchemy-utils url extras
Requires:       python3-sqlalchemy-utils = %{version}-%{release}
Requires:       python3dist(furl) >= 0.4.1
Provides:       python3dist(sqlalchemy-utils[url]) = %{version}-%{release}

%description -n python3-sqlalchemy-utils+url
Metapackage for python3-sqlalchemy-utils url extras.

%package -n       python3-sqlalchemy-utils+encrypted
Summary:        Metapackage for python3-sqlalchemy-utils encrypted extras
Requires:       python3-sqlalchemy-utils = %{version}-%{release}
Requires:       python3dist(cryptography) >= 0.6
Provides:       python3dist(sqlalchemy-utils[encrypted]) = %{version}-%{release}

%description -n python3-sqlalchemy-utils+encrypted
Metapackage for python3-sqlalchemy-utils encrypted extras.

%package -n       python3-sqlalchemy-utils+test_all
Summary:        Metapackage for python3-sqlalchemy-utils test_all extras
Requires:       python3-sqlalchemy-utils = %{version}-%{release}
Requires:       python3dist(pytest) == 7.4.4
Requires:       python3dist(pygments) >= 1.2
Requires:       python3dist(jinja2) >= 2.3
Requires:       python3dist(docutils) >= 0.10
Requires:       python3dist(flexmock) >= 0.9.7
Requires:       python3dist(psycopg) >= 3.1.8
Requires:       python3dist(psycopg2) >= 2.5.1
Requires:       python3dist(psycopg2cffi) >= 2.8.1
Requires:       python3dist(pg8000) >= 1.12.4
Requires:       python3dist(pytz) >= 2014.2
Requires:       python3dist(python-dateutil) >= 2.6
Requires:       python3dist(flake8) >= 2.4.0
Requires:       python3dist(isort) >= 4.2.2
Requires:       python3dist(babel) >= 1.3
Requires:       python3dist(arrow) >= 0.3.4
Requires:       python3dist(pendulum) >= 2.0.5
Requires:       python3dist(intervals) >= 0.7.1
Requires:       python3dist(phonenumbers) >= 5.9.2
Requires:       python3dist(passlib) >= 1.6
Requires:       python3dist(passlib) < 2.0
Requires:       python3dist(colour) >= 0.0.4
Requires:       python3dist(furl) >= 0.4.1
Requires:       python3dist(cryptography) >= 0.6
Provides:       python3dist(sqlalchemy-utils[test_all]) = %{version}-%{release}

%description -n python3-sqlalchemy-utils+test_all
Metapackage for python3-sqlalchemy-utils test_all extras.

%description

%package -n     python3-sqlalchemy-utils
Summary:        Various utility functions for SQLAlchemy.
# oreon:reqs
Requires:       python3dist(sqlalchemy) >= 1.4
# /oreon:reqs
%description -n python3-sqlalchemy-utils

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir sqlalchemy_utils-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sqlalchemy-utils usr/lib/python3*/site-packages/sqlalchemy_utils* usr/lib64/python3*/site-packages/sqlalchemy_utils* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sqlalchemy_utils* usr/lib64/python3*/site-packages/sqlalchemy_utils* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sqlalchemy-utils -f %{oreon_filedir}/python3-sqlalchemy-utils.list

%changelog

%autochangelog
