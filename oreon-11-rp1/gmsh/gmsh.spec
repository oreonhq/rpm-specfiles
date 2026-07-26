%global source0_hash 78411ec17204cca1060c71c4c9557cb2ca1ad8af17650d3f72ff3b2f3eff5210

%if 0%{?fedora} >= 40
%ifarch %{ix86}
%bcond_with openmpi
%else
%bcond_without openmpi
%endif
%else
%bcond_without openmpi
%endif
%bcond_without mpich

%global sover 4.15

%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
%bcond_without flexiblas
%endif

Name:       gmsh
Summary:    A three-dimensional finite element mesh generator
Version:    4.15.0
Release:    3%{?dist}
# MPI not available on i686
ExcludeArch: %{ix86}

# gmsh is GPL-2.0-or-later WITH Gmsh-exception, see LICENSE.txt
# contrib/{DiscreteIntegration, HighOrderMeshOptimizer, MeshOptimizer, onelab} are MIT, see respective README.txt
License:    GPL-2.0-or-later WITH Gmsh-exception AND MIT
URL:        http://geuz.org/gmsh/
# Download source from http://geuz.org/gmsh/src/%%{name}-%%{version}-source.tgz
# Delete contrib/blossom and contrib/mpeg_encode from source archive
Source0:    %{name}-%{version}-source-fedora.tar.xz
Source1:    %{name}.desktop

# Install onelab.py and gmsh.py into the python site-packages directory
Patch0:     gmsh_python.patch
# Adapt med.h include path
Patch1:     gmsh_med.patch
# Install Julia API to share/gmsh
Patch2:     gmsh_julia.patch
# Remove odd install of gmsh shared library
Patch3:     gmsh_install.patch
# Unbundle gl2ps
Patch4:     gmsh_unbundle_gl2ps.patch
# Make gmm use superlu
Patch5:     gmsh_gmm.patch

BuildRequires: ann-devel
%if %{with flexiblas}
BuildRequires: flexiblas-devel
%else
BuildRequires: blas-devel, lapack-devel
%endif
BuildRequires: cgnslib-devel
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: fltk-devel
BuildRequires: gcc-c++
BuildRequires: gcc-gfortran
BuildRequires: gmm-devel
BuildRequires: gmp-devel
BuildRequires: hdf5-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: liblbfgs-devel
BuildRequires: libpng-devel
BuildRequires: mathex-devel
BuildRequires: med-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: metis-devel
# NOTE: netgen is FTBFS on aarch64
%ifnarch aarch64
BuildRequires: netgen-mesher-devel-private
%endif
BuildRequires: opencascade-devel
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: SuperLU-devel
BuildRequires: voro++-devel
BuildRequires: zlib-devel
BuildRequires: texinfo
# For transforming icon
BuildRequires: ImageMagick

Requires:       %{name}-common = %{version}-%{release}

%description
Gmsh is a 3D finite element grid generator with a build-in CAD engine
and post-processor. Its design goal is to provide a fast, light and
user-friendly meshing tool with parametric input and advanced
visualization capabilities. Gmsh is built around four modules:
geometry, mesh, solver and post-processing. The specification of any
input to these modules is done either interactively using the
graphical user interface or in ASCII text files using Gmsh's own scripting
language.

%package common
Summary:        Common files for %{name}
Requires:       hicolor-icon-theme
BuildArch:      noarch

%description common
Common files for %{name}.

%package libs
Summary:        Libraries provided by %{name}

%description libs
Libraries provided by %{name}. These libraries are not required for
the base %{name} package and are used for development only.

%package -n python3-%{name}
Summary:        Python3 API for %{name}
%{?python_provide:%python_provide python3-%{name}}
Obsoletes:      python3-%{name}-private

BuildArch:      noarch

Requires:       %{name}-libs = %{version}-%{release}

%description -n python3-%{name}
Python3 API for %{name}.

%package devel
Summary:        Development with %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-devel-private

%description devel
Header files for development with %{name}.

%package doc
Summary:        Documentation, demos and tutorials for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
Documentation, demo projects and tutorials for %{name}.

###############################################################################

