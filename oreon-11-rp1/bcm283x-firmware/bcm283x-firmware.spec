%global source0_hash d34513b965fb685d032abb4c8b0cf61d116413a3fbda110e0b915e3709b4bae5
%global debug_package %{nil}
%global __strip /bin/true
%define gitshort 6bc3936
Name:          bcm283x-firmware
Version:       20260408
Release:        1%{?dist}
Summary:        Firmware for the Broadcom bcm283x/bcm271x used in the Raspberry Pi
SourceLicense: GPL-2.0-only WITH Linux-syscall-note AND LicenseRef-Fedora-Firmware
License:       LicenseRef-Fedora-Firmware
URL:           https://github.com/raspberrypi/
ExclusiveArch: aarch64
Requires:      efi-filesystem
Requires:      bcm283x-overlays
Requires:      bcm2835-firmware
Requires:      bcm2711-firmware
Requires:      bcm2712-firmware
Source0:        %{name}-%{gitshort}.tar.xz
Source1:       bcm-dtbs-v6.18.21.tar.xz
Source2:       config.txt
Source3:       nortc-time.service
Source4:       cma.dtbo
# oreon:deps
BuildRequires:  efi-filesystem
BuildRequires:  efi-srpm-macros
BuildRequires:  systemd-rpm-macros
# /oreon:deps
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
%oreon_autofiles bcm283x-overlays usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bcm2835-firmware usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bcm2711-firmware usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bcm2712-firmware usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n bcm283x-overlays -f %{oreon_filedir}/bcm283x-overlays.list
%files -n bcm2835-firmware -f %{oreon_filedir}/bcm2835-firmware.list
%files -n bcm2711-firmware -f %{oreon_filedir}/bcm2711-firmware.list
%files -n bcm2712-firmware -f %{oreon_filedir}/bcm2712-firmware.list

%changelog

%autochangelog
