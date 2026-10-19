%global source0_hash b92de4d8f626a9b20c84fc94f4f6a9976edd76e33fb1eae44f6804bdcc628c7b
%{!?octave_api:%global octave_api %(octave-config -p API_VERSION || echo 0)}
%bcond_without doc
%if 0%{?el8}%{?el9}
%bcond_with octave
%else
%bcond_without octave
%endif
%ifnarch %{GNAT_arches}
%bcond_with ada
%else
%bcond_without ada
%endif
%ifarch %{ix86} sparc64 s390 s390x
%bcond_with ocaml
%else
%bcond_without ocaml
%endif
%bcond_without itcl
%ifarch s390x
%if 0%{?el8}
%bcond check 1
%else
%bcond check 0
%endif
%else
%bcond check 0
%endif
%ifarch %{java_arches}
%bcond_without java
%else
%bcond_with java
%endif
%global commit 48a56ee63d25d24eeb44f392025953a6e9cc6b3f
Name:           plplot
Version:        5.15.0
Release:        1%{?dist}
Summary:        Library of functions for making scientific plots
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://plplot.sourceforge.net/
Source0:        https://downloads.sourceforge.net/plplot/%{name}-%{version}.tar.gz
Source1:        xorg.conf
Patch0:         plplot-ieee.patch
Patch1:         plplot-qt-5.15.patch
Patch2:         plplot-multiarch.patch
Patch3:         plplot-ocaml-rpath.patch
Patch4:         plplot-python3.13.patch
Patch5:         plplot-numpy.patch
Patch6:         plplot-signal.patch
Patch7:         plplot-ocaml.patch
Patch9:         plplot-5.12.0-safe-string.patch
Patch10:        plplot-pyqt5-sip-path.patch
Patch11:        plplot-sip-build-support.patch
Patch12:        plplot-cmake-c99.patch
Patch13:        plplot-ocaml-link.patch
Patch14:        plplot-5.15.0-swig-4.3.patch
Patch15:        https://sourceforge.net/p/plplot/support-requests/_discuss/thread/bd326c8bff/fec5/attachment/plplot-5.15.0-swig-4.4.patch
%global _cmake_generator "Unix Makefiles"
%if %{with ada}
%if %{with flexiblas}
%else
%endif
%endif
%if %{with octave}
%global build_octave -DTRY_OCTAVE4=ON
%else
Obsoletes:      %{name}-octave < %{version}-%{release}
%global build_octave -DENABLE_octave:BOOL=OFF
%endif
%if %{with java}
%if 0%{?el9}
%endif
%else
Obsoletes:      %{name}-java < %{version}-%{release}
Obsoletes:      %{name}-java-devel < %{version}-%{release}
%endif
%if %{with itcl}
%endif
%if %{with doc}
%endif
%if %{with ocaml}
%endif
%if %{with check}
%endif
Requires:       gnu-free-mono-fonts
Requires:       gnu-free-sans-fonts
Requires:       gnu-free-serif-fonts
Requires:       python3-numpy
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(qt5gui)
BuildRequires:  cmake(qt5printsupport)
BuildRequires:  docbook2X
BuildRequires:  doxygen
BuildRequires:  freetype-devel
BuildRequires:  gcc-gfortran
BuildRequires:  gd-devel
BuildRequires:  gnu-free-mono-fonts
BuildRequires:  gnu-free-sans-fonts
BuildRequires:  gnu-free-serif-fonts
BuildRequires:  itcl-devel
BuildRequires:  itk-devel
BuildRequires:  iwidgets
BuildRequires:  java-devel
BuildRequires:  lasi-devel
BuildRequires:  libharu-devel
BuildRequires:  libtool-ltdl-devel
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  mesa-dri-drivers
BuildRequires:  ncurses-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-camlidl-devel
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  octave-devel
BuildRequires:  perl(XML::DOM)
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-qt5-devel
BuildRequires:  python3dist(pyqt-builder)
BuildRequires:  python3dist(sip)
BuildRequires:  qhull-devel
BuildRequires:  shapelib-devel
BuildRequires:  swig
BuildRequires:  tcl-devel
BuildRequires:  tex(ulem.sty)
BuildRequires:  texlive-xmltex
BuildRequires:  tk-devel
BuildRequires:  wxGTK-devel
BuildRequires:  xmlto
BuildRequires:  xorg-x11-drv-dummy
# /oreon:deps
%description
PLplot is a library of functions that are useful for making scientific
plots.

PLplot can be used from within compiled languages such as C, C++,
FORTRAN and Java, and interactively from interpreted languages such as
Octave, Python, Perl and Tcl.

The PLplot library can be used to create standard x-y plots, semilog
plots, log-log plots, contour plots, 3D surface plots, mesh plots, bar
charts and pie charts. Multiple graphs (of the same or different sizes)
may be placed on a single page with multiple lines in each graph.

A variety of output file devices such as Postscript, png, jpeg, LaTeX
and others, as well as interactive devices such as xwin, tk, xterm and
Tektronics devices are supported. New devices can be easily added by
writing a small number of device dependent routines.

