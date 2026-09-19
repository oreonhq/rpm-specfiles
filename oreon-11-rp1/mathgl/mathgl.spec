%global source0_hash none

%if 0%{?fedora} >= 40
%ifarch %{ix86}
%global with_openmpi 0
%else
%global with_openmpi 1
%endif
%else
%global with_openmpi 1
%endif
%global with_mpich2 1
%global with_doc 1

%if 0%{?fedora}
%global with_octave 1
%global octpkg mathgl
%endif

%if 0%{?with_doc}
%global docs on
%else
%global docs off
%endif

Name:          mathgl
Version:       8.0.3
Release:       8%{?dist}
Summary:       Cross-platform library for making high-quality scientific graphics
Summary(de):   Plattformübergreifende Bibliothek für hochwertige wissenschaftliche Graphiken
Summary(ru):   Библиотека для осуществления высококачественной визуализации данных
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
Url:           http://mathgl.sourceforge.net
Source0:       http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

# Install binaries for generation examples of illustrations
Patch0:        mathgl-2.4.2-examples.patch

# Skip FLUID binary test
Patch1:        mathgl-2.4.1-fltk-skip-fluid.patch

# Mathgl's enable all tries to use hdf4 and 5 at the same time
Patch2:        mathgl-2.4.1-no_hdf4-and-hdf5-simultaneously.patch

# Let macros to decide how to install octave module
Patch3:        mathgl-nooctaveinstall.patch

# There is no easy way to disable ONLY octave. Have to cut it from CmakeList.txt
Patch4:        mathgl-2.4.1-nooctave.patch

# Fix python install location
# https://sourceforge.net/p/mathgl/discussion/508395/thread/a130201517/
Patch5:        mathgl-sitearch.patch

# Fix convertions
Patch6:        mathgl-2.4.1-gcc7.patch

# Disable uppdate-{destop,mine}-database during install process
Patch7:        mathgl-2.4.1-no_updatedb.patch

Patch8:        mathgl-freeglut.patch

# Disable rebuild of l10n files, rhbz #1808694
# .mo files built in compile time contain time stamp what make them different
# between different archs (or not if you are lucky. I'm not.)
Patch9: mathgl-2.4.2.1-norebuild_l10n.patch

# https://sourceforge.net/p/mathgl/bugs/48/
# Support for libharu 2.4
Patch10: mathgl-libharu2.4.patch

# Use flexiblas instead of gslcblas
Patch11:       mathgl-flexiblas.patch

Requires:      %{name}-common = %{version}-%{release}

# mandatory packages
BuildRequires: gsl-devel libpng-devel flexiblas-devel
BuildRequires: desktop-file-utils
BuildRequires: cmake
BuildRequires: perl(Storable)

# optional packages
BuildRequires: freeglut-devel hdf5-devel libjpeg-devel libtiff-devel
BuildRequires: fltk-devel
BuildRequires: qt5-qtbase-devel qt5-qtwebkit-devel
BuildRequires: wxGTK-devel giflib-devel libtool-ltdl-devel
BuildRequires: libharu-devel
BuildRequires: swig lua-devel
BuildRequires: libXmu-devel
BuildRequires: python%{python3_pkgversion}-devel python%{python3_pkgversion}-numpy

%description
Mathgl is a cross-platform library for making high-quality scientific
graphics. It provides fast data plotting and handling of large data
arrays, as well as  window and console modes and for easy embedding
into other programs. Mathgl integrates into fltk, qt and
opengl applications

%description -l ru
Mathgl - это кроссплатформенная библиотека для подготовки высококачественных
научных иллюстраций. Библиотека обладает возможностью работы с большими
массивами данных, быстрой отрисовки, при этом работая как в консольном, так и
оконном режимах, легко интегрируясь в другие приложения. Mathgl может быть
использована в FLTK, Qt и OpenGL приложениях.

%package devel
Summary:       Libraries and header files for %{name} library
Summary(ru):   Библиотеки и файлы заголовков для %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      gsl-devel%{?_isa}
Requires:      zlib-devel%{?_isa}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use serial version of %{name}.

