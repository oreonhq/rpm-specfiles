%global source0_hash 6752a6fcf6f8b20c808fe27fff8cb5ba5b40c6bec144bd118e69f2e90648868e

%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}

# Don't abort on compilation errors of the example python snippets
%global _python_bytecompile_errors_terminate_build 0

%if 0%{?el6}
	%ifarch ppc64
		%global build_mpich 0
	%else
		%global build_mpich 1
	%endif
%else
	%global build_mpich 1
%endif

%if 0%{?fedora} >= 40
%ifarch %{ix86}
%global build_openmpi 0
%global build_mpich   0
%else
%global build_openmpi 1
%endif
%else
%global build_openmpi 1
%endif

Name:           netgen-mesher
# Also update version in netgen_fallback-version.patch!
Version:        6.2.2601
Release:        1%{?dist}
Summary:        Automatic mesh generation tool
# FIXME https://github.com/NGSolve/netgen/issues/226
ExcludeArch:    %{ix86} aarch64

License:        LGPL-2.0-only
URL:            https://github.com/NGSolve/netgen
Source0:        https://github.com/NGSolve/netgen/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        netgen-mesher.png
Source2:        netgen-mesher.desktop
# Source99:       https://raw.githubusercontent.com/NGSolve/pybind11/7ec2ddfc95f65d1e986d359466a6c254aa514ef3/tools/pybind11Tools.cmake
# Source100:      https://raw.githubusercontent.com/NGSolve/pybind11/7ec2ddfc95f65d1e986d359466a6c254aa514ef3/tools/FindPythonLibsNew.cmake

# Rename shared libaries (the original names are often way too generic), add library version
Patch1:         0002-Rename-libraries-add-library-versions.patch
# Make some includes relative (needed for when headers are in -private subpackage)
Patch2:         0004-Make-some-includes-relative.patch
# Rename binary in cmake so that exported modules work correctly
Patch3:         0010-rename-netgen-binary.patch
# Link against libjpeg
Patch4:         netgen_libjpeg.patch
# Fix fallback version
# See https://bugzilla.redhat.com/show_bug.cgi?id=1993574#c11
Patch5:         netgen_fallback-version.patch
# Fix Status typedef symbol collision by re-ordering includes
# /usr/include/mpich-x86_64/mpicxx.h:160:18: error: expected identifier before ‘int’
#   160 |     friend class Status;
Patch6:         netgen_include-order.patch
# Fix invalid egg-info version
Patch7:         netgen-mesher_egg-info-version.patch
# Port bundled togl to tk9
# Patch8:         netgen-togl-tk9.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  tk-devel < 1:9
BuildRequires:  opencascade-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  metis-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  libXmu-devel
BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:  python3-devel
BuildRequires:  python-setuptools
BuildRequires:  pybind11-devel
BuildRequires:  git

# Bundles a modified version of togl-2.1
Provides: bundled(tcl-togl) = 2.1

Requires:       %{name}-common = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
NETGEN is an automatic 3d tetrahedral mesh generator. It accepts input from
constructive solid geometry (CSG) or boundary representation (BRep) from STL
file format. The connection to a geometry kernel allows the handling of IGES
and STEP files. NETGEN contains modules for mesh optimization and hierarchical
mesh refinement.

%package        common
Summary:        Common files for netgen
Requires:       hicolor-icon-theme
Requires:       tix
BuildArch:      noarch

%description    common
Common files for netgen.

%package        libs
Summary:        Netgen libraries

%description    libs
Netgen libraries.

%package        devel
Summary:        Development files for netgen
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for netgen.

%package        devel-private
Summary:        Private headers of netgen
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    devel-private
Private headers of netgen, needed to build certain netgen based software
packages.

%package -n     python3-%{name}
Summary:        Python3 interface for netgen
%{?python_provide:%python_provide python3-netgen}
Requires:       %{name}-openmpi-libs%{?_isa} = %{version}-%{release}

%description -n python3-%{name}
Python3 interface for netgen.

###############################################################################

%if %{build_openmpi}
%package        openmpi
Summary:        Netgen compiled against openmpi
BuildRequires:  environment-modules
BuildRequires:  openmpi-devel
BuildRequires:  python3-mpi4py-openmpi
# Require explicitly for dir ownership and to guarantee the pickup of the right runtime
Requires:       %{name}-common = %{version}-%{release}
Requires:       %{name}-openmpi-libs%{?_isa} = %{version}-%{release}

%description    openmpi
Netgen compiled against openmpi.

%package        openmpi-libs
Summary:        Netgen libraries compiled against openmpi

%description    openmpi-libs
Netgen libraries compiled against openmpi.

%package        openmpi-devel
Summary:        Development files for Netgen compiled against openmpi
# Require explicitly for dir ownership
Requires:       openmpi-devel
Requires:       %{name}-openmpi%{?_isa} = %{version}-%{release}

%description    openmpi-devel
Development files for Netgen compiled against openmpi.

