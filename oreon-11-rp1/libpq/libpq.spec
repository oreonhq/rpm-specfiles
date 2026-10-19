%global source1_hash 92b190ded4a002654768daa8ac41db530354b9be13c7c67059592ddf5bb0c43a
%global source0_hash 555610c24d53e4316da5b7d3fc25c279d96856d5e0e23ee308c328c5fa881d9f
%global majorversion 18
%global obsoletes_version %( echo $(( %majorversion + 1 )) )
%global betaversion %{version}
Summary:        PostgreSQL client library
Name: libpq
Version: %{majorversion}.6
Release:        1%{?dist}
License: PostgreSQL
Url: http://www.postgresql.org/
Source0:        https://ftp.postgresql.org/pub/source/v%{version}/postgresql-%{version}.tar.bz2
Source1:        https://ftp.postgresql.org/pub/source/v%{betaversion}/postgresql-%{betaversion}.tar.bz2.sha256
Patch1: libpq-10.3-rpm-pgsql.patch
Patch2: libpq-10.3-var-run-socket.patch
Patch3: libpq-12.1-symbol-versioning.patch
Obsoletes: postgresql-libs < %obsoletes_version
Provides: postgresql-libs = %version-%release
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glibc-devel
BuildRequires:  krb5-devel
BuildRequires:  libicu-devel
BuildRequires:  make
BuildRequires:  multilib-rpm-config
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  perl
BuildRequires:  zlib-devel
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
( cd "$(dirname "%SOURCE1")" ; sha256sum -c "%SOURCE1" )
%autosetup -n postgresql-%{betaversion} -p1

# remove .gitignore files to ensure none get into the RPMs (bug #642210)
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libpq-devel -f %{oreon_filedir}/libpq-devel.list

%changelog

%autochangelog
