%global source0_hash 9400e16c45bfa45f15585b2c933b86c449e7de05def0ecaaa62a4f38973a3a45

# Binaries not used in standard manner so debuginfo is useless
%global debug_package %{nil}

Name:      optee_os
Version:   4.9.0
Release:   2%{?dist}
Summary:   Trusted side of the TEE

# The TEE core of optee_os is provided under the BSD 2-Clause license. But
# there are also other software such as libraries included in optee_os.
# This "other" software will have different licenses that are compatible
# with BSD 2-Clause (i.e., non-contaminating licenses unlike GPL-v2 for example).
License:   BSD-2-Clause AND Apache-2.0 AND (BSD-2-Clause AND BSD-3-Clause) AND (BSD-2-Clause AND MIT) AND (BSD-2-Clause AND MIT-CMU) AND BSD-3-Clause AND BSD-Source-Code AND BSL-1.0 AND (GPL-2.0 OR BSD-2-Clause) AND (GPL-2.0-or-later OR BSD-2-Clause) AND (GPL-2.0 or BSD-3-Clause) AND (GPL-2.0+ or BSD-3-Clause) AND (GPL-2.0 OR MIT) AND (GPL-2.0+ OR MIT) AND ISC AND MIT AND Unlicense AND (Unlicense AND BSD-2-Clause) AND Zlib

URL:       https://www.trustedfirmware.org
Source0:   https://github.com/OP-TEE/optee_os/archive/%{version}/%{name}-%{version}.tar.gz
Source1:   aarch64-platforms

BuildRequires: dtc
BuildRequires: gcc
BuildRequires: gcc-arm-linux-gnu
BuildRequires: make
BuildRequires: python3-cryptography
BuildRequires: python3-pyelftools

ExclusiveArch: aarch64

%description
OP-TEE is a Trusted Execution Environment (TEE) designed as companion to a
non-secure Linux kernel running on Arm; Cortex-A cores using the TrustZone
technology. OP-TEE implements TEE Internal Core API v1.1.x which is the API
exposed to Trusted Applications.

Note: the contents of this package are generally just consumed by bootloaders
such as u-boot. As such the binaries aren't of general interest to users.

%package     -n optee-os-firmware-armv8
Summary:     OP-TEE Firmware for ARMv8-A
BuildArch:   noarch

%description -n optee-os-firmware-armv8
OP-TEE firmware for various ARMv8-A SoCs.

Note: the contents of this package are generally just consumed by bootloaders
such as u-boot. As such the binaries aren't of general interest to users.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1

cp %SOURCE1 .

%build
%undefine _auto_set_build_flags

for platform in $(cat aarch64-platforms)
do
make HOSTCC="gcc $RPM_OPT_FLAGS" CROSS_COMPILE64="" CROSS_COMPILE=arm-linux-gnu- PLATFORM="$(echo $platform)" CFG_ARM64_core=y O=builds/$(echo $platform)
done

%install
mkdir -p %{buildroot}%{_datadir}/%{name}

for platform in $(cat aarch64-platforms)
do
  mkdir -p %{buildroot}%{_datadir}/%{name}/$(echo $platform)/
  install -p -m 0644 builds/$(echo $platform)/core/tee-pager_v2.bin  /%{buildroot}%{_datadir}/%{name}/$(echo $platform)/
  # rockchip expects the .elf
  install -p -m 0644 builds/$(echo $platform)/core/tee.elf /%{buildroot}%{_datadir}/%{name}/$(echo $platform)
done

%files -n optee-os-firmware-armv8
%license LICENSE
%doc README.md
%{_datadir}/%{name}

%changelog
%autochangelog
