# This package calls binutils components directly and would need to pass
# in flags to enable the LTO plugins
# Disable LTO
%global _lto_cflags %{nil}

%undefine _hardened_build
%undefine _package_note_file

%global tarversion 2.12
%undefine _missing_build_ids_terminate_build
%global _configure_gnuconfig_hack 0

# It's a commit from their gnulib's development tree.  They don't do releases,
# and it is *awful* to update this.
%global gnulibversion 9f48fb992a3d7e96610c4ce8be969cff2d61a01b

Name:		grub2
Epoch:		1
Version:	2.12
Release:	55%{?dist}
Summary:	Bootloader with support for Linux, Multiboot and more
License:	GPL-3.0-or-later
URL:		http://www.gnu.org/software/grub/
Obsoletes:	grub < 1:0.98
Source0:	https://ftp.gnu.org/gnu/grub/grub-%{tarversion}.tar.xz
Source1:	grub.macros
Source2:	gnulib-%{gnulibversion}.tar.gz
Source3:	99-grub-mkconfig.install
Source4:	http://unifoundry.com/pub/unifont/unifont-13.0.06/font-builds/unifont-13.0.06.pcf.gz
Source5:	theme.tar.bz2
Source6:	gitignore
Source7:	bootstrap
Source8:	bootstrap.conf
Source9:	strtoull_test.c
Source10:	20-grub.install
Source11:	grub.patches
Source12:	sbat.csv.in
Source13:	gen_grub_cfgstub
Source14:	95-set-boot-entry.install

%include %{SOURCE1}

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	binutils
BuildRequires:	bison
BuildRequires:	bzip2-devel
BuildRequires:	dejavu-sans-fonts
BuildRequires:	device-mapper-devel
BuildRequires:	efi-srpm-macros
BuildRequires:	flex
BuildRequires:	freetype-devel
BuildRequires:	freetype-devel
BuildRequires:	fuse3-devel
BuildRequires:	gcc
BuildRequires:	gettext-devel
BuildRequires:	git
BuildRequires:	help2man
BuildRequires:	ncurses-devel
BuildRequires:	python3
BuildRequires:	rpm-devel
BuildRequires:	rpm-libs
BuildRequires:	squashfs-tools
BuildRequires:	texinfo
BuildRequires:	xz-devel

# For %%_userunitdir and %%systemd_* macros
BuildRequires:	systemd-rpm-macros

%ifarch %{efi_arch}
BuildRequires:	pesign >= 0.99-8
%endif

%if %{?_with_ccache: 1}%{?!_with_ccache: 0}
BuildRequires:	ccache
%endif

ExcludeArch:	s390 s390x %{ix86}
Obsoletes:	grub2 <= %{evr}

%if 0%{with_legacy_arch}
Requires:	grub2-%{legacy_package_arch} = %{evr}
%else
Requires:	grub2-%{package_arch} = %{evr}
%endif

%global desc \
The GRand Unified Bootloader (GRUB) is a highly configurable and \
customizable bootloader with modular architecture.  It supports a rich \
variety of kernel formats, file systems, computer architectures and \
hardware devices.\
%{nil}

# generate with do-rebase
%include %{SOURCE11}

%description
%{desc}

%package common
Summary:	grub2 common layout
BuildArch:	noarch
Conflicts:	grubby < 8.40-18
Requires(posttrans): util-linux-core
Requires(posttrans): coreutils
Requires(posttrans): grep

%description common
This package provides some directories which are required by various grub2
subpackages.

%package tools
Summary:	Support tools for GRUB.
Requires:	grub2-common = %{epoch}:%{version}-%{release}
Requires:	gettext-runtime os-prober file
Requires(pre):	dracut
Requires(pre):	grep
Requires(pre):	sed
%{?systemd_requires}

%description tools
%{desc}
This subpackage provides tools for support of all platforms.

%ifarch x86_64
%package tools-efi
Summary:	Support tools for GRUB.
Requires:	gettext-runtime os-prober file
Requires:	grub2-common = %{epoch}:%{version}-%{release}

