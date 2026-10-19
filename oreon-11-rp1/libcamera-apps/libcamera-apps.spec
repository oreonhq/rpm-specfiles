%global source0_hash 0df9674449f4a807d3728b60578ec0a980a370eb531119b048580b60d0c22f43
Name:    libcamera-apps
Version: 1.13.0
Release:        1%{?dist}
Summary:        A small suite of libcamera-based apps
License: BSD
URL:     https://github.com/raspberrypi/rpicam-apps
Source0:        https://github.com/raspberrypi/rpicam-apps/archive/v%{version}.tar.gz#/rpicam-apps-%{version}.tar.gz
Patch1: 0001-rpi-namespace.patch
ExcludeArch:   %{power64} s390x
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  libX11-devel
BuildRequires:  libavcodec-free-devel
BuildRequires:  libavdevice-free-devel
BuildRequires:  libavutil-free-devel
BuildRequires:  libcamera-devel
BuildRequires:  libdrm-devel
BuildRequires:  libepoxy-devel
BuildRequires:  libexif-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  libswresample-free-devel
BuildRequires:  libtiff-devel
BuildRequires:  meson
BuildRequires:  qt6-qtbase-devel
# /oreon:deps
%description
This is a small suite of libcamera-based apps that aim to copy the functionality
of the existing "raspicam" apps.

%package devel
Summary:        libcamera-apps library development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Headers for developing against libcamera-apps.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir rpicam-apps-%{version}
%oreon_prep
%build

%meson \
    -Denable_drm=enabled \
    -Denable_egl=enabled \
    -Denable_qt=enabled \
    -Denable_libav=enabled \
    -Denable_hailo=disabled \
%ifarch aarch64
    -Dneon_flags=arm64 \
%endif
%ifnarch aarch64
    -Ddisable_rpi_features=true \
%endif
    %{nil}
%meson_build
%install
%meson_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libcamera-apps-devel -f %{oreon_filedir}/libcamera-apps-devel.list

%changelog

%autochangelog
