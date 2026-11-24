# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 65a05310e3f16b930454aed7bed619edca8025ba96324c3e9b57dd508f1a014f
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global srcname oauth2client
%global sum Python client library for OAuth 2.0
%global _docdir_fmt %{name}

Name:           python-%{srcname}
Version:        4.1.3
Release:        1%{?dist}
Summary:        %{sum}

License:        Apache-2.0
URL:            https://github.com/google/%{srcname}
Source0:        https://github.com/google/%{srcname}/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
Patch0:         docs-build-fix.patch
Patch1:         doc-fix.patch
Patch2:         keyring-remove.patch

BuildArch:      noarch
BuildRequires: oreon-rpm-macros
BuildRequires:  python3-devel

BuildRequires:  python3-setuptools
BuildRequires:  python3-fasteners
BuildRequires:  python3-pyasn1 >= 0.1.7
BuildRequires:  python3-pyasn1-modules >= 0.0.5
BuildRequires:  python3-pytest

%description
This is a python client module for accessing resources protected by OAuth 2.0

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

Requires:       python3-pyOpenSSL
Requires:       python3-fasteners

%description -n python3-%{srcname}
This is a python client module for accessing resources protected by OAuth 2.0

%prep
%oreon_sha256
%setup -q -n %{srcname}-%{version}
%patch -P0 -p1 -b .doc
%patch -P1 -p1 -b .doc2
%patch -P2 -p1 -b .keyring

sed -i 's/httplib2>=0.9.1/httplib2/' setup.py

rm -f docs/source/oauth2client.contrib.appengine.rst oauth2client/appengine.py

rm oauth2client/contrib/keyring_storage.py tests/contrib/test_keyring_storage.py docs/source/oauth2client.contrib.keyring_storage.rst

find docs tests -type f \( -name '*.py' -o -name '*.py.doc' \) -exec \
    gawk '/^import mock$/ { print FILENAME; nextfile }' '{}' '+' |
  xargs -r -t sed -r -i 's/^import mock$/from unittest &/'
sed -r -i 's/\bmock.*//' tox.ini

%build
%py3_build

%install
%py3_install

%check

rm -r $(find %{_buildrootdir} -type d -name 'tests') || /bin/true

%files -n python3-%{srcname}
%license LICENSE 
%doc CHANGELOG.md CONTRIBUTING.md README.md 
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}*.egg-info

%changelog
%autochangelog
