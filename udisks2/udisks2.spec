%global glib2_version                   2.68
%global gobject_introspection_version   1.30.0
%global polkit_version                  0.102
%global systemd_version                 208
%global dbus_version                    1.4.0
%global with_gtk_doc                    1
%global libblockdev_version             3.4

%define with_btrfs                      1
%ifnarch %{ix86}
%define with_lsm                        1
%endif

%define is_fedora                       0%{?rhel} == 0
%define is_git                          %(git show > /dev/null 2>&1 && echo 1 || echo 0)
%define git_hash                        %(git log -1 --pretty=format:"%h" || true)
%define build_date                      %(date '+%Y%m%d')

# btrfs is not available on RHEL
%if 0%{?rhel}
%define with_btrfs 0
%endif


Name:    udisks2
Summary: Disk Manager
Version: 2.11.1
Release: 1%{?dist}
License: GPL-2.0-or-later
URL:     https://github.com/storaged-project/udisks
Source0: https://github.com/storaged-project/udisks/releases/download/udisks-%{version}/udisks-%{version}.tar.bz2

BuildRequires: make
BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: gobject-introspection-devel >= %{gobject_introspection_version}
BuildRequires: libgudev1-devel >= %{systemd_version}
BuildRequires: polkit-devel >= %{polkit_version}
BuildRequires: systemd >= %{systemd_version}
BuildRequires: systemd-devel >= %{systemd_version}
BuildRequires: systemd-rpm-macros
BuildRequires: libacl-devel
BuildRequires: chrpath
BuildRequires: gtk-doc
BuildRequires: gettext-devel
BuildRequires: redhat-rpm-config
BuildRequires: libblockdev-devel        >= %{libblockdev_version}
BuildRequires: libblockdev-part-devel   >= %{libblockdev_version}
BuildRequires: libblockdev-loop-devel   >= %{libblockdev_version}
BuildRequires: libblockdev-swap-devel   >= %{libblockdev_version}
BuildRequires: libblockdev-mdraid-devel >= %{libblockdev_version}
BuildRequires: libblockdev-fs-devel     >= %{libblockdev_version}
BuildRequires: libblockdev-crypto-devel >= %{libblockdev_version}
BuildRequires: libblockdev-nvme-devel   >= %{libblockdev_version}
BuildRequires: libblockdev-smart-devel  >= %{libblockdev_version}
BuildRequires: libmount-devel
BuildRequires: libuuid-devel

Requires: libblockdev        >= %{libblockdev_version}
Requires: libblockdev-part   >= %{libblockdev_version}
Requires: libblockdev-loop   >= %{libblockdev_version}
Requires: libblockdev-swap   >= %{libblockdev_version}
Requires: libblockdev-mdraid >= %{libblockdev_version}
Requires: libblockdev-fs     >= %{libblockdev_version}
Requires: libblockdev-crypto >= %{libblockdev_version}
Requires: libblockdev-nvme   >= %{libblockdev_version}
Requires: libblockdev-smart  >= %{libblockdev_version}

Requires: lib%{name}%{?_isa} = %{version}-%{release}

# Needed to pull in the system bus daemon
Requires: dbus >= %{dbus_version}
# Needed to pull in the udev daemon
Requires: udev >= %{systemd_version}
# For mount, umount, mkswap
Requires: util-linux
# For mkfs.ext3, mkfs.ext3, e2label
Recommends: e2fsprogs
# For mkfs.xfs, xfs_admin
Recommends: xfsprogs
# For mkfs.vfat
Recommends: dosfstools
# For exfat
Recommends: exfatprogs
# For UDF
Recommends: udftools
# For ejecting removable disks
Recommends: eject
# For utab monitor
Requires: libmount
# The actual polkit agent
Requires: polkit >= %{polkit_version}

# For mkntfs (not available on rhel or on ppc/ppc64) and f2fs
%if %{is_fedora}
Recommends: f2fs-tools
Recommends: nilfs-utils
%ifnarch ppc ppc64
Recommends: ntfsprogs
%endif
%endif
Recommends: ntfs-3g

# btrfs
%if 0%{?with_btrfs}
Recommends: btrfs-progs
%endif


# For /proc/self/mountinfo, only available in 2.6.26 or higher
Conflicts: kernel < 2.6.26

Provides:  storaged = %{version}-%{release}
Obsoletes: storaged < %{version}-%{release}

