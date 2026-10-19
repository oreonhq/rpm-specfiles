%global source0_hash 58c75f036970d47baebd549270c70cfc368ba6761ab732fa76e6a2a6f2341872
%global qemuroms \\\
  8086100e:e1000 \\\
  10ec8139:rtl8139 \\\
  1af41000:virtio \\\
  808610d3:e1000e
%global buildarches x86_64 aarch64
%global debug_package %{nil}
%global githash de8a0821c7bc737e724fa3dfb6d89dc36f591d7a
%global hash de8a0821
%global date 20240119
Name:    ipxe
Version: %{date}
Release:        1%{?dist}
Summary:        A network boot loader
License: BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-only AND (GPL-2.0-only OR MPL-1.1) AND GPL-2.0-or-later AND GPL-2.0-or-later WITH UBDL-exception AND ISC AND MIT
URL:     http://ipxe.org/
Source0:        https://github.com/ipxe/ipxe/archive/de8a0821c7bc737e724fa3dfb6d89dc36f591d7a.tar.gz#/ipxe--gitde8a0821.tar.gz
Patch0001:        0001-build-customize-configuration.patch
Patch0002:        0002-Use-spec-compliant-timeouts.patch
Patch0003:        gcc15.patch
%ifarch %{buildarches}
%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9 || 0%{?oreon} >= 11
%endif
%ifarch x86_64
%endif
Obsoletes: gpxe <= 1.0.1
%endif
%ifarch x86_64
# oreon:deps

# /oreon:deps
%package bootimgs-x86
Summary: X86 Network boot loader images in bootable USB, CD, floppy and GRUB formats
BuildArch: noarch
Provides: %{name}-bootimgs = %{version}-%{release}
Obsoletes: %{name}-bootimgs < 20200823-9.git4bd064de
Obsoletes: gpxe-bootimgs <= 1.0.1
%package roms
Summary: Network boot loader roms in .rom format
Requires: %{name}-roms-qemu = %{version}-%{release}
BuildArch: noarch
Obsoletes: gpxe-roms <= 1.0.1
%package roms-qemu
Summary: Network boot loader roms supported by QEMU, .rom format
BuildArch: noarch
Obsoletes: gpxe-roms-qemu <= 1.0.1
%description bootimgs-x86
iPXE is an open source network bootloader. It provides a direct
replacement for proprietary PXE ROMs, with many extra features such as
DNS, HTTP, iSCSI, etc.

This package contains the iPXE boot images in USB, CD, floppy, and PXE
UNDI formats.

%description roms
iPXE is an open source network bootloader. It provides a direct
replacement for proprietary PXE ROMs, with many extra features such as
DNS, HTTP, iSCSI, etc.

This package contains the iPXE roms in .rom format.

%description roms-qemu
iPXE is an open source network bootloader. It provides a direct
replacement for proprietary PXE ROMs, with many extra features such as
DNS, HTTP, iSCSI, etc.

This package contains the iPXE ROMs for devices emulated by QEMU, in
.rom format.
%endif

%ifarch aarch64
%package bootimgs-aarch64
Summary: ARM Network boot loader images in bootable USB and GRUB formats
BuildArch: noarch
%description bootimgs-aarch64
iPXE is an open source network bootloader. It provides a direct
replacement for proprietary PXE ROMs, with many extra features such as
DNS, HTTP, iSCSI, etc.

This package contains the iPXE ARM boot images in USB and GRUB formats.
%endif

%description
iPXE is an open source network bootloader. It provides a direct
replacement for proprietary PXE ROMs, with many extra features such as
DNS, HTTP, iSCSI, etc.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{githash}
%autopatch -p1
# ath9k drivers are too big for an Option ROM, and ipxe devs say it doesn't
# make sense anyways
# http://lists.ipxe.org/pipermail/ipxe-devel/2012-March/001290.html
rm -rf src/drivers/net/ath/ath9k

%build

