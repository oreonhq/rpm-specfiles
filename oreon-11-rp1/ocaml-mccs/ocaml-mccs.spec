%global source0_hash 071c83c0c5336476ff4b0ac4223c0494d399b6be17a1f47bd22c13a2df686e1d

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

# Upstream uses a + character in the version, which RPM does not support.
# We transform the + into a period.  See
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Versioning/#_upstream_uses_invalid_characters_in_the_version
%global basever  1.1
%global extraver 19

Name:           ocaml-mccs
Version:        %{basever}.%{extraver}
Release:        6%{?dist}
Summary:        Multi Criteria CUDF Solver with OCaml bindings

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

# Original C/C++ code is BSD-3-Clause, OCaml bindings are LGPL.
# The bundled glpk code is not used.
License:        BSD-3-Clause AND LGPL-3.0-or-later WITH OCaml-LGPL-linking-exception

URL:            https://github.com/AltGr/ocaml-mccs
VCS:            git:%{url}.git

# Upstream's use of a '+' instead of a '.' makes this hard to use a macro.
Source:         https://github.com/AltGr/ocaml-mccs/archive/%{basever}+%{extraver}/%{name}-%{basever}-%{extraver}.tar.gz

# Link against the system glpk library
Patch:          ocaml-mccs-1.1-glpk.patch

BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  gcc, gcc-c++
BuildRequires:  ocaml-cudf-devel
BuildRequires:  glpk-devel

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

%check
%dune_check

%files -f .ofiles
%license LICENCE
%doc README.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