There are almost 2000 characters in the extended character set. This
includes four different fonts, the Greek alphabet and a host of
mathematical, musical, and other symbols. Some devices supports its own
way of dealing with text, such as the Postscript and LaTeX drivers, or
the png and jpeg drivers that uses the Freetype library.

%package        libs
Summary:        Libraries for PLplot
Requires:       %{name}-data = %{version}-%{release}
Obsoletes:      %{name}-perl < 5.14.0-8
%description    libs
%{summary}.

%package        data
Summary:        Data files for PLplot
BuildArch:      noarch
%description    data
%{summary}.

%package        devel
Summary:        Development headers and libraries for PLplot
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    devel
%{summary}.

%package        doc
Summary:        Documentation for PLplot
Requires:       %{name} = %{version}-%{release}
%description    doc
%{summary}.

%if %{with ada}
%package        ada
Summary:        Functions for scientific plotting with Ada
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    ada
%{summary}.

%package        ada-devel
Summary:        Development files for using PLplot Ada bindings
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-ada%{?_isa} = %{version}-%{release}
Requires:       gcc-gnat
%description    ada-devel
%{summary}.
%endif

%package        fortran-devel
Summary:        Development files for using PLplot Fortran bindings
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       gcc-gfortran
%description    fortran-devel
%{summary}.

%if %{with java}
%package        java
Summary:        Functions for scientific plotting with Java
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       java-headless
%description    java
%{summary}.

%package        java-devel
Summary:        Development files for using PLplot GNOME
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-java%{?_isa} = %{version}-%{release}
%description    java-devel
%{summary}.
%endif

%package        lua
Summary:        Functions for scientific plotting with Lua
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       lua
%description    lua
%{summary}.

%if %{with ocaml}
%package        -n ocaml-plplot
Summary:        Functions for scientific plotting with OCaml
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       plplot-ocaml = %{version}-%{release}
Obsoletes:      plplot-ocaml < 5.9.10-3
%description    -n ocaml-plplot
%{summary}.

%package        -n ocaml-plplot-devel
Summary:        Development files for PLplot OCaml
Requires:       ocaml-plplot%{?_isa} = %{version}-%{release}
Provides:       plplot-ocaml-devel = %{version}-%{release}
Obsoletes:      plplot-ocaml-devel < 5.9.10-3
%description    -n ocaml-plplot-devel
%{summary}.
%endif

%if %{with octave}
%package        octave
Summary:        Functions for scientific plotting with Octave
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       octave(api) = %{octave_api}
%description    octave
%{summary}.
%endif

%package        pyqt
Summary:        Functions for scientific plotting with PyQt
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    pyqt
%{summary}.

%package        qt
Summary:        Functions for scientific plotting with Qt
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    qt
%{summary}.

%package        qt-devel
Summary:        Development files for using PLplot with Qt
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-qt%{?_isa} = %{version}-%{release}
Requires:       cmake(qt5gui)
Requires:       cmake(qt5printsupport)
Requires:       cmake(Qt5Svg)
%description    qt-devel
%{summary}.

%package        tk
Summary:        Functions for scientific plotting with Tk
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    tk
%{summary}.

%package        tk-devel
Summary:        Development files for using PLplot with Tk
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-tk%{?_isa} = %{version}-%{release}
Requires:       tk-devel%{?_isa}
%global __requires_exclude_from ^%{_datadir}/plplot%{version}/examples/tk/tk.*$
%description    tk-devel
%{summary}.

%package        wxGTK
Summary:        Functions for scientific plotting with wxGTK
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    wxGTK
%{summary}.

%package        wxGTK-devel
Summary:        Development files for using PLplot with wxGTK
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-wxGTK%{?_isa} = %{version}-%{release}
Requires:       wxGTK-devel%{?_isa}
%description    wxGTK-devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .ieee
%patch -P1 -p1 -b .qt5
%patch -P2 -p1 -b .multiarch
%patch -P3 -p1 -b .ocaml-rpath
%patch -P4 -p1 -b .python3.13
%patch -P5 -p1 -b .numpy
%patch -P6 -p1 -b .signal
%patch -P7 -p1 -b .ocaml
%patch -P9 -p1 -b .safestring
%patch -P10 -p1 -b .sip-path
%patch -P11 -p1 -b .sip-build
%patch -P12 -p1
%patch -P13 -p1 -b .ocamlmklib
%patch -P14 -p1
%patch -P15 -p1
# Use cmake FindLua
rm cmake/modules/FindLua.cmake

%build

