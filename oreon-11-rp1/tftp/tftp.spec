%global source0_hash 6064caa87435040181e4493b82a19fef5aa918f0e25d28ad2c3344c38e0d5a26

%global _hardened_build 1

Summary: The client for the Trivial File Transfer Protocol (TFTP)
Name: tftp
Version: 5.3
Release: 3%{?dist}
License: BSD-4-Clause-UC
URL: http://www.kernel.org/pub/software/network/tftp/
Source0: https://git.kernel.org/pub/scm/network/tftp/tftp-hpa.git/snapshot/tftp-hpa-%{version}.tar.gz
Source1: tftp.socket
Source2: tftp.service
Source3: tftp-server-tmpfiles.conf

Patch0: tftp-0.40-remap.patch
Patch2: tftp-hpa-0.39-tzfix.patch
Patch3: tftp-0.42-tftpboot.patch
Patch4: tftp-0.49-chk_retcodes.patch
Patch5: tftp-hpa-0.49-fortify-strcpy-crash.patch
Patch6: tftp-hpa-5.3-cmd_arg.patch
Patch7: tftp-hpa-0.49-stats.patch
Patch8: tftp-hpa-5.3-pktinfo.patch
Patch9: tftp-doc.patch
Patch10: tftp-enhanced-logging.patch
Patch12: tftp-off-by-one.patch
Patch14: tftp-hpa-5.2-osh.patch
# https://git.kernel.org/pub/scm/network/tftp/tftp-hpa.git/patch/?id=b9f2335e88dcb3939015843c7143f1533c755a46
Patch15: tftp-hpa-5.3-setjmp.patch
Patch16: tftp-hpa-5.3-tftp-exit-code-cmdmode.patch

BuildRequires: autoconf
BuildRequires: gcc
BuildRequires: make
BuildRequires: readline-devel
BuildRequires: systemd-rpm-macros

%description
The Trivial File Transfer Protocol (TFTP) is normally used only for
booting diskless workstations.  The tftp package provides the user
interface for TFTP, which allows users to transfer files to and from a
remote machine.  This program and TFTP provide very little security,
and should not be enabled unless it is expressly needed.

%package server
Summary: The server for the Trivial File Transfer Protocol (TFTP)
Requires: systemd-units
Requires(post): systemd-units
Requires(postun): systemd-units

%description server
The Trivial File Transfer Protocol (TFTP) is normally used only for
booting diskless workstations.  The tftp-server package provides the
server for TFTP, which allows users to transfer files to and from a
remote machine. TFTP provides very little security, and should not be
enabled unless it is expressly needed.  The TFTP server is run by using
systemd socket activation, and is disabled by default.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n tftp-hpa-%{version}
%patch -P0 -p1 -b .zero
%patch -P2 -p1 -b .tzfix
%patch -P3 -p1 -b .tftpboot
%patch -P4 -p1 -b .chk_retcodes
%patch -P5 -p1 -b .fortify-strcpy-crash
%patch -P6 -p1 -b .cmd_arg
%patch -P7 -p1 -b .stats
%patch -P8 -p1 -b .pktinfo
%patch -P9 -p1 -b .doc
%patch -P10 -p1 -b .logging
%patch -P12 -p1 -b .off-by-one
%patch -P14 -p1 -b .osh
%patch -P15 -p1 -b .setjmp
%patch -P16 -p1 -b .cmd_exit_code

%build
autoreconf
%configure
%make_build

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man{1,8}
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}
mkdir -p ${RPM_BUILD_ROOT}%{_localstatedir}/lib/tftpboot
mkdir -p ${RPM_BUILD_ROOT}%{_tmpfilesdir}
mkdir -p ${RPM_BUILD_ROOT}%{_unitdir}

%make_install INSTALLROOT=%{buildroot} SBINDIR=%{_sbindir} MANDIR=%{_mandir}

install -p -m 644 %SOURCE1 ${RPM_BUILD_ROOT}%{_unitdir}
install -p -m 644 %SOURCE2 ${RPM_BUILD_ROOT}%{_unitdir}
install -p -m 644 %SOURCE3 ${RPM_BUILD_ROOT}%{_tmpfilesdir}/%{name}.conf

%post server
%systemd_post tftp.socket

%preun server
%systemd_preun tftp.socket

%postun server
%systemd_postun_with_restart tftp.socket


%files
%doc README README.security CHANGES
%{_bindir}/tftp
%{_mandir}/man1/tftp.1*

%files server
%doc README README.security CHANGES
%dir %{_localstatedir}/lib/tftpboot
%{_sbindir}/in.tftpd
%{_mandir}/man8/in.tftpd.8*
%{_mandir}/man8/tftpd.8*
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/tftp.service
%{_unitdir}/tftp.socket

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.3-3
- Prepare for Oreon 11 (RP1)
