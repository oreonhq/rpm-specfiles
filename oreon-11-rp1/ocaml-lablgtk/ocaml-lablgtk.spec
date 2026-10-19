%global source0_hash b3b746d4aa8a2bf7d63b1eca9f5319aac0c1888c5c54cf0581f8d895fd78c277
ExcludeArch: %{ix86}
%global giturl  https://github.com/garrigue/lablgtk
Name:           ocaml-lablgtk
Version:        2.18.14
Release:        1%{?dist}
Summary:        Objective Caml interface to gtk+
License:        LGPL-2.0-only WITH OCaml-LGPL-linking-exception AND LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://garrigue.github.io/lablgtk/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/%{version}/lablgtk-%{version}.tar.gz
Patch:          %{name}-svgz.patch
Patch:          %{name}-unix.patch
%global __ocaml_requires_opts -i GtkSourceView2_types
# oreon:deps
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp-streams-devel
BuildRequires:  ocaml-findlib
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
# /oreon:deps
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
sed -e '/native/d' \
    -e '/exists_if/s/,[[:alnum:]]*\.cmxa,[[:alnum:]]*\.cmxs//' \
    -e '/exists_if/s/,[[:alnum:]]*\.cmx//' \
    META > $RPM_BUILD_ROOT%{ocamldir}/lablgtk2/META
touch -r META $RPM_BUILD_ROOT%{ocamldir}/lablgtk2/META
%endif
rm $RPM_BUILD_ROOT%{ocamldir}/ld.conf
pushd $RPM_BUILD_ROOT%{ocamldir}/lablgtk2
for f in *.ml; do \
  b=`basename $f .ml`; \
  if [ -f "$b.mli" ]; then \
    rm $f; \
  fi; \
done
popd
find examples -name .cvsignore -delete
export LD_LIBRARY_PATH=$PWD/src
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
cp -p src/lablgladecc src/lablgladecc2
for bin in gdk_pixbuf_mlsource lablgladecc2 lablgtk2; do
  help2man -N --version-string=%{version} src/$bin > \
    $RPM_BUILD_ROOT%{_mandir}/man1/$bin.1
done
%ocaml_files
sed -i '/propcc/d;/varcc/d' .ofiles
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ocaml-lablgtk-devel -f %{oreon_filedir}/ocaml-lablgtk-devel.list

%changelog

%autochangelog
