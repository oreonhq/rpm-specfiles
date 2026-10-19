%global source0_hash 6a24504a14de4a744103dcb936be976df6fbe88ccff26065e54c1c47946f4a5e
%bcond_with largefile
Summary:        A GNU set of database routines which use extensible hashing
Name: compat-gdbm
Version: 1.26
Release:        1%{?dist}
License: GPLv3+
URL: http://www.gnu.org/software/gdbm/
Source0:        http://ftp.gnu.org/gnu/gdbm/gdbm-%{version}.tar.gz
Patch1: gdbm-1.10-fedora.patch
Patch2: gdbm_gcc_10.patch
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  readline-devel
# /oreon:deps
%description
This is package is used only for rebase of gdbm in Fedora.
Don't use it!

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
%description libs
Libraries for the Gdbm GNU database indexing library

%package devel
Summary: Development libraries and header files for the gdbm library
Requires: %{name}%{?_isa} = %{version}-%{release}
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

%setup -q -n gdbm-%{version}
%patch -P1 -p1 -b .fedora
%patch -P2 -p1

%build

%configure \
    --disable-static \
%{!?with_largefile: --disable-largefile} \
    --disable-rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
%install
make DESTDIR=$RPM_BUILD_ROOT install
mkdir -p $RPM_BUILD_ROOT/%{_includedir}/gdbm 
ln -sf ../gdbm.h $RPM_BUILD_ROOT/%{_includedir}/gdbm/gdbm.h
ln -sf ../ndbm.h $RPM_BUILD_ROOT/%{_includedir}/gdbm/ndbm.h
ln -sf ../dbm.h $RPM_BUILD_ROOT/%{_includedir}/gdbm/dbm.h
find %{buildroot} -type f -name "*.la" -delete
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir
rm -rf %{buildroot}%{_datadir}/locale
rm %{buildroot}%{_bindir}/gdbm*
rm %{buildroot}%{_mandir}/man1/gdbm*
%oreon_autofiles compat-gdbm-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles compat-gdbm-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export LD_LIBRARY_PATH=`pwd`/src/.libs/:`pwd`/compat/.libs/
make check
%ldconfig_scriptlets libs
%files -f %{oreon_filedir}/main.list
%files -n compat-gdbm-libs -f %{oreon_filedir}/compat-gdbm-libs.list
%files -n compat-gdbm-devel -f %{oreon_filedir}/compat-gdbm-devel.list

%changelog

%autochangelog