%description tools-efi
%{desc}
This subpackage provides tools for support of EFI platforms.
%endif

%package tools-minimal
Summary:	Support tools for GRUB.
Requires:	gettext-runtime
Requires:	grub2-common = %{epoch}:%{version}-%{release}

%description tools-minimal
%{desc}
This subpackage provides tools for support of all platforms.

%package tools-extra
Summary:	Support tools for GRUB.
Requires:	gettext-runtime os-prober file
Requires:	grub2-tools-minimal = %{epoch}:%{version}-%{release}
Requires:	grub2-common = %{epoch}:%{version}-%{release}
Requires:	mtools

%description tools-extra
%{desc}
This subpackage provides tools for support of all platforms.

%if 0%{with_efi_arch}
%{expand:%define_efi_variant %%{package_arch} -o}
%endif
%if 0%{with_alt_efi_arch}
%{expand:%define_efi_variant %%{alt_package_arch}}
%endif
%if 0%{with_legacy_arch}
%{expand:%define_legacy_variant %%{legacy_package_arch}}
%endif
%if 0%{with_xen_arch}
%{expand:%define_xen_variant %%{xen_package_arch} -o}
%endif
%if 0%{with_xen_pvh_arch}
%{expand:%define_xen_pvh_variant %%{xen_pvh_package_arch} -o}
%endif

%if 0%{with_emu_arch}
%package emu
Summary:	GRUB user-space emulation.
Requires:	grub2-tools-minimal = %{epoch}:%{version}-%{release}

%description emu
%{desc}
This subpackage provides the GRUB user-space emulation support of all platforms.

%package emu-modules
Summary:	GRUB user-space emulation modules.
Requires:	grub2-tools-minimal = %{epoch}:%{version}-%{release}

%description emu-modules
%{desc}
This subpackage provides the GRUB user-space emulation modules.
%endif

%prep
%do_common_setup
%if 0%{with_efi_arch}
mkdir grub-%{grubefiarch}-%{tarversion}
grep -A100000 '# stuff "make" creates' .gitignore > grub-%{grubefiarch}-%{tarversion}/.gitignore
cp %{SOURCE4} grub-%{grubefiarch}-%{tarversion}/unifont.pcf.gz
sed -e "s,@@VERSION@@,%{version},g" -e "s,@@VERSION_RELEASE@@,%{version}-%{release},g" \
    %{SOURCE12} > grub-%{grubefiarch}-%{tarversion}/sbat.csv
git add grub-%{grubefiarch}-%{tarversion}
%endif
%if 0%{with_alt_efi_arch}
mkdir grub-%{grubaltefiarch}-%{tarversion}
grep -A100000 '# stuff "make" creates' .gitignore > grub-%{grubaltefiarch}-%{tarversion}/.gitignore
cp %{SOURCE4} grub-%{grubaltefiarch}-%{tarversion}/unifont.pcf.gz
git add grub-%{grubaltefiarch}-%{tarversion}
%endif
%if 0%{with_legacy_arch}
mkdir grub-%{grublegacyarch}-%{tarversion}
grep -A100000 '# stuff "make" creates' .gitignore > grub-%{grublegacyarch}-%{tarversion}/.gitignore
cp %{SOURCE4} grub-%{grublegacyarch}-%{tarversion}/unifont.pcf.gz
git add grub-%{grublegacyarch}-%{tarversion}
%endif
%if 0%{with_emu_arch}
mkdir grub-emu-%{tarversion}
grep -A100000 '# stuff "make" creates' .gitignore > grub-emu-%{tarversion}/.gitignore
cp %{SOURCE4} grub-emu-%{tarversion}/unifont.pcf.gz
git add grub-emu-%{tarversion}
%endif
%if 0%{with_xen_arch}
mkdir grub-%{grubxenarch}-%{tarversion}
grep -A100000 '# stuff "make" creates' .gitignore > grub-%{grubxenarch}-%{tarversion}/.gitignore
cp %{SOURCE4} grub-%{grubxenarch}-%{tarversion}/unifont.pcf.gz
sed -e "s,@@VERSION@@,%{version},g" -e "s,@@VERSION_RELEASE@@,%{version}-%{release},g" \
    %{SOURCE12} > grub-%{grubxenarch}-%{tarversion}/sbat.csv
