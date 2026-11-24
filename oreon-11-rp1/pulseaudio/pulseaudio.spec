# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 053794d6671a3e397d849e478a80b82a63cb9d8ca296bd35b73317bb5ceb87b5
%global source1_hash 212ceacdec35abed7370b0f412f775b9b6784795daa4dc0953cbd18e3acc417e
%global source5_hash a18ea3a17bf1c52011cb15f500973946625586786ad8f7c7eec1808f80ffd939
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global pa_major   17.0

%global with_webrtc 1

%if 0%{?fedora} || 0%{?oreon}
%global enable_daemon 1
%global enable_jack 1
%endif
%if 0%{?fedora}
%global enable_lirc 1
%endif
%if 0%{?oreon}
%global enable_gstreamer 0
%else
%global enable_gstreamer 1
%endif

%global _hardened_build 1

%global systemd 1

%if 0%{?fedora} < 28 && 0%{?rhel} < 8
%global gdm_hooks 1
%endif

%global tests 1

%global multilib_archs x86_64 %{ix86} ppc64 ppc s390x s390 sparc64 sparcv9 ppc64le

Name:           pulseaudio
Summary:        Improved Linux Sound Server
Version:        %{pa_major}%{?pa_minor:.%{pa_minor}}
Release:        11%{?snap:.%{snap}git%{shortcommit}}%{?dist}
License:        LGPL-2.1-or-later
URL:            http://www.freedesktop.org/wiki/Software/PulseAudio
%if 0%{?gitrel}
Source0:        pulseaudio-%{version}-%{gitrel}-g%{shortcommit}.tar.xz
%else
Source0:        https://freedesktop.org/software/pulseaudio/releases/pulseaudio-%{version}.tar.xz
Source1:        https://freedesktop.org/software/pulseaudio/releases/pulseaudio-%{version}.tar.xz.sha256sum
%endif

Source5:        default.pa-for-gdm

Patch201: pulseaudio-autostart.patch

Patch206: pulseaudio-11.1-autospawn_disable.patch

Patch0001: 0001-alsa-ucm-Check-UCM-verb-before-working-with-device-s.patch
Patch0002: 0002-alsa-ucm-Replace-port-device-UCM-context-assertion-w.patch
Patch0003: 0003-Don-t-log-battery-level-and-dock-status-every-minute.patch
Patch0004: 0004-tests-Don-t-run-volume-tests-with-impossible-alignme.patch
Patch0005: 0005-rtp-recv-Remove-inappropriate-byte-order-conversion.patch
Patch0006: 0006-stream-fix-array-out-of-bounds-in-stream_get_timing_.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig(bash-completion)
%global bash_completionsdir %(pkg-config --variable=completionsdir bash-completion 2>/dev/null || echo '/etc/bash_completion.d')
BuildRequires:  m4
BuildRequires:  pkgconfig
BuildRequires:  doxygen
BuildRequires:  xmltoman
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(sndfile)
%if 0%{?systemd}
BuildRequires:  pkgconfig(libsystemd)
%endif
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(libasyncns) >= 0.1
BuildRequires:  pkgconfig(gtk+-3.0)
%if 0%{?tests}
BuildRequires:  pkgconfig(check)
%endif

%if 0%{?enable_daemon}

BuildRequires:  libtool-ltdl-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  avahi-devel
BuildRequires:  pkgconfig(bluez) >= 5.0
BuildRequires:  sbc-devel
BuildRequires:  libXt-devel
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  libXtst-devel
BuildRequires:  libXi-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libICE-devel
BuildRequires:  xcb-util-devel
BuildRequires:  openssl-devel
BuildRequires:  orc-devel
BuildRequires:  libtdb-devel
%if 0%{?fedora} || 0%{?oreon}
BuildRequires:  pkgconfig(soxr)
%endif
BuildRequires:  pkgconfig(speexdsp) >= 1.2
BuildRequires:  libasyncns-devel
%if 0%{?systemd}
BuildRequires:  systemd-devel >= 184
BuildRequires:  systemd
%{?systemd_requires}
%endif
BuildRequires:  libcap-devel
%if 0%{?with_webrtc}
BuildRequires:  pkgconfig(webrtc-audio-processing-1) >= 1.0
%endif
%if 0%{?enable_gstreamer}
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.16.0
BuildRequires:  pkgconfig(gstreamer-app-1.0) >= 1.16.0
BuildRequires:  pkgconfig(gstreamer-rtp-1.0) >= 1.16.0
%endif

