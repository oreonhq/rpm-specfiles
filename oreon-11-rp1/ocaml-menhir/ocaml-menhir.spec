%global source0_hash 06f6e571aadd7d66cc3da808052d9a65f8be96fe27e0ad7e57bbbf8c20f4a832
%bcond manual %[!0%{?rhel}]
%global giturl  https://gitlab.inria.fr/fpottier/menhir
Name:           ocaml-menhir
Version:        20260209
Release:        1%{?dist}
Summary:        LR(1) parser generator for OCaml
License:        GPL-2.0-only
URL:            https://gallium.inria.fr/~fpottier/menhir/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/-/archive/%{version}/menhir-%{version}.tar.bz2
ExcludeArch:    %{ix86}
%if %{with manual}
%endif
Provides:       bundled(ocaml-fix) = 20250919
Provides:       bundled(ocaml-pprint) = 20230830
Requires:       ocaml-menhirlib-devel%{?_isa} = %{version}-%{release}
Obsoletes:      coq-menhirlib < 20230608-1
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  hevea
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  tex(latex)
BuildRequires:  tex(moreverb.sty)
BuildRequires:  tex(stmaryrd.sty)
BuildRequires:  texlive-times
# /oreon:deps
%description
Menhir is a LR(1) parser generator for the Objective Caml programming
language.  That is, Menhir compiles LR(1) grammar specifications down to OCaml
code.  Menhir was designed and implemented by François Pottier and Yann
Régis-Gianas.

%package     -n ocaml-menhirlib
Summary:        Runtime library for parsers produced by Menhir
License:        LGPL-2.0-only WITH OCaml-LGPL-linking-exception
%description -n ocaml-menhirlib
This package contains the runtime library for parsers produced by Menhir.

%package     -n ocaml-menhirlib-devel
Summary:        Development files for ocaml-menhirlib
License:        LGPL-2.0-only WITH OCaml-LGPL-linking-exception
Requires:       ocaml-menhirlib%{?_isa} = %{version}-%{release}
%description -n ocaml-menhirlib-devel
This ocaml-menhirlib-devel package contains libraries and signature files for
building applications with a parser produced by Menhir.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir menhir-%{version}
%oreon_prep
%build

%dune_build
%if %{with manual}
cd doc
rm manual.pdf
pdflatex -interaction=nonstopmode manual
bibtex manual
pdflatex -interaction=nonstopmode manual
pdflatex -interaction=nonstopmode manual
pdflatex -interaction=nonstopmode manual
cd -
%endif
%install
%dune_install -s
cp -p _build/default/lib/pack/menhirLib.ml %{buildroot}%{ocamldir}/menhirLib
rm -rf %{buildroot}%{ocamldir}/coq-menhirlib/
cat > %{buildroot}%{ocamldir}/menhir/META << EOF
version = "%{version}"
description = "Menhir command-line tool"
requires = ""
EOF
%oreon_autofiles ocaml-menhirlib usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ocaml-menhirlib-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ocaml-menhirlib -f %{oreon_filedir}/ocaml-menhirlib.list
%files -n ocaml-menhirlib-devel -f %{oreon_filedir}/ocaml-menhirlib-devel.list

%changelog

%autochangelog