%package -n     python3-%{name}-openmpi
Summary:        Python3 interface for netgen compiled against openmpi
%{?python_provide:%python_provide python3-netgen-openmpi}
Requires:       %{name}-openmpi-libs%{?_isa} = %{version}-%{release}

%description -n python3-%{name}-openmpi
Python3 interface for netgen compiled against openmpi.

%endif

###############################################################################

%if %{build_mpich}
%package        mpich
Summary:        Netgen compiled against mpich
BuildRequires:  environment-modules
BuildRequires:  mpich-devel
BuildRequires:  python3-mpi4py-mpich
# Require explicitly for dir ownership and to guarantee the pickup of the right runtime
Requires:       %{name}-common = %{version}-%{release}
Requires:       %{name}-mpich-libs%{?_isa} = %{version}-%{release}

%description    mpich
Netgen compiled against mpich.

%package        mpich-libs
Summary:        Netgen libraries compiled against mpich

%description    mpich-libs
Netgen libraries compiled against mpich.

%package        mpich-devel
Summary:        Development files for Netgen compiled against mpich
# Require explicitly for dir ownership
Requires:       mpich-devel
Requires:       %{name}-mpich%{?_isa} = %{version}-%{release}

%description    mpich-devel
Development files for Netgen compiled against mpich.

%package -n     python3-%{name}-mpich
Summary:        Python3 interface for netgen compiled against mpich
%{?python_provide:%python_provide python3-netgen-mpich}
Requires:       %{name}-openmpi-libs%{?_isa} = %{version}-%{release}

%description -n python3-%{name}-mpich
Python3 interface for netgen compiled against mpich.

%endif

###############################################################################

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n netgen-%{version}

# Pull in minimal cmake files from NGSolv pybind11 project to make this one happy.
# install -pm 0744 %{SOURCE99} cmake/
# install -pm 0744 %{SOURCE100} cmake/cmake_modules/

%build
### serial version ###
%define _vpath_builddir %{_target_platform}
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DNG_INSTALL_SUFFIX=netgen_mesher \
  -DUSE_NATIVE_ARCH=OFF \
  -DUSE_SUPERBUILD=OFF \
  -DNG_INSTALL_DIR_INCLUDE=%{_includedir}/%{name} \
  -DNG_INSTALL_DIR_LIB=%{_libdir} \
  -DNG_INSTALL_DIR_CMAKE=%{_libdir}/cmake/%{name} \
  -DNG_INSTALL_DIR_PYTHON=%{python3_sitearch} \
  -DPREFER_SYSTEM_PYBIND11=ON \
  -DUSE_JPEG=1 -DUSE_OCC=1 \
  -DOpenGL_GL_PREFERENCE=GLVND
%cmake_build

### openmpi version ###
%if %{build_openmpi}
%define _vpath_builddir %{_target_platform}-openmpi
%{_openmpi_load}
export CXX=mpicxx
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DNG_INSTALL_SUFFIX=netgen_mesher \
  -DUSE_NATIVE_ARCH=OFF \
  -DUSE_SUPERBUILD=OFF \
  -DNG_INSTALL_DIR_INCLUDE=%{_includedir}/openmpi/%{name} \
  -DNG_INSTALL_DIR_BIN=%{_libdir}/openmpi/bin/ \
  -DNG_INSTALL_DIR_LIB=%{_libdir}/openmpi/lib/ \
  -DNG_INSTALL_DIR_CMAKE=%{_libdir}/openmpi/lib/cmake/%{name} \
  -DNG_INSTALL_DIR_PYTHON=%{_libdir}/openmpi/python%{python3_version}/site-packages \
  -DPREFER_SYSTEM_PYBIND11=ON \
  -DUSE_JPEG=1 -DUSE_OCC=1 -DUSE_MPI=1
%cmake_build
%{_openmpi_unload}
%endif

### mpich version ###
%if %{build_mpich}
%define _vpath_builddir %{_target_platform}-mpich
%{_mpich_load}
export CXX=mpicxx
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DNG_INSTALL_SUFFIX=netgen_mesher \
  -DUSE_NATIVE_ARCH=OFF \
  -DUSE_SUPERBUILD=OFF \
  -DNG_INSTALL_DIR_INCLUDE=%{_includedir}/mpich/%{name} \
  -DNG_INSTALL_DIR_BIN=%{_libdir}/mpich/bin/ \
  -DNG_INSTALL_DIR_LIB=%{_libdir}/mpich/lib/ \
  -DNG_INSTALL_DIR_CMAKE=%{_libdir}/mpich/lib/cmake/%{name} \
  -DNG_INSTALL_DIR_PYTHON=%{_libdir}/mpich/python%{python3_version}/site-packages \
  -DPREFER_SYSTEM_PYBIND11=ON \
  -DUSE_JPEG=1 -DUSE_OCC=1 -DUSE_MPI=1
%cmake_build
%{_mpich_unload}
%endif

