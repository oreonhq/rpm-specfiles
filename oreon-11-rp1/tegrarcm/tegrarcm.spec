%global source0_hash 5ecd58cf3eaca00e856309e6604dc826b7f2a35096b2882b7d42654f7717d722
%global gitcommit0 debbac012a3f67bd0864a0f4ad8bfe8e4e57844e
Name:           tegrarcm
Version:        1.9
Release:        1%{?dist}
Summary:        Send code to a Tegra device in recovery mode
License:        BSD-3-Clause AND LicenseRef-Fedora-Firmware
URL:            https://gitlab.com/grate-driver/tegrarcm
Source0:        https://gitlab.com/grate-driver/%{name}/-/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libcryptopp)
BuildRequires:  pkgconfig(libusb-1.0)
# /oreon:deps
%description
This program is used to send code to a Tegra device in recovery mode.
It does not supported locked devices with an encrypted boot key, only
open devices such as the ventana, cardhu, or dalmore reference boards.
It is not capable of flashing firmware to a device, but can be used to
download firmware that is then capable of flashing.  For example in
ChromeOS tegrarcm is used to download a special build of u-boot to the
target Tegra device with a payload that it then flashes to the boot
device.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-v%{version}-%{gitcommit0}
./autogen.sh

%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
