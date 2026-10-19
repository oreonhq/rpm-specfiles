%global source0_hash e41d37507ce6f8ea47d6d41e62e0881139bd1f0c9d2ff982d9cd3048756aafbf
%global giturl  https://github.com/ocaml-ppx/ppxlib
Name:           ocaml-ppxlib
Epoch:          1
Version:        0.38.0
Release:        1%{?dist}
Summary:        Base library and tools for ppx rewriters
License:        MIT
URL:            https://ocaml-ppx.github.io/ppxlib/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/%{version}/ppxlib-%{version}.tar.gz
Patch:          %{name}-stdlib-shims.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-cinaps-devel
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-compiler-libs-janestreet-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ppx-derivers-devel
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-sexplib0-devel
BuildRequires:  ocaml-yojson-devel
# /oreon:deps
%description
The ppxlib project provides the basis for the ppx system, which is currently
the officially supported method for meta-programming in OCaml.  It offers a
principled way to generate code at compile time in OCaml projects.  It
features:
- an OCaml AST / parser/ pretty-printer snapshot, to create a full frontend
  independent of the version of OCaml;
- a library for ppx rewriters in general, and type-driven code generators in
  particular;
- a full-featured driver for OCaml AST transformers;
- a quotation mechanism for writing values representing OCaml AST in the OCaml
  syntax;
- a generator of open recursion classes from type definitions.

%package        tools
Summary:        Command line tools for %{name}
Requires:       %{name}%{?_isa} = 1:%{version}-%{release}
%description    tools
The %{name}-tools package contains command line tools for %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = 1:%{version}-%{release}
Requires:       %{name}-tools%{?_isa} = 1:%{version}-%{release}
Requires:       ocaml-compiler-libs-janestreet-devel%{?_isa}
Requires:       ocaml-ppx-derivers-devel%{?_isa}
Requires:       ocaml-sexplib0-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ppxlib-%{version}
%oreon_prep
%build

%dune_build -p ppxlib,ppxlib-tools
%install
%dune_install -s ppxlib ppxlib-tools
cat .ofiles-ppxlib-tools-devel >> .ofiles-ppxlib-tools
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check -p ppxlib,ppxlib-tools
%files -f %{oreon_filedir}/main.list
%files -n ocaml-ppxlib-tools -f %{oreon_filedir}/ocaml-ppxlib-tools.list
%files -n ocaml-ppxlib-devel -f %{oreon_filedir}/ocaml-ppxlib-devel.list

%changelog

%autochangelog
