%global source0_hash b2567ce355f3ea6dfa648f679f2f724b66a55f17205656cfd4eee4be1b429171
%bcond check 1
%global forgeurl https://gitlab.com/gabmus/envision
Name:           envision
Version:        3.2.0
Release:        1%{?dist}
Summary:        UI for building, configuring, and running Monado/WiVRn
%forgemeta
License:        %{shrink:
    AGPL-3.0-or-later
    AND Apache-2.0
    AND BSD-3-Clause
    AND GPL-2.0-only WITH GCC-exception-2.0
    AND ISC
    AND LGPL-2.1-or-later
    AND MIT
    AND Unicode-3.0
    AND Unicode-DFS-2016
    AND Zlib
    AND (Apache-2.0 OR MIT)
    AND (Apache-2.0 OR BSL-1.0)
    AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
    AND (BSD-2-Clause OR Apache-2.0 OR MIT)
    AND (Unlicense OR MIT)
}
URL:            %{forgeurl}
Source0:        %{forgeurl}/-/archive/%{version}/%{name}-%{version}.tar.bz2
Patch0:         0001-fix-drop-RUSTFLAGS-override-from-cargo-clippy-test.patch
Patch1:         0001-Bump-git2-dependency-from-0.19-to-0.20.patch
Patch2:         envision-fix-wivrn-apk-download-location.patch
Requires:       hicolor-icon-theme
Requires:       patch
Suggests:       android-tools
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  clippy
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  eigen3
BuildRequires:  g++
BuildRequires:  gdb-gdbserver
BuildRequires:  git
BuildRequires:  glib2-devel
BuildRequires:  glslang
BuildRequires:  glslc
BuildRequires:  gtk4-devel
BuildRequires:  gtksourceview5-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libadwaita-devel
BuildRequires:  libappstream-glib
BuildRequires:  libdrm
BuildRequires:  libgudev-devel
BuildRequires:  libusb1-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  meson
BuildRequires:  openssl-devel
BuildRequires:  openxr-devel
BuildRequires:  rustc
BuildRequires:  rustfmt
BuildRequires:  vte291-gtk4-devel
BuildRequires:  vulkan-headers
BuildRequires:  vulkan-loader-devel
# /oreon:deps
%description
UI for building, configuring, and running Monado, the open source 
OpenXR runtime.

This is still highly experimental software, while it's unlikely that 
anything bad will happen, it's still unstable and there is no guarantee 
that it will work on your system, with your particular hardware. If you 
encounter any problems while using the app, make sure to open an issue.

Also consider that due to the unstable nature of the app, it's possible 
to encounter unexpected behavior that while in VR might cause motion 
sickness or physical injury. Be very careful while in VR using this app!

