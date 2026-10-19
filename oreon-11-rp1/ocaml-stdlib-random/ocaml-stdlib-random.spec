%global source0_hash b479958eb83bab2d3e1c4ea1054e2d963b6adf2a1e671706e9130e617a5dcb03
Name:           ocaml-stdlib-random
Version:        1.2.0
Release:        1%{?dist}
Summary:        Versioned Random module from the OCaml standard library
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://github.com/ocaml/stdlib-random
VCS:            git:%{url}.git
Source0:        https://github.com/ocaml/stdlib-random/archive/%{version}/stdlib-random-%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-cppo
BuildRequires:  ocaml-dune
# /oreon:deps
%description
The stdlib-random package provides a stable and compiler-independent
implementation of all the PRNGs used in the Random module.  Those PRNGs are
available in the various libraries:
- stdlib-random.v3: OCaml 3.07 to 3.11 PRNG
- stdlib-random.v4: OCaml 3.12 to 4.14 PRNG
- stdlib-random.v5: current OCaml 5.0 PRNG
- stdlib-random.v5o: pure OCaml version of the OCaml 5 PRNG
All those libraries can be used together and the signature of their Random$n
module has been extended to the latest signature whenever possible.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files
for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir stdlib-random-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-stdlib-random-devel -f %{oreon_filedir}/ocaml-stdlib-random-devel.list

%changelog

%autochangelog
