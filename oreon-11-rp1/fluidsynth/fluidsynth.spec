%global source0_hash none


Summary:      Real-time software synthesizer
Name:         fluidsynth
Version:      2.5.4
Release:      1%{?dist}
URL:          http://www.fluidsynth.org/
Source0:      https://github.com/Fluidsynth/fluidsynth/archive/v%{version}/fluidsynth-%{version}.tar.gz
Source1:      https://github.com/kthohr/gcem/archive/refs/tags/gcem-1.18.0.tar.gz
License:      LGPL-2.1-or-later
Requires:     fluidsynth-libs%{?_isa} = %{version}-%{release}
Recommends:   fluid-soundfont-gm

BuildRequires: alsa-lib-devel
%if 0%{?el7}
BuildRequires: cmake3
%else
BuildRequires: cmake
%endif
BuildRequires: dbus-devel
BuildRequires: g++
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires:  pipewire-jack-audio-connection-kit-devel
%else
BuildRequires:  jack-audio-connection-kit-devel
%endif
BuildRequires: ladspa-devel
BuildRequires: libsndfile-devel
BuildRequires: ncurses-devel
BuildRequires: pkgconfig
# Disabled for now:
# http://sourceforge.net/apps/trac/fluidsynth/ticket/51
# To enable portaudio support one also has to pass
# -Denable-portaudio=on to cmake
# BuildRequires: portaudio-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: pipewire-devel
BuildRequires: libinstpatch-devel
BuildRequires: readline-devel
BuildRequires: graphviz
BuildRequires: systemd-devel

# For documentation:
BuildRequires: doxygen
BuildRequires: make

%description
FluidSynth is a real-time software synthesizer based on the SoundFont 2 
specifications. It is a "software synthesizer". FluidSynth can read MIDI events
from the MIDI input device and render them to the audio device. It features 
real-time effect modulation using SoundFont 2.01 modulators, and a built-in
command line shell. It can also play MIDI files (note: FluidSynth was previously
called IIWU Synth).

%package libs
Summary:   Real-time software synthesizer run-time libraries

%description libs
FluidSynth is a real-time software synthesizer based on the SoundFont 2 
specifications. It is a "software synthesizer". This package holds the run-time
shared libraries.

%package devel
Summary:   Real-time software synthesizer development files
Requires:  fluidsynth-libs%{?_isa} = %{version}-%{release}
Requires:  fluidsynth%{?_isa} = %{version}-%{release}

%description devel
FluidSynth is a real-time software synthesizer based on the SoundFont 2 
specifications. It is a "software synthesizer". This package holds header files
for building programs that link against fluidsynth.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
%setup -q -a 1
cp -r gcem-1.18.0/include gcem/

%build

%define enable_jack on
%define fluidsynth_env %{_sysconfdir}/sysconfig/fluidsynth

%if 0%{?el7}
%{cmake3} -Denable-ladspa=on -Denable-jack=%{enable_jack} -DFLUID_DAEMON_ENV_FILE=%{fluidsynth_env}
%else
%{cmake} -Denable-ladspa=on -Denable-jack=%{enable_jack} -DFLUID_DAEMON_ENV_FILE=%{fluidsynth_env}
%endif

# build fluidsynth
%if 0%{?el7}
%{cmake3_build}
%else
%{cmake_build}
%endif

# build docs
make doxygen -C doc

%install
%if 0%{?el7}
%{cmake3_install}
%else
%{cmake_install}
%endif
sed -i 's/^#SOUND_FONT/SOUND_FONT/' %{__cmake_builddir}/fluidsynth.conf
install -Dm 644 %{__cmake_builddir}/fluidsynth.conf %{buildroot}%{fluidsynth_env}
install -Dm 644 %{__cmake_builddir}/fluidsynth.service %{buildroot}%{_userunitdir}/fluidsynth.service

%files
%{_bindir}/fluid*
%{_mandir}/man1/fluidsynth*
%config(noreplace) %{fluidsynth_env}
%attr(0644,root,root) %{_userunitdir}/fluidsynth.service

%files libs
%license LICENSE
%doc AUTHORS README.md THANKS TODO
%{_libdir}/libfluidsynth.so.3
%{_libdir}/libfluidsynth.so.3.*

%files devel
%doc doc/*fluid*.txt doc/*.odt
%doc ChangeLog.old
%{_includedir}/fluidsynth.h
%{_includedir}/fluidsynth/
%{_libdir}/libfluidsynth.so
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/fluidsynth/


%changelog
%autochangelog

