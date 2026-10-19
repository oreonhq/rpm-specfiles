%global source0_hash b49157a38b520c919a327637bfa6478b9985d9ec7c78b47c68595ba0271371a1
%global	sname	ip4r
Summary:        IPv4/v6 type and IPv4/v6 range index type for PostgreSQL
Name:		postgresql-%{sname}
Version:	2.4.3
Release:        1%{?dist}
License:	LicenseRef-Callaway-BSD
Source0:        https://github.com/RhodiumToad/%{sname}/archive/%{version}/%{name}-%{version}.tar.gz
URL:		https://github.com/RhodiumToad/ip4r
Requires(pre): postgresql-server
# oreon:deps
BuildRequires:  clang-devel
BuildRequires:  gcc
BuildRequires:  llvm-devel
BuildRequires:  make
BuildRequires:  postgresql-server-devel
# /oreon:deps
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
%{__rm} -r %{buildroot}%{_includedir}/pgsql
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
