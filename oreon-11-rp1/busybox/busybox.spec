%global source0_hash 2806e2d689c6affb45ff8761a1011e6ab8a39369a617421fbff9c29f6dbefec6

# Groupings
%global build_petitboot 1

# musl is not available in EPEL.
%if 0%{?fedora}
# musl-gcc does not work on ppc64le (2022-03-22)
%ifnarch ppc64le
%global build_musl 1
%else
%global build_musl 0
%endif
%else
%global build_musl 0
%endif

# uclibc does not work. Except on EPEL9 where somehow it does.
# DISABLED AS OF 2022-03-19 - spot@fedoraproject.org
%ifnarch ppc %{power64} s390 s390x aarch64
%global build_uclibc 0
%else
%global build_uclibc 0
%endif

# We really only need this on EPEL where musl does not exist
# OR on ppc64le on Fedora.
%if 0%{?rhel}
%global build_glibc_static 1
%else
%ifarch ppc64le
%global build_glibc_static 1
%endif
%endif

# Default
# This logic changes if uclibc ever actually works again.
%if 0%{?fedora}
%ifnarch ppc64le
%global default_type musl
%else
%global default_type glibc
%endif
%else
%global default_type glibc
%endif

%global print_configs 0

# Some architectures like the hardened flags, others do not.
# If uclibc ever comes back, make variables for it.
%ifarch x86_64 aarch64
%global hcflags %{_hardening_cflags} -fstack-clash-protection
%global hldflags %{_hardening_ldflags} -Wl,-z,relro,-z,now
%endif

Name:		busybox
Version:	1.37.0
Release:	7%{?dist}
Epoch:		1
Summary:	Statically linked binary providing simplified versions of system commands
License:	GPL-2.0-only
URL:		http://www.busybox.net
Source0:	http://www.busybox.net/downloads/%{name}-%{version}.tar.bz2
Source2:	busybox-petitboot.config
Source3:	busybox-shared.config
Source4:	busybox-glibc-static.config
Source5:	busybox-uclibc-static.config
Source6:	busybox-musl-static.config
# musl kernel headers
Source10:	https://github.com/sabotage-linux/kernel-headers/archive/refs/tags/v4.19.88-1.tar.gz
Patch0:		busybox-1.31.1-stime-fix.patch
# Linux no longer supports CBQ UAPI as of
# https://github.com/torvalds/linux/commit/33241dca486264193ed68167c8eeae1fb197f3df
# I just changed networking/tc.c to print an unsupported message if you try to set options for cbq
# ... there is probably a better fix.
# Technically, the bundled headers from sabotage-linux still have the CBQ vars, but they're really old at this point.
# Felt safer to just disable CBQ, as that is what iproute did:
# https://github.com/iproute2/iproute2/commit/07ba0af3fee132eddc1c2eab643ff4910181c993
Patch1:		busybox-1.36.1-no-cbq.patch
# sha1_process_block64_shaNI is only valid on x86
# most of the calls are wrapped in an arch conditional, but they missed one.
Patch2:		busybox-1.37.0-fix-conditional-for-sha1_process_block64_shaNI.patch
BuildRequires:	gcc
BuildRequires:	libselinux-devel >= 1.27.7-2
BuildRequires:	libsepol-devel
BuildRequires:	libselinux-static
BuildRequires:	libsepol-static
BuildRequires:	glibc-static
%if 0%{?build_musl}
BuildRequires:	musl-libc-static, musl-devel, musl-gcc
%endif
%if 0%{?build_uclibc}
BuildRequires:	uClibc-static
%endif
BuildRequires:	make
# $DEITY help you if you need busybox for ia32 in 2022.
ExcludeArch:    i686

# Using header from Fedora, beacuse sabotage-linux/kernel-headers is not available for riscv64
%ifarch riscv64 s390x
BuildRequires:	kernel-headers
%endif

# libbb/hash_md5_sha.c
# https://bugzilla.redhat.com/1024549
Provides:	bundled(md5-drepper2)

%description
Busybox is a single binary which includes versions of a large number
of system commands, including a shell. This package can be very
useful for recovering from certain types of system failures,
particularly those involving broken shared libraries.

%if 0%{?build_petitboot}
%package petitboot
Summary:	Version of busybox configured for use with petitboot

%description petitboot
Busybox is a single binary which includes versions of a large number
of system commands, including a shell. The version contained in this
package is a minimal configuration intended for use with the Petitboot
bootloader used on PlayStation 3. The busybox package provides a binary
better suited to normal use.
%endif

%package shared
Summary:	A shared (non-static) version of busybox

%description shared
Busybox is a single binary which includes versions of a large number
of system commands, including a shell. The version contained in this
package is build against shared libraries, most notably glibc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -a 10
%patch -P0 -p1 -b .stime
%patch -P1 -p1 -b .cbq
%patch -P2 -p1 -b .shani-fix

%build
# Fix architecture name maps
arch=`uname -m | sed -e 's/i.86/i386/' -e 's/armv7l/arm/' -e 's/armv5tel/arm/'`

