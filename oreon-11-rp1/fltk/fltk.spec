%global source0_hash 94b464cce634182c8407adac1be5fc49678986ca93285699b444352af89b4efe

# Explicitly use Makefiles
%global _cmake_generator "Unix Makefiles"

# FLTK major version (intentionally lazily evaluated!)
%define majorver %(echo "%{version}" | cut -d. -f1,2)

# Break self-dependency cycles by disabling certain packages on major version bumps
%bcond bootstrap 0

# MinGW is enabled by default (except for RHEL), to disable use '--without mingw'
%if 0%{?rhel} || 0%{?flatpak} || 0%{?_with_bootstrap}
%bcond_with mingw
%else
%bcond_without mingw
%endif

Name:           fltk
Version:        1.4.4
Release:        5%{?dist}
Summary:        C++ user interface toolkit

# see COPYING (or http://www.fltk.org/COPYING.php ) for exceptions details
License:        LGPL-2.0-or-later WITH FLTK-exception
URL:            http://www.fltk.org/

Source0:        https://github.com/fltk/fltk/releases/download/release-1.4.4/fltk-1.4.4-source.tar.gz
Source1:        fltk-config.sh

# Use the correct cmake data install location
Patch0:         fltk-cmake.patch
# add lib64 support, drop extraneous libs (bug #708185) and ldflags (#1112930)
Patch1:         fltk-1.4.4-fltk_config.patch
# Fix cairo include
Patch2:         fltk-cairo_h.patch

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  texlive-latex
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(libdecor-0) >= 0.2.0
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(pango) pkgconfig(pangocairo)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(gl) pkgconfig(glu)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(wayland-client) >= 1.18
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
# includes cursor-shape and tablet-v2 with all current fixes
BuildRequires:  pkgconfig(wayland-protocols) >= 1.46
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xext) pkgconfig(xinerama) pkgconfig(xft) pkgconfig(xt) pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(zlib)

%if %{with mingw}
# For MinGW builds
BuildRequires:  fltk-fluid >= %{majorver}
# MinGW
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-zlib
# Libraries
BuildRequires:  mingw32-cairo
BuildRequires:  mingw32-libpng
BuildRequires:  mingw32-libjpeg

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-zlib
# Libraries
BuildRequires:  mingw64-cairo
BuildRequires:  mingw64-libpng
BuildRequires:  mingw64-libjpeg
%endif


%global _description \
FLTK (pronounced "fulltick") is a cross-platform C++ GUI toolkit. \
It provides modern GUI functionality without the bloat, and supports \
3D graphics via OpenGL and its built-in GLUT emulation.

%description
%{_description}

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libstdc++-devel
Requires:       pkgconfig(cairo)
Requires:       pkgconfig(libdecor-0) >= 0.2.0
Requires:       pkgconfig(wayland-client) >= 1.18
Requires:       pkgconfig(wayland-cursor)
Requires:       pkgconfig(xkbcommon)
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
Requires:       %{name}-devel = %{version}-%{release}
%description static
%{summary}.

%package options
Summary:        Fast Light Tool Kit Options Editor
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description options
%{summary}, an interactive options editor for applications
using %{name}.

%package fluid
Summary:        Fast Light User Interface Designer
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel
%description fluid
%{summary}, an interactive GUI designer for %{name}.

%if %{with mingw}
%package -n mingw32-fltk
Summary:       MinGW compiled fltk for the Win32 target

%description -n mingw32-fltk
%{_description}

# Win64
%package -n mingw64-fltk
Summary:       MinGW compiled fltk for the Win64 target

%description -n mingw64-fltk
%{_description}

%package -n mingw32-fltk-static
Summary:       MinGW compiled fltk for the Win32 target

%description -n mingw32-fltk-static
%{_description}

# Win64
%package -n mingw64-fltk-static
Summary:       MinGW compiled fltk for the Win64 target

%description -n mingw64-fltk-static
%{_description}

%{?mingw_debug_package}
%endif


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1