cd src
make_ipxe() {
    make %{?_smp_mflags} \
        NO_WERROR=1 V=1 \
        GITVERSION=%{hash} \
        "$@"
}
%ifarch x86_64
make_ipxe bin-i386-efi/ipxe.efi bin-x86_64-efi/ipxe.efi \
    bin-x86_64-efi/snponly.efi
make_ipxe ISOLINUX_BIN=/usr/share/syslinux/isolinux.bin \
    bin/undionly.kpxe bin/ipxe.{dsk,iso,usb,lkrn} \
    allroms
mkdir bin-combined
for romstr in %{qemuroms}; do
  rom=$(echo "$romstr" | cut -d ":" -f 1)
  make_ipxe CONFIG=qemu bin/${rom}.rom
  make_ipxe CONFIG=qemu bin-x86_64-efi/${rom}.efidrv
  vid="0x${rom%%????}"
  did="0x${rom#????}"
  EfiRom -f "$vid" -i "$did" --pci23 \
         -ec bin-x86_64-efi/${rom}.efidrv \
         -o  bin-combined/${rom}.eficrom
  util/catrom.pl \
      bin/${rom}.rom \
      bin-combined/${rom}.eficrom \
      > bin-combined/${rom}.rom
  EfiRom -d  bin-combined/${rom}.rom
  truncate -s \>256K bin-combined/${rom}.rom
  test $(stat -c '%s' bin-combined/${rom}.rom) -le $((256 * 1024))
done
%endif
%ifarch aarch64
make_ipxe bin-arm64-efi/snponly.efi
%endif
%install
%ifarch x86_64
mkdir -p %{buildroot}/%{_datadir}/%{name}/
mkdir -p %{buildroot}/%{_datadir}/%{name}.efi/
pushd src/bin/
cp -a undionly.kpxe ipxe.{iso,usb,dsk,lkrn} %{buildroot}/%{_datadir}/%{name}/
for img in *.rom; do
  if [ -e $img ]; then
    cp -a $img %{buildroot}/%{_datadir}/%{name}/
    echo %{_datadir}/%{name}/$img >> ../../rom.list
  fi
done
popd
cp -a src/bin-i386-efi/ipxe.efi %{buildroot}/%{_datadir}/%{name}/ipxe-i386.efi
cp -a src/bin-x86_64-efi/ipxe.efi %{buildroot}/%{_datadir}/%{name}/ipxe-x86_64.efi
cp -a src/bin-x86_64-efi/snponly.efi %{buildroot}/%{_datadir}/%{name}/ipxe-snponly-x86_64.efi
mkdir -p %{buildroot}%{_datadir}/%{name}/qemu/
for romstr in %{qemuroms}; do
  rom=$(echo "$romstr" | cut -d ":" -f 1)
  qemuname=$(echo "$romstr" | cut -d ":" -f 2)
  sed -i -e "/\/${rom}.rom/d" rom.list
  echo %{_datadir}/%{name}/${rom}.rom >> qemu.rom.list
  cp src/bin-combined/${rom}.rom %{buildroot}/%{_datadir}/%{name}.efi/
  echo %{_datadir}/%{name}.efi/${rom}.rom >> qemu.rom.list
  ln -s ../../ipxe/${rom}.rom %{buildroot}%{_datadir}/%{name}/qemu/pxe-${qemuname}.rom
  ln -s ../../ipxe.efi/${rom}.rom %{buildroot}%{_datadir}/%{name}/qemu/efi-${qemuname}.rom
done
%endif
%ifarch aarch64
mkdir -p %{buildroot}/%{_datadir}/%{name}/arm64-efi
cp -a src/bin-arm64-efi/snponly.efi %{buildroot}/%{_datadir}/%{name}/arm64-efi/snponly.efi
%endif
%ifarch x86_64
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Thu Apr 2 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20240119-5.gitde8a0821
- Source0 from GitHub archive, %%setup dir matches archive root

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20240119-5.gitde8a0821
- Prepare for Oreon 11 (RP1)
%endif
