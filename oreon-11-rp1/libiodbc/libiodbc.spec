%global source0_hash a0cf0375b462f98c0081c2ceae5ef78276003e57cdf1eb86bd04508fb62a0660
%global giturl https://github.com/openlink/iODBC
Summary:        iODBC Driver Manager
Name: libiodbc
Version: 3.52.16
Release:        4%{?dist}
License: LGPL-2.0-only OR BSD-3-Clause
URL: http://www.iodbc.org/
VCS: git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch100: libiodbc-3.52.12-multilib.patch
Patch101: libiodbc-3.52.16-lto.patch
Patch102: libiodbc-3.52.16-unicode.patch
%{?_enable_gui:BuildRequires: gtk2-devel}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
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

./autogen.sh
export CFLAGS='%{build_cflags} -std=gnu17'
%configure \
  --enable-odbc3 \
  --with-iodbc-inidir=%{_sysconfdir} \
  --with-layout=RedHat \
  --enable-pthreads \
  --disable-libodbc \
  --disable-static \
  --includedir=%{_includedir}/libiodbc \
  %{?_enable_gui} %{!?_enable_gui:--disable-gui}
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool
%make_build
%install
%make_install
rm -fv %{buildroot}%{_libdir}/lib*.la
rm -rfv %{buildroot}%{_datadir}/libiodbc/samples
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libiodbc-devel -f %{oreon_filedir}/libiodbc-devel.list
%files -n libiodbc-admin -f %{oreon_filedir}/libiodbc-admin.list

%changelog

%autochangelog
