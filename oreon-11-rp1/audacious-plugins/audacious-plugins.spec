%global source0_hash f4feedc32776acfa9d24701d3b794fc97822f76da6991e91e627e70e561fdd3b

# 'without' = build with Gtk+ by default
%bcond_without gtk

%bcond_without meson

%global aud_plugin_api %(grep '[ ]*#define[ ]*_AUD_PLUGIN_VERSION[ ]\\+' %{_includedir}/libaudcore/plugin.h 2>/dev/null | sed 's!.*_AUD_PLUGIN_VERSION[ ]*\\([0-9]\\+\\).*!\\1!')
%if 0%{aud_plugin_api} > 0
%global aud_plugin_dep Requires: audacious(plugin-api)%{?_isa} = %{aud_plugin_api}
%endif
%{?aud_plugin_dep}

Name: audacious-plugins
Version: 4.5.1
Release: 5%{?dist}

%global tar_ver %{version}

# Minimum audacious/audacious-plugins version in inter-package dependencies.
%global aud_ver 4.5
Requires: audacious%{?_isa} >= %{aud_ver}

Summary: Plugins for the Audacious audio player
URL: https://audacious-media-player.org/

# list of license per plugin in README.licences
License: GPL-2.0-or-later AND LGPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND MIT AND BSD-2-Clause-pkgconf-disclaimer AND LicenseRef-Fedora-Public-Domain

Source0: https://distfiles.audacious-media-player.org/%{name}-%{tar_ver}.tar.bz2
Source3: README.licenses
# for optional packages
Source100: audacious-plugins-amidi.metainfo.xml
Source101: audacious-plugins-exotic.metainfo.xml
Source102: audacious-plugins-jack.metainfo.xml

# Fedora customization
Patch0: audacious-plugins-3.7-alpha1-xmms-skindir.patch
# Fedora customization: add default system-wide module_path
Patch2: audacious-plugins-3.6-ladspa.patch

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: meson
BuildRequires: audacious-devel >= %{aud_ver}
BuildRequires: gettext-devel
BuildRequires: pkgconfig(neon)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(samplerate)
BuildRequires: pkgconfig(soxr)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(wavpack)
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires: pkgconfig(libsidplayfp) >= 2.0
%endif
BuildRequires: pkgconfig(libmodplug)
BuildRequires: pkgconfig(ogg) pkgconfig(vorbis) pkgconfig(vorbisenc) pkgconfig(vorbisfile)
BuildRequires: pkgconfig(faad2)
BuildRequires: pkgconfig(flac)
BuildRequires: pkgconfig(fluidsynth)
BuildRequires: pkgconfig(libcdio) pkgconfig(libcdio_cdda) pkgconfig(libcddb)
BuildRequires: pkgconfig(libcue)
BuildRequires: pkgconfig(sdl3) => 3.2.0
BuildRequires: pkgconfig(lirc)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libnotify) pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(libbs2b)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(adplug)
BuildRequires: pkgconfig(libbinio)
BuildRequires: pkgconfig(libopenmpt)
BuildRequires: pkgconfig(libmms)
BuildRequires: pkgconfig(libmpg123)
BuildRequires: lame-devel
BuildRequires: pkgconfig(opus) pkgconfig(opusfile)
BuildRequires: pkgconfig(json-glib-1.0) >= 1.0
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires: pkgconfig(libpipewire-0.3) >= 0.3.33
BuildRequires: pkgconfig(libspa-0.2)
# ffaudio / ffmpeg
BuildRequires: pkgconfig(libavcodec) >= 56.60.100
BuildRequires: pkgconfig(libavformat) >= 56.40.101
BuildRequires: pkgconfig(libavutil) >= 54.31.100
%endif

# for hotkey plugin / provided by gtk3-devel
BuildRequires: pkgconfig(gdk-x11-3.0)

%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(Qt6Multimedia)
BuildRequires: pkgconfig(Qt6Network)
BuildRequires: pkgconfig(Qt6Svg)
#BuildRequires: pkgconfig(Qt6X11Extras)
BuildRequires: pkgconfig(x11) pkgconfig(xcb-proto)
%else
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Multimedia)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5X11Extras)
%endif
# plugin is Qt based
BuildRequires: pkgconfig(ampache_browser_1)

# added 2025-07-17
Obsoletes: audacious-plugins-freeworld < 4.4.2-4
Provides:  audacious-plugins-freeworld = %{version}-%{release}
# added 2025-06-13
Obsoletes: audacious-plugins-freeworld-aac < 4.4.2-4
Provides:  audacious-plugins-freeworld-aac = %{version}-%{release}
# added 2025-12-20
Obsoletes: audacious-plugins-ffaudio < 4.5.1-3
Provides:  audacious-plugins-ffaudio = %{version}-%{release}

# plugin .so files
%if 0%{?fedora} > 29 || 0%{?rhel} > 8
%global __provides_exclude_from ^%{_libdir}/audacious/.*\\.so$
%else
%filter_provides_in %{_libdir}/audacious/
%filter_setup
%endif

