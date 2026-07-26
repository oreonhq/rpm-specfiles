%global source0_hash a3d10edbc4f98d16357b644d550fd1c06f4d9aa4990ab8ee6da01276c24d55b5

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-parsexp
Version:        0.17.0
Release:        %autorelease
Summary:        S-expression parsing library

License:        MIT
URL:            https://github.com/janestreet/parsexp
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/parsexp-%{version}.tar.gz

BuildRequires:  ocaml >= 5.1.0
BuildRequires:  ocaml-dune >= 3.11.0
BuildRequires:  ocaml-sexplib0-devel >= 0.17

%description
This library provides generic parsers for parsing S-expressions from strings
or other media.

The library is focused on performance but still provides full generic parsers
that can be used effortlessly with strings, bigstrings, lexing buffers,
character streams or any other source.

It provides three different classes of parsers:
- the normal parsers, producing `[Sexp.t]` or `[Sexp.t list]` values;
- the parsers with positions, building compact position sequences so that one
  can recover original positions in order to properly report error locations
  at little cost; and
- the Concrete Syntax Tree parsers, producing values of type `[Parsexp.Cst.t]`
  which record the concrete layout of the s-expression syntax, including
  comments.

This library is portable and doesn't provide I/O functions.  To read
s-expressions from files or other external sources, you should use parsexp_io.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-sexplib0-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n parsexp-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md README.org
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