Obsoletes:      padevchooser < 1.0
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       rtkit

Provides:       pulseaudio-daemon
Conflicts:      pulseaudio-daemon

Obsoletes:      pulseaudio-esound-compat < 15.0
Obsoletes:      pulseaudio-module-gconf < 15.0

%endif

%description
PulseAudio is a sound server for Linux and other Unix like operating
systems. It is intended to be an improved drop-in replacement for the
Enlightened Sound Daemon (ESOUND).

%if 0%{?enable_daemon}

%package qpaeq
Summary:	Pulseaudio equalizer interface
Requires: 	%{name}%{?_isa} = %{version}-%{release}
Requires:	python3-qt5-base
Requires:	python3-dbus
%description qpaeq
qpaeq is a equalizer interface for pulseaudio's equalizer sinks.

%if 0%{?enable_lirc}
%package module-lirc
Summary:        LIRC support for the PulseAudio sound server
BuildRequires:  lirc-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description module-lirc
LIRC volume control module for the PulseAudio sound server.
%endif

%package module-x11
Summary:        X11 support for the PulseAudio sound server
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-utils

%description module-x11
X11 bell and security modules for the PulseAudio sound server.

%package module-zeroconf
Summary:        Zeroconf support for the PulseAudio sound server
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-utils

%description module-zeroconf
Zeroconf publishing module for the PulseAudio sound server.

%package module-bluetooth
Summary:        Bluetooth support for the PulseAudio sound server
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       bluez >= 5.0

%description module-bluetooth
Contains Bluetooth audio (A2DP/HSP/HFP) support for the PulseAudio sound server.

%if 0%{?enable_jack}
%package module-jack
Summary:        JACK support for the PulseAudio sound server
BuildRequires:  jack-audio-connection-kit-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description module-jack
JACK sink and source modules for the PulseAudio sound server.
%endif

%package module-gsettings
Summary:        Gsettings support for the PulseAudio sound server
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description module-gsettings
GSettings configuration backend for the PulseAudio sound server.

%endif

%package libs
Summary:        Libraries for PulseAudio clients
License:        LGPL-2.1-or-later
Obsoletes:      pulseaudio-libs-zeroconf < 1.1

%description libs
This package contains the runtime libraries for any application that wishes
to interface with a PulseAudio sound server.

%package libs-glib2
Summary:        GLIB 2.x bindings for PulseAudio clients
License:        LGPL-2.1-or-later
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description libs-glib2
This package contains bindings to integrate the PulseAudio client library with
a GLIB 2.x based application.

%package libs-devel
Summary:        Headers and libraries for PulseAudio client development
License:        LGPL-2.1-or-later
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs-glib2%{?_isa} = %{version}-%{release}
%description libs-devel
Headers and libraries for developing applications that can communicate with
a PulseAudio sound server.

%package utils
Summary:        PulseAudio sound server utilities
License:        LGPL-2.1-or-later
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      pulseaudio-utils < 3.0-3

%description utils
This package contains command line utilities for the PulseAudio sound server.

%if 0%{?gdm_hooks}
%package gdm-hooks
Summary:        PulseAudio GDM integration
License:        LGPL-2.1-or-later
Requires:       gdm >= 1:2.22.0
Requires(pre):  gdm

%description gdm-hooks
This package contains GDM integration hooks for the PulseAudio sound server.
%endif

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source5_hash}  %{SOURCE5}' | sha256sum -c -
%setup -q -T -b0 -n %{name}-%{version}%{?gitrel:-%{gitrel}-g%{shortcommit}}

%patch 1 -p1 -b .ucm1
%patch 2 -p1 -b .ucm2
%patch 3 -p1 -b .battery_log
%patch 4 -p1 -b .volume_test
%patch 5 -p1 -b .byte_order
%patch 6 -p1 -b .array_oob

%patch 201 -p1 -b .autostart
%if 0%{?systemd}
%patch 206 -p1 -b .autospawn_disable
%endif

