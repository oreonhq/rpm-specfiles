%global source0_hash 3143f53b64257ba2a0685c940f5dce476c75871ff86b516de45cfd54ea93a62d
%global qt_module qtmultimedia
%global gst 0.10
%if 0%{?fedora} || 0%{?rhel} > 7 || (0%{?oreon} >= 11)
%global gst 1.0
%endif
%if 0%{?rhel} && ! 0%{?epel} || (0%{?oreon} >= 11)
%bcond_with ffmpeg
%else
%bcond_without ffmpeg
%endif
%if 0%{?unstable}
%global prerelease rc
%endif
%global examples 1
Summary:        Qt6 - Multimedia support
Name:    qt6-%{qt_module}
Version: 6.12.0
Release:        1%{?dist}
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global  majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)
%if 0%{?unstable}
%else
Source0:        https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-s%{prerelease}-%{version}.tar.xz
%endif
Patch0:        qtmultimedia-fix-build-on-x86-arch.patch
%global __provides_exclude_from ^(%{_qt6_archdatadir}/qml/.*\\.so|%{_qt6_plugindir}/.*\\.so)$
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
%if "%{?gst}" == "0.10"
%endif
%if %{with ffmpeg}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  ffmpeg-free-devel
BuildRequires:  gcc-c++
BuildRequires:  libavcodec-free-devel
BuildRequires:  libavformat-free-devel
BuildRequires:  libavutil-free-devel
BuildRequires:  libswresample-free-devel
BuildRequires:  libswscale-free-devel
BuildRequires:  ninja-build
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xv)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtquick3d-devel
BuildRequires:  qt6-qtshadertools-devel
BuildRequires:  qt6-rpm-macros
BuildRequires:  wayland-devel
# /oreon:deps
%description
The Qt Multimedia module provides a rich feature set that enables you to
easily take advantage of a platforms multimedia capabilites and hardware.
This ranges from the playback and recording of audio and video content to
the use of available devices like cameras and radios.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
Requires: qt6-qtdeclarative-devel%{?_isa}
Requires: pkgconfig(libpulse-mainloop-glib)
%description devel
%{summary}.

%if 0%{?examples}
%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{qt_module}-everywhere-src-%{qt_version}%{?unstable:-%{prerelease}} -p1

%build

%cmake_qt6 -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
  -DQT_BUILD_EXAMPLES:BOOL=%{?examples:ON}%{!?examples:OFF} \
  -DQT_INSTALL_EXAMPLES_SOURCES=%{?examples:ON}%{!?examples:OFF}
%cmake_build
%install
%cmake_install
pushd %{buildroot}%{_qt6_libdir}
for prl_file in *.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd
rm -r %{buildroot}%{_qt6_archdatadir}/mkspecs/features/ios/add_ios_ffmpeg_libraries.prf
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n qt6-qtmultimedia-devel -f %{oreon_filedir}/qt6-qtmultimedia-devel.list
%files -n qt6-qtmultimedia-examples -f %{oreon_filedir}/qt6-qtmultimedia-examples.list

%changelog

%autochangelog