%conf
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DFLTK_BUILD_SHARED_LIBS:BOOL=ON \
       -DOpenGL_GL_PREFERENCE=GLVND \
       -DFLTK_OPTION_CAIRO_WINDOW:BOOL=ON \
       -DFLTK_BUILD_HTML_DOCS:BOOL=ON \
       -DFLTK_BUILD_PDF_DOCS:BOOL=OFF \
       %{nil}

%if %{with mingw}
%mingw_cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
             -DFLTK_OPTION_CAIRO_WINDOW:BOOL=ON \
             -DFLTK_BUILD_SHARED_LIBS:BOOL=ON \
             -DFLTK_BUILD_HTML_DOCS:BOOL=OFF \
             -DFLTK_BUILD_PDF_DOCS:BOOL=OFF \
             %{nil}
%endif


%build
%cmake_build

%cmake_build --target docs

%if %{with mingw}
%mingw_make_build
%endif


%install
%cmake_install

# Replace "static" applications with their "shared" equivalents
mv %{buildroot}%{_bindir}/fltk-options-shared %{buildroot}%{_bindir}/fltk-options
mv %{buildroot}%{_bindir}/fluid-shared %{buildroot}%{_bindir}/fluid

# Delete installed demo applications
rm %{buildroot}%{_bindir}/{blocks,checkers,glpuzzle,sudoku}

# Deal with license file of same name
mv src/xutf8/COPYING ./COPYING.xutf8

# we only apply this hack to multilib arch's
%ifarch x86_64 %{ix86}
%global arch %(uname -m 2>/dev/null || echo undefined)
mv %{buildroot}%{_bindir}/fltk-config \
   %{buildroot}%{_bindir}/fltk-config-%{arch}
install -p -m755 -D %{SOURCE1} %{buildroot}%{_bindir}/fltk-config
%endif

%if %{with mingw}
%mingw_make_install
%mingw_debug_install_post

# Delete redundant man pages
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}

# Replace "static" applications with their "shared" equivalents
mv %{buildroot}%{mingw32_bindir}/fltk-options-shared.exe \
   %{buildroot}%{mingw32_bindir}/fltk-options.exe
mv %{buildroot}%{mingw64_bindir}/fltk-options-shared.exe \
   %{buildroot}%{mingw64_bindir}/fltk-options.exe

# Delete useless fluid binaries
rm -rf %{buildroot}{%{mingw32_bindir},%{mingw64_bindir}}/fluid*

# Delete installed demo applications
rm %{buildroot}{%{mingw32_bindir},%{mingw64_bindir}}/{blocks,checkers,glpuzzle,sudoku}.exe
%endif


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/fluid.desktop


%files
%doc ANNOUNCEMENT CHANGES.txt CREDITS.txt README.txt
%license COPYING COPYING.xutf8
%{_libdir}/libfltk.so.%{majorver}{,.*}
%{_libdir}/libfltk_cairo.so.%{majorver}{,.*}
%{_libdir}/libfltk_forms.so.%{majorver}{,.*}
%{_libdir}/libfltk_gl.so.%{majorver}{,.*}
%{_libdir}/libfltk_images.so.%{majorver}{,.*}

%files devel
%doc %{_vpath_builddir}/documentation/html
%{_bindir}/fltk-config
%{?arch:%{_bindir}/fltk-config-%{arch}}
%{_includedir}/FL/
%{_libdir}/libfltk.so
%{_libdir}/libfltk_cairo.so
%{_libdir}/libfltk_forms.so
%{_libdir}/libfltk_gl.so
%{_libdir}/libfltk_images.so
%{_libdir}/cmake/fltk/
%{_mandir}/man1/fltk-config.1*
%{_mandir}/man1/fltk-options.1*
%{_mandir}/man3/fltk.3*
%{_mandir}/man6/*.6*

%files static
%{_libdir}/libfltk.a
%{_libdir}/libfltk_cairo.a
%{_libdir}/libfltk_forms.a
%{_libdir}/libfltk_gl.a
%{_libdir}/libfltk_images.a

%files options
%{_bindir}/fltk-options
%{_mandir}/man1/fltk-options.1*
%{_datadir}/applications/fltk-options.desktop
%{_datadir}/mime/packages/fltk-options.xml
%{_datadir}/icons/hicolor/*/*/fltk-options.png

