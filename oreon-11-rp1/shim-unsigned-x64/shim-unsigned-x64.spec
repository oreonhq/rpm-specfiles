%global pesign_vre 0.106-1
%global openssl_vre 1.0.2j

# For prereleases, % global prerelease rc2, and downpatch Makefile
%if %{defined prerelease}
%global dashpre -%{prerelease}
%global dotpre .%{prerelease}
%global tildepre ~%{prerelease}
%global zdpd 0%{dotpre}.
%endif

# Shim bake-in and repo layout use EFI/<efidir>/ (must match signed shim %%os_id). Build host ID would wrongly yield fedora in mock.
%global efidir oreon
%global shimrootdir %{_datadir}/shim/
%global shimversiondir %{shimrootdir}/%{version}-%{release}
%global efiarch x64
%global shimdir %{shimversiondir}/%{efiarch}
%global efialtarch ia32
%global shimaltdir %{shimversiondir}/%{efialtarch}

%global debug_package %{nil}
%global __debug_package 1
%global _binaries_in_noarch_packages_terminate_build 0
%global __debug_install_post %{_builddir}/shim-%{version}/shim-find-debuginfo.sh %{efiarch} %{efialtarch}
%undefine _debuginfo_subpackages

# currently here's what's in our dbx: nothing
%global dbxfile %{nil}

Name:		shim-unsigned-%{efiarch}
Version:	15.8
Release:	9
Summary:	First-stage UEFI bootloader
ExclusiveArch:	x86_64
License:	BSD-2-Clause AND OpenSSL
URL:		https://github.com/rhboot/shim
Source0:	https://github.com/rhboot/shim/releases/download/%{version}%{?dashpre}/shim-%{version}%{?dotpre}.tar.bz2
# Vendor cert embedded in shim
Source1:	oreon-shim-vendor-ca.cer
%if 0%{?dbxfile}
Source2:	%{dbxfile}
%endif
Source3:	sbat.oreon.csv

BuildRequires:	gcc make
BuildRequires:	elfutils-libelf-devel
BuildRequires:	git openssl-devel openssl
BuildRequires:	pesign >= %{pesign_vre}
BuildRequires:	dos2unix findutils

# Shim uses OpenSSL, but cannot use the system copy as the UEFI ABI is not
# compatible with SysV (there's no red zone under UEFI) and there isn't a
# POSIX-style C library.
# BuildRequires:	OpenSSL
Provides:	bundled(openssl) = %{openssl_vre}

%global desc \
Initial UEFI bootloader that handles chaining to a trusted full \
bootloader under secure boot environments.
%global debug_desc \
This package provides debug information for package %{expand:%%{name}} \
Debug information is useful when developing applications that \
use this package or when debugging this package.

%description
%desc

%package -n shim-unsigned-%{efialtarch}
Summary:	First-stage UEFI bootloader (unsigned data)
Provides:	bundled(openssl) = %{openssl_vre}

%description -n shim-unsigned-%{efialtarch}
%desc

%package debuginfo
Summary:	Debug information for shim-unsigned-%{efiarch}
AutoReqProv:	0
BuildArch:	noarch

%description debuginfo
%debug_desc

%package -n shim-unsigned-%{efialtarch}-debuginfo
Summary:	Debug information for shim-unsigned-%{efialtarch}
AutoReqProv:	0
BuildArch:	noarch

%description -n shim-unsigned-%{efialtarch}-debuginfo
%debug_desc

%package debugsource
Summary:	Debug Source for shim-unsigned
AutoReqProv:	0
BuildArch:	noarch

%description debugsource
%debug_desc

%prep
%autosetup -S git_am -n shim-%{version}
git config --unset user.email
git config --unset user.name
# binutils 2.46+ treats %%--target as input bfd too and objcopy then rejects the %%%.so LP 2139340. Shim upstream still uses %%--target in Make.defaults.
sed -i 's/--target efi-app-/--output-target efi-app-/g' Make.defaults
mkdir build-%{efiarch}
mkdir build-%{efialtarch}
install -d data
cp -f %{SOURCE3} data/sbat.redhat.csv

