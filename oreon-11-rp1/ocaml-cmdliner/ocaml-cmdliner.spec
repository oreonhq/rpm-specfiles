%global source0_hash 05b938d1def4f54c478178f1982822834510431ed98f2ac67cb4d90aa120d6b6
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-cmdliner
Version:        2.1.1
Release:        1%{?dist}
Summary:        Declarative definition of command line interfaces for OCaml
License:        ISC
URL:            https://erratique.ch/software/cmdliner
VCS:            git:%{url}.git
Source0:        https://erratique.ch/software/cmdliner/releases/cmdliner-%{version}.tbz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
# /oreon:deps
%description
Cmdliner allows the declarative definition of command line
interfaces for OCaml.

It provides a simple and compositional mechanism to convert
command line arguments to OCaml values and pass them to your
functions. The module automatically handles syntax errors,
help messages and UNIX man page generation. It supports
programs with single or multiple commands and respects
most of the POSIX and GNU conventions.

Cmdliner has no dependencies and is distributed under
the ISC license.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir cmdliner-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-cmdliner-devel -f %{oreon_filedir}/ocaml-cmdliner-devel.list

%changelog

%autochangelog
