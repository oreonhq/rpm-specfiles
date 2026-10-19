%global source0_hash 2f44edc6fac952942a7963d45c5837bfc5c933fe9f5cb62d0c05ee4a9187e0e4
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-opam-file-format
Version:        2.2.0
Release:        1%{?dist}
Summary:        Parser and printer for the opam file syntax
License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception
URL:            https://github.com/ocaml/opam-file-format
VCS:            git:%{url}.git
Source0:        https://github.com/ocaml/opam-file-format/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-fmt-devel
BuildRequires:  ocaml-menhir
# /oreon:deps
%description
Parser and printer for the opam file syntax.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir opam-file-format-%{version}
%oreon_prep
%build

%{dune_build}
%check

%{dune_check}
%install
%{dune_install}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ocaml-opam-file-format-devel -f %{oreon_filedir}/ocaml-opam-file-format-devel.list

%changelog

%autochangelog
