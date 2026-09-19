%global source0_hash 628d365d687e12da12d02c6691170f4451db28d6d68d050007e4a40065868502

Name:           python3-openid
Version:        3.1.0
Release:        30%{?dist}
Summary:        Python 3 port of the python-openid library
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/necaris/python3-openid
Source0:        %{pypi_source}

# Python 3.9 compatibility
Patch1:         %{url}/pull/45.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-django
BuildRequires:  python3-psycopg2
BuildRequires:  python3-setuptools
BuildRequires:  python3-defusedxml

Requires:       python3-defusedxml

%description
This started out as a fork of the Python OpenID library,
with changes to make it Python 3 compatible.
It's now a port of that library,
including cleanups and updates to the code in general.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# replace env python shebangs with python3
grep -Erl '^#!/usr/bin/env python$' | xargs \
sed -i -r '1 s|^#!/usr/bin/env python$|#!%{__python3}|g'

%build
%py3_build

%install
%py3_install

# remove .po files
find %{buildroot} -name "*.po" | xargs rm -f

%check
%{python3} -m unittest openid.test.test_suite

%files
%doc LICENSE NEWS.md
%dir %{python3_sitelib}/openid
%{python3_sitelib}/openid/*.py
%dir %{python3_sitelib}/openid/__pycache__
%{python3_sitelib}/openid/__pycache__/*.pyc
%dir %{python3_sitelib}/openid/consumer
%{python3_sitelib}/openid/consumer/*.py
%dir %{python3_sitelib}/openid/consumer/__pycache__
%{python3_sitelib}/openid/consumer/__pycache__/*.pyc
%dir %{python3_sitelib}/openid/extensions
%{python3_sitelib}/openid/extensions/*.py
%dir %{python3_sitelib}/openid/extensions/__pycache__
%{python3_sitelib}/openid/extensions/__pycache__/*.pyc
%dir %{python3_sitelib}/openid/extensions/draft
%{python3_sitelib}/openid/extensions/draft/*.py
%dir %{python3_sitelib}/openid/extensions/draft/__pycache__
%{python3_sitelib}/openid/extensions/draft/__pycache__/*.pyc
%dir %{python3_sitelib}/openid/server
%{python3_sitelib}/openid/server/*.py
%dir %{python3_sitelib}/openid/server/__pycache__
%{python3_sitelib}/openid/server/__pycache__/*.pyc
%dir %{python3_sitelib}/openid/store
%{python3_sitelib}/openid/store/*.py
%dir %{python3_sitelib}/openid/store/__pycache__
%{python3_sitelib}/openid/store/__pycache__/*.pyc
%dir %{python3_sitelib}/openid/yadis
%{python3_sitelib}/openid/yadis/*.py
%dir %{python3_sitelib}/openid/yadis/__pycache__
%{python3_sitelib}/openid/yadis/__pycache__/*.pyc
%{python3_sitelib}/python3_openid-%{version}-py3.*.egg-info/

%changelog
%autochangelog
