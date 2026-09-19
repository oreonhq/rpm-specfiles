%global source0_hash ad71f62406e9bb4e7fb5d4593ede2af6c68f8b0d96f25574446e142c3eb0d9a4

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           ocaml-camlp-streams
Version:        5.0.1
Release:        21%{?dist}
Summary:        Stream and Genlex libraries for OCaml

License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception
URL:            https://github.com/ocaml/camlp-streams
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/camlp-streams-%{version}.tar.gz

BuildRequires:  ocaml >= 4.02.3
BuildRequires:  ocaml-dune >= 2.7

%description
The camlp-streams package provides two library modules:
- Stream: imperative streams, with in-place update and memoization of the
  latest element produced.
- Genlex: a small parameterized lexical analyzer producing streams of tokens
  from streams of characters.

The two modules are designed for use with Camlp4 and Camlp5:
- The stream patterns and stream expressions of Camlp4/Camlp5 consume and
  produce data of type `'a Stream.t`.
- The Genlex tokenizer can be used as a simple lexical analyzer for
  Camlp4/Camlp5-generated parsers.

The Stream module can also be used by hand-written recursive-descent parsers,
but is not very convenient for this purpose.

The Stream and Genlex modules were part of the OCaml standard library for a
long time, and were distributed as part of the core OCaml system.  They were
removed from the OCaml standard library in version 5.0, but are maintained and
distributed separately in this camlp-streams package.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n camlp-streams-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE

%files devel -f .ofiles-devel

%changelog
%autochangelog
