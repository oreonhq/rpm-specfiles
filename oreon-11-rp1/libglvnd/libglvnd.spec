# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 8797914ff69e62d7d89b331cab311b29fff5cfaddae5aae09695a7ccbaf353d7

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%if %{with bootstrap}
%global _without_mesa_glvnd_default 1
%endif

%global commit0 faa23f21fc677af5792825dc30cb1ccef4bf33a6

%global compositor weston

Name:           libglvnd
Version:        1.7.0
Release:        2%{?dist}
Epoch:          1
Summary:        The GL Vendor-Neutral Dispatch library

License:        MIT-feh AND MIT-Modern-Variant AND BSD-1-Clause AND BSD-3-Clause AND GPL-3.0-or-later WITH Autoconf-exception-macro
URL:            https://gitlab.freedesktop.org/glvnd/libglvnd
Source0:        %{url}/-/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:         0001-glx-Add-another-fallback-library-name.patch

BuildRequires:  oreon-rpm-macros
BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  python3-rpm-macros
BuildRequires:  python3-libxml2
BuildRequires:  pkgconfig(glproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
%bcond_with glvnd_tests
%if %{with glvnd_tests}
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  mesa-dri-drivers
BuildRequires:  %{compositor}
BuildRequires:  xwayland-run
%endif

%{?_without_mesa_glvnd_default:
%global __provides_exclude_from %{_libdir}/%{name}
%global __requires_exclude_from %{_libdir}/%{name}
}

%description
libglvnd is an implementation of the vendor-neutral dispatch layer for
arbitrating OpenGL API calls between multiple vendors on a per-screen basis.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-opengl%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-gles%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-glx%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-egl%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-core-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libX11-devel%{?_isa}
Obsoletes:      mesa-libGLES-devel < 19.3.0~rc1
Provides:       mesa-libGLES-devel = %{epoch}:%{version}-%{release}
Provides:       mesa-libGLES-devel%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:      mesa-khr-devel < 19.3.0~rc1
Provides:       mesa-khr-devel = %{epoch}:%{version}-%{release}
Provides:       mesa-khr-devel%{?_isa} = %{epoch}:%{version}-%{release}
Provides:       libGLES-devel = %{epoch}:%{version}-%{release}
Provides:       libGLES-devel%{?_isa} = %{epoch}:%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        core-devel
Summary:        Core development files for %{name}

%description core-devel
The %{name}-core-devel package is a bootstrap trick for Mesa, which wants
to build against the %{name} headers but does not link against any of
its libraries (and, initially, has file conflicts with them). If you are
not Mesa you almost certainly want %{name}-devel instead.

%package        opengl
Summary:        OpenGL support for libglvnd
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    opengl
libOpenGL is the common dispatch interface for the workstation OpenGL API.

%package        gles
Summary:        GLES support for libglvnd
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%{!?_without_mesa_glvnd_default:
Recommends:     mesa-libEGL%{?_isa} >= 13.0.4-1
Obsoletes:      mesa-libGLES < 19.3.0~rc1
Provides:       mesa-libGLES
Provides:       mesa-libGLES%{?_isa}
Provides:       libGLES
Provides:       libGLES%{?_isa}
}

%description    gles
libGLESv[12] are the common dispatch interface for the GLES API.

%package        egl
Summary:        EGL support for libglvnd
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%{!?_without_mesa_glvnd_default:
Recommends:     mesa-libEGL%{?_isa} >= 13.0.4-1
Provides:       libEGL
Provides:       libEGL%{?_isa}
}

%description    egl
libEGL are the common dispatch interface for the EGL API.

%package        glx
Summary:        GLX support for libglvnd
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%{!?_without_mesa_glvnd_default:
Recommends:     mesa-libGL%{?_isa} >= 13.0.4-1
Provides:       libGL
Provides:       libGL%{?_isa}
}

%description    glx
libGL and libGLX are the common dispatch interface for the GLX API.

%prep
%oreon_sha256

%autosetup -p1 -n %{name}-v%{version}-%{commit0}
autoreconf -vif

%build
export PYTHON=%{__python3}
%configure \
  --disable-static \
  --enable-asm \
  --enable-tls

%make_build V=1

%install
%make_install INSTALL="install -p"
find %{buildroot} -name '*.la' -delete

%{?_without_mesa_glvnd_default:
mkdir -p %{buildroot}%{_libdir}/%{name}/
for l in libEGL libGL libGLESv1_CM libGLESv2 libGLX; do
  mv %{buildroot}%{_libdir}/${l}.so* \
    %{buildroot}%{_libdir}/%{name}/
done
}

mkdir -p %{buildroot}%{_sysconfdir}/glvnd/egl_vendor.d/
mkdir -p %{buildroot}%{_datadir}/glvnd/egl_vendor.d/
mkdir -p %{buildroot}%{_sysconfdir}/egl/egl_external_platform.d/
mkdir -p %{buildroot}%{_datadir}/egl/egl_external_platform.d/

%check
%if %{without bootstrap}
export DO_X11_TESTS=1
xvfb-run -s '-screen 0 640x480x24' -d make check V=1 || \
%ifarch s390x ppc64
    :
%else
    (cat `find . -name test-suite.log` ; exit 1)
%endif
export DO_X11_TESTS=1
xwfb-run -c %{compositor} -- make check V=1 || \
%ifarch s390x ppc64
    :
%else
    (cat `find . -name test-suite.log` ; exit 1)
%endif
%else
make check V=1 || \
%ifarch s390x ppc64
    :
%else
    (cat `find . -name test-suite.log` ; exit 1)
%endif
%endif

%ldconfig_scriptlets
%files
%doc README.md
%dir %{_sysconfdir}/glvnd/
%dir %{_datadir}/glvnd/
%{_libdir}/libGLdispatch.so.0*

%ldconfig_scriptlets opengl
%files opengl
%{_libdir}/libOpenGL.so.0*

%ldconfig_scriptlets gles
%files gles
%if 0%{?_without_mesa_glvnd_default}
%{_libdir}/%{name}/libGLES*.so.*
%else
%{_libdir}/libGLES*.so.*
%endif

%ldconfig_scriptlets glx
%files glx
%if 0%{?_without_mesa_glvnd_default}
%{_libdir}/%{name}/libGL.so.*
%{_libdir}/%{name}/libGLX.so.*
%else
%{_libdir}/libGL.so.*
%{_libdir}/libGLX.so.*
%endif

%ldconfig_scriptlets egl
%files egl
%dir %{_sysconfdir}/glvnd/egl_vendor.d/
%dir %{_datadir}/glvnd/egl_vendor.d/
%dir %{_sysconfdir}/egl/
%dir %{_sysconfdir}/egl/egl_external_platform.d/
%dir %{_datadir}/egl/
%dir %{_datadir}/egl/egl_external_platform.d/
%if 0%{?_without_mesa_glvnd_default}
%{_libdir}/%{name}/libEGL*.so.*
%else
%{_libdir}/libEGL*.so.*
%endif

%files core-devel
%dir %{_includedir}/glvnd/
%{_includedir}/glvnd/*.h
%{_libdir}/pkgconfig/libglvnd.pc

%files devel
%dir %{_includedir}/EGL/
%dir %{_includedir}/GL/
%dir %{_includedir}/GLES/
%dir %{_includedir}/GLES2/
%dir %{_includedir}/GLES3/
%dir %{_includedir}/KHR/
%{_includedir}/EGL/*.h
%{_includedir}/GL/*.h
%{_includedir}/GLES/*.h
%{_includedir}/GLES2/*.h
%{_includedir}/GLES3/*.h
%{_includedir}/KHR/*.h
%{_libdir}/lib*.so
%if 0%{?_without_mesa_glvnd_default}
%{_libdir}/%{name}/lib*.so
%endif
%{_libdir}/pkgconfig/gl*.pc
%{_libdir}/pkgconfig/egl.pc
%{_libdir}/pkgconfig/opengl.pc

%changelog
%autochangelog
