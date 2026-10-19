%global source0_hash c5aa91fa7cbc7977d04676dac34357b08b4344504b68ab3ac2a4e85b85086452
%global commit0 cebbb63edfba502905470c904f8e6f1c6ce28ba9
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global commitdate0 20250221
Name:		glmark2
Version:	2023.01^%{commitdate0}git%{shortcommit0}
Release:        3%{?dist}
Summary:        Benchmark for OpenGL 2.0 and ES 2.0
License:	GPL-3.0-or-later AND MIT
URL:		https://github.com/glmark2/glmark2
Source0:        https://github.com/%{name}/%{name}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}-es2.desktop
Source8:	%{name}-es2-wayland.desktop
Source9:	%{name}-wayland.desktop
Source3:	%{name}.png
Source4:	%{name}-es2.png
Source12:	%{name}-es2-wayland.png
Source13:	%{name}-wayland.png
Source5:	%{name}.xcf
Source6:	%{name}-es2.xcf
Source10:	%{name}-es2-wayland.xcf
Source11:	%{name}-wayland.xcf
Source7:	%{name}.appdata.xml
Provides: bundled(libmatrix)
Requires:	%{name}-common = %{version}-%{release}
# oreon:deps
BuildRequires:  appdata-tools
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  glad2
BuildRequires:  libjpeg-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libpng16)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(x11)
# /oreon:deps
%description
glmark2 is an OpenGL 2.0 and ES 2.0 benchmark.

## 
##  sub-package
##  The noarch sub-package is easier on the mirrors.
##  One package for common noarch data shared with all architectures.
##  

%package common
Summary:	Models, Textures, and Shaders for GLmark2 Benchmark suite
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}
%description common
Common graphical assets for Glmark2 benchmark suite

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit0}

# Remove bundled libraries!
rm -r src/libjpeg-turbo src/libpng src/zlib
rm -r src/glad
glad \
  --reproducible \
  --out-path src/glad \
  --api egl=1.5,gl:compatibility=2.1,gles1:common=1.0,gles2=2.0,glx=1.4,wgl=1.0 \
  --extensions EGL_EXT_image_dma_buf_import_modifiers,EGL_EXT_platform_base,EGL_KHR_platform_gbm,EGL_KHR_platform_wayland,EGL_KHR_platform_x11,EGL_MESA_platform_surfaceless,GL_EXT_framebuffer_object,GL_OES_mapbuffer,GL_OES_required_internalformat,GLX_EXT_swap_control,GLX_MESA_swap_control,WGL_ARB_extensions_string,WGL_EXT_extensions_string,WGL_EXT_swap_control \
  c

%build

%meson -Dflavors=drm-gl,drm-glesv2,wayland-gl,wayland-glesv2,x11-gl,x11-glesv2,gbm-glesv2,gbm-gl
%meson_build
%install
%meson_install
desktop-file-install \
--dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
desktop-file-install \
--dir=%{buildroot}%{_datadir}/applications %{SOURCE2}
desktop-file-install \
--dir=%{buildroot}%{_datadir}/applications %{SOURCE8}
desktop-file-install \
--dir=%{buildroot}%{_datadir}/applications %{SOURCE9}
%{__install} -vd	"%{buildroot}%{_datadir}/pixmaps/"
%{__install} -vp	%{SOURCE3} \
					%{SOURCE4} \
					%{SOURCE12} \
					%{SOURCE13} \
					"%{buildroot}%{_datadir}/pixmaps/"
%{__install} -vd "%{buildroot}%{_datadir}/appdata/"
%{__install} -vp %{SOURCE7} "%{buildroot}%{_datadir}/appdata/"
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml || :
%files -f %{oreon_filedir}/main.list
%files -n glmark2-common -f %{oreon_filedir}/glmark2-common.list

%changelog

%autochangelog
