%global source0_hash b2d01e832f5debe3327726b15ef9094bfd1b1f2d47dfa3655436ef48526edfe8

Name:    libcamera-apps
Version: 1.11.1
Release: 1%{?dist}
Summary: A small suite of libcamera-based apps
License: BSD
URL:     https://github.com/raspberrypi/rpicam-apps
Source0: %{url}/archive/v%{version}.tar.gz#/rpicam-apps-%{version}.tar.gz

Patch1: 0001-rpi-namespace.patch

ExcludeArch:   %{power64} s390x
BuildRequires: meson
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: boost-devel
BuildRequires: git-core
BuildRequires: libcamera-devel
BuildRequires: libdrm-devel
BuildRequires: libepoxy-devel
BuildRequires: libexif-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: libX11-devel
BuildRequires: qt6-qtbase-devel
# FFMPEG deps
BuildRequires: libavcodec-free-devel
BuildRequires: libavdevice-free-devel
BuildRequires: libavutil-free-devel
BuildRequires: libswresample-free-devel
# Will review OpenCV support in the future
# BuildRequires: opencv-devel

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

%autosetup -p1 -n rpicam-apps-%{version}

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

%files
%license license.txt
%{_bindir}/camera-bug-report
%{_bindir}/rpicam-*
%{_libdir}/librpicam_app.so.*
%{_libdir}/rpicam-apps-*/
%{_datadir}/rpi-camera-assets/

%files devel
%{_libdir}/librpicam_app.so
%{_libdir}/pkgconfig/rpicam_app.pc
%{_includedir}/rpicam-apps/

%changelog
%autochangelog
