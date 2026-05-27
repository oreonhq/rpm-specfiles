%global source0_hash none

Summary:    X.Org X11 driver installation package
Name:       xorg-x11-drivers
Version:    2022
Release:    11%{?dist}
License:    MIT

Requires:   xorg-x11-drv-dummy
Requires:   xorg-x11-drv-evdev
Requires:   xorg-x11-drv-libinput

%if !0%{?rhel}

%ifnarch aarch64 s390x
Requires:   xorg-x11-drv-qxl
%endif

# only non-s390x
%ifnarch s390x
Requires:   xorg-x11-drv-ati
Requires:   xorg-x11-drv-nouveau
Requires:   xorg-x11-drv-wacom
%endif

%ifarch %{ix86} x86_64
Requires:   xorg-x11-drv-intel
Requires:   xorg-x11-drv-vmware
Requires:   xorg-x11-drv-openchrome
%endif

%endif

%description
The purpose of this package is to require all of the individual X.Org driver
rpms, to allow the OS installation software to install all drivers all at once,
without having to track which individual drivers are present on each
architecture.  By installing this package, it forces all of the individual
driver packages to be installed.

%files

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2022-11
- Prepare for Oreon 11 (RP1)
