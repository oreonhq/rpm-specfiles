%global source0_hash 35cd03fc4193969b1cce01190340e5c129c1ba8f02242a9e6dff4b83be118759
%bcond test 0
%global giturl  https://github.com/rocq-prover/rocq
Name:           rocq
Version:        9.2.0
Release:        1%{?dist}
Summary:        Proof management system
License:        LGPL-2.1-only AND LGPL-2.1-only WITH OCaml-LGPL-linking-exception AND MIT AND BSD-3-Clause
URL:            https://rocq-prover.org/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/V%{version}/%{name}-%{version}.tar.gz
Source1:        org.rocq-prover.rocqide.desktop
Source2:        org.rocq-prover.rocqide.metainfo.xml
Source3:        rocq.xml
Patch:          %{name}-mathlib.patch
Patch:          %{name}-no-generated-readme.patch
ExclusiveArch:  %{ocaml_native_compiler}
%if %{with test}
%endif
Requires:       %{name}-runtime%{_isa} = %{version}-%{release}
Requires:       %{name}-core%{_isa} = %{version}-%{release}
Requires:       csdp-tools
Requires:       ocaml-findlib
Recommends:     emacs-proofgeneral
Recommends:     rocq-stdlib
Recommends:     texlive-collection-latex
Provides:       coq = %{version}-%{release}
Obsoletes:      coq < 9.2.0
%global _desc %{expand:Rocq is a formal proof management system.  It provides a formal language to
write mathematical definitions, executable algorithms and theorems together
with an environment for semi-interactive development of machine-checked proofs.}
# oreon:deps
BuildRequires:  adwaita-icon-theme
BuildRequires:  antlr4
BuildRequires:  csdp-tools
BuildRequires:  desktop-file-utils
BuildRequires:  findutils
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-cairo-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-lablgtk3-sourceview3-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-ounit2-devel
BuildRequires:  ocaml-yojson-devel
BuildRequires:  ocaml-zarith-devel
BuildRequires:  ocaml-zip-devel
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx-latex
BuildRequires:  python3.15dist(antlr4-python3-runtime)
BuildRequires:  python3.15dist(beautifulsoup4)
BuildRequires:  python3.15dist(pexpect)
BuildRequires:  python3.15dist(sphinx)
BuildRequires:  python3.15dist(sphinx-rtd-theme)
BuildRequires:  python3.15dist(sphinxcontrib-bibtex)
BuildRequires:  rocq-stdlib
BuildRequires:  rsync
BuildRequires:  tex(adjustbox.sty)
BuildRequires:  tex(amssymb.sty)
BuildRequires:  tex(array.sty)
BuildRequires:  tex(fontenc.sty)
BuildRequires:  tex(fullpage.sty)
BuildRequires:  tex(ifpdf.sty)
BuildRequires:  tex(inputenc.sty)
BuildRequires:  tex(microtype.sty)
BuildRequires:  tex(polyglossia.sty)
BuildRequires:  tex(unicode-math.sty)
BuildRequires:  tex(verbatim.sty)
BuildRequires:  tex(xr.sty)
BuildRequires:  time
# /oreon:deps
%description
%_desc

Typical applications include the certification of properties of programming
languages (e.g., the CompCert compiler certification project, or the Bedrock
verified low-level programming library), the formalization of mathematics
(e.g., the full formalization of the Feit-Thompson theorem or homotopy type
theory) and teaching.

%package        runtime
Summary:        Core binaries and tools of the Rocq proof management system
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       coq-core = %{version}-%{release}
Obsoletes:      coq-core < 9.2.0
%description    runtime
%_desc

This package includes the Rocq prover core binaries, plugins, and tools, but
not the vernacular standard library.

%package        runtime-devel
Summary:        Development files for %{name}-runtime
Requires:       %{name}-runtime%{?_isa} = %{version}-%{release}
%description    runtime-devel
%_desc

The %{name}-runtime-devel package contains libraries and signature files
for developing applications that use %{name}-runtime.

