%global source0_hash 6d2d03f6e30e876e006160b32e3e866f37194f23a0ece983cf8af842e4fc9b20
ExcludeArch: %{ix86}
%global giturl  https://github.com/mmottl/sqlite3-ocaml
Name:           ocaml-sqlite
Version:        5.3.1
Release:        1%{?dist}
Summary:        OCaml library for accessing SQLite3 databases
License:        MIT
URL:            https://mmottl.github.io/sqlite3-ocaml
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/%{version}/sqlite3-ocaml-%{version}.tar.gz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-ppx-inline-test-devel
BuildRequires:  sqlite-devel
# /oreon:deps
%description
SQLite 3 database library wrapper for OCaml.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       sqlite-devel%{?_isa} >= 3
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir sqlite3-ocaml-%{version}
%oreon_prep
%build

%dune_build
%check

%dune_check
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ocaml-sqlite-devel -f %{oreon_filedir}/ocaml-sqlite-devel.list

%changelog

%autochangelog
