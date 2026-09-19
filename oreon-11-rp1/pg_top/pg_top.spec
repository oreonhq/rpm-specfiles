%global source0_hash 71c555801432e6eeaaaa69589d7291a9ef157073653712b1ae0fd5e94569c95e

Summary:	'top' for PostgreSQL process
Name:		pg_top
Version:	4.1.3
Release:	%autorelease
License:	BSD-3-Clause
Source:		https://gitlab.com/pg_top/pg_top/-/archive/v%{version}/pg_top-v%{version}.tar.bz2
URL:		https://pg_top.gitlab.io/
BuildRequires:	cmake
BuildRequires:	elfutils-libelf-devel
BuildRequires:	gcc
BuildRequires:	libbsd-devel
BuildRequires:	libpq-devel
BuildRequires:	readline-devel
BuildRequires:	/usr/bin/rst2man
Requires:	postgresql-server

%description
pg_top is 'top' for PostgreSQL processes. See running queries, 
query plans, issued locks, and table and index statistics.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-v%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%{_mandir}/man1/%{name}*
%{_bindir}/%{name}
%doc HISTORY.rst README.rst TODO Y2K
%license LICENSE

%changelog
%autochangelog
