%global source1_hash 846b45a82a31c9755ab86d9c051e706aff445e1e793575b7ae195a4edeb4d594
%global source0_hash f7abd337784a9d1bd39cb8a587518aff6f2a43d916145eafd80b1b8b7146db66
%define source_name usb-modeswitch
Name:       usb_modeswitch
Version:    2.6.2
Release:        1%{?dist}
Summary:        USB Modeswitch gets mobile broadband cards in operational mode
Summary(de):    USB Modeswitch aktiviert UMTS-Karten
License:    GPL-2.0-or-later
URL:        http://www.draisberghof.de/usb_modeswitch/
Source0:        http://www.draisberghof.de/%{name}/%{source_name}-%{version}.tar.bz2
Source1:    https://www.draisberghof.de/usb_modeswitch/device_reference.txt
Patch0: device_reference-utf8.patch
Patch1: usb_modeswitch-2.6.2-SIGTERM.patch
Requires:   usb_modeswitch-data >= 20121109
Requires:   systemd
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libusbx-devel
BuildRequires:  make
BuildRequires:  systemd
# /oreon:deps
%description
USB Modeswitch brings up your datacard into operational mode. When plugged
in they identify themselves as cdrom and present some non-Linux compatible
installation files. This tool deactivates this cdrom-device and enables
the real communication device. It supports most devices built and
sold by Huawei, T-Mobile, Vodafone, Option, ZTE, Novatel.

%description    -l de
USB Modeswitch deaktiviert die CDROM-Emulation einiger UMTS-Karten.
Dadurch erkennt Linux die Datenkarte und kann damit Internet-
Verbindungen aufbauen. Die gängigen Karten von Huawei, T-Mobile,
Vodafone, Option, ZTE und Novatell werden unterstützt.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{source_name}-%{version}
cp -f %{SOURCE1} device_reference.txt

%patch 0 -p0
%patch 1 -p1

%build

%{set_build_flags}
%make_build
%install
mkdir -p %{buildroot}%{_unitdir}
%make_install \
    SYSDIR=%{buildroot}%{_unitdir} \
    SBINDIR=%{buildroot}%{_sbindir} \
    UDEVDIR=%{buildroot}%{_prefix}/lib/udev
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.6.2-5
- Prepare for Oreon 11 (RP1)