%description
This package provides essential plugins for the Audacious audio player.

%package jack
Summary: Audacious output plugin for Jack Audio Connection Kit
License: BSD-2-Clause-pkgconf-disclaimer
%{?aud_plugin_dep}
Requires: audacious-plugins%{?_isa} >= %{aud_ver}

%description jack
This package provides an Audacious output plugin that uses the
Jack Audio Connection Kit (JACK) sound service.

%package exotic
Summary: Optional niche market plugins for Audacious 
# list of license per plugin in README.licences
License: GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND GPL-3.0-only AND MIT AND BSD-2-Clause-pkgconf-disclaimer
%{?aud_plugin_dep}
Requires: audacious-plugins%{?_isa} >= %{aud_ver}
# src/console/ for console.so input plugin in -exotic subpackage
Provides: bundled(game-music-emu) = 0.5.5

%description exotic
This package provides optional plugins for Audacious, which do not aim
at a wide demographic audience. Most users of Audacious do not need this.

For example, included are input plugins for exotic audio file formats,
SID music (from Commodore 64 and compatibles), AdLib/OPL2 emulation,
console game music, the Portable Sound Format PSF1/PSF2, Vortex AM/YM
emulation, Nintendo DS Sound Format 2SF.

%package amidi
Summary: Audacious input plugin for MIDI
License: GPL-2.0-or-later

%{?aud_plugin_dep}
Requires: audacious-plugins%{?_isa} >= %{aud_ver}

%description amidi
This package provides AMIDI-Plug, a modular MIDI music player, as an
input plugin for Audacious.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{tar_ver} -p1

for i in src/ladspa/plugin.cc
do
    sed -i -e 's!__RPM_LIBDIR__!%{_libdir}!g' $i
    sed -i -e 's!__RPM_LIB__!%{_lib}!g' $i
done
grep -q -s __RPM_LIB * -R && exit 1 || echo

%if %{without meson}
sed -i '\,^.SILENT:,d' buildsys.mk.in
sed -i 's!MAKE} -s!MAKE} !' buildsys.mk.in
%endif

%build
# Enforce availability of the audacious(plugin-api) dependency.
%{!?aud_plugin_dep:echo 'No audacious(plugin-api) dependency!' && exit -1}

# temporarily was required to make Qt's MOC accessible
#rm -rf _bin
#mkdir _bin
#ln -s /usr/bin/moc-qt5 _bin/moc
#ln -s /usr/bin/uic-qt5 _bin/uic
#export PATH=$PATH:$(pwd)/_bin

# not defining true/false for all plugins here, since for the RPM
# package build, all wanted plugins are specified in the %%files section,
# and the package build would fail for any missing files
%if %{with meson}
%meson \
    -Dsndio=false \
    -Dfilewriter-mp3=true \
    -Dstreamtuner=true \
%if 0%{?fedora} || 0%{?rhel} >= 9
    -Dffaudio=true \
%else
    -Dffaudio=false \
%endif
    -Dgtk=%{?with_gtk:true}%{!?with_gtk:false} \
%if 0%{?fedora} || 0%{?rhel} >= 9
    -Dqt=true
%else
    -Dqt5=true
%endif
%meson_build
%else
%configure  \
    --enable-filewriter-mp3 \
    --enable-streamtuner \
    --disable-sndio \
%if 0%{?fedora} || 0%{?rhel} >= 9
    --enable-ffaudio \
%else
    --disable-ffaudio \
%endif
    %{?with_gtk:--enable-gtk} \
    %{!?with_gtk:--disable-gtk} \
    --disable-rpath
%make_build
%endif

%install
%if %{with meson}
%meson_install
%else
%make_install INSTALL="install -p"
%endif
%find_lang %{name}

mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/appdata
install -p -m0644 %{SOURCE100} ${RPM_BUILD_ROOT}%{_datadir}/appdata
install -p -m0644 %{SOURCE101} ${RPM_BUILD_ROOT}%{_datadir}/appdata
install -p -m0644 %{SOURCE102} ${RPM_BUILD_ROOT}%{_datadir}/appdata

