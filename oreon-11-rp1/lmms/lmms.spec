%global source0_hash none

%ifarch %ix86
%bcond_with  wine
%else
%bcond_with  wine
%endif

Name:           lmms
Version:        1.2.2
Release:        20%{?dist}
Summary:        Linux MultiMedia Studio
URL:            https://lmms.io/

# - lmms itself is GPLv2+
# - third party code used by plugins:
#   - drumsynth files: GPLv2+ or MIT
#   - for ladspa-effects (note that we only include cmt and swh in the
#     binary rpm (see below):
#     - caps: GPLv2
#     - cmt: GPLv2(+?)
#     - swh: GPLv2+
#     - tap: GPLv2+
#     - calf: GPLv2+ and LGPLv2+
#   - Portsmf (midi_import plugin): MIT
#   - Blip_Buffer and Gb_Snd_Emu (papu plugin): LGPLv2.1+
#   - reSID (sid plugin): GPLv2+
#   - basename.c (vst_base): Copyright only
#   - embedded zynaddsubfx plugin: GPLv2+
#     - fltk (zynaddsubfx): LGPLv2+, with exceptions (but we use
#       system's fltk)
License:        GPLv2+ and GPLv2 and (GPLv2+ or MIT) and GPLv3+ and MIT and LGPLv2+ and (LGPLv2+ with exceptions) and Copyright only

# original tarfile can be found here:
# https://github.com/LMMS/lmms/releases/download/v%%{version}/lmms_%%{version}.tar.xz
Source0:        lmms_%{version}.stripped.tar.xz

# we strip all .ogg / .wav / .mmp(z) files from the tarfile,
# until their license situation becomes clearer.
Source1:        README.fedora

# see #1575262
Source2:        lmms.metainfo.xml

# Fix for finding libwine
Patch0:         lmms-1.2.2_winelib.patch

# Pass LIB_SUFFIX
Patch1:         lmms-1.2.2_lib_suffix.patch

# Fix building against Carla 2.4.3, see #6395
Patch2:         lmms-1.2.2_carla_2.4.3.patch

# according to upstream we should at least support oss, alsa, and
# jack. output via pulseaudio has high latency, but we enable it
# nevertheless as it is standard on fedora now. portaudio support is
# beta (and causes crashes), sdl is rarely used (?).
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel
BuildRequires:  fftw3-devel
BuildRequires:  fluidsynth-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libogg-devel
BuildRequires:  ladspa-devel
BuildRequires:  stk-devel
BuildRequires:  qt5-qt3d-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  xcb-util-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  fltk-devel
BuildRequires:  fltk-fluid
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  bash-completion
BuildRequires:  Carla-devel
BuildRequires:  libappstream-glib
# require packages owning directories we use
Requires:  shared-mime-info
Requires:  hicolor-icon-theme

%if %{with wine}
BuildRequires:  wine-devel 
%endif

Requires:       ladspa-caps-plugins
Requires:       ladspa-tap-plugins
# this has been retired:
#Requires: ladspa-swh-plugins
Requires:       ladspa-calf-plugins
# the version included in lmms contains patches sent to, but not yet
# applied by cmt's upstream.
#Requires: ladspa-cmt-plugins

# the -vst subpackage can only be built on ix86, but is also usable
# (and thus should be installed) on x86_64.
#ifarch #ix86 x86_64
%if %{with wine}
Requires:       %{name}-vst = %{version}-%{release}
%endif

%global __provides_exclude_from ^%{_libdir}/lmms/.*$
%global __requires_exclude ^libvstbase\\.so.*$|^libZynAddSubFxCore\\.so.*$|^libcarlabase\\.so.*$|^libcarla_native-plugin\\.so.*$

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

# remove unneeded file
rm -f %{buildroot}%{_libdir}/libqx11embedcontainer.a

desktop-file-install --vendor '' \
        --add-category=Midi \
        --add-category=Sequencer \
        --add-category=X-Jack \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

install -D -m 0644 -p %{SOURCE2} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files
%doc README.md README.fedora
%doc doc/AUTHORS doc/CONTRIBUTORS
%license LICENSE.txt
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.{png,svg}
%{_datadir}/icons/hicolor/*/mimetypes/application-x-%{name}-project.{png,svg}
%{_metainfodir}/%{name}.metainfo.xml
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}
%{_mandir}/man*/%{name}*

%files devel
%{_includedir}/%{name}

%if %{with wine}

%package vst
Summary:        VST hosting plugin for %{name}

%description vst
This package contains the necessary files to host VST plugins.

%files vst
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/RemoteVstPlugin*

%endif

%changelog
%autochangelog
