%global source0_hash 65a05310e3f16b930454aed7bed619edca8025ba96324c3e9b57dd508f1a014f
%global srcname oauth2client
%global sum Python client library for OAuth 2.0
%global _docdir_fmt %{name}
Name:           python-%{srcname}
Version:        4.1.3
Release:        33%{?dist}
Summary:        Python client library for OAuth 2.0
License:        Apache-2.0
URL:            https://github.com/google/%{srcname}
Source0:        https://github.com/google/%{srcname}/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
Patch0:         docs-build-fix.patch
Patch1:         doc-fix.patch
Patch2:         keyring-remove.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-fasteners
BuildRequires:  python3-pyasn1
BuildRequires:  python3-pyasn1-modules
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{srcname}-%{version}
%patch -P0 -p1 -b .doc
%patch -P1 -p1 -b .doc2
%patch -P2 -p1 -b .keyring

# Remove the version constraint on httplib2.  From reading upstream's git log,
# it seems the only reason they require a new version is to force python3
# support.  That doesn't affect us on EPEL7, so we can loosen the constraint.
sed -i 's/httplib2>=0.9.1/httplib2/' setup.py

# We do not have the package for google.appengine support
# This is removed because it breaks the docs build otherwise
rm -f docs/source/oauth2client.contrib.appengine.rst oauth2client/appengine.py

# Remove keyring support
rm oauth2client/contrib/keyring_storage.py tests/contrib/test_keyring_storage.py docs/source/oauth2client.contrib.keyring_storage.rst

# Remove deprecated PyPI mock dependency, replacing it with unittest.mock.  See
# https://fedoraproject.org/wiki/Changes/DeprecatePythonMock.  Since
# oauth2client is deprecated/archived upstream, this patch must be
# downstream-only. The find-then-modify pattern keeps us from discarding mtimes
# on any sources that do not need modification.
find docs tests -type f \( -name '*.py' -o -name '*.py.doc' \) -exec \
    gawk '/^import mock$/ { print FILENAME; nextfile }' '{}' '+' |
  xargs -r -t sed -r -i 's/^import mock$/from unittest &/'
sed -r -i 's/\bmock.*//' tox.ini

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

rm -r $(find %{_buildrootdir} -type d -name 'tests') || /bin/true
%files -f %{oreon_filedir}/main.list
%files -n python3-oauth2client -f %{oreon_filedir}/python3-oauth2client.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.1.3-33
- Prepare for Oreon 11 (RP1)
