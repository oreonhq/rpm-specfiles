%global source0_hash 3395d8f31970585afaf6e58e5fc4d4eb18b8dc9b9c6c339930f32966c37f3dd2
Name:		dm-zoned-tools
Version:	2.2.2
Release:        1%{?dist}
Summary:        Provides utilities to format, check and repair Linux dm-zoned devices
License:	GPL-3.0-or-later
URL:		https://github.com/westerndigitalcorporation/%{name}
Source0:        https://github.com/westerndigitalcorporation/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(devmapper)
BuildRequires:  pkgconfig(libkmod)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(uuid)
# /oreon:deps
%description
This package provides the dmzadm utility which can be used to format,
check and repair zoned block devices used with Linux dm-zoned device
mapper target driver.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

sh autogen.sh
%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
