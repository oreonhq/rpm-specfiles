%global source0_hash 9ee55642dd4450191a6452a0aa6de6d1c5f717ac64cbca0b9367b7c5808ae142

%global _build_id_links none
%global sname	pgpool-II
%global _varrundir %{_rundir}/pgpool

Summary:		Pgpool is a connection pooling/replication server for PostgreSQL
Name:			postgresql-%{sname}
Version:		4.7.1
Release:		1%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:		LicenseRef-Callaway-BSD

URL:			https://pgpool.net
Source0:		https://www.pgpool.net/mediawiki/images/%{sname}-%{version}.tar.gz
Source1:		pgpool.service
Source2:		pgpool.sysconfig
Source6:		%{sname}-sysusers.conf
Source7:		%{sname}-tmpfiles.d

BuildRequires:		make
BuildRequires:		gcc
BuildRequires:		clang-devel llvm-devel
BuildRequires:		postgresql-server-devel
BuildRequires:		pam-devel libmemcached-awesome-devel openssl-devel
BuildRequires:		libxcrypt-devel

BuildRequires:		systemd

# We require this to be present for %%{_prefix}/lib/tmpfiles.d
Requires:		systemd
Requires(post):		systemd-sysv
Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd

%description
Pgpool-II is a middleware that works between PostgreSQL servers and a
PostgreSQL database client. It provides the following features:
 * Connection Pooling
 * Replication
 * Load Balancing
 * Limiting Exceeding Connections
 * Watchdog
 * In Memory Query Cache

%package devel
Summary:	The development files for pgpool-II
Requires:	%{name}%{?_isa} = %{version}-%{release}

# Stop building i686 architecture
ExcludeArch: %{ix86}

%description devel
Development headers and libraries for pgpool-II.

%package extensions
Summary:	Postgresql extensions for pgpool-II
Obsoletes:	postgresql-pgpool-II-recovery <= 3.3.4-1
Provides:	postgresql-pgpool-II-recovery = %{version}-%{release}
Requires:	postgresql-server
Requires:	%{name}%{?_isa} = %{version}-%{release}

# Stop building i686 architecture
ExcludeArch: %{ix86}

%description extensions
Postgresql extensions libraries and sql files for pgpool-II.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{sname}-%{version}

%build
%configure \
	--with-pgsql-includedir=%{_includedir}/pgsql \
	--with-pgsql=%{_libdir}/pgsql \
	--disable-static \
	--with-pam \
	--with-openssl \
	--with-memcached=%{_includedir}/libmemcached \
	--sysconfdir=%{_sysconfdir}/%{sname}/

# https://fedoraproject.org/wiki/Packaging:Guidelines#Removing_Rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# GCC 10 defaults to -fno-common which
# https://gcc.gnu.org/gcc-10/changes.html (see C section)
%make_build CFLAGS="%{optflags} -fcommon"
%make_build CFLAGS="%{optflags} -fcommon" -C src/sql/pgpool-recovery
%make_build CFLAGS="%{optflags} -fcommon" -C src/sql/pgpool-regclass

%install
%make_install
%make_install -C src/sql/pgpool-recovery
%make_install -C src/sql/pgpool-regclass

%{__install} -d %{buildroot}%{_datadir}/%{sname}
%{__install} -d %{buildroot}%{_sysconfdir}/%{sname}
%{__mv} %{buildroot}/%{_sysconfdir}/%{sname}/pcp.conf.sample %{buildroot}%{_sysconfdir}/%{sname}/pcp.conf
%{__mv} %{buildroot}/%{_sysconfdir}/%{sname}/pgpool.conf.sample %{buildroot}%{_sysconfdir}/%{sname}/pgpool.conf
%{__mv} %{buildroot}/%{_sysconfdir}/%{sname}/pool_hba.conf.sample %{buildroot}%{_sysconfdir}/%{sname}/pool_hba.conf
%{__mv} %{buildroot}/%{_sysconfdir}/%{sname}/failover.sh.sample %{buildroot}%{_sysconfdir}/%{sname}/failover.sh
%{__mv} %{buildroot}/%{_sysconfdir}/%{sname}/pgpool_remote_start.sample %{buildroot}%{_sysconfdir}/%{sname}/pgpool_remote_start
%{__mv} %{buildroot}/%{_sysconfdir}/%{sname}/recovery_1st_stage.sample %{buildroot}%{_sysconfdir}/%{sname}/recovery_1st_stage

