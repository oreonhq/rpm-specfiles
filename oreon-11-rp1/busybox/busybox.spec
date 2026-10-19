%global source10_hash 2806e2d689c6affb45ff8761a1011e6ab8a39369a617421fbff9c29f6dbefec6
%global source0_hash 34f9ea6ff8636f2c9241153b9114eefa9e65674a45318ae1ef95bb5f31c53bb2
%global build_petitboot 1
%global build_musl 0
%ifnarch ppc %{power64} s390 s390x aarch64
%global build_uclibc 0
%else
%global build_uclibc 0
%endif
%ifarch ppc64le
%global build_glibc_static 1
%endif
%global default_type glibc
%global print_configs 0
%ifarch x86_64 aarch64
%global hcflags %{_hardening_cflags} -fstack-clash-protection
%global hldflags %{_hardening_ldflags} -Wl,-z,relro,-z,now
%endif
Name:		busybox
Version:	1.38.0
Release:        1%{?dist}
Epoch:		1
Summary:        Statically linked binary providing simplified versions of system commands
License:	GPL-2.0-only
URL:		http://www.busybox.net
Source0:        http://www.busybox.net/downloads/%{name}-%{version}.tar.bz2
Source2:	busybox-petitboot.config
Source3:	busybox-shared.config
Source4:	busybox-glibc-static.config
Source5:	busybox-uclibc-static.config
Source6:	busybox-musl-static.config
Source10:	https://github.com/sabotage-linux/kernel-headers/archive/refs/tags/v4.19.88-1.tar.gz
Patch0:		busybox-1.31.1-stime-fix.patch
Patch1:		busybox-1.36.1-no-cbq.patch
Patch2:		busybox-1.37.0-fix-conditional-for-sha1_process_block64_shaNI.patch
%if 0%{?build_musl}
%endif
%if 0%{?build_uclibc}
%endif
ExcludeArch:    i686
%ifarch riscv64 s390x
%endif
Provides:	bundled(md5-drepper2)
# oreon:deps
BuildRequires:  gcc
BuildRequires:  glibc-static
BuildRequires:  libselinux-devel
BuildRequires:  libselinux-static
BuildRequires:  libsepol-devel
BuildRequires:  libsepol-static
BuildRequires:  make
# /oreon:deps
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

arch=`uname -m | sed -e 's/i.86/i386/' -e 's/armv7l/arm/' -e 's/armv5tel/arm/'`
%ifarch riscv64 s390x
mkdir linux-header-stock
rpm -ql kernel-headers | xargs -i cp -v --parents {} ./linux-header-stock || :
%endif
%if 0%{?build_musl}
cp %{SOURCE6} .config
%ifarch s390x
sed -i -e "s/CONFIG_KBD_MODE=y/# CONFIG_KBD_MODE is not set/" -e "s/CONFIG_LOADFONT=y/# CONFIG_LOADFONT is not set/" -e "s/CONFIG_SETFONT=y/# CONFIG_SETFONT is not set/" -e "s/CONFIG_OPENVT=y/# CONFIG_OPENVT is not set/" -e "s/CONFIG_SHOWKEY=y/# CONFIG_SHOWKEY is not set/" .config
%endif
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
%if 0%{?build_uclibc}
cp %{SOURCE5} .config
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
%if 0%{?build_glibc_static}
cp %{SOURCE4} .config
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
%if 0%{?build_petitboot}
make clean
%if 0%{?build_musl}
cp %{SOURCE2} .config
%ifarch s390x
sed -i -e "s/CONFIG_KBD_MODE=y/# CONFIG_KBD_MODE is not set/" -e "s/CONFIG_LOADFONT=y/# CONFIG_LOADFONT is not set/" -e "s/CONFIG_SETFONT=y/# CONFIG_SETFONT is not set/" -e "s/CONFIG_OPENVT=y/# CONFIG_OPENVT is not set/" -e "s/CONFIG_SHOWKEY=y/# CONFIG_SHOWKEY is not set/" .config
%endif
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
%if 0%{?build_uclibc}
cp %{SOURCE2} .config
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
%if 0%{?build_glibc_static}
cp %{SOURCE2} .config
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
cp %{SOURCE3} .config
yes "" | make oldconfig
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
ln -s ./busybox %{buildroot}%{_sbindir}/udhcpc
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n busybox-petitboot -f %{oreon_filedir}/busybox-petitboot.list
%files -n busybox-shared -f %{oreon_filedir}/busybox-shared.list

%changelog

%autochangelog
