%global source0_hash 18dc7460470c6ff64ed5c04ee21c56dbfee7ab433a53213ba91e407eea44c34c
%bcond servers %{undefined rhel}
%global openldap_version 2.4.45-4
Name: python-ldap
Version: 3.4.8
Release:        1%{?dist}
License: python-ldap
Summary:        An object-oriented API to access LDAP directory servers
URL: https://python-ldap.org/
Source0:        https://files.pythonhosted.org/packages/source/p/python_ldap/python_ldap-3.4.8.tar.gz
Patch101: 0101-Disable-openldap-servers-tests.patch
%if %{with servers}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61
Requires:       python3-ldap = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-ldap
Summary:        An object-oriented API to access LDAP directory servers
Requires:  openldap >= %{openldap_version}
Obsoletes: python3-pyldap < 3
Provides:  python3-pyldap = %{version}-%{release}
Provides:  python3-pyldap%{?_isa} = %{version}-%{release}
# oreon:reqs
Requires:       python3dist(pyasn1) >= 0.3.7
Requires:       python3dist(pyasn1-modules) >= 0.1.5
# /oreon:reqs
%description -n python3-ldap

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n python_ldap-%{version}%{?prerelease} -N
%autopatch -p1 -M100
%if %{without servers}
%autopatch -p1 101
%endif

# Fix interpreter
find . -name '*.py' | xargs sed -i '1s|^#!/usr/bin/env python|#!%{__python3}|'

%build

%pyproject_wheel
%check

PYTHONPATH=%{buildroot}%{python3_sitearch} %{__python3} -m unittest discover -v -s Tests -p 't_*'
%install
%pyproject_install
%oreon_autofiles python3-ldap usr/lib/python3*/site-packages/ldap* usr/lib64/python3*/site-packages/ldap* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ldap* usr/lib64/python3*/site-packages/ldap* usr/bin/*

%files
%files -n python3-ldap -f %{oreon_filedir}/python3-ldap.list

%changelog

%autochangelog
