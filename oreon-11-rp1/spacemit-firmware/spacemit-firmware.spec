%global source1_hash 43b0f671f9b5c17dd5977fe7584974a4481a14a677afd9b36aee6612c2c7fcc0
%global source0_hash c01fe09c31cadbdbe27d2f41ff851a532cfcf7270aaa1c98dd07a46787c07861
%define __strip /bin/true
Name:           spacemit-firmware
Version:        20240829
Release:        1%{?dist}
Summary:        SpacemiT firmware
License:        LicenseRef-Fedora-Firmware
URL:            https://bianbu-linux.spacemit.com/en/faqs/
Source0:        https://gitee.com/bianbu-linux/buildroot-ext/raw/bl-v2.0.y/board/spacemit/k1/target_overlay/lib/firmware/esos.elf
Source1:        https://gitee.com/bianbu-linux/buildroot-ext/raw/k1-bl-v2.2.y/board/spacemit/k1/target_overlay/lib/firmware/LICENSE.spacemit_esos
Source2:        spacemit-firmware.conf
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
# /oreon:deps
%description
SpacemiT firmware for the internal MCU on their X60 series SOC's
and eventually other chips

%package dracut
Requires: spacemit-firmware
Summary: A dracut.conf.d file for spacemit-firmware
%description dracut
Provides /etc/dracut.cond.d/spacemit-firmware.conf to ensure the
spacemit firmware is included in the initramfs

%prep

cp -av %{SOURCE1} .

%build

%install
install -D -m644 %{SOURCE0} %{buildroot}/lib/firmware/esos.elf
install -D -m644 %{SOURCE2} %{buildroot}%{_sysconfdir}/dracut.conf.d/spacemit-firmware.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n spacemit-firmware-dracut -f %{oreon_filedir}/spacemit-firmware-dracut.list

%changelog

%autochangelog
