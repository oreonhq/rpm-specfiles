%global source0_hash 722601e01b78b7a12da4829cb450674935f404b0e508f3f20046fa77570e3272
Name:           OpenColorIO
Version:        2.5.2
Release:        1%{?dist}
Summary:        Enables color transforms and image display across graphics apps
License:        LicenseRef-Callaway-BSD
URL:            http://opencolorio.org/
Source0:        https://github.com/AcademySoftwareFoundation/OpenColorIO/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         OpenColorIO-mzver.patch
ExcludeArch:    i686
%if 0%{?docs}
%endif
%if ! 0%{?docs}
Obsoletes: %{name}-doc < %{version}-%{release}
%endif
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cmake(OpenEXR)
BuildRequires:  expat-devel
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  help2man
BuildRequires:  imath-devel
BuildRequires:  lcms2-devel
BuildRequires:  libX11-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  minizip-ng-compat-devel
BuildRequires:  opencv-devel
BuildRequires:  pybind11-devel
BuildRequires:  pystring-devel
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-markupsafe
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  yaml-cpp-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
OCIO enables color transforms and image display to be handled in a consistent
manner across multiple graphics applications. Unlike other color management
solutions, OCIO is geared towards motion-picture post production, with an
emphasis on visual effects and animation color pipelines.

%package tools
Summary:        Command line tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description tools
Command line tools for %{name}.

%package doc
BuildArch:      noarch
Summary:        API Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
%description doc
API documentation for %{name}.

%package devel
Summary:        Development libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development libraries and headers for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}%{?relcan:-rc%{relcan}}

# Fedora maps minzip-ng back to minizip so work around it here:
sed -i "s/minizip-ng/minizip/g" src/OpenColorIO/OCIOZArchive.cpp src/apps/ocioarchive/main.cpp

%build

%cmake -DCMAKE_CXX_STANDARD=17 \
       -DOCIO_BUILD_DOCS=%{?docs:ON}%{?!docs:OFF} \
       -DOCIO_BUILD_TESTS=%{?tests:ON}%{?!tests:OFF} \
	   -DOCIO_USE_HEADLESS=ON \
	   -DOCIO_INSTALL_EXT_PACKAGES=NONE \
%ifnarch x86_64
       -DOCIO_USE_SSE=OFF \
%endif
       -Dminizip-ng_LIBRARY=%{_libdir}/libminizip.so \
	   -Dminizip-ng_INCLUDE_DIR=%{_includedir}/minizip \
	   -Dminizip-ng_DIR=TRUE \
       -DOpenGL_GL_PREFERENCE=GLVND
%cmake_build
%install
%cmake_install
find %{buildroot} -type f -name "*.a" -exec rm -f {} \;
%oreon_autofiles OpenColorIO-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles OpenColorIO-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles OpenColorIO-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n OpenColorIO-tools -f %{oreon_filedir}/OpenColorIO-tools.list
%files -n OpenColorIO-doc -f %{oreon_filedir}/OpenColorIO-doc.list
%files -n OpenColorIO-devel -f %{oreon_filedir}/OpenColorIO-devel.list

%changelog

%autochangelog
