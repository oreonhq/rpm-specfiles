%global source14_hash da7eabb7bafdf7d3ae5e9f223aa5bdc1eece45ac569dc21b3b037520b4464768
%global source13_hash 207fe75c396c0ae197c57d42c727163428b6667d98cef3644e41c6f1afe1895f
%global source12_hash 51f83b2b4e9ed2beebc9b8eed2ecad29314a58ed8c5184b22ad8f9df703d3ce5
%global source11_hash 3c718661b01bcd4a9fdda1a49416caeaa955620adf0f2fe73ac6868429d70953
%global source10_hash 1cb6f8c64fe5b24a90b2699e42fea2c778b3e64118d4c80249ac4e272cc8bd5d
%global source0_hash 710d79d60c15c09f0aeb93e5d2f219e7f12ab93f62cab826e4280592a1ea155f
Summary:        Modular SIP user-agent with audio and video support
Name:           baresip
Version:        4.12.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            https://github.com/baresip/baresip
Source0:        https://github.com/baresip/baresip/archive/v%{version}/%{name}-%{version}.tar.gz
Source10:       https://gitlab.gnome.org/GNOME/adwaita-icon-theme/-/raw/1e1d692148e8ab958bfea4188f8575b673804e09/Adwaita/scalable/status/call-incoming-symbolic.svg
Source11:       https://gitlab.gnome.org/GNOME/adwaita-icon-theme/-/raw/1e1d692148e8ab958bfea4188f8575b673804e09/Adwaita/scalable/status/call-outgoing-symbolic.svg
Source12:       https://gitlab.gnome.org/GNOME/adwaita-icon-theme/-/raw/master/COPYING#/COPYING.adwaita-icon-theme
Source13:       https://gitlab.gnome.org/GNOME/adwaita-icon-theme/-/raw/master/COPYING_CCBYSA3#/COPYING_CCBYSA3.adwaita-icon-theme
Source14:       https://gitlab.gnome.org/GNOME/adwaita-icon-theme/-/raw/master/COPYING_LGPL#/COPYING_LGPL.adwaita-icon-theme
Patch0:         https://github.com/baresip/baresip/commit/c09b9ff1d11edf9609c8f91f9bf1c4a1c1d3b767.patch#/baresip-4.5.0-disable-peerconn-test.patch
Recommends:     %{name}-pulse%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-cairo < 1.1.0-1
Obsoletes:      %{name}-rst < 2.0.0-1
Obsoletes:      %{name}-speex_pp < 2.0.0-1
Obsoletes:      %{name}-x11grab < 2.0.0-1
Obsoletes:      %{name}-gsm < 2.6.0-1
Obsoletes:      %{name}-gst_video < 2.6.0-1
Obsoletes:      %{name}-omx < 2.7.0-1
Obsoletes:      %{name}-mpa < 4.3.0-1
# oreon:deps
BuildRequires:  /usr/bin/gdbus-codegen
BuildRequires:  SDL2-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  cjson-devel
BuildRequires:  cmake
BuildRequires:  codec2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fdk-aac-free-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libaom-devel
BuildRequires:  libpng-devel
BuildRequires:  libre-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libv4l-devel
BuildRequires:  libvpx-devel
BuildRequires:  mosquitto-devel
BuildRequires:  openssl-devel
BuildRequires:  opus-devel
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(vpx)
BuildRequires:  portaudio-devel
BuildRequires:  python3-devel
BuildRequires:  spandsp-devel
# /oreon:deps
%description
A modular SIP user-agent with support for audio and video, and many IETF
standards such as SIP, SDP, RTP/RTCP and STUN/TURN/ICE for both, IPv4 and
IPv6.

Additional modules provide support for audio codecs like Codec2, G.711,
G.722, G.726, GSM, L16, MPA and Opus, audio drivers like ALSA, GStreamer,
JACK Audio Connection Kit, Portaudio, and PulseAudio, video codecs like
AV1, VP8 or VP9, video sources like Video4Linux, video outputs like SDL2
or X11, NAT traversal via STUN, TURN, ICE, and NAT-PMP, media encryption
via TLS, SRTP or DTLS-SRTP, management features like embedded web-server
with HTTP interface, command-line console and interface, and MQTT.

%package devel
Summary:        Development files for the baresip library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
%description devel
The baresip-devel package includes header files and libraries necessary
for developing programs which use the baresip C library.

%package alsa
Summary:        ALSA audio driver for baresip
BuildRequires:  alsa-lib-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description alsa
Baresip is a modular SIP user-agent with audio and video support.

This module provides the Advanced Linux Sound Architecture (ALSA) audio
driver.

%package av1
Summary:        AV1 video codec module for baresip
BuildRequires:  libaom-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description av1
Baresip is a modular SIP user-agent with audio and video support.

This module provides the AV1 video codec, an open, royalty-free video
coding format developed as a successor to the VP9 video codec.

%package codec2
Summary:        Codec 2 audio codec module for baresip
BuildRequires:  codec2-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description codec2
Baresip is a modular SIP user-agent with audio and video support.

This module provides the Codec 2 audio codec, an Open Source speech codec
designed for communications quality speech between 700 and 3200 bit/s.

%package ctrl_dbus
Summary:        D-BUS communication channel control module for baresip
BuildRequires:  %{_bindir}/gdbus-codegen
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description ctrl_dbus
Baresip is a modular SIP user-agent with audio and video support.

This module provides a communication channel to control and monitor
baresip via D-BUS.