%description devel -l ru
Пакет %{name}-devel содержит библиотеки и файлы заголовков, необходимые
для разработки приложений с использованием однопоточной версии %{name}.

%package fonts
Requires:      %{name}-common = %{version}-%{release}
Summary:       Compiled fonts for the %{name}

%description fonts
%{summary}.

%if 0%{?with_doc}
%package doc
Summary:       HTML documentation and tutorial for the %{name} applications
BuildArch:     noarch
BuildRequires: texi2html texinfo-tex

%description doc
This package contains the documentation in the HTML and PDF format of the %{name}
package.
%endif

%package -n udav
Summary:       Viewer and editor for mathgl graphs
Summary(ru):   Редактор и средство визуализации для MathGL
Requires:      %{name} = %{version}-%{release}

%description -n udav
UDAV is cross-platform program for interactive data array visualization
using the MathGL library. UDAV works as a front-end to the mathgl
scripting engine, allowing for the generation of a wide variety of
scientific graph styles.

%package mgllab
Summary:       Viewer and editor for mathgl graphs
Summary(ru):   Редактор и средство визуализации для MathGL
Requires:      %{name} = %{version}-%{release}
Provides:      mgllab = %{version}-%{release}

%description mgllab
mgllab is FLTK port of UDAV, cross-platform program for interactive
data array visualization using the MathGL library. Mgllab works as a
front-end to the mathgl scripting engine, allowing for the generation
of a wide variety of scientific graph styles.

%description mgllab -l ru
mgllab - это FLTK порт UDAV, кроссплатформенное приложение для
интерактивной визуализации массивов данных с применением библиотеки MathGL.
Mgllab, как GUI для MathGL, может быть использован для формирования
различного вида научных иллюстраций.

%package mglview
Summary:       Execute MathGL scripts and show in an window
Requires:      %{name}-fltk = %{version}-%{release}

%description mglview
mglview reads MGL scripts from scriptfile to produce plots of
specified functions or data. The program will create a GUI window
showing the script result.

%package -n python%{python3_pkgversion}-mathgl
%{?python_provide:%python_provide python%{python3_pkgversion}-mathgl}
Summary:       Python3 module for MathGL
Requires:      %{name} = %{version}-%{release}

%description -n python%{python3_pkgversion}-mathgl
%{summary}.

%package lua
Summary:       Lua module for MathGL
Requires:      %{name} = %{version}-%{release}

%description lua
%{summary}.

%if 0%{?with_octave}
%package -n octave-mathgl
Summary:       Octave module for MathGL
Requires:      %{name} = %{version}-%{release}
Requires:      octave >= 2.9.12
BuildRequires: octave-devel

%description -n octave-mathgl
%{summary}.
%endif

%package common
Summary:       Common files for %{name}
BuildArch:     noarch
Requires:      %{name} = %{version}-%{release}
Requires:      %{name}-fonts = %{version}-%{release}
%if 0%{?with_doc}
Requires(post): info
Requires(preun): info
%endif

%description common
%{summary}.

%package examples
Summary:       Example illustration generators for %{name}
Requires:      %{name} = %{version}-%{release}

%description examples
Binaries for generation examples of illustrations that could be 
prepared by %{name}.

%if 0%{?with_openmpi}
%package openmpi
Summary:       OpenMPI version of %{name} library
BuildRequires: openmpi-devel
BuildRequires: hdf5-openmpi-devel
Requires:      %{name}-common = %{version}-%{release}

%description openmpi
%{summary}.

%package openmpi-devel
Summary:       Devel files for OpenMPI version of %{name} library
Requires:      %{name}-openmpi%{_isa} = %{version}-%{release}
Requires:      gsl-devel%{?_isa}
Requires:      zlib-devel%{?_isa}

%description openmpi-devel
%{summary}.
%endif

%if 0%{?with_mpich2}
%package mpich
Summary:       MPICH version of %{name} library
BuildRequires: mpich-devel
BuildRequires: hdf5-mpich-devel
Requires:      %{name}-common = %{version}-%{release}
Provides:      %{name}-mpich2 = %{version}-%{release}
Obsoletes:     %{name}-mpich2 < 2.1.2-9

