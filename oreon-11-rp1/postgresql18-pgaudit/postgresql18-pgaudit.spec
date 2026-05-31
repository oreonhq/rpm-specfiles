%global source0_hash 06eb41c0aa648266b661dea08c430977b1a50546b424bb223dda48bb76bf5708

%{!?postgresql_default:%global postgresql_default 1}

%global majorname pgaudit
%global pgversion 18
Name:		postgresql%{pgversion}-%{majorname}
Version:	18.0
Release:	2%{?dist}
Summary:	PostgreSQL Audit Extension

License:	PostgreSQL
URL:		http://pgaudit.org

# Temporary source until postgresql18 support is released
Source0:        https://github.com/pgaudit/pgaudit/archive/refs/heads/main.tar.gz
# ExecutorStart_hook_type type was changed from void to bool in pg17

%if %?postgresql_default
%global pkgname %{majorname}
%package -n %{pkgname}
Summary: PostgreSQL Audit Extension
%else
%global pkgname %name
%endif

BuildRequires: make
BuildRequires:	gcc
BuildRequires:	postgresql-server-devel
BuildRequires:	openssl-devel

Requires(pre): postgresql-server

%global precise_version %{?epoch:%epoch:}%version-%release
Provides: %{pkgname} = %precise_version
%if %?postgresql_default
Provides: %name = %precise_version
Provides: postgresql-%{majorname} = %precise_version
%endif
Provides: %{pkgname}%{?_isa} = %precise_version
Provides: %{majorname}-any
Conflicts: %{majorname}-any

%description
The PostgreSQL Audit extension (pgaudit) provides detailed session
and/or object audit logging via the standard PostgreSQL logging
facility.

The goal of the PostgreSQL Audit extension (pgaudit) is to provide
PostgreSQL users with capability to produce audit logs often required to
comply with government, financial, or ISO certifications.

An audit is an official inspection of an individual's or organization's
accounts, typically by an independent body. The information gathered by
the PostgreSQL Audit extension (pgaudit) is properly called an audit
trail or audit log. The term audit log is used in this documentation.

%description -n %{pkgname}
The PostgreSQL Audit extension (pgaudit) provides detailed session
and/or object audit logging via the standard PostgreSQL logging
facility.

The goal of the PostgreSQL Audit extension (pgaudit) is to provide
PostgreSQL users with capability to produce audit logs often required to
comply with government, financial, or ISO certifications.

An audit is an official inspection of an individual's or organization's
accounts, typically by an independent body. The information gathered by
the PostgreSQL Audit extension (pgaudit) is properly called an audit
trail or audit log. The term audit log is used in this documentation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{majorname}-main


%build
%make_build USE_PGXS=1 PG_CONFIG=/usr/bin/pg_server_config


%install
%make_install USE_PGXS=1 PG_CONFIG=/usr/bin/pg_server_config


%files -n %{pkgname}
%doc README.md
%license LICENSE
%{_libdir}/pgsql/%{majorname}.so
%if 0%{?postgresql_server_llvmjit}
%{_libdir}/pgsql/bitcode/%{majorname}.index.bc
%{_libdir}/pgsql/bitcode/%{majorname}/%{majorname}.bc
%endif
%{_datadir}/pgsql/extension/%{majorname}--1*.sql
%{_datadir}/pgsql/extension/%{majorname}.control


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 18.0-2
- Prepare for Oreon 11 (RP1)
