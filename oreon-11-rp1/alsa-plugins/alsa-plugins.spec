%global source0_hash 7bd8a83d304e8e2d86a25895d8dcb0ef0245a8df32e271959cdbdc6af39b66f2
%bcond_without avtp
%bcond_without jack
%bcond_without ffmpeg
Name:           alsa-plugins
Version:        1.2.12
Release:        7%{?dist}
Summary:        The Advanced Linux Sound Architecture (ALSA) Plugins
License:        GPL-2.0-or-later and LGPL-2.1-or-later and BSD-3-Clause
URL:            https://www.alsa-project.org/
Source0:        https://www.alsa-project.org/files/pub/plugins/%{name}-%{version}.tar.bz2
Patch0:         alsa-git.patch
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dbus-devel
BuildRequires:  ffmpeg-free-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libavtp-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  speex-devel
BuildRequires:  speexdsp-devel
# /oreon:deps
%description
The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI
functionality to the Linux operating system.

This package includes plugins for ALSA.

%if %{with jack}
%package jack
Recommends:     jack-audio-connection-kit
BuildRequires:  jack-audio-connection-kit-devel
Summary:        Jack PCM output plugin for ALSA
License:        LGPL-2.1-or-later
%description jack
This plugin converts the ALSA API over JACK (Jack Audio Connection
Kit, http://jackit.sf.net) API.  ALSA native applications can work
transparently together with jackd for both playback and capture.
This plugin provides the PCM type "jack"
%endif

%package oss
Summary:        Oss PCM output plugin for ALSA
License:        LGPL-2.1-or-later
%description oss
This plugin converts the ALSA API over OSS API.  With this plugin,
ALSA native apps can run on OSS drivers.

This plugin provides the PCM type "oss".

%package pulseaudio
Recommends:     pulseaudio-daemon
BuildRequires:  pulseaudio-libs-devel
Summary:        Alsa to PulseAudio backend
License:        LGPL-2.1-or-later
%description pulseaudio
This plugin allows any program that uses the ALSA API to access a PulseAudio
sound daemon. In other words, native ALSA applications can play and record
sound across a network. There are two plugins in the suite, one for PCM and
one for mixer control.

%package samplerate
BuildRequires:  libsamplerate-devel
Summary:        External rate converter plugin for ALSA
License:        GPL-2.0-or-later
%description samplerate
This plugin is an external rate converter using libsamplerate by Erik de
Castro Lopo.

%package upmix
BuildRequires:  libsamplerate-devel
Summary:        Upmixer channel expander plugin for ALSA
License:        LGPL-2.1-or-later
%description upmix
The upmix plugin is an easy-to-use plugin for upmixing to 4 or
6-channel stream.  The number of channels to be expanded is determined
by the slave PCM or explicitly via channel option.

%package vdownmix
BuildRequires:  libsamplerate-devel
Summary:        Downmixer to stereo plugin for ALSA
License:        LGPL-2.1-or-later
%description vdownmix
The vdownmix plugin is a downmixer from 4-6 channels to 2-channel
stereo headphone output.  This plugin processes the input signals with
a simple spacialization, so the output sounds like a kind of "virtual
surround".

%package usbstream
Summary:        USB stream plugin for ALSA
License:        LGPL-2.1-or-later
%description usbstream
The usbstream plugin is for snd-usb-us122l driver. It converts PCM
stream to USB specific stream.

%package arcamav
Summary:        Arcam AV amplifier plugin for ALSA
License:        LGPL-2.1-or-later
%description arcamav
This plugin exposes the controls for an Arcam AV amplifier
(see: http://www.arcam.co.uk/) as an ALSA mixer device.

%package speex
Requires:       speex speexdsp
BuildRequires:  speex-devel speexdsp-devel
Summary:        Rate Converter Plugin Using Speex Resampler
License:        LGPL-2.1-or-later
%description speex
The rate plugin is an external rate converter using the Speex resampler
(aka Public Parrot Hack) by Jean-Marc Valin. The pcm plugin provides
pre-processing of a mono stream like denoise using libspeex DSP API.

%package maemo
BuildRequires:  dbus-devel
Summary:        Maemo plugin for ALSA
License:        LGPL-2.1-or-later
%description maemo
This plugin converts the ALSA API over PCM task nodes protocol. In this way,
ALSA native applications can run over DSP Gateway and use DSP PCM task nodes.

%if %{with avtp}
%package avtp
BuildRequires:  libavtp-devel
Summary:        Audio Video Transport Protocol (AVTP) plugin for ALSA
License:        LGPL-2.1-or-later
%description avtp
This plugin supports Audio Video Transport Protocol (AVTP) as specified in
IEEE 1722-2016 spec. AVTP is part of the Audio/Video Broadcast using TSN.
%endif

%if %{with ffmpeg}
%package a52
BuildRequires:  ffmpeg-free-devel
Obsoletes:      alsa-plugins-freeworld-a52 <= %{version}-%{release}
Summary:        A52 output plugin for ALSA using libavcodec
License:        LGPL-2.1-or-later
%description a52
This plugin converts S16 linear format to A52 compressed stream and
send to an SPDIF output.  It requires libavcodec for encoding the
audio stream.

%package lavrate
BuildRequires:  ffmpeg-free-devel
Obsoletes:      alsa-plugins-freeworld-lavrate <= %{version}-%{release}
Summary:        Rate converter plugin for ALSA using libavcodec
License:        LGPL-2.1-or-later
%description lavrate
The plugin uses ffmpeg audio resample library to convert audio rates.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{version}%{?prever} -p1

%build

autoreconf -vif
%configure --disable-static \
           --with-speex=lib \
           --enable-maemo-plugin \
           --enable-maemo-resource-manager
%make_build
%install
%make_install
mv %{buildroot}%{_sysconfdir}/alsa/conf.d/99-pulseaudio-default.conf.example \
        %{buildroot}%{_sysconfdir}/alsa/conf.d/99-pulseaudio-default.conf
find %{buildroot} -name "*.la" -delete
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with jack}
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.12-7
- Prepare for Oreon 11 (RP1)
%endif