%description mpich
%{summary}.

%package mpich-devel
Summary:       Devel files for MPICH version of %{name} library
Requires:      %{name}-mpich%{_isa} = %{version}-%{release}
Provides:      %{name}-mpich2-devel = %{version}-%{release}
Obsoletes:     %{name}-mpich2-devel < 2.1.2-9
Requires:      gsl-devel%{?_isa}
Requires:      zlib-devel%{?_isa}

%description mpich-devel
%{summary}.
%endif

%package qt5
Summary:       Qt5 widgets of %{name} library
Requires:      %{name} = %{version}-%{release}
Obsoletes:     %{name}-qt < 2.4
Provides:      %{name}-qt = %{version}-%{release}
Obsoletes:     %{name}-qt4 < 8.0

%description qt5
%{summary}.

%package qt5-devel
Summary:       Devel files for qt5 widgets of %{name} library
Requires:      %{name}-devel = %{version}-%{release}
Requires:      %{name}-qt5 = %{version}-%{release}
Obsoletes:     %{name}-qt-devel < 2.4
Provides:      %{name}-qt-devel = %{version}-%{release}
Obsoletes:     %{name}-qt4-devel < 8.0
Requires:      qt5-qtbase-devel

%description qt5-devel
%{summary}.

%package fltk
Summary:       Fltk widgets of %{name} library
Requires:      %{name} = %{version}-%{release}
Requires:      fltk-fluid

%description fltk
%{summary}.

%package fltk-devel
Summary:       Devel files for fltk widgets of %{name} library
Requires:      %{name}-devel = %{version}-%{release}
Requires:      %{name}-fltk = %{version}-%{release}
Requires:      fltk-devel

%description fltk-devel
%{summary}.

%package wx
Summary:       wxWidgets widgets of %{name} library
Requires:      %{name} = %{version}-%{release}

%description wx
%{summary}.

%package wx-devel
Summary:       Devel files for wxWidgets widgets of %{name} library
Requires:      %{name}-devel = %{version}-%{release}
Requires:      %{name}-wx = %{version}-%{release}
Requires:      wxGTK-devel

%description wx-devel
%{summary}.

%prep
%setup -q

# get rid of 3d-paty getopt
rm -rf addons/getopt

# prep for both py2 and py3 build
#mkdir lang/python3
#touch lang/python3/CMakeLists.txt

#convert EOL encodings, maintaining timestames
for file in AUTHORS ChangeLog.txt README ; do
    sed 's/\r//' $file > $file.new && \
    touch -r $file $file.new && \
    mv $file.new $file
done

%patch -P0 -p1 -b .examples
%patch -P1 -p1 -b .fluid
%patch -P2 -p1 -b .no-hdf4-and-hdf5-simultaneously
%patch -P5 -p1 -b .sitearch
%patch -P6 -p1 -b .gcc7
%patch -P7 -p1 -b .no_updatedb
%if 0%{?with_octave}
%patch -P3 -p1 -b .nooctaveinstall
%else
%patch -P4 -p1 -b .no_octave
%endif
%patch -P8 -p0 -b .freeglut
%patch -P9 -p1 -b .norebuild_l10n
%patch -P10 -p1 -b .libharu2.4
%patch -P11 -p1 -b .flexiblas

# Fix hardcoded Python version
#sed -i -e 's,3\.[0-9],%{python3_version},g' \
#       -e 's,cpython-3[0-9],cpython-%{python3_version_nodots},g' \
#          lang/python3/CMakeLists.txt

# Fix hardcoded paths
sed -i s,/usr/local/share/doc/mathgl/,%{_docdir}/%{name}/, udav/udav_wnd.h
sed -i s,/usr/local/share/udav/,%{_datadir}/udav/, udav/udav_wnd.cpp
sed -i s,/usr/local/share/mathgl/fonts/,%{_datadir}/%{name}/fonts/, udav/prop_dlg.cpp

# Fix octave module version wether we need it or not
sed -i -e "s,Version:.*,Version: %{version}," lang/DESCRIPTION

