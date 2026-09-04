%global source0_hash 0033f2dfa89ae5f700b77875c6989172e6f4bf1170a3227f066e63c5b6e6f83f

Name: python-beaker
Version: 1.14.1
Release: 1%{?dist}
Summary: WSGI middleware layer to provide sessions
# Automatically converted from old format: BSD and MIT - review is highly recommended.
License: LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL: http://beaker.readthedocs.io
Source0: https://github.com/bbangert/beaker/archive/%{version}/beaker-%{version}.tar.gz
BuildArch: noarch

BuildRequires:  %{_bindir}/redis-server
BuildRequires:  %{_bindir}/netstat

%global _description\
Beaker is a caching library that includes Session and Cache objects built on\
Myghty's Container API used in MyghtyUtils. WSGI middleware is also included to\
manage Session objects and signed cookies.

Patch:          beaker-use-system-paste.patch
Patch:          unittest.mock.patch
# https://github.com/bbangert/beaker/issues/242
# https://github.com/bbangert/beaker/pull/243
# Avoid the new dbm.sqlite3 backend to fix tests
Patch:          0001-Avoid-using-dbm.sqlite3-242.patch

%description %_description

%package -n python3-beaker
Summary: %summary
BuildRequires: python3-devel
BuildRequires: python3dist(cryptography)
BuildRequires: python3dist(funcsigs)
BuildRequires: python3dist(paste)
BuildRequires: python3dist(pycrypto)
BuildRequires: python3dist(redis)
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(sqlalchemy)
BuildRequires: python3dist(webtest)
# for tests
BuildRequires: python3dist(pytest)
BuildRequires: glibc-langpack-it

Requires: python3dist(paste)
Recommends: python3dist(cryptography)
Recommends: python3dist(pycrypto)
Recommends: python3dist(pycryptodome)
Recommends: python3dist(pycryptopp)

%{?python_provide:%python_provide python3-beaker}

%description -n python3-beaker %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n beaker-%{version}

%build
%py3_build

%install
%py3_install

%check
# we can't test mongo
rm -f tests/test_managers/test_ext_mongodb.py

redis-server &

%pytest

%files -n python3-beaker
%license LICENSE
%doc README.rst CHANGELOG
%{python3_sitelib}/beaker/
%{python3_sitelib}/Beaker*

%changelog
%autochangelog
