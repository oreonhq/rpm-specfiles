%global source0_hash f80dcb757a623deda62200c08e0e1a88c76fb6b54964f31b35fa74da1c90ccc5
%global debug_package %{nil}
%global _firmwarepath	/usr/lib/firmware
%define _binaries_in_noarch_packages_terminate_build 0
Name:		linux-firmware
Version:	20260916
Release:        1%{?dist}
Summary:        Firmware files used by the Linux kernel
License:	GPL-1.0-or-later AND GPL-2.0-or-later AND MIT AND LicenseRef-Callaway-Redistributable-no-modification-permitted
URL:		http://www.kernel.org/
BuildArch:	noarch
Source0:        https://cdn.kernel.org/pub/linux/kernel/firmware/%{name}-%{version}.tar.xz
Requires:	linux-firmware-whence = %{version}-%{release}
Requires:	((linux-firmware = %{version}-%{release}) if linux-firmware)
Recommends:	qcom-wwan-firmware
Recommends:	amd-gpu-firmware
Recommends:	amd-ucode-firmware
Recommends:	atheros-firmware
Recommends:	brcmfmac-firmware
Recommends:	cirrus-audio-firmware
Recommends:	intel-audio-firmware
Recommends:	intel-gpu-firmware
Recommends:	mt7xxx-firmware
Recommends:	nvidia-gpu-firmware
Recommends:	nxpwireless-firmware
Recommends:	realtek-firmware
Recommends:	tiwilink-firmware
# oreon:deps
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  python3
# /oreon:deps
%description
This package includes firmware files required for some devices to
operate.

%package whence
Summary:	WHENCE License file
License:	GPL-1.0-or-later AND GPL-2.0-or-later AND MIT AND LicenseRef-Callaway-Redistributable-no-modification-permitted
%description whence
This package contains the WHENCE license file which documents the vendor license details.

# GPU firmwares
%package -n amd-gpu-firmware
Summary:	Firmware for AMD GPUs
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence = %{version}-%{release}
%description -n amd-gpu-firmware
Firmware for AMD amdgpu and radeon GPUs.

%package -n intel-gpu-firmware
Summary:	Firmware for Intel GPUs
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence = %{version}-%{release}
%description -n intel-gpu-firmware
Firmware for Intel GPUs including GuC (Graphics Microcontroller), HuC (HEVC/H.265
Microcontroller) and DMC (Display Microcontroller) firmware for Skylake and later
platforms.

%package -n nvidia-gpu-firmware
Summary:	Firmware for NVIDIA GPUs
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence = %{version}-%{release}
%description -n nvidia-gpu-firmware
Firmware for NVIDIA GPUs.

# Microcode updates
%package -n amd-ucode-firmware
Summary:	Microcode updates for AMD CPUs
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence = %{version}-%{release}
%description -n amd-ucode-firmware
Microcode updates for AMD CPUs, AMD SEV and AMD TEE.

# WiFi/Bluetooth/WWAN firmwares
%package -n atheros-firmware
Summary:	Firmware for Qualcomm Atheros WiFi/Bluetooth adapters
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence = %{version}-%{release}
%description -n atheros-firmware
Firmware for Qualcomm Atheros ath6k/ath9k/ath10k/ath11k WiFi adapters.

%package -n brcmfmac-firmware
Summary:	Firmware for Broadcom/Cypress brcmfmac WiFi/Bluetooth adapters
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence = %{version}-%{release}
%description -n brcmfmac-firmware
Firmware for Broadcom/Cypress brcmfmac WiFi/Bluetooth adapters.

%package -n iwlegacy-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 3945(A)BG and 4965AGN adapters
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence = %{version}-%{release}
%description -n iwlegacy-firmware
This package contains the firmware required by the iwlegacy driver
for Linux. This includes the 3945(A)BG and 4965AGN WiFi NICs. Usage
of the firmware is subject to the terms and conditions contained
inside the provided LICENSE file. Please read it carefully.

