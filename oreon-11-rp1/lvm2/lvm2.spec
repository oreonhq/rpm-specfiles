%global source0_hash d87ec0dac9061f1fa58ebced5c6b1360c87d4c5cd7b455dc0ebe1d3f036920d7
%global device_mapper_version 1.02.213
%global enable_cache 1
%global enable_lvmdbusd 1
%global enable_lvmlockd 1
%global enable_lvmpolld 1
%global enable_thin 1
%global enable_dmfilemapd 1
%global enable_testsuite 1
%global enable_vdo 1
%global enable_writecache 1
%global enable_integrity 1
%if 0%{?oreon} >= 11
%global system_release_version 11
%else
%global system_release_version 23
%endif
%global systemd_version 256~rc1
%global dracut_version 002-18
%global util_linux_version 2.24
%global bash_version 4.0
%global dlm_version 4.0.6-1
%global libselinux_version 1.30.19-4
%global persistent_data_version 0.7.0-0.1.rc6
%global sanlock_version 5.0.0-1
%global enable_lockd_sanlock %{enable_lvmlockd}
%global enable_lockd_dlm %{enable_lvmlockd}
Summary:        Userland logical volume management tools
Name: lvm2
Version: 2.03.43
Release:        1%{?dist}
License: GPL-2.0-only
URL: https://sourceware.org/lvm2
Source0:        https://sourceware.org/pub/lvm2/releases/LVM2.%{version}.tgz
%if %{enable_thin} || %{enable_cache}
%endif
%if %{enable_lockd_sanlock}
%endif
Requires: %{name}-libs = %{?epoch}:%{version}-%{release}
%if 0%{?fedora} || 0%{?oreon}
Requires(post): (system-release >= %{system_release_version} if system-release)
%endif
Requires: bash >= %{bash_version}
Requires(post): systemd-units >= %{systemd_version}
Requires(preun): systemd-units >= %{systemd_version}
Requires(postun): systemd-units >= %{systemd_version}
Requires: module-init-tools
%if %{enable_thin} || %{enable_cache}
Requires: device-mapper-persistent-data >= %{persistent_data_version}
%endif
%if "%{_sbindir}" == "%{_bindir}"
Requires:       filesystem(unmerged-sbin-symlinks)
Provides:       /usr/sbin/lvm
%endif
# oreon:deps
BuildRequires:  device-mapper-persistent-data
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libaio-devel
BuildRequires:  libblkid-devel
BuildRequires:  libedit-devel
BuildRequires:  libnvme-devel
BuildRequires:  libselinux-devel
BuildRequires:  libsepol-devel
BuildRequires:  make
BuildRequires:  module-init-tools
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-dbus
BuildRequires:  python3-devel
BuildRequires:  python3-pyudev
BuildRequires:  python3-setuptools
BuildRequires:  sanlock-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-units
BuildRequires:  xfsprogs-devel
# /oreon:deps
%description
LVM2 includes all of the support for handling read/write operations on
physical volumes (hard disks, RAID-Systems, magneto optical, etc.,
multiple devices (MD), see mdadm(8) or even loop devices, see
losetup(8)), creating volume groups (kind of virtual disks) from one
or more physical volumes and creating one or more logical volumes
(kind of logical partitions) in volume groups.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir LVM2.%{version}
%oreon_prep
%build

%global _default_pid_dir /run
%global _default_dm_run_dir /run
%global _default_run_dir /run/lvm
%global _default_locking_dir /run/lock/lvm
%global _udevdir %{_prefix}/lib/udev/rules.d
%configure \
  --with-default-dm-run-dir=%{_default_dm_run_dir} \
  --with-default-run-dir=%{_default_run_dir} \
  --with-default-pid-dir=%{_default_pid_dir} \
  --with-default-locking-dir=%{_default_locking_dir} \
  --with-usrlibdir=%{_libdir} \
  --enable-fsadm \
  --enable-write_install \
  --with-user= \
  --with-group= \
  --with-device-uid=0 \
  --with-device-gid=6 \
  --with-device-mode=0660 \
  --enable-pkgconfig \
  --enable-cmdlib \
  --enable-dmeventd \
  --enable-blkid_wiping \
  --with-udevdir=%{_udevdir} --enable-udev_sync \
  --with-thin=internal \
  --with-cache=internal \
  --enable-lvmpolld \
