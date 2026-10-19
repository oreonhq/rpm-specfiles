%global source0_hash 10c4d1a162a8f51eecf35d68118a96aa5f375350ff3abb357b41968faa7b4ef3
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           ocaml-ppxlib-jane
Version:        0.17.4
Release:        1%{?dist}
Summary:        Utilities for working with Jane Street AST constructs
License:        MIT
URL:            https://github.com/janestreet/ppxlib_jane
VCS:            git:%{url}.git
Source0:        https://github.com/janestreet/ppxlib_jane/archive/v%{version}/ppxlib_jane-%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppxlib-devel
# /oreon:deps
%description
A library for use in ppxes for constructing and matching on ASTs corresponding
to the augmented parsetree that is recognized by the Jane Street OCaml
compiler (flambda).

ASTs constructed using this library are compatible with the standard OCaml
compiler.  Any syntax change known to this library is encoded as attributes,
and the standard OCaml compiler's interpretation of the ASTs constructed by
these library (which amounts to ignoring the attributes) is reasonable.  That
is, we only expose "unsurprising" things in this library.  For example, if you
construct an *n*-ary function using this library, the standard OCaml compiler
will interpret it as *n* nested unary functions in the normal way.

Likewise, ppxes that use this library to match on Jane Street ASTs can also be
used with the standard OCaml compiler.  (The Jane Street AST cases of the
match will just never be triggered when using the standard OCaml compiler.)

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppxlib-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir ppxlib_jane-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-ppxlib-jane-devel -f %{oreon_filedir}/ocaml-ppxlib-jane-devel.list

%changelog

%autochangelog
