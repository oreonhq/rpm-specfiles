%global source0_hash ae2835b12081f7271a6b0b25d34b87d36b022c40370028ca4a10f90fcedfa661

%global pname   carla

Name:           Carla
Version:        2.5.10
Release:        3%{?dist}
Summary:        Audio plugin host

# The entire source code is GPLv2+ except
# - BSD
# source/modules/lilv/lilv-0.24.0/waf
# source/modules/lilv/serd-0.24.0/waf
# source/modules/lilv/sord-0.16.0/waf
# source/modules/lilv/sratom-0.6.0/waf
# source/modules/audio_decoder/ffcompat.h
# source/modules/rtaudio/include/soundcard.h
# - Boost
# source/modules/hylia/link/asio/*
# - ISC
# source/jackbridge/*
# source/modules/dgl/*
# source/modules/distrho/*
# source/modules/lilv/*
# source/modules/water/buffers/AudioSampleBuffer.h
# source/modules/water/containers
# source/modules/water/files/*
# source/modules/water/maths/*
# source/modules/water/memory/*
# source/modules/water/midi/*
# source/modules/water/misc/*
# source/modules/water/streams/OutputStream.h
# source/modules/water/synthesisers/*
# source/modules/water/text/*
# source/modules/water/threads/*
# source/modules/water/xml/*
# source/utils/CarlaJuceUtils.hpp
# - MIT/Expat
# source/modules/rtaudio/RtAudio.cpp
# source/modules/rtaudio/RtAudio.h
# source/modules/rtmidi/RtMidi.cpp
# source/modules/rtmidi/RtMidi.h
# source/modules/sfzero/LICENSE
# - zlib
# source/modules/dgl/src/nanovg/LICENSE.txt
# source/modules/dgl/src/nanovg/fontstash.h
# source/modules/dgl/src/nanovg/nanovg.c
# source/modules/dgl/src/nanovg/nanovg.h
# source/modules/dgl/src/nanovg/nanovg_gl.h
# source/modules/dgl/src/nanovg/nanovg_gl_utils.h

Epoch:   1
License:        GPL-2.0-or-later AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND ISC AND MIT AND Zlib
URL:            https://github.com/falkTX/Carla
Source0:        https://github.com/falkTX/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://github.com/falkTX/Carla/issues/1444
Patch0:         %{name}-libdir.patch
Patch1:         %{name}-single-libs-path.patch

BuildRequires:  gcc gcc-c++
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(mxml)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  python3-qt5-base
# BuildRequires:  python3-magic
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  desktop-file-utils
BuildRequires:  make
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
Requires:       python3-qt5
Requires:       python-pyliblo3
Requires:       hicolor-icon-theme
Requires:       shared-mime-info
Requires:       a2jmidid

# Dont provide or require internal libs. Using new rpm builtin filtering,
# see https://fedoraproject.org/wiki/Packaging:AutoProvidesAndRequiresFiltering#Private_Libraries
%global _privatelibs libjack[.]so.*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$

%description
Carla is a fully-featured audio plugin host, with support for many audio drivers
and plugin formats.
It's open source and licensed under the GNU General Public License, version 2 or
later.
Features

    LADSPA, DSSI, LV2 and VST plugin formats
    SF2/3 and SFZ sound banks
    Internal audio and midi file player
    Automation of plugin parameters via MIDI CC
    Remote control over OSC
    Rack and Patchbay processing modes, plus Single and Multi-Client if using
    JACK
    Native audio drivers (ALSA, DirectSound, CoreAudio, etc) and JACK

In experimental phase / work in progress:

    Export any Carla loadable plugin or sound bank as an LV2 plugin
    Plugin bridge support (such as running 32bit plugins on a 64bit Carla, or
    Windows plugins on Linux)
    Run JACK applications as audio plugins
    Transport controls, sync with JACK Transport or Ableton Link

Carla is also available as an LV2 plugin for MacOS and Linux, and VST plugin for
Linux.

%package        devel
Summary:        Header files to access Carla's API
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
This package contains header files needed when writing software using
Carla's several APIs.

%package        vst
Summary:        CarlaRack and CarlaPatchbay VST plugins
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    vst
This package contains Carla VST plugins, including CarlaPatchbayFX,
CarlaPatchbay, CarlaRackFX, and CarlaRack.