%if 0%{?fedora}
%global octave_tar_suffix %{octave_host}-%{octave_api}
%global mgl_octarch_dir %{_builddir}/%{buildsubdir}/build/
%global mgl_octarch_name %{octpkg}-%{version}-%{octave_tar_suffix}.tar.gz
%endif

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
OMP_NUM_THREADS=1
export OMP_NUM_THREADS

%define building() \
BUILD_MPI="-Denable-mpi=on -Denable-all-docs=off" %buildcommon

%define building_serial() \
BUILD_MPI="-Denable-mpi=off \
           -Denable-all-docs=%{docs} \
           -Denable-all-widgets=on \
           -Denable-all-swig=on \
           -Denable-all-widgets=on \
           -Denable-hdf4=off \
           " %buildcommon

# Disable SMP build

%define buildcommon() \
%cmake \\\
    -DMathGL_INSTALL_CMAKE_DIR=%{_libdir}/cmake/mathgl \\\
    -DMathGL_INSTALL_LIB_DIR=%{_libdir} \\\
    -Denable-all=on \\\
    -Denable-qt5asqt=off \\\
    $BUILD_MPI \\\
    ..; \
%{cmake_build}

# serial
%global _vpath_builddir %{_target_platform}_serial
%building_serial

# MPI vars
export CC=mpicc
export CXX=mpicxx

%if 0%{?with_openmpi}
# OpenMPI
%{_openmpi_load}
%global _vpath_builddir %{_target_platform}_openmpi
%building
%{_openmpi_unload}
%endif

%if 0%{?with_mpich2}
# MPICH2
%{_mpich_load}
%global _vpath_builddir %{_target_platform}_mpich
%building
%{_mpich_unload}
%endif

%install

