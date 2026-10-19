%global source0_hash ce4248be9b09a6a04a6ba09ef6009c699ee996ec9a2ba5755bc252e5045fc6c0
ExcludeArch: %{ix86}
Name:           ocaml-postgresql
Version:        5.4.0
Release:        1%{?dist}
Summary:        OCaml library for accessing PostgreSQL databases
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://github.com/mmottl/postgresql-ocaml
VCS:            git:%{url}.git
Source0:        https://github.com/mmottl/postgresql-ocaml/releases/download/%{version}/postgresql-%{version}.tbz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  pkgconfig(libpq)
# /oreon:deps
%description
This OCaml-library provides an interface to PostgreSQL, an efficient
and reliable, open source, relational database.  Almost all
functionality available through the C-API (libpq) is replicated in a
type-safe way.  This library uses objects for representing database
connections and results of queries.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir postgresql-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-postgresql-devel -f %{oreon_filedir}/ocaml-postgresql-devel.list

%changelog

%autochangelog