%if %{with openmpi}
%package        openmpi
Summary:        %{name} compiled against openmpi
BuildRequires:  openmpi-devel
%ifnarch aarch64
BuildRequires:  netgen-mesher-openmpi-devel
%endif
BuildRequires:  hdf5-openmpi-devel
Requires:       %{name}-common = %{version}-%{release}
Requires:       %{name}-openmpi-libs%{?_isa} = %{version}-%{release}

%description    openmpi
%{name} compiled against openmpi.

%package        openmpi-libs
Summary:        %{name} libraries compiled against openmpi

%description    openmpi-libs
%{name} libraries compiled against openmpi.

%package        openmpi-devel
Summary:        Development files for %{name} compiled against openmpi
# Require explicitly for dir ownership
Requires:       openmpi-devel
Requires:       %{name}-openmpi%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-openmpi-devel-private

%description    openmpi-devel
Development files for %{name} compiled against openmpi.
%endif

###############################################################################

%if %{with mpich}
%package        mpich
Summary:        %{name} compiled against mpich
BuildRequires:  mpich-devel
%ifnarch aarch64
BuildRequires:  netgen-mesher-mpich-devel
%endif
BuildRequires:  hdf5-mpich-devel
Requires:       %{name}-common = %{version}-%{release}
Requires:       %{name}-mpich-libs%{?_isa} = %{version}-%{release}

%description    mpich
%{name} compiled against mpich.

%package        mpich-libs
Summary:        %{name} libraries compiled against mpich

%description    mpich-libs
%{name} libraries compiled against mpich.

%package        mpich-devel
Summary:        Development files for %{name} compiled against mpich
# Require explicitly for dir ownership
Requires:       mpich-devel
Requires:       %{name}-mpich%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-mpich-devel-private

%description    mpich-devel
Development files for %{name} compiled against mpich.
%endif

###############################################################################

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}-source

# Copy these outside the contrib folder
cp contrib/Netgen/nglib_gmsh.h contrib/Netgen/nglib_gmsh.cpp src/mesh

# Bamg: part of freefem++, modified source code
# DiscreteIntegration: gmsh internal module
# HighOrderMeshOptimizer: gmsh internal module
# hxt: see contrib/hxt/CREDITS.txt
# kbipack: Source not available on the net anymore
# onelab: gmsh internal module
# WinslowUntangler: gmsh internal module (?)
(
cd contrib;
ls -1 | \
    grep -v ^bamg$ | \
    grep -v ^blossom$ | \
    grep -v ^DiscreteIntegration$ | \
    grep -v ^MeshOptimizer$ | \
    grep -v ^HighOrderMeshOptimizer$ | \
    grep -v ^QuadTri$ | \
    grep -v ^hxt$ | \
    grep -v ^kbipack$ | \
    grep -v ^onelab$ | \
    grep -v ^tinyobjloader$ | \
    grep -v ^WinslowUntangler$ | \
xargs rm -rf
)

%build
# mpeg not in fedora due to patent issues
# blossoms is nonfree, see contrib/blossoms/README.txt

gmsh_cmake_args="\
    %{?with_flexiblas:-DBLA_VENDOR=FlexiBLAS} \
    -DENABLE_SYSTEM_CONTRIB=YES \
    -DENABLE_BUILD_LIB=YES \
    -DENABLE_BUILD_SHARED=YES \
    -DENABLE_BUILD_DYNAMIC=YES \
%ifarch aarch64
    -DENABLE_NETGEN=NO \
%endif
    -DENABLE_MPEG_ENCODE=NO"

### serial version ###
%define _vpath_builddir %{_target_platform}
%cmake \
    -DENABLE_OPENMP=ON \
    $gmsh_cmake_args

%cmake_build

### openmpi version ###
%if %{with openmpi}
%{_openmpi_load}
export CXX=mpicxx
%define _vpath_builddir %{_target_platform}-openmpi
%cmake \
    -DENABLE_MPI=YES \
    -DCMAKE_INSTALL_BINDIR=$MPI_BIN \
    -DCMAKE_INSTALL_LIBDIR=$MPI_LIB \
    -DCMAKE_INSTALL_INCLUDEDIR=$MPI_INCLUDE \
%ifarch aarch64
    -DENABLE_NETGEN=NO \
