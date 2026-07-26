%global source0_hash 0f7b1f159974f49a47842a8ab6751aecca1ed1142b6d5e38d81b064b2ead1b4b

%global	sname	ip4r

Summary:	IPv4/v6 type and IPv4/v6 range index type for PostgreSQL
Name:		postgresql-%{sname}
Version:	2.4.2
Release:	8%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
# Note that the URL is generated, needs to be changed.
Source0:	https://github.com/RhodiumToad/%sname/archive/%version/%name-%version.tar.gz
URL:		https://github.com/RhodiumToad/ip4r

BuildRequires: make
BuildRequires:	gcc
BuildRequires:	clang-devel llvm-devel
BuildRequires:	postgresql-server-devel

Requires(pre): postgresql-server

%description
ip4, ip4r, ip6, ip6r, ipaddress and iprange are types that contain a single
IPv4/IPv6 address and a range of IPv4/IPv6 addresses respectively. They can
be used as a more flexible, indexable version of the cidr type.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{sname}-%{version} -p1

%build
%make_build PG_CONFIG=%_bindir/pg_server_config

%install
%make_install PG_CONFIG=%_bindir/pg_server_config
%{__rm} %{buildroot}/usr/share/doc/pgsql/extension/README.ip4r

# Package into *-devel once it is requested, more info:
# https://github.com/RhodiumToad/ip4r/pull/13
%{__rm} -r %{buildroot}%{_includedir}/pgsql

%files
%doc README.ip4r
%{_datadir}/pgsql/extension/*
%{_libdir}/pgsql/%{sname}.so
%if 0%{?postgresql_server_llvmjit}
%{_libdir}/pgsql/bitcode/%{sname}*.bc
%{_libdir}/pgsql/bitcode/%{sname}/src/*.bc
%endif

%changelog
%autochangelog
