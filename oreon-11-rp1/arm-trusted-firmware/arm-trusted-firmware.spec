%global source0_hash 67b772aaa58218712c062ccd103f1d53cf74d9543e251f20ac037a6dbf821a10
%global lts 1
%global debug_package %{nil}
%global pname trusted-firmware-a
%bcond_with cross
Name:    arm-trusted-firmware
Version: 2.15.0
Release:        1%{?dist}
Summary:        ARM Trusted Firmware
License: BSD-3-clause
URL:     https://github.com/TrustedFirmware-A/trusted-firmware-a
Source0:        https://github.com/TrustedFirmware-A/%{pname}/archive/v%{version}.tar.gz#/%{pname}-lts-v%{version}.tar.gz
Source1: aarch64-bl31
Patch1:  0001-fix-rk3576-shorten-names-to-fit-into-the-allocated-s.patch
%if %{with cross}
%define cross_compile aarch64-linux-gnu-
%else
%define cross_compile %{nil}
%endif
# oreon:deps
BuildRequires:  dtc
BuildRequires:  gcc
BuildRequires:  gcc-arm-linux-gnu
BuildRequires:  openssl-devel
# /oreon:deps
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
for soc in $(cat aarch64-bl31)
do
 for file in bl31.bin bl1.bin fip.bin
 do
  if [ -f build/$(echo $soc)/release/$(echo $file) ]; then
    install -pD -m 0644 build/$(echo $soc)/release/$(echo $file) %{buildroot}%{_datadir}/%{name}/$(echo $soc)/$(echo $file)
  elif [ $(echo $soc) = "k3" ]; then
    for board in generic j784s4 lite
    do
      if [ -f build/$(echo $soc)//$(echo $board)/release/$(echo $file) ]; then
        install -pD -m 0644 build/$(echo $soc)/$(echo $board)/release/$(echo $file) %{buildroot}%{_datadir}/%{name}/$(echo $soc)-$(echo $board)/$(echo $file)
      fi
    done
  fi
 done
done
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
