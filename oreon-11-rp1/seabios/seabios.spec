%global source0_hash cb708a548e4244c5021590a5e78ab6e331ded1750120b687039042994033a07c
Name:           seabios
Version:        1.17.0
Release:        1%{?dist}
Summary:        Open-source legacy BIOS implementation
License:        LGPL-3.0-only
URL:            http://www.coreboot.org/SeaBIOS
Source0:        http://code.coreboot.org/p/seabios/downloads/get/%{name}-%{version}.tar.gz
Patch0001:      0001-Workaround-for-a-win8.1-32-S4-resume-bug.patch
Patch0003:      0003-vgabios-Reorder-video-modes-to-work-around-a-Windows.patch
Patch0009:      0001-update-release-date.patch
Source10:       config.vga-cirrus
Source11:       config.vga-isavga
Source12:       config.vga-qxl
Source13:       config.vga-stdvga
Source14:       config.vga-vmware
Source15:       config.csm
Source16:       config.coreboot
Source17:       config.seabios-128k
Source18:       config.seabios-256k
Source19:       config.vga-virtio
Source20:       config.vga-ramfb
Source21:       config.vga-bochs-display
Source22:       config.vga-ati
Source23:       config.seabios-microvm
%if 0%{?cross:1}
Buildarch:     noarch
%else
ExclusiveArch: x86_64
%endif
Requires: %{name}-bin = %{version}-%{release}
Requires: seavgabios-bin = %{version}-%{release}
%global debug_package %{nil}
%global _binaries_in_noarch_packages_terminate_build   0
%global debug_level 1
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  python3
# /oreon:deps
%description
SeaBIOS is an open-source legacy BIOS implementation which can be used as
a coreboot payload. It implements the standard BIOS calling interfaces
that a typical x86 proprietary BIOS implements.

%package bin
Summary: Seabios for x86
Buildarch: noarch
Conflicts: libguestfs < 1:1.56.1
%description bin
SeaBIOS is an open-source legacy BIOS implementation which can be used as
a coreboot payload. It implements the standard BIOS calling interfaces
that a typical x86 proprietary BIOS implements.

%package -n seavgabios-bin
Summary: Seavgabios for x86
Buildarch: noarch
%description -n seavgabios-bin
SeaVGABIOS is an open-source VGABIOS implementation.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n seabios-rel-%{version}
%autopatch -p1

%build

%define _lto_cflags %{nil}
export CFLAGS="$RPM_OPT_FLAGS"
mkdir binaries
build_bios() {
    make clean distclean
    cp $1 .config
    echo "CONFIG_DEBUG_LEVEL=%{debug_level}" >> .config
    make oldnoconfig V=1
    make V=1 \
        EXTRAVERSION="-%{release}" \
        PYTHON=python3 \
%if 0%{?cross:1}
        HOSTCC=gcc \
        CC=x86_64-linux-gnu-gcc \
        AS=x86_64-linux-gnu-as \
        LD=x86_64-linux-gnu-ld \
        OBJCOPY=x86_64-linux-gnu-objcopy \
        OBJDUMP=x86_64-linux-gnu-objdump \
        STRIP=x86_64-linux-gnu-strip \
%endif
        $4
    cp out/$2 binaries/$3
}
build_bios %{_sourcedir}/config.seabios-128k bios.bin bios.bin
build_bios %{_sourcedir}/config.seabios-256k bios.bin bios-256k.bin
%global vgaconfigs bochs-display cirrus isavga qxl stdvga ramfb vmware virtio ati
for config in %{vgaconfigs}; do
    build_bios %{_sourcedir}/config.vga-${config} \
               vgabios.bin vgabios-${config}.bin out/vgabios.bin
done
%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/seabios
mkdir -p $RPM_BUILD_ROOT%{_datadir}/seavgabios
install -m 0644 binaries/bios.bin $RPM_BUILD_ROOT%{_datadir}/seabios/bios.bin
install -m 0644 binaries/bios-256k.bin $RPM_BUILD_ROOT%{_datadir}/seabios/bios-256k.bin
install -m 0644 binaries/vgabios*.bin $RPM_BUILD_ROOT%{_datadir}/seavgabios
%oreon_autofiles seavgabios-bin usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n seabios-bin -f %{oreon_filedir}/seabios-bin.list
%files -n seavgabios-bin -f %{oreon_filedir}/seavgabios-bin.list

%changelog

* Thu Apr 2 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.17.0-1
- Source0 from GitHub tag rel-1.17.0 (coreboot.org TLS issues)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.17.0-1
- Prepare for Oreon 11 (RP1)
