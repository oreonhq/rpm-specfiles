%global source0_hash 1a14dd04bb4379a41990248550628c77913a9c07f3c35c1370b6960e697787ff
ExcludeArch: %{ix86}
%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif
%bcond dune 0
%global giturl  https://github.com/ocaml-dune/csexp
Name:           ocaml-csexp
Version:        1.5.2
Release:        1%{?dist}
Summary:        Parsing and printing of S-expressions in canonical form
License:        MIT
URL:            https://ocaml-dune.github.io/csexp/
VCS:            git:%{giturl}.git
Source0:        https://github.com/ocaml-dune/csexp/releases/download/1.5.2/csexp-1.5.2.tbz
Patch:        https://github.com/ocaml-dune/csexp/commit/07eb898.patch
%if %{with dune}
%else
%endif
# oreon:deps
BuildRequires:  ocaml
BuildRequires:  ocaml-rpm-macros
# /oreon:deps
%description
This project provides minimal support for parsing and printing S-expressions
in canonical form, which is a very simple and canonical binary encoding of
S-expressions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir csexp-%{version}
%oreon_prep
%build

%if %{with dune}
%dune_build
%else
OFLAGS="-w -40 -g"
OCFLAGS="$OFLAGS -bin-annot"
cd src
ocamlc $OCFLAGS -no-alias-deps -o csexp.cmi -c -intf csexp.mli
ocamlc $OCFLAGS -intf-suffix .ml -no-alias-deps -o csexp.cmo -c -impl csexp.ml
ocamlc $OFLAGS -a -o csexp.cma csexp.cmo
%ifarch %{ocaml_native_compiler}
ocamlopt $OFLAGS -intf-suffix .ml -no-alias-deps -o csexp.cmx -c -impl csexp.ml
ocamlopt $OFLAGS -a -o csexp.cmxa csexp.cmx
ocamlopt $OFLAGS -shared -linkall -I . -o csexp.cmxs csexp.cmxa
%endif
%endif
%install
%if %{with dune}
%dune_install
%else
mkdir -p %{buildroot}%{ocamldir}/csexp
cp -p src/csexp.{cma,cmi,cmt,cmti,mli} %{buildroot}%{ocamldir}/csexp
%ifarch %{ocaml_native_compiler}
cp -p src/csexp.{a,cmx,cmxa,cmxs} %{buildroot}%{ocamldir}/csexp
%endif
cp -p csexp.opam %{buildroot}%{ocamldir}/csexp/opam
cat >> %{buildroot}%{ocamldir}/csexp/META << EOF
version = "%{version}"
description = "Parsing and printing of S-expressions in canonical form"
requires = ""
archive(byte) = "csexp.cma"
%ifarch %{ocaml_native_compiler}
archive(native) = "csexp.cmxa"
%endif
plugin(byte) = "csexp.cma"
%ifarch %{ocaml_native_compiler}
plugin(native) = "csexp.cmxs"
%endif
EOF
cat >> %{buildroot}%{ocamldir}/csexp/dune-package << EOF
(lang dune 3.20)
(name csexp)
(version %{version})
(sections (lib .) (libexec .) (doc ../../doc/csexp))
(files
 (lib
  (META
   csexp.a
   csexp.cma
   csexp.cmi
   csexp.cmt
   csexp.cmti
   csexp.cmx
%ifarch %{ocaml_native_compiler}
   csexp.cmxa
%endif
   csexp.ml
   csexp.mli
   dune-package
   opam))
%ifarch %{ocaml_native_compiler}
 (libexec (csexp.cmxs))
%endif
 (doc (CHANGES.md LICENSE.md README.md)))
(library
 (name csexp)
 (kind normal)
%ifarch %{ocaml_native_compiler}
 (archives (byte csexp.cma) (native csexp.cmxa))
 (plugins (byte csexp.cma) (native csexp.cmxs))
 (native_archives csexp.a)
%else
 (archives (byte csexp.cma))
 (plugins (byte csexp.cma))
%endif
 (main_module_name Csexp)
%ifarch %{ocaml_native_compiler}
 (modes byte native)
%else
 (modes byte)
%endif
 (modules
  (singleton
   (obj_name csexp)
   (visibility public)
   (source (path Csexp) (intf (path csexp.mli)) (impl (path csexp.ml))))))
EOF
%ocaml_files
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n ocaml-csexp-devel -f %{oreon_filedir}/ocaml-csexp-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.2-19
- Prepare for Oreon 11 (RP1)
