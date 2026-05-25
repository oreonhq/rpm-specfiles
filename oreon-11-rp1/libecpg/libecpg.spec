%global majorversion 16

Summary: ECPG - Embedded SQL in C
Name: libecpg
Version: %majorversion.4
Release: 4%{?dist}

License: PostgreSQL
Url: http://www.postgresql.org/

Source0: https://ftp.postgresql.org/pub/source/v%version/postgresql-%version.tar.bz2
Source1: https://ftp.postgresql.org/pub/source/v%version/postgresql-%version.tar.bz2.sha256


# Comments for these patches are in the patch files.
Patch1: libecpg-10.5-rpm-pgsql.patch
Patch2: libecpg-10.5-var-run-socket.patch
Patch3: libecpg-12.2-external-libpq.patch
Patch4: libecpg-10.5-no-compat-lib.patch
Patch5: libecpg-12.2-dependency-build.patch

BuildRequires: gcc
BuildRequires: glibc-devel bison flex gawk
BuildRequires: zlib-devel
BuildRequires: openssl-devel
BuildRequires: krb5-devel
BuildRequires: openldap-devel
BuildRequires: libpq-devel
BuildRequires: gettext
BuildRequires: multilib-rpm-config
BuildRequires: make
BuildRequires: libicu-devel

Requires: libpgtypes = %{version}-%{release}

%description
An embedded SQL program consists of code written in an ordinary programming
language, in this case C, mixed with SQL commands in specially marked sections.
To build the program, the source code (*.pgc) is first passed through the
embedded SQL preprocessor, which converts it to an ordinary C program (*.c), and
afterwards it can be processed by a C compiler.


%package devel
Summary: Development files for ECPG - Embedded SQL in C
Requires: %name%{?_isa} = %version-%release
Requires: libpgtypes%{?_isa} = %version-%release

%description devel
ECPG development files.  You will need to install this package to build any
package or any clients that use the ECPG to connect to a PostgreSQL server.


%package -n libpgtypes
Summary: Map PostgreSQL database types to C equivalents


%description -n libpgtypes
The pgtypes library maps PostgreSQL database types to C equivalents that can be
used in C programs. It also offers functions to do basic calculations with those
types within C, i.e., without the help of the PostgreSQL server.


%prep
( cd "$(dirname "%SOURCE1")" ; sha256sum -c "%SOURCE1" )
%autosetup -n postgresql-%version -p1

# remove .gitignore files to ensure none get into the RPMs (bug #642210)
find . -type f -name .gitignore | xargs rm


%build
export CFLAGS="$CFLAGS -std=c17"
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

%make_build -C "src/interfaces/ecpg" -j1


%install
%make_install -C "src/interfaces/ecpg"

# remove files not to be packaged
find $RPM_BUILD_ROOT -name '*.a' -delete

%multilib_fix_c_header --file "%{_includedir}/ecpg_config.h"

# function from postgresql.spec
find_lang_bins ()
{
    lstfile=$1 ; shift
    cp /dev/null "$lstfile"
    for binary; do
        %find_lang "$binary"-%majorversion
        cat "$binary"-%majorversion.lang >>"$lstfile"
    done
}

find_lang_bins %name.lst        ecpglib6
find_lang_bins %name-devel.lst  ecpg


%files -f %name.lst
%license COPYRIGHT
%_libdir/libecpg.so.6*


%files -n libpgtypes
%license COPYRIGHT
%_libdir/libpgtypes.so.3*


%files devel -f %name-devel.lst
%_bindir/ecpg
%_libdir/libecpg.so
%_libdir/libpgtypes.so
%_libdir/pkgconfig/libecpg.pc
%_libdir/pkgconfig/libpgtypes.pc
%_includedir/ecpg*.h
%_includedir/pgsql/informix
%_includedir/pgtypes*.h
%_includedir/sql3types.h
%_includedir/sqlca.h
%_includedir/sqlda*.h


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 16.4-4
- Import
