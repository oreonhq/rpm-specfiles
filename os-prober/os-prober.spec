Name:           os-prober
Version:        1.81
Release:        11%{?dist}
Summary:        Probes disks on the system for installed operating systems

# For more information about licensing, see copyright file.
License:        GPL-2.0-or-later AND GPL-1.0-or-later
URL:            http://kitenet.net/~joey/code/os-prober/
Source0:        http://ftp.us.debian.org/debian/pool/main/o/os-prober/%{name}_%{version}.tar.xz
Patch0:         os-prober-no-dummy-mach-kernel.patch
# Sent upstream
Patch1:         os-prober-mdraidfix.patch
Patch2:         os-prober-btrfsfix.patch
Patch3:         os-prober-bootpart-name-fix.patch
Patch4:         os-prober-mounted-partitions-fix.patch
Patch5:         os-prober-factor-out-logger.patch
# To be sent upstream
Patch6:         os-prober-factored-logger-efi-fix.patch
Patch7:         os-prober-umount-fix.patch
Patch8:         os-prober-grub2-parsefix.patch
Patch9:         os-prober-grepfix.patch
Patch10:        os-prober-grub2-mount-workaround.patch
Patch11:        os-prober-arm64-win11.patch
Patch12:        os-prober-efi-shell.patch
Patch13:        os-prober-trap_unmount.patch
Patch14:        os-prober-90fallback-include-possible-kernel-parameters-from-g.patch
Patch15:        os-prober-common.sh-do-not-resolve-symbolic-link-on-mapped-dev.patch

Requires:       udev coreutils util-linux
Requires:       grep /bin/sed /sbin/modprobe
Requires:       grub2-tools-minimal

BuildRequires: make
BuildRequires:  gcc git

%description
This package detects other OSes available on a system and outputs the results
in a generic machine-readable format. Support for new OSes and Linux
distributions can be added easily. 

%prep
%autosetup -n %{name}-%{version} -S git

find -type f -exec sed -i -e 's|usr/lib|usr/libexec|g' {} \;
sed -i -e 's|grub-probe|grub2-probe|g' os-probes/common/50mounted-tests \
     linux-boot-probes/common/50mounted-tests
sed -i -e 's|grub-mount|grub2-mount|g' os-probes/common/50mounted-tests \
     linux-boot-probes/common/50mounted-tests common.sh

%build
%set_build_flags
%make_build LDFLAGS="$LDFLAGS -fPIC" CFLAGS="$CFLAGS" CPPFLAGS="$CPPFLAGS"

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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.81-11
- Prepare for Oreon 11 (RP1)
