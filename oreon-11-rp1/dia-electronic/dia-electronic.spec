%global source0_hash 8259a01a89265280d99b862d462b8e5a575bc3b6248fc5f93a3cc51fb8f3a148

%global dia_datadir %{_datadir}/dia
%global shapes electronic

Name:           dia-%{shapes}
Version:        0.1
Release:        31%{?dist}
Summary:        Dia Digital IC logic shapes

License:        GPL-2.0-or-later
URL:            http://dia-installer.de/shapes/electronic/index_en.html
Source0:        http://dia-installer.de/shapes/electronic/electronic.zip

Requires:       dia
BuildArch:      noarch

%description
The following shapes are included in the package:
 * Antenna
 * Bell
 * Button
 * Capacitor
 * Electrolytic capacitor
 * Crystal
 * Di-Gate
 * Diac
 * Engine
 * Headphone
 * Inverse diode
 * Schottky diode
 * Tunnel diode
 * Zenner diode
 * Inductor
 * LED display
 * Microphone
 * Photo-emiting part
 * Photosensitive part
 * Potenciometer
 * Ground
 * Contact
 * Contact Pair
 * IN Port
 * OUT Port
 * IN/OUT Port
 * Voltmeter
 * Ampermeter
 * Source or Meter
 * Current source
 * Substitute linearised source
 * Voltage source
 * Alternating voltage source
 * Direct voltage source
 * Bipolar transistor NPN
 * Bipolar transistor NPN
 * Bipolar transistor PNP
 * Bipolar transistor PNP
 * JFE transitor - N
 * JFE transistor - P
 * MISFE conducting transistor - N
 * MISFE conducting transistor - P
 * MISFE inducting transistor - N
 * MISFE inducting transistor - P
 * Single ..... transistor
 * Triac
 * Diode tyristor, blocking
 * Triode tyristor, blocking
 * Vacuum diode
 * Vacuum pentode
 * Vacuum triode
 * Linear variable part
 * Nonlinear variable part
 * Varicap

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{dia_datadir}/sheets
cp -p sheets/%{shapes}.sheet %{buildroot}%{dia_datadir}/sheets
cp -pr shapes %{buildroot}%{dia_datadir}

%files
%doc COPYING
%{dia_datadir}/sheets/%{shapes}.sheet
%{dia_datadir}/shapes/%{shapes}/

%changelog
%autochangelog
