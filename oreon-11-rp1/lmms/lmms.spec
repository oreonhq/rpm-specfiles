%global source0_hash none
%ifarch %ix86
%bcond_with  wine
%else
%bcond_with  wine
%endif
Name:           lmms
Version:        1.2.2
Release:        1%{?dist}
Summary:        Linux MultiMedia Studio
URL:            https://lmms.io/
License:        GPLv2+ and GPLv2 and (GPLv2+ or MIT) and GPLv3+ and MIT and LGPLv2+ and (LGPLv2+ with exceptions) and Copyright only
Source0:        lmms_%{version}.stripped.tar.xz
Source1:        README.fedora
Source2:        lmms.metainfo.xml
Patch0:         lmms-1.2.2_winelib.patch
Patch1:         lmms-1.2.2_lib_suffix.patch
Patch2:         lmms-1.2.2_carla_2.4.3.patch
Requires:  shared-mime-info
Requires:  hicolor-icon-theme
%if %{with wine}
%endif
Requires:       ladspa-caps-plugins
Requires:       ladspa-tap-plugins
Requires:       ladspa-calf-plugins
%if %{with wine}
Requires:       %{name}-vst = %{version}-%{release}
%endif
%global __provides_exclude_from ^%{_libdir}/lmms/.*$
%global __requires_exclude ^libvstbase\\.so.*$|^libZynAddSubFxCore\\.so.*$|^libcarlabase\\.so.*$|^libcarla_native-plugin\\.so.*$
# oreon:deps
BuildRequires:  Carla-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  bash-completion
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fftw3-devel
BuildRequires:  fltk-devel
BuildRequires:  fltk-fluid
BuildRequires:  fluidsynth-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  ladspa-devel
BuildRequires:  libappstream-glib
BuildRequires:  libogg-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libvorbis-devel
BuildRequires:  make
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  qt5-qt3d-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  stk-devel
BuildRequires:  xcb-util-devel
BuildRequires:  xcb-util-keysyms-devel
# /oreon:deps
%description
LMMS aims to be a free alternative to popular (but commercial and
closed- source) programs like FruityLoops/FL Studio, Cubase and Logic
allowing you to produce music with your computer. This includes
creation of loops, synthesizing and mixing sounds, arranging samples,
having fun with your MIDI-keyboard and much more...

LMMS combines the features of a tracker-/sequencer-program and those
of powerful synthesizers, samplers, effects etc. in a modern,
user-friendly and easy to use graphical user-interface.

Features

 * Song-Editor for arranging the song
 * creating beats and basslines using the Beat-/Bassline-Editor
 * easy-to-use piano-roll for editing patterns and melodies
 * instrument- and effect-plugins
 * support for hosting VST(i)- and LADSPA-plugins (instruments/effects)
 * automation-editor
 * MIDI-support

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description devel
The %{name}-devel package contains header files for
developing addons for %{name}.

%prep

%autosetup -p1 -n %{name}

# remove spurious x-bits
find . -type f -exec chmod 0644 {} \;

cp -a %{SOURCE1} README.fedora

%build

%cmake \
       -DWANT_SDL:BOOL=OFF \
       -DWANT_PORTAUDIO:BOOL=OFF \
       -DWANT_CAPS:BOOL=OFF \
       -DWANT_TAP:BOOL=OFF \
       -DWANT_CALF:BOOL=OFF \
       -DWINE_CXX_FLAGS:STRING="-fno-lto" \
       -DWANT_QT5:BOOL=ON \
%ifarch %ix86 x86_64
       -DWANT_VST:BOOL=ON \
%else
       -DWANT_VST:BOOL=OFF \
%endif
%ifarch x86_64
       -DWANT_VST_NOWINE:BOOL=ON \
       -DREMOTE_VST_PLUGIN_FILEPATH="../../lib/lmms/RemoteVstPlugin" \
%endif
       -DCMAKE_INSTALL_LIBDIR=%{_lib} \
       -Wno-dev
%cmake_build
%install
%cmake_install
rm -f %{buildroot}%{_libdir}/libqx11embedcontainer.a
desktop-file-install --vendor '' \
        --add-category=Midi \
        --add-category=Sequencer \
        --add-category=X-Jack \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop
install -D -m 0644 -p %{SOURCE2} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%package vst
Summary:        VST hosting plugin for %{name}
%description vst
This package contains the necessary files to host VST plugins.

%files -f %{oreon_filedir}/main.list
%files -n lmms-devel -f %{oreon_filedir}/lmms-devel.list

%changelog

%autochangelog
