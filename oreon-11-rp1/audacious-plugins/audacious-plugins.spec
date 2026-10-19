%global source0_hash 22e58a8a2c3f3caa9687434353618c822963cc8846cd239de36d4e8e5bd166a6
%bcond_without gtk
%bcond_without meson
%global aud_plugin_api %(grep '[ ]*#define[ ]*_AUD_PLUGIN_VERSION[ ]\\+' %{_includedir}/libaudcore/plugin.h 2>/dev/null | sed 's!.*_AUD_PLUGIN_VERSION[ ]*\\([0-9]\\+\\).*!\\1!')
%if 0%{aud_plugin_api} > 0
%global aud_plugin_dep Requires: audacious(plugin-api)%{?_isa} = %{aud_plugin_api}
%endif
%{?aud_plugin_dep}
Name: audacious-plugins
Version: 4.6.1
Release:        1%{?dist}
%global tar_ver %{version}
%global aud_ver 4.6
Requires: audacious%{?_isa} >= %{aud_ver}
Summary:        Plugins for the Audacious audio player
URL: https://audacious-media-player.org/
License: GPL-2.0-or-later AND LGPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND MIT AND BSD-2-Clause-pkgconf-disclaimer AND LicenseRef-Fedora-Public-Domain
Source0:        https://distfiles.audacious-media-player.org/%{name}-%{version}.tar.bz2
Source3: README.licenses
Source100: audacious-plugins-amidi.metainfo.xml
Source101: audacious-plugins-exotic.metainfo.xml
Source102: audacious-plugins-jack.metainfo.xml
Patch0: audacious-plugins-3.7-alpha1-xmms-skindir.patch
Patch2: audacious-plugins-3.6-ladspa.patch
Obsoletes: audacious-plugins-freeworld < 4.4.2-4
Provides:  audacious-plugins-freeworld = %{version}-%{release}
Obsoletes: audacious-plugins-freeworld-aac < 4.4.2-4
Provides:  audacious-plugins-freeworld-aac = %{version}-%{release}
Obsoletes: audacious-plugins-ffaudio < 4.6.1-3
Provides:  audacious-plugins-ffaudio = %{version}-%{release}
%filter_provides_in %{_libdir}/audacious/
%filter_setup
# oreon:deps
BuildRequires:  audacious-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  lame-devel
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Multimedia)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(adplug)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(ampache_browser_1)
BuildRequires:  pkgconfig(faad2)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libbinio)
BuildRequires:  pkgconfig(libbs2b)
BuildRequires:  pkgconfig(libcddb)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libcdio_cdda)
BuildRequires:  pkgconfig(libcue)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libmms)
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libopenmpt)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsidplayfp)
BuildRequires:  pkgconfig(libspa-0.2)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(lirc)
BuildRequires:  pkgconfig(neon)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sdl3)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(soxr)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisenc)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(wavpack)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb-proto)
# /oreon:deps
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
License: GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND GPL-3.0-only AND MIT AND BSD-2-Clause-pkgconf-disclaimer
%{?aud_plugin_dep}
Requires: audacious-plugins%{?_isa} >= %{aud_ver}
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

%{!?aud_plugin_dep:echo 'No audacious(plugin-api) dependency!' && exit -1}
%if %{with meson}
%meson \
    -Dsndio=false \
    -Dfilewriter-mp3=true \
    -Dstreamtuner=true \
    -Dffaudio=false \
    -Dgtk=%{?with_gtk:true}%{!?with_gtk:false} \
    -Dqt5=true
%meson_build
%else
%configure  \
    --enable-filewriter-mp3 \
    --enable-streamtuner \
    --disable-sndio \
    --disable-ffaudio \
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
%oreon_autofiles audacious-plugins-jack usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles audacious-plugins-exotic usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles audacious-plugins-amidi usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n audacious-plugins-jack -f %{oreon_filedir}/audacious-plugins-jack.list
%files -n audacious-plugins-exotic -f %{oreon_filedir}/audacious-plugins-exotic.list
%files -n audacious-plugins-amidi -f %{oreon_filedir}/audacious-plugins-amidi.list

%changelog

%autochangelog
