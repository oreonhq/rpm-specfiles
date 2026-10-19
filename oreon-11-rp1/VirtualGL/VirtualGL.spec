%global source0_hash e7fb0f4266219d614de89530c7eea686dd9362897000ed0e541891ea817f2072
Name:           VirtualGL
Version:        3.1.5
Release:        1%{?dist}
Summary:        A toolkit for displaying OpenGL applications to thin clients
License:        LGPL-2.0-or-later WITH WxWindows-exception-3.1
URL:            https://www.virtualgl.org
Source0:        https://github.com/VirtualGL/virtualgl/archive/%{version}/VirtualGL-%{version}.tar.gz
Patch1:         %{name}-redhatpathsfix.patch
Patch2:         %{name}-redhatlibexecpathsfix.patch
Patch4:         %{name}-hostname.patch
Requires:       fltk
Provides:       bumblebee-bridge
# oreon:deps
BuildRequires:  cmake
BuildRequires:  fltk-devel
BuildRequires:  fltk-fluid
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glproto)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(ocl-icd)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xv)
BuildRequires:  turbojpeg-devel
# /oreon:deps
%description
VirtualGL is a toolkit that allows most Unix/Linux OpenGL applications to be
remotely displayed with hardware 3D acceleration to thin clients, regardless
of whether the clients have 3D capabilities, and regardless of the size of the
3D data being rendered or the speed of the network.

Using the vglrun script, the VirtualGL "faker" is loaded into an OpenGL
application at run time.  The faker then intercepts a handful of GLX calls,
which it reroutes to the server's X display (the "3D X Server", which
presumably has a 3D accelerator attached.)  The GLX commands are also
dynamically modified such that all rendering is redirected into a Pbuffer
instead of a window.  As each frame is rendered by the application, the faker
reads back the pixels from the 3D accelerator and sends them to the
"2D X Server" for compositing into the appropriate X Window.

VirtualGL can be used to give hardware-accelerated 3D capabilities to VNC or
other X proxies that either lack OpenGL support or provide it through software
rendering.  In a LAN environment, VGL can also be used with its built-in
high-performance image transport, which sends the rendered 3D images to a
remote client (vglclient) for compositing on a remote X server.  VirtualGL
also supports image transport plugins, allowing the rendered 3D images to be
sent or captured using other mechanisms.

VirtualGL is based upon ideas presented in various academic papers on
this topic, including "A Generic Solution for Hardware-Accelerated Remote
Visualization" (Stegmaier, Magallon, Ertl 2002) and "A Framework for
Interactive Hardware Accelerated Remote 3D-Visualization" (Engel, Sommer,
Ertl 2000.)

%package devel
Summary:    Development headers and libraries for VirtualGL
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   turbojpeg-devel%{?_isa}
Requires:   mesa-libGLU-devel%{?_isa}
Requires:   libXv-devel%{?_isa}
%description devel
Development headers and libraries for VirtualGL.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n virtualgl-%{version}

# Remove bundled libraries
rm -r server/fltk

%build

%cmake \
         -DVGL_SYSTEMFLTK=1 \
         -DVGL_FAKEXCB=1 \
         -DVGL_BUILDSTATIC=0 \
         -DVGL_FAKEOPENCL=1 \
         -DVGL_BUILDSERVER=1 \
         -DVGL_USEXV=1 \
         -DTJPEG_INCLUDE_DIR=%{_includedir} \
         -DTJPEG_LIBRARY=%{_libdir}/libturbojpeg.so \
         -DCMAKE_INSTALL_PREFIX=%{_prefix} \
         -DCMAKE_INSTALL_LIBDIR=%{_libdir}/VirtualGL \
         -DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name} \
         -DCMAKE_INSTALL_BINDIR=%{_bindir} \
         -DCMAKE_LIBRARY_PATH=%{_libdir}
%cmake_build
%install
%cmake_install
mv %{buildroot}/%{_bindir}/glxinfo %{buildroot}/%{_bindir}/vglxinfo
mv %{buildroot}/%{_bindir}/eglinfo %{buildroot}/%{_bindir}/veglinfo
mkdir -p %{buildroot}%{_libdir}/fakelib/
ln -rsf %{_libdir}/VirtualGL/librrfaker.so %{buildroot}%{_libdir}/fakelib/libGL.so
mkdir %{buildroot}%{_libexecdir}
%if 0%{?__isa_bits} == 64
mv %{buildroot}%{_bindir}/.vglrun.vars64 %{buildroot}%{_libexecdir}/vglrun.vars64
%else
mv %{buildroot}%{_bindir}/.vglrun.vars32 %{buildroot}%{_libexecdir}/vglrun.vars32
%endif
%ldconfig_scriptlets
%oreon_autofiles VirtualGL-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n VirtualGL-devel -f %{oreon_filedir}/VirtualGL-devel.list

%changelog

%autochangelog
