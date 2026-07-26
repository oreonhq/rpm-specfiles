%global source0_hash a34575fc2979b080bdfe07d744e28c5d11dcfba4004592856d723b482ff80de5

Summary:  Alsa Modular Synth, a realtime modular synthesizer
Name:     ams
Version:  2.2.1
Release:  10%{?dist}
URL:      http://alsamodular.sourceforge.net
Source0:  http://downloads.sourceforge.net/project/alsamodular/alsamodular/%{version}/%{name}-%{version}.tar.xz
Source1:  ams.desktop
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:  GPL-2.0-or-later

Requires: ladspa-cmt-plugins 
Requires: ladspa-swh-plugins 
Requires: ladspa-vco-plugins 
Requires: ladspa-rev-plugins 
Requires: ladspa-mcp-plugins

BuildRequires: gcc-c++
BuildRequires: desktop-file-utils alsa-lib-devel zita-alsa-pcmi-devel
BuildRequires: jack-audio-connection-kit-devel ladspa-devel
BuildRequires: fftw3-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-linguist
BuildRequires: make

%description
AlsaModularSynth is a realtime modular synthesizer and effect
processor. It features MIDI controlled modular software synthesis,
realtime effect processing with capture, full control of all synthesis
and effect parameters via MIDI, integrated LADSPA Browser with search
capability and JACK Support.

NOTE: Example files are in /usr/share/ams

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure --with-ladspa-path=%{_libdir}/ladspa
%make_build

%install
%make_install
chmod 755 %{buildroot}%{_bindir}/%{name}

# desktop categories
BASE="Application AudioVideo Audio"
XTRA="X-MIDI X-Jack X-Synthesis Midi"

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications    \
  `for c in ${BASE} ${XTRA} ; do echo "--add-category $c " ; done` \
  %{SOURCE1}

%files
%doc AUTHORS NEWS README THANKS ChangeLog
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}*
%{_datadir}/pixmaps/%{name}*

%changelog
%autochangelog