git add grub-%{grubxenarch}-%{tarversion}
%endif
%if 0%{with_xen_pvh_arch}
mkdir grub-%{grubxenpvharch}-%{tarversion}
grep -A100000 '# stuff "make" creates' .gitignore > grub-%{grubxenpvharch}-%{tarversion}/.gitignore
cp %{SOURCE4} grub-%{grubxenpvharch}-%{tarversion}/unifont.pcf.gz
sed -e "s,@@VERSION@@,%{version},g" -e "s,@@VERSION_RELEASE@@,%{version}-%{release},g" \
    %{SOURCE12} > grub-%{grubxenpvharch}-%{tarversion}/sbat.csv
git add grub-%{grubxenpvharch}-%{tarversion}
%endif
git commit -m "After making subdirs"

%build
%if 0%{with_efi_arch}
%{expand:%do_primary_efi_build %%{grubefiarch} %%{grubefiname} %%{grubeficdname} %%{_target_platform} %%{efi_target_cflags} %%{efi_host_cflags}}
%endif
%if 0%{with_alt_efi_arch}
%{expand:%do_alt_efi_build %%{grubaltefiarch} %%{grubaltefiname} %%{grubalteficdname} %%{_alt_target_platform} %%{alt_efi_target_cflags} %%{alt_efi_host_cflags}}
%endif
%if 0%{with_legacy_arch}
%{expand:%do_legacy_build %%{grublegacyarch}}
%endif
%if 0%{with_emu_arch}
%{expand:%do_emu_build}
%endif
%if 0%{with_xen_arch}
%{expand:%do_xen_build %%{grubxenarch} %%{_target_platform} %%{xen_target_cflags} %%{xen_host_cflags}}
%endif
%if 0%{with_xen_pvh_arch}
%{expand:%do_xen_pvh_build %%{grubxenpvharch} %%{_target_platform} %%{xen_pvh_target_cflags} %%{xen_pvh_host_cflags}}
%endif
%ifarch ppc64le
%{expand:%do_ieee1275_build_images %%{grublegacyarch} %{grubelfname} %{sb_cer} %{sb_key}}
%endif
makeinfo --info --no-split -I docs -o docs/grub-dev.info \
	docs/grub-dev.texi
makeinfo --info --no-split -I docs -o docs/grub.info \
	docs/grub.texi
makeinfo --html --no-split -I docs -o docs/grub-dev.html \
	docs/grub-dev.texi
makeinfo --html --no-split -I docs -o docs/grub.html \
	docs/grub.texi

%install
set -e
rm -fr $RPM_BUILD_ROOT

%do_common_install
%if 0%{with_efi_arch}
%{expand:%do_efi_install %%{grubefiarch} %%{grubefiname} %%{grubeficdname}}
%endif
%if 0%{with_alt_efi_arch}
%{expand:%do_alt_efi_install %%{grubaltefiarch} %%{grubaltefiname} %%{grubalteficdname}}
%endif
%if 0%{with_legacy_arch}
%{expand:%do_legacy_install %%{grublegacyarch} %%{alt_grub_target_name} 0%{with_efi_arch}}
%endif
%if 0%{with_emu_arch}
%{expand:%do_emu_install %%{package_arch}}
%endif
%if 0%{with_xen_arch}
%{expand:%do_xen_install %%{grubxenarch}}
%endif
%if 0%{with_xen_pvh_arch}
%{expand:%do_xen_pvh_install %%{grubxenpvharch}}
%endif
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
ln -s grub2-set-password ${RPM_BUILD_ROOT}/%{_sbindir}/grub2-setpassword
echo '.so man8/grub2-set-password.8' > ${RPM_BUILD_ROOT}/%{_datadir}/man/man8/grub2-setpassword.8
%ifnarch x86_64
rm -vf ${RPM_BUILD_ROOT}/%{_bindir}/grub2-render-label
rm -vf ${RPM_BUILD_ROOT}/%{_sbindir}/grub2-bios-setup
rm -vf ${RPM_BUILD_ROOT}/%{_sbindir}/grub2-macbless
%endif
%{expand:%%do_install_protected_file grub2-tools-minimal}

