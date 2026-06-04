%global source0_hash 74b1081d21fff13ae4bd7c16e5d6e504a4c26f7cde1dca0d963a484174bbcacd

%bcond_with largefile

Summary: A GNU set of database routines which use extensible hashing
Name: gdbm
Version: 1.23
Release: 11%{?dist}
Epoch: 1
License: GPL-3.0-or-later
URL: http://www.gnu.org/software/gdbm/

Source:        https://ftp.gnu.org/gnu/gdbm/gdbm-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: libtool
BuildRequires: gettext
BuildRequires: readline-devel
BuildRequires: make

# when -libs subpkg was introduced
Obsoletes: gdbm < 1:1.14.1-4

Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

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
# when -libs subpkg was introduced
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

# get rid of rpath (as per https://fedoraproject.org/wiki/Packaging:Guidelines#Beware_of_Rpath)
# currently --disable-rpath doesn't work for gdbm_dump|load, gdbmtool and libgdbm_compat.so.4
# https://puszcza.gnu.org.ua/bugs/index.php?359
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%make_install

%find_lang %{name}

# create symlinks for compatibility
mkdir -p $RPM_BUILD_ROOT/%{_includedir}/gdbm
ln -sf ../gdbm.h $RPM_BUILD_ROOT/%{_includedir}/gdbm/gdbm.h
ln -sf ../ndbm.h $RPM_BUILD_ROOT/%{_includedir}/gdbm/ndbm.h
ln -sf ../dbm.h $RPM_BUILD_ROOT/%{_includedir}/gdbm/dbm.h

# Remove libtool archives
find %{buildroot} -type f -name "*.la" -delete

rm -f $RPM_BUILD_ROOT/%{_infodir}/dir

%check
export LD_LIBRARY_PATH=`pwd`/src/.libs/:`pwd`/compat/.libs/
make check

%ldconfig_scriptlets libs

%files -f %{name}.lang
%doc NEWS README THANKS AUTHORS NOTE-WARNING
%{_bindir}/gdbm*
%{_mandir}/man1/gdbm*

%files libs
%license COPYING
%{_libdir}/libgdbm.so.6*
%{_libdir}/libgdbm_compat.so.4*

%files devel
%{_libdir}/libgdbm.so
%{_libdir}/libgdbm_compat.so
%{_includedir}/*
%{_infodir}/*.info*
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.23-11
- Prepare for Oreon 11 (RP1)
