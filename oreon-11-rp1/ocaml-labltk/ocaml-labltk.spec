%global source0_hash f816031d6fa024a7ff8cf768205ff24c528ae2c69eca86ad7d7b5ddab4e16022
%undefine _package_note_flags
ExcludeArch: %{ix86}
%global giturl https://github.com/garrigue/labltk
Name:          ocaml-labltk
Version:       8.06.16
Release:        1%{?dist}
Summary:        Tcl/Tk interface for OCaml
License:       LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:           https://garrigue.github.io/labltk/
VCS:           git:%{giturl}.git
Source0:        https://github.com/garrigue/labltk/archive/refs/tags/8.06.16.tar.gz#/labltk-8.06.15.tar.gz
Patch1:        labltk-8.06.11-enable-debugging.patch
Patch2:        labltk-8.06.12-use-fpic-configure.patch
%global _desc %{expand:
labltk or mlTk is a library for interfacing OCaml with the scripting
language Tcl/Tk (all versions since 8.0.3, but no betas).}
# oreon:deps
BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
# /oreon:deps
%description %_desc

%package devel
Summary:       Tcl/Tk interface for OCaml
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      tcl-devel%{?_isa}
Requires:      tk-devel%{?_isa}
%description devel %_desc

This package contains the development files.

%package doc
Summary:       Documentation for labltk
BuildArch:     noarch
%description doc %_desc

This package contains the API reference.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n labltk-%{version} -p1

# Remove version control files which might get copied into documentation.
find -name .gitignore -delete

# Don't build ocamlbrowser.
mv browser browser.old
mkdir browser
echo -e 'all:\ninstall:\n' > browser/Makefile

# Use of the hardening linker flags without the hardening C flags leads to
# failure of the configure script.  We don't need linker flags for this step.
sed -i 's/^cclibs=.*/cclibs=/' configure

%build

./configure -verbose
unset MAKEFLAGS
%ifarch %{ocaml_native_compiler}
make all opt \
     SHAREDCCCOMPOPTS='%{build_cflags} -fPIC' \
     TK_LINK="%{build_ldflags} $(pkg-config --libs tk)"
%else
make byte
%endif
MLIS=$(ls -1d labltk/*.mli | grep -Fv _tkgen.mli)
mkdir apiref
/usr/bin/ocamldoc -I +unix -I +threads -I support -I labltk -I camltk \
  support/fileevent.mli support/support.mli support/textvariable.mli \
  support/timer.mli support/tkthread.mli support/widget.mli $MLIS \
  labltk/tk.ml -sort -d apiref -html
%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/ocaml/labltk
mkdir -p $RPM_BUILD_ROOT%{_libdir}/ocaml/stublibs
make install \
    BINDIR=$RPM_BUILD_ROOT%{_bindir} \
    INSTALLDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml/labltk \
    STUBLIBDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml/stublibs \
    RANLIB=:
sed 's/8\.06\.6/%{version}/' support/META > \
    $RPM_BUILD_ROOT%{ocamldir}/labltk/META
%ocaml_files
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ocaml-labltk-devel -f %{oreon_filedir}/ocaml-labltk-devel.list
%files -n ocaml-labltk-doc -f %{oreon_filedir}/ocaml-labltk-doc.list

%changelog

%autochangelog
