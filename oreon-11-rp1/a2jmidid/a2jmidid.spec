%global source0_hash 2828d283e0c9a65f0683881f09676c8c35c45c97a8a56cf77b43b4ef0231df06

Summary:	Daemon for exposing ALSA sequencer applications in JACK MIDI system
Name:		a2jmidid
Version:	9
Release:	20%{?dist}
URL:		https://github.com/linuxaudio/a2jmidid
Source0:	https://github.com/linuxaudio/a2jmidid/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Backported from upstream
Patch0:		%{name}-man.patch
Patch1:		%{name}-portname.patch
Patch2:		%{name}-add-riscv64-support.patch

# a2jmidi_bridge.c and j2amidi_bridge.c are GPLv2+
# The rest is GPLv2
# Automatically converted from old format: GPLv2 and GPLv2+ - review is highly recommended.
License:	GPL-2.0-only AND GPL-2.0-or-later

BuildRequires:	alsa-lib-devel
BuildRequires:	dbus-devel
BuildRequires:	gcc
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires:	pipewire-jack-audio-connection-kit-devel
%else
BuildRequires:	jack-audio-connection-kit-devel
%endif
BuildRequires:	meson
Requires:	dbus
Requires:	python3

%description
a2jmidid is a project that aims to ease usage of legacy ALSA sequencer
applications, in a JACK MIDI enabled system. There are two ways to use legacy
ALSA sequencer applications in JACK MIDI system.

The first approach is to use automatic bridging. For every ALSA sequencer port
you get one JACK MIDI port. If ALSA sequencer port is both input and output
one, you get two JACK MIDI ports, one input and output.

The second approach is to static bridges. You start application that creates
one ALSA sequencer port and one JACK MIDI port. Such bridge is unidirectional.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Fix Python shebangs
sed -i 's|^#!/usr/bin/env python3|#!/usr/bin/python3|' a2j_control

%build
%meson
%meson_build

%install
%meson_install

%files
%doc AUTHORS.rst README.rst CHANGELOG.rst
%license LICENSE
%{_bindir}/a2j
%{_bindir}/%{name}
%{_bindir}/a2j_control
%{_bindir}/a2jmidi_bridge
%{_bindir}/j2amidi_bridge
%{_datadir}/dbus-1/services/org.gna.home.a2jmidid.service
%{_mandir}/man1/a2j*
%{_mandir}/man1/j2a*

%changelog
%autochangelog