%if 0%{?gitrel:1}
sed -i.PACKAGE_VERSION -e "s|^PACKAGE_VERSION=.*|PACKAGE_VERSION=\'%{version}\'|" configure
%else

%endif

%if 0%{?enable_daemon}
cat >pulseaudio.sysusers.conf <<EOF
g pulse-access -
g pulse-rt -
u pulse 171 'PulseAudio System Daemon' %{_localstatedir}/run/pulse -
EOF
%endif

%build
%meson \
  -D client=true \
  -D valgrind=disabled \
  -D systemd=%{?systemd:enabled}%{!?systemd:disabled} \
  -D oss-output=enabled \
  -D gtk=disabled \
%if 0%{?enable_daemon}
  -D daemon=true \
  -D system_user=pulse \
  -D system_group=pulse \
  -D access_group=pulse-access \
  -D jack=%{?enable_jack:enabled}%{!?enable_jack:disabled} \
  -D lirc=%{?enable_lirc:enabled}%{!?enable_lirc:disabled} \
  -D tcpwrap=disabled \
  -D bluez5=enabled \
  -D gstreamer=%{?enable_gstreamer:enabled}%{!?enable_gstreamer:disabled} \
  -D bluez5-gstreamer=%{?enable_gstreamer:enabled}%{!?enable_gstreamer:disabled} \
  -D gsettings=enabled \
  -D elogind=disabled \
  -D soxr=%{?fedora:enabled}%{?oreon:enabled}%{!?fedora:%{!?oreon:disabled}} \
  -D webrtc-aec=%{?with_webrtc:enabled}%{!?with_webrtc:disabled} \
  -D consolekit=disabled \
%else
  -D daemon=false \
%endif
  -D tests=%{?tests:true}%{!?tests:false}

%meson_build

%meson_build doxygen

%install
%meson_install

%ifarch %{multilib_archs}
pushd %{buildroot}%{_bindir}
%if "%{_libdir}" == "/usr/lib"
ln -s padsp padsp-32
%else
cp -a padsp padsp-32
sed -i -e "s|%{_libdir}/pulseaudio/libpulsedsp.so|/usr/lib/pulseaudio/libpulsedsp.so|g" padsp-32
%endif
popd
%endif

%if 0%{?enable_daemon}
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/udev/rules.d
mv -fv $RPM_BUILD_ROOT/lib/udev/rules.d/90-pulseaudio.rules $RPM_BUILD_ROOT%{_prefix}/lib/udev/rules.d
install -m0644 -D pulseaudio.sysusers.conf %{buildroot}%{_sysusersdir}/pulseaudio.conf
%endif

%if 0%{?gdm_hooks}
install -p -m644 -D %{SOURCE5} $RPM_BUILD_ROOT%{_localstatedir}/lib/gdm/.pulse/default.pa
%endif

rm -fv $RPM_BUILD_ROOT%{_libdir}/pulseaudio/modules/module-detect.so
rm -fv $RPM_BUILD_ROOT%{_libdir}/pulseaudio/modules/liboss-util.so
rm -fv $RPM_BUILD_ROOT%{_libdir}/pulseaudio/modules/module-oss.so
%if !0%{?enable_daemon}
rm -fv $RPM_BUILD_ROOT%{_bindir}/pa-info
%endif

%find_lang %{name}

%check
%if 0%{?tests}
%ifarch %{ix86} s390x
%global tests_nonfatal 1
%endif
%if 0%{?fedora} > 27
%global tests_nonfatal 1
%endif
%meson_test || TESTS_ERROR=$?
if [ "${TESTS_ERROR}" != "" ]; then
cat src/test-suite.log
%{!?tests_nonfatal:exit $TESTS_ERROR}
fi
%endif

%if 0%{?enable_daemon}

%posttrans
(grep '^load-module module-cork-music-on-phone$' %{_sysconfdir}/pulse/default.pa > /dev/null && \
 sed -i.rpmsave -e 's|^load-module module-cork-music-on-phone$|load-module module-role-cork|' \
 %{_sysconfdir}/pulse/default.pa
) ||:

%post
%{?ldconfig}
%if 0%{?systemd}
%if 0%{?fedora} < 31
%systemd_user_post pulseaudio.service
%endif
%systemd_user_post pulseaudio.socket
%endif

