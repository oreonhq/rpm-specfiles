%global source0_hash 1de1f220ebbf3eaed7b7d75c402ec0dbf799c73dee9ab6635cf106bfa8b117ab
Name:           asahi-scripts
Version:        20250713
Release:        1%{?dist}
Summary:        Miscellaneous admin scripts for Asahi Linux
License:        MIT
URL:            https://github.com/AsahiLinux/asahi-scripts
Source0:        https://github.com/AsahiLinux/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source2:        15-update-m1n1.install
Patch01:        0001-update-m1n1-Expand-DTBS-if-it-is-a-directory.patch
Patch02:        0002-fedora-update-m1n1-handle-dangling-boot-dtb-symlinks.patch
BuildArch:      noarch
Requires:       bash
Requires:       coreutils
Requires:       grep
Requires:       sed
Requires:       systemd-udev
Requires:       util-linux-core
# oreon:deps
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
This package contains miscellaneous admin scripts for the Asahi Linux reference
distro.

%package -n     asahi-fwupdate
Summary:        Asahi Linux firmware extractor
Requires:       %{name} = %{version}-%{release}
Requires:       python3-asahi_firmware >= 0.5.4
%description -n asahi-fwupdate
Asahi Linux firmware updater.

%package -n     dracut-asahi
Summary:        Dracut config for Apple Silicon Macs
Requires:       dracut
Requires:       linux-firmware-vendor = %{version}-%{release}
%description -n dracut-asahi
Dracut config for Apple Silicon Macs.

%package -n     linux-firmware-vendor
Summary:        Ensure /lib/firmware/vendor exists for firmware handoff
Requires:       linux-firmware
%description -n linux-firmware-vendor
This package ensures /lib/firmware/vendor exists so that firmware can be handed
over properly from the initramfs.

%package -n     update-m1n1
Summary:        Keep m1n1 up to date
Requires:       %{name} = %{version}-%{release}
Requires:       bash
Requires:       gzip
Requires:       m1n1
Requires:       uboot-images-armv8
Requires:       grubby
%description -n update-m1n1
Keep m1n1 up to date on Apple Silicon systems.

%package -n     asahi-battery
Summary:        Asahi Linux battery charge control scripts
Requires:       %{name} = %{version}-%{release}
Requires:       systemd
Requires:       systemd-udev
%description -n asahi-battery
Asahi Linux battery charge control scripts restore charge_control_end_threshold
on system start.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%make_install install-fedora \
  PREFIX="%{_prefix}" \
  BIN_DIR="%{_sbindir}" \
  CONFIG_DIR="%{_sysconfdir}/sysconfig"
install -Ddpm0755 %{buildroot}%{_prefix}/lib/firmware/vendor
install -Dpm0644 %SOURCE1 %{buildroot}%{_sysconfdir}/sysconfig/update-m1n1
install -Dpm0755 -t %{buildroot}%{_kernel_install_dir} %{SOURCE2}
%transfiletriggerin -n asahi-fwupdate -- %{_sbindir}/asahi-fwupdate %{_bindir}/asahi-fwextract
%{_sbindir}/asahi-fwupdate || :
%transfiletriggerin -n asahi-fwupdate -- /usr/lib/python
grep -q 'asahi_firmware' && %{_sbindir}/asahi-fwupdate || :
%transfiletriggerin -n update-m1n1 -- /usr/lib/m1n1 /usr/lib64/m1n1 /usr/share/uboot/apple_m1 /etc/m1n1.conf
%{_sbindir}/update-m1n1 || :
%oreon_autofiles asahi-fwupdate usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles dracut-asahi usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles linux-firmware-vendor usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles update-m1n1 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles asahi-battery usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n asahi-fwupdate -f %{oreon_filedir}/asahi-fwupdate.list
%files -n dracut-asahi -f %{oreon_filedir}/dracut-asahi.list
%files -n linux-firmware-vendor -f %{oreon_filedir}/linux-firmware-vendor.list
%files -n update-m1n1 -f %{oreon_filedir}/update-m1n1.list
%files -n asahi-battery -f %{oreon_filedir}/asahi-battery.list

%changelog

%autochangelog
