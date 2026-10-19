%global source0_hash 639cae38c95527b7a0f577beba5a6c4732e95d8d0ccec05f01cdf7868fab1f0e
%global source1_hash 43631ac5481c5b4d4d370cd2d1d57d2b751f71eb08e134100900e1a1b634bd70
Summary:        The client for the Trivial File Transfer Protocol (TFTP)
Name: tftp
Version: 6.1
Release:        1%{?dist}
License: BSD-4-Clause-UC
URL: http://www.kernel.org/pub/software/network/tftp/
Source0:        https://www.kernel.org/pub/software/network/tftp/tftp-hpa-%{version}.tar.gz
Source1: https://www.kernel.org/pub/software/network/tftp/tftp-hpa-%{version}.tar.sign
Source2: hpa.gpg
Source3: tftp.socket
Source4: tftp.service
Source5: tftp-server-sysusers.conf
Source6: tftp-server-tmpfiles.conf
Patch: tftp-enhanced-logging.patch
Patch: tftp-hpa-5.2-osh.patch
Patch: tftp-hpa-5.3-tftp-exit-code-cmdmode.patch
Patch: tftp-fedora-tftpboot.patch
# oreon:deps
BuildRequires:  bc
BuildRequires:  gcc
BuildRequires:  gpgverify
BuildRequires:  make
BuildRequires:  readline-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
gzip -cd '%{SOURCE0}' > 'tftp-hpa-%{version}.tar'
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='tftp-hpa-%{version}.tar'
%autosetup -p1 -n tftp-hpa-%{version}

%build

%configure
%make_build
%install
%make_install INSTALLROOT=%{buildroot} SBINDIR=%{_sbindir} MANDIR=%{_mandir}
mkdir -p %{buildroot}%{_localstatedir}/lib/tftpboot
install -D -p -m 644 %SOURCE3 %{buildroot}%{_unitdir}/%{name}.socket
install -D -p -m 644 %SOURCE4 %{buildroot}%{_unitdir}/%{name}.service
install -D -p -m 644 %SOURCE5 %{buildroot}%{_sysusersdir}/%{name}.conf
install -D -p -m 644 %SOURCE6 %{buildroot}%{_tmpfilesdir}/%{name}.conf
mkdir -p %{buildroot}%{_sysconfdir}/tftp
echo '# See tftpd(8) for the definition of remap rules' > %{buildroot}%{_sysconfdir}/%{name}/map-file
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

tests/test-tftp.sh
%post server

%systemd_post tftp.socket
%preun server

%systemd_preun tftp.socket
%postun server

%systemd_postun_with_restart tftp.socket
%files -f %{oreon_filedir}/main.list
%files -n tftp-server -f %{oreon_filedir}/tftp-server.list

%changelog

%autochangelog
