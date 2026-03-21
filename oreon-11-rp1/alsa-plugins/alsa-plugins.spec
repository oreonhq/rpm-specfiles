%if 0%{?rhel}
%bcond_with avtp
%bcond_with jack
%bcond_with ffmpeg
%else
%bcond_without avtp
%bcond_without jack
%bcond_without ffmpeg
%endif

Name:           alsa-plugins
Version:        1.2.12
Release:        7%{?dist}
Summary:        The Advanced Linux Sound Architecture (ALSA) Plugins
# All packages are LGPL-2.1-or-later with the exception of samplerate
# which is GPL-2.0-or-later, pph plugin is BSD-3-Clause licensed
License:        GPL-2.0-or-later and LGPL-2.1-or-later and BSD-3-Clause
URL:            https://www.alsa-project.org/
# HTTPS so spectool/mock can fetch without FTP (often blocked in builders).
Source0:        https://www.alsa-project.org/files/pub/plugins/%{name}-%{version}.tar.bz2
Patch0:         alsa-git.patch

BuildRequires:  autoconf automake libtool
BuildRequires:  make
BuildRequires:  alsa-lib-devel

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


%if %{with jack}
%files jack
%license COPYING COPYING.GPL
%doc doc/README-jack
%dir %{_sysconfdir}/alsa
%dir %{_sysconfdir}/alsa/conf.d
%config(noreplace) %{_sysconfdir}/alsa/conf.d/50-jack.conf
%dir %{_datadir}/alsa/alsa.conf.d
%{_datadir}/alsa/alsa.conf.d/50-jack.conf
%dir %{_libdir}/alsa-lib
%{_libdir}/alsa-lib/libasound_module_pcm_jack.so
%endif

%files oss
%license COPYING COPYING.GPL
%doc doc/README-pcm-oss
%dir %{_sysconfdir}/alsa
%dir %{_sysconfdir}/alsa/conf.d
%config(noreplace) %{_sysconfdir}/alsa/conf.d/50-oss.conf
%dir %{_datadir}/alsa/alsa.conf.d
%{_datadir}/alsa/alsa.conf.d/50-oss.conf
%dir %{_libdir}/alsa-lib
%{_libdir}/alsa-lib/libasound_module_ctl_oss.so
%{_libdir}/alsa-lib/libasound_module_pcm_oss.so

%files pulseaudio
%license COPYING COPYING.GPL
%doc doc/README-pulse
%dir %{_libdir}/alsa-lib
%{_libdir}/alsa-lib/libasound_module_pcm_pulse.so
%{_libdir}/alsa-lib/libasound_module_ctl_pulse.so
%{_libdir}/alsa-lib/libasound_module_conf_pulse.so
%dir %{_sysconfdir}/alsa
%dir %{_sysconfdir}/alsa/conf.d
%config(noreplace) %{_sysconfdir}/alsa/conf.d/50-pulseaudio.conf
%config(noreplace) %{_sysconfdir}/alsa/conf.d/99-pulseaudio-default.conf
%dir %{_datadir}/alsa/alsa.conf.d
%{_datadir}/alsa/alsa.conf.d/50-pulseaudio.conf

%files samplerate
%license COPYING COPYING.GPL
%doc doc/samplerate.txt
%dir %{_sysconfdir}/alsa
%dir %{_sysconfdir}/alsa/conf.d
%config(noreplace) %{_sysconfdir}/alsa/conf.d/10-samplerate.conf
%dir %{_datadir}/alsa/alsa.conf.d
%{_datadir}/alsa/alsa.conf.d/10-samplerate.conf
%dir %{_libdir}/alsa-lib
%{_libdir}/alsa-lib/libasound_module_rate_samplerate.so
%{_libdir}/alsa-lib/libasound_module_rate_samplerate_best.so
%{_libdir}/alsa-lib/libasound_module_rate_samplerate_linear.so
%{_libdir}/alsa-lib/libasound_module_rate_samplerate_medium.so
%{_libdir}/alsa-lib/libasound_module_rate_samplerate_order.so

%files upmix
%license COPYING COPYING.GPL
%doc doc/upmix.txt
%dir %{_sysconfdir}/alsa
%dir %{_sysconfdir}/alsa/conf.d
%config(noreplace) %{_sysconfdir}/alsa/conf.d/60-upmix.conf
%dir %{_datadir}/alsa/alsa.conf.d
%{_datadir}/alsa/alsa.conf.d/60-upmix.conf
%dir %{_libdir}/alsa-lib
%{_libdir}/alsa-lib/libasound_module_pcm_upmix.so

