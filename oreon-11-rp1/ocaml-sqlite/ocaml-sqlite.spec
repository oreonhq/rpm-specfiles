%global source0_hash 6d2d03f6e30e876e006160b32e3e866f37194f23a0ece983cf8af842e4fc9b20

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global giturl  https://github.com/mmottl/sqlite3-ocaml

Name:           ocaml-sqlite
Version:        5.3.1
Release:        4%{?dist}
Summary:        OCaml library for accessing SQLite3 databases
License:        MIT

URL:            https://mmottl.github.io/sqlite3-ocaml
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}/sqlite3-ocaml-%{version}.tar.gz

BuildRequires:  ocaml >= 4.12
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-ppx-inline-test-devel
BuildRequires:  sqlite-devel >= 3

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

%autosetup -n sqlite3-ocaml-%{version}

%build
%dune_build

%check
%dune_check

%install
%dune_install

%files -f .ofiles
%license LICENSE.md

%files devel -f .ofiles-devel
%license LICENSE.md
%doc CHANGELOG.md README.md

%changelog
%autochangelog
