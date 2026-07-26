%global source0_hash 93f7ef0106fbd731165a2723f3e436c911fc5e6880f5bc987b55516c20833e2b

%{?mingw_package_header}

%global qt_module qtmultimedia
#global pre rc

#global commit a73dfa7c63b82e25f93e44ed6386664373aaca74
#global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?commit:1}
%global source_folder %{qt_module}-%{commit}
%else
%global source_folder %{qt_module}-everywhere-src-%{qt_version}%{?pre:-%{pre}}
%endif

# first two digits of version
%global release_version %(echo %{version} | awk -F. '{print $1"."$2}')
%define qt_version %(echo %{version} | cut -d~ -f1)

Name:           mingw-qt6-%{qt_module}
Version:        6.10.2
Release:        1%{?dist}
Summary:        Qt6 for Windows - QtMultimedia component

License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            http://qt.io/

%if 0%{?commit:1}
Source0:        https://github.com/qt/%{qt_module}/archive/%{commit}/%{qt_module}-everywhere-src-%{commit}.tar.gz
%else
Source0:        http://download.qt.io/%{?pre:development}%{?!pre:official}_releases/qt/%{release_version}/%{qt_version}%{?pre:-%pre}/submodules/%{qt_module}-everywhere-src-%{qt_version}%{?pre:-%pre}.tar.xz
%endif

BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  mingw32-filesystem >= 107
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt6-qtbase = %{version}
BuildRequires:  mingw32-qt6-qtshadertools = %{version}

BuildRequires:  mingw64-filesystem >= 107
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt6-qtbase = %{version}
BuildRequires:  mingw64-qt6-qtshadertools = %{version}

%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the 32-bit Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win32
%package -n mingw32-qt6-%{qt_module}
Summary:        Qt6 for Windows - QtMultimedia component

%description -n mingw32-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win64
%package -n mingw64-qt6-%{qt_module}
Summary:        Qt6 for Windows - QtMultimedia component

%description -n mingw64-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the 64-bit Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{source_folder}

%build
export MINGW32_CXXFLAGS="%{mingw32_cflags} -msse2"
export MINGW64_CXXFLAGS="%{mingw64_cflags} -msse2"
%mingw_cmake -GNinja -DCMAKE_BUILD_TYPE=RelWithDebInfo
%mingw_ninja

%install
%mingw_ninja_install

