%global source0_hash a0e17eb352c32aa2f8e7123cf75ec5633d25e230112d4dc2ba2b7024011e2615
%bcond_without python
%bcond check 1
%global usd 0
%global forgeurl https://github.com/f3d-app/f3d
Version:        3.5.0
%forgemeta
Name:           f3d
Release:        1%{?dist}
Summary:        Fast and minimalist 3D viewer
License:        BSD-3-Clause
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch: %{ix86}
%if %{with check}
%endif
Requires:       hicolor-icon-theme
Requires:       shared-mime-info
# oreon:deps
BuildRequires:  alembic-devel
BuildRequires:  assimp-devel
BuildRequires:  cmake
BuildRequires:  cmake(draco)
BuildRequires:  cxxopts-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  imath-devel
BuildRequires:  json-devel
BuildRequires:  lapack-devel
BuildRequires:  libappstream-glib
BuildRequires:  mesa-dri-drivers
BuildRequires:  ninja-build
BuildRequires:  opencascade-devel
BuildRequires:  python3-devel
BuildRequires:  python3-pybind11
BuildRequires:  python3-pytest
BuildRequires:  vtk-devel
BuildRequires:  xorg-x11-drv-dummy
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
F3D is a fast and minimalist 3D viewer desktop application. It supports many
file formats, from digital content to scientific datasets (including glTF, USD,
STL, STEP, PLY, OBJ, FBX, Alembic), can show animations and support thumbnails
and many rendering and texturing options including real time physically based
rendering and raytracing.

It is fully controllable from the command line and support configuration files.
It can provide thumbnails, support interactive hotkeys, drag&drop and
integration into file managers.

F3D also contains the libf3d, a simple library to render meshes, with C++ and
Python Bindings, as well as experimental Java and Javascript bindings.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains development files for %{name}.

%if %{with python}
%package        python3
Summary:        Python 3 bindings for the %{name}
BuildRequires:  python3-devel
BuildRequires:  python3-pybind11
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       python3-%{name} = %{version}-%{release}
%description    python3
This package contains Python 3 bindings for %{name}.
%endif

%ifarch %{java_arches}
%package        java
Summary:        Java bindings for the %{name}
BuildRequires:  javapackages-tools
BuildRequires:  java-25-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    java
This package contains Java bindings for %{name}.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1
# remove bundled libraries of cxxopts and nlohmann_json
rm -rf external/{cxxopts,nlohmann_json}
# fix install location for -java sub-package
sed -i 's|${CMAKE_INSTALL_LIBDIR}|${CMAKE_INSTALL_LIBDIR}/f3d|' java/CMakeLists.txt
sed -i 's|share/java|%{_jnidir}|' java/CMakeLists.txt

%build

%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DF3D_PLUGINS_STATIC_BUILD=OFF \
    -DF3D_PLUGINS_INSTALL_DIR=%{_libdir}/f3d/plugins \
    -DF3D_USE_EXTERNAL_CXXOPTS=ON \
    -DF3D_USE_EXTERNAL_NLOHMANN_JSON=ON \
    -DF3D_LINUX_INSTALL_DEFAULT_CONFIGURATION_FILE_IN_PREFIX=ON \
    -DF3D_LINUX_GENERATE_MAN=ON \
    -DF3D_MODULE_RAYTRACING=OFF \
    -DF3D_MODULE_EXTERNAL_RENDERING=OFF \
    -DF3D_PLUGIN_BUILD_ALEMBIC=ON \
    -DF3D_PLUGIN_BUILD_ASSIMP=ON \
    -DF3D_PLUGIN_BUILD_DRACO=ON \
    -DF3D_PLUGIN_BUILD_EXODUS=ON \
    -DF3D_PLUGIN_BUILD_OCCT=ON \
    -DF3D_PLUGIN_OCCT_COLORING_SUPPORT=ON \
    -DF3D_PLUGIN_BUILD_VDB=OFF \
%if %{with python}
    -DF3D_BINDINGS_PYTHON=ON \
%endif
%ifarch %{java_arches}
    -DF3D_BINDINGS_JAVA=ON \
%endif
%if %{with check}
    -DBUILD_TESTING=ON \
    -DF3D_TESTING_ENABLE_OSMESA_TESTS=OFF \
%endif
    -DCMAKE_SKIP_INSTALL_RPATH=ON \
%cmake_build
%install
%cmake_install
%cmake_install --component mimetypes
%cmake_install --component sdk
%cmake_install --component configuration
rm -r %{buildroot}%{_datadir}/doc/F3D
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with check}
export MESA_DEBUG=silent
export LIBGL_ALWAYS_SOFTWARE=true
export MESA_LOADER_DRIVER_OVERRIDE=llvmpipe
xvfb-run -a bash -c "%ctest"
%endif
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%files -f %{oreon_filedir}/main.list
%files -n f3d-devel -f %{oreon_filedir}/f3d-devel.list
%files -n f3d-python3 -f %{oreon_filedir}/f3d-python3.list

%changelog

%autochangelog
