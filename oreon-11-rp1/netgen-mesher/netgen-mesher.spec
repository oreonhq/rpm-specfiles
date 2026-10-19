%global source0_hash 47c587bb49f89707fe8f9767c2283398312e7a7c44334e661d2c185b40de4603
%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}
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
%global build_openmpi 1
Name:           netgen-mesher
Version:        6.2.2607
Release:        1%{?dist}
Summary:        Automatic mesh generation tool
ExcludeArch:    %{ix86} aarch64
License:        LGPL-2.0-only
URL:            https://github.com/NGSolve/netgen
Source0:        https://github.com/NGSolve/netgen/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        netgen-mesher.png
Source2:        netgen-mesher.desktop
Patch1:         0002-Rename-libraries-add-library-versions.patch
Patch2:         0004-Make-some-includes-relative.patch
Patch3:         0010-rename-netgen-binary.patch
Patch4:         netgen_libjpeg.patch
Patch5:         netgen_fallback-version.patch
Patch6:         netgen_include-order.patch
Patch7:         netgen-mesher_egg-info-version.patch
Provides: bundled(tcl-togl) = 2.1
Requires:       %{name}-common = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:  environment-modules
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  libXmu-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  metis-devel
BuildRequires:  opencascade-devel
BuildRequires:  openmpi-devel
BuildRequires:  pybind11-devel
BuildRequires:  python-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3-mpi4py-openmpi
BuildRequires:  tk-devel
# /oreon:deps
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

%package        openmpi
Summary:        Netgen compiled against openmpi
BuildRequires:  environment-modules
BuildRequires:  openmpi-devel
BuildRequires:  python3-mpi4py-openmpi
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

###############################################################################

###############################################################################

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir netgen-%{version}
%oreon_prep
%build

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
%define _vpath_builddir %{_target_platform}-openmpi
%{_openmpi_load}
%cmake_install
%writepkgconfig
%{_openmpi_unload}
%define _vpath_builddir %{_target_platform}
%cmake_install
export MPI_LIB=%{_libdir}
export MPI_INCLUDE=%{_includedir}
%writepkgconfig
install -Dpm 0644 %SOURCE1 %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
desktop-file-install --dir %{buildroot}/%{_datadir}/applications/ %SOURCE2
rm -rf %{buildroot}/%{_prefix}/doc
(
cd libsrc
find \( -name *.hpp -or -name *.hxx -or -name *.h -or -name *.ixx -or -name *.jxx \) -exec install -Dpm 0644 {} %{buildroot}%{_includedir}/%{name}/private/{} \;
)
install -Dpm 0644 nglib/nglib.h %{buildroot}%{_includedir}/%{name}/nglib.h
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n netgen-mesher-common -f %{oreon_filedir}/netgen-mesher-common.list
%files -n netgen-mesher-libs -f %{oreon_filedir}/netgen-mesher-libs.list
%files -n netgen-mesher-devel -f %{oreon_filedir}/netgen-mesher-devel.list
%files -n netgen-mesher-devel-private -f %{oreon_filedir}/netgen-mesher-devel-private.list
%files -n python3-netgen-mesher -f %{oreon_filedir}/python3-netgen-mesher.list
%files -n netgen-mesher-openmpi -f %{oreon_filedir}/netgen-mesher-openmpi.list
%files -n netgen-mesher-openmpi-libs -f %{oreon_filedir}/netgen-mesher-openmpi-libs.list
%files -n netgen-mesher-openmpi-devel -f %{oreon_filedir}/netgen-mesher-openmpi-devel.list
%files -n python3-netgen-mesher-openmpi -f %{oreon_filedir}/python3-netgen-mesher-openmpi.list

%changelog

%autochangelog