%package        core
Summary:        The Rocq Prelude, and the Corelib and Ltac2 modules
Requires:       %{name}-runtime%{?_isa} = %{version}-%{release}
Provides:       coq = %{version}-%{release}
Obsoletes:      coq < 9.2.0
%description    core
%_desc

This package includes the Rocq prelude, that is loaded automatically
by Rocq in every .v file, as well as other modules bound to the
Corelib.* and Ltac2.* namespaces.

%package        core-source
Summary:        Source files of the Rocq Prelude, and the Corelib and Ltac2 modules
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
%description    core-source
%_desc

This package contains the source Rocq files for the Rocq Prelude, and the
Corelib and Ltac2 modules.  These files are not needed to use the Rocq Prelude,
and the Corelib and Ltac2 modules.  They are made available for informational
purposes.

%package     -n coq-core-compat
Summary:        Compatibility binaries for Coq after the Rocq renaming
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Provides:       coq-core = %{version}-%{release}
Obsoletes:      coq-core < 9.2.0
%description -n coq-core-compat
%_desc

This package includes compatibility binaries to call Rocq
through previous Coq commands like coqc coqtop,...

%package        coqide-server
Summary:        The coqidetop language server
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Provides:       coq-coqide-server = %{version}-%{release}
Obsoletes:      coq-coqide-server < 9.2.0
%description    coqide-server
%_desc

This package provides the coqidetop language server, an implementation of
Rocq's XML protocol which allows clients, such as RocqIDE, to interact with
Rocq in a structured way.

%package        coqide-server-devel
Summary:        Development files for %{name}-coqide-server
Requires:       %{name}-coqide-server%{?_isa} = %{version}-%{release}
%description    coqide-server-devel
%_desc

The %{name}-coqide-server-devel package contains libraries and signature files
for developing applications that use %{name}-coqide-server.

%package        rocqide
License:        LGPL-2.1-only AND LGPL-2.1-or-later
Summary:        RocqIDE for the Rocq proof management system
Requires:       %{name}-coqide-server%{?_isa} = %{version}-%{release}
Requires:       adwaita-icon-theme
Requires:       hicolor-icon-theme
Requires:       xdg-utils
Provides:       coq-coqide = %{version}-%{release}
Obsoletes:      coq-coqide < 9.2.0
Provides:       bundled(ocaml-xml-light)
%description    rocqide
%_desc

This package provides RocqIDE, a graphical user interface for the
development of interactive proofs.

%package        doc
Summary:        Documentation for the Rocq proof management system
License:        OPUBL-1.0 AND LGPL-2.1-only AND MIT
BuildArch:      noarch
Requires:       font(fontawesome)
Requires:       font(lato)
Requires:       font(robotoslab)
Provides:       coq-doc = %{version}-%{release}
Obsoletes:      coq-doc < 9.2.0
%description    doc
%_desc

This package provides documentation and tutorials for the system.  The
main documentation comes in two parts: the main Library documentation,
which describes all Corelib.* modules, and the Reference Manual, which
gives a more complete description of the whole system. Included are
HTML versions of both and a PDF version of the Reference Manual.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
fixtimestamp() {
    touch -r $1.orig $1
    rm -f $1.orig
}

# Use Fedora flags
sed -e 's|-Wall.*-O2|%{build_cflags} %{build_ldflags} -Wno-unused|' \
    -i tools/configure/configure.ml

# Make sure debuginfo is generated
sed -i 's,-shared,& -g,g' tools/CoqMakefile.in

# Do not invoke env
for f in doc/tools/coqrst/notations/fontsupport.py;
do
  sed -i.orig 's,/usr/bin/env python2,%{python3},' $f
  fixtimestamp $f
done
for f in $(grep -Frl '%{_bindir}/env'); do
  sed -r -i.orig 's,(%{_bindir}/)env[[:blank:]]+([[:alnum:]]+),\1\2,g' $f
  fixtimestamp $f
done

%build