%if 0%{?systemd}
%preun
%if 0%{?fedora} < 31
%systemd_user_preun pulseaudio.service
%endif
%systemd_user_preun pulseaudio.socket
%endif

%ldconfig_postun

%if 0%{?systemd}
%triggerun -- pulseaudio < 12.2-4
systemctl --no-reload preset --global pulseaudio.socket >/dev/null 2>&1 || :
%endif

%endif

%if 0%{?enable_daemon}

%files
%doc README
%license LICENSE GPL LGPL
%config(noreplace) %{_sysconfdir}/pulse/daemon.conf
%config(noreplace) %{_sysconfdir}/pulse/default.pa
%config(noreplace) %{_sysconfdir}/pulse/system.pa
%{bash_completionsdir}/pulseaudio
%if 0%{?systemd}
%{_userunitdir}/pulseaudio.service
%{_userunitdir}/pulseaudio.socket
%endif
%{_bindir}/pa-info
%{_bindir}/pulseaudio
%{_libdir}/pulseaudio/libpulsecore-%{pa_major}.so
%dir %{_libdir}/pulseaudio/
%dir %{_libdir}/pulseaudio/modules/
%{_libdir}/pulseaudio/modules/libalsa-util.so
%{_libdir}/pulseaudio/modules/libcli.so
%{_libdir}/pulseaudio/modules/libprotocol-cli.so
%{_libdir}/pulseaudio/modules/libprotocol-http.so
%{_libdir}/pulseaudio/modules/libprotocol-native.so
%{_libdir}/pulseaudio/modules/libprotocol-simple.so
%{_libdir}/pulseaudio/modules/librtp.so
%if 0%{?with_webrtc}
%{_libdir}/pulseaudio/modules/libwebrtc-util.so
%endif
%{_libdir}/pulseaudio/modules/module-allow-passthrough.so
%{_libdir}/pulseaudio/modules/module-alsa-sink.so
%{_libdir}/pulseaudio/modules/module-alsa-source.so
%{_libdir}/pulseaudio/modules/module-alsa-card.so
%{_libdir}/pulseaudio/modules/module-cli-protocol-tcp.so
%{_libdir}/pulseaudio/modules/module-cli-protocol-unix.so
%{_libdir}/pulseaudio/modules/module-cli.so
%{_libdir}/pulseaudio/modules/module-combine.so
%{_libdir}/pulseaudio/modules/module-combine-sink.so
%{_libdir}/pulseaudio/modules/module-dbus-protocol.so
%{_libdir}/pulseaudio/modules/module-filter-apply.so
%{_libdir}/pulseaudio/modules/module-filter-heuristics.so
%{_libdir}/pulseaudio/modules/module-device-manager.so
%{_libdir}/pulseaudio/modules/module-loopback.so
%{_libdir}/pulseaudio/modules/module-udev-detect.so
%{_libdir}/pulseaudio/modules/module-hal-detect.so
%{_libdir}/pulseaudio/modules/module-http-protocol-tcp.so
%{_libdir}/pulseaudio/modules/module-http-protocol-unix.so
%{_libdir}/pulseaudio/modules/module-match.so
%{_libdir}/pulseaudio/modules/module-mmkbd-evdev.so
%{_libdir}/pulseaudio/modules/module-native-protocol-fd.so
%{_libdir}/pulseaudio/modules/module-native-protocol-tcp.so
%{_libdir}/pulseaudio/modules/module-native-protocol-unix.so
%{_libdir}/pulseaudio/modules/module-null-sink.so
%{_libdir}/pulseaudio/modules/module-null-source.so
%{_libdir}/pulseaudio/modules/module-pipe-sink.so
%{_libdir}/pulseaudio/modules/module-pipe-source.so
%{_libdir}/pulseaudio/modules/module-remap-source.so
%{_libdir}/pulseaudio/modules/module-rescue-streams.so
%{_libdir}/pulseaudio/modules/module-role-ducking.so
%{_libdir}/pulseaudio/modules/module-rtp-recv.so
%{_libdir}/pulseaudio/modules/module-rtp-send.so
%{_libdir}/pulseaudio/modules/module-simple-protocol-tcp.so
%{_libdir}/pulseaudio/modules/module-simple-protocol-unix.so
%{_libdir}/pulseaudio/modules/module-sine.so
%{_libdir}/pulseaudio/modules/module-switch-on-port-available.so
%{_libdir}/pulseaudio/modules/module-systemd-login.so
%{_libdir}/pulseaudio/modules/module-tunnel-sink-new.so
%{_libdir}/pulseaudio/modules/module-tunnel-sink.so
%{_libdir}/pulseaudio/modules/module-tunnel-source-new.so
%{_libdir}/pulseaudio/modules/module-tunnel-source.so
%{_libdir}/pulseaudio/modules/module-volume-restore.so
%{_libdir}/pulseaudio/modules/module-suspend-on-idle.so
%{_libdir}/pulseaudio/modules/module-default-device-restore.so
%{_libdir}/pulseaudio/modules/module-device-restore.so
%{_libdir}/pulseaudio/modules/module-stream-restore.so
%{_libdir}/pulseaudio/modules/module-card-restore.so
%{_libdir}/pulseaudio/modules/module-ladspa-sink.so
%{_libdir}/pulseaudio/modules/module-remap-sink.so
%{_libdir}/pulseaudio/modules/module-always-sink.so
%{_libdir}/pulseaudio/modules/module-always-source.so
%{_libdir}/pulseaudio/modules/module-position-event-sounds.so
%{_libdir}/pulseaudio/modules/module-augment-properties.so
%{_libdir}/pulseaudio/modules/module-role-cork.so
%{_libdir}/pulseaudio/modules/module-sine-source.so
%{_libdir}/pulseaudio/modules/module-intended-roles.so
%{_libdir}/pulseaudio/modules/module-rygel-media-server.so
%{_libdir}/pulseaudio/modules/module-echo-cancel.so
%{_libdir}/pulseaudio/modules/module-switch-on-connect.so
%{_libdir}/pulseaudio/modules/module-virtual-sink.so
%{_libdir}/pulseaudio/modules/module-virtual-source.so
%{_libdir}/pulseaudio/modules/module-virtual-surround-sink.so
%dir %{_datadir}/pulseaudio/
%dir %{_datadir}/pulseaudio/alsa-mixer/
%{_datadir}/pulseaudio/alsa-mixer/paths/
%{_datadir}/pulseaudio/alsa-mixer/profile-sets/
%{_datadir}/dbus-1/system.d/pulseaudio-system.conf
%{_mandir}/man1/pulseaudio.1*
%{_mandir}/man5/default.pa.5*
%{_mandir}/man5/pulse-cli-syntax.5*
%{_mandir}/man5/pulse-daemon.conf.5*
%{_prefix}/lib/udev/rules.d/90-pulseaudio.rules
%dir %{_libexecdir}/pulse
%dir %{_datadir}/zsh/
%dir %{_datadir}/zsh/site-functions/
%{_datadir}/zsh/site-functions/_pulseaudio
%{_sysusersdir}/pulseaudio.conf

