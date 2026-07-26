%global source0_hash 92805abc84505e3e7e27aec775ab0754ecb4182fe2d8ff2a9d568ccdcb2811ac

# Explicitly use Makefiles
%global _cmake_generator "Unix Makefiles"

%global srcname fltk

Name:		    fltk1.3
Version:	    1.3.11
Release:	    5%{?dist}
Summary:	    C++ user interface toolkit

# see COPYING (or http://www.fltk.org/COPYING.php ) for exceptions details
License:	    LGPL-2.0-or-later WITH FLTK-exception
URL:            http://www.fltk.org/

Source0:        https://github.com/%{srcname}/%{srcname}/releases/download/release-%{version}/%{srcname}-%{version}-source.tar.gz
Source1:        fltk-config.sh

Patch0:         fltk-cmake.patch
# add lib64 support, drop extraneous libs (bug #708185) and ldflags (#1112930)
Patch1:         fltk-1.3.4-fltk_config.patch
# Fix cmake install location for MinGW build
Patch2:         mingw-fltk-cmake.patch

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  texlive-latex
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(gl) pkgconfig(glu)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(xext) pkgconfig(xinerama) pkgconfig(xft) pkgconfig(xt) pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(zlib)

%global _description \
FLTK (pronounced "fulltick") is a cross-platform C++ GUI toolkit. \
It provides modern GUI functionality without the bloat, and supports \
3D graphics via OpenGL and its built-in GLUT emulation.

%description
%{_description}

%package devel
Summary:        Development files for %{name}
Conflicts:      fltk-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libstdc++-devel
Requires:       pkgconfig(fontconfig)
Requires:       pkgconfig(gl) pkgconfig(glu)
Requires:       pkgconfig(ice) pkgconfig(sm)
Requires:       pkgconfig(xft) pkgconfig(xt) pkgconfig(x11)
Requires:       pkgconfig(libjpeg)
Requires:       pkgconfig(libpng)
Requires:       pkgconfig(zlib)
%description devel
%{summary}.

%package static
Summary:        Static libraries for %{name}
Conflicts:      fltk-static
Requires:       %{name}-devel = %{version}-%{release}
%description static
%{summary}.

%package fluid
Summary:        Fast Light User Interface Designer for FLTK 1.3
Conflicts:      fltk-fluid
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel
%description fluid
%{summary}, an interactive GUI designer for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -C -p1

%conf
%cmake -DFLTK_CONFIG_PATH:PATH=%{_libdir}/cmake/fltk \
       -DOpenGL_GL_PREFERENCE=GLVND \
       -DOPTION_BUILD_HTML_DOCUMENTATION:BOOL=ON \
       -DOPTION_BUILD_PDF_DOCUMENTATION:BOOL=OFF \
       -DOPTION_BUILD_SHARED_LIBS:BOOL=ON

%build
%cmake_build

%cmake_build --target docs

%install
%cmake_install

# Deal with license file of same name
mv src/xutf8/COPYING ./COPYING.xutf8

# we only apply this hack to multilib arch's
%ifarch x86_64 %{ix86}
%global arch %(uname -m 2>/dev/null || echo undefined)
mv $RPM_BUILD_ROOT%{_bindir}/fltk-config \
   $RPM_BUILD_ROOT%{_bindir}/fltk-config-%{arch}
install -p -m755 -D %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/fltk-config
%endif

%files
%doc ANNOUNCEMENT CHANGES CREDITS README
%license COPYING COPYING.xutf8
%{_libdir}/libfltk.so.1.3*
%{_libdir}/libfltk_forms.so.1.3*
%{_libdir}/libfltk_gl.so.1.3*
%{_libdir}/libfltk_images.so.1.3*

%files devel
%doc %{_vpath_builddir}/documentation/html
%{_bindir}/fltk-config
%{?arch:%{_bindir}/fltk-config-%{arch}}
%{_includedir}/FL/
%{_libdir}/libfltk.so
%{_libdir}/libfltk_forms.so
%{_libdir}/libfltk_gl.so
%{_libdir}/libfltk_images.so
%{_libdir}/cmake/fltk/
%{_mandir}/man1/fltk-config.1*
%{_mandir}/man3/fltk.3*
%{_mandir}/man6/*.6*

%files static
%{_libdir}/libfltk.a
%{_libdir}/libfltk_forms.a
%{_libdir}/libfltk_gl.a
%{_libdir}/libfltk_images.a

%files fluid
%{_bindir}/fluid
%{_mandir}/man1/fluid.1*
%{_datadir}/applications/fluid.desktop
%{_datadir}/mime/packages/fluid.xml
%{_datadir}/icons/hicolor/*/*/fluid.png

%changelog
%autochangelog
