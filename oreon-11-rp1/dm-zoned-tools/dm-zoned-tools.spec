%global source0_hash 6ce5447bd29e81fabcb9a290847c4cd316796baed7e0310da21518733958b29f

Name:		dm-zoned-tools
Version:	2.2.2
Release:	10%{?dist}
Summary:	Provides utilities to format, check and repair Linux dm-zoned devices

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		https://github.com/westerndigitalcorporation/%{name}
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(devmapper)
BuildRequires:	pkgconfig(libkmod)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(blkid)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	gcc

%description
This package provides the dmzadm utility which can be used to format,
check and repair zoned block devices used with Linux dm-zoned device
mapper target driver.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
sh autogen.sh
%configure
%make_build

%install
%make_install

%files
%{_sbindir}/dmzadm
%{_mandir}/man8/dmzadm.*

%license COPYING.GPL
%doc README.md CONTRIBUTING

%changelog
%autochangelog
