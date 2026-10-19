%global stable_kf6 stable
%global source0_hash 70cab22a089aa976627fb0f04ea2bf2e918a138c36ff0337d4a7709ea5462fa3
%ifnarch s390x
%bcond onnxruntime 1
%endif
%global appid org.kde.CrowTranslate
Name: crow-translate
Version: 4.1.0
Release:        1%{?dist}
Summary:        Application that allows you to translate and speak text
License: GPL-3.0-only AND GPL-3.0-or-later AND BSD-3-Clause AND MIT
URL: https://apps.kde.org/crowtranslate/
Source0:        https://download.kde.org/%{stable_kf6}/%{name}/%{version}/%{name}-%{version}.tar.gz
ExcludeArch: %{ix86}
%if %{with onnxruntime}
%endif
Requires: hicolor-icon-theme
Requires: qt6-qttools
Recommends: gstreamer-plugins-good
%if %{with onnxruntime}
Provides: bundled(espeak-ng)
%endif
Provides: bundled(qonlinetranslator)
Provides: bundled(qhotkey)
Provides: bundled(qtaskbarcontrol)
Provides: bundled(singleapplication)
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KWayland)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6StateMachine)
BuildRequires:  cmake(Qt6TextToSpeech)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(leptonica)
BuildRequires:  cmake(tesseract)
BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(libonnxruntime)
# /oreon:deps
%description
Application written in C++ / Qt6 that allows you to translate and speak text
using Mozhi with multiple TTS providers including high-quality neural
text-to-speech.

%prep

%autosetup -N -n %{name}
dos2unix cmake/*.cmake src/*.cpp
%autopatch -p1
# Unbundle
#   * Used only on Windows
rm -r src/qgittag

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%{cmake_kf6} \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    %{!?with_onnxruntime:-DWITH_PIPER_TTS:BOOL=OFF}
%cmake_build
%install
%cmake_install
%find_lang %{name} --with-qt
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{appid}.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{appid}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
