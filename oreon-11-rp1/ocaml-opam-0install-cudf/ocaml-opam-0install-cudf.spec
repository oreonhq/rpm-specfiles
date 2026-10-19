%global source0_hash d8dcc6b080ad8edddb012e6acf06df809fadd27877d2a711bbe51bc8474144e0
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-opam-0install-cudf
Version:        0.5.0
Release:        1%{?dist}
Summary:        A generic CUDF solver library meant to be used in opam
License:        ISC
URL:            https://github.com/ocaml-opam/opam-0install-cudf
VCS:            git:%{url}.git
Source0:        https://github.com/ocaml-opam/opam-0install-cudf/archive/v%{version}/opam-0install-cudf-%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-0install-solver-devel
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-cudf-devel
BuildRequires:  ocaml-dune
# /oreon:deps
%description
Opam's default solver is designed to maintain a set of packages over time,
minimizing disruption when installing new programs and finding a compromise
solution across all packages (e.g. avoiding upgrading some library to prevent
uninstalling another program).

In many situations (e.g. a CI system building in a clean environment, a
project-local opam root, or a duniverse build) this is not necessary, and we
can get a solution much faster by using a different algorithm.

This package provides a generic solver library which uses 0install's solver
library.  The CUDF library is used in order to interface with opam as it is
the format used to talk to the supported solvers.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir opam-0install-cudf-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-opam-0install-cudf-devel -f %{oreon_filedir}/ocaml-opam-0install-cudf-devel.list

%changelog

%autochangelog
