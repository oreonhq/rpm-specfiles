%global source0_hash ff9c425a88bc20bf9318a332eec50b17e77896eef65a0e69415ccb4e396d1812
Name:           mdbtools
Version:        1.0.1
Release:        1%{?dist}
Summary:        Access data stored in Microsoft Access databases
License:        GPL-2.0-or-later
URL:            https://github.com/mdbtools/mdbtools/
Source0:        https://github.com/mdbtools/mdbtools/releases/download/v%{version}/mdbtools-%{version}.tar.gz
Patch1:         mdbtools-0.9.3-mdb-sql-compile-fix.patch
Patch2:         mdbtools-1.0.0-s390x-build-fix.patch
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-gui <= 0.7.1-99
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bash-completion
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  rarian-compat
BuildRequires:  readline-devel
BuildRequires:  txt2man
BuildRequires:  unixODBC-devel
# /oreon:deps
%description
MDB Tools is a suite of programs for accessing data stored in Microsoft
Access databases.

%package libs
Summary:        Library for accessing data stored in Microsoft Access databases
License:        LGPLv2+
%description libs
This package contains the MDB Tools library, which can be used by applications
to access data stored in Microsoft Access databases.

%package        devel
Summary:        Development files for %{name}
License:        LGPLv2+
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}, glib2-devel, pkgconfig
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        odbc
Summary:        MDB Unix-ODBC driver
License:        LGPLv2+
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    odbc
The mdbtools-odbc package contains a Unix-ODBC driver using
the mdbtools SQL front-end for MDB files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
autoreconf -vif

%build

%configure --disable-static --with-unixodbc="%{_prefix}"
%make_build V=1
%install
%make_install
find %{buildroot} -type f -name "*.la" -delete
%ldconfig_scriptlets libs
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mdbtools-libs -f %{oreon_filedir}/mdbtools-libs.list
%files -n mdbtools-devel -f %{oreon_filedir}/mdbtools-devel.list
%files -n mdbtools-odbc -f %{oreon_filedir}/mdbtools-odbc.list

%changelog

%autochangelog
