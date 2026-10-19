%global source0_hash a0b8bd8193d96853d2876c552b3b2bdf46bd1258fffc9ac598acc67eb73b56d5
%global gittag 1.10.2
Name:           tlp
Version:        1.10.2
Release:        1%{?dist}
Summary:        Optimize laptop battery life
License:        GPL-2.0-or-later
URL:            https://linrunner.de/tlp
Source0:        https://github.com/linrunner/TLP/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         0000-license-wrong-address.patch
Requires:       ethtool
Requires:       hdparm
Requires:       iw
Requires:       rfkill
Requires:       systemd
Requires:       udev
Requires:       usbutils
Requires:       pciutils
Recommends:     kernel-tools
Recommends:     smartmontools
Conflicts:      %{_sbindir}/laptop_mode
BuildArch:      noarch
# oreon:deps
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  systemd
# /oreon:deps
%description
TLP is a feature-rich command-line utility, saving laptop battery power
without the need to delve deeper into technical details.

TLP’s default settings are already optimized for battery life and implement
Powertop’s recommendations out of the box. Moreover TLP is highly
customizable to fulfill specific user requirements.

Settings are organized into two profiles, allowing to adjust between
savings and performance independently for battery (BAT) and AC operation.
In addition TLP can enable or disable Bluetooth, NFC, Wi-Fi and WWAN radio
devices on boot.

For ThinkPads and selected other laptops it provides a unified way
to configure charge thresholds and re-calibrate the battery.

%package rdw
Summary:        Radio device wizard for TLP
Requires:       NetworkManager >= 1.20
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description rdw
Radio device wizard is an add-on to TLP. It provides event based
switching of Bluetooth, NFC, Wi-Fi and WWAN radio devices on:
 - network connect/disconnect
 - dock/undock

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n TLP-%{gittag}

%build

%make_build
%install
%make_install \
  TLP_SDSL=%{_unitdir}/../system-sleep \
  TLP_NO_INIT=1 \
  TLP_WITH_ELOGIND=0 \
  TLP_SYSD=%{_unitdir} \
  TLP_ULIB=%{_udevrulesdir}/.. \
  TLP_SBIN=%{_bindir}
make install-man DESTDIR=%{buildroot}
make install-man-rdw DESTDIR=%{buildroot}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet \
  %{buildroot}/%{_datadir}/metainfo/*.xml
%post

%systemd_post tlp.service
if [ $1 -eq 2 ] ; then
    systemctl unmask systemd-rfkill.service
    systemctl unmask power-profiles-daemon.service
fi
%preun

%systemd_preun tlp.service
%postun

%systemd_postun_with_restart tlp.service
%files -f %{oreon_filedir}/main.list
%files -n tlp-rdw -f %{oreon_filedir}/tlp-rdw.list

%changelog

%autochangelog