# Generated in %%prep so source prep does not need shim-find-debuginfo.sh in SOURCES (Fedora shim-find-debuginfo.sh logic).
cat > shim-find-debuginfo.sh << 'SHIMFINDDEBUGINFO_EOF'
#!/bin/bash
# Copyright (C) 2017 Peter Jones
# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-3.0-or-later
set -e
set -u

mainarch=$1 && shift
if [ $# == 1 ]; then
    altarch=$1 && shift
fi
if ! [ -v RPM_BUILD_ROOT ]; then
    echo "RPM_BUILD_ROOT must be set" 1>&2
    exit 1
fi

findsource()
{
    (
        cd "${RPM_BUILD_ROOT}"
        find usr/src/debug/ -type d | sed -e "s,^,%%dir /," | sort -u | tac
        find usr/src/debug/ -type f | sed -e "s,^,/," | sort -u | tac
    )
}

finddebug()
{
    arch=$1 && shift
    declare -a dirs=()
    declare -a files=()
    declare -a excludes=()
    declare -a tmp=()

    pushd "${RPM_BUILD_ROOT}" >/dev/null 2>&1

    mapfile -t tmp < <(find usr/lib/debug/ -type f -iname "*.efi.debug")
    for x in "${tmp[@]}" ; do
        if ! [ -e "${x}" ]; then
            break
        fi
        if [[ ${x} =~ ${arch}\.efi\.debug$ ]]; then
            files[${#files[@]}]=${x}
        else
            excludes[${#excludes[@]}]=${x}
        fi
    done
    for x in usr/lib/debug/.build-id/*/*.debug ; do
        if ! [ -e "${x}" ]; then
            break
        fi
        link=$(readlink "${x}")
        if [[ ${link} =~ ${arch}\.efi\.debug$ ]]; then
            files[${#files[@]}]=${x}
            files[${#files[@]}]=${x%%.debug}
        else
            excludes[${#excludes[@]}]=${x}
            excludes[${#excludes[@]}]=${x%%.debug}
        fi
    done
    for x in "${files[@]}" ; do
        declare name

        name=$(dirname "/${x}")
        while [ "${name}" != "/" ]; do
            case "${name}" in
                "/usr/lib/debug"|"/usr/lib"|"/usr")
                ;;
                *)
                    dirs[${#dirs[@]}]=${name}
                ;;
            esac
            name=$(dirname "${name}")
        done
    done

    popd >/dev/null 2>&1
    for x in "${dirs[@]}" ; do
        echo "%%dir ${x}"
    done | sort | uniq
    for x in "${files[@]}" ; do
        echo "/${x}"
    done | sort | uniq
    for x in "${excludes[@]}" ; do
        echo "%%exclude /${x}"
    done
}

findsource > "build-${mainarch}/debugsource.list"
finddebug "${mainarch}" > "build-${mainarch}/debugfiles.list"
if [ -v altarch ]; then
    finddebug "${altarch}" > "build-${altarch}/debugfiles.list"
fi
SHIMFINDDEBUGINFO_EOF
chmod 755 shim-find-debuginfo.sh

%build
COMMIT_ID=5914984a1ffeab841f482c791426d7ca9935a5e6
MAKEFLAGS="TOPDIR=.. -f ../Makefile COMMIT_ID=${COMMIT_ID} "
MAKEFLAGS+="EFIDIR=%{efidir} PKGNAME=shim RELEASE=%{release} "
MAKEFLAGS+="ENABLE_SHIM_HASH=true "
# -j1 avoid parallel %.efi and %.efi.debug (both objcopy the same %.so) which can break on binutils (shimx64.so file format not recognized).
MAKEFLAGS+=" -j1 "
if [ -f "%{SOURCE1}" ]; then
	MAKEFLAGS="$MAKEFLAGS VENDOR_CERT_FILE=%{SOURCE1} "
fi
%if 0%{?dbxfile}
if [ -f "%{SOURCE2}" ]; then
	MAKEFLAGS="$MAKEFLAGS VENDOR_DBX_FILE=%{SOURCE2} "
fi
%endif

cd build-%{efiarch}
make ${MAKEFLAGS} \
	FORMAT='--output-target efi-app-x86_64' \
	DEFAULT_LOADER='\\\\grub%{efiarch}.efi' \
	all
cd ..

cd build-%{efialtarch}
setarch linux32 -B make ${MAKEFLAGS} \
	ARCH=%{efialtarch} \
	FORMAT='--output-target efi-app-ia32' \
	DEFAULT_LOADER='\\\\grub%{efialtarch}.efi' \
	all
cd ..

%install
COMMIT_ID=5914984a1ffeab841f482c791426d7ca9935a5e6
MAKEFLAGS="TOPDIR=.. -f ../Makefile COMMIT_ID=${COMMIT_ID} "
MAKEFLAGS+="EFIDIR=%{efidir} PKGNAME=shim RELEASE=%{release} "
MAKEFLAGS+="ENABLE_SHIM_HASH=true "
if [ -f "%{SOURCE1}" ]; then
	MAKEFLAGS="$MAKEFLAGS VENDOR_CERT_FILE=%{SOURCE1} "
fi
%if 0%{?dbxfile}
if [ -f "%{SOURCE2}" ]; then
	MAKEFLAGS="$MAKEFLAGS VENDOR_DBX_FILE=%{SOURCE2} "
fi
%endif

cd build-%{efiarch}
make ${MAKEFLAGS} \
	FORMAT='--output-target efi-app-x86_64' \
	DEFAULT_LOADER='\\\\grub%{efiarch}.efi' \
	DESTDIR=${RPM_BUILD_ROOT} \
	install-as-data install-debuginfo install-debugsource
install -m 0644 BOOT*.CSV "${RPM_BUILD_ROOT}/%{shimdir}/"
cd ..

cd build-%{efialtarch}
setarch linux32 -B make ${MAKEFLAGS} \
	ARCH=%{efialtarch} \
	FORMAT='--output-target efi-app-ia32' \
	DEFAULT_LOADER='\\\\grub%{efialtarch}.efi' \
	DESTDIR=${RPM_BUILD_ROOT} \
	install-as-data install-debuginfo install-debugsource
install -m 0644 BOOT*.CSV "${RPM_BUILD_ROOT}/%{shimaltdir}/"
cd ..

%files
%license COPYRIGHT
%dir %{shimrootdir}
%dir %{shimversiondir}
%dir %{shimdir}
%{shimdir}/*.efi
%{shimdir}/*.hash
%{shimdir}/*.CSV

%files -n shim-unsigned-%{efialtarch}
%license COPYRIGHT
%dir %{shimrootdir}
%dir %{shimversiondir}
%dir %{shimaltdir}
%{shimaltdir}/*.efi
%{shimaltdir}/*.hash
%{shimaltdir}/*.CSV

%files debuginfo -f build-%{efiarch}/debugfiles.list

%files -n shim-unsigned-%{efialtarch}-debuginfo -f build-%{efialtarch}/debugfiles.list

%files debugsource -f build-%{efiarch}/debugsource.list

%changelog
* Wed Mar 26 2026 Oreon Packaging Team <packaging@oreonhq.com> - 15.8-8
- Set %%efidir to oreon so ESP path is EFI/oreon not mock chroot ID (fedora)

* Thu Mar 26 2026 Oreon Packaging Team <packaging@oreonhq.com> - 15.8-7
- Sed Make.defaults FORMAT to %%--output-target efi-app for binutils 2.46+ LP 2139340

* Thu Mar 26 2026 Oreon Packaging Team <packaging@oreonhq.com> - 15.8-6
- Build shim with make -j1 to avoid parallel objcopy on shared %%.so vs binutils

* Wed Mar 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 15.8-5
- Generate shim-find-debuginfo.sh in %%prep so SOURCES does not need that file

* Wed Mar 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 15.8-4
- Drop empty shim.patches %%include so source prep does not need shim.patches in SOURCES

* Sat Mar 21 2026 Oreon Packaging Team <packaging@oreonhq.com> - 15.8-3
- oreon-shim-vendor-ca sbat.oreon.csv as data sbat.redhat.csv

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 15.8-2
- Prepare for Oreon 11 (RP1)
