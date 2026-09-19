%global source0_hash edb489710f5f937e69c7c11bb165fca91595d35059990c877c79f292b3e00851

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-sedlex
Version:        3.7
Release:        3%{?dist}
Summary:        Unicode-friendly lexer generator

License:        MIT
URL:            https://github.com/ocaml-community/sedlex
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Use local Unicode files instead of attempting to download them
Patch:          %{name}-no-curl.patch

BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ppxlib-devel
BuildRequires:  ocaml-ppx-expect-devel
BuildRequires:  ocaml-gen-devel
BuildRequires:  unicode-ucd

%description
A lexer generator for OCaml, similar to ocamllex, but supporting Unicode.
Contrary to ocamllex, lexer specifications for sedlex are embedded in
regular OCaml source files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-ppxlib-devel%{?_isa}
Requires:       ocaml-gen-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n sedlex-%{version}

# Upstream's regression test is written for Unicode 16.0.0.  Our Unicode files
# may be from a more recent version of the standard.  The test has a good
# chance of succeeding anyway, so we cross our fingers and give it a try.
# If the regression test fails, we'll have to try another approach.
univer=$(sed -n 's/.*PropList-\([.[:digit:]]*\)\.txt/\1/p' %{_datadir}/unicode/ucd/PropList.txt)
sed -i "s/16\\.0\\.0/$univer/" examples/regressions.ml examples/unicode_old.ml \
  src/generator/data/base_url src/syntax/unicode.ml

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc README.md CHANGES.md
%license LICENSE

%files devel -f .ofiles-devel
%doc README.md CHANGES.md
%license LICENSE

%changelog
%autochangelog
