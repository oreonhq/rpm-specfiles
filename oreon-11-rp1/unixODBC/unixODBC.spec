%global source0_hash 4e2814de3e01fc30b0b9f75e83bb5aba91ab0384ee951286504bb70205524771
%bcond   gui_related_parts 1
Name:    unixODBC
Version: 2.3.14
Release:        1%{?dist}
License: GPL-2.0-or-later AND LGPL-2.1-or-later
Summary:        A complete ODBC driver manager for Linux
URL:     http://www.unixODBC.org/
Source0:        http://www.unixODBC.org/%{name}-%{version}.tar.gz
Source1: odbcinst.ini
Patch8:  so-version-bump.patch
Patch9:  keep-typedefs.patch
Conflicts: iodbc
Suggests: mariadb-connector-odbc
Suggests: mysql-connector-odbc
Suggests: postgresql-odbc
Suggests: unixODBC-gui-qt
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  make
BuildRequires:  multilib-rpm-config
BuildRequires:  readline-devel
# /oreon:deps
%description
Install unixODBC if you want to access databases through ODBC.
You will also need the mariadb-connector-odbc package if you want to access
a MySQL or MariaDB database, and/or the postgresql-odbc package for PostgreSQL.

%package devel
Summary: Development files for programs which will use the unixODBC library
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The unixODBC package can be used to access databases through ODBC
drivers. If you want to develop programs that will access data through
ODBC, you need to install this package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P8 -p1 -b .soname-bump
%patch -P9 -p1

autoreconf -vfi

%build

%configure \
  --with-gnu-ld=yes \
  --enable-threads=yes \
  --enable-drivers=no \
%if %{with gui_related_parts}
  --enable-driver-config=yes
%else
  --enable-driver-config=no
%endif
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build
%install
%make_install
install -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}
%multilib_fix_c_header --file %{_includedir}/unixODBC/unixodbc_conf.h
mkdir $RPM_BUILD_ROOT%{_libdir}/%{name}
find doc -name 'Makefile*' | xargs rm
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libltdl.*
rm -rf $RPM_BUILD_ROOT%{_datadir}/libtool
find $RPM_BUILD_ROOT%{_libdir} -name "*.so.*" | sed "s|^$RPM_BUILD_ROOT||" > base-so-list
find $RPM_BUILD_ROOT%{_libdir} -name "*.so"   | sed "s|^$RPM_BUILD_ROOT||" > devel-so-list
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n unixODBC-devel -f %{oreon_filedir}/unixODBC-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3.14-3
- Prepare for Oreon 11 (RP1)