%if %{enable_lockd_sanlock}
  --enable-lvmlockd-sanlock \
%endif
  --enable-dbus-service --enable-notify-dbus \
  --enable-dmfilemapd \
  --with-writecache=internal \
  --with-vdo=internal --with-vdo-format=%{_bindir}/vdoformat \
  --with-integrity=internal \
  --with-default-use-devices-file=1 \
  --disable-silent-rules \
  --enable-app-machineid \
  --enable-editline \
  --disable-readline
V=1 %make_build
%install
V=1 %make_install
V=1 make install_system_dirs DESTDIR=$RPM_BUILD_ROOT
V=1 make install_systemd_units DESTDIR=$RPM_BUILD_ROOT
V=1 make install_systemd_generators DESTDIR=$RPM_BUILD_ROOT
V=1 make install_tmpfiles_configuration DESTDIR=$RPM_BUILD_ROOT
%make_install -C test
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post blk-availability.service lvm2-monitor.service
if [ "$1" = "1" ] ; then
	systemctl enable lvm2-monitor.service
	systemctl start lvm2-monitor.service >/dev/null 2>&1 || :
fi
%systemd_post lvm2-lvmpolld.socket
systemctl enable lvm2-lvmpolld.socket
systemctl start lvm2-lvmpolld.socket >/dev/null 2>&1 || :
%preun

%systemd_preun blk-availability.service lvm2-monitor.service
%systemd_preun lvm2-lvmpolld.service lvm2-lvmpolld.socket
%postun

%systemd_postun lvm2-monitor.service
%systemd_postun_with_restart lvm2-lvmpolld.service
%triggerun -- %{name} < 2.02.86-2

%{_bindir}/systemd-sysv-convert --save lvm2-monitor >/dev/null 2>&1 || :
/bin/systemctl --no-reload enable lvm2-monitor.service > /dev/null 2>&1 || :
/sbin/chkconfig --del lvm2-monitor > /dev/null 2>&1 || :
/bin/systemctl try-restart lvm2-monitor.service > /dev/null 2>&1 || :
%package devel
Summary: Development libraries and headers
License: LGPL-2.1-only
Requires: %{name} = %{?epoch}:%{version}-%{release}
Requires: device-mapper-devel = %{?epoch}:%{device_mapper_version}-%{release}
Requires: device-mapper-event-devel = %{?epoch}:%{device_mapper_version}-%{release}
Requires: pkgconfig
%description devel
This package contains files needed to develop applications that use
the lvm2 libraries.

%{_bindir}/dmvdostats
%{_mandir}/man8/dmvdostats.8.gz
%package libs
Summary: Shared libraries for lvm2
License: LGPL-2.1-only
Requires: device-mapper-event = %{?epoch}:%{device_mapper_version}-%{release}
%description libs
This package contains shared lvm2 libraries for applications.

%ldconfig_scriptlets libs

%package lockd
Summary: LVM locking daemon
Requires: lvm2 = %{?epoch}:%{version}-%{release}
%if %{enable_lockd_sanlock}
Requires: sanlock-lib >= %{sanlock_version}
%endif
Requires(post): systemd-units >= %{systemd_version}
Requires(preun): systemd-units >= %{systemd_version}
Requires(postun): systemd-units >= %{systemd_version}
%description lockd

LVM commands use lvmlockd to coordinate access to shared storage.

%post lockd

%systemd_post lvmlockd.service lvmlocks.service
%preun lockd

%systemd_preun lvmlockd.service lvmlocks.service
%postun lockd

%systemd_postun lvmlockd.service lvmlocks.service
%package dbusd
Summary: LVM2 D-Bus daemon
License: GPL-2.0-only
BuildArch: noarch
Requires: lvm2 >= %{?epoch}:%{version}-%{release}
Requires: dbus
Requires: python3-dbus
Requires: python3-pyudev
Requires: python3-gobject-base
Requires(post): systemd-units >= %{systemd_version}
Requires(preun): systemd-units >= %{systemd_version}
Requires(postun): systemd-units >= %{systemd_version}
%description dbusd

Daemon for access to LVM2 functionality through a D-Bus interface.

%post dbusd

