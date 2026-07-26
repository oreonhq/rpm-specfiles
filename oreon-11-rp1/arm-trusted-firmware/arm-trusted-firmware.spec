%global source0_hash f70d2eb40c2d9912562ef15d450e03726b95abd6d16db4d46cd923ba5a029646

#global candidate rc1
# LTS has slightly adjusted naming
%global lts 1

# Binaries not used in standard manner so debuginfo is useless
%global debug_package %{nil}

# Project sub name
%global pname trusted-firmware-a

# This is a noarch package that can be built on any host architecture.
# The default configuration is to allow building only on aarch64 via
# "ExclusiveArch: aarch64".  Use "--with cross" to enable building on
# any host.
%bcond_with cross

Name:    arm-trusted-firmware
Version: 2.14.1
Release: 2%{?candidate:.%{candidate}}%{?dist}
Summary: ARM Trusted Firmware
License: BSD-3-clause
URL:     https://github.com/TrustedFirmware-A/trusted-firmware-a
Source0: %{url}/archive/v%{version}%{?candidate:-%{candidate}}.tar.gz#/%{pname}%{?lts:-lts}-v%{version}%{?candidate:-%{candidate}}.tar.gz
Source1: aarch64-bl31
Patch1:  0001-fix-rk3576-shorten-names-to-fit-into-the-allocated-s.patch

%if %{with cross}
BuildRequires: gcc-aarch64-linux-gnu
%define cross_compile aarch64-linux-gnu-
%else
%define cross_compile %{nil}
%endif

BuildRequires: dtc
BuildRequires: gcc
# This is needed for rk3399 which while aarch64 has an onboard Cortex-M0 base PMU
BuildRequires: gcc-arm-linux-gnu
BuildRequires: openssl-devel

%description
ARM Trusted firmware is a reference implementation of secure world software for
ARMv8-A including Exception Level 3 (EL3) software. It provides a number of
standard ARM interfaces like Power State Coordination (PSCI), Trusted Board
Boot Requirements (TBBR) and Secure Monitor.

Note: the contents of this package are generally just consumed by bootloaders
such as u-boot. As such the binaries aren't of general interest to users.

%ifarch aarch64
%package     -n arm-trusted-firmware-armv8
Summary:     ARM Trusted Firmware for ARMv8-A
BuildArch:   noarch

%description -n arm-trusted-firmware-armv8
ARM Trusted Firmware binaries for various  ARMv8-A SoCs.

Note: the contents of this package are generally just consumed by bootloaders
such as u-boot. As such the binaries aren't of general interest to users.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pname}%{?lts:-lts}-v%{version}%{?candidate:-%{candidate}} -p1

cp %SOURCE1 .

%build

%undefine _auto_set_build_flags

export CC=gcc
export M0_CROSS_COMPILE=arm-linux-gnu-

%ifarch aarch64
for soc in $(cat aarch64-bl31)
do
# At the moment we're only making the secure firmware (bl31) (except qemu_sbsa)
case $(echo $soc) in
  "k3")
    make HOSTCC="gcc $RPM_OPT_FLAGS" CROSS_COMPILE="%{cross_compile}" PLAT=$(echo $soc) ENABLE_PIE=0 TARGET_BOARD=generic SPD=opteed bl31
    make HOSTCC="gcc $RPM_OPT_FLAGS" CROSS_COMPILE="%{cross_compile}" PLAT=$(echo $soc) ENABLE_PIE=0 TARGET_BOARD=j784s4 SPD=opteed K3_USART=0x8 bl31
    make HOSTCC="gcc $RPM_OPT_FLAGS" CROSS_COMPILE="%{cross_compile}" PLAT=$(echo $soc) ENABLE_PIE=0 TARGET_BOARD=lite SPD=opteed bl31
    ;;
  "qemu_sbsa")
    make HOSTCC="gcc $RPM_OPT_FLAGS" CROSS_COMPILE="%{cross_compile}" PLAT=$(echo $soc) all fip
    ;;
  *)
    make HOSTCC="gcc $RPM_OPT_FLAGS" CROSS_COMPILE="%{cross_compile}" PLAT=$(echo $soc) bl31
    ;;
esac
done
%endif

%install

%ifarch aarch64
mkdir -p %{buildroot}/%{_datadir}/%{name}

# At the moment we just support adding bl31.bin (except qemu_sbsa)
for soc in $(cat aarch64-bl31)
do
 for file in bl31.bin bl1.bin fip.bin
 do
  if [ -f build/$(echo $soc)/release/$(echo $file) ]; then
    install -pD -m 0644 build/$(echo $soc)/release/$(echo $file) %{buildroot}%{_datadir}/%{name}/$(echo $soc)/$(echo $file)
  elif [ $(echo $soc) = "k3" ]; then
    # TI K3 platforms have a different directory layout, binaries are in build/k3/$board directory
    for board in generic j784s4 lite
    do
      if [ -f build/$(echo $soc)//$(echo $board)/release/$(echo $file) ]; then
        install -pD -m 0644 build/$(echo $soc)/$(echo $board)/release/$(echo $file) %{buildroot}%{_datadir}/%{name}/$(echo $soc)-$(echo $board)/$(echo $file)
      fi
    done
  fi
 done
done

# Rockchips wants the bl31.elf, plus rk3399 wants power management co-processor bits
for soc in rk3399 rk3368 rk3328 rk3568 rk3576 rk3588
do
 for file in bl31/bl31.elf m0/rk3399m0.bin m0/rk3399m0.elf
 do
  if [ -f build/$(echo $soc)/release/$(echo $file) ]; then
    install -pD -m 0644 build/$(echo $soc)/release/$(echo $file) -t %{buildroot}/%{_datadir}/%{name}/$(echo $soc)/
  fi
 done
done
%endif

%ifarch aarch64
%files -n arm-trusted-firmware-armv8
%license license.rst
%doc readme.rst
%{_datadir}/%{name}
%endif

%changelog
%autochangelog
