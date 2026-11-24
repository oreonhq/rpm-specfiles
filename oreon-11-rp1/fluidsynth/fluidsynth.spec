# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash c51ebe04c8a445f4a7dd5a86e09a27b5c5af547756574edc52fc61c88ebe8427
%global source1_hash 8e71a9f5b62956da6c409dda44b483f98c4a98ae72184f3aa4659ae5b3462e61
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Summary:      Real-time software synthesizer
Name:         fluidsynth
Version:      2.6.3
Release:      1%{?dist}
URL:          http://www.fluidsynth.org/
Source0:      https://github.com/Fluidsynth/fluidsynth/archive/v%{version}/fluidsynth-%{version}.tar.gz
Source1:      https://github.com/kthohr/gcem/archive/refs/tags/gcem-1.18.0.tar.gz
License:      LGPL-2.1-or-later
Requires:     fluidsynth-libs%{?_isa} = %{version}-%{release}
Recommends:   fluid-soundfont-gm

BuildRequires: oreon-rpm-macros
BuildRequires: clang
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
BuildRequires: pulseaudio-libs-devel
BuildRequires: pipewire-devel
BuildRequires: libinstpatch-devel
BuildRequires: readline-devel
BuildRequires: graphviz
BuildRequires: systemd-devel

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
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
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
