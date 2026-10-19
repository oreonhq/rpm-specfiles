%global source0_hash c1575341fa7bd40f5274ea465b34390f4dc64cdd0770af327005caaeb9f6b7ed
%global source1_hash be680cd4ef78048fd846aeb5e13b5b2f19bd5a3505ed2f2994ae52e4090bfc53
%global majorversion 16
Summary:        ECPG - Embedded SQL in C
Name: libecpg
Version: %majorversion.15
Release:        1%{?dist}
License: PostgreSQL
Url: http://www.postgresql.org/
Source0:        https://ftp.postgresql.org/pub/source/v%{version}/postgresql-%{version}.tar.bz2
Source1: https://ftp.postgresql.org/pub/source/v%version/postgresql-%version.tar.bz2.sha256
Patch1: libecpg-10.5-rpm-pgsql.patch
Patch2: libecpg-10.5-var-run-socket.patch
Patch3: libecpg-12.2-external-libpq.patch
Patch4: libecpg-10.5-no-compat-lib.patch
Patch5: libecpg-12.2-dependency-build.patch
%{!?rhel:BuildRequires: multilib-rpm-config}
Requires: libpgtypes = %{version}-%{release}
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glibc-devel
BuildRequires:  krb5-devel
BuildRequires:  libicu-devel
BuildRequires:  libpq-devel
BuildRequires:  make
BuildRequires:  multilib-rpm-config
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
( cd "$(dirname "%SOURCE1")" ; sha256sum -c "%SOURCE1" )
%autosetup -n postgresql-%version -p1

# remove .gitignore files to ensure none get into the RPMs (bug #642210)
find . -type f -name .gitignore | xargs rm

%build

export CFLAGS="$CFLAGS -std=c17"
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
find $RPM_BUILD_ROOT -name '*.a' -delete
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
%oreon_autofiles libpgtypes usr/*/lib*.so.*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libecpg-devel -f %{oreon_filedir}/libecpg-devel.list
%files -n libpgtypes -f %{oreon_filedir}/libpgtypes.list

%changelog

%autochangelog
