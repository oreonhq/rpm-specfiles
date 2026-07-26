%global source0_hash 22a3a26d3dbe4bf215aa33c0fd4a79c088549328477840d00e72e50c6e807e10

Summary:          An arpeggiator, sequencer and MIDI LFO for ALSA
Name:             qmidiarp
Version:          0.6.5
Release:          22%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:          GPL-2.0-or-later
URL:              http://sourceforge.net/projects/qmidiarp 
Source0:          http://downloads.sourceforge.net/qmidiarp/files/%{name}-%{version}.tar.bz2
BuildRequires: make
BuildRequires:    desktop-file-utils
BuildRequires:    alsa-lib-devel
BuildRequires:    gcc-c++
BuildRequires:    qt5-qtbase-devel
BuildRequires:    qt5-linguist
BuildRequires:    liblo-devel
BuildRequires:    jack-audio-connection-kit-devel
BuildRequires:    lv2-devel
Requires:         hicolor-icon-theme

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

%files 
%doc AUTHORS ChangeLog README NEWS
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/de/man1/%{name}.1.*
%{_mandir}/fr/man1/%{name}.1.*
%{_mandir}/man1/%{name}.1.*
%{_datadir}/metainfo/%{name}*

%files -n lv2-qmidiarp
%{_libdir}/lv2/qmidiarp*

%changelog
%autochangelog
