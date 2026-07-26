%global source0_hash 1c47d22772f8938ff23d7350575d88ff2a3cf0d1f3988162f7bb807bccb157af

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-postgresql
Version:        5.3.2
Release:        3%{?dist}
Summary:        OCaml library for accessing PostgreSQL databases

License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://github.com/mmottl/postgresql-ocaml
VCS:            git:%{url}.git
Source0:        %{url}/releases/download/%{version}/postgresql-%{version}.tbz

BuildRequires:  ocaml >= 4.12
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  pkgconfig(libpq)

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

%autosetup -n postgresql-%{version} -p1

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc README.md
%license LICENSE.md

%files devel -f .ofiles-devel
%doc CHANGELOG.md examples
%license LICENSE.md

%changelog
%autochangelog
