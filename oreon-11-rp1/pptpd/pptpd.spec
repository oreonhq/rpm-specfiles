%global source0_hash 6a724284b1ce00ea23f7d7608d081843a10c8a8d87d951cb2ea86e70aa1b4e77

# Available rpmbuild options:
#
# --without	bcrelay
#

# hardened build if not overriden
%{!?_hardened_build:%global _hardened_build 1}

%if %{?_hardened_build:%{_hardened_build}}%{!?_hardened_build:0}
%global harden -Wl,-z,relro,-z,now
%endif

# this package ships a ppp plugin, these are strictly tied to the ppp
# version, so it must be rebuilt when the ppp version changes or else this happens:
# /usr/sbin/pppd: Plugin /usr/lib64/pptpd/pptpd-logwtmp.so is for pppd version 2.5.0, this is 2.5.1
%global ppp_version %(pkg-config --modversion pppd 2>/dev/null || echo bad)

Summary:	PoPToP Point to Point Tunneling Server
Name:		pptpd
Version:	1.5.0
Release:	7%{?dist}
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	perl-generators
BuildRequires:	ppp-devel, systemd
URL:		http://poptop.sourceforge.net/
Source0:	http://downloads.sf.net/poptop/pptpd-%{version}.tar.gz
Source1:	pptpd.service
Source2:	pptpd.sysconfig
Source3:	modules-load.conf
Source4:	20-pptpd.conf
Requires:	ppp = %{ppp_version}
Requires:	perl-interpreter

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
This implements a Virtual Private Networking Server (VPN) that is
compatible with Microsoft VPN clients. It allows windows users to
connect to an internal firewalled network using their dialup.

%if 0%{?fedora} < 23
%package sysvinit
Summary: PoPToP Point to Point Tunneling Server
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
Requires(preun): /sbin/service

%description sysvinit
The SysV initscript for PoPToP Point to Point Tunneling Server.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Fix for distros with %%{_libdir} = /usr/lib64
perl -pi -e 's,/usr/lib/pptpd,%{_libdir}/pptpd,;' pptpctrl.c

%build
%configure \
	--without-libwrap \
	%{!?_without_bcrelay:--enable-bcrelay} \
	%{?_without_bcrelay:--disable-bcrelay}
make CFLAGS='-fno-builtin -fPIC -DSBINDIR=\"%{_sbindir}\" %{optflags} %{?harden}'

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man{5,8}

make %{?_smp_mflags} \
	DESTDIR=%{buildroot} \
	INSTALL="install -p" \
	LIBDIR=%{buildroot}%{_libdir}/pptpd \
	install
%if 0%{?fedora} < 23
install -Dpm 0755 pptpd.init %{buildroot}%{_sysconfdir}/rc.d/init.d/pptpd
%endif
install -Dpm 0644 samples/pptpd.conf %{buildroot}%{_sysconfdir}/pptpd.conf
install -Dpm 0644 samples/options.pptpd %{buildroot}%{_sysconfdir}/ppp/options.pptpd
install -pm 0755 tools/vpnuser %{buildroot}%{_bindir}/vpnuser
install -pm 0755 tools/vpnstats.pl %{buildroot}%{_bindir}/vpnstats.pl
install -pm 0755 tools/pptp-portslave %{buildroot}%{_sbindir}/pptp-portslave
install -pm 0644 pptpd.conf.5 %{buildroot}%{_mandir}/man5/pptpd.conf.5
install -pm 0644 pptpd.8 %{buildroot}%{_mandir}/man8/pptpd.8
install -pm 0644 pptpctrl.8 %{buildroot}%{_mandir}/man8/pptpctrl.8
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_unitdir}/pptpd.service
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/pptpd
install -Dpm 0644 %{SOURCE3} %{buildroot}%{_usr}/lib/modules-load.d/pptpd.conf
install -Dpm 0644 %{SOURCE4} %{buildroot}%{_usr}/lib/sysctl.d/20-pptpd.conf

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%if 0%{?fedora} < 23
%post sysvinit
/sbin/chkconfig --add pptpd >/dev/null 2>&1 ||:

%preun sysvinit
if [ "$1" = 0 ]; then
    %{_initrddir}/pptpd stop >/dev/null 2>&1 ||:
    /sbin/chkconfig --del pptpd >/dev/null 2>&1 ||:
fi

%postun sysvinit
[ "$1" -ge 1 ] && %{_initrddir}/pptpd condrestart >/dev/null 2>&1 ||:
%endif

%files
%doc AUTHORS COPYING README* TODO ChangeLog* samples
%{_sbindir}/pptpd
%{_sbindir}/pptpctrl
%{_sbindir}/pptp-portslave
%{!?_without_bcrelay:%{_sbindir}/bcrelay}
%dir %{_libdir}/pptpd
%{_libdir}/pptpd/pptpd-logwtmp.so
%{_bindir}/vpnuser
%{_bindir}/vpnstats.pl
%{_mandir}/man5/pptpd.conf.5*
%{_mandir}/man8/*.8*
%{_unitdir}/pptpd.service
%{_usr}/lib/modules-load.d/pptpd.conf
%{_usr}/lib/sysctl.d/20-pptpd.conf

%config(noreplace) %{_sysconfdir}/sysconfig/pptpd
%config(noreplace) %{_sysconfdir}/pptpd.conf
%config(noreplace) %{_sysconfdir}/ppp/options.pptpd

%if 0%{?fedora} < 23
%files sysvinit
%attr(0755,root,root) %{_sysconfdir}/rc.d/init.d/pptpd
%endif

%changelog
%autochangelog