%package -n iwlwifi-dvm-firmware
Summary:	DVM Firmware for Intel(R) Wireless WiFi adapters
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence = %{version}-%{release}
%description -n iwlwifi-dvm-firmware
This package contains the firmware required by the iwlwifi driver
for Linux built with DVM firmware support (CONFIG_IWLDVM=y/m). Usage of
the firmware is subject to the terms and conditions contained inside the
provided LICENSE file. Please read it carefully.

%package -n iwlwifi-mvm-firmware
Summary:	MVM Firmware for Intel(R) Wireless WiFi adapters
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence = %{version}-%{release}
Requires:	iwlwifi-mld-firmware = %{version}-%{release}
%description -n iwlwifi-mvm-firmware
This package contains the firmware required by the iwlwifi driver
for Linux built with MVM firmware support (CONFIG_IWLMVM=y/m).  Usage of
the firmware is subject to the terms and conditions contained inside the
provided LICENSE file. Please read it carefully.

%package -n iwlwifi-mld-firmware
Summary:	MLD Firmware for Intel(R) Wireless WiFi adapters
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence = %{version}-%{release}
%description -n iwlwifi-mld-firmware
This package contains the firmware required by the iwlwifi driver
for Linux built with MLD firmware support (CONFIG_IWLMLD=y/m).  Usage of
the firmware is subject to the terms and conditions contained inside the
provided LICENSE file. Please read it carefully.

%package -n libertas-firmware
Summary:	Firmware for Marvell Libertas SD/USB WiFi Network Adapters
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence = %{version}-%{release}
%description -n libertas-firmware
Firmware for the Marvell Libertas series of WiFi Network Adapters
Including the SD 8686/8787 and USB 8388/8388.

%package -n mt7xxx-firmware
Summary:	Firmware for Mediatek 7600/7900 series WiFi/Bluetooth adapters
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence = %{version}-%{release}
%description -n mt7xxx-firmware
Firmware for Mediatek 7600/7900 series WiFi/Bluetooth adapters

%package -n nxpwireless-firmware
Summary:	Firmware for NXP WiFi/Bluetooth/UWB adapters
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence = %{version}-%{release}
%description -n nxpwireless-firmware
Firmware for NXP WiFi/Bluetooth/UWB adapters.

%package -n realtek-firmware
Summary:	Firmware for Realtek WiFi/Bluetooth adapters
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence = %{version}-%{release}
%description -n realtek-firmware
Firmware for Realtek WiFi/Bluetooth adapters

%package -n qcom-wwan-firmware
Summary:	Firmware for Qualcomm Wireless WAN modems
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence = %{version}-%{release}
%description -n qcom-wwan-firmware
Firmware for Qualcomm Snapdragon X-series (SDX) wireless WAN modems used
across numerous WWAN cards from numerous vendors.

%package -n tiwilink-firmware
Summary:	Firmware for Texas Instruments WiFi/Bluetooth adapters
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence = %{version}-%{release}
%description -n tiwilink-firmware
Firmware for Texas Instruments WiFi/Bluetooth adapters

# SMART NIC and network switch firmwares
%package -n liquidio-firmware
Summary:	Firmware for Cavium LiquidIO Intelligent Server Adapter
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence = %{version}-%{release}
%description -n liquidio-firmware
Firmware for Cavium LiquidIO Intelligent Server Adapter

%package -n mlxsw_spectrum-firmware
Summary:	Firmware for Mellanox Spectrum 1/2/3 Switches
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence = %{version}-%{release}
%description -n mlxsw_spectrum-firmware
Firmware for Mellanox Spectrumi series 1/2/3 ethernet switches.

%package -n mrvlprestera-firmware
Summary:	Firmware for Marvell Prestera Switchdev/ASIC devices
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence = %{version}-%{release}
%description -n mrvlprestera-firmware
Firmware for Marvell Prestera Switchdev/ASIC devices

%package -n netronome-firmware
Summary:	Firmware for Netronome Smart NICs
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence = %{version}-%{release}
%description -n netronome-firmware
Firmware for Netronome Smart NICs

