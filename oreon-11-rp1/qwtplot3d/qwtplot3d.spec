%global source0_hash 6bd0afe01dde94d19cb6c19844cdf58abadbeac099a2130fc8076d4a73edaebd

%global commit 3ba6d52783752c97793ab7fde14d204fcf6348e6
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20260129

Name:           qwtplot3d
Epoch:          1
Version:        0.3.0
Release:        13.%{commitdate}git%{shortcommit}%{?dist}
Summary:        Extended version of the original QwtPlot3D library
License:        Zlib
URL:            https://github.com/SciDAVis/%{name}
Source0:        https://gitlab.com/anto.trande/qwtplot3d/-/archive/%{commit}/%{name}-%{commit}.tar.gz

Patch0:         %{name}-qt6-build.patch
Patch1:         %{name}-qt5-build.patch

# Qt6
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  qt6-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qt5compat-devel
# Qt5
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  qt5-rpm-macros
BuildRequires:  qt5-qtbase-devel
#
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  gl2ps-devel
BuildRequires:  gcc-c++
BuildRequires:  chrpath

%description
QwtPlot3D is not a program, but a feature-rich Qt/OpenGL-based C++
programming library, providing essentially a bunch of 3D-widgets for
programmers.

# Qt6
%package        -n %{name}-qt6
Summary:        Extended version of the original QwtPlot3D Qt6 library

%description    -n %{name}-qt6
QwtPlot3D is not a program, but a feature-rich Qt/OpenGL-based C++
programming library, providing essentially a bunch of 3D-widgets for
programmers.

%package        -n %{name}-qt6-devel
Summary:        Development files for %{name}
Requires:       %{name}-qt6%{?_isa} = %{epoch}:%{version}-%{release}

%description    -n %{name}-qt6-devel
The %{name}6-devel package contains Qt6 libraries and header files for
developing applications that use %{name}-qt6.
#

# Qt5
%package        -n %{name}-qt5
Summary:        Extended version of the original QwtPlot3D Qt5 library
Provides:       %{name}-qt5%{?_isa} = %{epoch}:%{version}-%{release}

%description    -n %{name}-qt5
QwtPlot3D is not a program, but a feature-rich Qt/OpenGL-based C++
programming library, providing essentially a bunch of 3D-widgets for
programmers.

%package        -n %{name}-qt5-devel
Summary:        Development files for %{name}
Requires:       %{name}-qt5%{?_isa} = %{epoch}:%{version}-%{release}
Provides:       %{name}-qt5-devel%{?_isa} = %{epoch}:%{version}-%{release}

%description    -n %{name}-qt5-devel
The %{name}6-devel package contains Qt5 libraries and header files for
developing applications that use %{name}-qt5.
#

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc -n %{name}-%{commit}

# Unbundle gl2ps
rm -rf %{name}-%{commit}/3rdparty/gl2ps

cp -a %{name}-%{commit} %{name}-qt5
mv %{name}-%{commit} %{name}-qt6

pushd %{name}-qt6
%patch -P 0 -p1 -b .backup
popd

pushd %{name}-qt5
%patch -P 1 -p1 -b .backup
popd

%build
pushd %{name}-qt6
export CXXFLAGS="%{build_cxxflags}"
%cmake -Wno-dev \
 -DPKG_CONFIG_ARGN:STRING="%(pkg-config --cflags Qt6Gui) %(pkg-config --cflags Qt6Core) %(pkg-config --cflags Qt6OpenGL)" \
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
 -DCMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} -lGLU" \
 -DCMAKE_INSTALL_LIBDIR:PATH=%{_qt6_libdir} -DCMAKE_INSTALL_INCLUDEDIR:PATH=%{_qt6_headerdir}/%{name}-qt6
%cmake_build
popd

pushd %{name}-qt5
export CXXFLAGS="%{build_cxxflags}"
%cmake -Wno-dev \
 -DPKG_CONFIG_ARGN:STRING="%(pkg-config --cflags Qt5Gui) %(pkg-config --cflags Qt5Core) %(pkg-config --cflags Qt5OpenGL)" \
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
 -DCMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} -lGLU" \
 -DCMAKE_INSTALL_LIBDIR:PATH=%{_qt5_libdir} -DCMAKE_INSTALL_INCLUDEDIR:PATH=%{_qt5_headerdir}/%{name}-qt5
%cmake_build
popd

