# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b22e0901227b820cd1c280abe681a15b773a5103a5e10dc442e94ebb34cbf58d
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global         _firmwarepath    /usr/lib/firmware

Name:           wireless-regdb
Version:        2026.09.03
Release:        1%{?dist}
Summary:        Regulatory database for 802.11 wireless networking

License:        ISC
URL:            https://wireless.wiki.kernel.org/en/developers/regulatory/wireless-regdb
BuildArch:      noarch

Requires:       udev, iw
Requires:       systemd >= 190

BuildRequires: oreon-rpm-macros
BuildRequires:  make
BuildRequires:  systemd-devel

Provides:       crda = 3.18_2019.03.01-3
Obsoletes:      crda <= 3.18_2019.03.01-2

Source0:        http://www.kernel.org/pub/software/network/wireless-regdb/wireless-regdb-%{version}.tar.xz
Source1:        setregdomain
Source2:        setregdomain.1
Source3:        85-regulatory.rules

%description
The wireless-regdb package provides the regulatory rules database
used by the kernels 802.11 networking stack in order to comply 
with radio frequency regulatory rules around the world.

%prep
%oreon_sha256
%autosetup -p1

%build
: # Package installs a firmware-like, prebuilt binary from upstream...

%install
make install DESTDIR=%{buildroot} MANDIR=%{_mandir} \
	FIRMWARE_PATH=%{_firmwarepath}

install -D -pm 0755 %SOURCE1 %{buildroot}%{_sbindir}/setregdomain
install -D -pm 0644 %SOURCE2 %{buildroot}%{_mandir}/man1/setregdomain.1
install -D -pm 0644 %SOURCE3 %{buildroot}%{_udevrulesdir}/85-regulatory.rules

rm -rf %{buildroot}/usr/lib/crda

%files
%{_sbindir}/setregdomain
%{_udevrulesdir}/85-regulatory.rules
%{_firmwarepath}/regulatory.db
%{_firmwarepath}/regulatory.db.p7s
%{_mandir}/man1/setregdomain.1*
%{_mandir}/man5/regulatory.db.5*
%{_mandir}/man5/regulatory.bin.5*
%license LICENSE
%doc README

%changelog
%autochangelog
