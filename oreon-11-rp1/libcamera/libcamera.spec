%global source0_hash 6f35dd479dd634a1ec50852fa9716c9da81a6c07af93bbf2990f7bbd829f0dfd
Name:    libcamera
Version: 0.7.2
Release:        1%{?dist}
Summary:        A library to support complex camera ISPs
License: LGPL-2.1-or-later
URL:     http://libcamera.org/
Source0:        https://gitlab.freedesktop.org/camera/libcamera/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
Source1: qcam.desktop
Source2: qcam.metainfo.xml
Source3: 70-libcamera.rules
Patch01: 0001-disable-rpi-pisp.patch
ExcludeArch: s390x ppc64le
Recommends: %{name}-ipa%{?_isa}
Obsoletes: libcamera-doc < 0.6.0
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gnutls-devel
BuildRequires:  gtest-devel
BuildRequires:  libatomic
BuildRequires:  libevent-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libtiff-devel
BuildRequires:  libyaml-devel
BuildRequires:  libyuv-devel
BuildRequires:  lttng-ust-devel
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  openssl
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6OpenGL)
BuildRequires:  pkgconfig(Qt6OpenGLWidgets)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-allocators-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pybind11-devel
BuildRequires:  python3-devel
BuildRequires:  python3-jinja2
BuildRequires:  python3-ply
BuildRequires:  python3-pyyaml
BuildRequires:  systemd-devel
# /oreon:deps
%description
libcamera is a library that deals with heavy hardware image processing
operations of complex camera devices that are shared between the linux
host all while allowing offload of certain aspects to the control of
complex camera hardware such as ISPs.

Hardware support includes USB UVC cameras, libv4l cameras as well as more
complex ISPs (Image Signal Processor).

%package     devel
Summary:     Development package for %{name}
Requires:    %{name}%{?_isa} = %{version}-%{release}
%description devel
Files for development with %{name}.

%package     ipa
Summary:     ISP Image Processing Algorithm Plugins for %{name}
License:     LGPL-2.1-or-later AND BSD-2-Clause
Requires:    %{name}%{?_isa} = %{version}-%{release}
%description ipa
Image Processing Algorithms plugins for interfacing with device
ISPs for %{name}

%package     tools
Summary:     Tools for %{name}
License:     LGPL-2.1-or-later AND BSD-3-Clause
Requires:    %{name}%{?_isa} = %{version}-%{release}
%description tools
Command line tools for %{name}

%package     qcam
Summary:     Graphical QCam application for %{name}
License:     GPL-2.0-or-later AND MIT
Requires:    %{name}%{?_isa} = %{version}-%{release}
%description qcam
Graphical QCam application for %{name}

%package     gstreamer
Summary:     GSTreamer plugin for %{name}
Requires:    %{name}%{?_isa} = %{version}-%{release}
%description gstreamer
GSTreamer plugins for %{name}

%package     v4l2
Summary:     V4L2 compatibility layer for %{name}
Requires:    %{name}%{?_isa} = %{version}-%{release}
%description v4l2
V4L2 compatibility layer for %{name}

%package     -n python3-%{name}
Summary:     Python bindings for %{name}
Requires:    %{name}%{?_isa} = %{version}-%{release}
%description -n python3-%{name}
Python bindings for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-v%{version}
%oreon_prep
%build

%global _lto_cflags %{nil}
export CFLAGS="%{optflags} -Wno-deprecated-declarations"
export CXXFLAGS="%{optflags} -Wno-deprecated-declarations --param=max-devirt-targets=1"
%meson \
    -Dv4l2=enabled \
    -Dlc-compliance=disabled \
    %{?rhel:-Dlibunwind=disabled} \
    -Dtest=true \
    -Ddocumentation=disabled \
    -Drpi-awb-nn=disabled \
    %{nil}
%meson_build
%define __spec_install_post \
    %{?__debug_package:%{__debug_install_post}} \
    %{__arch_install_post} \
    %{__os_install_post} \
    %{_builddir}/%{name}-v%{version}/src/ipa/ipa-sign-install.sh %{_builddir}/%{name}-v%{version}/%{_vpath_builddir}/src/ipa-priv-key.pem %{buildroot}/%{_libdir}/libcamera/ipa_*.so \
%{nil}
%install
%meson_install
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
                     %SOURCE1
mkdir -p %{buildroot}/%{_metainfodir}/
cp -a %SOURCE2 %{buildroot}/%{_metainfodir}/
mkdir -p %{buildroot}/%{_udevrulesdir}/
install -D -m 644 %SOURCE3 %{buildroot}/%{_udevrulesdir}/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n libcamera-devel -f %{oreon_filedir}/libcamera-devel.list
%files -n libcamera-ipa -f %{oreon_filedir}/libcamera-ipa.list
%files -n libcamera-tools -f %{oreon_filedir}/libcamera-tools.list
%files -n libcamera-qcam -f %{oreon_filedir}/libcamera-qcam.list
%files -n libcamera-gstreamer -f %{oreon_filedir}/libcamera-gstreamer.list
%files -n libcamera-v4l2 -f %{oreon_filedir}/libcamera-v4l2.list
%files -n python3-libcamera -f %{oreon_filedir}/python3-libcamera.list

%changelog

%autochangelog
