%global source0_hash fb52543bf4fc92073e3d1caba0e79db8ffc273d10e7f581f3653fbed71bee5ae

%if 0%{?fedora}
%global pg_config PG_CONFIG=%_bindir/pg_server_config
%else
%global pg_config PG_CONFIG=%_bindir/pg_config
%endif

Name:		pg-semver
Version:	0.32.1
Release:	8%{?dist}
Summary:	A semantic version data type for PostgreSQL
License:	PostgreSQL
Url:		https://github.com/theory/pg-semver
Source0:	http://api.pgxn.org/dist/semver/%{version}/semver-%{version}.zip
BuildRequires:	clang
BuildRequires:	gcc
BuildRequires:	llvm
BuildRequires:	make
BuildRequires:	postgresql-server-devel
Requires(pre):	postgresql-server

%description
PostgreSQL server extension implementing data type called "semver".
It's an implementation of the version number format specified by the
Semantic Versioning Specification.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n semver-%{version}

%build
%make_build CFLAGS="%{optflags}" %pg_config

%install
%make_install CFLAGS="%{optflags}" %pg_config

# remove misplaced documentation file, added via doc
rm -f %{buildroot}%{_docdir}/pgsql/contrib/semver.mmd
rm -f %{buildroot}%{_docdir}/pgsql/extension/semver.mmd

%files
%doc LICENSE README.md doc/semver.mmd
%{_libdir}/pgsql/semver.so
%{_datadir}/pgsql/extension/semver*.sql
%{_datadir}/pgsql/extension/semver.control

%changelog
%autochangelog