%files qpaeq
%{_bindir}/qpaeq
%{_libdir}/pulseaudio/modules/module-equalizer-sink.so

%if 0%{?enable_lirc}
%files module-lirc
%{_libdir}/pulseaudio/modules/module-lirc.so
%endif

%files module-x11
%config(noreplace) %{_sysconfdir}/xdg/autostart/pulseaudio.desktop
%config(noreplace) %{_sysconfdir}/xdg/Xwayland-session.d/00-pulseaudio-x11
%{_userunitdir}/pulseaudio-x11.service
%{_bindir}/start-pulseaudio-x11
%{_libdir}/pulseaudio/modules/module-x11-bell.so
%{_libdir}/pulseaudio/modules/module-x11-publish.so
%{_libdir}/pulseaudio/modules/module-x11-xsmp.so
%{_libdir}/pulseaudio/modules/module-x11-cork-request.so
%{_mandir}/man1/start-pulseaudio-x11.1.gz

%files module-zeroconf
%{_libdir}/pulseaudio/modules/libavahi-wrap.so
%{_libdir}/pulseaudio/modules/module-zeroconf-publish.so
%{_libdir}/pulseaudio/modules/module-zeroconf-discover.so
%{_libdir}/pulseaudio/modules/libraop.so
%{_libdir}/pulseaudio/modules/module-raop-discover.so
%{_libdir}/pulseaudio/modules/module-raop-sink.so

