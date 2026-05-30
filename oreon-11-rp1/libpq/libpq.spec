%global source0_hash none

%global majorversion 18
%global obsoletes_version %( echo $(( %majorversion + 1 )) )
%global betaversion 18beta1

Summary: PostgreSQL client library
Name: libpq
Version: %{majorversion}.0
Release: 4%{?dist}

License: PostgreSQL
Url: http://www.postgresql.org/

# Use this when 18.0 is released
# Source0: https://ftp.postgresql.org/pub/source/v%%{version}/postgresql-%%{version}.tar.bz2
# Source1: https://ftp.postgresql.org/pub/source/v%%{version}/postgresql-%%{version}.tar.bz2.sha256

Source0:        https://ftp.postgresql.org/pub/source/v18beta1/postgresql-18beta1.tar.bz2
Source1:        https://ftp.postgresql.org/pub/source/v18beta1/postgresql-18beta1.tar.bz2.sha256


# Comments for these patches are in the patch files.
Patch1: libpq-10.3-rpm-pgsql.patch
Patch2: libpq-10.3-var-run-socket.patch
Patch3: libpq-12.1-symbol-versioning.patch

BuildRequires: gcc
BuildRequires: glibc-devel bison flex gawk
BuildRequires: zlib-devel
BuildRequires: openssl-devel
BuildRequires: krb5-devel
BuildRequires: openldap-devel
BuildRequires: gettext
BuildRequires: multilib-rpm-config
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
# Historically we had 'postgresql-devel' package which was used for building
# both PG clients and PG server modules;  let's have this fake provide to cover
# most of the depending packages and the rest (those which want to build server
# modules) need to be fixed to require postgresql-server-devel package.
Provides: postgresql-devel = %version-%release
Obsoletes: postgresql-devel < %obsoletes_version

%description devel
The libpq package provides the essential shared library for any PostgreSQL
client program or interface.  You will need to install this package to build any
package or any clients that need to connect to a PostgreSQL server.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
( cd "$(dirname "%SOURCE1")" ; sha256sum -c "%SOURCE1" )
%autosetup -n postgresql-%{betaversion} -p1

# remove .gitignore files to ensure none get into the RPMs (bug #642210)
find . -type f -name .gitignore | xargs rm


%build
# complements symbol-versioning patch
export SYMBOL_VERSION_PREFIX=RHPG_

export CFLAGS="$CFLAGS -DOPENSSL_NO_ENGINE -std=c17"
# We don't build server nor client (e.g. /bin/psql) binaries in this package, so
# we can disable some configure options.
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

# remove files not to be packaged
find $RPM_BUILD_ROOT -name '*.a' -delete
# preserve just errcodes.h
mv $RPM_BUILD_ROOT%{_includedir}/pgsql/server/utils/errcodes.h \
   $RPM_BUILD_ROOT%{_includedir}/pgsql
rm -r $RPM_BUILD_ROOT%_includedir/pgsql/server
mkdir -p $RPM_BUILD_ROOT%{_includedir}/pgsql/server/utils
mv $RPM_BUILD_ROOT%{_includedir}/pgsql/errcodes.h \
   $RPM_BUILD_ROOT%{_includedir}/pgsql/server/utils
rm $RPM_BUILD_ROOT%_datadir/pgsql/postgres.bki
rm $RPM_BUILD_ROOT%_datadir/pgsql/system_constraints.sql

%multilib_fix_c_header --file "%_includedir/pg_config.h"

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
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 18.0-4
- Import
