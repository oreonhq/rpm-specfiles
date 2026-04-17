%global qt_module qtmultimedia

%global gst 0.10
%if 0%{?fedora} || 0%{?rhel} > 7
%global gst 1.0
%endif

# Oreon 11 composes expect the FFmpeg backend. %%{rhel} gating would otherwise default it off.
%bcond_without ffmpeg

#global unstable 0
%if 0%{?unstable}
%global prerelease rc
%endif

%global examples 1

# PCH plus distro LTO optflags runs one giant cc1plus per target. That OOMs low-RAM builders (x86_64 mock too).
%global _lto_cflags %{nil}

Summary: Qt6 - Multimedia support
Name:    qt6-%{qt_module}
Version: 6.10.3
Release: 5%{?dist}

License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global  majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)

%if 0%{?unstable}
Source0: https://download.qt.io/development_releases/qt/%{majmin}/%{qt_version}/submodules/%{qt_module}-everywhere-src-%{qt_version}-%{prerelease}.tar.xz
%else
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
%endif

Patch0:  qtmultimedia-fix-build-on-x86-arch.patch

# filter plugin/qml provides
%global __provides_exclude_from ^(%{_qt6_archdatadir}/qml/.*\\.so|%{_qt6_plugindir}/.*\\.so)$

BuildRequires: cmake
BuildRequires: gcc-c++
%if 0%{?rhel} && 0%{?rhel} < 10
BuildRequires: gcc-toolset-13
%endif
BuildRequires: ninja-build
BuildRequires: qt6-rpm-macros
BuildRequires: qt6-qtbase-devel >= %{version}
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: qt6-qtdeclarative-devel >= %{version}
BuildRequires: qt6-qtshadertools-devel >= %{version}
BuildRequires: qt6-qtquick3d-devel >= %{version}
BuildRequires: pkgconfig(alsa)
%if "%{?gst}" == "0.10"
BuildRequires: pkgconfig(gstreamer-interfaces-0.10)
%endif
BuildRequires: pkgconfig(gstreamer-%{gst})
BuildRequires: pkgconfig(gstreamer-app-%{gst})
BuildRequires: pkgconfig(gstreamer-audio-%{gst})
BuildRequires: pkgconfig(gstreamer-base-%{gst})
BuildRequires: pkgconfig(gstreamer-pbutils-%{gst})
BuildRequires: pkgconfig(gstreamer-plugins-bad-%{gst})
BuildRequires: pkgconfig(gstreamer-video-%{gst})
BuildRequires: pkgconfig(libpulse) pkgconfig(libpulse-mainloop-glib)
%if %{with ffmpeg}
BuildRequires: ffmpeg-free-devel
BuildRequires: libavcodec-free-devel
BuildRequires: libavutil-free-devel
BuildRequires: libavformat-free-devel
BuildRequires: libswscale-free-devel
BuildRequires: libswresample-free-devel
BuildRequires: pkgconfig(libva) pkgconfig(libva-drm)
BuildRequires: pkgconfig(libpipewire-0.3)
%endif
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xv)
BuildRequires: pkgconfig(xkbcommon) >= 0.5.0
BuildRequires: openssl-devel
# workaround missing dep
# /usr/include/gstreamer-1.0/gst/gl/wayland/gstgldisplay_wayland.h:26:10: fatal error: wayland-client.h: No such file or directory
BuildRequires: wayland-devel

%description
The Qt Multimedia module provides a rich feature set that enables you to
easily take advantage of a platforms multimedia capabilites and hardware.
This ranges from the playback and recording of audio and video content to
the use of available devices like cameras and radios.

# libgstreamermediaplugin.so links GStreamer and Pulse; explicit for minimal ISO trees
Requires:      gstreamer1%{?_isa}
Requires:      gstreamer1-plugins-base%{?_isa}
Requires:      gstreamer1-plugins-good%{?_isa}
Requires:      gstreamer1-plugins-bad-free%{?_isa}
# libgstphotography etc. live in the -libs split; explicit for ISO / minimal roots
Requires:      gstreamer1-plugins-bad-free-libs%{?_isa}
Requires:      pulseaudio-libs%{?_isa}
Requires:      libXrandr%{?_isa}
Requires:      libXext%{?_isa}
%if %{with ffmpeg}
Requires:      ffmpeg-libs%{?_isa}
%endif

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
Requires: qt6-qtdeclarative-devel%{?_isa}
# Qt6Multimedia.pc containts:
# Libs.private: ... -lpulse-mainloop-glib -lpulse -lglib-2.0
Requires: pkgconfig(libpulse-mainloop-glib)
%description devel
%{summary}.

%if 0%{?examples}
%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
# BuildRequires: qt6-qtmultimedia-devel (same version as this package)
%description examples
%{summary}.
%endif

%prep
%autosetup -n %{qt_module}-everywhere-src-%{qt_version}%{?unstable:-%{prerelease}} -p1


%build
%if 0%{?rhel} && 0%{?rhel} < 10
. /opt/rh/gcc-toolset-13/enable
%endif
%cmake_qt6 \
  -DCMAKE_DISABLE_PRECOMPILE_HEADERS=ON \
  -DQT_BUILD_EXAMPLES:BOOL=%{?examples:ON}%{!?examples:OFF} \
  -DQT_INSTALL_EXAMPLES_SOURCES=%{?examples:ON}%{!?examples:OFF}

%cmake_build


%install
%cmake_install

## .prl/.la file love
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
pushd %{buildroot}%{_qt6_libdir}
for prl_file in *.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd

# Probably not needed on Linux installs
rm -r %{buildroot}%{_qt6_archdatadir}/mkspecs/features/ios/add_ios_ffmpeg_libraries.prf

%ldconfig_scriptlets

