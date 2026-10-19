%global source0_hash b0956210863cc24f480203ba3c2ef06dfae5579536a05744364e7de58822b230
ExcludeArch: %{ix86}
%global giturl  https://github.com/backtracking/ocamlgraph
Name:           ocaml-ocamlgraph
Version:        2.2.0
Release:        1%{?dist}
Summary:        OCaml library for arc and node graphs
License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception
URL:            https://backtracking.github.io/ocamlgraph/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/%{version}/ocamlgraph-%{version}.tbz
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-graphics-devel
BuildRequires:  ocaml-lablgtk-devel
BuildRequires:  pkgconfig(libgnomecanvas-2.0)
# /oreon:deps
%description
Ocamlgraph provides several different implementations of graph data
structures.  It also provides implementations for a number of classical graph
algorithms like Kruskal's algorithm for MSTs, topological ordering of DAGs,
Dijkstra's shortest paths algorithm, and Ford-Fulkerson's maximal-flow
algorithm to name a few.  The algorithms and data structures are written
functorially for maximal reusability.  Also has input and output capability
for Graph Modeling Language file format and Dot and Neato graphviz (graph
visualization) tools.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        gtk
Summary:        Display graphs using OCamlGraph and GTK2
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    gtk
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        gtk-devel
Summary:        Development files for %{name}-gtk
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-gtk%{?_isa} = %{version}-%{release}
Requires:       ocaml-lablgtk-devel%{?_isa}
Requires:       libgnomecanvas-devel%{?_isa}
%description    gtk-devel
The %{name}-gtk-devel package contains libraries and signature files for
developing applications that use %{name}-gtk.

%package        tools
Summary:        Graph editing tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    tools
The %{name}-tools package contains graph editing tools for use with
%{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n ocamlgraph-%{version}

%conf
# Fix encoding
for fil in COPYING TODO.md; do
  iconv -f latin1 -t utf-8 $fil > $fil.utf8
  touch -r $fil $fil.utf8
  mv -f $fil.utf8 $fil
done

%build

%dune_build @default editor
%install
%dune_install -s
mkdir -p %{buildroot}%{_bindir}
install -m 0755 -p _build/default/editor/editor.exe \
        %{buildroot}/%{_bindir}/ocamlgraph-editor
install -m 0755 -p _build/default/editor/ed_main.exe \
        %{buildroot}/%{_bindir}/ocamlgraph-ed_main
install -m 0755 -p _build/default/editor/graphEdGTK.exe \
        %{buildroot}/%{_bindir}/graphEdGTK
install -m 0755 -p _build/default/dgraph/dGraphViewer.exe \
        %{buildroot}%{_bindir}/dGraphViewer
install -m 0755 -p _build/default/view_graph/viewGraph_test.exe \
        %{buildroot}%{_bindir}/ocamlgraph-viewgraph
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%dune_check
%files -f %{oreon_filedir}/main.list
%files -n ocaml-ocamlgraph-devel -f %{oreon_filedir}/ocaml-ocamlgraph-devel.list
%files -n ocaml-ocamlgraph-gtk -f %{oreon_filedir}/ocaml-ocamlgraph-gtk.list
%files -n ocaml-ocamlgraph-gtk-devel -f %{oreon_filedir}/ocaml-ocamlgraph-gtk-devel.list
%files -n ocaml-ocamlgraph-tools -f %{oreon_filedir}/ocaml-ocamlgraph-tools.list

%changelog

%autochangelog
