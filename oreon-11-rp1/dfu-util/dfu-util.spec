%global source0_hash b4b53ba21a82ef7e3d4c47df2952adf5fa494f499b6b0b57c58c5d04ae8ff19e
Name:          dfu-util
Version:       0.11
Release:        13%{?dist}
Summary:        USB Device Firmware Upgrade tool
License:       GPL-2.0-or-later
URL:            http://dfu-util.sourceforge.net/
Source0:        http://dfu-util.sourceforge.net/releases/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libusb1-devel
BuildRequires:  make
# /oreon:deps
%description
USB Device Firmware Upgrade (DFU) is an official USB device class specification 
of the USB Implementers Forum. It specifies a vendor and device independent way 
of updating the firmware of a USB device. The idea is to have only one 
vendor-independent firmware update tool as part of the operating system, which 
can then (given a particular firmware image) be downloaded into the device. 

In addition to firmware download, it also specifies firmware upload, i.e.
loading the currently installed device firmware to the USB Host.

The DFU specification can be found at:
 http://www.usb.org/developers/devclass_docs/usbdfu10.pdf

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%{make_build}
%install
%{make_install}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
