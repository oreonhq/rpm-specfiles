%global source0_hash 3046a3d26a7b051af7ebdd257a5f23bfeb160cad6ed952329cdff1e9f1ed496b

%global demodir %{_libdir}/mesa

Summary: Mesa demos
Name: mesa-demos
Version: 9.0.0
Release: 11%{?dist}
# SPDX
License: MIT
URL: http://www.mesa3d.org
Source:        https://archive.mesa3d.org/demos/%{name}-%{version}.tar.xz
# Patch pointblast/spriteblast/dinoshade out for legal reasons
# (not in public domain)
Patch0: mesa-demos-8.5.0-legal.patch
# Install glsl demos data
Patch1: mesa-demos-system-data.patch
BuildRequires: meson
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: pkgconfig
BuildRequires: freeglut-devel
BuildRequires: glslang
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libEGL-devel
BuildRequires: mesa-libGLES-devel
BuildRequires: mesa-libgbm-devel
BuildRequires: libGLU-devel
BuildRequires: libXext-devel
BuildRequires: libdecor-devel
BuildRequires: libxcb-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: vulkan-loader-devel
BuildRequires: wayland-devel
BuildRequires: wayland-protocols-devel
BuildRequires: freetype-devel

%description
This package provides some demo applications for testing Mesa.

%package -n glx-utils
Summary: GLX utilities
Provides: glxinfo glxinfo%{?__isa_bits}
# mesa-demos' glx-utils used to provide xdriinfo for a long time, but that has
# always been an additional external source, so it was split into its own
# package.
# Recommend it here so that it still gets pulled at first for anyone expecting
# it to be there, but it doesn't need to be a hard requirement anymore.
Recommends: xdriinfo

%description -n glx-utils
The glx-utils package provides the glxinfo and glxgears utilities.

%package -n egl-utils
Summary: EGL utilities
Provides: eglinfo es2_info

%description -n egl-utils
The egl-utils package provides the eglinfo, eglgears, es2_info and es2gears utilities.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{name}-%{version}
%patch -P0 -p1 -b .legal
%patch -P1 -p1 -b .systemdata

# These two files are distributable, but non-free (lack of permission to modify).
rm -rf src/demos/pointblast.c
rm -rf src/demos/spriteblast.c

%build
%meson \
    --bindir=%{demodir} \
    -Dwith-system-data-files=true \
    -Dx11=enabled \
    -Dwayland=enabled \
    -Degl=enabled \
    -Dgles2=enabled \
    -Dvulkan=enabled \
    -Dlibdrm=enabled \
    -Dosmesa=disabled

%meson_build

%install
%meson_install

mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{_vpath_builddir}/src/xdemos/glxgears %{buildroot}%{_bindir}
install -m 0755 %{_vpath_builddir}/src/xdemos/glxinfo %{buildroot}%{_bindir}
%if 0%{?__isa_bits} != 0
install -m 0755 %{_vpath_builddir}/src/xdemos/glxinfo %{buildroot}%{_bindir}/glxinfo%{?__isa_bits}
%endif

install -m 0755 %{_vpath_builddir}/src/egl/opengl/eglinfo %{buildroot}%{_bindir}
install -m 0755 %{_vpath_builddir}/src/egl/opengl/eglgears_x11 %{buildroot}%{_bindir}
install -m 0755 %{_vpath_builddir}/src/egl/opengl/eglgears_wayland %{buildroot}%{_bindir}
install -m 0755 %{_vpath_builddir}/src/egl/opengles2/es2_info %{buildroot}%{_bindir}
install -m 0755 %{_vpath_builddir}/src/egl/opengles2/es2gears_x11 %{buildroot}%{_bindir}
install -m 0755 %{_vpath_builddir}/src/egl/opengles2/es2gears_wayland %{buildroot}%{_bindir}

%check

%files
%{demodir}
%{_datadir}/%{name}/

%files -n glx-utils
%{_bindir}/glxinfo*
%{_bindir}/glxgears

%files -n egl-utils
%{_bindir}/eglinfo
%{_bindir}/eglgears_x11
%{_bindir}/eglgears_wayland
%{_bindir}/es2_info
%{_bindir}/es2gears_x11
%{_bindir}/es2gears_wayland

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 9.0.0-11
- Prepare for Oreon 11 (RP1)