%description
The Udisks project provides a daemon, tools and libraries to access and
manipulate disks, storage devices and technologies.

%package -n lib%{name}
Summary: Dynamic library to access the udisksd daemon
License: LGPL-2.0-or-later
Provides:  libstoraged = %{version}-%{release}
Obsoletes: libstoraged < %{version}-%{release}

%description -n lib%{name}
This package contains the dynamic library, which provides
access to the udisksd daemon.

%package -n %{name}-iscsi
Summary: Module for iSCSI
Requires: %{name}%{?_isa} = %{version}-%{release}
License: LGPL-2.0-or-later
Requires: iscsi-initiator-utils
BuildRequires: iscsi-initiator-utils-devel
Provides:  storaged-iscsi = %{version}-%{release}
Obsoletes: storaged-iscsi < %{version}-%{release}

%description -n %{name}-iscsi
This package contains module for iSCSI configuration.

%package -n %{name}-lvm2
Summary: Module for LVM2
Requires: %{name}%{?_isa} = %{version}-%{release}
License: LGPL-2.0-or-later
Requires: lvm2
Requires: libblockdev-lvm >= %{libblockdev_version}
BuildRequires: libblockdev-lvm-devel >= %{libblockdev_version}
Provides:  storaged-lvm2 = %{version}-%{release}
Obsoletes: storaged-lvm2 < %{version}-%{release}

%description -n %{name}-lvm2
This package contains module for LVM2 configuration.

%package -n lib%{name}-devel
Summary: Development files for lib%{name}
Requires: lib%{name}%{?_isa} = %{version}-%{release}
License: LGPL-2.0-or-later
Provides:  libstoraged-devel = %{version}-%{release}
Obsoletes: libstoraged-devel < %{version}-%{release}

%description -n lib%{name}-devel
This package contains the development files for the library lib%{name},
a dynamic library, which provides access to the udisksd daemon.

%if 0%{?with_btrfs}
%package -n %{name}-btrfs
Summary: Module for BTRFS
Requires: %{name}%{?_isa} = %{version}-%{release}
License: LGPL-2.0-or-later
Requires: libblockdev-btrfs >= %{libblockdev_version}
BuildRequires: libblockdev-btrfs-devel >= %{libblockdev_version}
Provides:  storaged-btrfs = %{version}-%{release}
Obsoletes: storaged-btrfs < %{version}-%{release}

%description -n %{name}-btrfs
This package contains module for BTRFS configuration.
%endif

%if 0%{?with_lsm}
%package -n %{name}-lsm
Summary: Module for LSM
Requires: %{name}%{?_isa} = %{version}-%{release}
License: LGPL-2.0-or-later
Requires: libstoragemgmt
BuildRequires: libstoragemgmt-devel
BuildRequires: libconfig-devel
Provides:  storaged-lsm = %{version}-%{release}
Obsoletes: storaged-lsm < %{version}-%{release}

%description -n %{name}-lsm
This package contains module for LSM configuration.
%endif

%prep
%autosetup -p1 -n udisks-%{version}
rm -f src/tests/dbus-tests/config_h.py
rm -f src/udisks-daemon-resources.{c,h}
# default to ntfs-3g (#2182206)
sed -i data/builtin_mount_options.conf -e 's/ntfs_drivers=ntfs3,ntfs/ntfs_drivers=ntfs,ntfs3/'

%build
# autoreconf -ivf
# modules need to be explicitly enabled
%configure            \
%if %{with_gtk_doc}
    --enable-gtk-doc  \
%else
    --disable-gtk-doc \
%endif
    --enable-smart    \
%if 0%{?with_btrfs}
    --enable-btrfs    \
%endif
%if 0%{?with_lsm}
    --enable-lsm      \
%endif
    --enable-lvm2     \
    --enable-iscsi
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%if %{with_gtk_doc} == 0
rm -fr %{buildroot}/%{_datadir}/gtk-doc/html/udisks2
%endif

# not created if lsm is disabled
mkdir -p %{buildroot}%{_sysconfdir}/udisks2/modules.conf.d

find %{buildroot} -name \*.la -o -name \*.a | xargs rm

chrpath --delete %{buildroot}/%{_sbindir}/umount.udisks2
chrpath --delete %{buildroot}/%{_bindir}/udisksctl
chrpath --delete %{buildroot}/%{_libexecdir}/udisks2/udisksd

