%global source92_hash ec68522271e9ac6c936c8731ce0d74417f8ed39296e85ab0e5801af195459214
%global source90_hash 2089e3125e611376cb44326b5765674255443b2484f88de97251939d18055f68
%global source0_hash a5df9c1be9b17de3d8318fd28003780cf679eb2ba3cae33a6a1890d7f60d27dd
%global source2_hash b28c91532a8b65a1f983b4c28b7488174e4a01008e29ce8e69bd789f28bc2a89
%global source4_hash 1d024d13b5086a3d6bba86314a38b267a3b371845b0227b4f803888ecbca5a7a
%global source5_hash ee90a0f879d2b7b7159124ff22b937a2a9a8c36d3bb65d1da7dd3f04370a10bd
%global source6_hash 29edce3d302a15563d8663198bbc398c5a0554765c83830d0d4c0409d21a16c4
%undefine _auto_set_build_flags
%define build_arches x86_64 aarch64 riscv64
%ifnarch %{build_arches}
%global debug_package %{nil}
%endif
%define GITDATE        20260213
%define GITCOMMIT      b7a715f7c03c
%define TOOLCHAIN      GCC
%define PLATFORMS_COMMIT c3efe816e1bb
%define OPENSSL_VER    3.5.5
%define DBXDATE        20251016
%define silent --silent
%define build_ovmf 1
%define build_aarch64 1
%define build_riscv64 1
%define build_loongarch64 1
%define qemuvars 1
%define cross %{defined fedora}
%define disable_werror %{defined fedora}
%if 0%{?copr_projectname:1}
  %define dist %{buildtag}
