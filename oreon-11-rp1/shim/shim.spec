%global source0_hash none

# this is to make us only expand %%{dist} if we're on a modularity build.
# it's 2 macros make vim's \c not put a brace at the end of the changelog.
%global _dist %{expand:%{?_module_build:%%{?dist}}}
%global dist %{expand:%%{_dist}}

Name:		shim
Version:	16.1
Release:	8%{?dist}
Summary:	First-stage UEFI bootloader
License:	BSD-3-Clause
URL:		https://github.com/rhboot/shim/
BuildRequires:	efi-filesystem
BuildRequires:	efi-srpm-macros >= 5-1

ExclusiveArch:	%{efi}
# but we don't build a .i686 package, just a shim-ia32.x86_64 package
ExcludeArch:	%{ix86}
# but we don't build a .arm package, just a shim-arm.aarch64 package
ExcludeArch:	%{arm}

Source1:        shim.conf

# keep these two lists of sources synched up arch-wise.  That is 0 and 10
# match, 1 and 11 match, ...
Source10:        BOOTAA64.CSV
Source20:        shimaa64.efi
Source11:        BOOTIA32.CSV
Source21:        shimia32.efi
Source12:        BOOTX64.CSV
Source22:        shimx64.efi
#Source13:	BOOTARM.CSV
#Source23:	shimarm.efi

%global _libdir %{_exec_prefix}/lib

%global vr %{version}-%{release}
%global os_id %(eval echo $(grep ^ID= /etc/os-release | sed -e 's/^ID=//' -e 's/rhel/redhat/'))
%global shim_vr_dir  %{_libdir}/efi/shim/%{vr}
%global shim_efi_dir  %{shim_vr_dir}/EFI/%{os_id}
%global shim_boot_dir %{shim_vr_dir}/EFI/BOOT

%global debug_package %{nil}
%global __brp_mangle_shebangs_exclude_from_file %{expand:%{_builddir}/shim-%{efi_arch}-%{version}-%{release}.%{_target_cpu}-shebangs.txt}
%global vendor_token_str %{expand:%%{nil}%%{?vendor_token_name:-t "%{vendor_token_name}"}}
%global vendor_cert_str %{expand:%%{!?vendor_cert_nickname:-c "Red Hat Test Certificate"}%%{?vendor_cert_nickname:-c "%%{vendor_cert_nickname}"}}

%global grub_version 2.06-63
%global fwupd_version 1.5.8

%define __pesign_client_cert grub2-signer

%global bootcsvaa64 %{expand:%{SOURCE10}}
%global bootcsvarm %{expand:%{SOURCE13}}
%global bootcsvia32 %{expand:%{SOURCE11}}
%global bootcsvx64 %{expand:%{SOURCE12}}

%global shimefiaa64 %{expand:%{SOURCE20}}
%global shimefiarm %{expand:%{SOURCE23}}
%global shimefiia32 %{expand:%{SOURCE21}}
%global shimefix64 %{expand:%{SOURCE22}}

%global shimveraa64 16.1-1
%global shimverarm 15.4-1.fc34
%global shimveria32 16.1-1
%global shimverx64 16.1-1

%global shimdiraa64 %{_datadir}/shim/%{shimveraa64}/aa64
%global shimdirarm %{_datadir}/shim/%{shimverarm}/arm
%global shimdiria32 %{_datadir}/shim/%{shimveria32}/ia32
%global shimdirx64 %{_datadir}/shim/%{shimverx64}/x64

%global unsignedaa64 shim-unsigned-aarch64
%global unsignedarm shim-unsigned-arm
%global unsignedia32 shim-unsigned-ia32
%global unsignedx64 shim-unsigned-x64

%global bootcsv %{expand:%{bootcsv%{efi_arch}}}
%global bootcsvalt %{expand:%{bootcsv%{?efi_alt_arch}}}
%global shimefi %{expand:%{shimefi%{efi_arch}}}
%global shimefialt %{expand:%{shimefi%{?efi_alt_arch}}}
%global shimver %{expand:%{shimver%{efi_arch}}}
%global shimveralt %{expand:%{shimver%{?efi_alt_arch}}}
%global shimdir %{expand:%{shimdir%{efi_arch}}}
%global shimdiralt %{expand:%{shimdir%{?efi_alt_arch}}}

%global unsignednone shim-unsigned-none
%global unsigned %{expand:%%{unsigned%{efi_arch}}}
%global unsignedalt %{expand:%%{unsigned%{efi_alt_arch}}}

