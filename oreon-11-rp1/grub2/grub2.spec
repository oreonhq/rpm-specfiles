%global source0_hash none
%global source1_hash 00a25a5c3a18d9d7b0deb456344f7ab02f6f9ef8422fbe6174afafc546c8ee36

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
Release:	57%{?dist}
Summary:	Bootloader with support for Linux, Multiboot and more
License:	GPL-3.0-or-later
URL:		http://www.gnu.org/software/grub/
Obsoletes:	grub < 1:0.98
Source0:        https://mirrors.kernel.org/gnu/grub/grub-%{tarversion}.tar.xz
# Savannah cgit snapshots are flaky for spectool or mock, use GitHub mirror + fixed name
Source1:        https://github.com/coreutils/gnulib/archive/9f48fb992a3d7e96610c4ce8be969cff2d61a01b.tar.gz#/gnulib-9f48fb992a3d7e96610c4ce8be969cff2d61a01b.tar.gz
Source2:        99-grub-mkconfig.install
Source3:	https://unifoundry.com/pub/unifont/unifont-13.0.06/font-builds/unifont-13.0.06.pcf.gz
Source5:        bootstrap
Source6:        bootstrap.conf
Source7:        strtoull_test.c
Source8:        20-grub.install
Source9:        sbat.csv.in
Source10:        gen_grub_cfgstub
Source11:        95-set-boot-entry.install


# Inlined from grub.macros (parse-time %%include removed for spectool)
# vim:filetype=spec
# Modules always contain just 32-bit code
%global evr %{epoch}:%{version}-%{release}
%global _libdir %{_exec_prefix}/lib

%if 0%{?oreon}
%global os_id oreon
%else
%global os_id %(eval echo $(grep ^ID= /etc/os-release | sed -e 's/^ID=//' -e 's/rhel/redhat/'))
%endif
%global grub_evr_dir %{_libdir}/efi/grub2/%{evr}
%global grub_efi_dir %{grub_evr_dir}/EFI/%{os_id}

%global _binaries_in_noarch_packages_terminate_build 0
#%%undefine _missing_build_ids_terminate_build
%{expand:%%{!?buildsubdir:%%global buildsubdir grub-%{tarversion}}}
%{expand:%%{!?_licensedir:%%global license %%%%doc}}

%global _configure ../configure

%if %{?_with_ccache: 1}%{?!_with_ccache: 0}
%global ccpath /usr/%{_lib}/ccache/gcc
%else
%global ccpath %{__cc}
%endif

# gnulib actively ignores CFLAGS because it's terrible
# build aarch64 gnulib with branch protection
%ifarch aarch64
%global cc_equals "CC=%{ccpath} -fPIE -Wl,-z,noexecstack -Wl,--no-warn-rwx-segments -mbranch-protection=standard"
%else
%global cc_equals "CC=%{ccpath} -fPIE -Wl,-z,noexecstack -Wl,--no-warn-rwx-segments"
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
		-e 's/^/ -fno-strict-aliasing /'		\\\
		%{nil}

%global host_cflags_ %{expand:%%(echo %{build_cflags} %{?_hardening_cflags} | %{cflags_sed})} -fstack-protector-strong
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
		-e 's/^$//'					\\\
		%{nil}

%global host_ldflags %{expand:%%(echo %{build_ldflags} %{?_hardening_ldflags} | %{ldflags_sed})}
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

# sparc is always compiled 64 bit
%ifarch %{sparc}
%global target_cpu_name sparc64
%global _target_platform %{target_cpu_name}-%{_vendor}-%{_target_os}%{?_gnu}
%global legacy_target_cpu_name %{_arch}
%global legacy_package_arch ieee1275
%global platform ieee1275
%endif
# ppc is always compiled 64 bit
%ifarch ppc ppc64 ppc64le
# GRUB emu fails to build on ppc64le
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
%{!?with_efi_arch:%global without_efi_arch 0}
%{?with_efi_arch:%global without_efi_arch 1}
%{!?with_efi_only:%global without_efi_only 0}
%{?with_efi_only:%global without_efi_only 1}

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
%global platform_modules " backtrace chain tpm usb usbserial_common usbserial_pl2303 usbserial_ftdi usbserial_usbdebug keylayouts at_keyboard "
%endif

%ifarch ppc64le
%global platform_modules " appendedsig tpm ofnet "
%endif

%ifarch aarch64 %{arm} riscv64
%global platform_modules " "
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
Requires:	gettext-runtime which file				\
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
cp %{SOURCE3} unifont.pcf.gz					\
cp %{SOURCE5} bootstrap						\
cp %{SOURCE6} bootstrap.conf					\
cp %{SOURCE7} ./grub-core/tests/strtoull_test.c			\
cp %{SOURCE1} gnulib-%{gnulibversion}.tar.gz			\
tar -zxf gnulib-%{gnulibversion}.tar.gz				\
mv gnulib-%{gnulibversion} gnulib				\
git init							\
echo '![[:digit:]][[:digit:]]_*.in' > util/grub.d/.gitignore	\
echo '!*.[[:digit:]]' > util/.gitignore				\
echo '!config.h' > include/grub/emu/.gitignore			\
git config user.email "packaging@oreonhq.com"			\
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
%{expand:%%define __pesign_client_cert oreon-grub2-signer} \
%{expand:%%{pesign -s -i %%{2}.onesig -o %%{2} -a %%{5} -c %%{6} -n %%{7}}}	\
%{expand:%%{pesign -s -i %%{3}.onesig -o %%{3} -a %%{5} -c %%{6} -n %%{7}}}	\
%{nil}
%endif

%ifarch ppc64le
# RHEL signs, Fedora + ELN + Oreon don't (ELN defines rhel)
%if 0%{?fedora} || 0%{?eln} || (0%{?oreon} >= 11)
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
# FIXME: using this prefix is fragile, must be done properly	\
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
%{expand:%%{efi_mkimage %{1} %{2} %{3} %{4}}}			\
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
%{expand:%%do_efi_build_images %{grub_target_name} %{2} %{3} ./ } \
cd ..								\
%{nil}

