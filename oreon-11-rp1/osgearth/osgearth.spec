%global source0_hash none

%global osg_ver 3.6.5

%global with_docs 1

Name:          osgearth
Version:       3.7.2
Release:       5%{?dist}
Summary:       Dynamic map generation toolkit for OpenSceneGraph

License:       LGPL-3.0-only
URL:           http://osgearth.org/
Source0:       https://github.com/gwaldron/osgearth/archive/%{name}-%{version}.tar.gz
# Fix mingw build failure due to header case mismatch
# Don't use _dupenv_s
Patch0:        osgearth_mingw.patch
# Support option to disable fastdxt build
Patch1:        osgearth_fastdxt.patch
# Unbundle liblerc, rapidjson
Patch2:        osgearth_unbundle.patch
# Link against liblerct
Patch3:        osgearth_link-lerc.patch
# Fix ambiguous namespace with gdal-3.12
Patch4:        osgearth-gdal-ns.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gdal-devel
BuildRequires: geos-devel
BuildRequires: glew-devel
BuildRequires: libcurl-devel
BuildRequires: liblerc-devel
BuildRequires: libzip-devel
BuildRequires: libzip-tools
BuildRequires: make
BuildRequires: OpenSceneGraph = %{osg_ver}
BuildRequires: OpenSceneGraph-devel
BuildRequires: protobuf-devel
BuildRequires: rapidjson-devel
BuildRequires: sqlite-devel
%if 0%{?with_docs}
BuildRequires: python3-recommonmark
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx-markdown-tables
BuildRequires: python3-myst-parser
%endif

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-curl
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-gdal
BuildRequires: mingw32-glew
BuildRequires: mingw32-glew-static
BuildRequires: mingw32-liblerc
BuildRequires: mingw32-OpenSceneGraph
BuildRequires: mingw32-protobuf

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-curl
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-gdal
BuildRequires: mingw64-glew
BuildRequires: mingw64-glew-static
BuildRequires: mingw64-liblerc
BuildRequires: mingw64-OpenSceneGraph
BuildRequires: mingw64-protobuf

Provides:      bundled(tinyxml)

Requires:      OpenSceneGraph = %{osg_ver}

%description
osgEarth is a C++ terrain rendering SDK. Just create a simple XML file, point
it at your imagery, elevation, and vector data, load it into your favorite
OpenSceneGraph application, and go! osgEarth supports all kinds of data and
comes with lots of examples to help you get up and running quickly and easily.

%package       devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      OpenSceneGraph-devel

%description   devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package       tools
Summary:       %{name} viewers and tools
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description   tools
The %{name}-tools contains viewers and data manipulation tools for %{name}.

%package       examples
Summary:       %{name} example applications
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      %{name}-examples-data = %{version}-%{release}

%description   examples
The %{name}-examples contains %{name} example applications.

%package       examples-data
Summary:       Data for %{name} example applications
BuildArch:     noarch
Requires:      %{name}-examples = %{version}-%{release}

%description   examples-data
The %{name}-examples-data contains data for the %{name} example
applications.

%if 0%{?with_docs}
%package doc
Summary:       Documentation files for %{name}
Provides:      bundled(jquery)
BuildArch:     noarch

%description doc
The %{name}-doc package contains documentation files for developing
applications that use %{name}.
%endif

%package -n mingw32-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw32-%{name}
MinGW Windows %{name} library.

%package -n mingw32-%{name}-tools
Summary:       MinGW Windows %{name} tools
BuildArch:     noarch

%description -n mingw32-%{name}-tools
MinGW Windows %{name} tools.

%package -n mingw64-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw64-%{name}
MinGW Windows %{name} library.

%package -n mingw64-%{name}-tools
Summary:       MinGW Windows %{name} tools
BuildArch:     noarch

%description -n mingw64-%{name}-tools
MinGW Windows %{name} tools.

%{?mingw_debug_package}

%prep
%autosetup -p1 -n %{name}-%{name}-%{version}

# Remove non-free content
rm -rf data/loopix

%build
# Native build
export CXXFLAGS="%{optflags} -Wno-error=format-security"
# Disable fastdxt driver on non x86 arches, requires x86 intrinsics
%ifnarch i686 x86_64
%cmake -DDISABLE_FASTDXT=ON
%else
%cmake
%endif
%cmake_build
%if 0%{?with_docs}
make -C docs html
rm -f docs/build/html/.buildinfo
%endif

# MinGW build
export MINGW32_CXXFLAGS="%{mingw32_cflags} -msse2 -Wno-error=format-security -fpermissive"
export MINGW64_CXXFLAGS="%{mingw64_cflags} -msse2 -Wno-error=format-security -fpermissive"
%mingw_cmake
%mingw_make_build

%install
%cmake_install
%mingw_make_install

install -Dd %{buildroot}%{_datadir}/%{name}
cp -a data %{buildroot}%{_datadir}/%{name}/data
cp -a tests %{buildroot}%{_datadir}/%{name}/tests

%mingw_debug_install_post

%files
%license LICENSE.txt
%{_libdir}/libosgEarth*.so.3.7.2
%{_libdir}/libosgEarth*.so.171
%{_libdir}/osgPlugins-%{osg_ver}/osgdb_*.so

%files devel
%{_includedir}/osgEarth/
%{_includedir}/osgEarthDrivers/
%{_includedir}/osgEarthImGui/
%{_libdir}/libosgEarth.so
%{_libdir}/libosgEarthImGui.so
%{_libdir}/cmake/osgearth/

%files tools
%{_bindir}/osgearth_atlas
%{_bindir}/osgearth_bakefeaturetiles
%{_bindir}/osgearth_boundarygen
%{_bindir}/osgearth_conv
%{_bindir}/osgearth_imgui
%{_bindir}/osgearth_tfs
%{_bindir}/osgearth_version
%{_bindir}/osgearth_viewer

%files examples
%{_bindir}/osgearth_3pv
%{_bindir}/osgearth_annotation
%{_bindir}/osgearth_clamp
%{_bindir}/osgearth_featurefilter
%{_bindir}/osgearth_features
%{_bindir}/osgearth_heatmap
%{_bindir}/osgearth_infinitescroll
%{_bindir}/osgearth_los
%{_bindir}/osgearth_map
%{_bindir}/osgearth_minimap
%{_bindir}/osgearth_mrt
%{_bindir}/osgearth_occlusionculling
%{_bindir}/osgearth_simple
%{_bindir}/osgearth_skyview
%{_bindir}/osgearth_terrainprofile
%{_bindir}/osgearth_video

%files examples-data
%{_datadir}/%{name}

%if 0%{?with_docs}
%files doc
%license LICENSE.txt
%doc docs/build/html
%endif

%files -n mingw32-%{name}
%license LICENSE.txt
%{mingw32_bindir}/libosgEarth*.dll
%{mingw32_bindir}/osgPlugins-%{osg_ver}/*.dll
%{mingw32_libdir}/libosgEarth*.dll.a
%{mingw32_libdir}/cmake/osgearth/
%{mingw32_includedir}/osgEarth*/

%files -n mingw32-%{name}-tools
%{mingw32_bindir}/*.exe

%files -n mingw64-%{name}
%license LICENSE.txt
%{mingw64_bindir}/libosgEarth*.dll
%{mingw64_bindir}/osgPlugins-%{osg_ver}/*.dll
%{mingw64_libdir}/libosgEarth*.dll.a
%{mingw64_libdir}/cmake/osgearth/
%{mingw64_includedir}/osgEarth*/

%files -n mingw64-%{name}-tools
%{mingw64_bindir}/*.exe

%changelog
%autochangelog
