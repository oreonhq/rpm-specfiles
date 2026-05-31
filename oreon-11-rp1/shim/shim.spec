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

Source0:	shim.rpmmacros
Source1:	shim.conf

# keep these two lists of sources synched up arch-wise.  That is 0 and 10
# match, 1 and 11 match, ...
Source10:	BOOTAA64.CSV
Source20:	shimaa64.efi
Source11:	BOOTIA32.CSV
Source21:	shimia32.efi
Source12:	BOOTX64.CSV
Source22:	shimx64.efi
#Source13:	BOOTARM.CSV
#Source23:	shimarm.efi

%include %{SOURCE0}

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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }cd %{_builddir}
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
