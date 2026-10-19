%global source1_hash 20e50fe7aae3e56378ebf0417d9de904f55a0e61e4df315333e632a4d3555d95
%global source0_hash 839d21eb4bd27bb0ee40d74c9da46df088c2e1425fcd8c3ea62b7e3a3dd28a91
%define dracutlibdir %{_prefix}/lib/dracut
%bcond_without doc
%global __requires_exclude pkg-config
Name: dracut
Version: 112
Release:        1%{?dist}
Summary:        Initramfs generator using udev
License: GPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-2.0-only
URL: https://github.com/dracut-ng/dracut-ng/wiki/
Source0:        https://github.com/dracut-ng/dracut-ng/archive/refs/tags/%{version}.tar.gz#/dracut-109.tar.gz
Source1: https://www.gnu.org/licenses/lgpl-2.1.txt
Patch1:  0001-revert-fix-install.d-correctly-install-pre-genned-im.patch
Patch2:  0002-feat-kernel-install-do-nothing-when-KERNEL_INSTALL_I.patch
Patch3:  0003-fix-kernel-install-do-not-generate-an-initrd-when-on.patch
Patch4:  0004-revert-fix-rescue-make-rescue-always-no-hostonly.patch
Patch5:  0005-feat-add-openssl-module.patch
Patch6:  0006-fix-ossl-ignore-compiler-warnings.patch
Patch7:  0007-Revert-feat-fips-include-openssl-s-fips.so-and-opens.patch
%if %{with doc}
%endif
Obsoletes: dracut-fips <= 047
Provides:  dracut-fips = %{version}-%{release}
Obsoletes: dracut-fips-aesni <= 047
Provides:  dracut-fips-aesni = %{version}-%{release}
Provides: bundled(crate(crosvm)) = 0.1.0
Requires: bash >= 4
Requires: coreutils
Requires: cpio
Requires: filesystem >= 2.1.0
Requires: findutils
Requires: grep
Requires: kmod
Requires: sed
Requires: zstd
Requires: xz
Recommends: memstrack
Recommends: hardlink
Recommends: kpartx
Recommends: (tpm2-tools if tpm2-tss)
Requires: util-linux >= 2.21
Requires: systemd >= 219
Requires: systemd-udev >= 219
Requires: procps-ng
Requires: libkcapi-hmaccalc
# oreon:deps
BuildRequires:  asciidoctor
BuildRequires:  bash
BuildRequires:  bash-completion
BuildRequires:  cargo
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  libxslt
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libkmod)
BuildRequires:  systemd
# /oreon:deps
%description
dracut contains tools to create bootable initramfses for the Linux
kernel. Unlike other implementations, dracut hard-codes as little
as possible into the initramfs. dracut contains various modules which
are driven by the event-based udev. Having root on MD, DM, LVM2, LUKS
is supported as well as NFS, iSCSI, NBD, FCoE with the dracut-network
package.

%package network
Summary: dracut modules to build a dracut initramfs with network support
Requires: %{name} = %{version}-%{release}
Requires: iputils
Requires: iproute
Requires: jq
Requires: NetworkManager >= 1.20
Suggests: NetworkManager
Obsoletes: dracut-generic < 008
Provides:  dracut-generic = %{version}-%{release}
%description network
This package requires everything which is needed to build a generic
all purpose initramfs with network support with dracut.

%package caps
Summary: dracut modules to build a dracut initramfs which drops capabilities
Requires: %{name} = %{version}-%{release}
Requires: libcap
%description caps
This package requires everything which is needed to build an
initramfs with dracut, which drops capabilities.

%package live
Summary: dracut modules to build a dracut initramfs with live image capabilities
Requires: %{name} = %{version}-%{release}
Requires: %{name}-network = %{version}-%{release}
Requires: tar coreutils bash device-mapper curl parted
%description live
This package requires everything which is needed to build an
initramfs with dracut, with live image capabilities, like Live CDs.

%package config-generic
Summary: dracut configuration to turn off hostonly image generation
Requires: %{name} = %{version}-%{release}
Obsoletes: dracut-nohostonly < 030
Provides:  dracut-nohostonly = %{version}-%{release}
%description config-generic
This package provides the configuration to turn off the host specific initramfs
generation with dracut and generates a generic image by default.

%package config-rescue
Summary: dracut configuration to turn on rescue image generation
Requires: %{name} = %{version}-%{release}
Obsoletes: dracut < 030
%description config-rescue
This package provides the configuration to turn on the rescue initramfs
generation with dracut.

