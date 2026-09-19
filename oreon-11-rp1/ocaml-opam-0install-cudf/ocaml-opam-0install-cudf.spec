%global source0_hash d8dcc6b080ad8edddb012e6acf06df809fadd27877d2a711bbe51bc8474144e0

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-opam-0install-cudf
Version:        0.5.0
Release:        %autorelease
Summary:        A generic CUDF solver library meant to be used in opam

License:        ISC
URL:            https://github.com/ocaml-opam/opam-0install-cudf
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/opam-0install-cudf-%{version}.tar.gz

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-0install-solver-devel >= 2.18
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-cudf-devel >= 0.10
BuildRequires:  ocaml-dune >= 2.7

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

%autosetup -n opam-0install-cudf-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