%package -n qcom-accel-firmware
Summary:	Firmware for Qualcomm Technologies data center / Open-vRAN Accelerators
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence = %{version}-%{release}
%description -n qcom-accel-firmware
Firmware for Qualcomm Technologies data center and Open-vRAN accelerators
including the X100 5G RAN Accelerator Card, the QRU100 5G RAN Platform
and the Cloud AI 100.

%package -n qed-firmware
Summary:	Firmware for Marvell FastLinQ adapters family
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence = %{version}-%{release}
%description -n qed-firmware
Firmware for Marvell FastLinQ adapters family (QDE), this device
supports RoCE (RDMA over Converged Ethernet), iSCSI, iWARP, FCoE
and ethernet including SRIOV, DCB etc.

# Silicon Vendor specific
%package -n mediatek-firmware
Summary:	Firmware for Mediatek SoCs
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence = %{version}-%{release}
%description -n mediatek-firmware
Firmware for various compoents in Mediatek SoCs, in particular SCP.

%package -n qcom-firmware
Summary:	Firmware for Qualcomm SoCs
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence = %{version}-%{release}
Requires:	atheros-firmware = %{version}-%{release}
%description -n qcom-firmware
Firmware for various compoents in Qualcomm SoCs including Adreno GPUs,
Venus video encode/decode, Audio DSP, Compute DSP, modem, Sensor DSPs.

# Vision and ISP hardware
%package -n intel-vsc-firmware
Summary:	Firmware files for Intel Visual Sensing Controller (IVSC)
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence = %{version}-%{release}
%description -n intel-vsc-firmware
Firmware files for Intel Visual Sensing Controller (IVSC) for
Tiger Lake, Alder Lake and Raptor Lake SoCs and the IPU3/6 firmware.

# Sound codec hardware
%package -n cirrus-audio-firmware
Summary:	Firmware for Cirrus audio amplifiers and codecs
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence = %{version}-%{release}
%description -n cirrus-audio-firmware
Firmware for Cirrus audio amplifiers and codecs

%package -n intel-audio-firmware
Summary:	Firmware for Intel audio DSP amplifiers and codecs
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence = %{version}-%{release}
%description -n intel-audio-firmware
Firmware for Intel audio DSP amplifiers and codecs

