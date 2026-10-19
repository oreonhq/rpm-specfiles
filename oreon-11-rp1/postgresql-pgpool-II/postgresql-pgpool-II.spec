%global source0_hash 9ee55642dd4450191a6452a0aa6de6d1c5f717ac64cbca0b9367b7c5808ae142
%global _build_id_links none
%global sname	pgpool-II
%global _varrundir %{_rundir}/pgpool
Summary:        Pgpool is a connection pooling/replication server for PostgreSQL
Name:			postgresql-%{sname}
Version:		4.7.1
Release:        1%{?dist}
License:		LicenseRef-Callaway-BSD
URL:			https://pgpool.net
Source0:        https://www.pgpool.net/mediawiki/images/%{sname}-%{version}.tar.gz
Source1:		pgpool.service
Source2:		pgpool.sysconfig
Source6:		%{sname}-sysusers.conf
Source7:		%{sname}-tmpfiles.d
Requires:		systemd
Requires(post):		systemd-sysv
Requires(post):		systemd
Requires(preun):	systemd
Requires(postun):	systemd
# oreon:deps
BuildRequires:  clang-devel
BuildRequires:  gcc
BuildRequires:  libmemcached-awesome-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  llvm-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  postgresql-server-devel
BuildRequires:  systemd
# /oreon:deps
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
ExcludeArch: %{ix86}
%description devel
Development headers and libraries for pgpool-II.

%package extensions
Summary:	Postgresql extensions for pgpool-II
Obsoletes:	postgresql-pgpool-II-recovery <= 3.3.4-1
Provides:	postgresql-pgpool-II-recovery = %{version}-%{release}
Requires:	postgresql-server
Requires:	%{name}%{?_isa} = %{version}-%{release}
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
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
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
%{__rm} -f %{buildroot}%{_libdir}/libpgpoolpcp.{a,la}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

/sbin/ldconfig
%systemd_post pgpool.service
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
%preun

%systemd_preun pgpool.service
%postun

/sbin/ldconfig
%systemd_postun_with_restart pgpool.service
%files -f %{oreon_filedir}/main.list
%files -n postgresql-pgpool-II-devel -f %{oreon_filedir}/postgresql-pgpool-II-devel.list
%files -n postgresql-pgpool-II-extensions -f %{oreon_filedir}/postgresql-pgpool-II-extensions.list

%changelog

%autochangelog
