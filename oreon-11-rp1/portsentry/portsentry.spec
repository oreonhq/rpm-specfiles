%global source0_hash 544cdc0fb4c83d9a5e345f1ea6f6c3d4414962b3c575f699ba3a9ddd583c4f8a
Name:		portsentry
%global forgeurl https://github.com/portsentry/portsentry
%global version0 2.0.7
%forgemeta
Version:	%forgeversion
Release:        1%{?dist}
Summary:        Tool to detect and respond to port scans
Summary(sv):	Verktyg för att upptäcka och svara på portskanningar
License:	BSD-2-Clause AND BSD-1-Clause AND CPL-1.0
URL:		https://portsentry.xyz/
Source0:        %{forgeurl}/archive/v%{version0}/%{name}-%{version0}.tar.gz
Source1:	fail2ban-jail.conf
Requires:	logrotate
Recommends:	portsentry-doc = %{version}-%{release}
Recommends:	portsentry-fail2ban = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libpcap-devel
BuildRequires:  pandoc
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Portsentry monitors network traffic in order to detect port scans in
real-time. It can identify several types of scans, including TCP, SYN,
FIN, XMAS, and NULL scans and UDP probing.

%description -l sv
Portsentry övervakar nätverkstrafik för att upptäcka portskanningar i
realtid. Den kan identifiera flera olika typer av skanningar,
inklusive TCP-, SYN-, FIN-, XMAS- och NULL-skanningar samt
UDP-avkänning.

%package doc
Summary: Documentation of Portsentry
Summary(sv): Dokumentation av Portsentry
Requires:	portsentry = %{version}-%{release}
BuildArch:	noarch
%description doc
This package contains documentation of the Portsentry monitoring tool

%description -l sv doc
Detta paket innehåller dokumentation av övervakningsverktyget
Portsentry.

%package fail2ban
Summary: Fail2ban configurations for Portsentry
Summary(sv): Fail2ban-konfigurationer för Portsentry
Requires:	portsentry = %{version}-%{release}
Requires:	fail2ban-server
BuildArch:	noarch
%description fail2ban 
This package contains configurations for Fail2ban to block IP
addresses detected by Portsentry. If you want to block hosts on
package detection, this is the recommended method.

%description -l sv fail2ban
Detta paket innehåller konfigurationer till Fail2ban för att blockera
IP-adresser som Portsentry upptäcker. Om man vill blockera värdar när
paket upptäcks är detta den rekommenderade metoden.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

%cmake -D CMAKE_BUILD_TYPE=Release \
       -D BUILD_TESTS=ON \
       -D CMAKE_VERBOSE_MAKEFILE:BOOL=ON \
       -D INSTALL_LICENSE=OFF \
       -D CMAKE_INSTALL_SYSCONFDIR=%_sysconfdir \
       -D CMAKE_INSTALL_LIBDIR=lib \
       -D SYSTEMD_SYSTEM_UNIT_DIR=%_unitdir
%cmake_build
%install
%cmake_install
install -d %buildroot%_sysconfdir/fail2ban/filter.d
install -m 644 fail2ban/%name.conf %buildroot%_sysconfdir/fail2ban/filter.d/%{name}2.conf
install -d %buildroot%_sysconfdir/fail2ban/jail.d
install -m 644 %{SOURCE1} %buildroot%_sysconfdir/fail2ban/jail.d/%{name}2.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%post

%systemd_post %name.service
%preun

%systemd_preun %name.service
%postun

%systemd_postun_with_restart %name.service
%files -f %{oreon_filedir}/main.list
%files -n portsentry-doc -f %{oreon_filedir}/portsentry-doc.list
%files -n portsentry-fail2ban -f %{oreon_filedir}/portsentry-fail2ban.list

%changelog

%autochangelog
