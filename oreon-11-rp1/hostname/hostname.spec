# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 5bb5d1be011158090157c9e7587ae5606c262a5020ecdc5caac6686b9910592e

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           hostname
Version:        3.25
Release:        1%{?dist}
Summary:        Utility to set/show the host name or domain name
License:        GPL-2.0-or-later
URL:            https://tracker.debian.org/pkg/hostname
Source0:        https://ftp.debian.org/debian/pool/main/h/hostname/hostname_%{version}.tar.xz
Source1:        gpl-2.0.txt
Source2:        nis-domainname
Source3:        nis-domainname.service
Patch1:         hostname-rh.patch

BuildRequires:  oreon-rpm-macros
BuildRequires:  gcc
BuildRequires:  make

%description
This package provides commands which can be used to display the system's
DNS name, and to display or set its hostname or NIS domain name.

%prep
%oreon_sha256
%autosetup -n hostname -p1

%build
%set_build_flags
%make_build CFLAGS="$CFLAGS -D_GNU_SOURCE" LDFLAGS="$LDFLAGS"

%install
%make_install
install -Dpm0755 %{SOURCE2} %{buildroot}%{_libexecdir}/%{name}/nis-domainname
install -Dpm0644 %{SOURCE3} %{buildroot}%{_prefix}/lib/systemd/system/nis-domainname.service

%check
./hostname --help 2>&1 | grep -q Usage
./hostname -V
./hostname | grep -q .

%post
if [ $1 -eq 1 ]; then
  systemctl --no-reload preset nis-domainname.service &>/dev/null || :
fi

%preun
if [ $1 -eq 0 ]; then
  systemctl --no-reload disable --now nis-domainname.service &>/dev/null || :
fi

%files
%doc COPYRIGHT
%license %{SOURCE1}
%{_bindir}/hostname
%{_bindir}/dnsdomainname
%{_bindir}/domainname
%{_bindir}/nisdomainname
%{_bindir}/ypdomainname
%{_mandir}/man1/hostname.1*
%{_mandir}/man1/dnsdomainname.1*
%{_mandir}/man1/domainname.1*
%{_mandir}/man1/nisdomainname.1*
%{_mandir}/man1/ypdomainname.1*
%{_prefix}/lib/systemd/system/nis-domainname.service
%{_libexecdir}/%{name}/

%changelog
%autochangelog