%if 0%{?enable_jack}
%files module-jack
%{_libdir}/pulseaudio/modules/module-jackdbus-detect.so
%{_libdir}/pulseaudio/modules/module-jack-sink.so
%{_libdir}/pulseaudio/modules/module-jack-source.so
%endif

%files module-bluetooth
%{_libdir}/pulseaudio/modules/libbluez*-util.so
%{_libdir}/pulseaudio/modules/module-bluez*-device.so
%{_libdir}/pulseaudio/modules/module-bluez*-discover.so
%{_libdir}/pulseaudio/modules/module-bluetooth-discover.so
%{_libdir}/pulseaudio/modules/module-bluetooth-policy.so

%files module-gsettings
%{_libdir}/pulseaudio/modules/module-gsettings.so
%{_libexecdir}/pulse/gsettings-helper
%{_datadir}/GConf/gsettings/pulseaudio.convert
%{_datadir}/glib-2.0/schemas/org.freedesktop.pulseaudio.gschema.xml

%endif

%ldconfig_scriptlets libs

%files libs -f %{name}.lang
%doc README
%license LICENSE GPL LGPL
%dir %{_sysconfdir}/pulse/
%config(noreplace) %{_sysconfdir}/pulse/client.conf
%{_libdir}/libpulse.so.0*
%{_libdir}/libpulse-simple.so.0*
%dir %{_libdir}/pulseaudio/
%{_libdir}/pulseaudio/libpulsecommon-%{pa_major}.so
%{_libdir}/pulseaudio/libpulsedsp.so

%ldconfig_scriptlets libs-glib2

%files libs-glib2
%{_libdir}/libpulse-mainloop-glib.so.0*

%files libs-devel
%doc %{_vpath_builddir}/doxygen/html
%{_includedir}/pulse/
%{_libdir}/libpulse.so
%{_libdir}/libpulse-mainloop-glib.so
%{_libdir}/libpulse-simple.so
%{_libdir}/pkgconfig/libpulse*.pc
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libpulse.vapi
%{_datadir}/vala/vapi/libpulse.deps
%{_datadir}/vala/vapi/libpulse-mainloop-glib.vapi
%{_datadir}/vala/vapi/libpulse-mainloop-glib.deps
%{_datadir}/vala/vapi/libpulse-simple.deps
%{_datadir}/vala/vapi/libpulse-simple.vapi

%dir %{_libdir}/cmake
%{_libdir}/cmake/PulseAudio/

%files utils
%{_bindir}/pacat
%{_bindir}/pactl
%{_bindir}/paplay
%{_bindir}/parec
%{_bindir}/pamon
%{_bindir}/parecord
%{_bindir}/pax11publish
%{_bindir}/padsp
%ifarch %{multilib_archs}
%{_bindir}/padsp-32
%endif
%if 0%{?enable_daemon}
%{_bindir}/pacmd
%{_bindir}/pasuspender
%endif
%{_mandir}/man1/pacat.1*
%{_mandir}/man1/pactl.1*
%{_mandir}/man1/padsp.1*
%{_mandir}/man1/pamon.1*
%{_mandir}/man1/paplay.1*
%{_mandir}/man1/parec.1*
%{_mandir}/man1/parecord.1*
%{_mandir}/man1/pax11publish.1*
%if 0%{?enable_daemon}
%{_mandir}/man1/pacmd.1*
%{_mandir}/man1/pasuspender.1*
%endif
%{_mandir}/man5/pulse-client.conf.5*
%{bash_completionsdir}/pacat
%{bash_completionsdir}/pactl
%{bash_completionsdir}/padsp
%{bash_completionsdir}/paplay
%{bash_completionsdir}/parec
%{bash_completionsdir}/parecord
%if 0%{?enable_daemon}
%{bash_completionsdir}/pacmd
%{bash_completionsdir}/pasuspender
%endif
%{_datadir}/zsh/site-functions/_pulseaudio

%if 0%{?gdm_hooks}
%files gdm-hooks
%attr(0700, gdm, gdm) %dir %{_localstatedir}/lib/gdm/.pulse
%attr(0600, gdm, gdm) %{_localstatedir}/lib/gdm/.pulse/default.pa
%endif

%changelog
%autochangelog
