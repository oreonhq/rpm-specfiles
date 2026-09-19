%global source0_hash f11d3810d7f72833997f634584a586dcced71a353f965abf81062ec431d02b12

Name:		zd1211-firmware
Version:	1.5
Release:	20%{?dist}
Summary:	Firmware for wireless devices based on zd1211 chipset
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		http://zd1211.wiki.sourceforge.net
Source0:	http://downloads.sourceforge.net/zd1211/zd1211-firmware-%{version}.tar.bz2
Patch0:		zd1211-firmware-1.4-build__from_headers.patch
BuildArch:	noarch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  xz

%description
This package contains the firmware required to work with the zd1211 chipset.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}
sed -i 's/\r//' *.h

%build
%{make_build}

%install
%{make_install} FW_DIR=$RPM_BUILD_ROOT/lib/firmware/zd1211
xz -C crc32 $RPM_BUILD_ROOT/lib/firmware/zd1211/*

%files
%doc README
%license COPYING
%dir /lib/firmware/zd1211
/lib/firmware/zd1211/*

%changelog
%autochangelog