%package g722
Summary:        G.722 audio codec module for baresip
BuildRequires:  spandsp-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description g722
Baresip is a modular SIP user-agent with audio and video support.

This module provides the G.722 audio codec, often used for HD voice.

%package g726
Summary:        G.726 audio codec module for baresip
BuildRequires:  spandsp-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description g726
Baresip is a modular SIP user-agent with audio and video support.

This module provides the G.726 audio codec.

%package gst
Summary:        GStreamer audio source driver for baresip
BuildRequires:  pkgconfig(gstreamer-1.0)
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description gst
Baresip is a modular SIP user-agent with audio and video support.

This module uses the GStreamer 1.0 framework to play external media and
provides them as an internal audio source.

%package gtk
Summary:        GTK+ menu-based user interface module for baresip
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  desktop-file-utils
License:        BSD-3-Clause AND (LGPL-3.0-or-later OR CC-BY-SA-3.0)
BuildRequires:  librsvg2
BuildRequires:  %{_bindir}/gtk-encode-symbolic-svg
Requires:       adwaita-icon-theme < 3.31.91-1
Requires:       (gnome-shell-extension-topicons-plus if gnome-shell)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Recommends:     libcanberra-gtk3
%description gtk
Baresip is a modular SIP user-agent with audio and video support.

This module provides a GTK+ menu-based user interface.

Note: GTK+ defaults to the Wayland backend, which baresip does not
support. Use 'GDK_BACKEND=x11 baresip' to override it to Xwayland.

%package jack
Summary:        JACK audio driver for baresip
BuildRequires:  pkgconfig(jack)
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description jack
Baresip is a modular SIP user-agent with audio and video support.

This module provides the JACK Audio Connection Kit audio driver.

%package mqtt
Summary:        MQTT management module for baresip
BuildRequires:  mosquitto-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description mqtt
Baresip is a modular SIP user-agent with audio and video support.

This module provides the Message Queue Telemetry Transport (MQTT)
management module.

%package opus
Summary:        Opus speech and audio codec module for baresip
BuildRequires:  opus-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description opus
Baresip is a modular SIP user-agent with audio and video support.

This module provides the Opus speech and audio codec module.

%package plc
Summary:        Packet Loss Concealment module for baresip
BuildRequires:  spandsp-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description plc
Baresip is a modular SIP user-agent with audio and video support.

This module provides the Packet Loss Concealment (PLC) module.

%package portaudio
Summary:        Portaudio audio driver for baresip
BuildRequires:  portaudio-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description portaudio
Baresip is a modular SIP user-agent with audio and video support.

This module provides the Portaudio audio driver.

%package pulse
Summary:        PulseAudio audio driver for baresip
BuildRequires:  pkgconfig(libpulse)
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description pulse
Baresip is a modular SIP user-agent with audio and video support.

This module provides the PulseAudio audio driver.

%package sdl
Summary:        SDL2 video output driver for baresip
BuildRequires:  SDL2-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description sdl
Baresip is a modular SIP user-agent with audio and video support.

This module provides the Simple DirectMedia Layer 2.0 (SDL2) video output
driver.

%package snapshot
Summary:        Snapshot video filter using libpng for baresip
BuildRequires:  libpng-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description snapshot
Baresip is a modular SIP user-agent with audio and video support.

This module takes snapshots of the video stream and saves them as PNG
files using libpng.

%package sndfile
Summary:        Audio dumper module using libsndfile for baresip
BuildRequires:  libsndfile-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description sndfile
Baresip is a modular SIP user-agent with audio and video support.

This module provides an audio dumper to write WAV audio sample files
using libsndfile.

%package tools
Summary:        Collection of tools and helper scripts for baresip
BuildRequires:  python3-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description tools
Baresip is a modular SIP user-agent with audio and video support.

This package provides a collection of tools and helper scripts.

%package vp8
Summary:        VP8 video codec module for baresip
BuildRequires:  libvpx-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description vp8
Baresip is a modular SIP user-agent with audio and video support.

This module provides the VP8 video codec, which is compatible with the
WebRTC standard.

%package vp9
Summary:        VP9 video codec module for baresip
BuildRequires:  pkgconfig(vpx) >= 1.3.0
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description vp9
Baresip is a modular SIP user-agent with audio and video support.

This module provides the VP9 video codec, which is compatible with the
WebRTC standard.

%package v4l2
Summary:        Video4Linux video source driver for baresip
BuildRequires:  libv4l-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description v4l2
Baresip is a modular SIP user-agent with audio and video support.

This module provides the Video4Linux video source driver.

%package x11
Summary:        X11 video output driver for baresip
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description x11
Baresip is a modular SIP user-agent with audio and video support.

This module provides the X11 video output driver.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake \
  -DDEFAULT_CAFILE:PATH="%{_sysconfdir}/pki/tls/certs/ca-bundle.crt" \
  -DDEFAULT_CAPATH:PATH="%{_sysconfdir}/pki/tls/certs" \
  -DDEFAULT_AUDIO_DEVICE:STRING="pulse" \
  -DEXTRA_MODULES:STRING="g726" \
%cmake_build
%install
%cmake_install
install -p -m 0755 tools/fritzbox2%{name} $RPM_BUILD_ROOT%{_bindir}/fritzbox2%{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/com.github.baresip.desktop
%if !0%{?__cmake_in_source_build}
cd %{__cmake_builddir}
%endif
./test/selftest -d %{!?__cmake_in_source_build:../}test/data/ -v
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
