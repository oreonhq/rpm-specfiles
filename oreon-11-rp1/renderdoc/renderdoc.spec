%global source0_hash e7ad6801dd0e14047f86e186938454398a1211c3a82a27fb4dfe4d34e3264ba7

%global vswig   modified-7
Name:           renderdoc
Version:        1.42
Release:        2%{?dist}
Summary:        A stand-alone graphics debugging tool

License:        MIT
URL:            https://renderdoc.org
Source0:        https://github.com/baldurk/renderdoc/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/baldurk/swig/archive/renderdoc-%{vswig}/swig-%{vswig}.tar.gz
Patch0:         renderdoc-swig-pcre2-1.patch
Patch1:         renderdoc-swig-pcre2-2.patch

# renderdoc is officially only supported on x86_64.
# however, it also builds on aarch64
ExclusiveArch: x86_64 aarch64

# for the local swig
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pcre2-devel

# for the renderdoc itself
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  bison
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(xcb-keysyms)
Requires:       hicolor-icon-theme

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
# renderdoc does not allow in-source builds. out-of-source builds
# are the default starting with F33, but for anything below the
# __cmake_in_source_build macro needs to be undefined.
%undefine __cmake_in_source_build

# compiling renderdoc with lto currently leads to crashes
# https://github.com/baldurk/renderdoc/issues/2373
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

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%license LICENSE.md
%{_bindir}/qrenderdoc
%{_bindir}/renderdoccmd
%{_datadir}/applications/%{name}.desktop
%dir %{_libdir}/renderdoc
%{_libdir}/renderdoc/lib%{name}.so
%{_datadir}/thumbnailers/%{name}.thumbnailer
%{_datadir}/icons/hicolor/*/mimetypes/application-x-renderdoc-capture.*
%{_datadir}/mime/packages/renderdoc-capture.xml
%{_datadir}/pixmaps/%{name}-icon-*.xpm
%doc %{_docdir}/%{name}/
%{_datadir}/vulkan/implicit_layer.d/%{name}_capture.json

%files devel
%{_includedir}/%{name}_app.h

%changelog
%autochangelog
