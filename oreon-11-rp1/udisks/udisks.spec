%global source0_hash f2ec82eb0ea7e01dc299b5b29b3c18cdf861236ec43dcff66b3552b4b31c6f71

%global dbus_version 1.2
%global dbus_glib_version 0.82
%global glib2_version 2.15.0
%global gudev_version 147
%global polkit_version 0.97
%global parted_version 1.8.8
%global udev_version 143
%global mdadm_version 2.6.7
%global device_mapper_version 1.02
%global libatasmart_version 0.14
%global sg3_utils_version 1.27
%global smp_utils_version 0.94
%global systemd_version 185

Summary: Storage Management Service
Name: udisks
Version: 1.0.5
Release: 31%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://www.freedesktop.org/wiki/Software/udisks
Source0: http://hal.freedesktop.org/releases/%{name}-%{version}.tar.gz
# https://bugs.freedesktop.org/show_bug.cgi?id=90778
Patch0:  udisks-1.0.5-fix-build-with-glibc-2.20.patch
Patch1:  fix_bash_completion.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=1238664
Patch2:  udisks-1.0.5-fix-service-file.patch
Patch3:  udisks-1.0.5-fix-makedev-failure.patch
BuildRequires: make
BuildRequires: pkgconfig(gio-unix-2.0) >= %{glib2_version}
BuildRequires: pkgconfig(dbus-1)  >= %{dbus_version}
BuildRequires: pkgconfig(dbus-glib-1) >= %{dbus_glib_version}
BuildRequires: pkgconfig(polkit-gobject-1) >= %{polkit_version}
BuildRequires: parted-devel >= %{parted_version}
BuildRequires: pkgconfig(devmapper) >= %{device_mapper_version}
BuildRequires: pkgconfig(libudev) >= %{udev_version}
BuildRequires: intltool
BuildRequires: pkgconfig(libatasmart) >= %{libatasmart_version}
BuildRequires: pkgconfig(gudev-1.0) >= %{gudev_version}
%if 0%{?fedora} > 17 || 0%{?rhel} > 6
BuildRequires: pkgconfig(systemd) >= %{systemd_version}
%else
BuildRequires: pkgconfig(libudev) >= %{udev_version}
%endif
BuildRequires: sg3_utils-devel >= %{sg3_utils_version}
BuildRequires: gtk-doc
# Needed for patch 3.
BuildRequires: autoconf automake libtool
BuildRequires: systemd
# needed to pull in the system bus daemon
Requires: dbus >= %{dbus_version}
# needed to pull in the udev daemon
Requires: udev >= %{udev_version}
# we need at least this version for bugfixes / features etc.
Requires: libatasmart >= %{libatasmart_version}
Requires: mdadm >= %{mdadm_version}
# for smp_rep_manufacturer
Requires: smp_utils >= %{smp_utils_version}
# for mount, umount, mkswap
Requires: util-linux
# for mkfs.ext3, mkfs.ext3, e2label
Requires: e2fsprogs
# for mkfs.xfs, xfs_admin
Requires: xfsprogs
# for mkfs.vfat
Requires: dosfstools
# for mlabel
Requires: mtools
# For ejecting removable disks
Requires: eject
# for mkntfs - no ntfsprogs on ppc, though
%ifnarch ppc ppc64
Requires: ntfsprogs
%endif
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

# for /proc/self/mountinfo, only available in 2.6.26 or higher
Conflicts: kernel < 2.6.26

# Obsolete and Provide DeviceKit-disks - udisks provides exactly the same
# ABI just with a different name and versioning-scheme
#
Obsoletes: DeviceKit-disks <= 009
Provides: DeviceKit-disks = 010

%description
udisks provides a daemon, D-Bus API and command line tools
for managing disks and storage devices.

%package devel
Summary: D-Bus interface definitions for udisks
Requires: %{name} = %{version}-%{release}

# See comment above
#
Obsoletes: DeviceKit-disks-devel <= 009
Provides: DeviceKit-disks-devel = 010

%description devel
D-Bus interface definitions and documentation for udisks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

# https://bugzilla.redhat.com/show_bug.cgi?id=673544#c15
rm -f src/*-glue.h tools/*-glue.h

autoreconf --force --install

%build
%configure --enable-gtk-doc
%make_build

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a

# for now, include a compat symlink for the command-line tool
# and man page
ln -s udisks $RPM_BUILD_ROOT%{_bindir}/devkit-disks
ln -s udisks.1 $RPM_BUILD_ROOT%{_datadir}/man/man1/devkit-disks.1

# TODO: should be fixed upstream
chmod 0644 $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/udisks-bash-completion.sh
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
mv $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/udisks-bash-completion.sh \
    $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d

%find_lang %{name}

%post
%systemd_post udisks.service

%preun
%systemd_preun udisks.service

%postun
%systemd_postun_with_restart udisks.service

%files -f %{name}.lang
%doc README AUTHORS NEWS HACKING doc/TODO
%license COPYING
%{_sysconfdir}/avahi/services/udisks.service
%{_sysconfdir}/bash_completion.d/udisks-bash-completion.sh
%{_sysconfdir}/dbus-1/system.d/*.conf
/lib/udev/rules.d/*.rules

/lib/udev/udisks-part-id
/lib/udev/udisks-dm-export
/lib/udev/udisks-probe-ata-smart
/lib/udev/udisks-probe-sas-expander
/sbin/umount.udisks

%{_bindir}/*
%{_libexecdir}/*
%{_mandir}/man1/*.1*
%{_mandir}/man7/%{name}.7*
%{_mandir}/man8/%{name}-daemon.8*
%{_datadir}/polkit-1/actions/*.policy

%{_datadir}/dbus-1/system-services/*.service
%{_unitdir}/udisks.service

%attr(0700,root,root) %dir %{_localstatedir}/lib/udisks

%files devel
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/pkgconfig/udisks.pc
%{_datadir}/gtk-doc

%changelog
%autochangelog
