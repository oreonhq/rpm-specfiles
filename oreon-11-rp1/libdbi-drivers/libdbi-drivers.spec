%global source0_hash 43d2eacd573a4faff296fa925dd97fbf2aedbf1ae35c6263478210c61004c854

Summary: Database-specific drivers for libdbi
Name: libdbi-drivers
Version: 0.9.0
Release: 33%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL: http://libdbi-drivers.sourceforge.net/

Source: http://prdownloads.sourceforge.net/libdbi-drivers/%{name}-%{version}.tar.gz
# old automake does not offer aarch64
Patch1: libdbi-drivers-aarch64.patch
Patch2: libdbi-drivers-sys-wait.patch
Patch3: libdbi-drivers-0.9.0-buffer_overflow.patch
Patch4: libdbi-drivers-c99.patch

Requires: libdbi%{?_isa} >= 0.9
BuildRequires: libdbi-devel >= 0.9
BuildRequires: autoconf openjade docbook-style-dsssl
BuildRequires: gcc

%description
libdbi implements a database-independent abstraction layer in C, similar to the
DBI/DBD layer in Perl. Writing one generic set of code, programmers can
leverage the power of multiple databases and multiple simultaneous database
connections by using this framework.

libdbi-drivers contains the database-specific plugins needed to connect
libdbi to particular database servers.

%package -n libdbi-dbd-mysql
Summary: MySQL plugin for libdbi
Requires:	%{name}%{?_isa} = %{version}-%{release}
BuildRequires: mariadb-connector-c-devel, openssl-devel

%description -n libdbi-dbd-mysql
This plugin provides connectivity to MySQL/MariaDB database servers through
the libdbi database independent abstraction layer. Switching a program's
plugin does not require recompilation or rewriting source code.

%package -n libdbi-dbd-pgsql
Summary: PostgreSQL plugin for libdbi
Requires:	%{name}%{?_isa} = %{version}-%{release}
BuildRequires: libpq-devel, krb5-devel, openssl-devel

%description -n libdbi-dbd-pgsql
This plugin provides connectivity to PostgreSQL database servers through the
libdbi database independent abstraction layer. Switching a program's plugin
does not require recompilation or rewriting source code.

%package -n libdbi-dbd-sqlite
Summary: SQLite plugin for libdbi
Requires:	%{name}%{?_isa} = %{version}-%{release}
BuildRequires: sqlite-devel
BuildRequires: make

%description -n libdbi-dbd-sqlite
This plugin provides access to an embedded SQL engine using libsqlite3 through
the libdbi database independent abstraction layer. Switching a program's plugin
does not require recompilation or rewriting source code.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
autoconf
# mariadb provides headers in a subfolder <mysql/mysql.h>
sed -i -r 's|<(mysql\.h)>|<mysql/\1>|' drivers/mysql/dbd_mysql.c
# exporting LDFLAGS or LIBS or SQLITE3_LIBS before running autoconf or
#   ./configure doesn't help => hardcode it
sed -i -r "s|(SQLITE3_LIBS=)-lsqlite[^[:space:]]*|\1$(pkg-config --libs-only-l sqlite3)|" \
  configure

%build
# configure is broken, must pass both --with-*sql-libdir _AND_
# --with-*sql-incdir in order for --with-*sql-libdir to be used
%configure --with-mysql --with-pgsql --with-sqlite3 \
	--with-mysql-libdir=%{_libdir}/mariadb \
	--with-mysql-incdir=%{_includedir} \
	--with-pgsql-libdir=%{_libdir} \
	--with-pgsql-incdir=%{_includedir} \
	--with-sqlite3-libdir=%{_libdir} \
	--with-sqlite3-incdir=%{_includedir} \
	--with-dbi-libdir=%{_libdir}

make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

rm -f ${RPM_BUILD_ROOT}%{_libdir}/dbd/*.a
rm -f ${RPM_BUILD_ROOT}%{_libdir}/dbd/*.la

# package the docs via %%doc directives
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog COPYING README
%doc drivers/mysql/dbd_mysql/*.html
%doc drivers/mysql/*.pdf
%doc drivers/pgsql/dbd_pgsql/*.html
%doc drivers/pgsql/*.pdf
%doc drivers/sqlite3/dbd_sqlite3/*.html
%doc drivers/sqlite3/*.pdf
%dir %{_libdir}/dbd

%files -n libdbi-dbd-mysql
%{_libdir}/dbd/libdbdmysql.*

%files -n libdbi-dbd-pgsql
%{_libdir}/dbd/libdbdpgsql.*

%files -n libdbi-dbd-sqlite
%{_libdir}/dbd/libdbdsqlite3.*

%changelog
%autochangelog