# MPI install libs only
%define installing() \
DESTDIR=%{buildroot}%{_libdir}/$MPI_COMPILER_NAME %__cmake --install %{_target_platform}_$MPI_COMPILER_NAME; \
mkdir -p %{buildroot}%{_libdir}/$MPI_COMPILER_NAME/lib/ \
mv %{buildroot}%{_libdir}/$MPI_COMPILER_NAME/%{_libdir}/libmgl* %{buildroot}%{_libdir}/$MPI_COMPILER_NAME/lib/; \
mkdir -p %{buildroot}%{_includedir}/$MPI_COMPILER/mgl2; \
mv %{buildroot}%{_libdir}/$MPI_COMPILER_NAME/%{_includedir}/mgl2/* %{buildroot}%{_includedir}/$MPI_COMPILER/mgl2/; \
rm -f %{buildroot}%{_libdir}/$MPI_COMPILER_NAME/lib/*.a; \
rm -r %{buildroot}%{_libdir}/$MPI_COMPILER_NAME/usr

# Serial
%global _vpath_builddir %{_target_platform}_serial
%{cmake_install}
%if 0%{?with_octave}
rm -f %{buildroot}%{_datadir}/%{name}/mathgl.tar.gz
mkdir -p %{mgl_octarch_dir}
cp %{_target_platform}_serial/lang/%{octpkg}.tar.gz %{mgl_octarch_dir}/%{mgl_octarch_name}
%octave_pkg_install
rm -f %{mgl_octarch_dir}/%{mgl_octarch_name}/%{octpkg}.tar.gz
%endif

# part of serial build
%find_lang %{name}
%find_lang udav --with-qt

# No that modern cmake_install macros for mpi install.
%if 0%{?with_openmpi}
# OpenMPI
%{_openmpi_load}
%global _vpath_builddir %{_target_platform}_openmpi
MPI_COMPILER_NAME=openmpi %installing
%{_openmpi_unload}
%endif

%if 0%{?with_mpich2}
# MPICH
%{_mpich_load}
%global _vpath_builddir %{_target_platform}_mpich
MPI_COMPILER_NAME=mpich %installing
%{_mpich_unload}
%endif

#Remove symlink to .so file in python dir. Let python find libs normally
# not needed now?
#unlink %{buildroot}/%{python3_sitelib}/_mathgl.so

#Remove static libraries generated by cmake
rm %{buildroot}/%{_libdir}/*.a

# Remove the binary mgl.cgi. Im not convinced about it (eg mem leak in main), and that its really needed
# The same with man file for it
rm %{buildroot}/%{_prefix}/lib/cgi-bin/mgl.cgi
%if 0%{?with_doc}
rm %{buildroot}/%{_mandir}/man1/mgl.cgi.1*

# Prepare for documentation
if [ -d _tmp_docdir ]
then
rm -r _tmp_docdir
fi
mv %{buildroot}%{_docdir}/mathgl _tmp_docdir
%endif

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/udav.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/mgllab.desktop

%ldconfig_scriptlets

%ldconfig_scriptlets qt5

%ldconfig_scriptlets fltk

%ldconfig_scriptlets wx

%if 0%{?with_octave}
%post -n octave-mathgl
%octave_cmd pkg rebuild

%preun -n octave-mathgl
%octave_pkg_preun

%postun -n octave-mathgl
%octave_cmd pkg rebuild
%endif

%files -f %{name}.lang
%doc AUTHORS ChangeLog.txt README COPYING  README_V2
%{_libdir}/libmgl.so.*
%{_bindir}/mglconv
%{_bindir}/mgltask
%exclude %{_bindir}/mgl_*example
%if 0%{?with_doc}
%{_mandir}/man1/mglconv.1.gz
%endif

%files devel
%{_libdir}/libmgl.so
%{_includedir}/mgl2/
%{_libdir}/cmake/mathgl/
%{_libdir}/cmake/mathgl2/

%files mgllab
%{_bindir}/mgllab
%{_datadir}/applications/mgllab.desktop

%files mglview
%{_bindir}/mglview
%if 0%{?with_doc}
%{_mandir}/man1/mglview.1.gz
%endif

%files qt5
%{_libdir}/libmgl-qt.so.*
%{_libdir}/libmgl-qt5.so.*
%{_libdir}/libmgl-wnd.so.*

%files qt5-devel
%{_libdir}/libmgl-qt.so
%{_libdir}/libmgl-qt5.so
%{_libdir}/libmgl-wnd.so

%files wx
%{_libdir}/libmgl-wx.so.*

%files wx-devel
%{_libdir}/libmgl-wx.so

%files fltk
%{_libdir}/libmgl-fltk.so.*
%{_libdir}/libmgl-glut.so.*

%files fltk-devel
%{_libdir}/libmgl-fltk.so
%{_libdir}/libmgl-glut.so

%files -n udav -f udav.lang
%{_bindir}/udav
%if 0%{?with_doc}
%{_mandir}/man1/udav.1.gz
%endif
%{_datadir}/applications/udav.desktop
%dir %{_datadir}/udav/

%files -n python%{python3_pkgversion}-mathgl
%{python3_sitearch}/*

%files lua
%{_libdir}/mgl-lua.so

%if 0%{?with_octave}
%files -n octave-mathgl
%{octpkglibdir}
%dir %{octpkgdir}
%{octpkgdir}/packinfo
%endif

%if 0%{?with_doc}
%files doc
%doc AUTHORS COPYING
%doc _tmp_docdir/*
%endif

%files fonts
%{_datadir}/%{name}/fonts/

%files common
%{_datadir}/pixmaps/*.png
%{_datadir}/mime/packages/mgl.xml
%if 0%{?with_doc}
%{_mandir}/man5/mgl.5.gz
%{_infodir}/%{name}*.gz
%endif

%files examples
%{_bindir}/mgl_*example

%if 0%{?with_openmpi}
%files openmpi
%doc COPYING
%{_libdir}/openmpi/lib/*.so.*

%files openmpi-devel
%{_libdir}/openmpi/lib/*.so
%{_includedir}/openmpi-%{_arch}/mgl2/
%endif

%if 0%{?with_mpich2}
%files mpich
%doc COPYING
%{_libdir}/mpich/lib/*.so.*

%files mpich-devel
%{_libdir}/mpich/lib/*.so
%{_includedir}/mpich-%{_arch}/mgl2/
%endif

%changelog
%autochangelog
