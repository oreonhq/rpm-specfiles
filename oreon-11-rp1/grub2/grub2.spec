# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash bc8d3c73535b8838d8c8e2654d73edc4e6ae8c8acdb45d5df5dc9a1547446d43
%global source2_hash 00a25a5c3a18d9d7b0deb456344f7ab02f6f9ef8422fbe6174afafc546c8ee36
%global source4_hash aea0ea746353c6c2b5b8874e65facd087bb0346ec198993f8aaaa21eea040378
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global _lto_cflags %{nil}

%undefine _hardened_build
%undefine _package_note_file

%global tarversion 2.14
%undefine _missing_build_ids_terminate_build
%global _configure_gnuconfig_hack 0

%global gnulibversion 9f48fb992a3d7e96610c4ce8be969cff2d61a01b

Name:		grub2
Epoch:		1
Version:	2.14
Release:	1%{?dist}
Summary:	Bootloader with support for Linux, Multiboot and more
License:	GPL-3.0-or-later
URL:		http://www.gnu.org/software/grub/
Obsoletes:	grub < 1:0.98
Source0:	https://ftp.gnu.org/gnu/grub/grub-%{tarversion}.tar.xz
Source2:	https://github.com/coreutils/gnulib/archive/%{gnulibversion}.tar.gz#/gnulib-%{gnulibversion}.tar.gz
Source3:	99-grub-mkconfig.install
Source4:	https://unifoundry.com/pub/unifont/unifont-13.0.06/font-builds/unifont-13.0.06.pcf.gz
Source6:	gitignore
Source7:	bootstrap
Source8:	bootstrap.conf
Source9:	strtoull_test.c
Source10:	20-grub.install
Source12:	sbat.csv.in
Source13:	gen_grub_cfgstub
Source14:	95-set-boot-entry.install

%global evr %{epoch}:%{version}-%{release}
%global _libdir %{_exec_prefix}/lib

%global grub_evr_dir %{_libdir}/efi/grub2/%{evr}
%global grub_efi_dir %{grub_evr_dir}/EFI/%{efi_vendor}

%global _binaries_in_noarch_packages_terminate_build 0
%{expand:%%{!?buildsubdir:%%global buildsubdir grub-%{tarversion}}}
%{expand:%%{!?_licensedir:%%global license %%%%doc}}

%global _configure ../configure

%if %{?_with_ccache: 1}%{?!_with_ccache: 0}
%global ccpath /usr/%{_lib}/ccache/clang
%else
%global ccpath %{__cc}
%endif

%ifarch aarch64
%global cc_equals "CC=%{ccpath} --start-no-unused-arguments -fuse-ld=bfd --end-no-unused-arguments -fPIE -Wl,-z,noexecstack -Wl,--no-warn-rwx-segments -mbranch-protection=standard"
%else
%global cc_equals "CC=%{ccpath} --start-no-unused-arguments -fuse-ld=bfd --end-no-unused-arguments -fPIE -Wl,-z,noexecstack -Wl,--no-warn-rwx-segments"
%endif

%global cflags_sed						\\\
	sed							\\\
		-e 's/-O. //g'					\\\
		-e 's/-fplugin=annobin//g'			\\\
		-e 's,-specs=[[:alnum:]/_-]*annobin[[:alnum:]_-]*,,g' \\\
		-e 's/-fstack-protector[[:alpha:]-]\\+//g'	\\\
		-e 's/-[^ ]*D_FORTIFY_SOURCE=[[:digit:]][^ ]*\\+//g'	\\\
		-e 's/--param=ssp-buffer-size=4//g'		\\\
		-e 's/-mregparm=3/-mregparm=4/g'		\\\
		-e 's/-fexceptions//g'				\\\
		-e 's/-fcf-protection//g'			\\\
		-e 's/-fasynchronous-unwind-tables//g'		\\\
		-e 's,--config=[^ ]*oreon-hardened-clang.cfg,,g'	\\\
		-e 's/-mprefer-vector-width=[[:digit:]]*//g'	\\\
		-e 's/^/ -fno-strict-aliasing /'		\\\
		%{nil}

%global host_cflags_ %{expand:%%(echo %{build_cflags} %{?_hardening_cflags} | %{cflags_sed})} -fPIE -fstack-protector-strong
%ifarch x86_64
%global host_cflags %{host_cflags_} -fcf-protection
%else
%global host_cflags %{host_cflags_}
%endif
%global legacy_host_cflags					\\\
	%{expand:%%(echo %{host_cflags} |			\\\
	sed							\\\
		-e 's/-m64//g'					\\\
		-e 's/-mcpu=power[[:alnum:]]\\+/-mcpu=power6/g'	\\\
	)}
%global efi_host_cflags %{expand:%%(echo %{host_cflags})}
%global xen_host_cflags %{expand:%%(echo %{host_cflags})}
%global xen_pvh_host_cflags %{expand:%%(echo %{host_cflags})}

%global target_cflags %{expand:%%(echo %{build_cflags} | %{cflags_sed})}
%global legacy_target_cflags					\\\
	%{expand:%%(echo %{target_cflags} | 			\\\
	%{cflags_sed}						\\\
		-e 's/-m64//g'					\\\
		-e 's/-mcpu=power[[:alnum:]]\\+/-mcpu=power6/g'	\\\
	)}
%global efi_target_cflags %{expand:%%(echo %{target_cflags})}
%global xen_target_cflags %{expand:%%(echo %{target_cflags})}
%global xen_pvh_target_cflags %{expand:%%(echo %{target_cflags})}

%global ldflags_sed						\\\
	sed							\\\
		-e 's,-specs=[[:alnum:]/_-]*annobin[[:alnum:]_-]*,,g' \\\
		-e 's,--config=[^ ]*oreon-hardened-clang-ld.cfg,,g' \\\
		-e 's/-fuse-ld=[[:alnum:]]*//g'		\\\
		-e 's/^$//'					\\\
		%{nil}

%global host_ldflags %{expand:%%(echo %{build_ldflags} %{?_hardening_ldflags} | %{ldflags_sed}) -pie}
%global legacy_host_ldflags					\\\
	%{expand:%%(echo %{host_ldflags} |			\\\
	%{ldflags_sed}						\\\
	)}
%global efi_host_ldflags %{expand:%%(echo %{host_ldflags})}
%global xen_host_ldflags %{expand:%%(echo %{host_ldflags})}
%global xen_pvh_host_ldflags %{expand:%%(echo %{host_ldflags})}

%global target_ldflags %{expand:%%(echo %{build_ldflags} -Wl,--no-warn-rwx-segments -static | %{ldflags_sed})}
%global legacy_target_ldflags					\\\
	%{expand:%%(echo %{target_ldflags} | 			\\\
	%{ldflags_sed}						\\\
	)}
%global efi_target_ldflags %{expand:%%(echo %{target_ldflags})}
%global xen_target_ldflags %{expand:%%(echo %{target_ldflags})}
%global xen_pvh_target_ldflags %{expand:%%(echo %{target_ldflags})}

%global with_efi_arch 0
%global with_alt_efi_arch 0
%global with_efi_cc 0
%global with_legacy_arch 0
%global with_emu_arch 1
%global with_xen_arch 0
%global with_xen_pvh_arch 0
%global emuarch %{_arch}
%global grubefiarch %{nil}
%global grublegacyarch %{nil}
%global grubelfname %{nil}
%global xen_package_arch %{nil}
%global xen_pvh_package_arch %{nil}

%ifarch %{sparc}
%global target_cpu_name sparc64
%global _target_platform %{target_cpu_name}-%{_vendor}-%{_target_os}%{?_gnu}
%global legacy_target_cpu_name %{_arch}
%global legacy_package_arch ieee1275
%global platform ieee1275
%endif
%ifarch ppc ppc64 ppc64le
%global with_emu_arch 0
%global target_cpu_name %{_arch}
%global legacy_target_cpu_name powerpc
%global legacy_package_arch %{_arch}
%global legacy_grub_dir powerpc-ieee1275
%global _target_platform %{target_cpu_name}-%{_vendor}-%{_target_os}%{?_gnu}
%global platform ieee1275
%endif

%global efi_only aarch64 %{arm} riscv64
%global efi_arch x86_64 ia64 %{efi_only}
%global efi_cc aarch64 x86_64
%ifarch %{efi_arch}
%global with_efi_arch 1
%else
%global with_efi_arch 0
%endif
%ifarch %{efi_only}
%global with_efi_only 1
%else
%global with_efi_only 0
%endif
%ifarch %{efi_cc}
%global with_efi_cc 1
%else
%global with_efi_cc 0
%endif
%{!?with_efi_arch:%global without_efi_arch 0}
%{?with_efi_arch:%global without_efi_arch 1}
%{!?with_efi_only:%global without_efi_only 0}
%{?with_efi_only:%global without_efi_only 1}
%{!?with_efi_cc:%global without_efi_cc 0}
%{?with_efi_cc:%global without_efi_cc 1}

%ifarch %{efi_arch}
%global efi_modules " efi_netfs efifwsetup efinet lsefi lsefimmap connectefi bli "
%endif

%global xen_arch x86_64
%ifarch %{xen_arch}
%global with_xen_arch 1
%else
%global with_xen_arch 0
%endif
%{!?with_xen_arch:%global without_xen_arch 0}
%{?with_xen_arch:%global without_xen_arch 1}

%global xen_pvh_arch x86_64
%ifarch %{xen_pvh_arch}
%global with_xen_pvh_arch 1
%else
%global with_xen_pvh_arch 0
%endif
%{!?with_xen_pvh_arch:%global without_xen_pvh_arch 0}
%{?with_xen_pvh_arch:%global without_xen_pvh_arch 1}

%ifarch x86_64 %{ix86}
%global platform_modules " backtrace chain tpm usb usbserial_common usbserial_pl2303 usbserial_ftdi usbserial_usbdebug keylayouts at_keyboard play "
%endif

%ifarch ppc64le
%global platform_modules " appendedsig tpm ofnet "
%endif

%ifarch aarch64 %{arm} riscv64
%global platform_modules " chain "
%endif

%ifarch aarch64 %{arm} riscv64
%global legacy_provides -l
%endif

%ifarch %{ix86}
%global efiarch ia32
%global target_cpu_name i386
%global grub_target_name i386-efi
%global package_arch efi-ia32

%global legacy_target_cpu_name i386
%global legacy_package_arch pc
%global platform pc
%endif

%ifarch x86_64
%global efiarch x64
%global target_cpu_name %{_arch}
%global grub_target_name %{_arch}-efi
%global package_arch efi-x64
%global xen_package_arch xen-x64
%global xen_pvh_package_arch xen_pvh-i386

