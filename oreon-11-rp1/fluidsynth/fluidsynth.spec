%global source0_hash 6d17570ea2086dd6fbcac995465773a6f316e689089b7fb7ba0b34c2ec6f680d
%global source1_hash 8e71a9f5b62956da6c409dda44b483f98c4a98ae72184f3aa4659ae5b3462e61
Summary:        Real-time software synthesizer
Name:         fluidsynth
Version:      2.6.0
Release:        1%{?dist}
URL:          http://www.fluidsynth.org/
Source0:        https://github.com/Fluidsynth/fluidsynth/archive/v%{version}/fluidsynth-%{version}.tar.gz
Source1:      https://github.com/kthohr/gcem/archive/refs/tags/v1.18.0.tar.gz#/gcem-1.18.0.tar.gz
License:      LGPL-2.1-or-later
Requires:     fluidsynth-libs%{?_isa} = %{version}-%{release}
Recommends:   fluid-soundfont-gm
%if 0%{?el7}
%else
%endif
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  cmake
BuildRequires:  dbus-devel
BuildRequires:  doxygen
BuildRequires:  g++
BuildRequires:  graphviz
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  ladspa-devel
BuildRequires:  libinstpatch-devel
BuildRequires:  libsndfile-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pipewire-devel
BuildRequires:  pkgconfig
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  readline-devel
BuildRequires:  systemd-devel
# /oreon:deps
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
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
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
%if 0%{?el7}
%{cmake3_build}
%else
%{cmake_build}
%endif
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n fluidsynth-libs -f %{oreon_filedir}/fluidsynth-libs.list
%files -n fluidsynth-devel -f %{oreon_filedir}/fluidsynth-devel.list

%changelog

%autochangelog
