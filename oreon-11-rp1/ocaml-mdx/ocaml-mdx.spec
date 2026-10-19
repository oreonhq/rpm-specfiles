%global source0_hash dd82980dd111a4806ff9a91d9d2ed7c26aefb1da7dccbd15e73c3a8f66e863f5
ExcludeArch: %{ix86}
%global giturl  https://github.com/realworldocaml/mdx
Name:           ocaml-mdx
Version:        2.6.0
Release:        1%{?dist}
Summary:        Executable code blocks inside markdown files
License:        ISC
URL:            https://realworldocaml.github.io/mdx/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/%{version}/mdx-%{version}.tbz
Provides:       bundled(ocaml-odoc-parser) = 2.3.0
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-astring-devel
BuildRequires:  ocaml-camlp-streams-devel
BuildRequires:  ocaml-cmdliner-devel
BuildRequires:  ocaml-cppo
BuildRequires:  ocaml-csexp-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-fmt-devel
BuildRequires:  ocaml-logs-devel
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-re-devel
BuildRequires:  ocaml-result-devel
BuildRequires:  ocaml-version-devel
# /oreon:deps
%description
mdx enables execution of code blocks inside markdown files.  There are
(currently) two sub-commands, corresponding to two modes of operation:
preprocessing (`ocaml-mdx pp`) and tests (`ocaml-mdx test`).

The preprocessor mode enables mixing documentation and code, and the practice
of "literate programming" using markdown and OCaml.

The test mode enables ensuring that shell scripts and OCaml fragments in the
documentation always stay up-to-date.

The blocks in markdown files can be parameterized by `mdx`-specific labels,
that will change the way `mdx` interprets the block.  The syntax is:
`<!-- $MDX labels -->`, where `labels` is a list of valid labels separated by
a comma.  This line must immediately precede the block it is attached to.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-astring-devel%{?_isa}
Requires:       ocaml-camlp-streams-devel%{?_isa}
Requires:       ocaml-csexp-devel%{?_isa}
Requires:       ocaml-fmt-devel%{?_isa}
Requires:       ocaml-logs-devel%{?_isa}
Requires:       ocaml-re-devel%{?_isa}
Requires:       ocaml-result-devel%{?_isa}
Requires:       ocaml-version-devel%{?_isa}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir mdx-%{version}
%oreon_prep
%build

%dune_build
%install
%dune_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-mdx-devel -f %{oreon_filedir}/ocaml-mdx-devel.list

%changelog

%autochangelog