# Random other hardware
%package -n dvb-firmware
Summary:	Firmware for various DVB broadcast receivers
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
Requires:	linux-firmware-whence = %{version}-%{release}
%description -n dvb-firmware
Firmware for various DVB broadcast receivers. These include the
Siano DTV devices, devices based on Conexant chipsets (cx18,
cx23885, cx23840, cx231xx), Xceive xc4000/xc5000, DiBcom dib0700,
Terratec H5 DRX-K, ITEtech IT9135 Ax and Bx, and av7110.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
mkdir -p %{buildroot}/%{_firmwarepath}
mkdir -p %{buildroot}/%{_firmwarepath}/updates
make DESTDIR=%{buildroot}/ FIRMWAREDIR=%{_firmwarepath} install-xz
pushd %{buildroot}/%{_firmwarepath}
rm -rf ess korg sb16 yamaha
rm -f ctefx.bin* ctspeq.bin*
rm -rf carl9170fw
rm -rf cis/{src,Makefile}
rm -f atusb/ChangeLog
rm -f av7110/{Boot.S,Makefile}
rm -f dsp56k/{bootstrap.asm,concat-bootstrap.pl,Makefile}
rm -f iscis/{*.c,*.h,README,Makefile}
rm -f keyspan_pda/{keyspan_pda.S,xircom_pgs.S,Makefile}
rm -f usbdux/*dux */*.asm
rm -f libertas/sd8686_v8*
rm -f libertas/usb8388_v5.bin*
rm -f check_whence.py Makefile README
popd
FILEDIR=`pwd`
pushd %{buildroot}/%{_firmwarepath}
find . \! -type d > $FILEDIR/linux-firmware.files
find . -type d | sed -e '/^.$/d' > $FILEDIR/linux-firmware.dirs
popd
sed -i -e 's:^./::' linux-firmware.{files,dirs}
sed \
	-i -e '/^a300_p/d' \
	-i -e '/^amdgpu/d' \
	-i -e '/^amdnpu/d' \
	-i -e '/^amd/d' \
	-i -e '/^amdtee/d' \
	-i -e '/^amd-ucode/d' \
	-i -e '/^ar3k/d' \
	-i -e '/^ath6k/d' \
	-i -e '/^ath9k_htc/d' \
	-i -e '/^ath10k/d' \
	-i -e '/^ath11k/d' \
	-i -e '/^ath12k/d' \
	-i -e '/^as102_data/d' \
	-i -e '/^av7110/d' \
	-i -e '/^brcm/d' \
	-i -e '/^cirrus/d' \
	-i -e '/^cmmb/d' \
	-i -e '/^cypress/d' \
	-i -e '/^dvb/d' \
	-i -e '/^i915/d' \
	-i -e '/^intel\/avs/d' \
	-i -e '/^intel\/catpt/d' \
	-i -e '/^intel\/IntcSST2.bin/d' \
	-i -e '/^intel\/dsp_fw/d' \
	-i -e '/^intel\/fw_sst/d' \
	-i -e '/^intel\/ipu/d' \
	-i -e '/^intel\/ipu3/d' \
	-i -e '/^intel\/irci_irci/d' \
	-i -e '/^intel\/vsc/d' \
	-i -e '/^isdbt/d' \
	-i -e '/^iwlwifi/d' \
	-i -e '/^intel\/iwlwifi/d' \
	-i -e '/^nvidia\/a/d' \
	-i -e '/^nvidia\/g/d' \
	-i -e '/^nvidia\/tu/d' \
	-i -e '/^libertas/d' \
	-i -e '/^liquidio/d' \
	-i -e '/^mellanox/d' \
	-i -e '/^mediatek/d' \
	-i -e '/^mrvl\/prestera/d' \
	-i -e '/^mrvl\/sd8787/d' \
	-i -e '/^mt76/d' \
	-i -e '/^netronome/d' \
	-i -e '/^nxp/d' \
	-i -e '/^qca/d' \
	-i -e '/^qcom/d' \
	-i -e '/^qed/d' \
	-i -e '/^radeon/d' \
	-i -e '/^rtl_bt/d' \
	-i -e '/^rtlwifi/d' \
	-i -e '/^rtw88/d' \
	-i -e '/^rtw89/d' \
	-i -e '/^sms1xxx/d' \
	-i -e '/^tdmb/d' \
	-i -e '/^ti-connectivity/d' \
	-i -e '/^v4l-cx2/d' \
	linux-firmware.{files,dirs}
sed -i -e 's!^!/usr/lib/firmware/!' linux-firmware.{files,dirs}
sed -i -e 's/^/"/;s/$/"/' linux-firmware.files
sed -e 's/^/%%dir /' linux-firmware.dirs >> linux-firmware.files
%oreon_autofiles amd-gpu-firmware usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles intel-gpu-firmware usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles nvidia-gpu-firmware usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles amd-ucode-firmware usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles atheros-firmware usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles brcmfmac-firmware usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles iwlegacy-firmware usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles iwlwifi-dvm-firmware usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles iwlwifi-mvm-firmware usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles iwlwifi-mld-firmware usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles libertas-firmware usr/*/lib*.so.*
%oreon_autofiles mt7xxx-firmware usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles nxpwireless-firmware usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles realtek-firmware usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qcom-wwan-firmware usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles tiwilink-firmware usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles liquidio-firmware usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mlxsw_spectrum-firmware usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mrvlprestera-firmware usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles netronome-firmware usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qcom-accel-firmware usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qed-firmware usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mediatek-firmware usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qcom-firmware usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles intel-vsc-firmware usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cirrus-audio-firmware usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles intel-audio-firmware usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles dvb-firmware usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/*/lib*.so.* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%pretrans -n nvidia-gpu-firmware -p <lua>

path = "/usr/lib/firmware/nvidia/ad103"
st = posix.stat(path)
if st and st.type == "directory" then
  status = os.rename(path, path .. ".rpmmoved")
  if not status then
    suffix = 0
    while not status do
      suffix = suffix + 1
      status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
    end
    os.rename(path, path .. ".rpmmoved")
  end