export PATH="%{_qt5_bindir}:$PATH"
unset TERM
printenv
tkver=$(echo 'puts [info patchlevel]; exit' | tclsh)
%if %{with itcl}
itclver=$(echo %{_libdir}/libitcl*.so | sed -e 's/.*itcl\([0-9.]*\)\.so/\1/')
itkver=$(echo %{_libdir}/libitk*.so | sed -e 's/.*itk\([0-9.]*\)\.so/\1/')
iwidgetsver=$(echo %{_datadir}/tcl*/iwidgets* | sed -e 's/.*iwidgets//')
%endif
%cmake \
        -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} \
        -DFORTRAN_MOD_DIR:PATH=%{_fmoddir} \
        -DUSE_RPATH:BOOL=OFF \
        -DENABLE_ada:BOOL=ON \
        %{?with_flexiblas:-DBLA_VENDOR=FlexiBLAS} \
        -DENABLE_d:BOOL=ON \
%if %{with itcl}
        -DENABLE_itcl:BOOL=ON \
        -DENABLE_itk:BOOL=ON \
        -DPLPLOT_ITCL_VERSION=$itclver \
        -DPLPLOT_ITK_VERSION=$itkver \
        -DIWIDGETS_VERSIONS_LIST:STRING="$iwidgetsver;$itkver;$itclver" \
        -DUSE_INCRTCL_VERSION_4:BOOL=ON \
%endif
        -DENABLE_lua:BOOL=ON \
        -DENABLE_ocaml:BOOL=ON \
        -DOCAML_INSTALL_DIR:PATH=`ocamlc -where` \
        %{build_octave} \
        -DENABLE_tk:BOOL=ON \
        -DJAVAWRAPPER_DIR:PATH="%{_libdir}/plplot%{version}" \
        -DNON_TRANSITIVE:BOOL=ON \
        -DPL_FREETYPE_FONT_PATH:PATH="/usr/share/fonts/gnu-free" \
        -DPLD_aqt:BOOL=ON \
        -DPLD_ntk:BOOL=ON \
        -DPLD_pstex:BOOL=ON \
        -DPLD_svg:BOOL=ON \
        -DPLD_wxwidgets:BOOL=ON \
        -DPLPLOT_TK_VERSION=$tkver \
        -DPLPLOT_USE_QT5=ON \
%if %{with doc}
        -DXML_DECL:FILEPATH=/usr/share/sgml/xml.dcl \
        -DBUILD_DOC:BOOL=ON \
        -DBUILD_DOX_DOC:BOOL=ON \
%else
        -DPREBUILT_DOC:BOOL=ON \
%endif
        -DBUILD_TEST:BOOL=ON
%cmake_build
%install
%cmake_install
find $RPM_BUILD_ROOT%{_datadir}/plplot%{version}/examples -type f | xargs chmod -x
%oreon_autofiles ocaml-plplot usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ocaml-plplot-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

cp %SOURCE1 .
if [ -x /usr/libexec/Xorg ]; then
   Xorg=/usr/libexec/Xorg
else
   Xorg=/usr/libexec/Xorg.bin
fi
$Xorg -noreset +extension GLX +extension RANDR +extension RENDER -nolisten tcp -nolisten unix -logfile ./xorg.log -config ./xorg.conf -configdir . :99 &
export DISPLAY=:99
export LD_LIBRARY_PATH=$PWD/%{_vpath_builddir}/bindings/ocaml:$RPM_BUILD_ROOT%{_libdir}
%ifarch ppc ppc64 ppc64le
%ctest --exclude-regex 'ocaml|octave'
%else
%ifarch %{arm} aarch64
%ctest --exclude-regex 'java|ocaml|octave'
%else
%ifarch s390x
%ctest || :
%else
%ctest --exclude-regex 'octave'
%ctest --tests-regex 'octave' || :
%endif
%endif
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n plplot-libs -f %{oreon_filedir}/plplot-libs.list
%files -n plplot-data -f %{oreon_filedir}/plplot-data.list
%files -n plplot-devel -f %{oreon_filedir}/plplot-devel.list
%files -n plplot-doc -f %{oreon_filedir}/plplot-doc.list
%files -n plplot-fortran-devel -f %{oreon_filedir}/plplot-fortran-devel.list
%files -n plplot-java -f %{oreon_filedir}/plplot-java.list
%files -n plplot-java-devel -f %{oreon_filedir}/plplot-java-devel.list
%files -n plplot-lua -f %{oreon_filedir}/plplot-lua.list
%files -n ocaml-plplot -f %{oreon_filedir}/ocaml-plplot.list
%files -n ocaml-plplot-devel -f %{oreon_filedir}/ocaml-plplot-devel.list
%files -n plplot-octave -f %{oreon_filedir}/plplot-octave.list
%files -n plplot-pyqt -f %{oreon_filedir}/plplot-pyqt.list
%files -n plplot-qt -f %{oreon_filedir}/plplot-qt.list
%files -n plplot-qt-devel -f %{oreon_filedir}/plplot-qt-devel.list
%files -n plplot-tk -f %{oreon_filedir}/plplot-tk.list
%files -n plplot-tk-devel -f %{oreon_filedir}/plplot-tk-devel.list
%files -n plplot-wxGTK -f %{oreon_filedir}/plplot-wxGTK.list
%files -n plplot-wxGTK-devel -f %{oreon_filedir}/plplot-wxGTK-devel.list

%changelog

%autochangelog
