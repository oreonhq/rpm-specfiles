%global source0_hash 10c4d1a162a8f51eecf35d68118a96aa5f375350ff3abb357b41968faa7b4ef3

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-ppxlib-jane
Version:        0.17.4
Release:        %autorelease
Summary:        Utilities for working with Jane Street AST constructs

License:        MIT
URL:            https://github.com/janestreet/ppxlib_jane
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/ppxlib_jane-%{version}.tar.gz

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  ocaml >= 5.3.0
BuildRequires:  ocaml-dune >= 3.11.0
BuildRequires:  ocaml-ppxlib-devel >= 0.36.0

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

%autosetup -n ppxlib_jane-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
