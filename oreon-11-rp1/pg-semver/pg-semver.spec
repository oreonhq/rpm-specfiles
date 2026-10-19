%global source0_hash 2b740332e742e80d682aa15f14967d94a8967a62bfe9eab8e8efdb71646658ac
%global pg_config PG_CONFIG=%_bindir/pg_config
Name:		pg-semver
Version:	0.41.0
Release:        1%{?dist}
Summary:        A semantic version data type for PostgreSQL
License:	PostgreSQL
Url:		https://github.com/theory/pg-semver
Source0:        http://api.pgxn.org/dist/semver/%{version}/semver-%{version}.zip
Requires(pre):	postgresql-server
# oreon:deps
BuildRequires:  clang
BuildRequires:  gcc
BuildRequires:  llvm
BuildRequires:  make
BuildRequires:  postgresql-server-devel
# /oreon:deps
%description
PostgreSQL server extension implementing data type called "semver".
It's an implementation of the version number format specified by the
Semantic Versioning Specification.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir semver-%{version}
%oreon_prep
%build

%make_build CFLAGS="%{optflags}" %pg_config
%install
%make_install CFLAGS="%{optflags}" %pg_config
rm -f %{buildroot}%{_docdir}/pgsql/contrib/semver.mmd
rm -f %{buildroot}%{_docdir}/pgsql/extension/semver.mmd
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