%global legacy_target_cpu_name i386
%global legacy_package_arch pc
%global platform pc

%global xen_grub_target_name %{_arch}-xen
%global xen_pvh_grub_target_name i386-xen_pvh
%global grubxenarch %{xen_grub_target_name}
%global grubxenpvharch %{xen_pvh_grub_target_name}

%global alt_efi_arch ia32
%global alt_target_cpu_name i386
%global alt_grub_target_name i386-efi
%global alt_platform efi
%global alt_package_arch efi-ia32

%global alt_efi_host_cflags %{expand:%%(echo %{efi_host_cflags})}
%global alt_efi_target_cflags					\\\
	%{expand:%%(echo %{target_cflags} |			\\\
	%{cflags_sed}						\\\
		-e 's/-m64//g'					\\\
	)}
%endif

%ifarch aarch64
%global emuarch arm64
%global efiarch aa64
%global target_cpu_name aarch64
%global grub_target_name arm64-efi
%global package_arch efi-aa64
%endif

%ifarch riscv64
%global emuarch riscv64
%global efiarch riscv64
%global target_cpu_name riscv64
%global grub_target_name riscv64-efi
%global package_arch efi-riscv64
%endif

%ifarch %{arm}
%global efiarch arm
%global target_cpu_name arm
%global grub_target_name arm-efi
%global package_arch efi-arm
%global efi_target_cflags						\\\
	%{expand:%%(echo %{optflags} |					\\\
	%{cflags_sed}							\\\
		-e 's/-march=armv7-a[[:alnum:]+-]*/&+nofp/g'		\\\
		-e 's/-mfpu=[[:alnum:]-]\\+//g'				\\\
		-e 's/-mfloat-abi=[[:alpha:]]\\+/-mfloat-abi=soft/g'	\\\
	)}
%endif

%global _target_platform %{target_cpu_name}-%{_vendor}-%{_target_os}%{?_gnu}
%global _alt_target_platform %{alt_target_cpu_name}-%{_vendor}-%{_target_os}%{?_gnu}

%ifarch %{efi_arch}
%global with_efi_arch 1
%global grubefiname grub%{efiarch}.efi
%global grubeficdname gcd%{efiarch}.efi
%global grubefiarch %{target_cpu_name}-efi
%ifarch %{ix86}
%global with_efi_modules 0
%global without_efi_modules 1
%else
%global with_efi_modules 1
%global without_efi_modules 0
%endif
%endif

%if 0%{?alt_efi_arch:1}
%global with_alt_efi_arch 1
%global grubaltefiname grub%{alt_efi_arch}.efi
%global grubalteficdname gcd%{alt_efi_arch}.efi
%global grubaltefiarch %{alt_target_cpu_name}-efi
%endif

%ifnarch %{efi_only}
%global with_legacy_arch 1
%global grublegacyarch %{legacy_target_cpu_name}-%{platform}
%global moduledir %{legacy_target_cpu_name}-%{platform}
%global grubelfname core.elf
%endif

%ifarch x86_64
%global with_efi_common 1
%global with_legacy_modules 1
%global with_legacy_common 1
%else
%global with_efi_common 0
%global with_legacy_common 1
%global with_legacy_modules 1
%endif

%define define_legacy_variant()						\
%{expand:%%package %%{1}}						\
Summary:	Bootloader with support for Linux, Multiboot, and more	\
Provides:	grub2 = %{evr}					\
Obsoletes:	grub2 < %{evr}					\
Requires:	grub2-common = %{evr}					\
Requires:	grub2-tools-minimal = %{evr}				\
Requires:	grub2-%{1}-modules = %{evr}				\
Requires:	gettext-runtime file					\
Requires:	grub2-tools = %{evr}					\
Requires(pre):	dracut							\
Requires(post): dracut							\
%{expand:%%description %%{1}}						\
%{desc}									\
This subpackage provides support for %{1} systems.			\
									\
%{expand:%%{?!buildsubdir:%%define buildsubdir grub-%%{1}-%{tarversion}}}\
%{expand:%%if 0%%{with_legacy_modules}					\
%%package %%{1}-modules							\
Summary:	Modules used to build custom grub images		\
BuildArch:	noarch							\
Requires:	grub2-common = %%{evr}				\
%%description %%{1}-modules						\
%%{desc}								\
This subpackage provides support for rebuilding your own grub.efi.	\
%%endif									\
}									\
									\
%{expand:%%{?!buildsubdir:%%define buildsubdir grub-%%{1}-%{tarversion}}}\
%{expand:%%package %%{1}-tools}						\
Summary:	Support tools for GRUB.					\
Requires:	gettext-runtime os-prober file system-logos	\
Requires:	grub2-common = %{evr}					\
Requires:	grub2-tools-minimal = %{evr}				\
Requires:	os-prober >= 1.58-11					\
									\
%{expand:%%description %%{1}-tools}					\
%{desc}									\
This subpackage provides tools for support of %%{1} platforms.		\
%{nil}

%define define_efi_variant(o)						\
%{expand:%%package %{1}}						\
Summary:	GRUB for EFI systems.					\
Requires:	efi-filesystem						\
Requires:	grub2-common = %{evr}					\
Requires:	grub2-tools-minimal >= %{evr}				\
Requires:	grub2-tools = %{evr}					\
Provides:	grub2-efi = %{evr}					\
%{?legacy_provides:Provides:	grub2 = %{evr}}			\
%{-o:Obsoletes:	grub2-efi < %{evr}}					\
									\
%{expand:%%description %{1}}						\
%{desc}									\
This subpackage provides support for %{1} systems.			\
									\
%{expand:%%{?!buildsubdir:%%define buildsubdir grub-%{1}-%{tarversion}}}\
%{expand:%if 0%{?with_efi_modules}					\
%{expand:%%package %{1}-modules}					\
Summary:	Modules used to build custom grub.efi images		\
BuildArch:	noarch							\
Requires:	grub2-common = %{evr}					\
Provides:	grub2-efi-modules = %{evr}				\
Obsoletes:	grub2-efi-modules < %{evr}				\
%{expand:%%description %{1}-modules}					\
%{desc}									\
This subpackage provides support for rebuilding your own grub.efi.	\
%endif}									\
									\
%{expand:%%package %{1}-cdboot}						\
Summary:	Files used to boot removeable media with EFI		\
Requires:	grub2-common = %{evr}					\
Provides:	grub2-efi-cdboot = %{evr}				\
%{expand:%%description %{1}-cdboot}					\
%{desc}									\
This subpackage provides optional components of grub used with removeable media on %{1} systems.\
%{nil}

%define define_xen_variant(o)						\
%{expand:%%{?!buildsubdir:%%define buildsubdir grub-%{1}-%{tarversion}}}\
%{expand:%%package %{1}-modules}					\
Summary:	Modules used to build custom grub-%{xen_grub_target_name}.bin images		\
BuildArch:	noarch							\
Requires:	grub2-tools = %{evr}					\
Provides:	grub2-xen-modules = %{evr}				\
Obsoletes:	grub2-xen-modules < %{evr}				\
%{expand:%%description %{1}-modules}					\
%{desc}									\
This subpackage provides support for rebuilding your own grub-%{xen_grub_target_name}.bin.	\
%{nil}

%define define_xen_pvh_variant(o)						\
%{expand:%%{?!buildsubdir:%%define buildsubdir grub-%{1}-%{tarversion}}}\
%{expand:%%package %{1}-modules}					\
Summary:	Modules used to build custom grub-%{xen_pvh_grub_target_name}.bin images		\
BuildArch:	noarch							\
Requires:	grub2-tools = %{evr}					\
Provides:	grub2-xen_pvh-modules = %{evr}				\
Obsoletes:	grub2-xen_pvh-modules < %{evr}				\
%{expand:%%description %{1}-modules}					\
%{desc}									\
This subpackage provides support for rebuilding your own grub-%{xen_pvh_grub_target_name}.bin.	\
%{nil}

