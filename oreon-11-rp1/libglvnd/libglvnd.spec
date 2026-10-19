%global source0_hash 8797914ff69e62d7d89b331cab311b29fff5cfaddae5aae09695a7ccbaf353d7
%global commit0 faa23f21fc677af5792825dc30cb1ccef4bf33a6
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global compositor weston
%global x11_tests 1
Name:           libglvnd
Version:        1.7.0
Release:        9%{?dist}
Epoch:          1
Summary:        The GL Vendor-Neutral Dispatch library
License:        MIT-feh AND MIT-Modern-Variant AND BSD-1-Clause AND BSD-3-Clause AND GPL-3.0-or-later WITH Autoconf-exception-macro
URL:            https://gitlab.freedesktop.org/glvnd/libglvnd
Source0:        https://gitlab.freedesktop.org/glvnd/libglvnd/-/archive/v1.7.0/libglvnd-1.7.0.tar.gz
Patch1:         0001-glx-Add-another-fallback-library-name.patch
%if 0%{?x11_tests}
%endif
%if 0%{?compositor:1}
%endif
%{?_without_mesa_glvnd_default:
%global __provides_exclude_from %{_libdir}/%{name}
%global __requires_exclude_from %{_libdir}/%{name}
}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mesa-dri-drivers
BuildRequires:  pkgconfig(glproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  python3-libxml2
BuildRequires:  python3-rpm-macros
BuildRequires:  weston
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  xwayland-run
# /oreon:deps
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
%{!?flatpak_runtime:
Requires:       mesa-libEGL%{?_isa} >= 13.0.4-1
}
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
%{!?flatpak_runtime:
Requires:       mesa-libEGL%{?_isa} >= 13.0.4-1
}
Provides:       libEGL
Provides:       libEGL%{?_isa}
}
%description    egl
libEGL are the common dispatch interface for the EGL API.

%package        glx
Summary:        GLX support for libglvnd
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%{!?_without_mesa_glvnd_default:
%{!?flatpak_runtime:
Requires:       mesa-libGL%{?_isa} >= 13.0.4-1
}
Provides:       libGL
Provides:       libGL%{?_isa}
}
%description    glx
libGL and libGLX are the common dispatch interface for the GLX API.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-v%{version}-%{?commit0}
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.*

%check

%if 0%{?x11_tests}
export DO_X11_TESTS=1
xvfb-run -s '-screen 0 640x480x24' -d make check V=1 || \
%ifarch s390x ppc64
    :
%else
    (cat `find . -name test-suite.log` ; exit 1)
%endif
%endif
%if 0%{?compositor:1}
export DO_X11_TESTS=1
xwfb-run -c %{compositor} -- make check V=1 || \
%ifarch s390x ppc64
    :
%else
    (cat `find . -name test-suite.log` ; exit 1)
%endif
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libglvnd-devel -f %{oreon_filedir}/libglvnd-devel.list
%files -n libglvnd-core-devel -f %{oreon_filedir}/libglvnd-core-devel.list
%files -n libglvnd-opengl -f %{oreon_filedir}/libglvnd-opengl.list
%files -n libglvnd-gles -f %{oreon_filedir}/libglvnd-gles.list
%files -n libglvnd-egl -f %{oreon_filedir}/libglvnd-egl.list
%files -n libglvnd-glx -f %{oreon_filedir}/libglvnd-glx.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.7.0-9
- Prepare for Oreon 11 (RP1)