%{__install} -d %{buildroot}%{_unitdir}
%{__install} -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/pgpool.service

%{__install} -m 0644 -D %{SOURCE6} %{buildroot}%{_sysusersdir}/%{sname}.conf

%{__mkdir} -p %{buildroot}/%{_tmpfilesdir}
%{__install} -m 0644 %{SOURCE7} %{buildroot}/%{_tmpfilesdir}/%{name}.conf

%{__install} -d %{buildroot}%{_sysconfdir}/sysconfig
%{__install} -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/pgpool

# nuke libtool archive and static lib
%{__rm} -f %{buildroot}%{_libdir}/libpgpoolpcp.{a,la}

%post
/sbin/ldconfig
%systemd_post pgpool.service
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf

%preun
%systemd_preun pgpool.service

%postun
/sbin/ldconfig
%systemd_postun_with_restart pgpool.service

%files
%doc README TODO COPYING AUTHORS ChangeLog NEWS
%{_bindir}/pg_enc
%{_bindir}/pgpool
%{_bindir}/pgpool_setup
%{_bindir}/pgproto
%{_bindir}/watchdog_setup
%{_bindir}/pcp_attach_node
%{_bindir}/pcp_detach_node
%{_bindir}/pcp_invalidate_query_cache
%{_bindir}/pcp_log_rotate
%{_bindir}/pcp_node_count
%{_bindir}/pcp_node_info
%{_bindir}/pcp_pool_status
%{_bindir}/pcp_proc_count
%{_bindir}/pcp_proc_info
%{_bindir}/pcp_promote_node
%{_bindir}/pcp_recovery_node
%{_bindir}/pcp_stop_pgpool
%{_bindir}/pcp_watchdog_info
%{_bindir}/pcp_health_check_stats
%{_bindir}/pcp_reload_config
%{_bindir}/wd_cli
%{_bindir}/pg_md5
%dir %{_datadir}/%{sname}
%{_datadir}/%{sname}/insert_lock.sql
%{_libdir}/libpgpoolpcp.so.*
%{_datadir}/%{sname}/pgpool.pam
%{_sysusersdir}/%{sname}.conf
%ghost %{_varrundir}
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/pgpool.service
%dir %{_sysconfdir}/%{sname}
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/%{sname}/*
%config(noreplace) %{_sysconfdir}/sysconfig/pgpool

%files devel
%{_includedir}/libpcp_ext.h
%{_includedir}/pcp.h
%{_includedir}/pool_process_reporting.h
%{_includedir}/pool_type.h
%{_libdir}/libpgpoolpcp.so

%files extensions
%{_libdir}/pgsql/pgpool-recovery.so
%{_datadir}/pgsql/extension/pgpool-recovery.sql
%{_datadir}/pgsql/extension/pgpool_recovery--1.1.sql
%{_datadir}/pgsql/extension/pgpool_recovery--1.2.sql
%{_datadir}/pgsql/extension/pgpool_recovery--1.3.sql
%{_datadir}/pgsql/extension/pgpool_recovery--1.4.sql
%{_datadir}/pgsql/extension/pgpool_recovery--1.1--1.2.sql
%{_datadir}/pgsql/extension/pgpool_recovery--1.2--1.3.sql
%{_datadir}/pgsql/extension/pgpool_recovery--1.3--1.4.sql
%{_datadir}/pgsql/extension/pgpool_recovery.control
%{_datadir}/pgsql/extension/pgpool-regclass.sql
%{_datadir}/pgsql/extension/pgpool_regclass--1.0.sql
%{_datadir}/pgsql/extension/pgpool_regclass.control
# From PostgreSQL 9.4 pgpool-regclass.so is not needed anymore
# because 9.4 or later has to_regclass.
%{_libdir}/pgsql/pgpool-regclass.so

%changelog
%autochangelog
