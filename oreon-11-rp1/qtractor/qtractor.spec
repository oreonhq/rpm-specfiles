%global source0_hash ad78e20f2b525dbf9a4996550124a4cc6beabe4c5a08576e05241651710a92ef
Name:           qtractor
Version:        1.6.4
Release:        1%{?dist}
Summary:        Audio/MIDI multi-track sequencer
License:        GPL-2.0-or-later
URL:            https://www.qtractor.org
Source0:        https://download.sourceforge.net/qtractor/qtractor-%{version}.tar.gz
Patch0:         0001-cmake-jack-libs.patch
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  ladspa-devel
BuildRequires:  libappstream-glib
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(aubio)
BuildRequires:  pkgconfig(dssi)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(lilv-0)
BuildRequires:  pkgconfig(lv2)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(rubberband)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisenc)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
Qtractor is an Audio/MIDI multi-track sequencer application written in C++ with
the Qt framework. Target platform is Linux, where the Jack Audio Connection Kit
(JACK) for audio, and the Advanced Linux Sound Architecture (ALSA) for MIDI, are
the main infrastructures to evolve as a fairly-featured Linux desktop audio
workstation GUI, specially dedicated to the personal home-studio.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCONFIG_XUNIQUE=ON \
    -DCONFIG_STACKTRACE=ON \
    -DCONFIG_WAYLAND=ON \
    -DCONFIG_QT6=ON \
    -DCONFIG_LIBJACK=ON \
    -DCONFIG_LIBASOUND=ON \
    -DCONFIG_LV2_UI_GTK2=OFF \
    -DCONFIG_LV2_UI_GTKMM2=OFF
%cmake_build
%install
%cmake_install
%find_lang %{name} --with-qt
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
