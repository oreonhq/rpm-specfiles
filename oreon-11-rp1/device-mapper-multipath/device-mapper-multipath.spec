%global source0_hash none

Name:    device-mapper-multipath
Version: 0.13.1
Release: 1%{?dist}
Summary: Tools to manage multipath devices using device-mapper
# readline uses GPL-3.0-only
License: GPL-2.0-only AND GPL-3.0-only
URL:     http://christophe.varoqui.free.fr/

# The source for this package was pulled from upstream's git repo.  Use the
# following command to generate the tarball
# curl -L https://github.com/opensvc/multipath-tools/archive/0.13.1.tar.gz -o multipath-tools-0.13.1.tgz
Source0: multipath-tools-0.13.1.tgz
Source1: multipath.conf
Patch0001: 0001-RH-fixup-udev-rules-for-redhat.patch
Patch0002: 0002-RH-Remove-the-property-blacklist-exception-builtin.patch
Patch0003: 0003-RH-don-t-start-without-a-config-file.patch
Patch0004: 0004-RH-Fix-nvme-function-missing-argument.patch
Patch0005: 0005-RH-use-rpm-optflags-if-present.patch
Patch0006: 0006-RH-add-mpathconf.patch
Patch0007: 0007-RH-add-wwids-from-kernel-cmdline-mpath.wwids-with-A.patch
Patch0008: 0008-RH-reset-default-find_mutipaths-value-to-off.patch
Patch0009: 0009-RH-attempt-to-get-ANA-info-via-sysfs-first.patch
Patch0010: 0010-RH-make-parse_vpd_pg83-match-scsi_id-output.patch
Patch0011: 0011-RH-add-scsi-device-handlers-to-modules-load.d.patch
Patch0012: 0012-RH-compile-with-libreadline-support.patch
Patch0013: 0013-RH-Add-mpathcleanup.patch

# runtime
Requires: %{name}-libs = %{version}-%{release}
Requires: kpartx = %{version}-%{release}
Requires: device-mapper >= 1.02.96
Requires: userspace-rcu
Requires: readline
Requires: libmount
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
# Starting with 0.7.7-1, 62-multipath.rules changed in a way that is
# incompatible with 65-md-incremental.rules in earlier mdadm packages.
# Later mdadm packages are compatible with any version of
# device-mapper-multipath. See bz #1628192 for more details
Conflicts: mdadm < 4.1-rc2.0.2
# Starting with 0.7.7-1, 62-multipath.rules changed in a way that is
# incompatible with 80-udisks2.rules in earlier udisks2 packages.
# Later udisks2 packages are compatible with any version of
# device-mapper-multipath. See bz #1628192 for more details
Conflicts: udisks2 < 2.8.0-2

# build/setup
BuildRequires: libaio-devel, device-mapper-devel >= 1.02.89
BuildRequires: libselinux-devel, libsepol-devel
BuildRequires: readline-devel, ncurses-devel
BuildRequires: systemd-units, systemd-devel
BuildRequires: json-c-devel, perl-interpreter, pkgconfig, gcc
BuildRequires: userspace-rcu-devel
BuildRequires: libmount-devel
BuildRequires: make

%description
%{name} provides tools to manage multipath devices by
instructing the device-mapper multipath kernel module what to do. 
The tools are :
* multipath - Scan the system for multipath devices and assemble them.
* multipathd - Detects when paths fail and execs multipath to update things.

%package libs
Summary: The %{name} modules and shared library
# only libmpathcmd is LGPL-2.1-or-later AND LGPL-2.0-or-later
License: GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-2.0-or-later

%description libs
The %{name}-libs provides the path checker
and prioritizer modules. It also contains the libmpathpersist and
libmpathcmd shared libraries, as well as multipath's internal library,
libmultipath.

%package devel
Summary: Development libraries and headers for %{name}
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libs = %{version}-%{release}

%description devel
This package contains the files need to develop applications that use
device-mapper-multipath's lbmpathpersist and libmpathcmd libraries.

%package -n kpartx
Summary: Partition device manager for device-mapper devices

%description -n kpartx
kpartx manages partition creation and removal for device-mapper devices.

%package -n libdmmp
Summary: device-mapper-multipath C API library
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
Requires: json-c
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libs = %{version}-%{release}

%description -n libdmmp
This package contains the shared library for the device-mapper-multipath
C API library.

%package -n libdmmp-devel
Summary: device-mapper-multipath C API library headers
Requires: pkgconfig
Requires: libdmmp = %{version}-%{release}

