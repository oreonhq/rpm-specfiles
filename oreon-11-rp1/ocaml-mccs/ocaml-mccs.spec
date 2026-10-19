%global source0_hash 071c83c0c5336476ff4b0ac4223c0494d399b6be17a1f47bd22c13a2df686e1d
ExcludeArch: %{ix86}
%global basever  1.1
%global extraver 19
Name:           ocaml-mccs
Version:        %{basever}.%{extraver}
Release:        1%{?dist}
Summary:        Multi Criteria CUDF Solver with OCaml bindings
%global libname %(echo %{name} | sed -e 's/^ocaml-//')
License:        BSD-3-Clause AND LGPL-3.0-or-later WITH OCaml-LGPL-linking-exception
URL:            https://github.com/AltGr/ocaml-mccs
VCS:            git:%{url}.git
Source0:        https://github.com/AltGr/%{name}/archive/%{basever}+%{extraver}/%{name}-%{basever}-%{extraver}.tar.gz
Patch:          ocaml-mccs-1.1-glpk.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glpk-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-cudf-devel
BuildRequires:  ocaml-dune
# /oreon:deps
%description
mccs (which stands for Multi Criteria CUDF Solver) is a CUDF problem solver
developed at UNS during the European MANCOOSI project.

This project contains a stripped-down version of the mccs solver, taken from
snapshot 1.1, with a binding as an OCaml library, and building with dune.

The binding enables interoperation with binary CUDF data from the OCaml CUDF
library, and removes the native C++ parsers and printers.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-cudf-devel%{?_isa}
Requires:       glpk-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{basever}-%{extraver} -p1

%conf
# Choose the build method that uses an installed glpk
cp -p src/glpk/dune-shared src/glpk/dune

# Temporary workaround for https://github.com/ocaml-opam/ocaml-mccs/issues/54
sed -i 's,clibs,../clibs,' src/glpk/dune

%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-mccs-devel -f %{oreon_filedir}/ocaml-mccs-devel.list

%changelog

%autochangelog