%define define_pkg(a:p:)						\
%{expand:%%package -n shim-%{-a*}}					\
Summary: First-stage UEFI bootloader					\
Requires: mokutil >= 1:0.3.0-15						\
Requires: efi-filesystem						\
Provides: shim-signed-%{-a*} = %{version}-%{release}			\
Conflicts: fwupd < %{fwupd_version}					\
Requires: grub2-efi-%{-a*} >= %{grub_version}				\
Conflicts: grub2-efi-%{-a*} < %{grub_version}				\
%{expand:%%if 0%%{-p*}							\
Provides: shim = %{version}-%{release}					\
Provides: shim-signed = %{version}-%{release}				\
Obsoletes: shim-signed < %{version}-%{release}				\
Obsoletes: shim < %{version}-%{release}					\
%%endif}								\
# Shim uses OpenSSL, but cannot use the system copy as the UEFI ABI	\
# is not compatible with SysV (there's no red zone under UEFI) and	\
# there isn't a POSIX-style C library.					\
# BuildRequires: OpenSSL						\
Provides: bundled(openssl) = 1.0.2j					\
									\
%{expand:%%description -n shim-%{-a*}}					\
Initial UEFI bootloader that handles chaining to a trusted full		\
bootloader under secure boot environments. This package contains the	\
version signed by the UEFI signing service.				\
%{nil}

# -a <efiarch>
# -i <input>
%define hash(a:i:d:)							\
	pesign -i %{-i*} -h -P > shim.hash				\
	read hash0 file0 < shim.hash					\
	read hash1 file1 < %{-d*}/shim%{-a*}.hash			\
	if ! [ "$hash0" = "$hash1" ]; then				\
		echo Invalid signature\! > /dev/stderr			\
		echo $hash0 vs $hash1					\
		exit 1							\
	fi								\
	%{nil}

# -i <input>
# -o <output>
%define sign(i:o:)							\
	%{expand:%%pesign -s -i %{-i*} -o %{-o*}}			\
	%{nil}

# -b <binary prefix>
# -a <efiarch>
# -i <input>
%define distrosign(b:a:d:)						\
	cp -av %{-d*}/%{-b*}%{-a*}.efi %{-b*}%{-a*}-unsigned.efi	\
	%{expand:%%sign -i %{-b*}%{-a*}-unsigned.efi -o %{-b*}%{-a*}-signed.efi}\
	%{nil}

# -a <efiarch>
# -A <EFIARCH>
# -b <1|0> # signed by this builder?
# -c <1|0> # signed by UEFI CA?
# -i <shimARCH.efi>
%define define_build(a:A:b:c:i:d:)					\
if [ "%{-c*}" = "yes" ]; then						\
	%{expand:%%hash -i %{-i*} -a %{-a*} -d %{-d*}}			\
fi									\
cp %{-i*} shim%{-a*}.efi						\
if [ "%{-b*}" = "yes" ]; then						\
	%{expand:%%distrosign -b shim -a %{-a*} -d %{-d*}}		\
	mv shim%{-a*}-signed.efi shim%{-a*}-%{efi_vendor}.efi		\
fi									\
if [ "%{-c*}" = "no" ] && [ "%{-b*}" = "yes" ]; then			\
	cp shim%{-a*}-%{efi_vendor}.efi shim%{-a*}.efi			\
fi									\
%{expand:%%distrosign -b mm -a %{-a*} -d %{-d*}}			\
mv mm%{-a*}-signed.efi mm%{-a*}.efi					\
%{expand:%%distrosign -b fb -a %{-a*} -d %{-d*}}			\
mv fb%{-a*}-signed.efi fb%{-a*}.efi					\
rm -vf									\\\
	mm%{-a*}-unsigned.efi						\\\
	fb%{-a*}-unsigned.efi						\\\
	shim%{-a*}-unsigned.efi						\
%{nil}

# -a <efiarch>
# -A <EFIARCH>
# -b <BOOTCSV>
%define do_install(a:A:b:)						\
install -m 0700 shim%{-a*}.efi						\\\
	$RPM_BUILD_ROOT%{shim_efi_dir}/shim%{-a*}.efi			\
install -m 0700 mm%{-a*}.efi						\\\
	$RPM_BUILD_ROOT%{shim_efi_dir}/mm%{-a*}.efi			\
install -m 0600 %{-b*}							\\\
	$RPM_BUILD_ROOT%{shim_efi_dir}/BOOT%{-A*}.CSV			\
install -m 0700 shim%{-a*}.efi						\\\
	$RPM_BUILD_ROOT%{shim_boot_dir}/BOOT%{-A*}.EFI			\
install -m 0700 fb%{-a*}.efi						\\\
	$RPM_BUILD_ROOT%{shim_boot_dir}/fb%{-a*}.efi			\
%nil