## TODO: CC="gcc %{optflags}" ?

## STATIC BUILDS

%ifarch riscv64 s390x
mkdir linux-header-stock
rpm -ql kernel-headers | xargs -i cp -v --parents {} ./linux-header-stock || :
%endif

# 1. Musl
%if 0%{?build_musl}
# We use musl-libc. It has broader architecture support and is still small.
cp %{SOURCE6} .config
%ifarch s390x
sed -i -e "s/CONFIG_KBD_MODE=y/# CONFIG_KBD_MODE is not set/" -e "s/CONFIG_LOADFONT=y/# CONFIG_LOADFONT is not set/" -e "s/CONFIG_SETFONT=y/# CONFIG_SETFONT is not set/" -e "s/CONFIG_OPENVT=y/# CONFIG_OPENVT is not set/" -e "s/CONFIG_SHOWKEY=y/# CONFIG_SHOWKEY is not set/" .config
%endif
# set all new options to defaults
yes "" | make oldconfig && \
%if 0%{?print_configs}
cat .config && \
%endif
%ifarch riscv64 s390x
make V=1 \
CC="musl-gcc -static" \
EXTRA_CFLAGS="-g -Ilinux-header-stock/usr/include %{?hcflags}" \
CFLAGS_busybox="-L%{_prefix}/$arch-linux-musl %{?hldflags}"
%else
make V=1 \
CC="musl-gcc -static" \
EXTRA_CFLAGS="-g -Ikernel-headers-4.19.88-1/$arch/include %{?hcflags}" \
CFLAGS_busybox="-L%{_prefix}/$arch-linux-musl %{?hldflags}"
%endif
cp busybox_unstripped busybox.musl.static
cp docs/busybox.1 docs/busybox.musl.static.1
%endif

make clean

# 2. uclibc
%if 0%{?build_uclibc}
# We use uclibc. It has smaller architecture support, but is more feature rich than musl.
# uclibc can't be built on ppc64,s390,ia64
cp %{SOURCE5} .config
# set all new options to defaults
yes "" | make oldconfig && \
%if 0%{?print_configs}
cat .config && \
%endif
make V=1 \
EXTRA_CFLAGS="-fstack-protector-strong -fstack-clash-protection -g -isystem %{_includedir}/uClibc" \
CFLAGS_busybox="-Wl,-z,relro,-z,now -nostartfiles -L%{_libdir}/uClibc %{_libdir}/uClibc/crt*.o"

cp busybox_unstripped busybox.uclibc.static
cp docs/busybox.1 docs/busybox.uclibc.static.1
%endif

make clean

# 3. glibc (static)
%if 0%{?build_glibc_static}
cp %{SOURCE4} .config
# set all new options to defaults
yes "" | make oldconfig && \
%if 0%{?print_configs}
cat .config && \
%endif
make V=1 \
EXTRA_CFLAGS="%{?hcflags} -g" \
CFLAGS_busybox="-static %{?hldflags}"

cp busybox_unstripped busybox.glibc.static
cp docs/busybox.1 docs/busybox.glibc.static.1
%endif

#    grep -v \
#        -e ^CONFIG_FEATURE_HAVE_RPC \
#        -e ^CONFIG_FEATURE_MOUNT_NFS \
#        -e ^CONFIG_FEATURE_INETD_RPC \
#        .config1 >.config && \
#    echo "# CONFIG_FEATURE_HAVE_RPC is not set" >>.config && \
#    echo "# CONFIG_FEATURE_MOUNT_NFS is not set" >>.config && \
#    echo "# CONFIG_FEATURE_INETD_RPC is not set" >>.config && \

%if 0%{?build_petitboot}

make clean

# 4. Petitboot

# 4a. Musl
%if 0%{?build_musl}
cp %{SOURCE2} .config
%ifarch s390x
sed -i -e "s/CONFIG_KBD_MODE=y/# CONFIG_KBD_MODE is not set/" -e "s/CONFIG_LOADFONT=y/# CONFIG_LOADFONT is not set/" -e "s/CONFIG_SETFONT=y/# CONFIG_SETFONT is not set/" -e "s/CONFIG_OPENVT=y/# CONFIG_OPENVT is not set/" -e "s/CONFIG_SHOWKEY=y/# CONFIG_SHOWKEY is not set/" .config
%endif
# set all new options to defaults
yes "" | make oldconfig
%if 0%{?print_configs}
cat .config && \
%endif
sed -i -e "s/CONFIG_FEATURE_VI_REGEX_SEARCH=y/CONFIG_FEATURE_VI_REGEX_SEARCH=n/" -e "s/CONFIG_EXTRA_COMPAT=y/CONFIG_EXTRA_COMPAT=n/" -e "s/CONFIG_FEATURE_INETD_RPC=y/CONFIG_FEATURE_INETD_RPC=n/" -e "s/CONFIG_FEATURE_UTMP=y/CONFIG_FEATURE_UTMP=n/" .config && \
%ifarch riscv64 s390x
make V=1 \
CC="musl-gcc -static" \
EXTRA_CFLAGS="-g -Ilinux-header-stock/usr/include %{?hcflags}" \
CFLAGS_busybox="-L%{_prefix}/$arch-linux-musl %{?hldflags}"
%else
make V=1 \
CC="musl-gcc -static" \
EXTRA_CFLAGS="-g -Ikernel-headers-4.19.88-1/$arch/include %{?hcflags}" \
CFLAGS_busybox="-L%{_prefix}/$arch-linux-musl %{?hldflags}"
%endif

