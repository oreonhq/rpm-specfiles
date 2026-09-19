%global source0_hash 845477ed8d5aeaad63907a9edfc1d8f8d62b932c6e37a32502926ee402a6271f

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

Name:           ocaml-lablgl
Epoch:          1
Version:        1.07
Release:        20%{?dist}
Summary:        LablGL is an OpenGL interface for Objective Caml
License:        BSD-3-Clause

URL:            https://github.com/garrigue/lablgl
VCS:            git:%{url}.git
Source0:        %{url}/archive/v%{version}/lablgl-%{version}.tar.gz

# Fix a use-after-free bug
# https://github.com/garrigue/lablgl/pull/5
Patch:          0001-Avoid-possible-use-after-free-in-Togl.patch
# Fix a build error with the Modern C initiative
# https://github.com/garrigue/lablgl/pull/6
Patch:          0002-Fix-mismatched-pointer-types-for-GCC-14.patch
# https://github.com/garrigue/lablgl/pull/11
Patch:          0003-Add-a-gitignore-file-to-ignore-various-generated-fil.patch
# Adapt to OCaml 5
# https://github.com/garrigue/lablgl/pull/10
Patch:          0004-Update-Tk-code-for-OCaml-5.patch
# Fix for Tcl/Tk 9.0
# https://github.com/garrigue/lablgl/pull/12
Patch:          0005-Togl-Remove-useless-definition-of-NULL.patch
Patch:          0006-Togl-Remove-use-of-some-Tcl-Tk-macros.patch
Patch:          0007-Togl-Pass-object-style-parameters-to-Tk_ConfigureWid.patch
Patch:          0008-Togl-Replace-Tk_-functions-with-new-Tcl_-equivalents.patch

BuildRequires:  make
BuildRequires:  freeglut-devel 
BuildRequires:  ocaml >= 4.14
BuildRequires:  ocaml-findlib >= 1.2.1
BuildRequires:  ocaml-camlp-streams-devel
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-labltk-devel
BuildRequires:  ocaml-rpm-macros
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXmu-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel

%description
LablGL is is an Objective Caml interface to OpenGL. Support is
included for use inside LablTk, and LablGTK also includes specific
support for LablGL.  It can be used either with proprietary OpenGL
implementations (SGI, Digital Unix, Solaris...), with XFree86 GLX
extension, or with open-source Mesa.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       ocaml-labltk-devel%{?_isa}
Requires:       freeglut-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n lablgl-%{version} -p1

cat > Makefile.config <<EOF
BINDIR = %{_bindir}
XINCLUDES = -I%{_prefix}/X11R6/include
XLIBS = -lXext -lXmu -lX11
TKINCLUDES = -I%{_includedir}
TKLIBS = $(pkg-config --libs tk)
GLINCLUDES =
GLLIBS = -lGL -lGLU
GLUTLIBS = -lglut
RANLIB = :
LIBDIR = %{_libdir}/ocaml
DLLDIR = %{_libdir}/ocaml/stublibs
INSTALLDIR = %{_libdir}/ocaml/lablGL
TOGLDIR=Togl
COPTS = %{build_cflags}
EOF

# Prepare the examples for inclusion in the docs
mkdir -p examples/LablGlut examples/Togl
cp -a LablGlut/examples examples/LablGlut
cp -a Togl/examples examples/Togl

# Fix the version number in META
sed -i.orig 's/1\.05/%{version}/' META
touch -r META.orig META

# Build with debuginfo
sed -i 's/\$(CAMLC)/& -g/;s/\$(CAMLOPT)/& -g/;s/ocamlmklib/& -g/' Makefile.common
sed -i 's/ocamlmktop/& -g/' LablGlut/src/Makefile Togl/src/Makefile

%build
# Parallel builds don't work.
unset MAKEFLAGS
make all \
%ifarch %{ocaml_native_compiler}
opt
%endif

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/ocaml/lablGL
mkdir -p $RPM_BUILD_ROOT%{_libdir}/ocaml/stublibs
make INSTALLDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml/lablGL \
    DLLDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml/stublibs \
    BINDIR=$RPM_BUILD_ROOT%{_bindir} \
    install

# Install package META.
cp -p META $RPM_BUILD_ROOT%{_libdir}/ocaml/lablGL/

# Remove unnecessary *.ml files (ones which have a *.mli).
pushd $RPM_BUILD_ROOT%{_libdir}/ocaml/lablGL
for f in *.ml; do \
  b=`basename $f .ml`; \
  if [ -f "$b.mli" ]; then \
    rm $f; \
  fi; \
done
popd

%ocaml_files

%files -f .ofiles
%doc README
%license COPYRIGHT

%files devel -f .ofiles-devel
%doc CHANGES README examples/LablGlut examples/Togl
%license COPYRIGHT

%changelog
%autochangelog
