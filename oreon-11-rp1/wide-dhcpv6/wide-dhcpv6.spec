%global source0_hash 55a66174a1edeabd90029b83cb3fff8e0b63718a556ce95b97d464a87fd1bd81

#
# spec file for package wide-dhcpv6
#

%global ubuntu_release 23
%global my_release 3
%global _hardened_build 1

Name:           wide-dhcpv6
BuildRequires:  gcc
BuildRequires:  bison flex libfl-static systemd
# The entire source code is BSD except the bison parser code which is GPL
# Automatically converted from old format: BSD and GPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND GPL-2.0-or-later
Summary:        DHCP Client and Server for IPv6
Version:        20080615
Url:            https://launchpad.net/ubuntu/+source/%{name}/%{version}-%{ubuntu_release}
Release:        %{ubuntu_release}.%{my_release}%{dist}.9
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        CHANGELOG-LINUX
Source2:        COPYRIGHT
Source3:        dhcp6c-script
Source4:        dhcp6c.service
Source5:        dhcp6r.service
Source6:        dhcp6s.service
Source7:        RELEASENOTES
Source8:        dhcp6c@.service
Patch1:		wide-dhcpv6-0001-Fix-manpages.patch
Patch2:		wide-dhcpv6-0002-Don-t-strip-binaries.patch
Patch3:		wide-dhcpv6-0003-Close-inherited-file-descriptors.patch
Patch4:		wide-dhcpv6-0004-GNU-libc6-fixes.patch
Patch5:		wide-dhcpv6-0005-Update-ifid-on-interface-restart.patch
Patch6:		wide-dhcpv6-0006-Add-new-feature-dhcp6c-profiles.patch
Patch7:		wide-dhcpv6-0007-Adding-ifid-option-to-the-dhcp6c.conf-prefix-interfa.patch
Patch8:		wide-dhcpv6-0008-Close-file-descriptors-on-exec.patch
Patch9:		wide-dhcpv6-0009-Fix-renewal-of-IA-NA.patch
Patch10:	wide-dhcpv6-0010-Call-client-script-after-interfaces-have-been-update.patch
Patch11:	wide-dhcpv6-0011-resolv-warnings-so-as-to-make-blhc-and-gcc-both-happ.patch
Patch12:	wide-dhcpv6-0012-fix-a-redefined-YYDEBUG-warning-of-gcc-for-the-code-.patch
Patch13:	wide-dhcpv6-0013-added-several-comments-examples-by-Stefan-Sperling.patch
Patch14:	wide-dhcpv6-0014-Support-to-build-on-kFreeBSD-n-GNU-Hurd-platform.patch
Patch15:	wide-dhcpv6-0015-a-bit-info-to-logger-when-get-OPTION_RECONF_ACCEPT.patch
Patch16:	wide-dhcpv6-0016-fix-typo-in-dhcp6c.8-manpage.patch
Patch17:	wide-dhcpv6-0017-Remove-unused-linking-with-libfl.patch
Patch18:	wide-dhcpv6-0018-dhcpv6-ignore-advertise-messages-with-none-of-reques.patch
Patch19:	wide-dhcpv6-0019-Server-should-not-bind-control-port-if-there-is-no-s.patch
Patch20:	wide-dhcpv6-0020-Adding-option-to-randomize-interface-id.patch
Patch21:	wide-dhcpv6-0021-Make-sla-len-config-optional.patch
Patch22:	wide-dhcpv6-0022-Make-sla-id-config-optional.patch
Patch23:	wide-dhcpv6-0023-fix-the-parallel-build-fix.patch
Patch99:	wide-dhcpv6-fedora-c99.patch
Requires(preun): systemd
Requires(postun): systemd

%description
This is the DHCPv6 package from WIDE project. For more information visit the
project web site at http://wide-dhcpv6.sourceforge.net/

DHCPv6 allows prefix delegation and host configuration for the IPv6 network
protocol.

Multiple network interfaces are supported by this DHCPv6 package.

This package contains the server, relay and client.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q 
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
%patch -P10 -p1
%patch -P11 -p1
%patch -P12 -p1
%patch -P13 -p1
%patch -P14 -p1
%patch -P15 -p1
%patch -P16 -p1
%patch -P17 -p1
%patch -P18 -p1
%patch -P19 -p1
%patch -P20 -p1
%patch -P21 -p1
%patch -P22 -p1
%patch -P23 -p1
%patch -P99 -p1

%build
%configure --sysconfdir=%{_sysconfdir}/%{name} --enable-libdhcp=no
make %{?_smp_mflags}	

%install
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man{8,5}
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
mkdir -p %{buildroot}%{_unitdir}
install -p -m 755 dhcp6c dhcp6s dhcp6relay dhcp6ctl %{buildroot}%{_sbindir}
install -p -m 644 dhcp6c.8 dhcp6s.8 dhcp6relay.8 dhcp6ctl.8 %{buildroot}/%{_mandir}/man8
install -p -m 644 dhcp6c.conf.5 dhcp6s.conf.5 %{buildroot}/%{_mandir}/man5
install -p -m 644 %{SOURCE1} %{buildroot}%{_defaultdocdir}/%{name}
install -p -m 644 %{SOURCE2} %{buildroot}%{_defaultdocdir}/%{name}
install -p -m 644 %{SOURCE3} %{buildroot}%{_defaultdocdir}/%{name}
install -p -m 644 %{SOURCE4} %{buildroot}%{_defaultdocdir}/%{name}
install -p -m 644 %{SOURCE5} %{buildroot}%{_defaultdocdir}/%{name}
install -p -m 644 %{SOURCE6} %{buildroot}%{_defaultdocdir}/%{name}
install -p -m 644 %{SOURCE7} %{buildroot}%{_defaultdocdir}/%{name}
install -p -m 644 %{SOURCE8} %{buildroot}%{_unitdir}
install -p -m 644 README CHANGES %{buildroot}%{_defaultdocdir}/%{name}
install -p -m 644 dhcp6c.conf.sample %{buildroot}%{_defaultdocdir}/%{name}
install -p -m 644 dhcp6s.conf.sample %{buildroot}%{_defaultdocdir}/%{name}

%preun
if [ $1 -lt 1 ] ; then
%systemd_preun dhcp6c@.service
fi
%systemd_preun dhcp6c.service
%systemd_preun dhcp6r.service
%systemd_preun dhcp6s.service

%postun
%systemd_postun_with_restart dhcp6c.service
%systemd_postun_with_restart dhcp6r.service
%systemd_postun_with_restart dhcp6s.service

%files
%dir %{_sysconfdir}/%{name}
%{_defaultdocdir}/%{name}/*
%{_sbindir}/*
%{_mandir}/man?/*
%{_unitdir}/*

%changelog
%autochangelog