%description -n libdmmp-devel
This package contains the files needed to develop applications that use
device-mapper-multipath's libdmmp C API library

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n multipath-tools-0.13.1 -p1
cp %{SOURCE1} .

%build
%define _libdir /usr/%{_lib}
%define _libmpathdir %{_libdir}/multipath
%define _pkgconfdir %{_libdir}/pkgconfig
%make_build LIB=%{_lib}

%install
%make_install \
	bindir=%{_sbindir} \
	syslibdir=%{_libdir} \
	usrlibdir=%{_libdir} \
	plugindir=%{_libmpathdir} \
	mandir=%{_mandir} \
	unitdir=%{_unitdir} \
	includedir=%{_includedir} \
	pkgconfdir=%{_pkgconfdir} \
	tmpfilesdir=%{_tmpfilesdir}

# tree fix up
install -d %{buildroot}/etc/multipath
rm -rf %{buildroot}/%{_initrddir}


%post
%systemd_post multipathd.service

%preun
%systemd_preun multipathd.service

%postun
if [ $1 -ge 1 ] ; then
	multipathd forcequeueing daemon > /dev/null 2>&1 || :
fi
%systemd_postun_with_restart multipathd.service

%triggerun -- %{name} < 0.4.9-37
# make sure old systemd symlinks are removed after changing the [Install]
# section in multipathd.service from multi-user.target to sysinit.target
/bin/systemctl --quiet is-enabled multipathd.service >/dev/null 2>&1 && /bin/systemctl reenable multipathd.service ||:

%files
%license LICENSES/GPL-2.0 LICENSES/LGPL-2.0 LICENSES/GPL-3.0
%{_sbindir}/multipath
%{_sbindir}/multipathd
%{_sbindir}/multipathc
%{_sbindir}/mpathconf
%{_sbindir}/mpathcleanup
%{_sbindir}/mpathpersist
%{_unitdir}/multipathd.service
%{_unitdir}/multipathd-queueing.service
%{_unitdir}/multipathd.socket
%{_mandir}/man5/multipath.conf.5*
%{_mandir}/man8/multipath.8*
%{_mandir}/man8/multipathd.8*
%{_mandir}/man8/multipathc.8*
%{_mandir}/man8/mpathconf.8*
%{_mandir}/man8/mpathpersist.8*
%config /usr/lib/udev/rules.d/62-multipath.rules
%config /usr/lib/udev/rules.d/11-dm-mpath.rules
%config /usr/lib/udev/rules.d/99-z-dm-mpath-late.rules
%dir %{_modulesloaddir}
%{_modulesloaddir}/scsi_dh.conf
%{_tmpfilesdir}/multipath.conf
%doc README.md
%doc multipath.conf
%dir /etc/multipath

%files libs
%license LICENSES/GPL-2.0 LICENSES/LGPL-2.0 LICENSES/LGPL-2.1
%doc README.md
%{_libdir}/libmultipath.so
%{_libdir}/libmultipath.so.*
%{_libdir}/libmpathutil.so
%{_libdir}/libmpathutil.so.*
%{_libdir}/libmpathpersist.so.*
%{_libdir}/libmpathcmd.so.*
%{_libdir}/libmpathvalid.so.*
%dir %{_libmpathdir}
%{_libmpathdir}/*

%ldconfig_scriptlets libs

%files devel
%doc README.md
%{_libdir}/libmpathpersist.so
%{_libdir}/libmpathcmd.so
%{_libdir}/libmpathvalid.so
%{_includedir}/mpath_cmd.h
%{_includedir}/mpath_persist.h
%{_includedir}/mpath_valid.h
%{_mandir}/man3/mpath_persistent_reserve_in.3*
%{_mandir}/man3/mpath_persistent_reserve_out.3*

%files -n kpartx
%license LICENSES/GPL-2.0
%doc README.md
%{_sbindir}/kpartx
/usr/lib/udev/kpartx_id
%{_mandir}/man8/kpartx.8*
%config /usr/lib/udev/rules.d/11-dm-parts.rules
%config /usr/lib/udev/rules.d/66-kpartx.rules
%config /usr/lib/udev/rules.d/68-del-part-nodes.rules

%files -n libdmmp
%license LICENSES/GPL-3.0
%doc README.md
%{_libdir}/libdmmp.so.*

%ldconfig_scriptlets -n libdmmp

%files -n libdmmp-devel
%doc README.md
%{_libdir}/libdmmp.so
%dir %{_includedir}/libdmmp
%{_includedir}/libdmmp/*
%{_mandir}/man3/dmmp_*
%{_mandir}/man3/libdmmp.h.3*
%{_pkgconfdir}/libdmmp.pc

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.13.1-1
- Import