# Win32
%files -n mingw32-qt6-%{qt_module}
%license LICENSES/*GPL*
%{mingw32_bindir}/Qt6Multimedia.dll
%{mingw32_bindir}/Qt6MultimediaWidgets.dll
%{mingw32_bindir}/Qt6SpatialAudio.dll
%{mingw32_includedir}/qt6/QtMultimedia/
%{mingw32_includedir}/qt6/QtMultimediaTestLib/
%{mingw32_includedir}/qt6/QtMultimediaWidgets/
%{mingw32_includedir}/qt6/QtSpatialAudio/
%{mingw32_libdir}/cmake/Qt6/FindFFmpeg.cmake
%{mingw32_libdir}/cmake/Qt6/FindPipeWire.cmake
%{mingw32_libdir}/cmake/Qt6/FindGObject.cmake
%{mingw32_libdir}/cmake/Qt6/FindGStreamer.cmake
%{mingw32_libdir}/cmake/Qt6/FindMMRendererCore.cmake
%{mingw32_libdir}/cmake/Qt6/FindVAAPI.cmake
%{mingw32_libdir}/cmake/Qt6/FindWrapBundledResonanceAudioConfigExtra.cmake
%{mingw32_libdir}/cmake/Qt6/FindWrapPulseAudio.cmake
%{mingw32_libdir}/cmake/Qt6/FindMMRenderer.cmake
%{mingw32_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtMultimediaTestsConfig.cmake
%{mingw32_libdir}/cmake/Qt6BundledResonanceAudio/
%{mingw32_libdir}/cmake/Qt6Multimedia/
%{mingw32_libdir}/cmake/Qt6MultimediaPrivate/
%{mingw32_libdir}/cmake/Qt6MultimediaTestLibPrivate/
%{mingw32_libdir}/cmake/Qt6MultimediaWidgets/
%{mingw32_libdir}/cmake/Qt6MultimediaWidgetsPrivate/
%{mingw32_libdir}/cmake/Qt6SpatialAudio/
%{mingw32_libdir}/cmake/Qt6SpatialAudioPrivate/
%{mingw32_libdir}/pkgconfig/Qt6Multimedia.pc
%{mingw32_libdir}/pkgconfig/Qt6MultimediaWidgets.pc
%{mingw32_libdir}/pkgconfig/Qt6SpatialAudio.pc
%{mingw32_libdir}/libQt6BundledResonanceAudio.a
%{mingw32_libdir}/libQt6Multimedia.dll.a
%{mingw32_libdir}/libQt6MultimediaTestLib.a
%{mingw32_libdir}/libQt6MultimediaWidgets.dll.a
%{mingw32_libdir}/libQt6SpatialAudio.dll.a
%{mingw32_libdir}/Qt6MultimediaWidgets.prl
%{mingw32_libdir}/Qt6Multimedia.prl
%{mingw32_libdir}/Qt6MultimediaTestLib.prl
%{mingw32_libdir}/Qt6SpatialAudio.prl
%dir %{mingw32_libdir}/qt6/plugins/multimedia/
%{mingw32_libdir}/qt6/plugins/multimedia/windowsmediaplugin.dll
%{mingw32_libdir}/qt6/mkspecs/features/ios/add_ios_ffmpeg_libraries.prf
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_multimedia.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_multimedia_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_multimediatestlibprivate_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_multimediawidgets.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_multimediawidgets_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_spatialaudio.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_spatialaudio_private.pri
%{mingw32_libdir}/qt6/metatypes/qt6multimedia_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6multimediatestlibprivate_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6multimediawidgets_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6spatialaudio_metatypes.json
%{mingw32_libdir}/qt6/modules/Multimedia.json
%{mingw32_libdir}/qt6/modules/MultimediaTestLibPrivate.json
%{mingw32_libdir}/qt6/modules/MultimediaWidgets.json
%{mingw32_libdir}/qt6/modules/SpatialAudio.json
%{mingw32_libdir}/qt6/sbom/%{qt_module}-%{qt_version}.spdx

# Win64
%files -n mingw64-qt6-%{qt_module}
%license LICENSES/*GPL*
%{mingw64_bindir}/Qt6Multimedia.dll
%{mingw64_bindir}/Qt6MultimediaWidgets.dll
%{mingw64_bindir}/Qt6SpatialAudio.dll
%{mingw64_includedir}/qt6/QtMultimedia/
%{mingw64_includedir}/qt6/QtMultimediaTestLib/
%{mingw64_includedir}/qt6/QtMultimediaWidgets/
%{mingw64_includedir}/qt6/QtSpatialAudio/
%{mingw64_libdir}/cmake/Qt6/FindFFmpeg.cmake
%{mingw64_libdir}/cmake/Qt6/FindPipeWire.cmake
%{mingw64_libdir}/cmake/Qt6/FindGObject.cmake
%{mingw64_libdir}/cmake/Qt6/FindGStreamer.cmake
%{mingw64_libdir}/cmake/Qt6/FindMMRendererCore.cmake
%{mingw64_libdir}/cmake/Qt6/FindVAAPI.cmake
%{mingw64_libdir}/cmake/Qt6/FindWrapBundledResonanceAudioConfigExtra.cmake
%{mingw64_libdir}/cmake/Qt6/FindWrapPulseAudio.cmake
%{mingw64_libdir}/cmake/Qt6/FindMMRenderer.cmake
%{mingw64_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtMultimediaTestsConfig.cmake
%{mingw64_libdir}/cmake/Qt6BundledResonanceAudio/
%{mingw64_libdir}/cmake/Qt6Multimedia/
%{mingw64_libdir}/cmake/Qt6MultimediaPrivate/
%{mingw64_libdir}/cmake/Qt6MultimediaTestLibPrivate/
%{mingw64_libdir}/cmake/Qt6MultimediaWidgets/
%{mingw64_libdir}/cmake/Qt6MultimediaWidgetsPrivate/
%{mingw64_libdir}/cmake/Qt6SpatialAudio/
%{mingw64_libdir}/cmake/Qt6SpatialAudioPrivate/
%{mingw64_libdir}/pkgconfig/Qt6Multimedia.pc
%{mingw64_libdir}/pkgconfig/Qt6MultimediaWidgets.pc
%{mingw64_libdir}/pkgconfig/Qt6SpatialAudio.pc
%{mingw64_libdir}/libQt6BundledResonanceAudio.a
%{mingw64_libdir}/libQt6Multimedia.dll.a
%{mingw64_libdir}/libQt6MultimediaTestLib.a
%{mingw64_libdir}/libQt6MultimediaWidgets.dll.a
%{mingw64_libdir}/libQt6SpatialAudio.dll.a
%{mingw64_libdir}/Qt6MultimediaWidgets.prl
%{mingw64_libdir}/Qt6Multimedia.prl
%{mingw64_libdir}/Qt6MultimediaTestLib.prl
%{mingw64_libdir}/Qt6SpatialAudio.prl
%dir %{mingw64_libdir}/qt6/plugins/multimedia/
%{mingw64_libdir}/qt6/plugins/multimedia/windowsmediaplugin.dll
%{mingw64_libdir}/qt6/mkspecs/features/ios/add_ios_ffmpeg_libraries.prf
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_multimedia.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_multimedia_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_multimediatestlibprivate_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_multimediawidgets.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_multimediawidgets_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_spatialaudio.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_spatialaudio_private.pri
%{mingw64_libdir}/qt6/metatypes/qt6multimedia_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6multimediatestlibprivate_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6multimediawidgets_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6spatialaudio_metatypes.json
%{mingw64_libdir}/qt6/modules/Multimedia.json
%{mingw64_libdir}/qt6/modules/MultimediaTestLibPrivate.json
%{mingw64_libdir}/qt6/modules/MultimediaWidgets.json
%{mingw64_libdir}/qt6/modules/SpatialAudio.json
%{mingw64_libdir}/qt6/sbom/%{qt_module}-%{qt_version}.spdx

%changelog
%autochangelog
