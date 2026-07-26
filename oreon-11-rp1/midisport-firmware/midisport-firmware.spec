%global source0_hash 2aa82ef0bf26647fbdda4c2e9ed0033b41bd0f1b4020b87fa073e4462a048b2d

Name:		midisport-firmware
Version:	1.2
Release:	38%{dist}
Summary:	Firmware for the M-Audio/Midiman USB MIDI and Audio devices
License:	LicenseRef-Fedora-Firmware
URL:		http://usb-midi-fw.sourceforge.net/
Source0:	http://downloads.sourceforge.net/usb-midi-fw/midisport-firmware-%{version}.tar.gz
Patch0:		midisport-firmware-1.2-udev-attrs.patch
BuildArch:	noarch
Requires:	fxload
BuildRequires:	systemd

%description
This package contains the firmware for M-Audio/Midiman USB MIDI & Audio devices.

Supported devices:
 - MidiSport 1x1
 - MidiSport 2x2
 - MidiSport 4x4
 - MidiSport 8x8
 - MidiSport Uno
 - Keystation
 - Oxygen
 - Radium

(You do not need a firmware download for the USB Audio Quattro, Duo, or
MidiSport 2x4.)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
sed -i -e 's|@fxload@|/sbin/fxload|g' -e 's|@firmwaredir@|/lib/firmware|g' 42-midisport-firmware.rules.in

%install
mkdir -p $RPM_BUILD_ROOT/lib/firmware
install -pm 0644 *.ihx $RPM_BUILD_ROOT/lib/firmware

mkdir -p $RPM_BUILD_ROOT%{_udevrulesdir}
install -pm 0644 42-midisport-firmware.rules.in $RPM_BUILD_ROOT/%{_udevrulesdir}/42-midisport-firmware.rules

%files
%doc LICENSE README Changelog
/lib/firmware/MidiSport1x1.ihx
/lib/firmware/MidiSport2x2.ihx
/lib/firmware/MidiSport4x4.ihx
/lib/firmware/MidiSportKS.ihx
/lib/firmware/MidiSportLoader.ihx
/lib/firmware/MidiSport8x8-2.10.ihx
/lib/firmware/MidiSport8x8-2.21.ihx
%config %{_udevrulesdir}/42-midisport-firmware.rules

%changelog
%autochangelog
