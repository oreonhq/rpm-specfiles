%global source0_hash none

# NOTE: This specfile is generated from upstream at https://github.com/rhinstaller/lorax
# NOTE: Please submit changes as a pull request
%define debug_package %{nil}
%global forgeurl https://github.com/weldr/lorax

Name:           lorax
Version:        44.6
Release:        1%{?dist}
Summary:        Tool for creating the anaconda install images
License:        GPL-2.0-or-later

# qemu is no longer available on 32-bit
ExcludeArch:    %{ix86}

%global tag %{version}
%forgemeta
Url:            %{forgeurl}
Source0:        https://github.com/weldr/lorax/archive/refs/tags/lorax-%{version}-1.tar.gz#/lorax-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  make
BuildRequires:  systemd-rpm-macros

Requires:       lorax-templates
%if 0%{?rhel} >= 9 || (0%{?oreon} >= 11)
Requires:       lorax-templates-rhel
%endif

Requires:       cpio
Requires:       device-mapper
Requires:       dosfstools
Requires:       e2fsprogs
Requires:       findutils
Requires:       gawk
Requires:       xorriso
Requires:       glib2
Requires:       glibc
Requires:       glibc-common
Requires:       gzip
Requires:       isomd5sum
Requires:       module-init-tools
Requires:       parted
Requires:       squashfs-tools >= 4.2
Requires:       erofs-utils >= 1.8.2
Requires:       util-linux
Requires:       xz-lzma-compat
Requires:       xz
Requires:       pigz
Requires:       pbzip2
Requires:       dracut >= 030
Requires:       kpartx
Requires:       psmisc

# Python modules
Requires:       libselinux-python3
Requires:       python3-mako
Requires:       python3-kickstart >= 3.19
Requires:       python3-libdnf5
Requires:       python3-librepo
Requires:       python3-pycdio

%if 0%{?fedora} || (0%{?oreon} >= 11)
# Fedora specific deps
%ifarch x86_64
Requires:       hfsplus-tools
%endif
%endif

%ifarch x86_64 ppc64le
Requires:       grub2
Requires:       grub2-tools
%endif

%ifarch s390 s390x
Requires:       openssh
Requires:       s390utils >= 2.15.0-2
%endif

# Moved image-minimizer tool to lorax
Provides:       appliance-tools-minimizer = %{version}-%{release}
Obsoletes:      appliance-tools-minimizer < 007.7-3

%description
Lorax is a tool for creating the anaconda install images.

It also includes livemedia-creator which is used to create bootable livemedia,
including live isos and disk images. It can use libvirtd for the install, or
Anaconda's image install feature.

%package docs
Summary: Lorax html documentation
Requires: lorax = %{version}-%{release}

%description docs
Includes the full html documentation for lorax, livemedia-creator, and the pylorax library.

%if ! (0%{?rhel} >= 10 && "%{_arch}" == "ppc64le") || (0%{?oreon} >= 11)
%package lmc-virt
Summary:  livemedia-creator libvirt dependencies
Requires: lorax = %{version}-%{release}
%if 0%{?rhel} || (0%{?oreon} >= 11)
# RHEL doesn't have qemu, just qemu-kvm
Requires: qemu-kvm
%else
Requires: qemu
Recommends: qemu-kvm
%endif

# edk2 builds currently only support these arches
%ifarch x86_64
Requires: edk2-ovmf
%endif
%ifarch aarch64
Requires: edk2-aarch64
%endif

%description lmc-virt
Additional dependencies required by livemedia-creator when using it with qemu.
%endif

%package lmc-novirt
Summary:  livemedia-creator no-virt dependencies
Requires: lorax = %{version}-%{release}
Requires: anaconda-core
Requires: anaconda-tui
Requires: anaconda-install-env-deps
Requires: system-logos
Requires: python3-psutil

%description lmc-novirt
Additional dependencies required by livemedia-creator when using it with --no-virt
to run Anaconda.

%package templates-generic
Summary:  Generic build templates for lorax and livemedia-creator
Requires: lorax = %{version}-%{release}
Provides: lorax-templates = %{version}-%{release}

%description templates-generic
Lorax templates for creating the boot.iso and live isos are placed in
/usr/share/lorax/templates.d/99-generic

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n lorax-lorax-44.6-1

%build

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT mandir=%{_mandir} install

%files
%defattr(-,root,root,-)
%license COPYING
%doc AUTHORS
%doc docs/lorax.rst docs/livemedia-creator.rst docs/product-images.rst
%doc docs/*ks
%{python3_sitelib}/pylorax
%{python3_sitelib}/pylorax-%{version}.dist-info
%{_bindir}/lorax
%{_bindir}/mkefiboot
%{_bindir}/livemedia-creator
%{_bindir}/mkksiso
%{_bindir}/image-minimizer
%dir %{_sysconfdir}/lorax
%config(noreplace) %{_sysconfdir}/lorax/lorax.conf
%dir %{_datadir}/lorax
%{_mandir}/man1/lorax.1*
%{_mandir}/man1/livemedia-creator.1*
%{_mandir}/man1/mkksiso.1*
%{_mandir}/man1/image-minimizer.1*
%{_tmpfilesdir}/lorax.conf

%files docs
%doc docs/html/*

%if ! (0%{?rhel} >= 10 && "%{_arch}" == "ppc64le") || (0%{?oreon} >= 11)
%files lmc-virt
%endif

%files lmc-novirt

%files templates-generic
%dir %{_datadir}/lorax/templates.d
%{_datadir}/lorax/templates.d/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 44.6-1
- Import