%package wivrn
Summary:        WiVRn Build Dependencies for Envision
Requires:       %{name} = %{version}-%{release}
Requires:       boost-devel
Requires:       cmake
Requires:       desktop-file-utils
Requires:       extra-cmake-modules
Requires:       gcc-c++
Requires:       gettext-devel
Requires:       git
Requires:       glslc
Requires:       kf6-kcoreaddons-devel
Requires:       kf6-ki18n-devel
Requires:       kf6-kiconthemes-devel
Requires:       kf6-kirigami-devel
Requires:       libappstream-glib
Requires:       librsvg2-tools
Requires:       ninja-build
Requires:       openxr-devel
Requires:       python
Requires:       pkgconfig(avahi-client)
Requires:       pkgconfig(avahi-glib)
Requires:       pkgconfig(bluez)
Requires:       pkgconfig(CLI11)
Requires:       pkgconfig(dbus-1)
Requires:       pkgconfig(eigen3)
Requires:       pkgconfig(glslang)
Requires:       pkgconfig(gstreamer-1.0)
Requires:       pkgconfig(gstreamer-app-1.0)
Requires:       pkgconfig(gstreamer-video-1.0)
Requires:       pkgconfig(hidapi-libusb)
Requires:       pkgconfig(libarchive)
Requires:       pkgconfig(libavcodec)
Requires:       pkgconfig(libavfilter)
Requires:       pkgconfig(libavutil)
Requires:       pkgconfig(libbsd)
Requires:       pkgconfig(libcap)
Requires:       pkgconfig(libcjson)
Requires:       pkgconfig(libdrm)
Requires:       pkgconfig(libjpeg)
Requires:       pkgconfig(libnotify)
Requires:       pkgconfig(libpipewire-0.3)
Requires:       pkgconfig(libudev)
Requires:       pkgconfig(libusb-1.0)
Requires:       pkgconfig(libuvc)
Requires:       pkgconfig(librsvg-2.0)
Requires:       pkgconfig(libswscale)
Requires:       pkgconfig(libva)
Requires:       pkgconfig(nlohmann_json)
Requires:       pkgconfig(opencv)
Requires:       pkgconfig(openhmd)
Requires:       pkgconfig(openssl)
Requires:       pkgconfig(openvr)
Requires:       pkgconfig(Qt6)
Requires:       pkgconfig(Qt6Linguist)
Requires:       pkgconfig(Qt6Quick)
Requires:       pkgconfig(realsense2)
Requires:       pkgconfig(sdl2)
Requires:       pkgconfig(vulkan)
Requires:       pkgconfig(wayland-client)
Requires:       pkgconfig(wayland-eglstream)
Requires:       pkgconfig(wayland-protocols)
Requires:       pkgconfig(wayland-scanner)
Requires:       pkgconfig(xrandr)
Requires:       qcoro-qt6-devel
Requires:       qt6-qtbase-private-devel
Requires:       qt6-qtdeclarative-devel
Requires:       qt6qml(org.kde.desktop)
Requires:       android-tools
Requires:       firewalld-filesystem
Requires:       hicolor-icon-theme
%description wivrn
Build dependencies for WiVRn. Install this to automatically
bring in all needed dependencies for building WiVRn.

%package monado
Summary:        Monado Build Dependencies for Envision
Requires:       %{name} = %{version}-%{release}
Requires:       cmake
Requires:       gcc-c++
Requires:       glslc
Requires:       ninja-build
Requires:       pkgconfig(bluez)
Requires:       pkgconfig(dbus-1)
Requires:       pkgconfig(dri)
Requires:       pkgconfig(eigen3)
Requires:       pkgconfig(glslang)
Requires:       pkgconfig(gstreamer-1.0)
Requires:       pkgconfig(gstreamer-app-1.0)
Requires:       pkgconfig(gstreamer-video-1.0)
Requires:       pkgconfig(hidapi-libusb)
Requires:       pkgconfig(libavcodec)
Requires:       pkgconfig(libbsd)
Requires:       pkgconfig(libcjson)
Requires:       pkgconfig(libdrm)
Requires:       pkgconfig(libjpeg)
%ifnarch s390x %{arm} %{ix86}
Requires:       pkgconfig(libonnxruntime)
%endif
Requires:       pkgconfig(libudev)
Requires:       pkgconfig(libusb-1.0)
Requires:       pkgconfig(libuvc)
Requires:       pkgconfig(opencv)
Requires:       pkgconfig(openhmd)
Requires:       pkgconfig(openvr)
Requires:       pkgconfig(openxr)
Requires:       pkgconfig(realsense2)
Requires:       pkgconfig(sdl2)
Requires:       pkgconfig(vulkan)
Requires:       pkgconfig(wayland-client)
Requires:       pkgconfig(wayland-eglstream)
Requires:       pkgconfig(wayland-protocols)
Requires:       pkgconfig(wayland-scanner)
Requires:       pkgconfig(xrandr)
Requires:       pkgconfig(zlib)
%description monado
Build dependencies for Monado. Install this to automatically
bring in all needed dependencies for building Monado.

%package xrizer
Summary:        Xrizer Build Dependencies for Envision
Requires:       %{name} = %{version}-%{release}
Recommends:     cargo
Requires:       clang19-devel
Requires:       libxcb-devel
Requires:       wayland-devel
%description xrizer
Build dependencies for xrizer. Install this to automatically
bring in all needed dependencies for building xrizer.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

%meson -D profile=release
%meson_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%meson_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/org.gabmus.envision.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%if %{with check}
%meson_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n envision-wivrn -f %{oreon_filedir}/envision-wivrn.list
%files -n envision-monado -f %{oreon_filedir}/envision-monado.list
%files -n envision-xrizer -f %{oreon_filedir}/envision-xrizer.list

%changelog

%autochangelog
