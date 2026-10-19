%global source0_hash a35114400f29a63e8c509a5d630abfccdfd56ec45396f102e551d1bd10d1d7b0
Summary:        An arpeggiator, sequencer and MIDI LFO for ALSA
Name:             qmidiarp
Version:          0.7.5
Release:        1%{?dist}
License:          GPL-2.0-or-later
URL:              http://sourceforge.net/projects/qmidiarp 
Source0:        http://downloads.sourceforge.net/qmidiarp/files/%{name}-%{version}.tar.bz2
Requires:         hicolor-icon-theme
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  liblo-devel
BuildRequires:  lv2-devel
BuildRequires:  make
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
# /oreon:deps
%description
QMidiArp is a MIDI phrase generator and controller LFO for the ALSA sequencer. 
It can run multiple synchronized arpeggiators, LFOs and step sequencers. 
QMidiArp has been growing since June 2009 on top of Matthias Nagorni's original 
arp idea.  

%package -n lv2-qmidiarp 
Summary:          LV2 plugins of the QMidiArp MIDI arpeggiator, sequencer and LFO
%description -n lv2-qmidiarp
lv2-qmidiarp contains LV2 versions of the QMidiArp's LFO, ARP and sequencer

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q 

# Fix encoding issues
for file in ChangeLog AUTHORS README COPYING NEWS; do
   sed 's|\r||' $file > $file.tmp
   iconv -f ISO-8859-1 -t UTF8 $file.tmp > $file.tmp2
   touch -r $file $file.tmp2
   mv -f $file.tmp2 $file
done

%build

%configure --enable-nsm 
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%oreon_autofiles lv2-qmidiarp usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n lv2-qmidiarp -f %{oreon_filedir}/lv2-qmidiarp.list

%changelog

%autochangelog