%define do_alt_efi_build()					\
cd grub-%{1}-%{tarversion}					\
%{expand:%%do_efi_configure %%{4} %%{5} %%{6}}			\
%do_efi_build_modules						\
%{expand:%%do_efi_link_utils %{grubefiarch}}			\
%{expand:%%do_efi_build_images %{alt_grub_target_name} %{2} %{3} ../grub-%{grubefiarch}-%{tarversion}/ } \
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
install -d -m 0700 ${RPM_BUILD_ROOT}%{grub_efi_dir}/		\
install -m 700 %{2} $RPM_BUILD_ROOT%{grub_efi_dir}/%{2}	\
install -m 700 %{3} $RPM_BUILD_ROOT%{grub_efi_dir}/%{3}	\
%ifarch %{arm}							\
install -D -m 700 %{2} $RPM_BUILD_ROOT%{efi_esp_boot}/BOOTARM.EFI \
%endif								\
install -D -m 700 %{SOURCE10}					\\\
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
install -d -m 0700 ${RPM_BUILD_ROOT}/boot/loader/entries	\
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
%dir %attr(0700,root,root)/boot/loader/entries			\
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
%dir %attr(0700,root,root) %{grub_efi_dir}                      \
%attr(0700,root,root) %{grub_efi_dir}/%{2} 	\
%ifarch %{arm}							\
%attr(0700,root,root) %verify(not mtime) %{efi_esp_boot}/BOOTARM.EFI \
%endif								\
%attr(0700,root,root)/boot/grub2/fonts			\
%attr(0700,root,root)/usr/bin/gen_grub_cfgstub			\
%dir %attr(0700,root,root)/boot/loader/entries			\
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
# Inlined from grub.patches
Patch0001:        0001-Revert-templates-Fix-user-facing-typo-with-an-incorr.patch
Patch0002:        0002-Revert-templates-Properly-disable-the-os-prober-by-d.patch
Patch0003:        0003-Revert-templates-Disable-the-os-prober-by-default.patch
Patch0004:        0004-Rework-linux-command.patch
Patch0005:        0005-Rework-linux16-command.patch
Patch0006:        0006-re-write-.gitignore.patch
Patch0007:        0007-IBM-client-architecture-CAS-reboot-support.patch
Patch0008:        0008-for-ppc-reset-console-display-attr-when-clear-screen.patch
Patch0009:        0009-Disable-GRUB-video-support-for-IBM-power-machines.patch
Patch0010:        0010-Move-bash-completion-script-922997.patch
Patch0011:        0011-Allow-fallback-to-include-entries-by-title-not-just-.patch
Patch0012:        0012-Make-exit-take-a-return-code.patch
Patch0013:        0013-Make-efi-machines-load-an-env-block-from-a-variable.patch
Patch0014:        0014-Migrate-PPC-from-Yaboot-to-Grub2.patch
Patch0015:        0015-Add-fw_path-variable-revised.patch
Patch0016:        0016-Pass-x-hex-hex-straight-through-unmolested.patch
Patch0017:        0017-blscfg-add-blscfg-module-to-parse-Boot-Loader-Specif.patch
Patch0018:        0018-Add-devicetree-loading.patch
Patch0019:        0019-Enable-pager-by-default.-985860.patch
Patch0020:        0020-Don-t-say-GNU-Linux-in-generated-menus.patch
Patch0021:        0021-Add-.eh_frame-to-list-of-relocations-stripped.patch
Patch0022:        0022-Don-t-require-a-password-to-boot-entries-generated-b.patch
Patch0023:        0023-use-fw_path-prefix-when-fallback-searching-for-grub-.patch
Patch0024:        0024-Try-mac-guid-etc-before-grub.cfg-on-tftp-config-file.patch
Patch0025:        0025-Generate-OS-and-CLASS-in-10_linux-from-etc-os-releas.patch
Patch0026:        0026-Try-prefix-if-fw_path-doesn-t-work.patch
Patch0027:        0027-Make-grub2-mkconfig-construct-titles-that-look-like-.patch
Patch0028:        0028-Add-friendly-grub2-password-config-tool-985962.patch
Patch0029:        0029-tcp-add-window-scaling-support.patch
Patch0030:        0030-efinet-and-bootp-add-support-for-dhcpv6.patch
Patch0031:        0031-bootp-New-net_bootp6-command.patch
Patch0032:        0032-Add-grub-get-kernel-settings-and-use-it-in-10_linux.patch
Patch0033:        0033-Make-grub_fatal-also-backtrace.patch
Patch0034:        0034-Make-our-info-pages-say-grub2-where-appropriate.patch
Patch0035:        0035-macos-just-build-chainloader-entries-don-t-try-any-x.patch
Patch0036:        0036-grub2-btrfs-Add-ability-to-boot-from-subvolumes.patch
Patch0037:        0037-btrfs-fix-a-bad-null-check.patch
Patch0038:        0038-export-btrfs_subvol-and-btrfs_subvolid.patch
Patch0039:        0039-grub2-btrfs-03-follow_default.patch
Patch0040:        0040-grub2-btrfs-04-grub2-install.patch
Patch0041:        0041-grub2-btrfs-05-grub2-mkconfig.patch
Patch0042:        0042-grub2-btrfs-06-subvol-mount.patch
Patch0043:        0043-Fallback-to-old-subvol-name-scheme-to-support-old-sn.patch
Patch0044:        0044-Grub-not-working-correctly-with-btrfs-snapshots-bsc-.patch
Patch0045:        0045-Add-grub_efi_allocate_pool-and-grub_efi_free_pool-wr.patch
Patch0046:        0046-Use-grub_efi_.-memory-helpers-where-reasonable.patch
Patch0047:        0047-Add-PRIxGRUB_EFI_STATUS-and-use-it.patch
Patch0048:        0048-don-t-use-int-for-efi-status.patch
Patch0049:        0049-make-GRUB_MOD_INIT-declare-its-function-prototypes.patch
Patch0050:        0050-Don-t-guess-boot-efi-as-HFS-on-ppc-machines-in-grub-.patch
Patch0051:        0051-20_linux_xen-load-xen-or-multiboot-2-modules-as-need.patch
Patch0052:        0052-align-struct-efi_variable-better.patch
Patch0053:        0053-Add-BLS-support-to-grub-mkconfig.patch
Patch0054:        0054-Don-t-attempt-to-backtrace-on-grub_abort-for-grub-em.patch
Patch0055:        0055-Add-grub2-switch-to-blscfg.patch
Patch0056:        0056-normal-don-t-draw-our-startup-message-if-debug-is-se.patch
Patch0057:        0057-Work-around-some-minor-include-path-weirdnesses.patch
Patch0058:        0058-Make-it-possible-to-enabled-build-id-sha1.patch
Patch0059:        0059-make-better-backtraces.patch
Patch0060:        0060-Fixup-for-newer-compiler.patch
Patch0061:        0061-Don-t-attempt-to-export-the-start-and-_start-symbols.patch
Patch0062:        0062-Fixup-for-newer-compiler.patch
Patch0063:        0063-Add-support-for-non-Ethernet-network-cards.patch
Patch0064:        0064-efinet-UEFI-IPv6-PXE-support.patch
Patch0065:        0065-grub.texi-Add-net_bootp6-doument.patch
Patch0066:        0066-bootp-Add-processing-DHCPACK-packet-from-HTTP-Boot.patch
Patch0067:        0067-Fix-const-char-pointers-in-grub-core-net-bootp.c.patch
Patch0068:        0068-efinet-Setting-network-from-UEFI-device-path.patch
Patch0069:        0069-efinet-Setting-DNS-server-from-UEFI-protocol.patch
Patch0070:        0070-Support-UEFI-networking-protocols.patch
Patch0071:        0071-AUDIT-0-http-boot-tracker-bug.patch
Patch0072:        0072-grub-editenv-Add-incr-command-to-increment-integer-v.patch
Patch0073:        0073-Add-auto-hide-menu-support.patch
Patch0074:        0074-Add-grub-set-bootflag-utility.patch
Patch0075:        0075-docs-Add-grub-boot-indeterminate.service-example.patch
Patch0076:        0076-gentpl-add-disable-support.patch
Patch0077:        0077-gentpl-add-pc-firmware-type.patch
Patch0078:        0078-efinet-also-use-the-firmware-acceleration-for-http.patch
Patch0079:        0079-efi-http-Make-root_url-reflect-the-protocol-hostname.patch
Patch0080:        0080-Make-it-so-we-can-tell-configure-which-cflags-utils-.patch
Patch0081:        0081-Rework-how-the-fdt-command-builds.patch
Patch0082:        0082-Disable-non-wordsize-allocations-on-arm.patch
Patch0083:        0083-Prepend-prefix-when-HTTP-path-is-relative.patch
Patch0084:        0084-Make-grub_error-more-verbose.patch
Patch0085:        0085-Make-reset-an-alias-for-the-reboot-command.patch
Patch0086:        0086-Add-a-version-command.patch
Patch0087:        0087-Add-more-dprintf-and-nerf-dprintf-in-script.c.patch
Patch0088:        0088-Attempt-to-fix-up-all-the-places-Wsign-compare-error.patch
Patch0089:        0089-Don-t-use-Wno-sign-compare-Wno-conversion-Wno-error-.patch
Patch0090:        0090-Fix-getroot.c-s-trampolines.patch
Patch0091:        0091-Do-not-allow-stack-trampolines-anywhere.patch
Patch0092:        0092-Reimplement-boot_counter.patch
Patch0093:        0093-Fix-menu-entry-selection-based-on-ID-and-title.patch
Patch0094:        0094-Make-the-menu-entry-users-option-argument-to-be-opti.patch
Patch0095:        0095-Add-efi-export-env-and-efi-load-env-commands.patch
Patch0096:        0096-Export-all-variables-from-the-initial-context-when-c.patch
Patch0097:        0097-grub.d-Split-out-boot-success-reset-from-menu-auto-h.patch
Patch0098:        0098-Don-t-assume-that-boot-commands-will-only-return-on-.patch
Patch0099:        0099-grub-set-bootflag-Update-comment-about-running-as-ro.patch
Patch0100:        0100-grub-set-bootflag-Write-new-env-to-tmpfile-and-then-.patch
Patch0101:        0101-grub.d-Fix-boot_indeterminate-getting-set-on-boot_su.patch
Patch0102:        0102-Add-start-symbol-for-RISC-V.patch
Patch0103:        0103-bootstrap.conf-Force-autogen.sh-to-use-python3.patch
Patch0104:        0104-efi-http-Export-fw-http-_path-variables-to-make-them.patch
Patch0105:        0105-efi-http-Enclose-literal-IPv6-addresses-in-square-br.patch
Patch0106:        0106-efi-net-Allow-to-specify-a-port-number-in-addresses.patch
Patch0107:        0107-efi-ip4_config-Improve-check-to-detect-literal-IPv6-.patch
Patch0108:        0108-efi-net-Print-a-debug-message-if-parsing-the-address.patch
Patch0109:        0109-kern-term-Also-accept-F8-as-a-user-interrupt-key.patch
Patch0110:        0110-http-Prepend-prefix-when-the-HTTP-path-is-relative-a.patch
Patch0111:        0111-Fix-a-missing-return-in-efi-export-env-and-efi-load-.patch
Patch0112:        0112-efi-dhcp-fix-some-allocation-error-checking.patch
Patch0113:        0113-efi-http-fix-some-allocation-error-checking.patch
Patch0114:        0114-efi-ip-46-_config.c-fix-some-potential-allocation-ov.patch
Patch0115:        0115-Fix-const-char-pointers-in-grub-core-net-efi-ip4_con.patch
Patch0116:        0116-Fix-const-char-pointers-in-grub-core-net-efi-ip6_con.patch
Patch0117:        0117-Fix-const-char-pointers-in-grub-core-net-efi-net.c.patch
Patch0118:        0118-Fix-const-char-pointers-in-grub-core-net-efi-pxe.c.patch
Patch0119:        0119-Add-systemd-integration-scripts-to-make-systemctl-re.patch
Patch0120:        0120-systemd-integration.sh-Also-set-old-menu_show_once-g.patch
Patch0121:        0121-at_keyboard-use-set-1-when-keyboard-is-in-Translate-.patch
Patch0122:        0122-grub-install-disable-support-for-EFI-platforms.patch
Patch0123:        0123-New-with-debug-timestamps-configure-flag-to-prepend-.patch
Patch0124:        0124-Added-debug-statements-to-grub_disk_open-and-grub_di.patch
Patch0125:        0125-Introduce-function-grub_debug_is_enabled-void-return.patch
Patch0126:        0126-Don-t-clear-screen-when-debugging-is-enabled.patch
Patch0127:        0127-grub_file_-instrumentation-new-file-debug-tag.patch
Patch0128:        0128-ieee1275-Avoiding-many-unecessary-open-close.patch
Patch0129:        0129-ieee1275-powerpc-implements-fibre-channel-discovery-.patch
Patch0130:        0130-ieee1275-powerpc-enables-device-mapper-discovery.patch
Patch0131:        0131-Add-at_keyboard_fallback_set-var-to-force-the-set-ma.patch
Patch0132:        0132-Add-suport-for-signing-grub-with-an-appended-signatu.patch
Patch0133:        0133-docs-grub-Document-signing-grub-under-UEFI.patch
Patch0134:        0134-docs-grub-Document-signing-grub-with-an-appended-sig.patch
Patch0135:        0135-dl-provide-a-fake-grub_dl_set_persistent-for-the-emu.patch
Patch0136:        0136-pgp-factor-out-rsa_pad.patch
Patch0137:        0137-crypto-move-storage-for-grub_crypto_pk_-to-crypto.c.patch
Patch0138:        0138-posix_wrap-tweaks-in-preparation-for-libtasn1.patch
Patch0139:        0139-libtasn1-import-libtasn1-4.16.0.patch
Patch0140:        0140-libtasn1-disable-code-not-needed-in-grub.patch
Patch0141:        0141-libtasn1-changes-for-grub-compatibility.patch
Patch0142:        0142-libtasn1-compile-into-asn1-module.patch
Patch0143:        0143-test_asn1-test-module-for-libtasn1.patch
Patch0144:        0144-grub-install-support-embedding-x509-certificates.patch
Patch0145:        0145-appended-signatures-import-GNUTLS-s-ASN.1-descriptio.patch
Patch0146:        0146-appended-signatures-parse-PKCS-7-signedData-and-X.50.patch
Patch0147:        0147-appended-signatures-support-verifying-appended-signa.patch
Patch0148:        0148-appended-signatures-verification-tests.patch
Patch0149:        0149-appended-signatures-documentation.patch
Patch0150:        0150-ieee1275-enter-lockdown-based-on-ibm-secure-boot.patch
Patch0151:        0151-ieee1275-drop-HEAP_MAX_ADDR-HEAP_MIN_SIZE.patch
Patch0152:        0152-appendedsig-x509-Also-handle-the-Extended-Key-Usage-.patch
Patch0153:        0153-ieee1275-ofdisk-retry-on-open-failure.patch
Patch0154:        0154-efinet-Add-DHCP-proxy-support.patch
Patch0155:        0155-Don-t-update-the-cmdline-when-generating-legacy-menu.patch
Patch0156:        0156-Suppress-gettext-error-message.patch
Patch0157:        0157-grub-set-password-Always-use-boot-grub2-user.cfg-as-.patch
Patch0158:        0158-normal-main-Discover-the-device-to-read-the-config-f.patch
Patch0159:        0159-powerpc-adjust-setting-of-prefix-for-signed-binary-c.patch
Patch0160:        0160-powerpc-ieee1275-load-grub-at-4MB-not-2MB.patch
Patch0161:        0161-Add-Fedora-location-of-DejaVu-SANS-font.patch
Patch0162:        0162-efi-new-connectefi-command.patch
Patch0163:        0163-powerpc-prefix-detection-support-device-names-with-c.patch
Patch0164:        0164-make-ofdisk_retries-optional.patch
Patch0165:        0165-misc-Make-grub_min-and-grub_max-more-resilient.patch
Patch0166:        0166-ReiserFS-switch-to-using-grub_min-grub_max.patch
Patch0167:        0167-misc-make-grub_boot_time-also-call-grub_dprintf-boot.patch
Patch0168:        0168-modules-make-.module_license-read-only.patch
Patch0169:        0169-modules-strip-.llvm_addrsig-sections-and-similar.patch
Patch0170:        0170-modules-Don-t-allocate-space-for-non-allocable-secti.patch
Patch0171:        0171-modules-load-module-sections-at-page-aligned-address.patch
Patch0172:        0172-nx-add-memory-attribute-get-set-API.patch
Patch0173:        0173-nx-set-page-permissions-for-loaded-modules.patch
Patch0174:        0174-nx-set-the-nx-compatible-flag-in-EFI-grub-images.patch
Patch0175:        0175-grub_fs_probe-dprint-errors-from-filesystems.patch
Patch0176:        0176-Make-debug-file-show-which-file-filters-get-run.patch
Patch0177:        0177-BLS-create-etc-kernel-cmdline-during-mkconfig.patch
Patch0178:        0178-squish-don-t-dup-rhgb-quiet-check-mtimes.patch
Patch0179:        0179-squish-give-up-on-rhgb-quiet.patch
Patch0180:        0180-squish-BLS-only-write-etc-kernel-cmdline-if-writable.patch
Patch0181:        0181-blscfg-Don-t-root-device-in-emu-builds.patch
Patch0182:        0182-ppc64le-signed-boot-media-changes.patch
Patch0183:        0183-core-Fix-several-implicit-function-declarations.patch
Patch0184:        0184-ieee1275-request-memory-with-ibm-client-architecture.patch
Patch0185:        0185-hostdisk-work-around-proc-not-reporting-size.patch
Patch0186:        0186-blscfg-check-for-mounted-boot-in-emu.patch
Patch0187:        0187-grub_dl_set_mem_attrs-fix-format-string.patch
Patch0188:        0188-grub_dl_set_mem_attrs-add-self-check-for-the-tramp-G.patch
Patch0189:        0189-grub_dl_load_segments-page-align-the-tramp-GOT-areas.patch
Patch0190:        0190-emu-Add-switch-root-to-grub-emu.patch
Patch0191:        0191-util-Enable-default-kernel-for-updates.patch
Patch0192:        0192-efi-http-change-uint32_t-to-uintn_t.patch
Patch0193:        0193-Add-Install-section-to-aux-systemd-units.patch
Patch0194:        0194-Fix-missing-include-in-ofdisk.c.patch
Patch0195:        0195-add-flag-to-only-search-root-dev.patch
Patch0196:        0196-cryptdisk-fix-incorrect-sign-comparison.patch
Patch0197:        0197-grub-install-fix-a-sign-comparison-error.patch
Patch0198:        0198-grub-mount-work-around-bad-integer-comparison.patch
Patch0199:        0199-power-Fix-use-after-free-in-get_slave_from_dm.patch
Patch0200:        0200-Fix-some-sign-comparison-errors.patch
Patch0201:        0201-normal-Fix-a-discarded-const.patch
Patch0202:        0202-at_keyboard-mark-grub_keyboard_controller_write-unus.patch
Patch0203:        0203-Fix-another-minor-sign-comparison-error.patch
Patch0204:        0204-Track-explicit-module-dependencies-in-Makefile.core..patch
Patch0205:        0205-Revert-mm-Assert-that-we-preserve-header-vs-region-a.patch
Patch0206:        0206-make-use-the-_CPU-variety-of-build-flags-for-PROGRAM.patch
Patch0207:        0207-Work-around-extra_deps.lst-issue.patch
Patch0208:        0208-include-proper-attribute-for-an-EFI-API-call-definit.patch
Patch0209:        0209-cast-grub_error-status-parameter.patch
Patch0210:        0210-remove-unused-varible.patch
Patch0211:        0211-cast-grub_net_bootp_packet-pointer.patch
Patch0212:        0212-libtasn1-fix-string-overflow-warning.patch
Patch0213:        0213-Add-support-for-Linux-EFI-stub-loading.patch
Patch0214:        0214-fix-i386_pc-on-legacycfg-module.patch
Patch0215:        0215-Add-secureboot-support-on-efi-chainloader.patch
Patch0216:        0216-Make-any-of-the-loaders-that-link-in-efi-mode-honor-.patch
Patch0217:        0217-Minimize-the-sort-ordering-for-.debug-and-rescue-ker.patch
Patch0218:        0218-Add-grub_qdprintf-grub_dprintf-without-the-file-line.patch
Patch0219:        0219-Make-a-gdb-dprintf-that-tells-us-load-addresses.patch
Patch0220:        0220-Handle-multi-arch-64-on-32-boot-in-linuxefi-loader.patch
Patch0221:        0221-Try-to-pick-better-locations-for-kernel-and-initrd.patch
Patch0222:        0222-x86-efi-Use-bounce-buffers-for-reading-to-addresses-.patch
Patch0223:        0223-x86-efi-Re-arrange-grub_cmd_linux-a-little-bit.patch
Patch0224:        0224-x86-efi-Make-our-own-allocator-for-kernel-stuff.patch
Patch0225:        0225-x86-efi-Allow-initrd-params-cmdline-allocations-abov.patch
Patch0226:        0226-efi-Set-image-base-address-before-jumping-to-the-PE-.patch
Patch0227:        0227-x86-efi-Reduce-maximum-bounce-buffer-size-to-16-MiB.patch
Patch0228:        0228-efilinux-Fix-integer-overflows-in-grub_cmd_initrd.patch
Patch0229:        0229-linuxefi-fail-kernel-validation-without-shim-protoco.patch
Patch0230:        0230-Allow-chainloading-EFI-apps-from-loop-mounts.patch
Patch0231:        0231-grub-core-loader-i386-efi-linux.c-do-not-validate-ke.patch
Patch0232:        0232-grub-core-loader-efi-chainloader.c-do-not-validate-c.patch
Patch0233:        0233-grub-core-loader-efi-linux.c-drop-now-unused-grub_li.patch
Patch0234:        0234-loader-efi-chainloader-grub_load_and_start_image-doe.patch
Patch0235:        0235-loader-efi-chainloader-simplify-the-loader-state.patch
Patch0236:        0236-loader-efi-chainloader-Use-grub_loader_set_ex.patch
Patch0237:        0237-loader-i386-efi-linux-Avoid-a-use-after-free-in-the-.patch
Patch0238:        0238-loader-i386-efi-linux-Use-grub_loader_set_ex.patch
Patch0239:        0239-loader-i386-efi-linux-Fix-a-memory-leak-in-the-initr.patch
Patch0240:        0240-EFI-allocate-kernel-in-EFI_RUNTIME_SERVICES_CODE-ins.patch
Patch0241:        0241-efi-use-enumerated-array-positions-for-our-allocatio.patch
Patch0242:        0242-efi-split-allocation-policy-for-kernel-vs-initrd-mem.patch
Patch0243:        0243-efi-allocate-the-initrd-within-the-bounds-expressed-.patch
Patch0244:        0244-efi-use-EFI_LOADER_-CODE-DATA-for-kernel-and-initrd-.patch
Patch0245:        0245-x86-efi-Fix-an-incorrect-array-size-in-kernel-alloca.patch
Patch0246:        0246-grub-install-on-EFI-if-forced.patch
Patch0247:        0247-Remove-Install-section-from-aux-systemd-units.patch
Patch0248:        0248-chainloader-remove-device-path-debug-message.patch
Patch0249:        0249-grub-set-bootflag-Conservative-partial-fix-for-CVE-2.patch
Patch0250:        0250-grub-set-bootflag-More-complete-fix-for-CVE-2024-104.patch
Patch0251:        0251-grub-set-bootflag-Exit-calmly-when-not-running-as-ro.patch
Patch0252:        0252-Makefile.core.def-fix-linux-module.patch
Patch0253:        0253-Add-support-for-Linux-EFI-stub-loading-on-arm-archit.patch
Patch0254:        0254-arm-arm64-loader-Better-memory-allocation-and-error-.patch
Patch0255:        0255-arm64-Fix-EFI-loader-kernel-image-allocation.patch
Patch0256:        0256-pe-add-the-DOS-header-struct-and-fix-some-bad-naming.patch
Patch0257:        0257-Correct-BSS-zeroing-on-aarch64.patch
Patch0258:        0258-arm64-Use-proper-memory-type-for-kernel-allocation.patch
Patch0259:        0259-normal-Remove-grub_env_set-prefix-in-grub_try_normal.patch
Patch0260:        0260-fs-xfs-Handle-non-continuous-data-blocks-in-director.patch
Patch0261:        0261-Ignore-warnings-for-incompatible-types.patch
Patch0262:        0262-cmd-search-Rework-of-CVE-2023-4001-fix.patch
Patch0263:        0263-loader-efi-linux.c-read-the-kernel-image-before-head.patch
Patch0264:        0264-nx-set-attrs-in-our-kernel-loaders.patch
Patch0265:        0265-efi-Provide-wrappers-for-load_image-start_image.patch
Patch0266:        0266-efi-Disallow-fallback-to-legacy-Linux-loader-when-sh.patch
Patch0267:        0267-Set-non-executable-stack-sections-on-EFI-assembly-fi.patch
Patch0268:        0268-grub-mkconfig.in-turn-off-executable-owner-bit.patch
Patch0269:        0269-kern-ieee1275-init-Add-IEEE-1275-Radix-support-for-K.patch
Patch0270:        0270-grub2-mkconfig-Ensure-grub-cfg-stub-is-not-overwritt.patch
Patch0271:        0271-grub2-mkconfig-Simplify-os_name-detection.patch
Patch0272:        0272-grub-mkconfig-Remove-check-for-mount-point-for-grub-.patch
Patch0273:        0273-efi-api.h-include-missing-__grub_efi_api-macros-on-E.patch
Patch0274:        0274-grub-core-net-arp.c-fix-variable-name.patch
Patch0275:        0275-load-EFI-commands-inside-test-expressions.patch
Patch0276:        0276-efi-loader-Check-if-NX-is-required-in-grub_efi_linux.patch
Patch0277:        0277-Stop-grub.efi-from-always-printing-dynamic_load_symb.patch
Patch0278:        0278-acpi-Fix-out-of-bounds-access-in-grub_acpi_xsdt_find.patch
Patch0279:        0279-cmd-search-Fix-a-possible-NULL-ptr-dereference.patch
Patch0280:        0280-Enable-building-blscfg-module-on-xen-and-xen_pvh.patch
Patch0281:        0281-loader-efi-Fix-RISC-V-build.patch
Patch0282:        0282-kern-riscv-efi-init-Use-time-register-in-grub_efi_ge.patch
Patch0283:        0283-Use-medany-instead-of-large-model-for-RISCV.patch
Patch0284:        0284-fs-xfs-Fix-large-extent-counters-incompat-feature-su.patch
Patch0285:        0285-term-nns8250-spcr-return-if-redirection-is-disabled.patch
Patch0286:        0286-commands-legacycfg-Avoid-closing-file-twice.patch
Patch0287:        0287-disk-ahci.c-remove-conditional-operator-for-endtime.patch
Patch0288:        0288-commands-bli-Fix-crash-in-get_part_uuid.patch
Patch0289:        0289-misc-Implement-grub_strlcpy.patch
Patch0290:        0290-fs-ufs-Fix-a-heap-OOB-write.patch
Patch0291:        0291-fs-hfs-Fix-stack-OOB-write-with-grub_strcpy.patch
Patch0292:        0292-fs-tar-Initialize-name-in-grub_cpio_find_file.patch
Patch0293:        0293-fs-tar-Integer-overflow-leads-to-heap-OOB-write.patch
Patch0294:        0294-fs-f2fs-Set-a-grub_errno-if-mount-fails.patch
Patch0295:        0295-fs-hfsplus-Set-a-grub_errno-if-mount-fails.patch
Patch0296:        0296-fs-iso9660-Set-a-grub_errno-if-mount-fails.patch
Patch0297:        0297-fs-iso9660-Fix-invalid-free.patch
Patch0298:        0298-fs-jfs-Fix-OOB-read-in-jfs_getent.patch
Patch0299:        0299-fs-jfs-Fix-OOB-read-caused-by-invalid-dir-slot-index.patch
Patch0300:        0300-fs-jfs-Use-full-40-bits-offset-and-address-for-a-dat.patch
Patch0301:        0301-fs-jfs-Inconsistent-signed-unsigned-types-usage-in-r.patch
Patch0302:        0302-fs-ext2-Fix-out-of-bounds-read-for-inline-extents.patch
Patch0303:        0303-fs-ntfs-Fix-out-of-bounds-read.patch
Patch0304:        0304-fs-ntfs-Track-the-end-of-the-MFT-attribute-buffer.patch
Patch0305:        0305-fs-ntfs-Use-a-helper-function-to-access-attributes.patch
Patch0307:        0307-fs-xfs-Fix-out-of-bounds-read.patch
Patch0308:        0308-fs-xfs-Ensuring-failing-to-mount-sets-a-grub_errno.patch
Patch0309:        0309-kern-file-Ensure-file-data-is-set.patch
Patch0310:        0310-kern-file-Implement-filesystem-reference-counting.patch
Patch0311:        0311-cli_lock-Add-build-option-to-block-command-line-inte.patch
Patch0312:        0312-disk-cryptodisk-Require-authentication-after-TPM-unl.patch
Patch0313:        0313-disk-loopback-Reference-tracking-for-the-loopback.patch
Patch0314:        0314-kern-disk-Limit-recursion-depth.patch
Patch0315:        0315-kern-partition-Limit-recursion-in-part_iterate.patch
Patch0316:        0316-script-execute-Limit-the-recursion-depth.patch
Patch0317:        0317-net-Unregister-net_default_ip-and-net_default_mac-va.patch
Patch0318:        0318-net-Remove-variables-hooks-when-interface-is-unregis.patch
Patch0319:        0319-net-Fix-OOB-write-in-grub_net_search_config_file.patch
Patch0320:        0320-net-tftp-Fix-stack-buffer-overflow-in-tftp_open.patch
Patch0321:        0321-video-readers-jpeg-Do-not-permit-duplicate-SOF0-mark.patch
Patch0322:        0322-kern-dl-Fix-for-an-integer-overflow-in-grub_dl_ref.patch
Patch0323:        0323-kern-dl-Check-for-the-SHF_INFO_LINK-flag-in-grub_dl_.patch
Patch0324:        0324-commands-extcmd-Missing-check-for-failed-allocation.patch
Patch0325:        0325-commands-ls-Fix-NULL-dereference.patch
Patch0326:        0326-commands-pgp-Unregister-the-check_signatures-hooks-o.patch
Patch0327:        0327-normal-Remove-variables-hooks-on-module-unload.patch
Patch0328:        0328-gettext-Remove-variables-hooks-on-module-unload.patch
Patch0329:        0329-gettext-Integer-overflow-leads-to-heap-OOB-write-or-.patch
Patch0330:        0330-gettext-Integer-overflow-leads-to-heap-OOB-write.patch
Patch0331:        0331-commands-read-Fix-an-integer-overflow-when-supplying.patch
Patch0332:        0332-commands-test-Stack-overflow-due-to-unlimited-recurs.patch
Patch0333:        0333-commands-minicmd-Block-the-dump-command-in-lockdown-.patch
Patch0334:        0334-commands-memrw-Disable-memory-reading-in-lockdown-mo.patch
Patch0335:        0335-commands-hexdump-Disable-memory-reading-in-lockdown-.patch
Patch0336:        0336-fs-bfs-Disable-under-lockdown.patch
Patch0337:        0337-fs-Disable-many-filesystems-under-lockdown.patch
Patch0338:        0338-disk-Use-safe-math-macros-to-prevent-overflows.patch
Patch0339:        0339-disk-Prevent-overflows-when-allocating-memory-for-ar.patch
Patch0340:        0340-disk-Check-if-returned-pointer-for-allocated-memory-.patch
Patch0341:        0341-disk-ieee1275-ofdisk-Call-grub_ieee1275_close-when-g.patch
Patch0342:        0342-fs-Use-safe-math-macros-to-prevent-overflows.patch
Patch0343:        0343-fs-Prevent-overflows-when-allocating-memory-for-arra.patch
Patch0344:        0344-fs-Prevent-overflows-when-assigning-returned-values-.patch
Patch0345:        0345-fs-zfs-Use-safe-math-macros-to-prevent-overflows.patch
Patch0346:        0346-fs-zfs-Prevent-overflows-when-allocating-memory-for-.patch
Patch0347:        0347-fs-zfs-Check-if-returned-pointer-for-allocated-memor.patch
Patch0348:        0348-fs-zfs-Add-missing-NULL-check-after-grub_strdup-call.patch
Patch0349:        0349-net-Use-safe-math-macros-to-prevent-overflows.patch
Patch0350:        0350-net-Prevent-overflows-when-allocating-memory-for-arr.patch
Patch0351:        0351-net-Check-if-returned-pointer-for-allocated-memory-i.patch
Patch0352:        0352-fs-sfs-Check-if-allocated-memory-is-NULL.patch
Patch0353:        0353-script-execute-Fix-potential-underflow-and-NULL-dere.patch
Patch0354:        0354-osdep-unix-getroot-Fix-potential-underflow.patch
Patch0355:        0355-misc-Ensure-consistent-overflow-error-messages.patch
Patch0356:        0356-bus-usb-ehci-Define-GRUB_EHCI_TOGGLE-as-grub_uint32_.patch
Patch0357:        0357-normal-menu-Use-safe-math-to-avoid-an-integer-overfl.patch
Patch0358:        0358-kern-partition-Add-sanity-check-after-grub_strtoul-c.patch
Patch0359:        0359-kern-misc-Add-sanity-check-after-grub_strtoul-call.patch
Patch0360:        0360-loader-i386-linux-Cast-left-shift-to-grub_uint32_t.patch
Patch0361:        0361-loader-i386-bsd-Use-safe-math-to-avoid-underflow.patch
Patch0362:        0362-fs-ext2-Rework-out-of-bounds-read-for-inline-and-ext.patch
Patch0363:        0363-powerpc-increase-MIN-RMA-size-for-CAS-negotiation.patch
Patch0364:        0364-script-execute-Don-t-let-trailing-blank-lines-determ.patch
Patch0365:        0365-normal-menu-Check-return-code-of-the-script-when-exe.patch
Patch0366:        0366-ieee1275-ofnet-Fix-grub_malloc-removed-after-added-s.patch
Patch0367:        0367-grub-mkimage-Create-new-ELF-note-for-SBAT.patch
Patch0368:        0368-grub-mkimage-Add-SBAT-metadata-into-ELF-note-for-Pow.patch
Patch0369:        0369-10_linux.in-escape-kernel-option-characters-properly.patch
Patch0370:        0370-blscfg-check-if-variable-is-escaped-before-consideri.patch
Patch0371:        0371-kern-rescue_reader-Block-the-rescue-mode-until-the-C.patch
Patch0372:        0372-commands-search-Introduce-the-cryptodisk-only-argume.patch
Patch0373:        0373-disk-diskfilter-Introduce-the-cryptocheck-command.patch
Patch0374:        0374-commands-search-Add-the-diskfilter-support.patch
Patch0375:        0375-docs-Document-available-crypto-disks-checks.patch
Patch0376:        0376-disk-cryptodisk-Add-the-erase-secrets-function.patch
Patch0377:        0377-disk-cryptodisk-Wipe-the-passphrase-from-memory.patch
Patch0378:        0378-cryptocheck-Add-quiet-option.patch
Patch0379:        0379-loader-efi-chainloader-Fix-double-free.patch
Patch0380:        0380-loader-efi-chainloader-Fix-null-pointer-dereference.patch
Patch0381:        0381-osdep-linux-getroot-Detect-DDF-container-similar-to-.patch
Patch0382:        0382-Set-correctly-the-memory-attributes-for-the-kernel-P.patch
Patch0383:        0383-Include-function-name-on-debug-print-function.patch
Patch0384:        0384-kern-misc-Implement-grub_strtok.patch
Patch0385:        0385-blsuki-Add-blscfg-command-to-parse-Boot-Loader-Speci.patch
Patch0386:        0386-util-misc.c-Change-offset-type-for-grub_util_write_i.patch
Patch0387:        0387-blsuki-Check-for-mounted-boot-in-emu.patch
Patch0388:        0388-blsuki-Add-uki-command-to-load-Unified-Kernel-Image-.patch
Patch0389:        0389-posix_wrap-Tweaks-in-preparation-for-libtasn1.patch
Patch0390:        0390-blsuki-do-not-register-blscfg-command.patch
Patch0391:        0391-misc-add-z-length-modifier-support.patch
Patch0392:        0392-tests-add-z-modifier-printf-tests.patch
Patch0393:        0393-util-grub-editenv-add-fs_envblk-open-helper.patch
Patch0394:        0394-util-grub-editenv-add-fs_envblk-write-helper.patch
Patch0395:        0395-util-grub-editenv-wire-set_variables-to-optional-fs_.patch
Patch0396:        0396-util-grub-editenv-wire-unset_variables-to-optional-f.patch
Patch0397:        0397-util-grub-editenv-wire-list_variables-to-optional-fs.patch
Patch0398:        0398-util-grub-editenv-add-probe-call-for-external-envblk.patch
Patch0399:        0399-btrfs-add-environment-block-to-reserved-header-area.patch
Patch0400:        0400-00_header.in-wire-grub.cfg-to-use-env_block-when-pre.patch
Patch0401:        0401-btrfs-update-doc-link-for-bootloader-support.patch
Patch0402:        0402-docs-add-Btrfs-env-block-and-special-env-vars.patch
Patch0403:        0403-kern-fs-Honour-file-read_hook-in-grub_fs_blocklist_r.patch
Patch0404:        0404-util-grub.d-00_header.in-Prefer-dev-instead-of-root-.patch
Patch0405:        0405-grub.d-Support-the-external-environment-block-for-au.patch
Patch0406:        0406-grub-editenv-Make-automatic-hidden-menu-and-boot-cou.patch
Patch0407:        0407-ieee1275-ofnet-Fix-hw_addr-variable-initialization.patch
Patch0408:        0408-fs-xfs-Add-new-superblock-features-added-in-Linux-6..patch
Patch0409:        0409-Revert-loader-efi-Fix-RISC-V-build.patch
Patch0410:        0410-Revert-efi-Disallow-fallback-to-legacy-Linux-loader-.patch
Patch0411:        0411-Partial-revert-nx-set-attrs-in-our-kernel-loaders.patch
Patch0412:        0412-Revert-loader-efi-linux.c-read-the-kernel-image-befo.patch
Patch0413:        0413-Revert-arm64-Use-proper-memory-type-for-kernel-alloc.patch
Patch0414:        0414-Revert-Correct-BSS-zeroing-on-aarch64.patch
Patch0415:        0415-Revert-arm64-Fix-EFI-loader-kernel-image-allocation.patch
Patch0416:        0416-Revert-Add-support-for-Linux-EFI-stub-loading-on-arm.patch
Patch0417:        0417-loader-efi-linux.c-Free-mempath-after-use.patch
Patch0418:        0418-loader-efi-linux.c-Unload-image-on-errors.patch
Patch0419:        0419-loader-efi-linux.c-Disable-code-not-used-on-x86-when.patch
Patch0420:        0420-commands-test-Fix-error-in-recursion-depth-calculati.patch
Patch0421:        0421-kern-file-Call-grub_dl_unref-after-fs-fs_close.patch
Patch0422:        0422-net-net-Unregister-net_set_vlan-command-on-unload.patch
Patch0423:        0423-gettext-gettext-Unregister-gettext-command-on-module.patch
Patch0424:        0424-normal-main-Unregister-commands-on-module-unload.patch
Patch0425:        0425-tests-lib-functional_test-Unregister-commands-on-mod.patch
Patch0426:        0426-commands-usbtest-Use-correct-string-length-field.patch
Patch0427:        0427-commands-usbtest-Ensure-string-length-is-sufficient-.patch
Patch0428:        0428-verifiers-Allocate-EFI-pages-instead-of-grub_malloc-.patch


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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%do_common_setup
%if 0%{with_efi_arch}
mkdir grub-%{grubefiarch}-%{tarversion}
grep -A100000 '# stuff "make" creates' .gitignore > grub-%{grubefiarch}-%{tarversion}/.gitignore
cp %{SOURCE3} grub-%{grubefiarch}-%{tarversion}/unifont.pcf.gz
sed -e "s,@@VERSION@@,%{version},g" -e "s,@@VERSION_RELEASE@@,%{version}-%{release},g" \
    %{SOURCE9} > grub-%{grubefiarch}-%{tarversion}/sbat.csv