%package tools
Summary: dracut tools to build the local initramfs
Requires: %{name} = %{version}-%{release}
%description tools
This package contains tools to assemble the local initrd and host configuration.

%package squash
Summary: dracut module to build an initramfs with most files in a squashfs image
Requires: %{name} = %{version}-%{release}
Requires: squashfs-tools
%description squash
This package provides a dracut module to build an initramfs, but store most files
in a squashfs image, result in a smaller initramfs size and reduce runtime memory
usage.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n dracut-%{version} -S git_am
cp %{SOURCE1} .

%build

%configure  --systemdsystemunitdir=%{_unitdir} \
            --bashcompletiondir=$(pkg-config --variable=completionsdir bash-completion) \
            --libdir=%{_prefix}/lib \
            --enable-dracut-cpio \
%if %{without doc}
            --disable-documentation \
%endif
            ${NULL}
%make_build
%install
%make_install %{?_smp_mflags} \
     libdir=%{_prefix}/lib
echo "DRACUT_VERSION=%{version}-%{release}" > $RPM_BUILD_ROOT/%{dracutlibdir}/dracut-version.sh
rm -fr -- $RPM_BUILD_ROOT/%{dracutlibdir}/modules.d/10dash
rm -fr -- $RPM_BUILD_ROOT/%{dracutlibdir}/modules.d/00mksh
rm -fr -- $RPM_BUILD_ROOT/%{dracutlibdir}/modules.d/35network-legacy
%ifnarch s390 s390x
rm -fr -- $RPM_BUILD_ROOT/%{dracutlibdir}/modules.d/68cms
rm -fr -- $RPM_BUILD_ROOT/%{dracutlibdir}/modules.d/69cio_ignore
rm -fr -- $RPM_BUILD_ROOT/%{dracutlibdir}/modules.d/73zipl
rm -fr -- $RPM_BUILD_ROOT/%{dracutlibdir}/modules.d/74dasd
rm -fr -- $RPM_BUILD_ROOT/%{dracutlibdir}/modules.d/74dasd_mod
rm -fr -- $RPM_BUILD_ROOT/%{dracutlibdir}/modules.d/74dcssblk
rm -fr -- $RPM_BUILD_ROOT/%{dracutlibdir}/modules.d/74zfcp
rm -fr -- $RPM_BUILD_ROOT/%{dracutlibdir}/modules.d/74znet
%else
rm -fr -- $RPM_BUILD_ROOT/%{dracutlibdir}/modules.d/10warpclock
%endif
rm -fr -- $RPM_BUILD_ROOT/%{dracutlibdir}/dracut.conf.d
rm -fr -- $RPM_BUILD_ROOT/%{dracutlibdir}/test
rm -fr -- $RPM_BUILD_ROOT/%{dracutlibdir}/modules.d/80test*
mkdir -p $RPM_BUILD_ROOT/boot/dracut
mkdir -p $RPM_BUILD_ROOT/var/lib/dracut/overlay
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/log
touch $RPM_BUILD_ROOT%{_localstatedir}/log/dracut.log
mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/initramfs
mkdir -p $RPM_BUILD_ROOT%{dracutlibdir}/dracut.conf.d
install -m 0644 dracut.conf.d/fedora/01-dist.conf $RPM_BUILD_ROOT%{dracutlibdir}/dracut.conf.d/01-dist.conf
rm -f $RPM_BUILD_ROOT%{_mandir}/man?/*suse*
echo 'hostonly="no"' > $RPM_BUILD_ROOT%{dracutlibdir}/dracut.conf.d/02-generic-image.conf
echo 'dracut_rescue_image="yes"' > $RPM_BUILD_ROOT%{dracutlibdir}/dracut.conf.d/02-rescue.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n dracut-network -f %{oreon_filedir}/dracut-network.list
%files -n dracut-caps -f %{oreon_filedir}/dracut-caps.list
%files -n dracut-live -f %{oreon_filedir}/dracut-live.list
%files -n dracut-config-generic -f %{oreon_filedir}/dracut-config-generic.list
%files -n dracut-config-rescue -f %{oreon_filedir}/dracut-config-rescue.list
%files -n dracut-tools -f %{oreon_filedir}/dracut-tools.list
%files -n dracut-squash -f %{oreon_filedir}/dracut-squash.list

%changelog

%autochangelog
