%global source0_hash 7a82c276ca1540faa7f5bb25010f4a59d45323a31c44a30fbe4a6e484dd18b1a

Summary: A port-knocking server/client
Name: knock
Version: 0.8
Release: 13%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://www.zeroflux.org/projects/%{name}
Source0: https://github.com/jvinet/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1: %{name}d.sysconfig
Source2: %{name}d.conf
Source3: %{name}d.service
# Installs the helper executable in /usr/libexec instead of /usr/sbin
Patch0: knock_fix_knock_helper_ipt_location.patch
%{?systemd_requires}
BuildRequires:  gcc
BuildRequires: systemd-rpm-macros
BuildRequires: libpcap-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: make

%description
This is a port-knocking server/client.  Port-knocking is a method where a
server can sniff one of its interfaces for a special "knock" sequence of
port-hits.  When detected, it will run a specified event bound to that port
knock sequence.  These port-hits need not be on open ports, since we use
libpcap to sniff the raw interface traffic. This package contains the
knock client.

%package server
Summary: A port-knocking server/client

%description server
Knock is a port-knocking server/client.  Port-knocking is a method where a
server can sniff one of its interfaces for a special "knock" sequence of
port-hits.  When detected, it will run a specified event bound to that port
knock sequence.  These port-hits need not be on open ports, since we use
libpcap to sniff the raw interface traffic. This package contains the
knockd server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
autoreconf -vif
%configure
%make_build
iconv -f iso8859-1 -t utf-8 ChangeLog > ChangeLog.conv && mv -f ChangeLog.conv ChangeLog

%install
%make_install
%{__install} -d %{buildroot}%{_sysconfdir}/sysconfig
%{__install} -d %{buildroot}%{_unitdir}

%{__install} -m 0644 -p %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/%{name}d
%{__install} -m 0644 -p %{SOURCE2} %{buildroot}%{_sysconfdir}/
%{__install} -m 0644 -p %{SOURCE3} %{buildroot}%{_unitdir}/%{name}d.service

# Added as license
%{__rm} -f %{buildroot}%{_docdir}/COPYING

%post server
%systemd_post knockd.service

%preun server
%systemd_preun knockd.service

%postun server
%systemd_postun_with_restart knockd.service

%files
%license COPYING
%doc %{_docdir}/%{name}
%{_bindir}/%{name}
%{_mandir}/man?/%{name}.*

%files server
%license COPYING
%doc %{_docdir}/%{name}
%{_sbindir}/%{name}d
%{_libexecdir}/knock_helper_ipt.sh
%{_unitdir}/%{name}d.service
%config(noreplace) %{_sysconfdir}/%{name}d.conf
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}d
%{_mandir}/man?/%{name}d.*

%changelog
%autochangelog