%files
%license LICENSES/*
%{_qt6_archdatadir}/sbom/%{qt_module}-%{qt_version}.spdx
%{_qt6_libdir}/libQt6Multimedia.so.6*
%{_qt6_libdir}/libQt6MultimediaQuick.so.6*
%{_qt6_libdir}/libQt6MultimediaWidgets.so.6*
%{_qt6_libdir}/libQt6SpatialAudio.so.6*
%{_qt6_libdir}/libQt6Quick3DSpatialAudio.so.6*
%{_qt6_archdatadir}/qml/QtMultimedia/
%dir %{_qt6_archdatadir}/qml/QtQuick3D/SpatialAudio
%{_qt6_archdatadir}/qml/QtQuick3D/SpatialAudio/
%dir %{_qt6_plugindir}/multimedia
%{_qt6_plugindir}/multimedia/libgstreamermediaplugin.so
%if %{with ffmpeg}
%{_qt6_plugindir}/multimedia/libffmpegmediaplugin.so
%endif

%files devel
%if %{with ffmpeg}
%{_qt6_headerdir}/QtFFmpegMediaPluginImpl/
%endif
%{_qt6_headerdir}/QtGstreamerMediaPluginImpl/
%{_qt6_headerdir}/QtMultimedia/
%{_qt6_headerdir}/QtMultimediaTestLib/
%{_qt6_headerdir}/QtMultimediaQuick/
%{_qt6_headerdir}/QtMultimediaWidgets/
%{_qt6_headerdir}/QtSpatialAudio/
%{_qt6_headerdir}/QtQuick3DSpatialAudio/
%{_qt6_libdir}/libQt6BundledResonanceAudio.a
%if %{with ffmpeg}
%{_qt6_libdir}/libQt6FFmpegMediaPluginImpl.a
%{_qt6_libdir}/libQt6FFmpegMediaPluginImpl.prl
%endif
%{_qt6_libdir}/libQt6GstreamerMediaPluginImpl.a
%{_qt6_libdir}/libQt6GstreamerMediaPluginImpl.prl
%{_qt6_libdir}/libQt6Multimedia.so
%{_qt6_libdir}/libQt6Multimedia.prl
%{_qt6_libdir}/libQt6MultimediaTestLib.a
%{_qt6_libdir}/libQt6MultimediaTestLib.prl
%{_qt6_libdir}/libQt6MultimediaQuick.so
%{_qt6_libdir}/libQt6MultimediaQuick.prl
%{_qt6_libdir}/libQt6MultimediaWidgets.so
%{_qt6_libdir}/libQt6MultimediaWidgets.prl
%{_qt6_libdir}/libQt6SpatialAudio.so
%{_qt6_libdir}/libQt6SpatialAudio.prl
%{_qt6_libdir}/libQt6Quick3DSpatialAudio.so
%{_qt6_libdir}/libQt6Quick3DSpatialAudio.prl
%dir  %{_qt6_libdir}/cmake/Qt6MultimediaQuickPrivate
%dir %{_qt6_libdir}/cmake/Qt6BundledResonanceAudio/
%if %{with ffmpeg}
%dir %{_qt6_libdir}/cmake/Qt6FFmpegMediaPluginImplPrivate
%endif
%dir %{_qt6_libdir}/cmake/Qt6GstreamerMediaPluginImplPrivate
%dir %{_qt6_libdir}/cmake/Qt6Multimedia
%dir %{_qt6_libdir}/cmake/Qt6MultimediaPrivate
%dir %{_qt6_libdir}/cmake/Qt6MultimediaTestLibPrivate/
%dir %{_qt6_libdir}/cmake/Qt6MultimediaWidgets
%dir %{_qt6_libdir}/cmake/Qt6MultimediaWidgetsPrivate
%dir %{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins
%dir %{_qt6_libdir}/cmake/Qt6Quick3DSpatialAudioPrivate
%dir %{_qt6_libdir}/cmake/Qt6SpatialAudio/
%dir %{_qt6_libdir}/cmake/Qt6SpatialAudioPrivate
%{_qt6_libdir}/cmake/Qt6/*.cmake
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/*.cmake
%{_qt6_libdir}/cmake/Qt6BundledResonanceAudio/*.cmake
%if %{with ffmpeg}
%{_qt6_libdir}/cmake/Qt6FFmpegMediaPluginImplPrivate/*.cmake
%endif
%{_qt6_libdir}/cmake/Qt6GstreamerMediaPluginImplPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6Multimedia/*.cmake
%{_qt6_libdir}/cmake/Qt6MultimediaPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6MultimediaQuickPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6MultimediaTestLibPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6MultimediaWidgets/*.cmake
%{_qt6_libdir}/cmake/Qt6MultimediaWidgetsPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_libdir}/cmake/Qt6Quick3DSpatialAudioPrivate/*cmake
%{_qt6_libdir}/cmake/Qt6SpatialAudio/*cmake
%{_qt6_libdir}/cmake/Qt6SpatialAudioPrivate/*.cmake
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/qt6/modules/*.json
%{_qt6_libdir}/pkgconfig/*.pc

%if 0%{?examples}
%files examples
%{_qt6_examplesdir}/
%endif


%changelog
* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.3-5
- Require gstreamer1-plugins-bad-free-libs (libgstphotography etc.) for minimal ISO trees

* Tue Apr 14 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.3-4
- Sync module to Qt 6.10.3 (match qt6-qtbase / qt6-rpm-macros)

* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.2-4
- Clear %%_lto_cflags and disable CMake PCH so MultimediaQuick cmake_pch.hxx gch does not OOM cc1plus

* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.2-3
- Drop aarch64 and s390x %%_smp_mflags and %%_lto_cflags OOM workarounds

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.2-1
- Prepare for Oreon 11 (RP1)
