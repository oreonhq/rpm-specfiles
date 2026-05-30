%global source0_hash 3f039b60791c21c7cb15c7986cac89650f076dc274798fa242231b910785eaf9

%global source_name	usb-modeswitch-data

Name:		usb_modeswitch-data
Version:	20191128
Release:	15%{?dist}
Summary:	USB Modeswitch gets mobile broadband cards in operational mode
Summary(de):	USB Modeswitch aktiviert UMTS-Karten
License:	GPL-2.0-or-later
URL:		http://www.draisberghof.de/usb_modeswitch/
Source0:        http://www.draisberghof.de/usb_modeswitch/%{source_name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires: make
BuildRequires:	systemd
Requires:	systemd
Requires:	usb_modeswitch >= 2.4.0


%description
USB Modeswitch brings up your datacard into operational mode. When plugged
in they identify themselves as cdrom and present some non-Linux compatible
installation files. This tool deactivates this cdrom-devices and enables
the real communication device. It supports most devices built and
sold by Huawei, T-Mobile, Vodafone, Option, ZTE, Novatel.

This package contains the data files needed for usb_modeswitch to function.

%description	-l de
USB Modeswitch deaktiviert die CDROM-Emulation einiger UMTS-Karten.
Dadurch erkennt Linux die Datenkarte und kann damit Internet-
Verbindungen aufbauen. Die gängigen Karten von Huawei, T-Mobile,
Vodafone, Option, ZTE und Novatell werden unterstützt.

Dieses Paket enthält die Dateien für usb_modeswitch benötigt 
um zu funktionieren.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{source_name}-%{version}

%build

%install
make install \
	DESTDIR=$RPM_BUILD_ROOT \
	RULESDIR=$RPM_BUILD_ROOT%{_udevrulesdir}

%post 
%udev_rules_update

%postun
%udev_rules_update

%files
%{_udevrulesdir}/40-usb_modeswitch.rules
%{_datadir}/usb_modeswitch
%license COPYING
%doc ChangeLog README REFERENCE

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20191128-15
- Import
