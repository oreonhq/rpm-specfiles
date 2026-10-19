%global source0_hash 6a24504a14de4a744103dcb936be976df6fbe88ccff26065e54c1c47946f4a5e
%bcond_with largefile
Summary:        A GNU set of database routines which use extensible hashing
Name: gdbm
Version: 1.26
Release:        1%{?dist}
Epoch: 1
License: GPL-3.0-or-later
URL: http://www.gnu.org/software/gdbm/
Source0:        https://mirrors.kernel.org/gnu/gdbm/gdbm-%{version}.tar.gz
Obsoletes: gdbm < 1:1.14.1-4
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  readline-devel
# /oreon:deps
%description
Gdbm is a GNU database indexing library, including routines which use
extensible hashing.  Gdbm works in a similar way to standard UNIX dbm
routines.  Gdbm is useful for developers who write C applications and
need access to a simple and efficient database or who are building C
applications which will use such a database.

If you're a C developer and your programs need access to simple
database routines, you should install gdbm.  You'll also need to
install gdbm-devel.

%package libs
Summary: Libraries files for gdbm
Obsoletes: gdbm < 1:1.14.1-4
%description libs
Libraries for the Gdbm GNU database indexing library

%package devel
Summary: Development libraries and header files for the gdbm library
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires(post): info
Requires(preun): info
%description devel
Gdbm-devel contains the development libraries and header files for
gdbm, the GNU database system.  These libraries and header files are
necessary if you plan to do development using the gdbm database.

Install gdbm-devel if you are developing C programs which will use the
gdbm database library.  You'll also need to install the gdbm package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

CFLAGS="$CFLAGS -std=gnu11"
export CFLAGS
%configure \
    --disable-static \
%{!?with_largefile: --disable-largefile} \
    --disable-rpath \
    --enable-libgdbm-compat
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install
%find_lang %{name}
mkdir -p $RPM_BUILD_ROOT/%{_includedir}/gdbm
ln -sf ../gdbm.h $RPM_BUILD_ROOT/%{_includedir}/gdbm/gdbm.h
ln -sf ../ndbm.h $RPM_BUILD_ROOT/%{_includedir}/gdbm/ndbm.h
ln -sf ../dbm.h $RPM_BUILD_ROOT/%{_includedir}/gdbm/dbm.h
find %{buildroot} -type f -name "*.la" -delete
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export LD_LIBRARY_PATH=`pwd`/src/.libs/:`pwd`/compat/.libs/
make check
%ldconfig_scriptlets libs
%files -f %{oreon_filedir}/main.list
%files -n gdbm-libs -f %{oreon_filedir}/gdbm-libs.list
%files -n gdbm-devel -f %{oreon_filedir}/gdbm-devel.list

%changelog

%autochangelog
