%global source0_hash 82ffcd608fea9cfaa903b7731c47a8d36ba346bf49cf98f8dabee83083d08412

%global modname anykeystore

Name:           python-%{modname}
Version:        0.2
Release:        48%{?dist}
Summary:        A key-value store supporting multiple backends
License:        MIT
URL:            http://pypi.python.org/pypi/%{modname}
Source0:        http://pypi.python.org/packages/source/a/%{modname}/%{modname}-%{version}.tar.gz
Patch0:         python-anykeystore-use-unittest1.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest

# Optional backends for the tests
BuildRequires:  python3-sqlalchemy
BuildRequires:  python3-pymongo
BuildRequires:  python3-redis
#BuildRequires:  python3-memcached  # Not yet packaged..

%global _description\
A generic interface wrapping multiple different backends to provide a\
consistent key-value storage API. This library is intended to be used by\
other libraries that require some form of generic storage.

%description %_description

%package -n python3-%{modname}
Summary:        A key-value store supporting multiple backends

%description -n python3-%{modname}
A generic interface wrapping multiple different backends to provide a
consistent key-value storage API. This library is intended to be used by
other libraries that require some form of generic storage.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{modname}-%{version}
%patch -P0 -p1

# Use the standard library instead of a backport
sed -i -e 's/^import mock/from unittest import mock/' \
       -e 's/^from mock import /from unittest.mock import /' \
    %{modname}/tests/test_backends/*

rm -rf %{modname}/tests/integration/tests.py

%build
%py3_build

%install
%py3_install

%check
%pytest

%files -n python3-%{modname}
%doc README.rst LICENSE.txt
%{python3_sitelib}/%{modname}
%{python3_sitelib}/%{modname}-%{version}*

%changelog
%autochangelog