%install
%define writepkgconfig() \
install -d -m 0755 %{buildroot}/$MPI_LIB/pkgconfig; \
cat > %{buildroot}/$MPI_LIB/pkgconfig/%{name}.pc << EOF\
prefix=%{_prefix}\
exec_prefix=${prefix}\
libdir=$MPI_LIB\
includedir=$MPI_INCLUDE/%{name}\
\
Name: %{name}\
Description:  %{summary}\
Version: %{version}\
Libs: -L\\\${libdir} -lnglib\
Libs.private: -lngcgs -lnggeom2d -lngmesh -lngocc -lngstl\
Cflags: -I\\\${includedir}\
EOF\
%{nil}

### openmpi version ###
%if %{build_openmpi}
%define _vpath_builddir %{_target_platform}-openmpi
%{_openmpi_load}
%cmake_install
%writepkgconfig
%{_openmpi_unload}
%endif

### mpich version ###
%if %{build_mpich}
%define _vpath_builddir %{_target_platform}-mpich
%{_mpich_load}
%cmake_install
%writepkgconfig
%{_mpich_unload}
%endif

### serial version ###
%define _vpath_builddir %{_target_platform}
%cmake_install
export MPI_LIB=%{_libdir}
export MPI_INCLUDE=%{_includedir}
%writepkgconfig

# Install icon and desktop file
install -Dpm 0644 %SOURCE1 %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
desktop-file-install --dir %{buildroot}/%{_datadir}/applications/ %SOURCE2

# Delete the doc folder, the files are in %%doc below
rm -rf %{buildroot}/%{_prefix}/doc

# Install private headers
(
cd libsrc
find \( -name *.hpp -or -name *.hxx -or -name *.h -or -name *.ixx -or -name *.jxx \) -exec install -Dpm 0644 {} %{buildroot}%{_includedir}/%{name}/private/{} \;
)

# Install the nglib.h header
install -Dpm 0644 nglib/nglib.h %{buildroot}%{_includedir}/%{name}/nglib.h

# R

%files common
%doc AUTHORS doc/ng4.pdf
%license LICENSE
%{_datadir}/netgen_mesher/
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/netgen-mesher

%files libs
%{_libdir}/libngcore.so.6.2
%{_libdir}/libnggui.so.6.2
%{_libdir}/libnglib.so.6.2

%files devel
%{_includedir}/%{name}
%exclude %{_includedir}/%{name}/private
%{_libdir}/libngcore.so
%{_libdir}/libnggui.so
%{_libdir}/libnglib.so
%{_libdir}/libngtogl.a
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/*

%files devel-private
%{_includedir}/%{name}/private

%files -n python3-%{name}
%{python3_sitearch}/pyngcore/
%{python3_sitearch}/netgen_mesher/
%{python3_sitearch}/netgen_mesher-py3.egg-info

%if %{build_openmpi}
%files openmpi
%{_libdir}/openmpi/bin/netgen-mesher

%files openmpi-libs
%{_libdir}/openmpi/lib/libngcore.so.6.2
%{_libdir}/openmpi/lib/libnggui.so.6.2
%{_libdir}/openmpi/lib/libnglib.so.6.2

%files openmpi-devel
%{_includedir}/openmpi*/%{name}
%{_libdir}/openmpi/lib/libngcore.so
%{_libdir}/openmpi/lib/libnggui.so
%{_libdir}/openmpi/lib/libnglib.so
%{_libdir}/openmpi/lib/libngtogl.a
%{_libdir}/openmpi/lib/pkgconfig/%{name}.pc
%{_libdir}/openmpi/lib/cmake/%{name}/

%files -n python3-%{name}-openmpi
%{_libdir}/openmpi/python%{python3_version}/site-packages/pyngcore/
%{_libdir}/openmpi/python%{python3_version}/site-packages/netgen_mesher/
%{_libdir}/openmpi/python%{python3_version}/site-packages/netgen_mesher-py3.egg-info
%endif

%if %{build_mpich}
%files mpich
%{_libdir}/mpich/bin/netgen-mesher

%files mpich-libs
%{_libdir}/mpich/lib/libngcore.so.6.2
%{_libdir}/mpich/lib/libnggui.so.6.2
%{_libdir}/mpich/lib/libnglib.so.6.2

%files mpich-devel
%{_includedir}/mpich*/%{name}
%{_libdir}/mpich/lib/libngcore.so
%{_libdir}/mpich/lib/libnggui.so
%{_libdir}/mpich/lib/libnglib.so
%{_libdir}/mpich/lib/libngtogl.a
%{_libdir}/mpich/lib/pkgconfig/%{name}.pc
%{_libdir}/mpich/lib/cmake/%{name}/

%files -n python3-%{name}-mpich
%{_libdir}/mpich/python%{python3_version}/site-packages/pyngcore/
%{_libdir}/mpich/python%{python3_version}/site-packages/netgen_mesher/
%{_libdir}/mpich/python%{python3_version}/site-packages/netgen_mesher-py3.egg-info
%endif

%changelog
%autochangelog
