# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 81a81ec695fb0c7901407defaa1d2f7973617154cf27ba74e3a7ab8e64436094
%global source1_hash 88d2b6ccf64d7cc524db18b124461e744cda67e86b7d677f8bdc83172dd4e73a
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global majorversion 18
%global obsoletes_version %( echo $(( %majorversion + 1 )) )

Summary: PostgreSQL client library
Name: libpq
Version: %{majorversion}.4
Release: 1%{?dist}

License: PostgreSQL
Url: http://www.postgresql.org/

Source0: https://ftp.postgresql.org/pub/source/v%{version}/postgresql-%{version}.tar.bz2
Source1: https://ftp.postgresql.org/pub/source/v%{version}/postgresql-%{version}.tar.bz2.sha256

Patch1: libpq-10.3-rpm-pgsql.patch
Patch2: libpq-10.3-var-run-socket.patch
Patch3: libpq-12.1-symbol-versioning.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: bison
BuildRequires: flex
BuildRequires: gawk
BuildRequires: zlib-devel
BuildRequires: openssl-devel
BuildRequires: krb5-devel
BuildRequires: openldap-devel
BuildRequires: gettext
%{!?rhel:BuildRequires: multilib-rpm-config}
BuildRequires: make
BuildRequires: libicu-devel
BuildRequires: perl

Obsoletes: postgresql-libs < %obsoletes_version
Provides: postgresql-libs = %version-%release

%description
The libpq package provides the essential shared library for any PostgreSQL
client program or interface.  You will need to install this package to use any
other PostgreSQL package or any clients that need to connect to a PostgreSQL
server.

%package devel
Summary: Development files for building PostgreSQL client tools
Requires: %name%{?_isa} = %version-%release
Provides: postgresql-devel = %version-%release
Obsoletes: postgresql-devel < %obsoletes_version

%description devel
The libpq package provides the essential shared library for any PostgreSQL
client program or interface.  You will need to install this package to build any
package or any clients that need to connect to a PostgreSQL server.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
( cd "$(dirname "%SOURCE1")" ; sha256sum -c "%SOURCE1" )
%autosetup -n postgresql-%{version} -p1

find . -type f -name .gitignore | xargs rm

%build
export SYMBOL_VERSION_PREFIX=RHPG_

export CFLAGS="$CFLAGS -DOPENSSL_NO_ENGINE -std=c17"
%configure \
    --disable-rpath \
    --with-ldap \
    --with-openssl \
    --with-gssapi \
    --enable-nls \
    --without-readline \
    --datadir=%_datadir/pgsql

%global build_subdirs \\\
        src/include \\\
        src/common \\\
        src/port \\\
        src/interfaces/libpq \\\
        src/bin/pg_config

for subdir in %build_subdirs; do
    %make_build -C "$subdir"
done

%install
for subdir in %build_subdirs; do
    %make_install -C "$subdir"
done

find $RPM_BUILD_ROOT -name '*.a' -delete
mv $RPM_BUILD_ROOT%{_includedir}/pgsql/server/utils/errcodes.h \
   $RPM_BUILD_ROOT%{_includedir}/pgsql
rm -r $RPM_BUILD_ROOT%_includedir/pgsql/server
mkdir -p $RPM_BUILD_ROOT%{_includedir}/pgsql/server/utils
mv $RPM_BUILD_ROOT%{_includedir}/pgsql/errcodes.h \
   $RPM_BUILD_ROOT%{_includedir}/pgsql/server/utils
rm $RPM_BUILD_ROOT%_datadir/pgsql/postgres.bki
rm $RPM_BUILD_ROOT%_datadir/pgsql/system_constraints.sql

%if %{undefined rhel}
%multilib_fix_c_header --file "%_includedir/pg_config.h"
%endif

find_lang_bins ()
{
    lstfile=$1 ; shift
    cp /dev/null "$lstfile"
    for binary; do
        %find_lang "$binary"-%majorversion
        cat "$binary"-%majorversion.lang >>"$lstfile"
    done
}

find_lang_bins %name.lst        libpq5
find_lang_bins %name-devel.lst  pg_config

%files -f %name.lst
%license COPYRIGHT
%_libdir/libpq.so.5*
%dir %_datadir/pgsql
%doc %_datadir/pgsql/pg_service.conf.sample

%files devel -f %name-devel.lst
%_bindir/pg_config
%_includedir/*
%_libdir/libpq.so
%_libdir/pkgconfig/libpq.pc

%changelog
%autochangelog