%find_lang grub

# Install kernel-install scripts
install -d -m 0755 %{buildroot}%{_prefix}/lib/kernel/install.d/
install -D -m 0755 -t %{buildroot}%{_prefix}/lib/kernel/install.d/ %{SOURCE10}
install -D -m 0755 -t %{buildroot}%{_prefix}/lib/kernel/install.d/ %{SOURCE14}
install -D -m 0755 -t %{buildroot}%{_prefix}/lib/kernel/install.d/ %{SOURCE3}
install -d -m 0755 %{buildroot}%{_sysconfdir}/kernel/install.d/
# Install systemd user service to set the boot_success flag
install -D -m 0755 -t %{buildroot}%{_userunitdir} \
	docs/grub-boot-success.{timer,service}
# Install systemd system-update unit to set boot_indeterminate for offline-upd
install -D -m 0755 -t %{buildroot}%{_unitdir} docs/grub-boot-indeterminate.service
install -d -m 0755 %{buildroot}%{_unitdir}/system-update.target.wants
install -d -m 0755 %{buildroot}%{_unitdir}/reboot.target.wants
ln -s ../grub-boot-indeterminate.service \
	%{buildroot}%{_unitdir}/system-update.target.wants
ln -s ../grub2-systemd-integration.service \
	%{buildroot}%{_unitdir}/reboot.target.wants

# Don't run debuginfo on all the grub modules and whatnot; it just
# rejects them, complains, and slows down extraction.
%global finddebugroot "%{_builddir}/%{?buildsubdir}/debug"

%global dip RPM_BUILD_ROOT=%{finddebugroot} %{__debug_install_post}
%define __debug_install_post (						\
	mkdir -p %{finddebugroot}/usr					\
	mv %{buildroot}/usr/bin %{finddebugroot}/usr/bin		\
	[ "%{_sbindir}" != "%{_bindir}" ] &&				\\\
		mv %{buildroot}/usr/sbin %{finddebugroot}/usr/sbin	\
	%{dip}								\
	install -m 0755 -d %{buildroot}/usr/lib/ %{buildroot}/usr/src/	\
	cp -al %{finddebugroot}/usr/lib/debug/				\\\
		%{buildroot}/usr/lib/debug/				\
	cp -al %{finddebugroot}/usr/src/debug/				\\\
		%{buildroot}/usr/src/debug/ )				\
	mv %{finddebugroot}/usr/bin %{buildroot}/usr/bin		\
	[ "%{_sbindir}" != "%{_bindir}" ] &&				\\\
		mv %{finddebugroot}/usr/sbin %{buildroot}/usr/sbin	\
	%{nil}

%undefine buildsubdir

%pre tools
if [ -f /boot/grub2/user.cfg ]; then
    if grep -q '^GRUB_PASSWORD=' /boot/grub2/user.cfg ; then
	sed -i 's/^GRUB_PASSWORD=/GRUB2_PASSWORD=/' /boot/grub2/user.cfg
    fi
elif [ -f %{efi_esp_dir}/user.cfg ]; then
    if grep -q '^GRUB_PASSWORD=' %{efi_esp_dir}/user.cfg ; then
	sed -i 's/^GRUB_PASSWORD=/GRUB2_PASSWORD=/' \
	    %{efi_esp_dir}/user.cfg
    fi
