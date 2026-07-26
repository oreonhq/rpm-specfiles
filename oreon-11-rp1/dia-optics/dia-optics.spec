%global source0_hash 212d973aa0e342465842760b68542fdedf4aed167b29655fb26ac4bc1223983b

%global dia_datadir %{_datadir}/dia
%global shapes Optics

Name:           dia-optics
Version:        0.1
Release:        31%{?dist}
Summary:        Dia Optics shapes

License:        GPL-2.0-or-later
URL:            http://dia-installer.de/shapes/optics/index_en.html
Source0:        http://dia-installer.de/shapes/optics/optics.zip

Requires:       dia
BuildArch:      noarch

%description
The following shapes are included in the package:
 * Polarisation Controller
 * Directional Coupler
 * Tuneable Coupler
 * DFB Laser
 * Long Fibre
 * Detector
 * Osilloscope
 * Spectrum Analyser
 * Optical Isolator
 * EDFA
 * Variable Attenuator
 * MZ Modulator
 * Phase Modulator
 * Sine Wave Source
 * Square Wave Source
 * Long Period Grating
 * Light Beam
 * Wave

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
