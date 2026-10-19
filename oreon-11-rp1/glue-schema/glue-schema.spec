%global source0_hash 0ca06c1a6ab847253a802ac692e745aa22fffbcfbb6c06ce888991bc931eb156
Name:		glue-schema
Version:	2.1.1
Release:        1%{?dist}
Summary:        LDAP schema files for the GLUE 1.3 and GLUE 2.0 Schema
License:	Apache-2.0
URL:		https://github.com/EGI-Foundation/%{name}
Source0:        https://github.com/EGI-Foundation/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch
# oreon:deps
BuildRequires:  make
# /oreon:deps
%description
The GLUE specification is an information model for Grid entities such
as computing clusters and data storage facilities. As a conceptual
model, it is designed to be independent from the concrete data models
adopted for its implementation. The specification can be rendered to
several concrete data models such as XML Schema, LDAP Schema or SQL.

This package provides LDAP schema files for the GLUE 1.3 and GLUE 2.0 Schema.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build 

%install
make install prefix=%{buildroot}
rm -rf %{buildroot}%{_docdir}
rm -rf %{buildroot}%{_licensedir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