elif [ -f /etc/grub.d/01_users ] && \
	grep -q '^password_pbkdf2 root' /etc/grub.d/01_users ; then
    if [ -f %{efi_esp_dir}/grub.cfg ]; then
	# on EFI we don't get permissions on the file, but
	# the directory is protected.
	grep '^password_pbkdf2 root' /etc/grub.d/01_users | \
		sed 's/^password_pbkdf2 root \(.*\)$/GRUB2_PASSWORD=\1/' \
	    > %{efi_esp_dir}/user.cfg
    fi
    if [ -f /boot/grub2/grub.cfg ]; then
	install -m 0600 /dev/null /boot/grub2/user.cfg
	chmod 0600 /boot/grub2/user.cfg
	grep '^password_pbkdf2 root' /etc/grub.d/01_users | \
		sed 's/^password_pbkdf2 root \(.*\)$/GRUB2_PASSWORD=\1/' \
	    > /boot/grub2/user.cfg
    fi
fi
# ensure we exit 0
:

%post tools
%systemd_user_post grub-boot-success.timer

%preun tools
%systemd_user_preun grub-boot-success.timer

%postun tools
%systemd_user_postun_with_restart grub-boot-success.timer

%triggerpostun tools -- grub2-tools < 1:2.06-107
# grub-boot-success.timer was moved from a hard symlink under /lib/systemd
# to a preset, apply the preset when upgrading from pre-preset versions
/usr/lib/systemd/systemd-update-helper install-user-units grub-boot-success.timer

%posttrans common
set -eu

EFI_HOME=%{grub_efi_dir}
GRUB_HOME=/boot/grub2
ESP_PATH=/boot/efi

if ! mountpoint -q ${ESP_PATH}; then
    exit 0 # no ESP mounted, nothing to do
fi

if test ! -f ${GRUB_HOME}/grub.cfg; then
    # there's no config in GRUB home, create one
    grub2-mkconfig -o ${GRUB_HOME}/grub.cfg
else
    GRUB_CFG_MODE=$(stat --format="%a" ${GRUB_HOME}/grub.cfg)
    if ! test "${GRUB_CFG_MODE}" = "600"; then
        # when upgrading from <=2.06-126 to newer versions, the grub config stub
        # may have different mode than 0600, so set the latter if this is the case
        chmod 0600 ${GRUB_HOME}/grub.cfg
    fi
fi

if test -f ${EFI_HOME}/grub.cfg; then
    if (((grep -q "configfile" ${EFI_HOME}/grub.cfg && grep -q "root-dev-only" ${EFI_HOME}/grub.cfg) || grep -q "source" ${EFI_HOME}/grub.cfg) && ! grep -q "# It is automatically generated by grub2-mkconfig using templates" ${EFI_HOME}/grub.cfg); then
        exit 0 #Already unified
    fi
fi

# create a stub grub2 config in EFI
gen_grub_cfgstub $GRUB_HOME $EFI_HOME || :

if test -f ${EFI_HOME}/grubenv; then
    cp -a ${EFI_HOME}/grubenv ${EFI_HOME}/grubenv.rpmsave
    mv --force ${EFI_HOME}/grubenv ${GRUB_HOME}/grubenv
fi

%if 0%{with_efi_arch}
%posttrans efi-%{efiarch}
set -eu

# On image mode, bootupd takes care of installing bootloader updates to the ESP
if [[ ! -e "/run/ostree-booted" ]]; then
    cp -a %{grub_efi_dir}/. %{efi_esp_dir} || :
fi

%endif