%install
pushd %{name}-qt6
%cmake_install
# Install executable examples files
mkdir -p %{buildroot}%{_libexecdir}/%{name}-qt6
install -pm 755 %{__cmake_builddir}/examples/simpleplot/simpleplot %{buildroot}%{_libexecdir}/%{name}-qt6/
install -pm 755 %{__cmake_builddir}/examples/axes/axes %{buildroot}%{_libexecdir}/%{name}-qt6/
install -pm 755 %{__cmake_builddir}/examples/enrichments/enrichments %{buildroot}%{_libexecdir}/%{name}-qt6/
install -pm 755 %{__cmake_builddir}/examples/autoswitch/autoswitch %{buildroot}%{_libexecdir}/%{name}-qt6/
install -pm 755 %{__cmake_builddir}/examples/mesh2/mesh2 %{buildroot}%{_libexecdir}/%{name}-qt6/

mkdir -p %{buildroot}%{_qt6_headerdir}/%{name}-qt6
install -pm 644 include/*  %{buildroot}%{_qt6_headerdir}/%{name}-qt6/
mv %{buildroot}%{_qt6_headerdir}/%{name}-qt6/qwt3d_version.h.in %{buildroot}%{_qt6_headerdir}/%{name}-qt6/qwt3d_version.h
sed -e 's|@PROJECT_VERSION_MAJOR@|0|g' -i %{buildroot}%{_qt6_headerdir}/%{name}-qt6/qwt3d_version.h
sed -e 's|@PROJECT_VERSION_MINOR@|3|g' -i %{buildroot}%{_qt6_headerdir}/%{name}-qt6/qwt3d_version.h
sed -e 's|@PROJECT_VERSION_PATCH@|0|g' -i %{buildroot}%{_qt6_headerdir}/%{name}-qt6/qwt3d_version.h

# Remove rpaths
chrpath -d %{buildroot}%{_libexecdir}/%{name}-qt6/*
popd

pushd %{name}-qt5
%cmake_install
# Install executable examples files
mkdir -p %{buildroot}%{_libexecdir}/%{name}-qt5
install -pm 755 %{__cmake_builddir}/examples/simpleplot/simpleplot %{buildroot}%{_libexecdir}/%{name}-qt5/
install -pm 755 %{__cmake_builddir}/examples/axes/axes %{buildroot}%{_libexecdir}/%{name}-qt5/
install -pm 755 %{__cmake_builddir}/examples/enrichments/enrichments %{buildroot}%{_libexecdir}/%{name}-qt5/
install -pm 755 %{__cmake_builddir}/examples/autoswitch/autoswitch %{buildroot}%{_libexecdir}/%{name}-qt5/
install -pm 755 %{__cmake_builddir}/examples/mesh2/mesh2 %{buildroot}%{_libexecdir}/%{name}-qt5/

mkdir -p %{buildroot}%{_qt5_headerdir}/%{name}-qt5
install -pm 644 include/*  %{buildroot}%{_qt5_headerdir}/%{name}-qt5/
mv %{buildroot}%{_qt5_headerdir}/%{name}-qt5/qwt3d_version.h.in %{buildroot}%{_qt5_headerdir}/%{name}-qt5/qwt3d_version.h
sed -e 's|@PROJECT_VERSION_MAJOR@|0|g' -i %{buildroot}%{_qt5_headerdir}/%{name}-qt5/qwt3d_version.h
sed -e 's|@PROJECT_VERSION_MINOR@|3|g' -i %{buildroot}%{_qt5_headerdir}/%{name}-qt5/qwt3d_version.h
sed -e 's|@PROJECT_VERSION_PATCH@|0|g' -i %{buildroot}%{_qt5_headerdir}/%{name}-qt5/qwt3d_version.h

# Remove rpaths
chrpath -d %{buildroot}%{_libexecdir}/%{name}-qt5/*
popd

# Qt6
%files -n %{name}-qt6
%license %{name}-qt6/COPYING %{name}-qt6/LICENSE
%doc %{name}-qt6/README.md
%{_qt6_libdir}/lib%{name}-qt6.so.0.3.0
%{_qt6_libdir}/lib%{name}-qt6.so.0.3

%files -n %{name}-qt6-devel
%{_qt6_headerdir}/%{name}-qt6/
%{_qt6_libdir}/lib%{name}-qt6.so
%{_libexecdir}/%{name}-qt6/
#

# Qt5
%files -n %{name}-qt5
%license %{name}-qt5/COPYING %{name}-qt5/LICENSE
%doc %{name}-qt5/README.md
%{_qt5_libdir}/lib%{name}-qt5.so.0.3.0
%{_qt5_libdir}/lib%{name}-qt5.so.0.3

%files -n %{name}-qt5-devel
%{_qt5_headerdir}/%{name}-qt5/
%{_qt5_libdir}/lib%{name}-qt5.so
%{_libexecdir}/%{name}-qt5/
#

%changelog
%autochangelog
