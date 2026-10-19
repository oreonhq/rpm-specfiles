%global source1_hash e7ad6801dd0e14047f86e186938454398a1211c3a82a27fb4dfe4d34e3264ba7
%global source0_hash 4d23c2b77f6142bfeaa1563621d7a0be394294ed750f67d472277d14aae9bbcc
%global vswig   modified-7
Name:           renderdoc
Version:        1.46
Release:        1%{?dist}
Summary:        A stand-alone graphics debugging tool
License:        MIT
URL:            https://renderdoc.org
Source0:        https://github.com/baldurk/renderdoc/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/baldurk/swig/archive/renderdoc-%{vswig}/swig-%{vswig}.tar.gz
Patch0:         renderdoc-swig-pcre2-1.patch
Patch1:         renderdoc-swig-pcre2-2.patch
ExclusiveArch: x86_64 aarch64
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
# /oreon:deps
%description
A free MIT licensed stand-alone graphics debugger that allows quick
and easy single-frame capture and detailed introspection of any
application using Vulkan, OpenGL.

%package devel
Summary: Development files for renderdoc
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains headers and other files that are
required to develop applications that want to integrate with
renderdoc.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -b 1
%patch -p1 -d %{_builddir}/swig-renderdoc-%{vswig} 0
%patch -p1 -d %{_builddir}/swig-renderdoc-%{vswig} 1

%build

%undefine __cmake_in_source_build
%define _lto_cflags %{nil}
%cmake -DQMAKE_QT5_COMMAND=qmake-qt5 \
       -DRENDERDOC_SWIG_PACKAGE=%{_builddir}/swig-renderdoc-%{vswig} \
       -DPCRE_HEADER=1 \
       -DENABLE_GL=ON \
       -DENABLE_VULKAN=ON \
       -DENABLE_WAYLAND=ON \
       -DENABLE_RENDERDOCCMD=ON \
       -DENABLE_QRENDERDOC=ON \
       -DBUILD_VERSION_STABLE=ON \
       -DBUILD_VERSION_DIST_NAME="fedora" \
       -DBUILD_DISTRIBUTION_VERSION="%{version}-%{release}" \
       -DBUILD_VERSION_DIST_CONTACT="https://bugzilla.redhat.com" \
       -DCMAKE_INSTALL_PREFIX=%{_prefix} \
       -DLIB_SUBFOLDER=renderdoc \
       -DVULKAN_LAYER_FOLDER=/usr/share/vulkan/implicit_layer.d \
       -DCMAKE_BUILD_TYPE=Release \
       %{nil}
%cmake_build
%install
%cmake_install
rm %{buildroot}/%{_datadir}/menu/renderdoc
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%files -f %{oreon_filedir}/main.list
%files -n renderdoc-devel -f %{oreon_filedir}/renderdoc-devel.list

%changelog

%autochangelog
