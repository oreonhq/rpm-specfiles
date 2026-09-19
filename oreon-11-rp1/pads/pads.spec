%global source0_hash 935470b2440987d9c4efa49769cbe9eef213cd7437ec6726f0fbb1fc32ed614c

%define _default_patch_fuzz 2
Name: pads
Version: 1.2
Release: 44%{?dist}
Summary: Passive Asset Detection System
License: GPL-2.0-or-later 
URL: http://passive.sourceforge.net/
Source0: http://prdownloads.sourceforge.net/passive/%{name}-%{version}.tar.gz
Source1: pads.service
Source2: pads.sysconfig
Patch1: pads-1.2-cleanup.patch
Patch2: pads-1.2-memleak.patch
Patch3: pads-1.2-overrun.patch
Patch4: pads-1.2-disable-debug.patch
Patch5: pads-1.2-daemonize.patch
Patch6: pads-1.2-ether-codes-update.patch
Patch7: pads-1.2-misc.patch
Patch8: pads-1.2-arp.patch
Patch9: pads-1.2-prelude.patch
Patch10: pads+vlan.patch
Patch11: pads-1.2-prelude-cleanup.patch
Patch12: pads-1.2-readonly.patch
Patch13: pads-1.2-bstring.patch
Patch14: pads-1.2-leak.patch
Patch15: pads-1.2-perf.patch
Patch16: pads-1.2-daemon.patch
Patch17: pads-1.2-pthreads.patch
Patch18: pads-aarch64.patch
Patch19: pads-1.2-inline-cleanup.patch
Patch20: pads-1.2-extra-libs.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires: automake autoconf
BuildRequires: pcre-devel libpcap-devel
BuildRequires: perl-generators
BuildRequires: systemd
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description
PADS is a libpcap based detection engine used to passively 
detect network assets.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch 1 -p1
%patch 2 -p1
%patch 3 -p1
%patch 4 -p1
%patch 5 -p1
%patch 6 -p1
%patch 7 -p1
%patch 8 -p1
%patch 9 -p1
%patch 10 -p1
%patch 11 -p1
%patch 12 -p1
%patch 13 -p1
%patch 14 -p1
%patch 15 -p1
%patch 16 -p1
%patch 17 -p1
%patch 18 -p1
%patch 19 -p1
%patch 20 -p1

%build
autoreconf -fv --install
%configure 
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
make install DESTDIR=%{buildroot}
install -m 644 %SOURCE1 %{buildroot}%{_unitdir}/pads.service
install -m 640 %SOURCE2 %{buildroot}%{_sysconfdir}/sysconfig/%{name}
# Remove installed docs since we pick this up another way
rm -rf $RPM_BUILD_ROOT/usr/share/pads/

%post
%systemd_post pads.service

%preun
%systemd_preun pads.service

%postun
%systemd_postun_with_restart pads.service

%files
%doc doc/AUTHORS doc/COPYING doc/README doc/ChangeLog
%{_sysconfdir}/pads-ether-codes
%{_sysconfdir}/pads-signature-list
%config(noreplace) %attr(0640,root,root) %{_sysconfdir}/pads.conf
%config(noreplace) %attr(0640,root,root) %{_sysconfdir}/sysconfig/%{name}
%{_unitdir}/pads.service
%{_bindir}/pads
%{_bindir}/pads-report
%{_mandir}/*/*

%changelog
%autochangelog