%find_lang udisks2

%post -n %{name}
%systemd_post udisks2.service
# skip retriggering if udevd isn't even accessible, e.g. containers or
# rpm-ostree-based systems
if [ -S /run/udev/control ]; then
    udevadm control --reload
    udevadm trigger
fi

%preun -n %{name}
%systemd_preun udisks2.service

%postun -n %{name}
%systemd_postun_with_restart udisks2.service

%ldconfig_scriptlets -n lib%{name}

%files -f udisks2.lang
%doc README.md AUTHORS NEWS HACKING
%license COPYING

%dir %{_sysconfdir}/udisks2
%if %{is_fedora}
%dir %{_sysconfdir}/udisks2/modules.conf.d
%endif
%{_sysconfdir}/udisks2/udisks2.conf
%{_sysconfdir}/udisks2/mount_options.conf.example

%{_datadir}/dbus-1/system.d/org.freedesktop.UDisks2.conf
%{_datadir}/bash-completion/completions/udisksctl
%{_datadir}/zsh/site-functions/_udisks2
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/udisks2.service
%{_udevrulesdir}/80-udisks2.rules
%{_sbindir}/umount.udisks2


%dir %{_libdir}/udisks2
%dir %{_libdir}/udisks2/modules
%dir %{_libexecdir}/udisks2
%{_libexecdir}/udisks2/udisksd

%{_bindir}/udisksctl

%{_mandir}/man1/udisksctl.1*
%{_mandir}/man5/udisks2.conf.5*
%{_mandir}/man8/udisksd.8*
%{_mandir}/man8/udisks.8*
%{_mandir}/man8/umount.udisks2.8*

%{_datadir}/polkit-1/actions/org.freedesktop.UDisks2.policy
%{_datadir}/dbus-1/system-services/org.freedesktop.UDisks2.service

# Permissions for local state data are 0700 to avoid leaking information
# about e.g. mounts to unprivileged users
%attr(0700,root,root) %dir %{_localstatedir}/lib/udisks2

%files -n lib%{name}
%{_libdir}/libudisks2.so.*
%{_libdir}/girepository-1.0/UDisks-2.0.typelib

%files -n %{name}-lvm2
%{_libdir}/udisks2/modules/libudisks2_lvm2.so
%{_datadir}/polkit-1/actions/org.freedesktop.UDisks2.lvm2.policy

%files -n %{name}-iscsi
%{_libdir}/udisks2/modules/libudisks2_iscsi.so
%{_datadir}/polkit-1/actions/org.freedesktop.UDisks2.iscsi.policy

%files -n lib%{name}-devel
%{_libdir}/libudisks2.so
%dir %{_includedir}/udisks2
%dir %{_includedir}/udisks2/udisks
%{_includedir}/udisks2/udisks/*.h
%{_datadir}/gir-1.0/UDisks-2.0.gir
%if %{with_gtk_doc}
%dir %{_datadir}/gtk-doc/html/udisks2
%{_datadir}/gtk-doc/html/udisks2/*
%endif
%{_libdir}/pkgconfig/udisks2.pc
%{_libdir}/pkgconfig/udisks2-lvm2.pc
%{_libdir}/pkgconfig/udisks2-iscsi.pc
%if 0%{?with_btrfs}
%{_libdir}/pkgconfig/udisks2-btrfs.pc
%endif
%if 0%{?with_lsm}
%{_libdir}/pkgconfig/udisks2-lsm.pc
%endif

%if 0%{?with_btrfs}
%files -n %{name}-btrfs
%{_libdir}/udisks2/modules/libudisks2_btrfs.so
%{_datadir}/polkit-1/actions/org.freedesktop.UDisks2.btrfs.policy
%endif

%if 0%{?with_lsm}
%files -n %{name}-lsm
%dir %{_sysconfdir}/udisks2/modules.conf.d
%{_libdir}/udisks2/modules/libudisks2_lsm.so
%{_mandir}/man5/udisks2_lsm.conf.*
%{_datadir}/polkit-1/actions/org.freedesktop.UDisks2.lsm.policy
%attr(0600,root,root) %{_sysconfdir}/udisks2/modules.conf.d/udisks2_lsm.conf
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.11.1-1
- Prepare for Oreon 11 (RP1)
