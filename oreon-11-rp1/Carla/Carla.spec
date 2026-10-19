%global source0_hash ae2835b12081f7271a6b0b25d34b87d36b022c40370028ca4a10f90fcedfa661
%global pname   carla
Name:           Carla
Version:        2.5.10
Release:        3%{?dist}
Summary:        Audio plugin host
Epoch:   1
License:        GPL-2.0-or-later AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND ISC AND MIT AND Zlib
URL:            https://github.com/falkTX/Carla
Source0:        https://github.com/falkTX/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         %{name}-libdir.patch
Patch1:         %{name}-single-libs-path.patch
Requires:       python3-qt5
Requires:       python-pyliblo3
Requires:       hicolor-icon-theme
Requires:       shared-mime-info
Requires:       a2jmidid
%global _privatelibs libjack[.]so.*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(mxml)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-qt5-base
# /oreon:deps
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
make features
%make_build SKIP_STRIPPING=true NOOPT=true V=1
%install 
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}
install -m 755 -d %{buildroot}/%{_libdir}/vst/
find %{buildroot} -type f \( -name "*.py" \) -exec chmod a+x {} \;
chmod a+x %{buildroot}%{_datadir}/%{pname}/{carla,carla-control,carla-jack-multi,carla-jack-single,carla-patchbay,carla-rack}
find %{buildroot}%{_libdir} -name '*.so' -exec chmod +x '{}' ';'
%oreon_autofiles Carla-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles Carla-vst usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles lv2-carla usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/studio.kx.carla.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n Carla-devel -f %{oreon_filedir}/Carla-devel.list
%files -n Carla-vst -f %{oreon_filedir}/Carla-vst.list
%files -n lv2-carla -f %{oreon_filedir}/lv2-carla.list

%changelog

%autochangelog