%endif
    $gmsh_cmake_args

%cmake_build
%{_openmpi_unload}
%endif

### mpich version ###
%if %{with mpich}
%{_mpich_load}
export CXX=mpicxx
%define _vpath_builddir %{_target_platform}-mpich
%cmake \
    -DENABLE_MPI=YES \
    -DCMAKE_INSTALL_BINDIR=$MPI_BIN \
    -DCMAKE_INSTALL_LIBDIR=$MPI_LIB \
    -DCMAKE_INSTALL_INCLUDEDIR=$MPI_INCLUDE \
%ifarch aarch64
    -DENABLE_NETGEN=NO \
%endif
    $gmsh_cmake_args

%cmake_build
%{_mpich_unload}
%endif

# Built html documentation
%cmake_build --target html

# Fix to create correct debuginfo
cp -a src/parser/Gmsh.* %{_target_platform}
%if %{with openmpi}
cp -a src/parser/Gmsh.* %{_target_platform}-openmpi
%endif
%if %{with mpich}
cp -a src/parser/Gmsh.* %{_target_platform}-mpich
%endif

%install
%if %{with openmpi}
%define _vpath_builddir %{_target_platform}-openmpi
%cmake_install
%endif
%if %{with mpich}
%define _vpath_builddir %{_target_platform}-mpich
%cmake_install
%endif
%define _vpath_builddir %{_target_platform}
%cmake_install

# Remove static libraries
find %{buildroot} -type f -name libgmsh.a -exec rm -f {} \;

# Install icon and .desktop file
magick utils/icons/gmsh.png -scale 128 icon_128x128.png
install -Dpm 0644 icon_128x128.png  %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

# Install License.txt via %%license
rm -f %{buildroot}%{_defaultdocdir}/%{name}/LICENSE.txt

%files common
%doc %{_defaultdocdir}/%{name}/CREDITS.txt
%doc %{_defaultdocdir}/%{name}/README.txt
%doc %{_defaultdocdir}/%{name}/CHANGELOG.txt
%license LICENSE.txt
%{_mandir}/man1/gmsh.1.gz
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{python3_sitelib}/onelab.py
%{python3_sitelib}/__pycache__/onelab.*

%files doc
%license LICENSE.txt
%doc %{_defaultdocdir}/%{name}/tutorials
%doc %{_defaultdocdir}/%{name}/examples
%doc %{_defaultdocdir}/%{name}/%{name}.html
%doc %{_defaultdocdir}/%{name}/images/

%files
%{_bindir}/%{name}

%files devel
%{_includedir}/gmsh.h
%{_includedir}/gmshc.h
%{_includedir}/gmsh.h_cwrap
%{_includedir}/gmsh.f90
%{_libdir}/libgmsh.so

%files libs
%license LICENSE.txt
%{_libdir}/libgmsh.so.%{sover}*

%files -n python3-%{name}
%{python3_sitelib}/gmsh.py
%{python3_sitelib}/__pycache__/gmsh.*.pyc
%{python3_sitelib}/gmsh-%{version}*.dist-info/

%if %{with openmpi}
%files openmpi
%{_libdir}/openmpi/bin/%{name}

%files openmpi-devel
%{_includedir}/openmpi*/gmsh.h
%{_includedir}/openmpi*/gmshc.h
%{_includedir}/openmpi*/gmsh.h_cwrap
%{_includedir}/openmpi*/gmsh.f90
%{_libdir}/openmpi/lib/libgmsh.so

%files openmpi-libs
%license LICENSE.txt
%{_libdir}/openmpi/lib/libgmsh.so.%{sover}*
%endif

%if %{with mpich}
%files mpich
%{_libdir}/mpich/bin/%{name}

%files mpich-devel
%{_includedir}/mpich*/gmsh.h
%{_includedir}/mpich*/gmshc.h
%{_includedir}/mpich*/gmsh.h_cwrap
%{_includedir}/mpich*/gmsh.f90
%{_libdir}/mpich/lib/libgmsh.so

%files mpich-libs
%license LICENSE.txt
%{_libdir}/mpich/lib/libgmsh.so.%{sover}*
%endif

%changelog
%autochangelog
