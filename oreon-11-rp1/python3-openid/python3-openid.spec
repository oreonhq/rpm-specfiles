%global source0_hash 628d365d687e12da12d02c6691170f4451db28d6d68d050007e4a40065868502
Name:           python3-openid
Version:        3.1.0
Release:        30%{?dist}
Summary:        Python 3 port of the python-openid library
License:        Apache-2.0
URL:            https://github.com/necaris/python3-openid
Source0:        https://files.pythonhosted.org/packages/source/p/python3-openid/python3-openid-%{version}.tar.gz
Patch1:         %{url}/pull/45.patch
BuildArch:      noarch
Requires:       python3-defusedxml
# oreon:deps
BuildRequires:  python3-defusedxml
BuildRequires:  python3-devel
BuildRequires:  python3-django
BuildRequires:  python3-psycopg2
BuildRequires:  python3-setuptools
# /oreon:deps
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
find %{buildroot} -name "*.po" | xargs rm -f
%oreon_autofiles main

%check

%{python3} -m unittest openid.test.test_suite
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