%files vdownmix
%license COPYING COPYING.GPL
%doc doc/vdownmix.txt
%dir %{_sysconfdir}/alsa
%dir %{_sysconfdir}/alsa/conf.d
%config(noreplace) %{_sysconfdir}/alsa/conf.d/60-vdownmix.conf
%dir %{_datadir}/alsa/alsa.conf.d
%{_datadir}/alsa/alsa.conf.d/60-vdownmix.conf
%dir %{_libdir}/alsa-lib
%{_libdir}/alsa-lib/libasound_module_pcm_vdownmix.so

%files usbstream
%license COPYING COPYING.GPL
%dir %{_sysconfdir}/alsa
%dir %{_sysconfdir}/alsa/conf.d
%config(noreplace) %{_sysconfdir}/alsa/conf.d/98-usb-stream.conf
%dir %{_datadir}/alsa/alsa.conf.d
%{_datadir}/alsa/alsa.conf.d/98-usb-stream.conf
%dir %{_libdir}/alsa-lib
%{_libdir}/alsa-lib/libasound_module_pcm_usb_stream.so

%files arcamav
%license COPYING COPYING.GPL
%doc doc/README-arcam-av
%dir %{_sysconfdir}/alsa
%dir %{_sysconfdir}/alsa/conf.d
%config(noreplace) %{_sysconfdir}/alsa/conf.d/50-arcam-av-ctl.conf
%dir %{_datadir}/alsa/alsa.conf.d
%{_datadir}/alsa/alsa.conf.d/50-arcam-av-ctl.conf
%dir %{_libdir}/alsa-lib
%{_libdir}/alsa-lib/libasound_module_ctl_arcam_av.so

%files speex
%license COPYING COPYING.GPL
%doc doc/speexdsp.txt doc/speexrate.txt
%dir %{_sysconfdir}/alsa
%dir %{_sysconfdir}/alsa/conf.d
%config(noreplace) %{_sysconfdir}/alsa/conf.d/10-speexrate.conf
%config(noreplace) %{_sysconfdir}/alsa/conf.d/60-speex.conf
%dir %{_datadir}/alsa/alsa.conf.d
%{_datadir}/alsa/alsa.conf.d/10-speexrate.conf
%{_datadir}/alsa/alsa.conf.d/60-speex.conf
%dir %{_libdir}/alsa-lib
%{_libdir}/alsa-lib/libasound_module_pcm_speex.so
%{_libdir}/alsa-lib/libasound_module_rate_speexrate.so
%{_libdir}/alsa-lib/libasound_module_rate_speexrate_best.so
%{_libdir}/alsa-lib/libasound_module_rate_speexrate_medium.so

%files maemo
%license COPYING COPYING.GPL
%doc doc/README-maemo
%dir %{_sysconfdir}/alsa
%dir %{_sysconfdir}/alsa/conf.d
%config(noreplace) %{_sysconfdir}/alsa/conf.d/98-maemo.conf
%dir %{_datadir}/alsa/alsa.conf.d
%{_datadir}/alsa/alsa.conf.d/98-maemo.conf
%dir %{_libdir}/alsa-lib
%{_libdir}/alsa-lib/libasound_module_ctl_dsp_ctl.so
%{_libdir}/alsa-lib/libasound_module_pcm_alsa_dsp.so

%if %{with avtp}
%files avtp
%license COPYING COPYING.GPL
%{_libdir}/alsa-lib/libasound_module_pcm_aaf.so
%endif

%if %{with ffmpeg}
%files a52
%license COPYING COPYING.GPL
%doc doc/a52.txt
%dir %{_sysconfdir}/alsa
%dir %{_sysconfdir}/alsa/conf.d
%config(noreplace) %{_sysconfdir}/alsa/conf.d/60-a52-encoder.conf
%dir %{_datadir}/alsa/alsa.conf.d
%{_datadir}/alsa/alsa.conf.d/60-a52-encoder.conf
%dir %{_libdir}/alsa-lib
%{_libdir}/alsa-lib/libasound_module_pcm_a52.so

%files lavrate
%license COPYING COPYING.GPL
%doc doc/lavrate.txt
%dir %{_sysconfdir}/alsa
%dir %{_sysconfdir}/alsa/conf.d
%config(noreplace) %{_sysconfdir}/alsa/conf.d/10-rate-lav.conf
%dir %{_datadir}/alsa/alsa.conf.d
%{_datadir}/alsa/alsa.conf.d/10-rate-lav.conf
%dir %{_libdir}/alsa-lib
%{_libdir}/alsa-lib/libasound_module_rate_lavrate.so
%{_libdir}/alsa-lib/libasound_module_rate_lavrate_fast.so
%{_libdir}/alsa-lib/libasound_module_rate_lavrate_faster.so
%{_libdir}/alsa-lib/libasound_module_rate_lavrate_high.so
%{_libdir}/alsa-lib/libasound_module_rate_lavrate_higher.so
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.12-7
- Prepare for Oreon 11 (RP1)
