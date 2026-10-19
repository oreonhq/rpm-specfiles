%global source0_hash 6b8d56e3949baacac81f27caf0378f7a87b692bac60f187e15498303872c5cd3
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-unionfind
Version:        20260226
Release:        1%{?dist}
Summary:        OCaml implementations of the union-find data structure
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://gitlab.inria.fr/fpottier/unionfind
VCS:            git:%{url}.git
Source0:        https://gitlab.inria.fr/fpottier/unionfind/-/archive/%{version}/unionfind-%{version}.tar.bz2
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-store-devel
# /oreon:deps
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
%global oreon_srcdir unionfind-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-unionfind-devel -f %{oreon_filedir}/ocaml-unionfind-devel.list

%changelog

%autochangelog
