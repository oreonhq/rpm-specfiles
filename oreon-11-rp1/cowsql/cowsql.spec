%global source0_hash 257aee775f68fd145bfae012dc394fdf62c2f97f0360b0bcf6bd1f66bc58ca04

%global forgeurl https://github.com/cowsql/cowsql
Version:        1.15.9
%forgemeta

Name:           cowsql
Release:        %autorelease
Summary:        Embeddable, replicated and fault tolerant SQL engine
License:        LGPL-3.0-only WITH LGPL-3.0-linking-exception
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(raft)

%description
cowsql is a C library that implements an embeddable and replicated SQL database
engine with high availability and automatic failover.

cowsql extends SQLite with a network protocol that can connect together various
instances of your application and have them act as a highly-available cluster,
with no dependency on external databases.

The name "cowsql" loosely refers to the "pets vs. cattle" concept, since it's
generaly fine to delete or rebuild a particular node of an application that uses
cowsql for data storage.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build
export CFLAGS="%{optflags} -Wno-error=discarded-qualifiers"
autoreconf -i
%configure --disable-static
%make_build

%install
%make_install

%check
make check

%files
%license LICENSE
%doc README.md
%{_libdir}/libcowsql.so.0*

%files devel
%{_libdir}/libcowsql.so
%{_libdir}/pkgconfig/cowsql.pc
%{_includedir}/cowsql.h

%changelog
%autochangelog
