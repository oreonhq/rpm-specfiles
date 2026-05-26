# This breaks basic usage of the package:
# ocamlfind ocamlopt -package labltk tktest.ml -linkpkg -o tktest
# gcc: fatal error: environment variable ‘RPM_ARCH’ not defined
%undefine _package_note_flags

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%global giturl https://github.com/garrigue/labltk

Name:          ocaml-labltk
Version:       8.06.15
Release:       6%{?dist}

Summary:       Tcl/Tk interface for OCaml

License:       LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception

URL:           https://garrigue.github.io/labltk/
VCS:           git:%{giturl}.git
Source0:        https://github.com/garrigue/labltk/archive/8.06.15/labltk-8.06.15.tar.gz

# This adds debugging (-g) everywhere.
Patch1:        labltk-8.06.11-enable-debugging.patch

# Resolve an issue with ./configure and Tcl detection.
Patch2:        labltk-8.06.12-use-fpic-configure.patch
# oreon url source checksums begin
%global source0_sha256 fe0e11bacdb537ce9027aec072262405f01fe4017d19213d5a82ef053e50594d
%global source0_file labltk-8.06.15.tar.gz
# oreon url source checksums end

BuildRequires: make
BuildRequires: ocaml
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-rpm-macros
BuildRequires: tcl-devel, tk-devel

%global _desc %{expand:
labltk or mlTk is a library for interfacing OCaml with the scripting
language Tcl/Tk (all versions since 8.0.3, but no betas).}


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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/labltk-8.06.15.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "fe0e11bacdb537ce9027aec072262405f01fe4017d19213d5a82ef053e50594d" || { echo "oreon: Source0 SHA256 mismatch for labltk-8.06.15.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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

# Build does not work in parallel.
unset MAKEFLAGS

%ifarch %{ocaml_native_compiler}
make all opt \
     SHAREDCCCOMPOPTS='%{build_cflags} -fPIC' \
     TK_LINK="%{build_ldflags} $(pkg-config --libs tk)"
%else
make byte
%endif

# Build documentation
# make apiref does not work
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


%files -f .ofiles
%doc Changes README.mlTk


%files devel -f .ofiles-devel
%doc README.mlTk


%files doc
%doc examples_camltk
%doc examples_labltk
%doc apiref


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 8.06.15-6
- Prepare for Oreon 11 (RP1)
