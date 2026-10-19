%global source0_hash c29712aba58ce3c428e6fcf4c96f86c853dde5449da9adfaedbe69e6116e2e17
Name:           libzdb
Version:        3.6.0
Release:        1%{?dist}
Summary:        Small, easy to use Database Connection Pool Library
License:        GPL-3.0-or-later AND LicenseRef-Callaway-MIT
URL:            http://www.tildeslash.com/libzdb/
Source0:        http://www.tildeslash.com/%{name}/dist/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  libpq-devel
BuildRequires:  make
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  sqlite-devel
# /oreon:deps
%description
The Zild C Database Library implements a small, fast, and easy to use database
API with thread-safe connection pooling. The library can connect transparently
to multiple database systems, has zero configuration and connections are
specified via a standard URL scheme.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# Errant file
rm -f doc/api-docs/._*

%build

%configure --disable-static --enable-protected --enable-sqliteunlock
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libzdb-devel -f %{oreon_filedir}/libzdb-devel.list

%changelog

%autochangelog