%files fluid
%{_bindir}/fluid
%{_mandir}/man1/fluid.1*
%{_datadir}/applications/fluid.desktop
%{_datadir}/mime/packages/fluid.xml
%{_datadir}/icons/hicolor/*/*/fluid.png

%if %{with mingw}
%files -n mingw32-fltk
%license COPYING COPYING.xutf8
%{mingw32_bindir}/fltk-config
%{mingw32_bindir}/fltk-options-cmd.exe
%{mingw32_bindir}/fltk-options.exe
%{mingw32_bindir}/libfltk.dll
%{mingw32_libdir}/libfltk.dll.a
%{mingw32_bindir}/libfltk_cairo.dll
%{mingw32_libdir}/libfltk_cairo.dll.a
%{mingw32_bindir}/libfltk_forms.dll
%{mingw32_libdir}/libfltk_forms.dll.a
%{mingw32_bindir}/libfltk_images.dll
%{mingw32_libdir}/libfltk_images.dll.a
%{mingw32_bindir}/libfltk_jpeg.dll
%{mingw32_libdir}/libfltk_jpeg.dll.a
%{mingw32_bindir}/libfltk_png.dll
%{mingw32_libdir}/libfltk_png.dll.a
%{mingw32_bindir}/libfltk_gl.dll
%{mingw32_libdir}/libfltk_gl.dll.a
%{mingw32_bindir}/libfltk_z.dll
%{mingw32_libdir}/libfltk_z.dll.a
%{mingw32_includedir}/FL/
%{mingw32_libdir}/cmake/fltk/

%files -n mingw64-fltk
%license COPYING COPYING.xutf8
%{mingw64_bindir}/fltk-config
%{mingw64_bindir}/fltk-options-cmd.exe
%{mingw64_bindir}/fltk-options.exe
%{mingw64_bindir}/libfltk.dll
%{mingw64_libdir}/libfltk.dll.a
%{mingw64_bindir}/libfltk_cairo.dll
%{mingw64_libdir}/libfltk_cairo.dll.a
%{mingw64_bindir}/libfltk_forms.dll
%{mingw64_libdir}/libfltk_forms.dll.a
%{mingw64_bindir}/libfltk_images.dll
%{mingw64_libdir}/libfltk_images.dll.a
%{mingw64_bindir}/libfltk_jpeg.dll
%{mingw64_libdir}/libfltk_jpeg.dll.a
%{mingw64_bindir}/libfltk_png.dll
%{mingw64_libdir}/libfltk_png.dll.a
%{mingw64_bindir}/libfltk_gl.dll
%{mingw64_libdir}/libfltk_gl.dll.a
%{mingw64_bindir}/libfltk_z.dll
%{mingw64_libdir}/libfltk_z.dll.a
%{mingw64_includedir}/FL/
%{mingw64_libdir}/cmake/fltk/

%files -n mingw32-fltk-static
%{mingw32_libdir}/libfltk.a
%{mingw32_libdir}/libfltk_cairo.a
%{mingw32_libdir}/libfltk_forms.a
%{mingw32_libdir}/libfltk_images.a
%{mingw32_libdir}/libfltk_jpeg.a
%{mingw32_libdir}/libfltk_png.a
%{mingw32_libdir}/libfltk_gl.a
%{mingw32_libdir}/libfltk_z.a

%files -n mingw64-fltk-static
%{mingw64_libdir}/libfltk.a
%{mingw64_libdir}/libfltk_cairo.a
%{mingw64_libdir}/libfltk_forms.a
%{mingw64_libdir}/libfltk_images.a
%{mingw64_libdir}/libfltk_jpeg.a
%{mingw64_libdir}/libfltk_png.a
%{mingw64_libdir}/libfltk_gl.a
%{mingw64_libdir}/libfltk_z.a
%endif


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.4-5
- Prepare for Oreon 11 (RP1)
