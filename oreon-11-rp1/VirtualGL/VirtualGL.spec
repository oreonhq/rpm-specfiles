%global source0_hash 055b781d6ac7b109eccd6c8be9f27f8bb60f92f1001ded84d2619f9e349894a7

Name:           VirtualGL
Version:        3.1.3
Release:        6%{?dist}
Summary:        A toolkit for displaying OpenGL applications to thin clients

# Automatically converted from old format: wxWindows - review is highly recommended.
License:        LGPL-2.0-or-later WITH WxWindows-exception-3.1
URL:            https://www.virtualgl.org
Source0:        https://github.com/VirtualGL/virtualgl/archive/%{version}/VirtualGL-%{version}.tar.gz
# fix for bz923961
Patch1:         %{name}-redhatpathsfix.patch
# fix for bz1088475
Patch2:         %{name}-redhatlibexecpathsfix.patch
# Do not rely on hostname package
Patch4:         %{name}-hostname.patch

%if 0%{?rhel} == 7
BuildRequires:  cmake3
%else
BuildRequires:  cmake
%endif
BuildRequires:  fltk-devel
BuildRequires:  turbojpeg-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  pkgconfig
# no need OpenCL-Headers, ocl-icd seems enough
#BuildRequires:  pkgconfig(OpenCL-Headers)
BuildRequires:  pkgconfig(ocl-icd)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glproto)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xv)
%if 0%{?fedora:1} || 0%{?rhel} <= 7
BuildRequires:  fltk-fluid
%endif
Requires:       fltk
Provides:       bumblebee-bridge

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
%if 0%{?rhel} == 7
cmake3 \
%else
%cmake \
%endif
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

%if 0%{?rhel} == 7
make %{?_smp_mflags}
%else
%cmake_build
%endif

%install
%if 0%{?rhel} == 7
make install DESTDIR=$RPM_BUILD_ROOT
%else
%cmake_install
%endif
# glxinfo conflicts with command from glx-utils so lets do what Arch does
# and rename the command
mv %{buildroot}/%{_bindir}/glxinfo %{buildroot}/%{_bindir}/vglxinfo
# eglinfo conflics with the command from egl-utils, rename eglinfo to veglinfo
mv %{buildroot}/%{_bindir}/eglinfo %{buildroot}/%{_bindir}/veglinfo

mkdir -p %{buildroot}%{_libdir}/fakelib/
ln -rsf %{_libdir}/VirtualGL/librrfaker.so %{buildroot}%{_libdir}/fakelib/libGL.so
# fix for bz1088475
mkdir %{buildroot}%{_libexecdir}
%if 0%{?__isa_bits} == 64
mv %{buildroot}%{_bindir}/.vglrun.vars64 %{buildroot}%{_libexecdir}/vglrun.vars64
%else
mv %{buildroot}%{_bindir}/.vglrun.vars32 %{buildroot}%{_libexecdir}/vglrun.vars32
%endif

%ldconfig_scriptlets

%files
%{_docdir}/%{name}/
%{_bindir}/tcbench
%{_bindir}/nettest
%{_bindir}/cpustat
%{_bindir}/veglinfo
%{_bindir}/eglxinfo
%{_bindir}/vglclient
%{_bindir}/vglconfig
%{_bindir}/vglconnect
%{_bindir}/vglgenkey
%{_bindir}/vgllogin
%{_bindir}/vglserver_config
%{_bindir}/vglrun
%{_bindir}/vglxinfo
%{_bindir}/glreadtest
%if 0%{?__isa_bits} == 64
%{_bindir}/eglxspheres64
%{_bindir}/glxspheres64
%{_libexecdir}/vglrun.vars64
%else
%{_bindir}/eglxspheres
%{_bindir}/glxspheres
%{_libexecdir}/vglrun.vars32
%endif
%{_libdir}/VirtualGL/
%{_libdir}/fakelib/

%files devel
%{_includedir}/rrtransport.h
%{_includedir}/rr.h

%changelog
%autochangelog
