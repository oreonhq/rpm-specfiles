%global source0_hash a43b27547309ac95ce428a737428f18bf5f61f957d026e17500e5840dda01d8c
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-store
Version:        0.2
Release:        1%{?dist}
Summary:        Snapshottable data structures
License:        MIT
SourceLicense:  %{license} AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://gitlab.com/basile.clement/store
VCS:            git:%{url}.git
Source0:        https://gitlab.com/basile.clement/store/-/archive/v%{version}/store-v%{version}.tar.bz2
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
# /oreon:deps
%description
`Store` is a library to add snapshotting capabilities to imperative data
structures with low runtime cost and safe, user-friendly APIs.  It is designed
for (and works best with) applications that exploit backtracking algorithms,
such as SMT solvers, type-checking and type-inference algorithms.

Currently, `Store` only provides snapshottable references; support for custom
built-in data structures that benefit from non-backtracked operations (such as
resizing a dynamic array) is planned.

The design of the Store library is described in the ICFP'24 paper:

    Clément Allain, Basile Clément, Alexandre Moine, and Gabriel Scherer. 2024.
    Snapshottable Stores.
    Proc. ACM Program. Lang. 8, ICFP, Article 248 (August 2024), 32 pages.
    https://doi.org/10.1145/3674637

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir store-v%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-store-devel -f %{oreon_filedir}/ocaml-store-devel.list

%changelog

%autochangelog