end
path = "/usr/lib/firmware/nvidia/ad104"
st = posix.stat(path)
if st and st.type == "directory" then
  status = os.rename(path, path .. ".rpmmoved")
  if not status then
    suffix = 0
    while not status do
      suffix = suffix + 1
      status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
    end
    os.rename(path, path .. ".rpmmoved")
  end
end
path = "/usr/lib/firmware/nvidia/ad106"
st = posix.stat(path)
if st and st.type == "directory" then
  status = os.rename(path, path .. ".rpmmoved")
  if not status then
    suffix = 0
    while not status do
      suffix = suffix + 1
      status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
    end
    os.rename(path, path .. ".rpmmoved")
  end
end
path = "/usr/lib/firmware/nvidia/ad107"
st = posix.stat(path)
if st and st.type == "directory" then
  status = os.rename(path, path .. ".rpmmoved")
  if not status then
    suffix = 0
    while not status do
      suffix = suffix + 1
      status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
    end
    os.rename(path, path .. ".rpmmoved")
  end
end
%files -f %{oreon_filedir}/main.list
%files -n linux-firmware-whence -f %{oreon_filedir}/linux-firmware-whence.list
%files -n amd-gpu-firmware -f %{oreon_filedir}/amd-gpu-firmware.list
%files -n intel-gpu-firmware -f %{oreon_filedir}/intel-gpu-firmware.list
%files -n nvidia-gpu-firmware -f %{oreon_filedir}/nvidia-gpu-firmware.list
%files -n amd-ucode-firmware -f %{oreon_filedir}/amd-ucode-firmware.list
%files -n atheros-firmware -f %{oreon_filedir}/atheros-firmware.list
%files -n brcmfmac-firmware -f %{oreon_filedir}/brcmfmac-firmware.list
%files -n iwlegacy-firmware -f %{oreon_filedir}/iwlegacy-firmware.list
%files -n iwlwifi-dvm-firmware -f %{oreon_filedir}/iwlwifi-dvm-firmware.list
%files -n iwlwifi-mvm-firmware -f %{oreon_filedir}/iwlwifi-mvm-firmware.list
%files -n iwlwifi-mld-firmware -f %{oreon_filedir}/iwlwifi-mld-firmware.list
%files -n libertas-firmware -f %{oreon_filedir}/libertas-firmware.list
%files -n mt7xxx-firmware -f %{oreon_filedir}/mt7xxx-firmware.list
%files -n nxpwireless-firmware -f %{oreon_filedir}/nxpwireless-firmware.list
%files -n realtek-firmware -f %{oreon_filedir}/realtek-firmware.list
%files -n qcom-wwan-firmware -f %{oreon_filedir}/qcom-wwan-firmware.list
%files -n tiwilink-firmware -f %{oreon_filedir}/tiwilink-firmware.list
%files -n liquidio-firmware -f %{oreon_filedir}/liquidio-firmware.list
%files -n mlxsw_spectrum-firmware -f %{oreon_filedir}/mlxsw_spectrum-firmware.list
%files -n mrvlprestera-firmware -f %{oreon_filedir}/mrvlprestera-firmware.list
%files -n netronome-firmware -f %{oreon_filedir}/netronome-firmware.list
%files -n qcom-accel-firmware -f %{oreon_filedir}/qcom-accel-firmware.list
%files -n qed-firmware -f %{oreon_filedir}/qed-firmware.list
%files -n mediatek-firmware -f %{oreon_filedir}/mediatek-firmware.list
%files -n qcom-firmware -f %{oreon_filedir}/qcom-firmware.list
%files -n intel-vsc-firmware -f %{oreon_filedir}/intel-vsc-firmware.list
%files -n cirrus-audio-firmware -f %{oreon_filedir}/cirrus-audio-firmware.list
%files -n intel-audio-firmware -f %{oreon_filedir}/intel-audio-firmware.list
%files -n dvb-firmware -f %{oreon_filedir}/dvb-firmware.list

%changelog

%autochangelog
