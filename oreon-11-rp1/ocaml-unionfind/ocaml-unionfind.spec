%global source0_hash 6b8d56e3949baacac81f27caf0378f7a87b692bac60f187e15498303872c5cd3

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-unionfind
Version:        20260226
Release:        %autorelease
Summary:        OCaml implementations of the union-find data structure

License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://gitlab.inria.fr/fpottier/unionfind
VCS:            git:%{url}.git
Source:         %{url}/-/archive/%{version}/unionfind-%{version}.tar.bz2

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  ocaml >= 5.4.0
BuildRequires:  ocaml-dune >= 3.11
BuildRequires:  ocaml-store-devel >= 0.1

%description
The OCaml library unionFind offers two implementations of the union-find data
structure.  Both implementations are based on disjoint sets forests, with path
compression and linking-by-rank, so as to guarantee good asymptotic
complexity: every operation requires a quasi-constant number of accesses to
the store.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n unionfind-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%license LICENSE
%doc AUTHORS CHANGES.md README.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
