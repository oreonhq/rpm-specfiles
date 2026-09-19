%global source0_hash 404bc9921ba9b726d29ce2f2ba9ad131f90198c15b78ec1438095ae172d6165c

%define usb_version 0.1

Name:           atmel-firmware
Version:        1.3
Release:        37%{?dist}
Summary:        Firmware for Atmel at76c50x wireless network chips

License:        LicenseRef-Fedora-Firmware
URL:            http://at76c503a.berlios.de/
Source0:        http://www.thekelleys.org.uk/atmel/atmel-firmware-%{version}.tar.gz
Source1:        http://download.berlios.de/at76c503a/at76_usb-firmware-%{usb_version}.tar.gz

BuildArch:      noarch
BuildRequires:  xz

%description
The drivers for Atmel at76c50x wireless network chips in the Linux kernel
but do not include the firmware.
This firmware needs to be loaded by the host on most cards using these chips.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q 
%setup -q -D -T -a 1 
install -pm 0644 at76_usb-firmware-%{usb_version}/COPYRIGHT COPYRIGHT-usb
install -pm 0644 at76_usb-firmware-%{usb_version}/README README-usb

%build
# Nothing to build

%install
mkdir -p $RPM_BUILD_ROOT/lib/firmware

install -pm 0644 images/*.bin $RPM_BUILD_ROOT/lib/firmware
install -pm 0644 at76_usb-firmware-%{usb_version}/*.bin $RPM_BUILD_ROOT/lib/firmware
xz -C crc32 $RPM_BUILD_ROOT/lib/firmware/atmel*

%files
%license COPYING COPYRIGHT-usb
%doc README README-usb
/lib/firmware/*xz

%changelog
%autochangelog
