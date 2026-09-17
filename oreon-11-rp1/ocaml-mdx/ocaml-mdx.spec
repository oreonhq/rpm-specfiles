%global source0_hash dd82980dd111a4806ff9a91d9d2ed7c26aefb1da7dccbd15e73c3a8f66e863f5

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global giturl  https://github.com/realworldocaml/mdx

Name:           ocaml-mdx
Version:        2.5.1
Release:        4%{?dist}
Summary:        Executable code blocks inside markdown files

License:        ISC
URL:            https://realworldocaml.github.io/mdx/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/%{version}/mdx-%{version}.tbz

BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-astring-devel
BuildRequires:  ocaml-camlp-streams-devel
BuildRequires:  ocaml-cmdliner-devel >= 1.1.0
BuildRequires:  ocaml-cppo >= 1.1.0
BuildRequires:  ocaml-csexp-devel >= 1.3.2
BuildRequires:  ocaml-dune >= 3.5
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-fmt-devel >= 0.8.7
BuildRequires:  ocaml-logs-devel >= 0.7.0
BuildRequires:  ocaml-lwt-devel
BuildRequires:  ocaml-re-devel >= 1.7.2
BuildRequires:  ocaml-result-devel >= 1.5
BuildRequires:  ocaml-version-devel >= 2.3.0

# odoc-parser has been merged back into odoc
# This package now vendors odoc-parser
Provides:       bundled(ocaml-odoc-parser) = 2.3.0

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

%autosetup -n mdx-%{version} -p1

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
