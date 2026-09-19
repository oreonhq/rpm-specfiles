%global source0_hash c5aa91fa7cbc7977d04676dac34357b08b4344504b68ab3ac2a4e85b85086452

%global commit0 cebbb63edfba502905470c904f8e6f1c6ce28ba9
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global commitdate0 20250221

Name:		glmark2
Version:	2023.01^%{commitdate0}git%{shortcommit0}
Release:	3%{?dist}
Summary:	Benchmark for OpenGL 2.0 and ES 2.0

# all sources are GPL-3.0-or-later
# src/libmatrix: MIT
License:	GPL-3.0-or-later AND MIT
URL:		https://github.com/glmark2/glmark2
Source0:	%{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

## The bellow sources are carried by Fedora package maintaners

##
## .desktop files
##

# 9a43f39f0ddfc91e758e7d7cc44169df30f432b85e668ac135eb38e5dbaa48d8
Source1:	%{name}.desktop

# 5f4c57f5d183ab1b989f293bbc2a6abc27d54f6f796a62318fe7519cc9311a21
Source2:	%{name}-es2.desktop
Source8:	%{name}-es2-wayland.desktop
Source9:	%{name}-wayland.desktop

##
## .desktop pixmap icons
##

# de1229366912806f838409c7ff315be5cc48c6e659d78dfd80d0c5db4dcede1d
Source3:	%{name}.png

# aabcddd0c23d20daf0ed024ae4e7b925ec2fb63bb656843d7180904093a8020e
Source4:	%{name}-es2.png
Source12:	%{name}-es2-wayland.png
Source13:	%{name}-wayland.png

##
## gimp icon sources (not packaged into final rpm, just source rpm)
##

# 1e96f5291318a9c466eed0435ad0e740c789a9b418476807b7253ce0d88b5421
Source5:	%{name}.xcf

# 163b7db2a293e1e86a34c6f84294bb1f54e313ef983fff511a4fe1abca9acd5f
Source6:	%{name}-es2.xcf
Source10:	%{name}-es2-wayland.xcf
Source11:	%{name}-wayland.xcf

##
## appdata - glmark2 only!
##

# 2d5b3e7c9380d068598f272b2f5b55ca736fa157fd205246a86c2473e08577d4
Source7:	%{name}.appdata.xml

##
## BRs
##

BuildRequires:	gcc-c++
BuildRequires:	glad2
BuildRequires:	meson
BuildRequires:	libjpeg-devel
BuildRequires:	pkgconfig(libpng16)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(glesv2)
BuildRequires:	pkgconfig(gbm)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-egl)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	desktop-file-utils
BuildRequires:	appdata-tools

# https://launchpad.net/libmatrix/ MIT
Provides: bundled(libmatrix)

Requires:	%{name}-common = %{version}-%{release}

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

## The .desktop files
desktop-file-install \
--dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

desktop-file-install \
--dir=%{buildroot}%{_datadir}/applications %{SOURCE2}

desktop-file-install \
--dir=%{buildroot}%{_datadir}/applications %{SOURCE8}

desktop-file-install \
--dir=%{buildroot}%{_datadir}/applications %{SOURCE9}

## The ICON files
%{__install} -vd	"%{buildroot}%{_datadir}/pixmaps/"
%{__install} -vp	%{SOURCE3} \
					%{SOURCE4} \
					%{SOURCE12} \
					%{SOURCE13} \
					"%{buildroot}%{_datadir}/pixmaps/"

## The appdata
%{__install} -vd "%{buildroot}%{_datadir}/appdata/"
%{__install} -vp %{SOURCE7} "%{buildroot}%{_datadir}/appdata/"

## Upstream presently does not have any %%check's 
## Here we validate .appdata.xml files, but make erros non-fatal
%check
#appdata-validate %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml || true
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml || :

%files
## the x11 opengl benchmark
%doc NEWS README
%license COPYING COPYING.SGI
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.png
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

## x11 Opengl benchmark DRM
%{_bindir}/%{name}-drm
%{_mandir}/man1/%{name}-drm.1.gz

## Opengl benchmark gbm
%{_bindir}/%{name}-gbm
%{_mandir}/man1/%{name}-gbm.1.gz

## Opengl ES 2 benchmark
%{_datadir}/applications/%{name}-es2.desktop
%{_datadir}/pixmaps/%{name}-es2.png
%{_bindir}/%{name}-es2
%{_mandir}/man1/%{name}-es2.1.gz

## Opengl ES 2 benchmark DRM
%{_bindir}/%{name}-es2-drm
%{_mandir}/man1/%{name}-es2-drm.1.gz

## Opengl ES 2 benchmark gbm
%{_bindir}/%{name}-es2-gbm
%{_mandir}/man1/%{name}-es2-gbm.1.gz

## Opengl ES 2 benchmark wayland
%{_datadir}/applications/%{name}-es2-wayland.desktop
%{_datadir}/pixmaps/%{name}-es2-wayland.png
%{_bindir}/glmark2-es2-wayland
%{_mandir}/man1/glmark2-es2-wayland.1.gz

## Opengl benchmark wayland
%{_datadir}/applications/%{name}-wayland.desktop
%{_datadir}/pixmaps/%{name}-wayland.png
%{_bindir}/glmark2-wayland
%{_mandir}/man1//glmark2-wayland.1.gz

%files common
## assets: models, shaders, textures
%{_datadir}/%{name}/

%changelog
%autochangelog