cp busybox_unstripped busybox.musl.petitboot
cp docs/busybox.1 docs/busybox.musl.petitboot.1
%endif

make clean

#4b. Uclibc
%if 0%{?build_uclibc}
cp %{SOURCE2} .config
# set all new options to defaults
yes "" | make oldconfig
%if 0%{?print_configs}
cat .config && \
%endif
sed -i -e "s/CONFIG_UNICODE_PRESERVE_BROKEN=y/CONFIG_UNICODE_PRESERVE_BROKEN=n/" .config && \
make V=1 \
EXTRA_CFLAGS="-g -isystem %{_includedir}/uClibc" \
CFLAGS_busybox="%{_hardening_ldflags} -Wl,-z,relro,-z,now -static -nostartfiles -L%{_libdir}/uClibc %{_libdir}/uClibc/crt1.o %{_libdir}/uClibc/crti.o %{_libdir}/uClibc/crtn.o"; \
LDFLAGS="--static"

cp busybox_unstripped busybox.uclibc.petitboot
cp docs/busybox.1 docs/busybox.uclibc.petitboot.1
%endif

make clean

#4c. Glibc static
%if 0%{?build_glibc_static}
cp %{SOURCE2} .config
# set all new options to defaults
yes "" | make oldconfig
%if 0%{?print_configs}
cat .config && \
%endif
make V=1 \
EXTRA_CFLAGS="-g %{?hcflags}" \
LDFLAGS="%{?hldflags}"

cp busybox_unstripped busybox.glibc.petitboot
cp docs/busybox.1 docs/busybox.glibc.petitboot.1
%endif

%endif

make clean

## Shared
# 5. Glibc

# copy new configuration file
cp %{SOURCE3} .config
# set all new options to defaults
yes "" | make oldconfig
# Use optflags
%if 0%{?print_configs}
cat .config
%endif
make V=1 EXTRA_CFLAGS="%{optflags}" CFLAGS_busybox="%{build_ldflags}"
cp busybox_unstripped busybox.shared
cp docs/busybox.1 docs/busybox.shared.1

%install
mkdir -p %{buildroot}%{_sbindir}
install -m 755 busybox.*.static %{buildroot}%{_sbindir}
mv %{buildroot}%{_sbindir}/busybox.%{default_type}.static %{buildroot}%{_sbindir}/busybox
ln -s ./busybox %{buildroot}%{_sbindir}/busybox.%{default_type}.static
%if 0%{?build_petitboot}
install -m 755 busybox.*.petitboot %{buildroot}%{_sbindir}
mv %{buildroot}%{_sbindir}/busybox.%{default_type}.petitboot %{buildroot}%{_sbindir}/busybox.petitboot
ln -s ./busybox.petitboot %{buildroot}%{_sbindir}/busybox.%{default_type}.petitboot
%endif
install -m 755 busybox.shared %{buildroot}%{_sbindir}/busybox.shared
mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 docs/busybox.*.static.1 %{buildroot}%{_mandir}/man1/
mv %{buildroot}%{_mandir}/man1/busybox.%{default_type}.static.1 %{buildroot}%{_mandir}/man1/busybox.static.1
ln -s ./busybox.static.1 %{buildroot}%{_mandir}/man1/busybox.%{default_type}.static.1
%if 0%{?build_petitboot}
install -m 644 docs/busybox.*.petitboot.1 %{buildroot}%{_mandir}/man1/
mv %{buildroot}%{_mandir}/man1/busybox.%{default_type}.petitboot.1 %{buildroot}%{_mandir}/man1/busybox.petitboot.1
ln -s ./busybox.petitboot.1 %{buildroot}%{_mandir}/man1/busybox.%{default_type}.petitboot.1
%endif
install -m 644 docs/busybox.shared.1 %{buildroot}%{_mandir}/man1/busybox.shared.1

# Create symlink for udhcpc so cloud-init can use it. rhbz#2247055
ln -s ./busybox %{buildroot}%{_sbindir}/udhcpc

%files
%doc LICENSE README
%{_sbindir}/busybox
%{_sbindir}/busybox*.static
%{_sbindir}/udhcpc
%{_mandir}/man1/busybox*.static.1.gz

%if 0%{?build_petitboot}
%files petitboot
%doc LICENSE README
%{_sbindir}/busybox*.petitboot
%{_mandir}/man1/busybox*.petitboot.1.gz
%endif

%files shared
%doc LICENSE README
%{_sbindir}/busybox.shared
%{_mandir}/man1/busybox.shared.1.gz

%changelog
%autochangelog