git add grub-%{grubefiarch}-%{tarversion}
%endif
%if 0%{with_alt_efi_arch}
mkdir grub-%{grubaltefiarch}-%{tarversion}
grep -A100000 '# stuff "make" creates' .gitignore > grub-%{grubaltefiarch}-%{tarversion}/.gitignore
cp %{SOURCE3} grub-%{grubaltefiarch}-%{tarversion}/unifont.pcf.gz
git add grub-%{grubaltefiarch}-%{tarversion}
%endif
%if 0%{with_legacy_arch}
mkdir grub-%{grublegacyarch}-%{tarversion}
grep -A100000 '# stuff "make" creates' .gitignore > grub-%{grublegacyarch}-%{tarversion}/.gitignore
cp %{SOURCE3} grub-%{grublegacyarch}-%{tarversion}/unifont.pcf.gz
git add grub-%{grublegacyarch}-%{tarversion}
%endif
%if 0%{with_emu_arch}
mkdir grub-emu-%{tarversion}
grep -A100000 '# stuff "make" creates' .gitignore > grub-emu-%{tarversion}/.gitignore
cp %{SOURCE3} grub-emu-%{tarversion}/unifont.pcf.gz
git add grub-emu-%{tarversion}
%endif
%if 0%{with_xen_arch}
mkdir grub-%{grubxenarch}-%{tarversion}
grep -A100000 '# stuff "make" creates' .gitignore > grub-%{grubxenarch}-%{tarversion}/.gitignore
cp %{SOURCE3} grub-%{grubxenarch}-%{tarversion}/unifont.pcf.gz
sed -e "s,@@VERSION@@,%{version},g" -e "s,@@VERSION_RELEASE@@,%{version}-%{release},g" \
    %{SOURCE9} > grub-%{grubxenarch}-%{tarversion}/sbat.csv
