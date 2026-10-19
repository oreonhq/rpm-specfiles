%global source0_hash 16e2c984b563e4be457830b35375f8cd37d25f7168e5a60a7f0024d86875de6c
Name:           easyeffects
Version:        8.3.0
Release:        1%{?dist}
Summary:        Audio effects for PipeWire applications
License:        GPL-3.0-or-later
Url:            https://github.com/wwmm/easyeffects
Source0:        https://github.com/wwmm/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Provides:       pulseeffects = 6.1.1-1
Obsoletes:      pulseeffects < 6.1.1-1
Requires:       breeze-icon-theme
Requires:       kf6-qqc2-desktop-style%{?_isa}
Recommends:     plasma-breeze%{?_isa}
Requires:       qt6qml(org.kde.kirigami)
Requires:       qt6qml(org.kde.kirigamiaddons.components)
Requires:       qt6qml(QtGraphs)
Requires:       qt6qml(QtWebEngine)
Requires:       hicolor-icon-theme
Requires:       dbus-common
Recommends:     lv2-calf-plugins
Recommends:     lv2-mdala-plugins
Recommends:     lsp-plugins-lv2
Recommends:     lv2-zam-plugins
ExclusiveArch:  %{qt6_qtwebengine_arches}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6QQC2DesktopStyle)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Graphs)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6WebEngineQuick)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(TBB)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  itstool
BuildRequires:  ladspa-devel
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(libbs2b)
BuildRequires:  pkgconfig(libebur128)
BuildRequires:  pkgconfig(libmysofa)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(libportal-qt6)
BuildRequires:  pkgconfig(lilv-0)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(rnnoise)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(soundtouch)
BuildRequires:  pkgconfig(speexdsp)
BuildRequires:  pkgconfig(webrtc-audio-processing-2)
BuildRequires:  qt6qml(org.kde.kirigami)
BuildRequires:  zita-convolver-devel
# /oreon:deps
%description
Limiters, compressor, reverberation, high-pass filter, low pass filter,
equalizer many more effects for PipeWire applications.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%conf
%cmake

%build

%cmake_build
%install
%cmake_install
%find_lang %{name}
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/com.github.wwmm.%{name}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