%global rocqdocdir %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/rocq-%{version}}
cd doc/tools/coqrst/notations
antlr4 -Dlanguage=Python3 -visitor -no-listener TacticNotations.g
cd -
./configure -prefix %{_prefix}                       \
            -libdir %{ocamldir}/coq                  \
            -configdir %{_sysconfdir}/xdg/%{name}    \
            -mandir %{_mandir}                       \
            -docdir %{rocqdocdir}                    \
%ifarch %{ocaml_natdynlink}
            -natdynlink yes                          \
%else
            -natdynlink no                           \
%endif
            -browser "xdg-open %s"                   \
            -bytecode-compiler yes                   \
            -native-compiler no
make dunestrap VERBOSE=1 DUNEOPT="--verbose --profile=release"
%dune_build %{!?_with_test:-p rocq-runtime,rocq-core,coq-core,coqide-server,rocqide}
export ROCQLIB=${PWD}/_build/install/default/lib/coq
export SPHINXWARNOPT="-w$PWD/sphinx-warn.log"
%dune_build @refman-html @refman-pdf @corelib-html
%install
%dune_install %{!?_with_test:rocq-runtime rocq-core coq-core coqide-server rocqide}
mkdir -p %{buildroot}%{_texmf_main}/tex/latex/misc
mv %{buildroot}%{_datadir}/texmf/tex/latex/misc/coqdoc.sty \
   %{buildroot}%{_texmf_main}/tex/latex/misc
rm -fr %{buildroot}%{_datadir}/texmf
mkdir -p %{buildroot}%{_sysconfdir}/xdg/%{name}
find _build/default/doc -name .buildinfo -delete
rm -fr _build/default/doc/refman-html/.doctrees
mkdir -p %{buildroot}%{rocqdocdir}/refman-pdf
mv _build/default/doc/refman-pdf/rocq*.pdf %{buildroot}%{rocqdocdir}/refman-pdf/
mv _build/default/doc/refman-html %{buildroot}%{rocqdocdir}/refman-html
mv _build/default/doc/corelib/html %{buildroot}%{rocqdocdir}/corelib
mv _build/default/doc/corelib/_index.html %{buildroot}%{rocqdocdir}/corelib/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/mimetypes
cp --preserve=timestamps ide/rocqide/coq.png \
   %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/rocq.png
cp --preserve=timestamps ide/rocqide/coq.png \
   %{buildroot}%{_datadir}/icons/hicolor/256x256/mimetypes/rocqfile.png
mkdir -p %{buildroot}%{_datadir}/mime/packages
cp -p %{SOURCE3} %{buildroot}%{_datadir}/mime/packages
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE2} %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/org.rocq-prover.rocqide.metainfo.xml
mkdir -p %{buildroot}%{_datadir}/gtksourceview-3.0/language-specs
for fil in coq.lang coq-ssreflect.lang; do
  ln -s ../../coq/$fil %{buildroot}%{_datadir}/gtksourceview-3.0/language-specs
done
mkdir -p %{buildroot}%{_datadir}/gtksourceview-3.0/styles
ln -s ../../coq/coq_style.xml %{buildroot}%{_datadir}/gtksourceview-3.0/styles
%py_byte_compile %{python3} %{buildroot}%{ocamldir}/coq-core/tools
%ocaml_files -s
%oreon_autofiles coq-core-compat usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with test}
%check

%dune_check
%endif
%files -f %{oreon_filedir}/main.list
%files -n rocq-runtime -f %{oreon_filedir}/rocq-runtime.list
%files -n rocq-runtime-devel -f %{oreon_filedir}/rocq-runtime-devel.list
%files -n rocq-core -f %{oreon_filedir}/rocq-core.list
%files -n rocq-core-source -f %{oreon_filedir}/rocq-core-source.list
%files -n coq-core-compat -f %{oreon_filedir}/coq-core-compat.list
%files -n rocq-coqide-server -f %{oreon_filedir}/rocq-coqide-server.list
%files -n rocq-coqide-server-devel -f %{oreon_filedir}/rocq-coqide-server-devel.list
%files -n rocq-rocqide -f %{oreon_filedir}/rocq-rocqide.list
%files -n rocq-doc -f %{oreon_filedir}/rocq-doc.list

%changelog

%autochangelog