%global do_common_setup()					\
%setup -q -n grub-%{tarversion}					\
rm -fv docs/*.info						\
cp %{SOURCE6} .gitignore					\
cp %{SOURCE7} bootstrap						\
cp %{SOURCE8} bootstrap.conf					\
cp %{SOURCE9} ./grub-core/tests/strtoull_test.c			\
cp %{SOURCE2} gnulib-%{gnulibversion}.tar.gz			\
tar -zxf gnulib-%{gnulibversion}.tar.gz				\
mv gnulib-%{gnulibversion} gnulib				\
git init							\
echo '![[:digit:]][[:digit:]]_*.in' > util/grub.d/.gitignore	\
echo '!*.[[:digit:]]' > util/.gitignore				\
echo '!config.h' > include/grub/emu/.gitignore			\
git config user.email "packaging@oreonhq.com"		\
git config user.name "Oreon Packaging"				\
git config gc.auto 0						\
rm -f configure							\
git add .							\
git commit -a -q -m "%{tarversion} baseline."			\
git am --whitespace=nowarn %%{patches} </dev/null		\
rm -r build-aux m4						\
./bootstrap							\
%{nil}

%define do_efi_configure()					\
%configure							\\\
	%{cc_equals}						\\\
	HOST_CFLAGS="%{3}"					\\\
	HOST_CPPFLAGS="-I$(pwd)"				\\\
	HOST_LDFLAGS="%{efi_host_ldflags}"			\\\
	TARGET_CFLAGS="%{2}"					\\\
	TARGET_CPPFLAGS="-I$(pwd)"				\\\
	TARGET_LDFLAGS="%{efi_target_ldflags}"			\\\
	--with-rpm-version=%{version}-%{release}		\\\
	--with-platform=efi					\\\
	--with-utils=host					\\\
	--target=%{1}						\\\
	--with-grubdir=grub2					\\\
	--program-transform-name=s,grub,grub2,		\\\
	--disable-werror || ( cat config.log ; exit 1 )		\
git add .							\
git commit -m "After efi configure"				\
%{nil}

%define do_xen_configure()					\
%configure							\\\
	%{cc_equals}						\\\
	HOST_CFLAGS="%{3}"					\\\
	HOST_CPPFLAGS="-I$(pwd)"				\\\
	HOST_LDFLAGS="%{xen_host_ldflags}"			\\\
	TARGET_CFLAGS="%{2}"					\\\
	TARGET_CPPFLAGS="-I$(pwd)"				\\\
	TARGET_LDFLAGS="%{xen_target_ldflags}"			\\\
	--with-rpm-version=%{version}-%{release}		\\\
	--with-platform=xen					\\\
	--with-utils=host					\\\
	--target=%{1}						\\\
	--with-grubdir=grub2					\\\
	--program-transform-name=s,grub,grub2,		\\\
	--disable-werror || ( cat config.log ; exit 1 )		\
git add .							\
git commit -m "After xen configure"				\
%{nil}

%define do_xen_pvh_configure()					\
%configure							\\\
	%{cc_equals}						\\\
	HOST_CFLAGS="%{3}"					\\\
	HOST_CPPFLAGS="-I$(pwd)"				\\\
	HOST_LDFLAGS="%{xen_pvh_host_ldflags}"			\\\
	TARGET_CFLAGS="%{2}"					\\\
	TARGET_CPPFLAGS="-I$(pwd)"				\\\
	TARGET_LDFLAGS="%{xen_pvh_target_ldflags}"			\\\
	--with-rpm-version=%{version}-%{release}		\\\
	--with-platform=xen_pvh					\\\
	--with-utils=host					\\\
	--target=%{1}						\\\
	--with-grubdir=grub2					\\\
	--program-transform-name=s,grub,grub2,		\\\
	--disable-werror || ( cat config.log ; exit 1 )		\
git add .							\
git commit -m "After xen_pvh configure"				\
%{nil}

%define do_efi_build_modules()					\
make %{?_smp_mflags} ascii.h widthspec.h			\
make %{?_smp_mflags} -C grub-core				\
%{nil}

%define do_efi_build_all()					\
make %{?_smp_mflags}						\
%{nil}

%define do_efi_link_utils()					\
for x in grub-mkimage ; do					\\\
	ln ../grub-%{1}-%{tarversion}/${x} ./ ;			\\\
done								\
%{nil}

%define do_xen_build_modules()					\
make %{?_smp_mflags} ascii.h widthspec.h			\
make %{?_smp_mflags} -C grub-core				\
%{nil}

%define do_xen_pvh_build_modules()					\
make %{?_smp_mflags} ascii.h widthspec.h			\
make %{?_smp_mflags} -C grub-core				\
%{nil}

%define do_install_protected_file()				\
touch %{1}.conf							\
echo %{1} > %{1}.conf						\
install -d -m 755 ${RPM_BUILD_ROOT}/etc/dnf/protected.d/	\
install -m 644 %{1}.conf ${RPM_BUILD_ROOT}/etc/dnf/protected.d/ \
rm -f %{1}.conf							\
%{nil}

%global grub_modules  " all_video boot blscfg btrfs blsuki	\\\
			cat configfile cryptodisk		\\\
			echo ext2 f2fs fat font			\\\
			gcry_rijndael gcry_rsa gcry_serpent	\\\
			gcry_sha256 gcry_twofish gcry_whirlpool	\\\
			gfxmenu gfxterm gzio			\\\
			halt hfsplus http increment iso9660	\\\
			jpeg loadenv loopback linux lvm luks	\\\
			luks2					\\\
			memdisk					\\\
			mdraid09 mdraid1x minicmd net		\\\
			normal part_apple part_msdos part_gpt	\\\
			password_pbkdf2 pgp png reboot regexp	\\\
			search search_fs_uuid search_fs_file	\\\
			search_label serial sleep		\\\
			squash4					\\\
			syslinuxcfg				\\\
			test tftp version video xfs zstd "	\

%ifarch %{efi_arch}
%define efi_mkimage()						\
mkdir -p memdisk/fonts						\
cp %{4}/unicode.pf2 memdisk/fonts				\
mksquashfs memdisk memdisk.squashfs -comp lzo			\
%{4}./grub-mkimage -O %{1} -o %{2}.orig				\\\
	-d grub-core						\\\
	--sbat %{4}./sbat.csv					\\\
	-m memdisk.squashfs					\\\
	-p /EFI/%{efi_vendor}					\\\
	${GRUB_MODULES}						\
%{4}./grub-mkimage -O %{1} -o %{3}.orig				\\\
	-d grub-core						\\\
	--sbat %{4}./sbat.csv					\\\
	-m memdisk.squashfs					\\\
	-p /EFI/BOOT						\\\
	${GRUB_MODULES}						\
%{expand:%%define ___pesign_client_cert %{?___pesign_client_cert}%{!?___pesign_client_cert:%{__pesign_client_cert}}} \
%{?__pesign_client_cert:%{expand:%%define __pesign_client_cert %{___pesign_client_cert}}} \
%{expand:%%{pesign -s -i %%{2}.orig -o %%{2}.onesig -a %%{5} -c %%{6} -n %%{7}}}	\
%{expand:%%{pesign -s -i %%{3}.orig -o %%{3}.onesig -a %%{5} -c %%{6} -n %%{7}}}	\
%{expand:%%define __pesign_client_cert grub2-signer} \
%{expand:%%{pesign -s -i %%{2}.onesig -o %%{2} -a %%{5} -c %%{6} -n %%{7}}}	\
%{expand:%%{pesign -s -i %%{3}.onesig -o %%{3} -a %%{5} -c %%{6} -n %%{7}}}	\
%{nil}
%endif

%ifarch ppc64le
%if 0%{?oreon}
%define ieee1275_mkimage()					\
mkdir -p memdisk/fonts						\
cp %{5}/unicode.pf2 memdisk/fonts				\
mksquashfs memdisk memdisk.squashfs -comp lzo			\
./grub-mkimage -O %{1} -o %{2} -p '/grub2' -d grub-core ${GRUB_MODULES} \
%{nil}
%else
%define ieee1275_mkimage()					\
mkdir -p memdisk/fonts						\
cp %{5}/unicode.pf2 memdisk/fonts				\
mksquashfs memdisk memdisk.squashfs -comp lzo			\
APPENDED_SIG_SIZE=0						\
if [ -x /usr/bin/rpm-sign ]; then				\
	touch empty.unsigned					\
	rpm-sign --key %{4}					\\\
		 --lkmsign empty.unsigned			\\\
		 --output empty.signed				\
	APPENDED_SIG_SIZE="$(stat -c '%s' empty.signed)"	\
	rm empty.{un,}signed					\
fi								\
./grub-mkimage -O %{1} -o %{2}.orig				\\\
	-d grub-core						\\\
	-m memdisk.squashfs					\\\
	-p '/grub2'						\\\
	-x %{3}							\\\
	--appended-signature-size ${APPENDED_SIG_SIZE}		\\\
	${GRUB_MODULES}						\
if [ -x /usr/bin/rpm-sign ]; then				\
	truncate -s -${APPENDED_SIG_SIZE} %{2}.orig		\
	rpm-sign --key %{4}					\\\
		 --lkmsign %{2}.orig				\\\
		 --output %{2}					\
else								\
	mv %{2}.orig %{2}					\
fi								\
%{nil}
%endif
%endif

%define do_efi_build_images()					\
GRUB_MODULES+=%{grub_modules}					\
GRUB_MODULES+=%{efi_modules}					\
GRUB_MODULES+=%{platform_modules}				\
%{expand:%%{efi_mkimage %{1} %{2} %{3} %{4} %%{5} %%{6} %%{7}}}			\
%{nil}

%define do_ieee1275_build_images()			\
GRUB_MODULES+=%{grub_modules}				\
GRUB_MODULES+=%{platform_modules}			\
cd grub-%{1}-%{tarversion}				\
%{expand:%%ieee1275_mkimage %%{1} %%{2} %%{3} %%{4} ./ }\
cd ..							\
%{nil}

%define do_primary_efi_build()					\
cd grub-%{1}-%{tarversion}					\
%{expand:%%do_efi_configure %%{4} %%{5} %%{6}}			\
%do_efi_build_all						\
%{expand:%%do_efi_build_images %{grub_target_name} %{2} %{3} ./ %%{7} %%{8} %%{9}} \
cd ..								\
%{nil}

%define do_alt_efi_build()					\
cd grub-%{1}-%{tarversion}					\
%{expand:%%do_efi_configure %%{4} %%{5} %%{6}}			\
%do_efi_build_modules						\
%{expand:%%do_efi_link_utils %{grubefiarch}}			\
%{expand:%%do_efi_build_images %{alt_grub_target_name} %{2} %{3} ../grub-%{grubefiarch}-%{tarversion}/ %%{7} %%{8} %%{9}} \
cd ..								\
%{nil}

%define do_legacy_build()					\
cd grub-%{1}-%{tarversion}					\
%configure							\\\
	%{cc_equals}						\\\
	HOST_CFLAGS="%{legacy_host_cflags}"			\\\
	HOST_CPPFLAGS="-I$(pwd)"				\\\
	HOST_LDFLAGS="%{legacy_host_ldflags}"			\\\
	TARGET_CFLAGS="%{legacy_target_cflags}"			\\\
	TARGET_CPPFLAGS="-I$(pwd)"				\\\
	TARGET_LDFLAGS="%{legacy_target_ldflags}"		\\\
	--with-platform=%{platform}				\\\
	--with-utils=host					\\\
	--target=%{_target_platform}				\\\
	--with-grubdir=grub2					\\\
	--program-transform-name=s,grub,grub2,		\\\
	--disable-werror || ( cat config.log ; exit 1 )		\
git add .							\
git commit -m "After legacy configure"				\
make %{?_smp_mflags}						\
cd ..								\
%{nil}

%define do_emu_build()						\
cd grub-emu-%{tarversion}					\
%configure							\\\
	%{cc_equals}						\\\
	HOST_CFLAGS="%{legacy_host_cflags}"			\\\
	HOST_CPPFLAGS="-I$(pwd)"				\\\
	HOST_LDFLAGS="%{legacy_host_ldflags}"			\\\
	--with-platform=emu					\\\
	--with-grubdir=grub2					\\\
	--program-transform-name=s,grub,grub2,		\\\
	--disable-werror || ( cat config.log ; exit 1 )		\
git add .							\
git commit -m "After emu configure"				\
make %{?_smp_mflags} ascii.h widthspec.h			\
make %{?_smp_mflags} -C grub-core/lib/gnulib			\
make %{?_smp_mflags} -C grub-core				\
cd ..								\
%{nil}

%define do_xen_build()					\
cd grub-%{1}-%{tarversion}					\
%{expand:%%do_xen_configure %%{2} %%{3} %%{4}}			\
%do_xen_build_modules						\
cd ..								\
%{nil}

%define do_xen_pvh_build()					\
cd grub-%{1}-%{tarversion}					\
%{expand:%%do_xen_pvh_configure %%{2} %%{3} %%{4}}			\
%do_xen_pvh_build_modules						\
cd ..								\
%{nil}

%define do_alt_efi_install()					\
cd grub-%{1}-%{tarversion}					\
install -d -m 755 $RPM_BUILD_ROOT/usr/lib/grub/%{grubaltefiarch}/ \
find . '(' -iname gdb_grub					\\\
	-o -iname kernel.exec					\\\
	-o -iname kernel.img					\\\
	-o -iname config.h					\\\
	-o -iname gmodule.pl					\\\
	-o -iname modinfo.sh					\\\
	-o -iname '*.lst'					\\\
	-o -iname '*.mod'					\\\
	')'							\\\
	-exec cp {} $RPM_BUILD_ROOT/usr/lib/grub/%{grubaltefiarch}/ \\\; \
find $RPM_BUILD_ROOT -type f -iname "*.mod*" -exec chmod a-x {} '\;'	\
install -d -m 0755 ${RPM_BUILD_ROOT}%{_libdir}/efi		\
install -d -m 0755 ${RPM_BUILD_ROOT}%{_libdir}/efi/grub2	\
install -d -m 0755 ${RPM_BUILD_ROOT}%{grub_evr_dir}		\
install -d -m 0755 ${RPM_BUILD_ROOT}%{grub_evr_dir}/EFI		\
install -d -m 0700 ${RPM_BUILD_ROOT}%{grub_efi_dir}/		\
install -m 700 %{2} $RPM_BUILD_ROOT%{grub_efi_dir}/%{2} \
install -m 700 %{3} $RPM_BUILD_ROOT%{grub_efi_dir}/%{3} \
%{expand:%%do_install_protected_file grub2-%{alt_package_arch}} \
cd ..								\
%{nil}

%define do_efi_install()					\
cd grub-%{1}-%{tarversion}					\
make DESTDIR=$RPM_BUILD_ROOT install				\
if [ -f $RPM_BUILD_ROOT%{_infodir}/grub.info ]; then		\
	rm -f $RPM_BUILD_ROOT%{_infodir}/grub.info		\
fi								\
if [ -f $RPM_BUILD_ROOT%{_infodir}/grub-dev.info ]; then	\
	rm -f $RPM_BUILD_ROOT%{_infodir}/grub-dev.info		\
fi								\
find $RPM_BUILD_ROOT -iname "*.module" -exec chmod a-x {} '\;'	\
ln -s ../boot/grub2/grub.cfg					\\\
	$RPM_BUILD_ROOT%{_sysconfdir}/grub2-efi.cfg		\
install -d -m 0755 ${RPM_BUILD_ROOT}%{_libdir}/efi		\
install -d -m 0755 ${RPM_BUILD_ROOT}%{_libdir}/efi/grub2	\
install -d -m 0755 ${RPM_BUILD_ROOT}%{grub_evr_dir}		\
install -d -m 0755 ${RPM_BUILD_ROOT}%{grub_evr_dir}/EFI		\
install -d -m 0700 ${RPM_BUILD_ROOT}%{grub_efi_dir}/		\
install -m 700 %{2} $RPM_BUILD_ROOT%{grub_efi_dir}/%{2}	\
install -m 700 %{3} $RPM_BUILD_ROOT%{grub_efi_dir}/%{3}	\
%ifarch %{arm}							\
install -D -m 700 %{2} $RPM_BUILD_ROOT%{efi_esp_boot}/BOOTARM.EFI \
%endif								\
install -D -m 700 %{SOURCE13}					\\\
    ${RPM_BUILD_ROOT}/usr/bin/gen_grub_cfgstub		\
install -D -m 700 unicode.pf2					\\\
	${RPM_BUILD_ROOT}/boot/grub2/fonts/unicode.pf2		\
${RPM_BUILD_ROOT}/%{_bindir}/grub2-editenv			\\\
		${RPM_BUILD_ROOT}/boot/grub2/grubenv create	\
%{expand:%%do_install_protected_file grub2-%{package_arch}}	\
cd ..								\
%{nil}

%define do_legacy_install()					\
cd grub-%{1}-%{tarversion}					\
make DESTDIR=$RPM_BUILD_ROOT install				\
if [ -f $RPM_BUILD_ROOT%{_infodir}/grub.info ]; then		\
	rm -f $RPM_BUILD_ROOT%{_infodir}/grub.info		\
fi								\
if [ -f $RPM_BUILD_ROOT%{_infodir}/grub-dev.info ]; then	\
	rm -f $RPM_BUILD_ROOT%{_infodir}/grub-dev.info		\
fi								\
%{expand:%ifarch ppc64le					\
	install -m 700 %{grubelfname} $RPM_BUILD_ROOT/%{_libdir}/grub/%{1} \
%endif}								\
if [ -f $RPM_BUILD_ROOT/%{_libdir}/grub/%{1}/grub2.chrp ]; then \
	mv $RPM_BUILD_ROOT/%{_libdir}/grub/%{1}/grub2.chrp	\\\
	   $RPM_BUILD_ROOT/%{_libdir}/grub/%{1}/grub.chrp	\
fi								\
if [ %{3} -eq 0 ]; then						\
	${RPM_BUILD_ROOT}/%{_bindir}/grub2-editenv		\\\
		${RPM_BUILD_ROOT}/boot/grub2/grubenv create	\
fi								\
%{expand:%ifnarch ppc64le					\
mkdir pxe							\
./grub-mknetdir							\\\
	--directory ./grub-core					\\\
	--fonts=""						\\\
	--locales=""						\\\
	--themes=""						\\\
	--modules="configfile gzio linux reboot test"		\\\
	--net-directory=pxe					\\\
	--subdir .						\
mv pxe/*/core.0 $RPM_BUILD_ROOT/%{_libdir}/grub/%{1}/		\
%endif}								\
%{expand:%%do_install_protected_file grub2-%{legacy_package_arch}} \
cd ..								\
%{nil}

