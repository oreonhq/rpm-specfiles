%global source0_hash 3d1e87cbcf22a1ed548f0fb0bdb9a1dbd3b4dcea0d23fd84444bd1673050b201

Name:		driverctl
Version:	0.121
Release:	%autorelease
Summary:	Device driver control utility

License:	LGPL-2.1-or-later
URL:		https://gitlab.com/driverctl/driverctl
BuildArch:	noarch

Source0:        https://gitlab.com/driverctl/driverctl/-/archive/0.121/driverctl-0.121.tar.bz2

# for udev macros
BuildRequires: systemd
BuildRequires: make
Requires(post,postun): %{_sbindir}/udevadm
Requires: coreutils udev

%description
driverctl is a tool for manipulating and inspecting the system
device driver choices.

Devices are normally assigned to their sole designated kernel driver
by default. However in some situations it may be desireable to
override that default, for example to try an older driver to
work around a regression in a driver or to try an experimental alternative
driver. Another common use-case is pass-through drivers and driver
stubs to allow userspace to drive the device, such as in case of
virtualization.

driverctl integrates with udev to support overriding
driver selection for both cold- and hotplugged devices from the
moment of discovery, but can also change already assigned drivers,
assuming they are not in use by the system. The driver overrides
created by driverctl are persistent across system reboots
by default.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q

%install
%make_install PREFIX=%{_prefix} SBINDIR=%{_sbindir}

%files
%license COPYING
%doc README TODO
%{_sbindir}/driverctl
%{_udevrulesdir}/*.rules
%{_udevrulesdir}/../vfio_name
%{_unitdir}/driverctl@.service
%dir %{_sysconfdir}/driverctl.d
%{_datadir}/bash-completion/
%{_mandir}/man8/driverctl.8*

%post
%udev_rules_update

%postun
%udev_rules_update

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.121-1
- Prepare for Oreon 11 (RP1)
