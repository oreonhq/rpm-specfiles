%global source0_hash cdceff00ffe014495bed3aed71c7910aa88bf29379f795abc0f46d4ee5f8bc5f

%bcond_with largefile

Summary: A GNU set of database routines which use extensible hashing
Name: compat-gdbm
Version: 1.14.1
Release: 21%{?dist}
License: GPLv3+
URL: http://www.gnu.org/software/gdbm/

Source: http://ftp.gnu.org/gnu/gdbm/gdbm-%{version}.tar.gz
# See https://bugzilla.redhat.com/show_bug.cgi?id=4457
# Upstream bug http://puszcza.gnu.org.ua/bugs/?func=detailitem&item_id=151
# Fixed in http://cvs.gnu.org.ua/viewvc/gdbm/gdbm/src/gdbmopen.c?r1=1.12&r2=1.13
# - version 1.10
#Patch0: gdbm-1.10-zeroheaders.patch

Patch1: gdbm-1.10-fedora.patch
Patch2: gdbm_gcc_10.patch

BuildRequires: gcc
BuildRequires: libtool
BuildRequires: gettext
BuildRequires: readline-devel
BuildRequires: make
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

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

# get rid of rpath (as per https://fedoraproject.org/wiki/Packaging:Guidelines#Beware_of_Rpath)
# currently --disable-rpath doesn't work for gdbm_dump|load, gdbmtool and libgdbm_compat.so.4
# https://puszcza.gnu.org.ua/bugs/index.php?359
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

# create symlinks for compatibility
mkdir -p $RPM_BUILD_ROOT/%{_includedir}/gdbm 
ln -sf ../gdbm.h $RPM_BUILD_ROOT/%{_includedir}/gdbm/gdbm.h
ln -sf ../ndbm.h $RPM_BUILD_ROOT/%{_includedir}/gdbm/ndbm.h
ln -sf ../dbm.h $RPM_BUILD_ROOT/%{_includedir}/gdbm/dbm.h

# Remove libtool archives
find %{buildroot} -type f -name "*.la" -delete

rm -f $RPM_BUILD_ROOT/%{_infodir}/dir

rm -rf %{buildroot}%{_datadir}/locale

# Remove binaries from compat library
rm %{buildroot}%{_bindir}/gdbm*
rm %{buildroot}%{_mandir}/man1/gdbm*

%check
export LD_LIBRARY_PATH=`pwd`/src/.libs/:`pwd`/compat/.libs/
make check

%ldconfig_scriptlets libs

%files
%doc NEWS README THANKS AUTHORS NOTE-WARNING

%files libs
%license COPYING
%{_libdir}/libgdbm.so.5*

%files devel
%{_libdir}/libgdbm.so
%{_includedir}/*
%{_infodir}/*.info*
%{_mandir}/man3/*

%changelog
%autochangelog
