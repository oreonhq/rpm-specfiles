%global _hardened_build 1

Summary: Network monitoring tools including ping
Name: iputils
Version: 20250605
Release: 2%{?dist}
# some parts are under the original BSD (ping.c)
# some are under GPLv2+ (tracepath.c)
License: BSD-4-Clause-UC AND GPL-2.0-or-later
URL: https://github.com/iputils/iputils

Source0: https://github.com/iputils/iputils/archive/%{version}/%{name}-%{version}.tar.gz
Source1: ifenslave.tar.gz
# Taken from ping.c on 2014-07-12
Source4: bsd.txt
Source5: https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

Patch100: iputils-ifenslave.patch
Patch101: iputils-ifenslave-CWE-170.patch

BuildRequires: gcc
BuildRequires: meson
BuildRequires: gettext
BuildRequires: glibc-kernheaders >= 2.4-8.19
BuildRequires: libidn2-devel
BuildRequires: libcap-devel
BuildRequires: libxslt docbook5-style-xsl
BuildRequires: systemd
BuildRequires: iproute
%{?systemd_ordering}
Provides: /bin/ping
Provides: /bin/ping6
Provides: /sbin/arping

%description
The iputils package contains basic utilities for monitoring a network,
including ping. The ping command sends a series of ICMP protocol
ECHO_REQUEST packets to a specified network host to discover whether
the target machine is alive and receiving network traffic.

%prep
%autosetup -a 1 -n %{name}-%{version} -p1
cp %{SOURCE4} %{SOURCE5} .

%build
%meson
%meson_build
gcc $RPM_OPT_FLAGS $CFLAGS $RPM_LD_FLAGS $LDFLAGS ifenslave.c -o ifenslave

%install
%meson_install
%find_lang %{name}

mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}
ln -sf --relative ${RPM_BUILD_ROOT}%{_bindir}/ping ${RPM_BUILD_ROOT}%{_sbindir}/ping6
ln -sf --relative ${RPM_BUILD_ROOT}%{_bindir}/tracepath ${RPM_BUILD_ROOT}%{_sbindir}/tracepath6
%if "%{_sbindir}" != "%{_bindir}"
ln -sf --relative ${RPM_BUILD_ROOT}%{_bindir}/ping ${RPM_BUILD_ROOT}%{_sbindir}/
ln -sf --relative ${RPM_BUILD_ROOT}%{_bindir}/tracepath ${RPM_BUILD_ROOT}%{_sbindir}/
ln -sf --relative ${RPM_BUILD_ROOT}%{_bindir}/arping ${RPM_BUILD_ROOT}%{_sbindir}/
%endif

echo ".so man8/ping.8" > ${RPM_BUILD_ROOT}%{_mandir}/man8/ping6.8
echo ".so man8/tracepath.8" > ${RPM_BUILD_ROOT}%{_mandir}/man8/tracepath6.8
install -cp ifenslave ${RPM_BUILD_ROOT}%{_sbindir}/
install -cp ifenslave.8 ${RPM_BUILD_ROOT}%{_mandir}/man8/

%files -f %{name}.lang
%doc README.bonding
%license bsd.txt gpl-2.0.txt
%attr(0755,root,root) %caps(cap_net_raw=p) %{_bindir}/clockdiff
%attr(0755,root,root) %caps(cap_net_raw=p) %{_bindir}/arping
%attr(0755,root,root) %{_bindir}/ping
%{_sbindir}/ifenslave
%{_bindir}/tracepath
%{_sbindir}/ping6
%{_sbindir}/tracepath6
%if "%{_sbindir}" != "%{_bindir}"
%{_sbindir}/ping
%{_sbindir}/tracepath
%{_sbindir}/arping
%endif
%attr(644,root,root) %{_mandir}/man8/clockdiff.8*
%attr(644,root,root) %{_mandir}/man8/arping.8*
%attr(644,root,root) %{_mandir}/man8/ping.8*
%{_mandir}/man8/ping6.8*
%attr(644,root,root) %{_mandir}/man8/tracepath.8*
%{_mandir}/man8/tracepath6.8*
%attr(644,root,root) %{_mandir}/man8/ifenslave.8*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20250605-2
- Prepare for Oreon 11 (RP1)