%files common -f grub.lang
%dir %{_libdir}/grub/
%dir %{_datarootdir}/grub/
%attr(0700,root,root) %dir %{_sysconfdir}/grub.d
%{_prefix}/lib/kernel/install.d/20-grub.install
%{_prefix}/lib/kernel/install.d/95-set-boot-entry.install
%{_prefix}/lib/kernel/install.d/99-grub-mkconfig.install
%dir %{_datarootdir}/grub
%exclude %{_datarootdir}/grub/*
%dir /boot/grub2
%dir /boot/grub2/themes/
%dir /boot/grub2/themes/system
%attr(0700,root,root) %dir /boot/grub2
%exclude /boot/grub2/*
%exclude %{grub_efi_dir}/*
%ghost %config(noreplace) %verify(not size mode md5 mtime) /boot/grub2/grubenv
%license COPYING
%doc THANKS
%doc docs/grub.html
%doc docs/grub-dev.html
%doc docs/font_char_metrics.png

%files tools-minimal
%{_sbindir}/grub2-get-kernel-settings
%{_sbindir}/grub2-probe
%attr(4755, root, root) %{_sbindir}/grub2-set-bootflag
%{_sbindir}/grub2-set-default
%{_sbindir}/grub2-set*password
%{_bindir}/grub2-editenv
%{_bindir}/grub2-mkpasswd-pbkdf2
%{_bindir}/grub2-mount
%attr(0644,root,root) %config(noreplace) /etc/dnf/protected.d/grub2-tools-minimal.conf

%{_datadir}/man/man3/grub2-get-kernel-settings*
%{_datadir}/man/man8/grub2-set-default*
%{_datadir}/man/man8/grub2-set*password*
%{_datadir}/man/man1/grub2-editenv*
%{_datadir}/man/man1/grub2-mkpasswd-*

%ifarch x86_64
%files tools-efi
%{_bindir}/grub2-glue-efi
%{_bindir}/grub2-render-label
%{_sbindir}/grub2-macbless
%{_datadir}/man/man1/grub2-glue-efi*
%{_datadir}/man/man1/grub2-render-label*
%{_datadir}/man/man8/grub2-macbless*
%endif

%files tools
%attr(0644,root,root) %ghost %config(noreplace) %{_sysconfdir}/default/grub
%config %{_sysconfdir}/grub.d/??_*
%{_sysconfdir}/grub.d/README
%{_userunitdir}/grub-boot-success.timer
%{_userunitdir}/grub-boot-success.service
%{_unitdir}/grub-boot-indeterminate.service
%{_unitdir}/system-update.target.wants
%{_unitdir}/grub2-systemd-integration.service
%{_unitdir}/reboot.target.wants
%{_unitdir}/systemd-logind.service.d
%{_infodir}/grub2*
%{_datarootdir}/grub/*
%{_sbindir}/grub2-install
%exclude %{_datarootdir}/grub/themes
%exclude %{_datarootdir}/grub/*.h
%{_datarootdir}/bash-completion/completions/grub
%{_sbindir}/grub2-mkconfig
%{_sbindir}/grub2-switch-to-blscfg
%{_sbindir}/grub2-reboot
%{_bindir}/grub2-file
%{_bindir}/grub2-menulst2cfg
%{_bindir}/grub2-mkimage
%{_bindir}/grub2-mkrelpath
%{_bindir}/grub2-script-check
%{_libexecdir}/grub2
%{_datadir}/man/man?/*

# exclude man pages from tools-extra
%exclude %{_datadir}/man/man8/grub2-sparc64-setup*
%exclude %{_datadir}/man/man1/grub2-fstest*
%exclude %{_datadir}/man/man1/grub2-glue-efi*
%exclude %{_datadir}/man/man1/grub2-kbdcomp*
%exclude %{_datadir}/man/man1/grub2-mkfont*
%exclude %{_datadir}/man/man1/grub2-mklayout*
%exclude %{_datadir}/man/man1/grub2-mknetdir*
%exclude %{_datadir}/man/man1/grub2-mkrescue*
%exclude %{_datadir}/man/man1/grub2-mkstandalone*
%exclude %{_datadir}/man/man1/grub2-syslinux2cfg*

# exclude man pages from tools-minimal
%exclude %{_datadir}/man/man3/grub2-get-kernel-settings*
%exclude %{_datadir}/man/man8/grub2-set-default*
%exclude %{_datadir}/man/man8/grub2-set*password*
%exclude %{_datadir}/man/man1/grub2-editenv*
%exclude %{_datadir}/man/man1/grub2-mkpasswd-*
%exclude %{_datadir}/man/man8/grub2-macbless*
%exclude %{_datadir}/man/man1/grub2-render-label*

%if %{with_legacy_arch}
%ifarch x86_64
%{_sbindir}/grub2-bios-setup
%else
%exclude %{_sbindir}/grub2-bios-setup
%exclude %{_datadir}/man/man8/grub2-bios-setup*
%endif
%ifarch %{sparc}
%{_sbindir}/grub2-sparc64-setup
%else
%exclude %{_sbindir}/grub2-sparc64-setup
%exclude %{_datadir}/man/man8/grub2-sparc64-setup*
%endif
%ifarch %{sparc} ppc ppc64 ppc64le
%{_sbindir}/grub2-ofpathname
%else
%exclude %{_sbindir}/grub2-ofpathname
%exclude %{_datadir}/man/man8/grub2-ofpathname*
%endif
%endif

%files tools-extra
%{_bindir}/grub2-fstest
%{_bindir}/grub2-kbdcomp
%{_bindir}/grub2-mkfont
%{_bindir}/grub2-mklayout
%{_bindir}/grub2-mknetdir
%ifnarch %{sparc}
%{_bindir}/grub2-mkrescue
%{_datadir}/man/man1/grub2-mkrescue*
%else
%exclude %{_datadir}/man/man1/grub2-mkrescue*
%endif
%{_bindir}/grub2-mkstandalone
%{_bindir}/grub2-syslinux2cfg
%{_sysconfdir}/sysconfig/grub
%{_datadir}/man/man1/grub2-fstest*
%{_datadir}/man/man1/grub2-kbdcomp*
%{_datadir}/man/man1/grub2-mkfont*
%{_datadir}/man/man1/grub2-mklayout*
%{_datadir}/man/man1/grub2-mknetdir*
%{_datadir}/man/man1/grub2-mkstandalone*
%{_datadir}/man/man1/grub2-syslinux2cfg*
%exclude %{_bindir}/grub2-glue-efi
%exclude %{_sbindir}/grub2-sparc64-setup
%exclude %{_sbindir}/grub2-ofpathname
%exclude %{_datadir}/man/man1/grub2-glue-efi*
%exclude %{_datadir}/man/man8/grub2-ofpathname*
%exclude %{_datadir}/man/man8/grub2-sparc64-setup*
%exclude %{_datarootdir}/grub/themes/starfield

%if 0%{with_efi_arch}
%{expand:%define_efi_variant_files %%{package_arch} %%{grubefiname} %%{grubeficdname} %%{grubefiarch} %%{target_cpu_name} %%{grub_target_name}}
%endif
%if 0%{with_alt_efi_arch}
%{expand:%define_efi_variant_files %%{alt_package_arch} %%{grubaltefiname} %%{grubalteficdname} %%{grubaltefiarch} %%{alt_target_cpu_name} %%{alt_grub_target_name}}
%endif
%if 0%{with_legacy_arch}
%{expand:%define_legacy_variant_files %%{legacy_package_arch} %%{grublegacyarch}}
%endif
%if 0%{with_xen_arch}
%{expand:%define_xen_variant_files %%{xen_package_arch} %%{xen_grub_target_name}}
%endif
%if 0%{with_xen_pvh_arch}
%{expand:%define_xen_pvh_variant_files %%{xen_pvh_package_arch} %%{xen_pvh_grub_target_name}}
%endif

%if 0%{with_emu_arch}
%files emu
%{_bindir}/grub2-emu*
%{_datadir}/man/man1/grub2-emu*

%files emu-modules
%{_libdir}/grub/%{emuarch}-emu/*
%exclude %{_libdir}/grub/%{emuarch}-emu/*.module
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.12-55
- Prepare for Oreon 11 (RP1)