%endif
Name:       edk2
Version:    %{GITDATE}
Release:        1%{?dist}
Summary:        UEFI firmware for 64-bit virtual machines
License:    Apache-2.0 AND (BSD-2-Clause OR GPL-2.0-or-later) AND BSD-2-Clause-Patent AND BSD-3-Clause AND BSD-4-Clause AND ISC AND MIT AND LicenseRef-Fedora-Public-Domain
URL:        http://www.tianocore.org
Source0:        https://github.com/tianocore/edk2/archive/b7a715f7c03c.tar.gz#/edk2-b7a715f7c03c.tar.gz
Source1:        ovmf-whitepaper-c770f8c.txt
Source2:        https://github.com/openssl/openssl/releases/download/openssl-3.5.5/openssl-3.5.5.tar.gz
Source4:        https://github.com/tianocore/edk2-platforms/archive/c3efe816e1bb.tar.gz#/edk2-platforms-c3efe816e1bb.tar.gz
Source5: https://github.com/akheron/jansson/releases/download/v2.13.1/jansson-2.13.1.tar.bz2
Source6: https://www.kernel.org/pub/software/utils/dtc/dtc-1.7.0.tar.xz
Source9:        README.experimental
Source10:        50-edk2-aarch64-qcow2.json
Source11:        51-edk2-aarch64-raw.json
Source12:        52-edk2-aarch64-verbose-qcow2.json
Source13:        53-edk2-aarch64-verbose-raw.json
Source20:        90-edk2-ovmf-qemuvars-x64-sb-enrolled.json
Source21:        91-edk2-ovmf-qemuvars-x64-sb.json
Source22:        90-edk2-aarch64-qemuvars-sb-enrolled.json
Source23:        91-edk2-aarch64-qemuvars-sb.json
Source24:        92-edk2-ovmf-igvm-x64-nosb.json
Source40:        30-edk2-ovmf-4m-qcow2-x64-sb-enrolled.json
Source41:        31-edk2-ovmf-2m-raw-x64-sb-enrolled.json
Source42:        40-edk2-ovmf-4m-qcow2-x64-sb.json
Source43:        41-edk2-ovmf-2m-raw-x64-sb.json
Source44:        50-edk2-ovmf-x64-microvm.json
Source45:        50-edk2-ovmf-4m-qcow2-x64-nosb.json
Source46:        51-edk2-ovmf-2m-raw-x64-nosb.json
Source47:        60-edk2-ovmf-x64-stateless.json
Source48:        61-edk2-ovmf-x64-amdsev.json
Source49:        61-edk2-ovmf-x64-inteltdx.json
Source50:        50-edk2-riscv-qcow2.json
Source60:        50-edk2-loongarch64.json
Source80:        edk2-build.py
Source81:        edk2-build.fedora
Source82:        edk2-build.fedora.platforms
Source83:        edk2-build.rhel-9
Source84:        edk2-build.rhel-10
Source90:        https://raw.githubusercontent.com/microsoft/secureboot_objects/main/PostSignedObjects/DBX/amd64/DBXUpdate.bin#/DBXUpdate-%{DBXDATE}.x64.bin
Source92:        https://raw.githubusercontent.com/microsoft/secureboot_objects/main/PostSignedObjects/DBX/arm64/DBXUpdate.bin#/DBXUpdate-%{DBXDATE}.aa64.bin
Patch0001:        0001-BaseTools-do-not-build-BrotliCompress-RH-only.patch
Patch0002:        0002-MdeModulePkg-remove-package-private-Brotli-include-p.patch
Patch0003:        0003-MdeModulePkg-TerminalDxe-set-xterm-resolution-on-mod.patch
Patch0004:        0004-OvmfPkg-take-PcdResizeXterm-from-the-QEMU-command-li.patch
Patch0005:        0005-ArmVirtPkg-take-PcdResizeXterm-from-the-QEMU-command.patch
Patch0006:        0006-OvmfPkg-enable-DEBUG_VERBOSE-RHEL-only.patch
Patch0007:        0007-OvmfPkg-silence-DEBUG_VERBOSE-0x00400000-in-QemuVide.patch
Patch0008:        0008-ArmVirtPkg-silence-DEBUG_VERBOSE-0x00400000-in-QemuR.patch
Patch0009:        0009-OvmfPkg-QemuRamfbDxe-Do-not-report-DXE-failure-on-Aa.patch
Patch0010:        0010-OvmfPkg-silence-EFI_D_VERBOSE-0x00400000-in-NvmExpre.patch
Patch0011:        0011-OvmfPkg-QemuKernelLoaderFsDxe-suppress-error-on-no-k.patch
Patch0012:        0012-SecurityPkg-Tcg2Dxe-suppress-error-on-no-swtpm-in-si.patch
Patch0013:        0013-OvmfPkg-set-PcdVariableStoreSize-PcdMaxVolatileVaria.patch
%if 0%{?fedora} >= 38 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
Patch0014:        0014-silence-.-has-a-LOAD-segment-with-RWX-permissions-wa.patch
%endif
Patch0015:        0015-OvmfPkg-X64-add-opt-org.tianocore-UninstallMemAttrPr.patch
Patch0016:        0016-OvmfPkg-PlatformDxe-register-page-fault-handler-for-.patch
Patch0017:        0017-OvmfPkg-PlatformDxe-add-check-for-1g-page-support.patch
Patch0018:        0018-Revert-OvmfPkg-X86QemuLoadImageLib-flip-default-for-.patch
%ifarch %{build_arches}
%if %{build_ovmf}
%endif
%if %{cross}
%endif
%endif
# oreon:deps
BuildRequires:  git
# /oreon:deps
%description
EDK II is a modern, feature-rich, cross-platform firmware development
environment for the UEFI and PI specifications. This package contains sample
64-bit UEFI firmware builds for QEMU and KVM.

%ifarch %{build_arches}

%package ovmf
Summary:    UEFI firmware for x86_64 virtual machines
BuildArch:  noarch
Provides:   OVMF = %{version}-%{release}
Obsoletes:  OVMF < 20180508-100.gitee3198e672e2.el7
Recommends: edk2-shell-x64
Conflicts:  libvirt-daemon-driver-qemu < 9.7.0
Provides:   bundled(openssl) = %{OPENSSL_VER}
License:    Apache-2.0 AND (BSD-2-Clause OR GPL-2.0-or-later) AND BSD-2-Clause-Patent AND BSD-4-Clause AND ISC AND LicenseRef-Fedora-Public-Domain
URL:        http://www.tianocore.org/ovmf/
%description ovmf
OVMF (Open Virtual Machine Firmware) is a project to enable UEFI support for
Virtual Machines. This package contains a sample 64-bit UEFI firmware for QEMU
and KVM.

%package shell-x64
Summary:        EFI Shell for x64
BuildArch:      noarch
%description shell-x64
EFI Shell for x64

