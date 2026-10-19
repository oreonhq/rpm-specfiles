%global source0_hash 99e4a4b8c245479dd5c5d473a031acb67d752b94dcd76be172279cd445845421
Name:    device-mapper-multipath
Version: 0.15.1
Release:        1%{?dist}
Summary:        Tools to manage multipath devices using device-mapper
License: GPL-2.0-only AND GPL-3.0-only
URL:     http://christophe.varoqui.free.fr/
Source0:        https://github.com/opensvc/multipath-tools/archive/refs/tags/%{version}.tar.gz#/multipath-tools-%{version}.tgz
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
Requires: %{name}-libs = %{version}-%{release}
Requires: kpartx = %{version}-%{release}
Requires: device-mapper >= 1.02.96
Requires: userspace-rcu
Requires: readline
Requires: libmount
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
Conflicts: mdadm < 4.1-rc2.0.2
Conflicts: udisks2 < 2.8.0-2
# oreon:deps
BuildRequires:  device-mapper-devel
BuildRequires:  gcc
BuildRequires:  json-c-devel
BuildRequires:  libaio-devel
BuildRequires:  libmount-devel
BuildRequires:  libselinux-devel
BuildRequires:  libsepol-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-units
BuildRequires:  userspace-rcu-devel
# /oreon:deps
%description
%{name} provides tools to manage multipath devices by
instructing the device-mapper multipath kernel module what to do. 
The tools are :
* multipath - Scan the system for multipath devices and assemble them.
* multipathd - Detects when paths fail and execs multipath to update things.

%package libs
Summary: The %{name} modules and shared library
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n multipath-tools-%{version} -p1
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
install -d %{buildroot}/etc/multipath
rm -rf %{buildroot}/%{_initrddir}
%oreon_autofiles kpartx usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles libdmmp usr/*/lib*.so.*
%oreon_autofiles libdmmp-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

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

/bin/systemctl --quiet is-enabled multipathd.service >/dev/null 2>&1 && /bin/systemctl reenable multipathd.service ||:
%files -f %{oreon_filedir}/main.list
%files -n device-mapper-multipath-libs -f %{oreon_filedir}/device-mapper-multipath-libs.list
%files -n device-mapper-multipath-devel -f %{oreon_filedir}/device-mapper-multipath-devel.list
%files -n kpartx -f %{oreon_filedir}/kpartx.list
%files -n libdmmp -f %{oreon_filedir}/libdmmp.list
%files -n libdmmp-devel -f %{oreon_filedir}/libdmmp-devel.list

%changelog

%autochangelog
