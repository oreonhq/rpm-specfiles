%global source0_hash 679d719b2c6ea7c6119c937bdffa72aad54e8e9e9f489c1746e21de5486bdeed

%global githubversion 4_9_0

Name:		orafce
Version:	4.9.0
Release:	4%{?dist}
Summary:	Implementation of some Oracle functions into PostgreSQL
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		http://github.com/orafce/orafce
Source0:	https://github.com/orafce/orafce/archive/VERSION_%{githubversion}.tar.gz

Requires(pre): postgresql-server

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	clang-devel llvm-devel
BuildRequires:	postgresql-server-devel openssl-devel krb5-devel bison flex

%description
The goal of this project is implementation some functions from Oracle database.
Some date functions (next_day, last_day, trunc, round, ...) are implemented
now. Functionality was verified on Oracle 10g and module is useful
for production work.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-VERSION_%{githubversion}

%build
%make_build USE_PGXS=1 PG_CONFIG=/usr/bin/pg_server_config

%install
%make_install USE_PGXS=1 PG_CONFIG=/usr/bin/pg_server_config

%files
%license COPYRIGHT.orafce
%doc INSTALL.orafce README.asciidoc
%{_libdir}/pgsql/
%{_datadir}/pgsql/
%exclude %{_docdir}/pgsql/

%changelog
%autochangelog
