%global source0_hash 85377cbac10a1b2fafd0fc0cc8394d958d5b1da14cada3e1c93fc2c3ecabec7e
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
Name:           not-ocamlfind
Version:        0.15
Release:        1%{?dist}
Summary:        Front-end to ocamlfind that adds a few new commands
License:        MIT
URL:            https://github.com/chetmurthy/not-ocamlfind
VCS:            git:%{url}.git
Source0:        https://github.com/chetmurthy/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
Requires:       ocaml-findlib%{?_isa}
Recommends:     %{py3_dist xdot}
# oreon:deps
BuildRequires:  m4
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp-streams-devel
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-fmt-devel
BuildRequires:  ocaml-ocamlgraph-devel
BuildRequires:  ocaml-rresult-devel
BuildRequires:  which
# /oreon:deps
%description
The command not-ocamlfind is a pass-thru to ocamlfind, but adds three new
commands: preprocess, reinstall-if-diff and package-graph.

- reinstall-if-diff does what it says on the label: only reinstalls (remove
  then install) if the file-content of the package has changed.

- preprocess produces the source and does not attempt to compile it; as an
  added benefit, it prints (to stderr) the commands it executed to produce
  that source.   So you can use this for debugging multi-stage PPX rewriter
  sequences.

- package-graph outputs a graph in the format accepted by the dot command of
  graphviz.  By default you get the package-dependency graph, with sizes of
  the archives for each packages as part of the node-label.  If you add
  `-dominator-from <node>`, it will compute the dominator-tree from that node,
  and if you add `-xdot`, it will automatically invoke xdot on the graph.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%ifarch %{ocaml_native_compiler}
ocamlfind ocamlopt \
  -I +findlib findlib.cmxa \
%else
ocamlfind ocamlc \
  -I +findlib findlib.cma \
%endif
  -g \
  -package str,unix,fmt,rresult,ocamlgraph,camlp-streams \
  -linkall \
  -linkpkg \
  fsmod.ml frontend.ml main.ml \
  -o not-ocamlfind
%ifarch %{ocaml_native_compiler}
ocamlfind ocamlopt \
  -I +findlib findlib.cmxa \
%else
ocamlfind ocamlc \
  -I +findlib findlib.cma \
%endif
  -g \
  -package str,unix,compiler-libs.common \
  -linkall \
  -linkpkg \
  papr_official.ml \
  -o papr_official.exe
%install
mkdir -p %{buildroot}%{_bindir}
cp -p not-ocamlfind %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{ocamldir}/not-ocamlfind
cp -p META opam papr_official.exe %{buildroot}%{ocamldir}/not-ocamlfind
%oreon_autofiles main

%check

./not-ocamlfind package-graph -predicates true -package findlib
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
