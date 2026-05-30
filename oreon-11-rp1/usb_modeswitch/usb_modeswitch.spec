%global source0_hash f7abd337784a9d1bd39cb8a587518aff6f2a43d916145eafd80b1b8b7146db66

%define source_name usb-modeswitch

Name:       usb_modeswitch
Version:    2.6.2
Release:    5%{?dist}
Summary:    USB Modeswitch gets mobile broadband cards in operational mode
Summary(de):    USB Modeswitch aktiviert UMTS-Karten
License:    GPL-2.0-or-later
URL:        http://www.draisberghof.de/usb_modeswitch/

Source0:        http://www.draisberghof.de/%{name}/%{source_name}-%{version}.tar.bz2
Source1:    http://www.draisberghof.de/usb_modeswitch/device_reference.txt

# Submitted upstream (2014-11-24)
Patch0: device_reference-utf8.patch
# Not submitted upstream due to lack of courage
Patch1: usb_modeswitch-2.6.2-SIGTERM.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libusbx-devel
# "tcl" or "jimsh"), use the light-weight installation:
#BuildRequires: jimtcl-devel
BuildRequires:  systemd
Requires:   usb_modeswitch-data >= 20121109
Requires:   systemd

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{source_name}-%{version}
cp -f %{SOURCE1} device_reference.txt

%patch 0 -p0
%patch 1 -p1


%build
%{set_build_flags}
# this will require jimtcl-devel
#make_build all-with-dynlink-dispatcher
%make_build


%install
mkdir -p %{buildroot}%{_unitdir}
%make_install \
    SYSDIR=%{buildroot}%{_unitdir} \
    SBINDIR=%{buildroot}%{_sbindir} \
    UDEVDIR=%{buildroot}%{_prefix}/lib/udev


%files
%{_sbindir}/usb_modeswitch
%{_sbindir}/usb_modeswitch_dispatcher
%{_mandir}/man1/usb_modeswitch.1.gz
%{_mandir}/man1/usb_modeswitch_dispatcher.1.gz
%{_prefix}/lib/udev/usb_modeswitch
%{_unitdir}/usb_modeswitch@.service
%config(noreplace) %{_sysconfdir}/usb_modeswitch.conf
%doc README ChangeLog device_reference.txt
%license COPYING


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.6.2-5
- Prepare for Oreon 11 (RP1)
