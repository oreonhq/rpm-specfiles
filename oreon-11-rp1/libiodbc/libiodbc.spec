%global source0_hash a0cf0375b462f98c0081c2ceae5ef78276003e57cdf1eb86bd04508fb62a0660

%global giturl https://github.com/openlink/iODBC

## admin gui build currently busted, FIXME?
#define _enable_gui --enable-gui

Summary: iODBC Driver Manager
Name: libiodbc
Version: 3.52.16
Release: 4%{?dist}
License: LGPL-2.0-only OR BSD-3-Clause
URL: http://www.iodbc.org/
VCS: git:%{giturl}.git
Source0: %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz

## upstream patches

## downstream patches
Patch100: libiodbc-3.52.12-multilib.patch
# Fix LTO type mismatches
# https://github.com/openlink/iODBC/issues/107
# https://github.com/openlink/iODBC/issues/108
Patch101: libiodbc-3.52.16-lto.patch
# Fix FTBFS due to a type mismatch in unicode.c
Patch102: libiodbc-3.52.16-unicode.patch

%{?_enable_gui:BuildRequires: gtk2-devel}
BuildRequires: gcc
# Needed for autogen.sh
BuildRequires: libtool
BuildRequires: make

%description
The iODBC Driver Manager is a free implementation of the SAG CLI and
ODBC compliant driver manager which allows developers to write ODBC
compliant applications that can connect to various databases using
appropriate backend drivers.

%package devel
Summary: Header files and libraries for iODBC development
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains the header files and libraries needed to develop
programs that use the driver manager.

%package admin
Summary: Gui administrator for iODBC development
Requires: %{name}%{?_isa} = %{version}-%{release}
%description admin
This package contains a Gui administrator program for maintaining
DSN information in odbc.ini and odbcinst.ini files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n iODBC-%{version}

# fix header permissions
chmod -x include/*.h

%build
# github tarball does not ship configure
./autogen.sh
# The code is not ready for C23 mode
export CFLAGS='%{build_cflags} -std=gnu17'
# --disable-libodbc to minimize conflicts with unixODBC
%configure \
  --enable-odbc3 \
  --with-iodbc-inidir=%{_sysconfdir} \
  --with-layout=RedHat \
  --enable-pthreads \
  --disable-libodbc \
  --disable-static \
  --includedir=%{_includedir}/libiodbc \
  %{?_enable_gui} %{!?_enable_gui:--disable-gui}

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build

%install
%make_install

# unpackaged files
rm -fv %{buildroot}%{_libdir}/lib*.la
rm -rfv %{buildroot}%{_datadir}/libiodbc/samples

%files 
%doc AUTHORS ChangeLog README
%doc etc/odbc*.ini.sample
%license LICENSE*
%{_bindir}/iodbctest
%{_bindir}/iodbctestw
%{_libdir}/libiodbc.so.2*
%{_libdir}/libiodbcinst.so.2*
%{_mandir}/man1/iodbctest.1*
%{_mandir}/man1/iodbctestw.1*

%files devel
%{_bindir}/iodbc-config
%{_includedir}/libiodbc/
%{_libdir}/libiodbc.so
%{_libdir}/libiodbcinst.so
%{_mandir}/man1/iodbc-config.1*
%{_libdir}/pkgconfig/libiodbc.pc

%if 0%{?_enable_gui:1}
%files admin
%{_bindir}/iodbcadm-gtk
%{_libdir}/libdrvproxy.so*
%{_libdir}/libiodbcadm.so*
%{_mandir}/man1/iodbcadm-gtk.1*
%endif

%changelog
%autochangelog