# -a <efiarch>
# -A <EFIARCH>
%define define_files(a:A:)						\
%{expand:%%files -n shim-%{-a*}}					\
%{shim_efi_dir}/*%{-a*}*.efi						\
%{shim_efi_dir}/BOOT%{-A*}.CSV						\
%{shim_boot_dir}/*%{-a*}.efi						\
%{shim_boot_dir}/*%{-A*}.EFI						\
%ghost %attr(0700,root,root) %{efi_esp_dir}/BOOT%{-A*}.CSV     \
%ghost %attr(0700,root,root) %{efi_esp_dir}/mm%{-a*}.efi       \
%ghost %attr(0700,root,root) %{efi_esp_dir}/shim.efi        \
%ghost %attr(0700,root,root) %{efi_esp_dir}/shim%{-a*}.efi     \
%ghost %attr(0700,root,root) %{efi_esp_boot}/fb%{-a*}.efi      \
%ghost %attr(0700,root,root) %{efi_esp_boot}/BOOT%{-A*}.EFI    \
%{nil}

%ifarch x86_64
%global is_signed yes
%global is_alt_signed no
%global provide_legacy_shim 1
%endif
%ifarch aarch64
%global is_signed no
%global is_alt_signed no
%global provide_legacy_shim 1
%endif
%ifnarch x86_64 aarch64
%global is_signed no
%global is_alt_signed no
%global provide_legacy_shim 0
%endif

%if ! 0%{?vendor:1}
%global vendor nopenopenope
%endif

# vim:filetype=rpmmacros

BuildRequires:	pesign >= 0.112-20.fc27
# We need this because %%{efi} won't expand before choosing where to make
# the src.rpm in koji, and we could be on a non-efi architecture, in which
# case we won't have a valid expansion here...  To be solved in the future
# (shim 16+) by making the unsigned packages all provide "shim-unsigned", so
# we can just BuildRequires that.
%ifarch x86_64
BuildRequires: %{unsignedx64} = %{shimverx64}
BuildRequires: %{unsignedia32} = %{shimveria32}
%endif
%ifarch aarch64
BuildRequires: %{unsignedaa64} = %{shimveraa64}
#BuildRequires: %% {unsignedarm} = %% {shimverarm}
%endif

%description
Initial UEFI bootloader that handles chaining to a trusted full bootloader
under secure boot environments. This package contains the version signed by
the UEFI signing service.

%define_pkg -a %{efi_arch} -p 1
%if %{efi_has_alt_arch}
%define_pkg -a %{efi_alt_arch}
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
cd %{_builddir}
rm -rf shim-%{version}
mkdir shim-%{version}

%build

cd shim-%{version}
%if %{efi_has_alt_arch}
%define_build -a %{efi_alt_arch} -A %{efi_alt_arch_upper} -i %{shimefialt} -b no -c %{is_alt_signed} -d %{shimdiralt}
%endif
%define_build -a %{efi_arch} -A %{efi_arch_upper} -i %{shimefi} -b no -c %{is_signed} -d %{shimdir}

%install
rm -rf $RPM_BUILD_ROOT
cd shim-%{version}
install -D -d -m 0755 $RPM_BUILD_ROOT/boot/
install -D -d -m 0700 $RPM_BUILD_ROOT%{_prefix}/lib/shim/
install -D -d -m 0700 $RPM_BUILD_ROOT%{shim_efi_dir}/
install -D -d -m 0700 $RPM_BUILD_ROOT%{shim_boot_dir}/

%do_install -a %{efi_arch} -A %{efi_arch_upper} -b %{bootcsv}
%if %{efi_has_alt_arch}
%do_install -a %{efi_alt_arch} -A %{efi_alt_arch_upper} -b %{bootcsvalt}
%endif

%if %{provide_legacy_shim}
install -m 0700 %{shimefi} $RPM_BUILD_ROOT%{shim_efi_dir}/shim.efi
%endif
install -D -d -m 0755 $RPM_BUILD_ROOT%{_sysconfdir}/dnf/protected.d/
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/dnf/protected.d/

( cd $RPM_BUILD_ROOT ; find .%{efi_esp_root} -type f ) \
  | sed -e 's/\./\^/' -e 's,^\\\./,.*/,' -e 's,$,$,' > %{__brp_mangle_shebangs_exclude_from_file}

%define_files -a %{efi_arch} -A %{efi_arch_upper}
%if %{provide_legacy_shim}
%{shim_efi_dir}/shim.efi
%endif
%{_sysconfdir}/dnf/protected.d/shim.conf

%if %{efi_has_alt_arch}
%define_files -a %{efi_alt_arch} -A %{efi_alt_arch_upper}
%{_sysconfdir}/dnf/protected.d/shim.conf
%endif

%posttrans %{efi_arch}
set -eu

# On image mode, bootupd takes care of installing bootloader updates to the ESP
if [[ ! -e "/run/ostree-booted" ]]; then
   cp -pR %{shim_efi_dir}/.  %{efi_esp_dir} || :
   cp -pR %{shim_boot_dir}/. %{efi_esp_boot} || :
fi

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 16.1-8
- Import
