# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 58e8fd2c02a7094ea0e9628597f58268e0ff544f479c94e6ab39ddea5362b982
%global source1_hash 739d9421f24bf6f46be439ec56989be1ce6cefa4878eb9956268c3a2cdea9ef3
%global source2_hash 9d50aa6dd4afe0b6c20693df0f5a4bce7b47e4f3a60efd44d954f874e1a47142
%global source3_hash 4fa512367f7602581703e977f4ca1eaed42199faf8ae15f1a7f47986daced955
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%ifarch %{arm64}
%bcond pisp %{undefined rhel}
%endif

Name:    libcamera
Version: 0.8.0
Release: 1%{?dist}
Summary: A library to support complex camera ISPs
License: LGPL-2.1-or-later
URL:     http://libcamera.org/

Source0: https://gitlab.freedesktop.org/camera/libcamera/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
Source1: qcam.desktop
Source2: qcam.metainfo.xml
Source3: 70-libcamera.rules

Patch0:  0001-optional-rpi-pisp.patch

ExcludeArch: s390x ppc64le

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires: gtest-devel
BuildRequires: desktop-file-utils
BuildRequires: meson
BuildRequires: openssl
BuildRequires: ninja-build
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: gnutls-devel
BuildRequires: pkgconfig(gstreamer-video-1.0)
BuildRequires: pkgconfig(gstreamer-allocators-1.0)
BuildRequires: libatomic
BuildRequires: pkgconfig(libdw)
BuildRequires: libevent-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libtiff-devel
BuildRequires: libyaml-devel
BuildRequires: libyuv-devel
BuildRequires: lttng-ust-devel
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6OpenGL)
BuildRequires: pkgconfig(Qt6OpenGLWidgets)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pybind11-devel
BuildRequires: python3-devel
BuildRequires: python3-jinja2
BuildRequires: python3-ply
BuildRequires: python3-pyyaml
BuildRequires: SDL2-devel
BuildRequires: systemd-devel
%if %{with pisp}
BuildRequires: libpisp-devel
%endif
Recommends: %{name}-ipa%{?_isa}
Obsoletes: libcamera-doc < 0.6.0

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
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
echo '%{source3_hash}  %{SOURCE3}' | sha256sum -c -
%autosetup -p1 -n %{name}-v%{version}

%build
export CFLAGS="%{optflags} -Wno-deprecated-declarations"
export CXXFLAGS="%{optflags} -Wno-deprecated-declarations"

%meson \
    -Dv4l2=enabled \
    -Dlc-compliance=disabled \
    -Dlibunwind=disabled \
    -Dtest=true \
    -Ddocumentation=disabled \
    -Drpi-awb-nn=disabled \
    %{nil}
%meson_build

%define __spec_install_post \
    %{?__debug_package:%{__debug_install_post}} \
    %{__arch_install_post} \
    %{__os_install_post} \
    %{_builddir}/%{name}-v%{version}/src/ipa/ipa-sign-install.sh %{_builddir}/%{name}-v%{version}/%{_vpath_builddir}/src/ipa-priv-key.pem %{buildroot}/%{_libdir}/libcamera/ipa/ipa_*.so \
%{nil}

%install
%meson_install

desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
                     %SOURCE1

mkdir -p %{buildroot}/%{_metainfodir}/
cp -a %SOURCE2 %{buildroot}/%{_metainfodir}/

mkdir -p %{buildroot}/%{_udevrulesdir}/
install -D -m 644 %SOURCE3 %{buildroot}/%{_udevrulesdir}/

%files
%license COPYING.rst LICENSES/LGPL-2.1-or-later.txt
%{_libdir}/libcamera*.so.0.8
%{_libdir}/libcamera*.so.%{version}
%{_udevrulesdir}/70-libcamera.rules

%files devel
%{_includedir}/%{name}/
%{_libdir}/libcamera*.so
%{_libdir}/pkgconfig/libcamera-base.pc
%{_libdir}/pkgconfig/libcamera.pc

%files ipa
%{_datadir}/libcamera/
%{_libdir}/libcamera/
%{_libexecdir}/libcamera/
%exclude %{_libexecdir}/libcamera/v4l2-compat.so

%files gstreamer
%{_libdir}/gstreamer-1.0/libgstlibcamera.so

%files qcam
%{_bindir}/qcam
%{_datadir}/applications/qcam.desktop
%{_metainfodir}/qcam.metainfo.xml

%files tools
%license LICENSES/GPL-2.0-only.txt
%{_bindir}/cam
%{_bindir}/libcamera-bug-report

%files v4l2
%{_bindir}/libcamerify
%{_libexecdir}/libcamera/v4l2-compat.so

%files -n python3-%{name}
%{python3_sitearch}/*

%changelog
%autochangelog