%package aarch64
Summary:    UEFI firmware for aarch64 virtual machines
BuildArch:  noarch
Provides:   AAVMF = %{version}-%{release}
Obsoletes:  AAVMF < 20180508-100.gitee3198e672e2.el7
Recommends: edk2-shell-aa64
Conflicts:  libvirt-daemon-driver-qemu < 9.7.0
Provides:   bundled(openssl) = %{OPENSSL_VER}
License:    Apache-2.0 AND (BSD-2-Clause OR GPL-2.0-or-later) AND BSD-2-Clause-Patent AND BSD-4-Clause AND ISC AND LicenseRef-Fedora-Public-Domain
URL:        https://github.com/tianocore/tianocore.github.io/wiki/ArmVirtPkg
%description aarch64
AAVMF (ARM Architecture Virtual Machine Firmware) is an EFI Development Kit II
platform that enables UEFI support for QEMU/KVM ARM Virtual Machines. This
package contains a 64-bit build.

%package shell-aa64
Summary:        EFI Shell for aa64
BuildArch:      noarch
%description shell-aa64
EFI Shell for aa64

%package tools
Summary:        EFI Development Kit II Tools
License:        BSD-2-Clause-Patent AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/tianocore/tianocore.github.io/wiki/BaseTools
%description tools
This package provides tools that are needed to
build EFI executables and ROMs using the GNU tools.

%package tools-doc
Summary:        Documentation for EFI Development Kit II Tools
BuildArch:      noarch
License:        BSD-2-Clause-Patent
URL:            https://github.com/tianocore/tianocore.github.io/wiki/BaseTools
%description tools-doc
This package documents the tools that are needed to
build EFI executables and ROMs using the GNU tools.