%define do_emu_install()					\
cd grub-emu-%{tarversion}					\
make DESTDIR=$RPM_BUILD_ROOT install -C grub-core		\
if [ -f $RPM_BUILD_ROOT%{_infodir}/grub.info ]; then		\
	rm -f $RPM_BUILD_ROOT%{_infodir}/grub.info		\
fi								\
if [ -f $RPM_BUILD_ROOT%{_infodir}/grub-dev.info ]; then	\
	rm -f $RPM_BUILD_ROOT%{_infodir}/grub-dev.info		\
fi								\
if [ -f $RPM_BUILD_ROOT/%{_libdir}/grub/%{1}/grub2.chrp ]; then \
	mv $RPM_BUILD_ROOT/%{_libdir}/grub/%{1}/grub2.chrp	\\\
	   $RPM_BUILD_ROOT/%{_libdir}/grub/%{1}/grub.chrp	\
fi								\
cd ..								\
%{nil}

%define do_xen_install()					\
cd grub-%{1}-%{tarversion}					\
make DESTDIR=$RPM_BUILD_ROOT install				\
if [ -f $RPM_BUILD_ROOT%{_infodir}/grub.info ]; then		\
	rm -f $RPM_BUILD_ROOT%{_infodir}/grub.info		\
fi								\
if [ -f $RPM_BUILD_ROOT%{_infodir}/grub-dev.info ]; then	\
	rm -f $RPM_BUILD_ROOT%{_infodir}/grub-dev.info		\
fi								\
find $RPM_BUILD_ROOT -iname "*.module" -exec chmod a-x {} '\;'	\
cd ..								\
%{nil}

%define do_xen_pvh_install()					\
cd grub-%{1}-%{tarversion}					\
make DESTDIR=$RPM_BUILD_ROOT install				\
if [ -f $RPM_BUILD_ROOT%{_infodir}/grub.info ]; then		\
	rm -f $RPM_BUILD_ROOT%{_infodir}/grub.info		\
fi								\
if [ -f $RPM_BUILD_ROOT%{_infodir}/grub-dev.info ]; then	\
	rm -f $RPM_BUILD_ROOT%{_infodir}/grub-dev.info		\
fi								\
find $RPM_BUILD_ROOT -iname "*.module" -exec chmod a-x {} '\;'	\
cd ..								\
%{nil}

%define do_common_install()					\
install -d -m 0755 						\\\
	$RPM_BUILD_ROOT%{_datarootdir}/locale/en\@quot		\\\
	$RPM_BUILD_ROOT%{_datarootdir}/locale/en		\\\
	$RPM_BUILD_ROOT%{_infodir}/				\
cp -a $RPM_BUILD_ROOT%{_datarootdir}/locale/en\@quot		\\\
	$RPM_BUILD_ROOT%{_datarootdir}/locale/en		\
cp docs/grub.info $RPM_BUILD_ROOT%{_infodir}/grub2.info	\
cp docs/grub-dev.info						\\\
	$RPM_BUILD_ROOT%{_infodir}/grub2-dev.info		\