%package     -n lv2-%{pname}
Summary:        LV2 plugin
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description -n lv2-%{pname}
This package contains the Carla LV2 plugin.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

#%%autosetup -p0 -n %%{name}-%%{version}
%setup -qn %{name}-%{version}
%patch 0 -p1
%patch 1 -p1

# remove windows stuff
rm -rf data/{macos,windows}

# E: wrong-script-interpreter /usr/lib64/python3/dist-packages/carla_backend.py /usr/bin/env python3
find . -type f \( -name "*.py" \) -exec sed -i "s|#!/usr/bin/env python3|#!%{__python3}|g" {} \;
sed -i "s|#!/usr/bin/env python3|#!%{__python3}|" source/frontend/{carla,carla-control,carla-jack-multi,carla-jack-single,carla-patchbay,carla-rack}
sed -i "s|#!/usr/bin/env python|#!%{__python3}|" source/frontend/widgets/paramspinbox.py

# fix libdir path
sed -i "s|/lib/carla|/%{_lib}/carla|" data/{carla,carla-control,carla-database,carla-jack-multi,carla-jack-single,carla-patchbay,carla-rack,carla-settings}

# Fix metainfo install dir
sed -i -e 's|$(DESTDIR)$(PREFIX)/share/appdata/studio.kx.carla.appdata.xml|$(DESTDIR)$(PREFIX)/share/metainfo/studio.kx.carla.appdata.xml|g' Makefile
sed -i -e 's|$(DESTDIR)$(PREFIX)/share/appdata|$(DESTDIR)$(PREFIX)/share/metainfo|g' Makefile

%build
%{set_build_flags}
# list build configuration, no need for optflags or -j
make features
%make_build SKIP_STRIPPING=true NOOPT=true V=1

%install 
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}

# Create a vst directory
install -m 755 -d %{buildroot}/%{_libdir}/vst/

# E: non-executable-script /usr/share/carla/paramspinbox.py 644 /usr/bin/env python
find %{buildroot} -type f \( -name "*.py" \) -exec chmod a+x {} \;

# E: non-executable-script /usr/share/carla/carla 644 /usr/bin/python3
chmod a+x %{buildroot}%{_datadir}/%{pname}/{carla,carla-control,carla-jack-multi,carla-jack-single,carla-patchbay,carla-rack}

# fix perm due rpmlint W: unstripped-binary-or-object /usr/lib64/carla/libcarla_interposer-jack-x11.so
find %{buildroot}%{_libdir} -name '*.so' -exec chmod +x '{}' ';'

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/studio.kx.carla.appdata.xml

%files
%doc README.md
%license doc/GPL.txt doc/LGPL.txt
%{_bindir}/%{pname}
%{_bindir}/%{pname}-control
%{_bindir}/%{pname}-database
%{_bindir}/%{pname}-jack-multi
%{_bindir}/%{pname}-jack-single
%{_bindir}/%{pname}-patchbay
%{_bindir}/%{pname}-rack
%{_bindir}/%{pname}-settings
%{_bindir}/%{pname}-single
%{_bindir}/%{pname}-jack-patchbayplugin
%{_bindir}/%{pname}-osc-gui
%{_libdir}/%{pname}/
%{_datadir}/applications/%{pname}-control.desktop
%{_datadir}/applications/%{pname}.desktop
%{_datadir}/applications/%{pname}-jack-multi.desktop
%{_datadir}/applications/%{pname}-jack-single.desktop
%{_datadir}/applications/%{pname}-patchbay.desktop
%{_datadir}/applications/%{pname}-rack.desktop
%{_datadir}/%{pname}/
%{_datadir}/icons/hicolor/*/apps/%{pname}*.png
%{_datadir}/icons/hicolor/*/apps/%{pname}*.svg
%{_datadir}/mime/packages/%{pname}.xml
%{_datadir}/metainfo/studio.kx.carla.appdata.xml

%files vst
%{_libdir}/vst/

%files -n lv2-%{pname}
%dir %{_libdir}/lv2
%{_libdir}/lv2/carla.lv2/

%files devel
%{_includedir}/%{pname}/
%{_libdir}/pkgconfig/%{pname}-standalone.pc
%{_libdir}/pkgconfig/%{pname}-utils.pc
%{_libdir}/pkgconfig/%{pname}-native-plugin.pc
%{_libdir}/pkgconfig/%{pname}-host-plugin.pc

%changelog
%autochangelog