git add grub-%{grubxenarch}-%{tarversion}
%endif
%if 0%{with_xen_pvh_arch}
mkdir grub-%{grubxenpvharch}-%{tarversion}
grep -A100000 '# stuff "make" creates' .gitignore > grub-%{grubxenpvharch}-%{tarversion}/.gitignore
cp %{SOURCE3} grub-%{grubxenpvharch}-%{tarversion}/unifont.pcf.gz
sed -e "s,@@VERSION@@,%{version},g" -e "s,@@VERSION_RELEASE@@,%{version}-%{release},g" \
    %{SOURCE9} > grub-%{grubxenpvharch}-%{tarversion}/sbat.csv
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
install -D -m 0755 -t %{buildroot}%{_prefix}/lib/kernel/install.d/ %{SOURCE8}
install -D -m 0755 -t %{buildroot}%{_prefix}/lib/kernel/install.d/ %{SOURCE11}
install -D -m 0755 -t %{buildroot}%{_prefix}/lib/kernel/install.d/ %{SOURCE2}
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
* Fri Apr 03 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.12-56
- Gnulib Source1 GitHub mirror with #/ rename, drop theme.tar.bz2, renumber SourceN
- Inline grub.macros and grub.patches for spectool parse without extra SOURCES

* Sat Mar 21 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.12-56
- SBAT grub.oreon macros oreon-grub2-signer git ids ppc64le %%{?oreon}

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.12-55
- Prepare for Oreon 11 (RP1)
