%global source0_hash d34513b965fb685d032abb4c8b0cf61d116413a3fbda110e0b915e3709b4bae5

%global debug_package %{nil}
%global __strip /bin/true

# Tarfile created using git 		
# git clone https://github.com/raspberrypi/firmware.git
# cd firmware/boot
# tar cJvf ../bcm283x-firmware-%{gitshort}.tar.xz *bin *dat *elf LICENCE.broadcom COPYING.linux overlays/
%define gitshort 6bc3936

Name:          bcm283x-firmware
Version:       20260408
Release:       1.%{gitshort}%{?dist}
Summary:       Firmware for the Broadcom bcm283x/bcm271x used in the Raspberry Pi
# see LICENSE.broadcom
# DT Overlays covered under Linux Kernel GPLv2
SourceLicense: GPL-2.0-only WITH Linux-syscall-note AND LicenseRef-Fedora-Firmware
License:       LicenseRef-Fedora-Firmware
URL:           https://github.com/raspberrypi/

ExclusiveArch: aarch64

BuildRequires: efi-filesystem
BuildRequires: efi-srpm-macros
BuildRequires: systemd-rpm-macros
Requires:      efi-filesystem
Requires:      bcm283x-overlays
Requires:      bcm2835-firmware
Requires:      bcm2711-firmware
Requires:      bcm2712-firmware

Source0:       %{name}-%{gitshort}.tar.xz
# tar cJvf bcm-dtbs-v<ker-ver>.tar.xz bcm271*dtb
Source1:       bcm-dtbs-v6.18.21.tar.xz
Source2:       config.txt
Source3:       nortc-time.service
Source4:       cma.dtbo

%description
Firmware for the Broadcom bcm283x and bcm2711 series of systems on a chip as
shipped in the Raspberry Pi series of devices.

%package -n bcm283x-overlays
Summary:       HAT Overlays for the Raspberry Pi
License:       GPL-2.0-only WITH Linux-syscall-note

%description -n bcm283x-overlays
Hardware Attached Ontop (HATs) overlays for the Raspberry Pi series of devices.

%package -n bcm2835-firmware
Summary:       Firmware for the Raspberry Pi 2, 3, 3+ and CM3
Requires:      efi-filesystem
Requires:      bcm283x-firmware
Requires:      bcm283x-overlays

%description -n bcm2835-firmware
Firmware for the Raspberry Pi 3 series (3, 3+ and CM3) and Zero2W

%package -n bcm2711-firmware
Summary:       Firmware for the Raspberry Pi 4 series of devices
Requires:      efi-filesystem
Requires:      bcm283x-firmware
Requires:      bcm283x-overlays

%description -n bcm2711-firmware
Firmware for the Raspberry Pi 4 series of devices such as the
Raspberry Pi 4B, 400 and CM4.

%package -n bcm2712-firmware
Summary:       Firmware for the Raspberry Pi 5 series of devices
Requires:      efi-filesystem
Requires:      bcm283x-firmware
Requires:      bcm283x-overlays

%description -n bcm2712-firmware
Firmware for the Raspberry Pi 5 series of devices such as the
Raspberry Pi 5B, 500 and CM5.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{gitshort} -c %{name}-%{gitshort}
cp %{SOURCE4} overlays
tar xf %{SOURCE1}

%build

%install
mkdir -p %{buildroot}%{efi_esp_root}/overlays
install -p %{SOURCE2} %{buildroot}%{efi_esp_root}/config.txt
mkdir -p %{buildroot}%{_unitdir}/
install -p %{SOURCE3} %{buildroot}%{_unitdir}/nortc-time.service
install -p *bin %{buildroot}%{efi_esp_root}
install -p *dat %{buildroot}%{efi_esp_root}
install -p *elf %{buildroot}%{efi_esp_root}
install -p bcm2710*dtb %{buildroot}%{efi_esp_root}
install -p bcm2711*dtb %{buildroot}%{efi_esp_root}
install -p bcm2712*dtb %{buildroot}%{efi_esp_root}
install -p overlays/README %{buildroot}%{efi_esp_root}/overlays
install -p overlays/*.dtbo %{buildroot}%{efi_esp_root}/overlays

%files
%license LICENCE.broadcom COPYING.linux
%config(noreplace) %{efi_esp_root}/config.txt
%{efi_esp_root}/bootcode.bin
%{_unitdir}/nortc-time.service
%dir %{efi_esp_root}/overlays
%{efi_esp_root}/overlays/cma.dtbo

%files -n bcm283x-overlays
# DT Overlays covered under Linux Kernel GPLv2
%license COPYING.linux
%dir %{efi_esp_root}/overlays
%{efi_esp_root}/overlays/*

%files -n bcm2835-firmware
%license LICENCE.broadcom
%{efi_esp_root}/bcm2710*
%{efi_esp_root}/fixup[_.]*
%{efi_esp_root}/start[_.]*

%files -n bcm2711-firmware
%license LICENCE.broadcom
%{efi_esp_root}/bcm2711*
%{efi_esp_root}/fixup4*
%{efi_esp_root}/start4*

%files -n bcm2712-firmware
%license LICENCE.broadcom
%{efi_esp_root}/bcm2712*

%changelog
%autochangelog
