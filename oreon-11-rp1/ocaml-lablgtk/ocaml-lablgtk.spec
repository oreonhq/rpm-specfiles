%global source0_hash b3b746d4aa8a2bf7d63b1eca9f5319aac0c1888c5c54cf0581f8d895fd78c277

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global giturl  https://github.com/garrigue/lablgtk

Name:           ocaml-lablgtk
Version:        2.18.14
Release:        5%{?dist}

Summary:        Objective Caml interface to gtk+

# The project as a whole is LGPL-2.0-only.  LGPL-2.1-or-later files:
# - src/gtkSourceView2_types.mli
# - src/introspection/xml-light/* (not included in the binary RPM)
License:        LGPL-2.0-only WITH OCaml-LGPL-linking-exception AND LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception

URL:            https://garrigue.github.io/lablgtk/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}/lablgtk-%{version}.tar.gz
# Provide a definition of ml_rsvg_handle_new_gz for newer versions of librsvg
# which do not explicitly expose an SVGZ interface.
Patch:          %{name}-svgz.patch
# Adapt to new paths to Unix library in OCaml 5.1.0
Patch:          %{name}-unix.patch

BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  ocaml >= 4.06
BuildRequires:  ocaml-camlp-streams-devel
BuildRequires:  ocaml-findlib >= 1.2.1
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtksourceview-2.0)
BuildRequires:  pkgconfig(gtkspell-2.0)
BuildRequires:  pkgconfig(libglade-2.0)
BuildRequires:  pkgconfig(libgnomecanvas-2.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(zlib)

%global __ocaml_requires_opts -i GtkSourceView2_types

%description
LablGTK is an Objective Caml interface to gtk2.

It uses the rich type system of Objective Caml to provide a strongly typed,
yet very comfortable, object-oriented interface to gtk2.  This is not that
easy if you know the dynamic typing approach taken by gtk2.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gtk2-devel%{?_isa}

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n lablgtk-%{version} -p1

# Remove spurious executable bits
chmod a-x README*

%build
# Parallel builds don't work.
unset MAKEFLAGS
%configure --without-gnomeui
sed -e "s|-O|%{build_cflags}|" \
    -e "s|-shared|& -ccopt '%{build_ldflags}'|" \
    -e "s|(CAMLMKLIB)|& -ldopt '%{build_ldflags}'|" \
    -e "s|-warn-error [-A-Za-z0-9]\+||" \
    -i src/Makefile
%ifarch %{ocaml_native_compiler}
make world CAMLOPT="ocamlopt.opt -g" CAMLC="ocamlc.opt -g"
%else
make world CAMLC="ocamlc -g"
%endif

%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{ocamldir}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{ocamldir}/lablgtk2
mkdir -p $RPM_BUILD_ROOT%{ocamldir}/stublibs
make install \
     RANLIB=true \
     BINDIR=$RPM_BUILD_ROOT%{_bindir} \
     LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
     INSTALLDIR=$RPM_BUILD_ROOT%{ocamldir}/lablgtk2 \
     DLLDIR=$RPM_BUILD_ROOT%{ocamldir}/stublibs
%ifarch %{ocaml_native_compiler}
cp -p META $RPM_BUILD_ROOT%{ocamldir}/lablgtk2
%else
# Do not require the native artifacts
sed -e '/native/d' \
    -e '/exists_if/s/,[[:alnum:]]*\.cmxa,[[:alnum:]]*\.cmxs//' \
    -e '/exists_if/s/,[[:alnum:]]*\.cmx//' \
    META > $RPM_BUILD_ROOT%{ocamldir}/lablgtk2/META
touch -r META $RPM_BUILD_ROOT%{ocamldir}/lablgtk2/META
%endif

# Remove ld.conf (part of main OCaml dist).
rm $RPM_BUILD_ROOT%{ocamldir}/ld.conf

# Remove unnecessary *.ml files (ones which have a *.mli).
pushd $RPM_BUILD_ROOT%{ocamldir}/lablgtk2
for f in *.ml; do \
  b=`basename $f .ml`; \
  if [ -f "$b.mli" ]; then \
    rm $f; \
  fi; \
done
popd

# Remove .cvsignore files from examples directory.
find examples -name .cvsignore -delete

# Generate man pages
export LD_LIBRARY_PATH=$PWD/src
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
cp -p src/lablgladecc src/lablgladecc2
for bin in gdk_pixbuf_mlsource lablgladecc2 lablgtk2; do
  help2man -N --version-string=%{version} src/$bin > \
    $RPM_BUILD_ROOT%{_mandir}/man1/$bin.1
done

%ocaml_files

# Move two files from the main package to the devel package
sed -i '/propcc/d;/varcc/d' .ofiles

%files -f .ofiles

%files devel -f .ofiles-devel
%doc CHANGES.API
%{ocamldir}/lablgtk2/propcc
%{ocamldir}/lablgtk2/varcc

%changelog
%autochangelog