install -d -m 0700 ${RPM_BUILD_ROOT}%{efi_esp_dir}/		\
install -d -m 0700 ${RPM_BUILD_ROOT}/boot/grub2/		\
install -d -m 0700 ${RPM_BUILD_ROOT}/boot/grub2/themes/system	\
install -d -m 0700 ${RPM_BUILD_ROOT}%{_sysconfdir}/default	\
install -d -m 0700 ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig	\
touch ${RPM_BUILD_ROOT}%{_sysconfdir}/default/grub		\
ln -sf ../default/grub						\\\
	${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/grub		\
touch grub.cfg							\
install -m 0600 grub.cfg ${RPM_BUILD_ROOT}/boot/grub2/		\
ln -s ../boot/grub2/grub.cfg					\\\
	${RPM_BUILD_ROOT}%{_sysconfdir}/grub2.cfg		\
%{nil}

%define define_legacy_variant_files()				\
%{expand:%%files %{1}}						\
%defattr(-,root,root,-)						\
%config(noreplace) %{_sysconfdir}/grub2.cfg			\
%ghost %config(noreplace) %attr(0600,root,root)/boot/grub2/grub.cfg	\
%attr(0644,root,root) %config(noreplace) /etc/dnf/protected.d/grub2-%{1}.conf \
%ifarch ppc64le							\
%dir %{_libdir}/grub/%{2}/					\
%{_libdir}/grub/%{2}/%{grubelfname}				\
%endif								\
								\
%{expand:%if 0%{?with_legacy_modules}				\
%{expand:%%files %{1}-modules}					\
%defattr(-,root,root)						\
%dir %{_libdir}/grub/%{2}/					\
%{_libdir}/grub/%{2}/*						\
%ifarch ppc64le							\
%exclude %{_libdir}/grub/%{2}/%{grubelfname}			\
%endif								\
%exclude %{_libdir}/grub/%{2}/*.module				\
%exclude %{_libdir}/grub/%{2}/{boot,boot_hybrid,cdboot,diskboot,lzma_decompress,pxeboot}.image \
%exclude %{_libdir}/grub/%{2}/*.o				\
%else								\
%%exclude %%{_libdir}/grub/%%{grublegacyarch}/*			\
%endif}								\
%{nil}

%define define_efi_variant_files()				\
%{expand:%%files %{1}}						\
%defattr(-,root,root,-)						\
%config(noreplace) %{_sysconfdir}/grub2.cfg			\
%config(noreplace) %{_sysconfdir}/grub2-efi.cfg		\
%ghost %attr(0700,root,root) %{efi_esp_dir}/%{2} \
%dir %attr(0755,root,root) %{_libdir}/efi			\
%dir %attr(0755,root,root) %{_libdir}/efi/grub2			\
%dir %attr(0755,root,root) %{grub_evr_dir}			\
%dir %attr(0755,root,root) %{grub_evr_dir}/EFI			\
%dir %attr(0700,root,root) %{grub_efi_dir}                      \
%attr(0700,root,root) %{grub_efi_dir}/%{2} 	\
%ifarch %{arm}							\
%attr(0700,root,root) %verify(not mtime) %{efi_esp_boot}/BOOTARM.EFI \
%endif								\
%attr(0700,root,root)/boot/grub2/fonts			\
%attr(0700,root,root)/usr/bin/gen_grub_cfgstub			\
%ghost %config(noreplace) %attr(0600,root,root)/boot/grub2/grub.cfg	\
%ghost %config(noreplace) %attr(0700,root,root)%{efi_esp_dir}/grub.cfg	\
%ghost %config(noreplace) %attr(0600,root,root)%{grub_efi_dir}/grub.cfg	\
%config(noreplace) %verify(not size mode md5 mtime) /boot/grub2/grubenv	\
%attr(0644,root,root) %config(noreplace) /etc/dnf/protected.d/grub2-%{1}.conf \
%{expand:%if 0%{?without_efi_modules}				\
%exclude %{_libdir}/grub/%{6}					\
%exclude %{_libdir}/grub/%{6}/*					\
%endif}								\
								\
%{expand:%if 0%{?with_efi_modules}				\
%{expand:%%files %{1}-modules}					\
%defattr(-,root,root,-)						\
%dir %{_libdir}/grub/%{6}/					\
%{_libdir}/grub/%{6}/*						\
%exclude %{_libdir}/grub/%{6}/*.module				\
%endif}								\
								\
%{expand:%%files %{1}-cdboot}					\
%defattr(-,root,root,-)						\
%ghost %attr(0700,root,root) %{efi_esp_dir}/%{3}	\
%attr(0700,root,root) %{grub_efi_dir}/%{3}	\
%attr(0700,root,root)/boot/grub2/fonts			\
%{nil}

%define define_xen_variant_files()				\
%{expand:%%files %{1}-modules}					\
%defattr(-,root,root,-)						\
%dir %{_libdir}/grub/%{2}/					\
%{_libdir}/grub/%{2}/*						\
%exclude %{_libdir}/grub/%{2}/*.module				\
%{nil}

%define define_xen_pvh_variant_files()				\
%{expand:%%files %{1}-modules}					\
%defattr(-,root,root,-)						\
%dir %{_libdir}/grub/%{2}/					\
%{_libdir}/grub/%{2}/*						\
%exclude %{_libdir}/grub/%{2}/*.module				\
%{nil}

%define sb_ca	 %{nil}
%define sb_cer	 %{nil}
%define sb_key	 %{nil}

BuildRequires: oreon-rpm-macros
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
BuildRequires:	fuse3-devel
BuildRequires:	clang
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

Patch0001: 0001-Revert-templates-Fix-user-facing-typo-with-an-incorr.patch
Patch0002: 0002-Revert-templates-Properly-disable-the-os-prober-by-d.patch
Patch0003: 0003-Revert-templates-Disable-the-os-prober-by-default.patch
Patch0004: 0004-Rework-linux-command.patch
Patch0005: 0005-Rework-linux16-command.patch
Patch0006: 0006-IBM-client-architecture-CAS-reboot-support.patch
Patch0007: 0007-for-ppc-reset-console-display-attr-when-clear-screen.patch
Patch0008: 0008-Disable-GRUB-video-support-for-IBM-power-machines.patch
Patch0009: 0009-Move-bash-completion-script-922997.patch
Patch0010: 0010-Allow-fallback-to-include-entries-by-title-not-just-.patch
Patch0011: 0011-Make-exit-take-a-return-code.patch
Patch0012: 0012-Make-efi-machines-load-an-env-block-from-a-variable.patch
Patch0013: 0013-Migrate-PPC-from-Yaboot-to-Grub2.patch
Patch0014: 0014-Add-fw_path-variable-revised.patch
Patch0015: 0015-Pass-x-hex-hex-straight-through-unmolested.patch
Patch0016: 0016-blscfg-add-blscfg-module-to-parse-Boot-Loader-Specif.patch
Patch0017: 0017-Add-devicetree-loading.patch
Patch0018: 0018-Enable-pager-by-default.-985860.patch
Patch0019: 0019-Don-t-say-GNU-Linux-in-generated-menus.patch
Patch0020: 0020-Add-.eh_frame-to-list-of-relocations-stripped.patch
Patch0021: 0021-Don-t-require-a-password-to-boot-entries-generated-b.patch
Patch0022: 0022-use-fw_path-prefix-when-fallback-searching-for-grub-.patch
Patch0023: 0023-Generate-OS-and-CLASS-in-10_linux-from-etc-os-releas.patch
Patch0024: 0024-Try-prefix-if-fw_path-doesn-t-work.patch
Patch0025: 0025-Make-grub2-mkconfig-construct-titles-that-look-like-.patch
Patch0026: 0026-Add-friendly-grub2-password-config-tool-985962.patch
Patch0027: 0027-tcp-add-window-scaling-support.patch
Patch0028: 0028-efinet-and-bootp-add-support-for-dhcpv6.patch
Patch0029: 0029-bootp-New-net_bootp6-command.patch
Patch0030: 0030-Add-grub-get-kernel-settings-and-use-it-in-10_linux.patch
Patch0031: 0031-Make-grub_fatal-also-backtrace.patch
Patch0032: 0032-Make-our-info-pages-say-grub2-where-appropriate.patch
Patch0033: 0033-macos-just-build-chainloader-entries-don-t-try-any-x.patch
Patch0034: 0034-grub2-btrfs-Add-ability-to-boot-from-subvolumes.patch
Patch0035: 0035-btrfs-fix-a-bad-null-check.patch
Patch0036: 0036-export-btrfs_subvol-and-btrfs_subvolid.patch
Patch0037: 0037-grub2-btrfs-03-follow_default.patch
Patch0038: 0038-grub2-btrfs-04-grub2-install.patch
Patch0039: 0039-grub2-btrfs-05-grub2-mkconfig.patch
Patch0040: 0040-grub2-btrfs-06-subvol-mount.patch
Patch0041: 0041-Fallback-to-old-subvol-name-scheme-to-support-old-sn.patch
Patch0042: 0042-Grub-not-working-correctly-with-btrfs-snapshots-bsc-.patch
Patch0043: 0043-Add-grub_efi_allocate_pool-and-grub_efi_free_pool-wr.patch
Patch0044: 0044-Use-grub_efi_.-memory-helpers-where-reasonable.patch
Patch0045: 0045-Add-PRIxGRUB_EFI_STATUS-and-use-it.patch
Patch0046: 0046-don-t-use-int-for-efi-status.patch
Patch0047: 0047-make-GRUB_MOD_INIT-declare-its-function-prototypes.patch
Patch0048: 0048-Don-t-guess-boot-efi-as-HFS-on-ppc-machines-in-grub-.patch
Patch0049: 0049-20_linux_xen-load-xen-or-multiboot-2-modules-as-need.patch
Patch0050: 0050-align-struct-efi_variable-better.patch
Patch0051: 0051-Add-BLS-support-to-grub-mkconfig.patch
Patch0052: 0052-Don-t-attempt-to-backtrace-on-grub_abort-for-grub-em.patch
Patch0053: 0053-Add-grub2-switch-to-blscfg.patch
Patch0054: 0054-normal-don-t-draw-our-startup-message-if-debug-is-se.patch
Patch0055: 0055-Work-around-some-minor-include-path-weirdnesses.patch
Patch0056: 0056-Make-it-possible-to-enabled-build-id-sha1.patch
Patch0057: 0057-make-better-backtraces.patch
Patch0058: 0058-Fixup-for-newer-compiler.patch
Patch0059: 0059-Don-t-attempt-to-export-the-start-and-_start-symbols.patch
Patch0060: 0060-Fixup-for-newer-compiler.patch
Patch0061: 0061-Add-support-for-non-Ethernet-network-cards.patch
Patch0062: 0062-efinet-UEFI-IPv6-PXE-support.patch
Patch0063: 0063-grub.texi-Add-net_bootp6-doument.patch
Patch0064: 0064-bootp-Add-processing-DHCPACK-packet-from-HTTP-Boot.patch
Patch0065: 0065-Fix-const-char-pointers-in-grub-core-net-bootp.c.patch
Patch0066: 0066-efinet-Setting-network-from-UEFI-device-path.patch
Patch0067: 0067-efinet-Setting-DNS-server-from-UEFI-protocol.patch
Patch0068: 0068-Support-UEFI-networking-protocols.patch
Patch0069: 0069-AUDIT-0-http-boot-tracker-bug.patch
Patch0070: 0070-grub-editenv-Add-incr-command-to-increment-integer-v.patch
Patch0071: 0071-Add-auto-hide-menu-support.patch
Patch0072: 0072-Add-grub-set-bootflag-utility.patch
Patch0073: 0073-docs-Add-grub-boot-indeterminate.service-example.patch
Patch0074: 0074-gentpl-add-disable-support.patch
Patch0075: 0075-gentpl-add-pc-firmware-type.patch
Patch0076: 0076-efinet-also-use-the-firmware-acceleration-for-http.patch
Patch0077: 0077-efi-http-Make-root_url-reflect-the-protocol-hostname.patch
Patch0078: 0078-Make-it-so-we-can-tell-configure-which-cflags-utils-.patch
Patch0079: 0079-Rework-how-the-fdt-command-builds.patch
Patch0080: 0080-Disable-non-wordsize-allocations-on-arm.patch
Patch0081: 0081-Prepend-prefix-when-HTTP-path-is-relative.patch
Patch0082: 0082-Make-reset-an-alias-for-the-reboot-command.patch
Patch0083: 0083-Add-a-version-command.patch
Patch0084: 0084-Add-more-dprintf-and-nerf-dprintf-in-script.c.patch
Patch0085: 0085-Attempt-to-fix-up-all-the-places-Wsign-compare-error.patch
Patch0086: 0086-Don-t-use-Wno-sign-compare-Wno-conversion-Wno-error-.patch
Patch0087: 0087-Fix-getroot.c-s-trampolines.patch
Patch0088: 0088-Do-not-allow-stack-trampolines-anywhere.patch
Patch0089: 0089-Reimplement-boot_counter.patch
Patch0090: 0090-Fix-menu-entry-selection-based-on-ID-and-title.patch
Patch0091: 0091-Make-the-menu-entry-users-option-argument-to-be-opti.patch
Patch0092: 0092-Add-efi-export-env-and-efi-load-env-commands.patch
Patch0093: 0093-Export-all-variables-from-the-initial-context-when-c.patch
Patch0094: 0094-grub.d-Split-out-boot-success-reset-from-menu-auto-h.patch
Patch0095: 0095-Don-t-assume-that-boot-commands-will-only-return-on-.patch
Patch0096: 0096-grub-set-bootflag-Update-comment-about-running-as-ro.patch
Patch0097: 0097-grub-set-bootflag-Write-new-env-to-tmpfile-and-then-.patch
Patch0098: 0098-grub.d-Fix-boot_indeterminate-getting-set-on-boot_su.patch
Patch0099: 0099-Add-start-symbol-for-RISC-V.patch
Patch0100: 0100-efi-http-Export-fw-http-_path-variables-to-make-them.patch
Patch0101: 0101-efi-http-Enclose-literal-IPv6-addresses-in-square-br.patch
Patch0102: 0102-efi-net-Allow-to-specify-a-port-number-in-addresses.patch
Patch0103: 0103-efi-ip4_config-Improve-check-to-detect-literal-IPv6-.patch
Patch0104: 0104-efi-net-Print-a-debug-message-if-parsing-the-address.patch
Patch0105: 0105-kern-term-Also-accept-F8-as-a-user-interrupt-key.patch
Patch0106: 0106-http-Prepend-prefix-when-the-HTTP-path-is-relative-a.patch
Patch0107: 0107-Fix-a-missing-return-in-efi-export-env-and-efi-load-.patch
Patch0108: 0108-efi-dhcp-fix-some-allocation-error-checking.patch
Patch0109: 0109-efi-http-fix-some-allocation-error-checking.patch
Patch0110: 0110-efi-ip-46-_config.c-fix-some-potential-allocation-ov.patch
Patch0111: 0111-Fix-const-char-pointers-in-grub-core-net-efi-ip4_con.patch
Patch0112: 0112-Fix-const-char-pointers-in-grub-core-net-efi-ip6_con.patch
Patch0113: 0113-Fix-const-char-pointers-in-grub-core-net-efi-net.c.patch
Patch0114: 0114-Fix-const-char-pointers-in-grub-core-net-efi-pxe.c.patch
Patch0115: 0115-Add-systemd-integration-scripts-to-make-systemctl-re.patch
Patch0116: 0116-systemd-integration.sh-Also-set-old-menu_show_once-g.patch
Patch0117: 0117-at_keyboard-use-set-1-when-keyboard-is-in-Translate-.patch
Patch0118: 0118-grub-install-disable-support-for-EFI-platforms.patch
Patch0119: 0119-New-with-debug-timestamps-configure-flag-to-prepend-.patch
Patch0120: 0120-Added-debug-statements-to-grub_disk_open-and-grub_di.patch
Patch0121: 0121-Introduce-function-grub_debug_is_enabled-void-return.patch
Patch0122: 0122-Don-t-clear-screen-when-debugging-is-enabled.patch
Patch0123: 0123-grub_file_-instrumentation-new-file-debug-tag.patch
Patch0124: 0124-ieee1275-Avoiding-many-unecessary-open-close.patch
Patch0125: 0125-ieee1275-powerpc-implements-fibre-channel-discovery-.patch
Patch0126: 0126-ieee1275-powerpc-enables-device-mapper-discovery.patch
Patch0127: 0127-Add-at_keyboard_fallback_set-var-to-force-the-set-ma.patch
Patch0128: 0128-Add-suport-for-signing-grub-with-an-appended-signatu.patch
Patch0129: 0129-docs-grub-Document-signing-grub-under-UEFI.patch
Patch0130: 0130-docs-grub-Document-signing-grub-with-an-appended-sig.patch
Patch0131: 0131-dl-provide-a-fake-grub_dl_set_persistent-for-the-emu.patch
Patch0132: 0132-pgp-factor-out-rsa_pad.patch
Patch0133: 0133-crypto-move-storage-for-grub_crypto_pk_-to-crypto.c.patch
Patch0134: 0134-libtasn1-disable-code-not-needed-in-grub.patch
Patch0135: 0135-libtasn1-changes-for-grub-compatibility.patch
Patch0136: 0136-grub-install-support-embedding-x509-certificates.patch
Patch0137: 0137-appended-signatures-support-verifying-appended-signa.patch
Patch0138: 0138-appended-signatures-verification-tests.patch
Patch0139: 0139-appended-signatures-documentation.patch
Patch0140: 0140-ieee1275-enter-lockdown-based-on-ibm-secure-boot.patch
Patch0141: 0141-ieee1275-drop-HEAP_MAX_ADDR-HEAP_MIN_SIZE.patch
Patch0142: 0142-appendedsig-x509-Also-handle-the-Extended-Key-Usage-.patch
Patch0143: 0143-ieee1275-ofdisk-retry-on-open-failure.patch
Patch0144: 0144-efinet-Add-DHCP-proxy-support.patch
Patch0145: 0145-Don-t-update-the-cmdline-when-generating-legacy-menu.patch
Patch0146: 0146-Suppress-gettext-error-message.patch
Patch0147: 0147-grub-set-password-Always-use-boot-grub2-user.cfg-as-.patch
Patch0148: 0148-normal-main-Discover-the-device-to-read-the-config-f.patch
Patch0149: 0149-powerpc-adjust-setting-of-prefix-for-signed-binary-c.patch
Patch0150: 0150-powerpc-ieee1275-load-grub-at-4MB-not-2MB.patch
Patch0151: 0151-Add-Fedora-location-of-DejaVu-SANS-font.patch
Patch0152: 0152-efi-new-connectefi-command.patch
Patch0153: 0153-powerpc-prefix-detection-support-device-names-with-c.patch
Patch0154: 0154-make-ofdisk_retries-optional.patch
Patch0155: 0155-misc-Make-grub_min-and-grub_max-more-resilient.patch
Patch0156: 0156-ReiserFS-switch-to-using-grub_min-grub_max.patch
Patch0157: 0157-misc-make-grub_boot_time-also-call-grub_dprintf-boot.patch
Patch0158: 0158-modules-Don-t-allocate-space-for-non-allocable-secti.patch
Patch0159: 0159-modules-load-module-sections-at-page-aligned-address.patch
Patch0160: 0160-nx-add-memory-attribute-get-set-API.patch
Patch0161: 0161-nx-set-page-permissions-for-loaded-modules.patch
Patch0162: 0162-grub_fs_probe-dprint-errors-from-filesystems.patch
Patch0163: 0163-Make-debug-file-show-which-file-filters-get-run.patch
Patch0164: 0164-BLS-create-etc-kernel-cmdline-during-mkconfig.patch
Patch0165: 0165-squish-don-t-dup-rhgb-quiet-check-mtimes.patch
Patch0166: 0166-squish-give-up-on-rhgb-quiet.patch
Patch0167: 0167-squish-BLS-only-write-etc-kernel-cmdline-if-writable.patch
Patch0168: 0168-blscfg-Don-t-root-device-in-emu-builds.patch
Patch0169: 0169-ppc64le-signed-boot-media-changes.patch
Patch0170: 0170-core-Fix-several-implicit-function-declarations.patch
Patch0171: 0171-ieee1275-request-memory-with-ibm-client-architecture.patch
Patch0172: 0172-hostdisk-work-around-proc-not-reporting-size.patch
Patch0173: 0173-blscfg-check-for-mounted-boot-in-emu.patch
Patch0174: 0174-grub_dl_set_mem_attrs-fix-format-string.patch
Patch0175: 0175-grub_dl_set_mem_attrs-add-self-check-for-the-tramp-G.patch
Patch0176: 0176-grub_dl_load_segments-page-align-the-tramp-GOT-areas.patch
Patch0177: 0177-emu-Add-switch-root-to-grub-emu.patch
Patch0178: 0178-util-Enable-default-kernel-for-updates.patch
Patch0179: 0179-efi-http-change-uint32_t-to-uintn_t.patch
Patch0180: 0180-Add-Install-section-to-aux-systemd-units.patch
Patch0181: 0181-Fix-missing-include-in-ofdisk.c.patch
Patch0182: 0182-add-flag-to-only-search-root-dev.patch
Patch0183: 0183-cryptdisk-fix-incorrect-sign-comparison.patch
Patch0184: 0184-grub-install-fix-a-sign-comparison-error.patch
Patch0185: 0185-grub-mount-work-around-bad-integer-comparison.patch
Patch0186: 0186-power-Fix-use-after-free-in-get_slave_from_dm.patch
Patch0187: 0187-Fix-some-sign-comparison-errors.patch
Patch0188: 0188-normal-Fix-a-discarded-const.patch
Patch0189: 0189-at_keyboard-mark-grub_keyboard_controller_write-unus.patch
Patch0190: 0190-Fix-another-minor-sign-comparison-error.patch
Patch0191: 0191-Revert-mm-Assert-that-we-preserve-header-vs-region-a.patch
Patch0192: 0192-make-use-the-_CPU-variety-of-build-flags-for-PROGRAM.patch
Patch0193: 0193-include-proper-attribute-for-an-EFI-API-call-definit.patch
Patch0194: 0194-cast-grub_error-status-parameter.patch
Patch0195: 0195-remove-unused-varible.patch
Patch0196: 0196-cast-grub_net_bootp_packet-pointer.patch
Patch0197: 0197-Add-support-for-Linux-EFI-stub-loading.patch
Patch0198: 0198-fix-i386_pc-on-legacycfg-module.patch
Patch0199: 0199-Add-secureboot-support-on-efi-chainloader.patch
Patch0200: 0200-Make-any-of-the-loaders-that-link-in-efi-mode-honor-.patch
Patch0201: 0201-Minimize-the-sort-ordering-for-.debug-and-rescue-ker.patch
Patch0202: 0202-Add-grub_qdprintf-grub_dprintf-without-the-file-line.patch
Patch0203: 0203-Make-a-gdb-dprintf-that-tells-us-load-addresses.patch
Patch0204: 0204-Handle-multi-arch-64-on-32-boot-in-linuxefi-loader.patch
Patch0205: 0205-Try-to-pick-better-locations-for-kernel-and-initrd.patch
Patch0206: 0206-x86-efi-Use-bounce-buffers-for-reading-to-addresses-.patch
Patch0207: 0207-x86-efi-Re-arrange-grub_cmd_linux-a-little-bit.patch
Patch0208: 0208-x86-efi-Make-our-own-allocator-for-kernel-stuff.patch
Patch0209: 0209-x86-efi-Allow-initrd-params-cmdline-allocations-abov.patch
Patch0210: 0210-efi-Set-image-base-address-before-jumping-to-the-PE-.patch
Patch0211: 0211-x86-efi-Reduce-maximum-bounce-buffer-size-to-16-MiB.patch
Patch0212: 0212-efilinux-Fix-integer-overflows-in-grub_cmd_initrd.patch
Patch0213: 0213-linuxefi-fail-kernel-validation-without-shim-protoco.patch
Patch0214: 0214-Allow-chainloading-EFI-apps-from-loop-mounts.patch
Patch0215: 0215-grub-core-loader-i386-efi-linux.c-do-not-validate-ke.patch
Patch0216: 0216-grub-core-loader-efi-chainloader.c-do-not-validate-c.patch
Patch0217: 0217-grub-core-loader-efi-linux.c-drop-now-unused-grub_li.patch
Patch0218: 0218-loader-efi-chainloader-grub_load_and_start_image-doe.patch
Patch0219: 0219-loader-efi-chainloader-simplify-the-loader-state.patch
Patch0220: 0220-loader-i386-efi-linux-Avoid-a-use-after-free-in-the-.patch
Patch0221: 0221-loader-i386-efi-linux-Use-grub_loader_set_ex.patch
Patch0222: 0222-loader-i386-efi-linux-Fix-a-memory-leak-in-the-initr.patch
Patch0223: 0223-EFI-allocate-kernel-in-EFI_RUNTIME_SERVICES_CODE-ins.patch
Patch0224: 0224-efi-use-enumerated-array-positions-for-our-allocatio.patch
Patch0225: 0225-efi-split-allocation-policy-for-kernel-vs-initrd-mem.patch
Patch0226: 0226-efi-allocate-the-initrd-within-the-bounds-expressed-.patch
Patch0227: 0227-efi-use-EFI_LOADER_-CODE-DATA-for-kernel-and-initrd-.patch
Patch0228: 0228-x86-efi-Fix-an-incorrect-array-size-in-kernel-alloca.patch
Patch0229: 0229-grub-install-on-EFI-if-forced.patch
Patch0230: 0230-Remove-Install-section-from-aux-systemd-units.patch
Patch0231: 0231-grub-set-bootflag-Conservative-partial-fix-for-CVE-2.patch
Patch0232: 0232-grub-set-bootflag-More-complete-fix-for-CVE-2024-104.patch
Patch0233: 0233-grub-set-bootflag-Exit-calmly-when-not-running-as-ro.patch
Patch0234: 0234-Makefile.core.def-fix-linux-module.patch
Patch0235: 0235-Add-support-for-Linux-EFI-stub-loading-on-arm-archit.patch
Patch0236: 0236-arm-arm64-loader-Better-memory-allocation-and-error-.patch
Patch0237: 0237-arm64-Fix-EFI-loader-kernel-image-allocation.patch
Patch0238: 0238-pe-add-the-DOS-header-struct-and-fix-some-bad-naming.patch
Patch0239: 0239-Correct-BSS-zeroing-on-aarch64.patch
Patch0240: 0240-arm64-Use-proper-memory-type-for-kernel-allocation.patch
Patch0241: 0241-normal-Remove-grub_env_set-prefix-in-grub_try_normal.patch
Patch0242: 0242-Ignore-warnings-for-incompatible-types.patch
Patch0243: 0243-cmd-search-Rework-of-CVE-2023-4001-fix.patch
Patch0244: 0244-loader-efi-linux.c-read-the-kernel-image-before-head.patch
Patch0245: 0245-nx-set-attrs-in-our-kernel-loaders.patch
Patch0246: 0246-efi-Provide-wrappers-for-load_image-start_image.patch
Patch0247: 0247-efi-Disallow-fallback-to-legacy-Linux-loader-when-sh.patch
Patch0248: 0248-Set-non-executable-stack-sections-on-EFI-assembly-fi.patch
Patch0249: 0249-grub-mkconfig.in-turn-off-executable-owner-bit.patch
Patch0250: 0250-grub2-mkconfig-Ensure-grub-cfg-stub-is-not-overwritt.patch
Patch0251: 0251-grub2-mkconfig-Simplify-os_name-detection.patch
Patch0252: 0252-grub-mkconfig-Remove-check-for-mount-point-for-grub-.patch
Patch0253: 0253-efi-api.h-include-missing-__grub_efi_api-macros-on-E.patch
Patch0254: 0254-grub-core-net-arp.c-fix-variable-name.patch
Patch0255: 0255-load-EFI-commands-inside-test-expressions.patch
Patch0256: 0256-efi-loader-Check-if-NX-is-required-in-grub_efi_linux.patch
Patch0257: 0257-Stop-grub.efi-from-always-printing-dynamic_load_symb.patch
Patch0258: 0258-cmd-search-Fix-a-possible-NULL-ptr-dereference.patch
Patch0259: 0259-Enable-building-blscfg-module-on-xen-and-xen_pvh.patch
Patch0260: 0260-loader-efi-Fix-RISC-V-build.patch
Patch0261: 0261-Use-medany-instead-of-large-model-for-RISCV.patch
Patch0262: 0262-fs-xfs-fix-large-extent-counters-incompat-feature-su.patch
Patch0263: 0263-term-nns8250-spcr-return-if-redirection-is-disabled.patch
Patch0264: 0264-commands-bli-Fix-crash-in-get_part_uuid.patch
Patch0265: 0265-misc-Implement-grub_strlcpy.patch
Patch0266: 0266-fs-tar-Integer-overflow-leads-to-heap-OOB-write.patch
Patch0267: 0267-fs-jfs-Fix-OOB-read-in-jfs_getent.patch
Patch0268: 0268-fs-jfs-Fix-OOB-read-caused-by-invalid-dir-slot-index.patch
Patch0269: 0269-fs-ext2-Fix-out-of-bounds-read-for-inline-extents.patch
Patch0270: 0270-fs-ntfs-Fix-out-of-bounds-read.patch
Patch0271: 0271-fs-ntfs-Use-a-helper-function-to-access-attributes.patch
Patch0272: 0272-kern-file-Ensure-file-data-is-set.patch
Patch0273: 0273-kern-file-Implement-filesystem-reference-counting.patch
Patch0274: 0274-cli_lock-Add-build-option-to-block-command-line-inte.patch
Patch0275: 0275-disk-cryptodisk-Require-authentication-after-TPM-unl.patch
Patch0276: 0276-disk-loopback-Reference-tracking-for-the-loopback.patch
Patch0277: 0277-net-Remove-variables-hooks-when-interface-is-unregis.patch
Patch0278: 0278-kern-dl-Fix-for-an-integer-overflow-in-grub_dl_ref.patch
Patch0279: 0279-kern-dl-Check-for-the-SHF_INFO_LINK-flag-in-grub_dl_.patch
Patch0280: 0280-commands-ls-Fix-NULL-dereference.patch
Patch0281: 0281-gettext-Remove-variables-hooks-on-module-unload.patch
Patch0282: 0282-commands-test-Stack-overflow-due-to-unlimited-recurs.patch
Patch0283: 0283-fs-bfs-Disable-under-lockdown.patch
Patch0284: 0284-fs-Disable-many-filesystems-under-lockdown.patch
Patch0285: 0285-disk-Use-safe-math-macros-to-prevent-overflows.patch
Patch0286: 0286-disk-Check-if-returned-pointer-for-allocated-memory-.patch
Patch0287: 0287-fs-Use-safe-math-macros-to-prevent-overflows.patch
Patch0288: 0288-fs-Prevent-overflows-when-assigning-returned-values-.patch
Patch0289: 0289-net-Use-safe-math-macros-to-prevent-overflows.patch
Patch0290: 0290-fs-ext2-Rework-out-of-bounds-read-for-inline-and-ext.patch
Patch0291: 0291-normal-menu-Check-return-code-of-the-script-when-exe.patch
Patch0292: 0292-ieee1275-ofnet-Fix-grub_malloc-removed-after-added-s.patch
Patch0293: 0293-grub-mkimage-Create-new-ELF-note-for-SBAT.patch
Patch0294: 0294-grub-mkimage-Add-SBAT-metadata-into-ELF-note-for-Pow.patch
Patch0295: 0295-10_linux.in-escape-kernel-option-characters-properly.patch
Patch0296: 0296-blscfg-check-if-variable-is-escaped-before-consideri.patch
Patch0297: 0297-kern-rescue_reader-Block-the-rescue-mode-until-the-C.patch
Patch0298: 0298-commands-search-Introduce-the-cryptodisk-only-argume.patch
Patch0299: 0299-commands-search-Add-the-diskfilter-support.patch
Patch0300: 0300-disk-cryptodisk-Add-the-erase-secrets-function.patch
Patch0301: 0301-cryptocheck-Add-quiet-option.patch
Patch0302: 0302-loader-efi-chainloader-Fix-double-free.patch
Patch0303: 0303-loader-efi-chainloader-Fix-null-pointer-dereference.patch
Patch0304: 0304-Set-correctly-the-memory-attributes-for-the-kernel-P.patch
Patch0305: 0305-util-grub-editenv-add-fs_envblk-open-helper.patch
Patch0306: 0306-util-grub-editenv-add-fs_envblk-write-helper.patch
Patch0307: 0307-util-grub-editenv-add-probe-call-for-external-envblk.patch
Patch0308: 0308-btrfs-add-environment-block-to-reserved-header-area.patch
Patch0309: 0309-docs-add-Btrfs-env-block-and-special-env-vars.patch
Patch0310: 0310-util-grub.d-00_header.in-Prefer-dev-instead-of-root-.patch
Patch0311: 0311-grub.d-Support-the-external-environment-block-for-au.patch
Patch0312: 0312-grub-editenv-Make-automatic-hidden-menu-and-boot-cou.patch
Patch0313: 0313-ieee1275-ofnet-Fix-hw_addr-variable-initialization.patch
Patch0314: 0314-Revert-loader-efi-Fix-RISC-V-build.patch
Patch0315: 0315-Revert-efi-Disallow-fallback-to-legacy-Linux-loader-.patch
Patch0316: 0316-Partial-revert-nx-set-attrs-in-our-kernel-loaders.patch
Patch0317: 0317-Revert-loader-efi-linux.c-read-the-kernel-image-befo.patch
Patch0318: 0318-Revert-arm64-Use-proper-memory-type-for-kernel-alloc.patch
Patch0319: 0319-Revert-Correct-BSS-zeroing-on-aarch64.patch
Patch0320: 0320-Revert-arm64-Fix-EFI-loader-kernel-image-allocation.patch
Patch0321: 0321-Revert-Add-support-for-Linux-EFI-stub-loading-on-arm.patch
Patch0322: 0322-loader-efi-linux.c-Free-mempath-after-use.patch
Patch0323: 0323-loader-efi-linux.c-Unload-image-on-errors.patch
Patch0324: 0324-loader-efi-linux.c-Disable-code-not-used-on-x86-when.patch
Patch0325: 0325-commands-test-Fix-error-in-recursion-depth-calculati.patch
Patch0326: 0326-kern-file-Call-grub_dl_unref-after-fs-fs_close.patch
Patch0327: 0327-term-serial.c-default-efi0-as-serial-port-if-present.patch
Patch0328: 0328-util-grub-editenv-remove-stale-env_block-on-unsuppor.patch
Patch0329: 0329-Change-login-error-message.patch
Patch0330: 0330-mdraid-fix-metadata-1.0-detection-in-userspace-utili.patch
Patch0331: 0331-grub-install-use-search.fs_uuid-for-RAID1-on-IEEE127.patch
Patch0332: 0332-ieee1275-powerpc-implements-fibre-channel-discovery-.patch
Patch0333: 0333-ieee1275-implement-FCP-methods-for-WWPN-and-LUNs.patch
Patch0334: 0334-ieee1275-change-the-logic-of-ieee1275_get_devargs.patch
Patch0335: 0335-ieee1275-ofpath-enable-NVMeoF-logical-device-transla.patch
Patch0336: 0336-ieee1275-support-added-for-multiple-nvme-bootpaths.patch
Patch0337: 0337-ieee1275-add-support-for-NVMeoFC.patch
Patch0338: 0338-grub-get-kernel-settings-Treate-kernel-uki-dtbloader.patch
Patch0339: 0339-mm-try-allocating-regions-above-defined-limit-as-las.patch
Patch0340: 0340-tpm-Only-skip-TPM-string-PCR-measurements-with-expli.patch
Patch0341: 0341-bli-Allow-overriding-PACKAGE_STRING-via-grub-mkimage.patch
Patch0342: 0342-Revert-Use-medany-instead-of-large-model-for-RISCV.patch
Patch0343: 0343-configure-Add-mno-relax-on-riscv.patch
Patch0344: 0344-platform-Return-i386-pc-when-proc-device-tree-is-pre.patch
Patch0345: 0345-term-serial-Reject-caller-supplied-port-addresses-un.patch
Patch0346: 0346-kern-efi-mm-try-allocating-in-the-lower-4GB-first.patch
Patch0347: 0347-ieee1275-use-namespace-instead-of-disk-for-PCIe-NVMe.patch
Patch0348: 0348-work-around-clang-miscompilation-w-grub-2.12.patch
Patch0349: 0349-build-force-no-pie.patch
Patch0350: 0350-disable-falign-loops-which-is-not-supported-on-clang.patch
Patch0351: 0351-workaround-enable-R_X86_64_32.patch
Patch0352: 0352-arm64-add-missing-relocations-for-clang.patch
Patch0353: 0353-freestanding-do-not-emit-.interp.patch
Patch0354: 0354-fix-leftover-rebase-conflict-markers.patch
Patch0355: 0355-apply-leftover-reject-hunks-that-apply-cleanly-to-2..patch
Patch0356: 0356-restore-mkconfig-BLS-DTB-btrfs-exports-and-minicmd-e.patch

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
%oreon_sha256
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
echo '%{source4_hash}  %{SOURCE4}' | sha256sum -c -
%do_common_setup
%if 0%{with_efi_arch}
mkdir grub-%{grubefiarch}-%{tarversion}
grep -A100000 '# stuff "make" creates' .gitignore > grub-%{grubefiarch}-%{tarversion}/.gitignore
cp %{SOURCE4} grub-%{grubefiarch}-%{tarversion}/unifont.pcf.gz
sed -e "s,@@VERSION@@,%{version},g" -e "s,@@VERSION_RELEASE@@,%{version}-%{release},g" \
    %{SOURCE12} > grub-%{grubefiarch}-%{tarversion}/sbat.csv
git add grub-%{grubefiarch}-%{tarversion}
mkdir grub-%{grubefiarch}-%{tarversion}-cc
grep -A100000 '# stuff "make" creates' .gitignore > grub-%{grubefiarch}-%{tarversion}-cc/.gitignore
cp %{SOURCE4} grub-%{grubefiarch}-%{tarversion}-cc/unifont.pcf.gz
sed -e "s,@@VERSION@@,%{version},g" -e "s,@@VERSION_RELEASE@@,%{version}-%{release},g" \
    %{SOURCE12} > grub-%{grubefiarch}-%{tarversion}-cc/sbat.csv
git add grub-%{grubefiarch}-%{tarversion}-cc
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
%{expand:%do_primary_efi_build %%{grubefiarch} %%{grubefiname} %%{grubeficdname} %%{_target_platform} %%{efi_target_cflags} %%{efi_host_cflags} %{sb_ca} %{sb_cer} %{sb_key}}
%endif
%if 0%{with_alt_efi_arch}
%{expand:%do_alt_efi_build %%{grubaltefiarch} %%{grubaltefiname} %%{grubalteficdname} %%{_alt_target_platform} %%{alt_efi_target_cflags} %%{alt_efi_host_cflags} %{sb_ca} %{sb_cer} %{sb_key}}
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

install -d -m 0755 %{buildroot}%{_prefix}/lib/kernel/install.d/
install -D -m 0755 -t %{buildroot}%{_prefix}/lib/kernel/install.d/ %{SOURCE10}
install -D -m 0755 -t %{buildroot}%{_prefix}/lib/kernel/install.d/ %{SOURCE14}
install -D -m 0755 -t %{buildroot}%{_prefix}/lib/kernel/install.d/ %{SOURCE3}
install -d -m 0755 %{buildroot}%{_sysconfdir}/kernel/install.d/
install -D -m 0644 -t %{buildroot}%{_userunitdir} \
	docs/grub-boot-success.{timer,service}
install -D -m 0644 -t %{buildroot}%{_unitdir} docs/grub-boot-indeterminate.service
install -d -m 0755 %{buildroot}%{_unitdir}/system-update.target.wants
install -d -m 0755 %{buildroot}%{_unitdir}/reboot.target.wants
ln -s ../grub-boot-indeterminate.service \
	%{buildroot}%{_unitdir}/system-update.target.wants
ln -s ../grub2-systemd-integration.service \
	%{buildroot}%{_unitdir}/reboot.target.wants

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
:

%post tools
%systemd_user_post grub-boot-success.timer

%preun tools
%systemd_user_preun grub-boot-success.timer

%postun tools
%systemd_user_postun_with_restart grub-boot-success.timer

%triggerpostun tools -- grub2-tools < 1:2.06-107
/usr/lib/systemd/systemd-update-helper install-user-units grub-boot-success.timer

%posttrans common
set -eu

GRUB_DIR=/boot/grub2

if test ! -f ${GRUB_DIR}/grub.cfg; then
    grub2-mkconfig -o ${GRUB_DIR}/grub.cfg  || :
else
    GRUB_CFG_MODE=$(stat --format="%a" ${GRUB_DIR}/grub.cfg)
    if ! test "${GRUB_CFG_MODE}" = "600"; then
        chmod 0600 ${GRUB_DIR}/grub.cfg || :
    fi
fi

%if "%{platform}" == "pc"
%posttrans pc
set -eu
set -o pipefail

SYS_FIRMWARE_EFI_DIR=/sys/firmware/efi
BOOT_DIR=/boot

find_grub_devices() {
    local boot_device
    local component_devs=()
    local block_devs=()

    if test -d $SYS_FIRMWARE_EFI_DIR ; then
	exit 0
    fi

    if ! command -v grub2-probe &>/dev/null; then
	exit 0;
    fi

    boot_device=$(grub2-probe --target=device $BOOT_DIR)

    if command -v mdadm &>/dev/null && \
       mdadm --detail --verbose --brief "$boot_device" &> /dev/null; then
	out=$(mdadm --detail --verbose --brief "$boot_device")
	for d in $(echo "$out" | sed -n -e 's/.* devices=\([^ ]*\).*/\1/p' | sed 's/,/ /g'); do
	    component_devs+=("$d")
	done
    else
	component_devs+=("$boot_device")
    fi

    for d in "${component_devs[@]}"; do
	block_devs+=("$(lsblk -spnlo name "$d" | tail -1)")
    done

    for d in "${block_devs[@]}"; do
	if dd if="$d" bs=446 count=1 status=none | grep -aq "GRUB"; then
	    echo "$d"
	fi
    done
}

grub_install () {
    if ! command -v grub2-install &>/dev/null; then
	exit 0
    fi
    for d in $(find_grub_devices); do
	echo "Installing on $d" >&2
	grub2-install "$d"
    done
}

grub_install || :
%endif

%if 0%{with_efi_arch}
%posttrans efi-%{efiarch}
set -eu

GRUB_DIR=/boot/grub2
EFI_DIR=%{grub_efi_dir}
EFI_ESP_DIR=%{efi_esp_dir}
ESP_PATH=/boot/efi

if test -f ${EFI_DIR}/grub.cfg; then
    if (((grep -q "configfile" ${EFI_DIR}/grub.cfg && grep -q "root-dev-only" ${EFI_DIR}/grub.cfg) || grep -q "source" ${EFI_DIR}/grub.cfg) && ! grep -q "# It is automatically generated by grub2-mkconfig using templates" ${EFI_DIR}/grub.cfg); then
        : # Already unified
    else
        gen_grub_cfgstub ${GRUB_DIR} ${EFI_DIR} || :
    fi
else
    gen_grub_cfgstub ${GRUB_DIR} ${EFI_DIR} || :
fi

if [[ ! -e "/run/ostree-booted" ]]; then
   cp -d --preserve=all ${EFI_DIR}/* ${EFI_ESP_DIR} || :
fi

if test -f ${EFI_DIR}/grubenv; then
    cp -a ${EFI_DIR}/grubenv ${EFI_DIR}/grubenv.rpmsave
    mv --force ${EFI_DIR}/grubenv ${GRUB_DIR}/grubenv
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
%attr(0644,root,root) %{_userunitdir}/grub-boot-success.timer
%attr(0644,root,root) %{_userunitdir}/grub-boot-success.service
%attr(0644,root,root) %{_unitdir}/grub-boot-indeterminate.service
%{_unitdir}/system-update.target.wants
%attr(0644,root,root) %{_unitdir}/grub2-systemd-integration.service
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
%autochangelog
