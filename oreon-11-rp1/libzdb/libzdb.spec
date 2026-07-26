%global source0_hash 5b4633fc2a16880f776197f4045f62ef8db5062f63030fa221011d4b85d736cb

Name:           libzdb
Version:        3.4.1
Release:        3%{?dist}
Summary:        Small, easy to use Database Connection Pool Library
# Automatically converted from old format: GPLv3+ and MIT - review is highly recommended.
License:        GPL-3.0-or-later AND LicenseRef-Callaway-MIT
URL:            http://www.tildeslash.com/libzdb/
Source0:        http://www.tildeslash.com/%{name}/dist/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  flex
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  libpq-devel
BuildRequires:  sqlite-devel >= 3.6.12
BuildRequires: make

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

%files
%doc AUTHORS CHANGES COPYING README
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/zdb/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/zdb.pc
%doc doc/api-docs

%changelog
%autochangelog
