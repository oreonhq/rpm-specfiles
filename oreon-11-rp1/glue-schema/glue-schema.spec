%global source0_hash 708d73e6e3ebd2f552c44f854845f71bc1bcc6d5f9b2023f0f98120bc33563b9

Name:		glue-schema
Version:	2.1.0
Release:	8%{?dist}
Summary:	LDAP schema files for the GLUE 1.3 and GLUE 2.0 Schema
License:	Apache-2.0
URL:		https://github.com/EGI-Foundation/%{name}
Source:		https://github.com/EGI-Foundation/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	make

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
# Nothing to build

%install
make install prefix=%{buildroot}

rm -rf %{buildroot}%{_docdir}
rm -rf %{buildroot}%{_licensedir}

%files
%dir %{_sysconfdir}/ldap
%dir %{_sysconfdir}/ldap/schema
%config(noreplace) %{_sysconfdir}/ldap/schema/*
%doc AUTHORS.md
%doc README.md
%license COPYRIGHT
%license LICENSE.txt

%changelog
%autochangelog
