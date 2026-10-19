%global source0_hash 0d5296f3af83560caf391e5757195af2205a5237fbee4ecfcf5d8eb89a01bb2c
Summary:        Tools for Linux kernel block layer cache
Name: bcache-tools
Version: 1.1
Release:        16%{?dist}
License: GPL-2.0-only
URL: http://bcache.evilpiepirate.org/
VCS: git://git.kernel.org/pub/scm/linux/kernel/git/colyli/bcache-tools.git
Source0:        %{name}-%{version}.tar.gz
Source1: bcache-status-20140220.tar.gz
Patch0: %{name}-status-20160804-man.patch
Patch1: %{name}-1.1-cmdline.patch
Patch2: %{name}-20131018-fedconf.patch
Patch3: %{name}-1.0.8-noprobe.2.patch
Patch4: %{name}-1.1-util-linux-hdr.patch
Patch5: bcache-status-python3.patch
Patch6: bcache-status-rootgc.patch
Patch7: bcache-tools-1.1-man.pach
Patch8: bcache-tools-sbin.patch
Requires: libblkid >= 2.24
Conflicts: dracut < 034
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libblkid-devel
BuildRequires:  libsmartcols-devel
BuildRequires:  libuuid-devel
BuildRequires:  systemd
# /oreon:deps
%description
Bcache is a Linux kernel block layer cache. It allows one or more fast disk
drives such as flash-based solid state drives (SSDs) to act as a cache for
one or more slower hard disk drives.
This package contains the utilities for manipulating bcache.

%global _udevlibdir %{_prefix}/lib/udev
%global dracutlibdir %{_prefix}/lib/dracut

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n bcache-tools-%{version}
tar xzf %{SOURCE1} --strip-components=1
%patch -P0 -p1 -b .man
%patch -P1 -p1 -b .cmdline
%patch -P2 -p1 -b .fedconfmake
chmod +x configure
%patch -P3 -p1 -b .noprobe
%patch -P4 -p1 -b .util-linux-hdr

%patch -P5 -p1 -b .python3
%patch -P6 -p1 -b .rootgc
%patch -P7 -p1 -b .man
%patch -P8 -p1 -b .sbin

%build

%configure
make %{?_smp_mflags} SBINDIR=%{_sbindir}
%install
mkdir -p \
    %{buildroot}%{_sbindir} \
    %{buildroot}%{_mandir}/man8 \
    %{buildroot}%{_udevlibdir} \
    %{buildroot}%{_udevrulesdir} \
    %{buildroot}%{dracutlibdir}/modules.d
%make_install \
    INSTALL="install -p" \
    UDEVLIBDIR=%{_udevlibdir} \
    DRACUTLIBDIR=%{dracutlibdir} \
    MANDIR=%{_mandir} \
    SBINDIR=%{_sbindir}
rm %{buildroot}%{_udevlibdir}/probe-bcache
rm %{buildroot}%{_mandir}/man8/probe-bcache.8
rm %{buildroot}%{_prefix}/lib/initcpio/install/bcache
rm %{buildroot}%{_datarootdir}/initramfs-tools/hooks/bcache
install -p  -m 755 bcache-status %{buildroot}%{_sbindir}/bcache-status
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
