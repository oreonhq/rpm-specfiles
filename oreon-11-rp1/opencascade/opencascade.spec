%global source0_hash 0d6913eae4bcc09a3653ceced6dda1aec11c35a1513d4c06762c9b002092c68a
%global major 8
%global minor 0
%global patch 1
%global ver_under %{major}_%{minor}_%{patch}
Name:           opencascade
Version:        8.0.1
Release:        1%{?dist}
Summary:        SDK intended for development of applications dealing with 3D CAD data
License:        LGPL-2.1-only WITH OCCT-exception-1.0
URL:            https://www.opencascade.com/content/overview
Source0:        https://github.com/Open-Cascade-SAS/OCCT/archive/refs/tags/V%{ver_under}.tar.gz#/%{name}-%{version}.tgz
Source1:        DRAWEXE.1
Source2:        opencascade-draw.desktop
Source3:        occ-256.png
Source4:        occ-128.png
Source5:        occ-64.png
Source6:        occ-48.png
Patch0:         occt-config.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(RapidJSON)
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  freeimage-devel
BuildRequires:  ftgl-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gl2ps-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXdmcp-devel
BuildRequires:  libXi-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXres-devel
BuildRequires:  libXtst-devel
BuildRequires:  libXv-devel
BuildRequires:  libgomp
BuildRequires:  libxkbfile-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  ninja-build
BuildRequires:  rapidjson-static
BuildRequires:  tbb-devel
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRequires:  vtk-devel
BuildRequires:  xorg-x11-proto-devel
# /oreon:deps
%description
Open CASCADE Technology (OCCT) is a suite for 3D surface and solid
modeling, visualization, data exchange and rapid application development. It
is an excellent platform for development of numerical simulation software
including CAD/CAM/CAE, AEC and GIS, as well as PDM applications.

%package foundation
Summary:        OpenCASCADE CAE platform shared libraries
%description foundation
OpenCASCADE CAE platform shared libraries

This package contains foundation classes which provide a variety of
general-purpose services such as automated management of heap memory,
exception handling, classes for manipulating aggregates of data, basic
math tools.

%package modeling
Summary:        OpenCASCADE CAE platform shared libraries
%description modeling
OpenCASCADE CAE platform shared libraries

This package supplies data structures to represent 2D and 3D geometric models,
as well as topological and geometrical algorithms.

%package ocaf
Summary:        OpenCASCADE CAE platform shared libraries
%description ocaf
OpenCASCADE CAE platform shared libraries

This package provides OpenCASCADE Application Framework services and
support for data exchange.

%package visualization
Summary:        OpenCASCADE CAE platform shared libraries
%description visualization
OpenCASCADE CAE platform shared libraries

This package provides services for displaying 2D and 3D graphics.

%package examples
Summary:        OpenCASCADE CAE platform shared libraries
%description examples
OpenCASCADE CAE platform shared libraries

This package contains example input files for OpenCASCADE in various formats.

%package draw
Summary:        OpenCASCADE CAE platform shared libraries
%description draw
OpenCASCADE CAE DRAW test harness.

%package devel
Summary:        OpenCASCADE CAE platform library development files
Requires:       %{name}-draw%{?_isa} = %{version}-%{release}
Requires:       %{name}-foundation%{?_isa} = %{version}-%{release}
Requires:       %{name}-modeling%{?_isa} = %{version}-%{release}
Requires:       %{name}-ocaf%{?_isa} = %{version}-%{release}
Requires:       %{name}-visualization%{?_isa} = %{version}-%{release}
Requires:       freeimage-devel
Requires:       freetype-devel
Requires:       gl2ps-devel
Requires:       libICE-devel
Requires:       libSM-devel
Requires:       libX11-devel
Requires:       libXext-devel
Requires:       libXScrnSaver-devel
Requires:       libXrandr-devel
Requires:       libXpm-devel
Requires:       libxkbfile-devel
Requires:       libXinerama-devel
Requires:       libXres-devel
Requires:       libXtst-devel
Requires:       libXcomposite-devel
Requires:       libXcursor-devel
Requires:       libXdmcp-devel
Requires:       libXi-devel
Requires:       libXv-devel
Requires:       mesa-libGL-devel
Requires:       mesa-libGLU-devel
Requires:       cmake(RapidJSON)
Requires:       rapidjson-static
Requires:       tbb-devel
Requires:       tcl-devel
Requires:       tk-devel
Requires:       vtk-devel
%description devel
OpenCASCADE CAE platform library development files

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n OCCT-%{ver_under}

# Sources are marked executable for no good reason...
find ./src -type f -exec chmod -x {} \;

# Fix executable set on text files.
chmod 0644 *.txt

%build

export DESTDIR="%{buildroot}"
%cmake -GNinja \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DUSE_RAPIDJSON=True \
       -DUSE_TBB=True \
       -D3RDPARTY_TBB_LIBRARY_DIR=%{_libdir} \
       -D3RDPARTY_TBB_INCLUDE_DIR=%{_includedir} \
       -DUSE_VTK=True \
	   -DINSTALL_VTK=False \
	   -D3RDPARTY_VTK_LIBRARY_DIR=%{_libdir} \
	   -D3RDPARTY_VTK_INCLUDE_DIR=%{_includedir} \
       -DBUILD_DOC_Overview:BOOL=OFF \
       -DINSTALL_DIR_LIB=%{_lib} \
       -DINSTALL_DIR_CMAKE=%{_lib}/cmake/%{name}
%cmake_build
%install
%cmake_install
mv %{buildroot}%{_bindir}/DRAWEXE-* \
   %{buildroot}%{_bindir}/DRAWEXE
install -Dm 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/DRAWEXE.1
desktop-file-install                           \
    --dir=%{buildroot}%{_datadir}/applications \
    %{SOURCE2}
for size in 256 128 64 48; do
    icon=%{_sourcedir}/occ-${size}.png
    install -Dm 0644 $icon \
        %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/occ.png
done
rm -f %{buildroot}%{_docdir}/%{name}/{LICENSE_LGPL_21.txt,OCCT_LGPL_EXCEPTION.txt}
chmod 0755 %{buildroot}%{_bindir}/*.sh
sed -i "s/\\\\\${OCCT_INSTALL_BIN_LETTER}//g" %{buildroot}%{_libdir}/cmake/opencascade/*.cmake
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n opencascade-foundation -f %{oreon_filedir}/opencascade-foundation.list
%files -n opencascade-modeling -f %{oreon_filedir}/opencascade-modeling.list
%files -n opencascade-ocaf -f %{oreon_filedir}/opencascade-ocaf.list
%files -n opencascade-visualization -f %{oreon_filedir}/opencascade-visualization.list
%files -n opencascade-examples -f %{oreon_filedir}/opencascade-examples.list
%files -n opencascade-draw -f %{oreon_filedir}/opencascade-draw.list
%files -n opencascade-devel -f %{oreon_filedir}/opencascade-devel.list

%changelog

%autochangelog
