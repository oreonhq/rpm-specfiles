# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 b2f6ef1c37fe2c6a5a85212efe71311ee21847766a7d45fcb711f3b270a5f79a
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

### Abstract ###
%bcond servers %{undefined rhel}

# global prerelease b4

%global openldap_version 2.4.45-4

Name: python-ldap
Version: 3.4.5
Release: %autorelease
License: python-ldap
Summary: An object-oriented API to access LDAP directory servers
URL: https://python-ldap.org/
Source0:        https://files.pythonhosted.org/packages/source/p/python_ldap/python_ldap-3.4.5.tar.gz

# Conditionally applied paches, numbereed > 100
Patch101: 0101-Disable-openldap-servers-tests.patch

### Build Dependencies ###
BuildRequires: gcc
BuildRequires: openldap-devel >= %{openldap_version}
BuildRequires: openssl-devel
BuildRequires: cyrus-sasl-devel
BuildRequires: python3-devel
# Test dependencies
%if %{with servers}
BuildRequires: openldap-servers >= %{openldap_version}
%endif
BuildRequires: openldap-clients >= %{openldap_version}

%global _description\
python-ldap provides an object-oriented API for working with LDAP within\
Python programs.  It allows access to LDAP directory servers by wrapping the\
OpenLDAP 2.x libraries, and contains modules for other LDAP-related tasks\
(including processing LDIF, LDAPURLs, LDAPv3 schema, etc.).

%description %_description


%package -n     python3-ldap
Summary:        %{summary}

Requires:  openldap >= %{openldap_version}
Obsoletes: python3-pyldap < 3
Provides:  python3-pyldap = %{version}-%{release}
Provides:  python3-pyldap%{?_isa} = %{version}-%{release}

%description -n python3-ldap %_description


%prep
%oreon_verify_sources
%autosetup -p1 -n python_ldap-%{version}%{?prerelease} -N
%autopatch -p1 -M100
%if %{without servers}
%autopatch -p1 101
%endif

# Fix interpreter
find . -name '*.py' | xargs sed -i '1s|^#!/usr/bin/env python|#!%{__python3}|'


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%check
PYTHONPATH=%{buildroot}%{python3_sitearch} %{__python3} -m unittest discover -v -s Tests -p 't_*'


%install
%pyproject_install
%pyproject_save_files -l ldap slapdtest ldapurl ldif _ldap

%files -n python3-ldap -f %{pyproject_files}
%doc CHANGES README TODO Demo

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.4.5-1
- Prepare for Oreon 11 (RP1)