%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source2_hash}" = "none" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source2_hash}" || { echo "oreon: Source2 hash mismatch" >&2; exit 1; }; }
test "%{source4_hash}" = "none" || { f="%{SOURCE4}"; test -f "$f" || { echo "oreon: missing Source4 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source4_hash}" || { echo "oreon: Source4 hash mismatch" >&2; exit 1; }; }
test "%{source5_hash}" = "none" || { f="%{SOURCE5}"; test -f "$f" || { echo "oreon: missing Source5 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source5_hash}" || { echo "oreon: Source5 hash mismatch" >&2; exit 1; }; }
test "%{source6_hash}" = "none" || { f="%{SOURCE6}"; test -f "$f" || { echo "oreon: missing Source6 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source6_hash}" || { echo "oreon: Source6 hash mismatch" >&2; exit 1; }; }
# We needs some special git config options that %%autosetup won't give us.
# We init the git dir ourselves, then tell %%autosetup not to blow it away.
%setup -q -T -D -c -n edk2-%{GITCOMMIT}
tar -xf %{SOURCE0} --strip-components=1
tar -xf %{SOURCE4} --strip-components=1 "*/Drivers" "*/Features" "*/Platform" "*/Silicon"
git init -q
git config core.whitespace cr-at-eol
git config am.keepcr true
# -T is passed to %%setup to not re-extract the archive
# -D is passed to %%setup to not delete the existing archive dir
%autosetup -T -D -n edk2-%{GITCOMMIT} -S git_am

cp -a -- %{SOURCE1} .
# extract tarballs into place
tar -xf %{SOURCE2} --strip-components=1 --directory CryptoPkg/Library/OpensslLib/openssl
tar -xf %{SOURCE5} --strip-components=1 --directory RedfishPkg/Library/JsonLib/jansson
tar -xf %{SOURCE6} --strip-components=1 --directory MdePkg/Library/BaseFdtLib/libfdt
# include paths pointing to unused submodules
mkdir -p MdePkg/Library/MipiSysTLib/mipisyst/library/include
mkdir -p CryptoPkg/Library/MbedTlsLib/mbedtls/include
mkdir -p CryptoPkg/Library/MbedTlsLib/mbedtls/include/mbedtls
mkdir -p CryptoPkg/Library/MbedTlsLib/mbedtls/library
mkdir -p SecurityPkg/DeviceSecurity/SpdmLib/libspdm/include

# Done by %%setup, but we do not use it for the auxiliary tarballs
chmod -Rf a+rX,u+w,g-w,o-w .

cp -a -- \
   %{SOURCE9} \
   %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} \
   %{SOURCE20} %{SOURCE21} %{SOURCE22} %{SOURCE23} %{SOURCE24} \
   %{SOURCE40} %{SOURCE41} %{SOURCE42} %{SOURCE43} %{SOURCE44} \
   %{SOURCE45} %{SOURCE46} %{SOURCE47} %{SOURCE48} %{SOURCE49} \
   %{SOURCE50} \
   %{SOURCE60} \
   %{SOURCE80} %{SOURCE81} %{SOURCE82} %{SOURCE83} %{SOURCE84} \
   %{SOURCE90} %{SOURCE92} \
   .

%build

%ifarch %{build_arches}
build_iso() {
  dir="$1"
  UEFI_SHELL_BINARY=${dir}/Shell.efi
  ENROLLER_BINARY=${dir}/EnrollDefaultKeys.efi
  UEFI_SHELL_IMAGE=uefi_shell.img
  ISO_IMAGE=${dir}/UefiShell.iso
  UEFI_SHELL_BINARY_BNAME=$(basename -- "$UEFI_SHELL_BINARY")
  UEFI_SHELL_SIZE=$(stat --format=%s -- "$UEFI_SHELL_BINARY")
  ENROLLER_SIZE=$(stat --format=%s -- "$ENROLLER_BINARY")
  UEFI_SHELL_IMAGE_KB=$((
    (UEFI_SHELL_SIZE + ENROLLER_SIZE + 1 * 1024 * 1024) * 11 / 10 / 1024
  ))
  rm -f -- "$UEFI_SHELL_IMAGE"
  mkdosfs -C "$UEFI_SHELL_IMAGE" -n UEFI_SHELL -- "$UEFI_SHELL_IMAGE_KB"
  export MTOOLS_SKIP_CHECK=1
  mmd   -i "$UEFI_SHELL_IMAGE"                       ::efi
  mmd   -i "$UEFI_SHELL_IMAGE"                       ::efi/boot
  mcopy -i "$UEFI_SHELL_IMAGE"  "$UEFI_SHELL_BINARY" ::efi/boot/bootx64.efi
  mcopy -i "$UEFI_SHELL_IMAGE"  "$ENROLLER_BINARY"   ::
  mdir  -i "$UEFI_SHELL_IMAGE"  -/                   ::
  mkisofs -input-charset ASCII -J -rational-rock \
    -e "$UEFI_SHELL_IMAGE" -no-emul-boot \
    -o "$ISO_IMAGE" "$UEFI_SHELL_IMAGE"
}
export EXTRA_OPTFLAGS="%{optflags}"
export EXTRA_LDFLAGS="%{__global_ldflags}"
export RELEASE_DATE="$(echo %{GITDATE} | sed -e 's|\(....\)\(..\)\(..\)|\2/\3/\1|')"
touch OvmfPkg/AmdSev/Grub/grub.efi   # dummy
python3 CryptoPkg/Library/OpensslLib/configure.py
%if %{build_ovmf}
./edk2-build.py --config edk2-build.fedora %{?silent} --release-date "$RELEASE_DATE" -m ovmf
./edk2-build.py --config edk2-build.fedora.platforms %{?silent} -m x64
virt-fw-vars --input   Fedora/ovmf/OVMF_VARS.fd \
             --output  Fedora/ovmf/OVMF_VARS.secboot.fd \
             --set-dbx DBXUpdate-%{DBXDATE}.x64.bin \
             --enroll-redhat --secure-boot
virt-fw-vars --input   Fedora/ovmf/OVMF_VARS_4M.fd \
             --output  Fedora/ovmf/OVMF_VARS_4M.secboot.fd \
             --set-dbx DBXUpdate-%{DBXDATE}.x64.bin \
             --enroll-redhat --secure-boot
virt-fw-vars --input   Fedora/ovmf/OVMF.inteltdx.fd \
             --output  Fedora/ovmf/OVMF.inteltdx.secboot.fd \
             --set-dbx DBXUpdate-%{DBXDATE}.x64.bin \
             --enroll-redhat --secure-boot
%if %{qemuvars}
virt-fw-vars --output-json Fedora/ovmf/vars.blank.json
virt-fw-vars --output-json Fedora/ovmf/vars.secboot.json \
             --set-dbx DBXUpdate-%{DBXDATE}.x64.bin \
             --enroll-redhat --secure-boot
%endif
build_iso Fedora/ovmf
cp DBXUpdate-%{DBXDATE}.x64.bin Fedora/ovmf
igvm-wrap --input Fedora/ovmf/OVMF_CODE_4M.fd \
          --vars Fedora/ovmf/OVMF_VARS_4M.fd \
          --output Fedora/ovmf/OVMF.igvm \
          --meta --inspect --snp
for raw in */ovmf/*_4M*.fd; do
    qcow2="${raw%.fd}.qcow2"
    qemu-img convert -f raw -O qcow2 -o cluster_size=4096 -S 4096 "$raw" "$qcow2"
    rm -f "$raw"
done
virt-fw-vars --input   Fedora/ovmf/OVMF.stateless.fd \
             --output  Fedora/ovmf/OVMF.stateless.secboot.fd \
             --set-dbx DBXUpdate-%{DBXDATE}.x64.bin \
             --enroll-redhat --secure-boot \
             --set-fallback-no-reboot
for image in \
	Fedora/ovmf/OVMF_CODE.secboot.fd \
	Fedora/ovmf/OVMF_CODE_4M.secboot.qcow2 \
	Fedora/ovmf/OVMF.stateless.secboot.fd \
; do
	pcr="${image}"
	pcr="${pcr%.fd}"
	pcr="${pcr%.qcow2}"
	pcr="${pcr}.pcrlock"
	python3 /usr/share/doc/python3-virt-firmware/experimental/measure.py \
		--image "$image" \
		--version "%{name}-%{version}-%{release}" \
                --no-shim --pcrlock \
                --bank sha256 --bank sha384 \
		> "$pcr"
done
%endif
%if %{build_aarch64}
./edk2-build.py --config edk2-build.fedora %{?silent} --release-date "$RELEASE_DATE" -m armvirt
./edk2-build.py --config edk2-build.fedora.platforms %{?silent} -m aa64
virt-fw-vars --input   Fedora/aarch64/vars-template-pflash.raw \
             --output  Fedora/experimental/vars-template-secboot-testonly-pflash.raw \
             --set-dbx DBXUpdate-%{DBXDATE}.aa64.bin \
             --enroll-redhat --secure-boot --distro-keys rhel
%if %{qemuvars}
virt-fw-vars --output-json Fedora/aarch64/vars.blank.json
virt-fw-vars --output-json Fedora/aarch64/vars.secboot.json \
             --set-dbx DBXUpdate-%{DBXDATE}.aa64.bin \
             --enroll-redhat --secure-boot
%endif
cp DBXUpdate-%{DBXDATE}.aa64.bin Fedora/aarch64
for raw in */aarch64/*.raw; do
    qcow2="${raw%.raw}.qcow2"
    qemu-img convert -f raw -O qcow2 -o cluster_size=4096 -S 4096 "$raw" "$qcow2"
done
%endif
%if %{build_riscv64}
./edk2-build.py --config edk2-build.fedora %{?silent} --release-date "$RELEASE_DATE" -m riscv
./edk2-build.py --config edk2-build.fedora.platforms %{?silent} -m riscv
for raw in */riscv/*.raw; do
    qcow2="${raw%.raw}.qcow2"
    qemu-img convert -f raw -O qcow2 -o cluster_size=4096 -S 4096 "$raw" "$qcow2"
    rm -f "$raw"
done
%endif
%if %{build_loongarch64}
./edk2-build.py --config edk2-build.fedora %{?silent} -m loongarch
find Build -name *.fd
%endif
%endif
%install
%ifarch %{build_arches}
cp -a OvmfPkg/License.txt License.OvmfPkg.txt
cp -a CryptoPkg/Library/OpensslLib/openssl/LICENSE.txt LICENSE.openssl
mkdir -p %{buildroot}%{_datadir}/qemu/firmware
mkdir -p %{buildroot}%{_bindir} \
         %{buildroot}%{_datadir}/%{name}/Conf \
         %{buildroot}%{_datadir}/%{name}/Scripts
install BaseTools/Source/C/bin/* \
        %{buildroot}%{_bindir}
install BaseTools/BinWrappers/PosixLike/LzmaF86Compress \
        %{buildroot}%{_bindir}
install BaseTools/BuildEnv \
        %{buildroot}%{_datadir}/%{name}
install BaseTools/Conf/*.template \
        %{buildroot}%{_datadir}/%{name}/Conf
install BaseTools/Scripts/GccBase.lds \
        %{buildroot}%{_datadir}/%{name}/Scripts
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -av Fedora/* %{buildroot}%{_datadir}/%{name}
%if %{build_ovmf}
mkdir -p %{buildroot}%{_datadir}/OVMF
ln -s ../%{name}/ovmf/OVMF_CODE.fd         %{buildroot}%{_datadir}/OVMF/
ln -s ../%{name}/ovmf/OVMF_CODE.secboot.fd %{buildroot}%{_datadir}/OVMF/
ln -s ../%{name}/ovmf/OVMF_VARS.fd         %{buildroot}%{_datadir}/OVMF/
ln -s ../%{name}/ovmf/OVMF_VARS.secboot.fd %{buildroot}%{_datadir}/OVMF/
ln -s ../%{name}/ovmf/UefiShell.iso        %{buildroot}%{_datadir}/OVMF/
ln -s OVMF_CODE.fd %{buildroot}%{_datadir}/%{name}/ovmf/OVMF_CODE.cc.fd
mkdir -p %{buildroot}%{_datadir}/qemu/firmware
install -m 0644 \
        30-edk2-ovmf-4m-qcow2-x64-sb-enrolled.json \
        31-edk2-ovmf-2m-raw-x64-sb-enrolled.json \
        40-edk2-ovmf-4m-qcow2-x64-sb.json \
        41-edk2-ovmf-2m-raw-x64-sb.json \
        50-edk2-ovmf-4m-qcow2-x64-nosb.json \
        51-edk2-ovmf-2m-raw-x64-nosb.json \
        61-edk2-ovmf-x64-amdsev.json \
        61-edk2-ovmf-x64-inteltdx.json \
        %{buildroot}%{_datadir}/qemu/firmware
%if %{qemuvars}
install -m 0644 \
        90-edk2-ovmf-qemuvars-x64-sb-enrolled.json \
        91-edk2-ovmf-qemuvars-x64-sb.json \
        %{buildroot}%{_datadir}/qemu/firmware
%endif
%endif
%if %{build_aarch64}
mkdir -p %{buildroot}%{_datadir}/AAVMF
ln -s ../%{name}/aarch64/QEMU_EFI-pflash.raw \
  %{buildroot}%{_datadir}/AAVMF/AAVMF_CODE.verbose.fd
ln -s ../%{name}/aarch64/QEMU_EFI-silent-pflash.raw \
  %{buildroot}%{_datadir}/AAVMF/AAVMF_CODE.fd
ln -s ../%{name}/aarch64/vars-template-pflash.raw \
  %{buildroot}%{_datadir}/AAVMF/AAVMF_VARS.fd
install -m 0644 \
        50-edk2-aarch64-qcow2.json \
        51-edk2-aarch64-raw.json \
        52-edk2-aarch64-verbose-qcow2.json \
        53-edk2-aarch64-verbose-raw.json \
        %{buildroot}%{_datadir}/qemu/firmware
%if %{qemuvars}
install -m 0644 \
        90-edk2-aarch64-qemuvars-sb-enrolled.json \
        91-edk2-aarch64-qemuvars-sb.json \
        %{buildroot}%{_datadir}/qemu/firmware
%endif
%endif
%if %{build_riscv64}
install -m 0644 \
        50-edk2-riscv-qcow2.json \
        %{buildroot}%{_datadir}/qemu/firmware
%endif
%if %{build_loongarch64}
install -m 0644 \
        50-edk2-loongarch64.json \
        %{buildroot}%{_datadir}/qemu/firmware
%oreon_autofiles main
%endif
%endif
%check

%ifarch %{build_arches}
for file in %{buildroot}%{_datadir}/%{name}/*/*VARS.secboot.fd; do
    test -f "$file" || continue
    virt-fw-vars --input $file --print | grep "SecureBootEnable.*ON" || exit 1
done
%endif
%global common_files \
  %%license License.txt License.OvmfPkg.txt License-History.txt LICENSE.openssl \
  %%dir %%{_datadir}/%%{name}/ \
  %%dir %%{_datadir}/qemu \
  %%dir %%{_datadir}/qemu/firmware
%ifarch %{build_arches}
%if %{build_ovmf}
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{GITDATE}-1
- Prepare for Oreon 11 (RP1)
%endif
%endif