%systemd_post lvm2-lvmdbusd.service
%preun dbusd

%systemd_preun lvm2-lvmdbusd.service
%postun dbusd

%systemd_postun lvm2-lvmdbusd.service
%package -n device-mapper
Summary: Device mapper utility
Version: %{device_mapper_version}
License: GPL-2.0-only
URL: https://www.sourceware.org/dm/
Requires: device-mapper-libs = %{?epoch}:%{device_mapper_version}-%{release}
Requires: util-linux-core >= %{util_linux_version}
Requires: systemd >= %{systemd_version}
Conflicts: dracut < %{dracut_version}
%description -n device-mapper
This package contains the supporting userspace utility, dmsetup,
for the kernel device-mapper.

%package -n device-mapper-devel
Summary: Development libraries and headers for device-mapper
Version: %{device_mapper_version}
License: LGPL-2.1-only
Requires: device-mapper = %{?epoch}:%{device_mapper_version}-%{release}
Requires: pkgconfig
%description -n device-mapper-devel
This package contains files needed to develop applications that use
the device-mapper libraries.

%package -n device-mapper-libs
Summary: Device-mapper shared library
Version: %{device_mapper_version}
License: LGPL-2.1-only
Requires: device-mapper = %{?epoch}:%{device_mapper_version}-%{release}
%description -n device-mapper-libs
This package contains the device-mapper shared library, libdevmapper.

%ldconfig_scriptlets -n device-mapper-libs

%package -n device-mapper-event
Summary: Device-mapper event daemon
Version: %{device_mapper_version}
Requires: device-mapper = %{?epoch}:%{device_mapper_version}-%{release}
Requires: device-mapper-event-libs = %{?epoch}:%{device_mapper_version}-%{release}
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
%description -n device-mapper-event
This package contains the dmeventd daemon for monitoring the state
of device-mapper devices.

%post -n device-mapper-event

%systemd_post dm-event.socket
systemctl enable dm-event.socket
systemctl start dm-event.socket >/dev/null 2>&1 || :
if [ -e %{_default_pid_dir}/dmeventd.pid ]; then
	%{_sbindir}/dmeventd -R || echo "Failed to restart dmeventd daemon. Please, try manual restart."
fi
%preun -n device-mapper-event

%systemd_preun dm-event.service dm-event.socket
%package -n device-mapper-event-libs
Summary: Device-mapper event daemon shared library
Version: %{device_mapper_version}
License: LGPL-2.1-only
%description -n device-mapper-event-libs
This package contains the device-mapper event daemon shared library,
libdevmapper-event.

%ldconfig_scriptlets -n device-mapper-event-libs

%package -n device-mapper-event-devel
Summary: Development libraries and headers for the device-mapper event daemon
Version: %{device_mapper_version}
License: LGPL-2.1-only
Requires: device-mapper-event = %{?epoch}:%{device_mapper_version}-%{release}
Requires: pkgconfig
%description -n device-mapper-event-devel
This package contains files needed to develop applications that use
the device-mapper event library.

%package testsuite
Summary: LVM2 Testsuite
License: GPL-2.0-only AND LGPL-2.1-only AND BSD-2-Clause
%description testsuite
An extensive functional testsuite for LVM2.

%files -f %{oreon_filedir}/main.list
%files -n lvm2-devel -f %{oreon_filedir}/lvm2-devel.list
%files -n lvm2-libs -f %{oreon_filedir}/lvm2-libs.list
%files -n lvm2-lockd -f %{oreon_filedir}/lvm2-lockd.list
%files -n lvm2-dbusd -f %{oreon_filedir}/lvm2-dbusd.list
%files -n device-mapper -f %{oreon_filedir}/device-mapper.list
%files -n device-mapper-devel -f %{oreon_filedir}/device-mapper-devel.list
%files -n device-mapper-libs -f %{oreon_filedir}/device-mapper-libs.list
%files -n device-mapper-event -f %{oreon_filedir}/device-mapper-event.list
%files -n device-mapper-event-libs -f %{oreon_filedir}/device-mapper-event-libs.list
%files -n device-mapper-event-devel -f %{oreon_filedir}/device-mapper-event-devel.list
%files -n lvm2-testsuite -f %{oreon_filedir}/lvm2-testsuite.list

%changelog

%autochangelog