%files -f %{name}.lang
%license COPYING
%dir %{_libdir}/audacious
%dir %{_libdir}/audacious/Container/
%{_libdir}/audacious/Container/asx.so
%{_libdir}/audacious/Container/asx3.so
%{_libdir}/audacious/Container/audpl.so
%{_libdir}/audacious/Container/cue.so
%{_libdir}/audacious/Container/m3u.so
%{_libdir}/audacious/Container/pls.so
%{_libdir}/audacious/Container/xspf.so
%dir %{_libdir}/audacious/Effect/
%{_libdir}/audacious/Effect/background_music.so
%{_libdir}/audacious/Effect/bitcrusher.so
%{_libdir}/audacious/Effect/bs2b.so
%{_libdir}/audacious/Effect/compressor.so
%{_libdir}/audacious/Effect/crossfade.so
%{_libdir}/audacious/Effect/crystalizer.so
%{_libdir}/audacious/Effect/echo.so
%{_libdir}/audacious/Effect/mixer.so
%{_libdir}/audacious/Effect/resample.so
%{_libdir}/audacious/Effect/silence-removal.so
%{_libdir}/audacious/Effect/sox-resampler.so
%{_libdir}/audacious/Effect/speed-pitch.so
%{_libdir}/audacious/Effect/stereo.so
%{_libdir}/audacious/Effect/voice_removal.so
%dir %{_libdir}/audacious/General/
%{_libdir}/audacious/General/albumart-qt.so
%{_libdir}/audacious/General/ampache.so
%{_libdir}/audacious/General/playback-history-qt.so
%{_libdir}/audacious/General/playlist-manager-qt.so
%{_libdir}/audacious/General/qtui.so
%{_libdir}/audacious/General/search-tool-qt.so
%{_libdir}/audacious/General/skins-qt.so
%{_libdir}/audacious/General/song-info-qt.so
%{_libdir}/audacious/General/statusicon-qt.so
%{_libdir}/audacious/General/cd-menu-items.so
%{_libdir}/audacious/General/delete-files.so
%{_libdir}/audacious/General/lirc.so
%{_libdir}/audacious/General/lyrics-qt.so
%{_libdir}/audacious/General/mpris2.so
%{_libdir}/audacious/General/notify.so
%{_libdir}/audacious/General/scrobbler.so
%{_libdir}/audacious/General/song_change.so
%{_libdir}/audacious/General/streamtuner.so
%{_libdir}/audacious/General/qthotkey.so
%dir %{_libdir}/audacious/Input/
%{_libdir}/audacious/Input/aac-raw.so
%{_libdir}/audacious/Input/cdaudio-ng.so
%{_libdir}/audacious/Input/ffaudio.so
%{_libdir}/audacious/Input/flacng.so
%{_libdir}/audacious/Input/metronom.so
%{_libdir}/audacious/Input/modplug.so
%{_libdir}/audacious/Input/openmpt.so
%{_libdir}/audacious/Input/opus.so
%{_libdir}/audacious/Input/sndfile.so
%{_libdir}/audacious/Input/tonegen.so
%{_libdir}/audacious/Input/vorbis.so
%{_libdir}/audacious/Input/wavpack.so
# name is misleading as it's based on libmpg123 not libmad
%{_libdir}/audacious/Input/madplug.so
%dir %{_libdir}/audacious/Output/
%{_libdir}/audacious/Output/alsa.so
%{_libdir}/audacious/Output/filewriter.so
%{_libdir}/audacious/Output/oss4.so
%if 0%{?fedora} || 0%{?rhel} >= 9
%{_libdir}/audacious/Output/pipewire.so
%endif
%{_libdir}/audacious/Output/pulse_audio.so
%{_libdir}/audacious/Output/qtaudio.so
%{_libdir}/audacious/Output/sdlout.so
%dir %{_libdir}/audacious/Visualization/
%{_libdir}/audacious/Visualization/blur_scope-qt.so
%{_libdir}/audacious/Visualization/gl-spectrum-qt.so
%{_libdir}/audacious/Visualization/qt-spectrum.so
%{_libdir}/audacious/Visualization/vumeter-qt.so
%{_libdir}/audacious/Visualization/vumeter.so
%dir %{_libdir}/audacious/Transport/
%{_libdir}/audacious/Transport/gio.so
%{_libdir}/audacious/Transport/mms.so
%{_libdir}/audacious/Transport/neon.so

# optional Gtk+ plugins
%if %{with gtk}
%{_libdir}/audacious/General/albumart.so
%{_libdir}/audacious/General/aosd.so
%{_libdir}/audacious/General/gtkui.so
%{_libdir}/audacious/General/hotkey.so
%{_libdir}/audacious/General/lyrics-gtk.so
%{_libdir}/audacious/General/playlist-manager.so
%{_libdir}/audacious/General/search-tool.so
%{_libdir}/audacious/General/skins.so
%{_libdir}/audacious/General/statusicon.so
%{_libdir}/audacious/Effect/ladspa.so
%{_libdir}/audacious/Visualization/blur_scope.so
%{_libdir}/audacious/Visualization/cairo-spectrum.so
%{_libdir}/audacious/Visualization/gl-spectrum.so
%endif

%{_datadir}/audacious/

%files jack
%{_libdir}/audacious/Output/jack-ng.so
%{_datadir}/appdata/%{name}-jack.metainfo.xml

%files exotic
%{_libdir}/audacious/Input/adplug.so
%{_libdir}/audacious/Input/console.so
%{_libdir}/audacious/Input/psf2.so
%if 0%{?fedora} || 0%{?rhel} >= 9
%{_libdir}/audacious/Input/sid.so
%endif
%{_libdir}/audacious/Input/vtx.so
%{_libdir}/audacious/Input/xsf.so
%{_datadir}/appdata/%{name}-exotic.metainfo.xml

%files amidi
%{_libdir}/audacious/Input/amidi-plug.so
#%%{_libdir}/audacious/Input/amidi-plug/
%{_datadir}/appdata/%{name}-amidi.metainfo.xml

%changelog
%autochangelog
