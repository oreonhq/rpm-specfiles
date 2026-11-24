# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash f06094db841a214f975e79d66e2a79ea8c2b39b0f762e9d384b2feffd4ae7447
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           os-prober
Version:        1.85
Release:        1%{?dist}
Summary:        Probes disks on the system for installed operating systems

License:        GPL-2.0-or-later AND GPL-1.0-or-later
URL:            https://salsa.debian.org/installer-team/os-prober
Source0:        https://deb.debian.org/debian/pool/main/o/os-prober/%{name}_%{version}.tar.xz
Patch0:         os-prober-no-dummy-mach-kernel.patch
Patch1:         os-prober-mdraidfix.patch
Patch2:         os-prober-btrfsfix.patch
Patch3:         os-prober-bootpart-name-fix.patch
Patch4:         os-prober-mounted-partitions-fix.patch
Patch5:         os-prober-factor-out-logger.patch
Patch6:         os-prober-factored-logger-efi-fix.patch
Patch7:         os-prober-umount-fix.patch
Patch8:         os-prober-grub2-parsefix.patch
Patch9:         os-prober-grepfix.patch
Patch10:        os-prober-grub2-mount-workaround.patch
Patch11:        os-prober-arm64-win11.patch
Patch13:        os-prober-trap_unmount.patch
Patch14:        os-prober-90fallback-include-possible-kernel-parameters-from-g.patch
Patch15:        os-prober-common.sh-do-not-resolve-symbolic-link-on-mapped-dev.patch
Patch16:        os-prober-arm64-efi-fd-result-fix.patch

Requires:       udev coreutils util-linux
Requires:       grep /bin/sed /sbin/modprobe
Requires:       grub2-tools-minimal

BuildRequires: oreon-rpm-macros
BuildRequires: make
BuildRequires:  clang
BuildRequires:  git

%description
This package detects other OSes available on a system and outputs the results
in a generic machine-readable format. Support for new OSes and Linux
distributions can be added easily. 

%prep
%oreon_sha256
%autosetup -n %{name}-%{version} -S git

mkdir -p os-probes/mounted/riscv64/
cp -p os-probes/mounted/arm64/05efi os-probes/mounted/riscv64/05efi

find -type f -exec sed -i -e 's|usr/lib|usr/libexec|g' {} \;
sed -i -e 's|grub-probe|grub2-probe|g' os-probes/common/50mounted-tests \
     linux-boot-probes/common/50mounted-tests
sed -i -e 's|grub-mount|grub2-mount|g' os-probes/common/50mounted-tests \
     linux-boot-probes/common/50mounted-tests common.sh

%build
%set_build_flags
%make_build CC=%{__cc} LDFLAGS="$LDFLAGS -fPIC" CFLAGS="$CFLAGS" CPPFLAGS="$CPPFLAGS"

%install
install -m 0755 -d %{buildroot}%{_bindir}
install -m 0755 -d %{buildroot}%{_var}/lib/%{name}

install -m 0755 -p os-prober linux-boot-prober %{buildroot}%{_bindir}
install -m 0755 -Dp newns %{buildroot}%{_libexecdir}/os-prober/newns
install -m 0644 -Dp common.sh %{buildroot}%{_datadir}/%{name}/common.sh

%ifarch m68k
ARCH=m68k
%endif
%ifarch ppc ppc64
ARCH=powerpc
%endif
%ifarch sparc sparc64
ARCH=sparc
%endif
%ifarch %{ix86} x86_64
ARCH=x86
%endif
%ifarch aarch64
ARCH=arm64
%endif
%ifarch riscv64
ARCH=riscv64
%endif

for probes in os-probes os-probes/mounted os-probes/init \
              linux-boot-probes linux-boot-probes/mounted; do
        install -m 755 -d %{buildroot}%{_libexecdir}/$probes 
        cp -a $probes/common/* %{buildroot}%{_libexecdir}/$probes
        if [ -e "$probes/$ARCH" ]; then 
                cp -a $probes/$ARCH/* %{buildroot}%{_libexecdir}/$probes 
        fi
done
if [ "$ARCH" = x86 ]; then
        install -m 755 -p os-probes/mounted/powerpc/20macosx \
            %{buildroot}%{_libexecdir}/os-probes/mounted
fi

%files
%doc README TODO debian/changelog
%license debian/copyright
%{_bindir}/*
%{_libexecdir}/*
%{_datadir}/%{name}
%{_var}/lib/%{name}

%changelog
%autochangelog
