%global source1_hash 77b48fd2657520db9229b82bc1bab3f5c00b1b6f7ac2dbb9111b1c8584d6e335
%global source0_hash d44d28a839ea9daf969cc69150fde59910b2b39361dad81a3bd6cbd19218db11
%if 0%{?!noselinux:1}
%global WITH_SELINUX 1
%else
%global WITH_SELINUX 0
%endif
%global _hardened_build 1
%global pie 1
%global kerberos5 0
%global gsi 1
%global libedit 1
%global openssh_ver 10.5p1
Summary:        An implementation of the SSH protocol with GSI authentication
Name: gsi-openssh
Version: %{openssh_ver}
Release:        1%{?dist}
Provides: gsissh = %{version}-%{release}
Obsoletes: gsissh < 5.8p2-2
URL: http://www.openssh.com/portable.html
Source0:        https://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-%{version}.tar.gz
Source1: https://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-%{version}.tar.gz.asc
Source2: gsisshd.pam
Source3: gpgkey-736060BA.gpg
Source7: gsisshd.sysconfig
Source9: gsisshd@.service
Source10: gsisshd.socket
Source11: gsisshd.service
Source12: gsisshd-keygen@.service
Source13: gsisshd-keygen
Source15: gsisshd-keygen.target
Source19: %{name}-server-systemd-sysusers.conf
Source20: gsissh-host-keys-migration.sh
Source21: gsissh-host-keys-migration.service
Source99: README.sshd-and-gsisshd
Patch0001: 0001-openssh-7.8p1-role-mls.patch
Patch0002: 0002-openssh-6.6p1-keycat.patch
Patch0003: 0003-openssh-6.6p1-allow-ip-opts.patch
Patch0004: 0004-openssh-5.9p1-ipv6man.patch
Patch0005: 0005-openssh-5.8p2-sigpipe.patch
Patch0006: 0006-openssh-7.2p2-x11.patch
Patch0007: 0007-openssh-5.1p1-askpass-progress.patch
Patch0008: 0008-openssh-4.3p2-askpass-grab-info.patch
Patch0009: 0009-openssh-8.7p1-redhat.patch
Patch0010: 0010-openssh-7.8p1-UsePAM-warning.patch
Patch0011: 0011-openssh-9.6p1-gssapi-keyex.patch
Patch0012: 0012-openssh-6.6p1-force_krb.patch
Patch0013: 0013-openssh-7.7p1-gssapi-new-unique.patch
Patch0014: 0014-openssh-7.2p2-k5login_directory.patch
Patch0015: 0015-openssh-6.6p1-kuserok.patch
Patch0016: 0016-openssh-6.4p1-fromto-remote.patch
Patch0017: 0017-openssh-6.6.1p1-log-in-chroot.patch
Patch0018: 0018-openssh-6.6.1p1-scp-non-existing-directory.patch
Patch0019: 0019-openssh-6.6p1-GSSAPIEnablek5users.patch
Patch0020: 0020-openssh-6.8p1-sshdT-output.patch
Patch0021: 0021-openssh-6.7p1-sftp-force-permission.patch
Patch0022: 0022-openssh-7.2p2-s390-closefrom.patch
Patch0023: 0023-openssh-7.6p1-cleanup-selinux.patch
Patch0024: 0024-openssh-7.5p1-sandbox.patch
Patch0025: 0025-openssh-7.8p1-scp-ipv6.patch
Patch0026: 0026-openssh-8.0p1-crypto-policies.patch
Patch0027: 0027-openssh-8.0p1-openssl-kdf.patch
Patch0028: 0028-openssh-8.2p1-visibility.patch
Patch0029: 0029-openssh-8.2p1-x11-without-ipv6.patch
Patch0030: 0030-openssh-8.0p1-preserve-pam-errors.patch
Patch0031: 0031-openssh-8.7p1-scp-kill-switch.patch
Patch0032: 0032-openssh-8.7p1-recursive-scp.patch
Patch0033: 0033-openssh-8.7p1-minrsabits.patch
Patch0034: 0034-openssh-8.7p1-ibmca.patch
Patch0035: 0035-openssh-7.6p1-audit.patch
Patch0036: 0036-openssh-7.1p2-audit-race-condition.patch
Patch0037: 0037-openssh-9.0p1-audit-log.patch
Patch0038: 0038-openssh-7.7p1-fips.patch
Patch0039: 0039-openssh-8.7p1-ssh-manpage.patch
Patch0040: 0040-openssh-8.7p1-negotiate-supported-algs.patch
Patch0041: 0041-openssh-9.0p1-evp-fips-kex.patch
Patch0042: 0042-openssh-8.7p1-nohostsha1proof.patch
Patch0043: 0043-openssh-9.9p1-separate-keysign.patch
Patch0044: 0044-openssh-9.9p1-openssl-mlkem.patch
Patch0045: 0045-openssh-9.9p2-error_processing.patch
Patch0046: 0046-Provide-better-error-for-non-supported-private-keys.patch
Patch0047: 0047-Ignore-bad-hostkeys-in-known_hosts-file.patch
Patch0048: 0048-support-authentication-indicators-in-GSSAPI.patch
Patch0049: 0049-NIST-curves-hybrid-KEX-implementation.patch
Patch0050: 0050-Provide-a-way-to-disable-GSSAPIDelegateCredentials-s.patch
Patch0051: 0051-openssh-7.3p1-x11-max-displays.patch
Patch0052: 0052-openssh-10.2p1-pkcs11-uri.patch
Patch0053: 0053-openssh-10.2p1-pam-auth.patch
Patch1000: 1000-openssh-6.7p1-coverity.patch
Patch2000: 2000-openssh-10.2p1-gsissh.patch
Patch2001: 2001-openssh-10.2p1-hpn-18.8.0.patch
License: BSD-3-Clause AND BSD-2-Clause AND ISC AND SSH-OpenSSH AND ssh-keyscan AND sprintf AND LicenseRef-Fedora-Public-Domain AND X11-distribute-modifications-variant
Requires: /sbin/nologin
Requires: openssl-libs >= 3.5.0
Recommends: p11-kit
# oreon:deps
BuildRequires:  audit-libs-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  globus-common-devel
BuildRequires:  globus-gss-assist-devel
BuildRequires:  globus-gssapi-gsi-devel
BuildRequires:  gnupg2
BuildRequires:  groff
BuildRequires:  libedit-devel
BuildRequires:  libfido2-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  p11-kit-devel
BuildRequires:  pam-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  util-linux
BuildRequires:  xauth
BuildRequires:  zlib-devel
# /oreon:deps
%package clients
Summary: SSH client applications with GSI authentication
Provides: gsissh-clients = %{version}-%{release}
Obsoletes: gsissh-clients < 5.8p2-2
Requires: %{name} = %{version}-%{release}
Requires: crypto-policies >= 20220824-1
%package keysign
Summary: A helper program used for host-based authentication
Requires: %{name} = %{version}-%{release}
%package server
Summary: SSH server daemon with GSI authentication
Provides: gsissh-server = %{version}-%{release}
Obsoletes: gsissh-server < 5.8p2-2
Requires: %{name} = %{version}-%{release}
Requires(pre): /usr/sbin/useradd
Requires: pam >= 1.0.1-3
Requires: crypto-policies >= 20220824-1
%{?systemd_requires}
Requires(pre): policycoreutils-python-utils
Requires(postun): policycoreutils-python-utils
%description
SSH (Secure SHell) is a program for logging into and executing
commands on a remote machine. SSH is intended to replace rlogin and
rsh, and to provide secure encrypted communications between two
untrusted hosts over an insecure network. X11 connections and
arbitrary TCP/IP ports can also be forwarded over the secure channel.

OpenSSH is OpenBSD's version of the last free version of SSH, bringing
it up to date in terms of security and features.

This version of OpenSSH has been modified to support GSI authentication.

This package includes the core files necessary for both the gsissh
client and server. To make this package useful, you should also
install gsi-openssh-clients, gsi-openssh-server, or both.

%description clients
OpenSSH is a free version of SSH (Secure SHell), a program for logging
into and executing commands on a remote machine. This package includes
the clients necessary to make encrypted connections to SSH servers.

This version of OpenSSH has been modified to support GSI authentication.

%description keysign
OpenSSH is a free version of SSH (Secure SHell), a program for logging
into and executing commands on a remote machine. ssh-keysign is a
helper program used for host-based authentication disabled by default.

%description server
OpenSSH is a free version of SSH (Secure SHell), a program for logging
into and executing commands on a remote machine. This package contains
the secure shell daemon (sshd). The sshd daemon allows SSH clients to
securely connect to your SSH server.

This version of OpenSSH has been modified to support GSI authentication.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gpgv2 --quiet --keyring %{SOURCE3} %{SOURCE1} %{SOURCE0}
%autosetup -T -b 0 -p1 -n openssh-%{version}

sed 's/sshd.pid/gsisshd.pid/' -i pathnames.h
sed 's!$(piddir)/sshd.pid!$(piddir)/gsisshd.pid!' -i Makefile.in
sed 's!/etc/pam.d/sshd!/etc/pam.d/gsisshd!' -i sshd_config_redhat

cp -p %{SOURCE99} .

autoreconf

%build

%set_build_flags
%ifarch s390 s390x sparc sparcv9 sparc64
CFLAGS="$CFLAGS -fPIC"
%else
CFLAGS="$CFLAGS -fpic"
%endif
LDFLAGS="$LDFLAGS -pie -z relro -z now"
export CFLAGS
export LDFLAGS
%configure \
	--sysconfdir=%{_sysconfdir}/gsissh \
	--libexecdir=%{_libexecdir}/gsissh \
	--datadir=%{_datadir}/gsissh \
	--with-default-path=%{_libexecdir}/gsissh/bin:/usr/local/bin:/usr/bin \
	--with-superuser-path=%{_libexecdir}/gsissh/bin:/usr/local/bin:/usr/bin \
	--with-privsep-path=%{_datadir}/empty.sshd \
	--disable-strip \
	--without-zlib-version-check \
	--with-ipaddr-display \
	--with-pie=no \
	--without-hardening `# The hardening flags are configured by system` \
	--with-default-pkcs11-provider=yes \
	--with-security-key-builtin=yes \
	--with-pam \
	--with-pam-service=gsisshd \
	--without-kerberos5 \
	--with-gsi \
	--with-libedit
%make_build SSH_PROGRAM=%{_bindir}/gsissh \
     ASKPASS_PROGRAM=%{_libexecdir}/openssh/ssh-askpass
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p -m755 $RPM_BUILD_ROOT%{_sysconfdir}/gsissh
mkdir -p -m755 $RPM_BUILD_ROOT%{_sysconfdir}/gsissh/ssh_config.d
mkdir -p -m755 $RPM_BUILD_ROOT%{_sysconfdir}/gsissh/sshd_config.d
mkdir -p -m755 $RPM_BUILD_ROOT%{_libexecdir}/gsissh
%make_install
install -d $RPM_BUILD_ROOT/etc/pam.d/
install -d $RPM_BUILD_ROOT/etc/sysconfig/
install -d $RPM_BUILD_ROOT%{_libexecdir}/gsissh
install -m644 %{SOURCE2} $RPM_BUILD_ROOT/etc/pam.d/gsisshd
install -m644 %{SOURCE7} $RPM_BUILD_ROOT/etc/sysconfig/gsisshd
install -m644 ssh_config_redhat $RPM_BUILD_ROOT%{_sysconfdir}/gsissh/ssh_config.d/50-redhat.conf
install -m644 sshd_config_redhat_cp $RPM_BUILD_ROOT%{_sysconfdir}/gsissh/sshd_config.d/40-redhat-crypto-policies.conf
install -m644 sshd_config_redhat $RPM_BUILD_ROOT%{_sysconfdir}/gsissh/sshd_config.d/50-redhat.conf
install -d -m755 $RPM_BUILD_ROOT/%{_unitdir}
install -m644 %{SOURCE9} $RPM_BUILD_ROOT/%{_unitdir}/gsisshd@.service
install -m644 %{SOURCE10} $RPM_BUILD_ROOT/%{_unitdir}/gsisshd.socket
install -m644 %{SOURCE11} $RPM_BUILD_ROOT/%{_unitdir}/gsisshd.service
install -m644 %{SOURCE12} $RPM_BUILD_ROOT/%{_unitdir}/gsisshd-keygen@.service
install -m644 %{SOURCE15} $RPM_BUILD_ROOT/%{_unitdir}/gsisshd-keygen.target
install -m755 %{SOURCE13} $RPM_BUILD_ROOT/%{_libexecdir}/gsissh/sshd-keygen
install -d -m711 ${RPM_BUILD_ROOT}/%{_datadir}/empty.sshd
install -p -D -m 0644 %{SOURCE19} $RPM_BUILD_ROOT%{_sysusersdir}/%{name}-server.conf
install -m744 %{SOURCE20} $RPM_BUILD_ROOT/%{_libexecdir}/gsissh/ssh-host-keys-migration.sh
install -m644 %{SOURCE21} $RPM_BUILD_ROOT/%{_unitdir}/gsissh-host-keys-migration.service
install -d $RPM_BUILD_ROOT/%{_localstatedir}/lib
touch $RPM_BUILD_ROOT/%{_localstatedir}/lib/.gsissh-host-keys-migration
rm $RPM_BUILD_ROOT%{_bindir}/ssh-add
rm $RPM_BUILD_ROOT%{_bindir}/ssh-agent
rm $RPM_BUILD_ROOT%{_bindir}/ssh-keyscan
rm $RPM_BUILD_ROOT%{_libexecdir}/gsissh/ssh-keycat
rm $RPM_BUILD_ROOT%{_libexecdir}/gsissh/ssh-pkcs11-helper
rm $RPM_BUILD_ROOT%{_mandir}/man1/ssh-add.1*
rm $RPM_BUILD_ROOT%{_mandir}/man1/ssh-agent.1*
rm $RPM_BUILD_ROOT%{_mandir}/man1/ssh-keyscan.1*
rm $RPM_BUILD_ROOT%{_mandir}/man8/ssh-pkcs11-helper.8*
for f in $RPM_BUILD_ROOT%{_bindir}/* \
%if "%{_sbindir}" != "%{_bindir}"
	 $RPM_BUILD_ROOT%{_sbindir}/* \
%endif
	 $RPM_BUILD_ROOT%{_mandir}/man*/* ; do
    mv $f `dirname $f`/gsi`basename $f`
done
mkdir $RPM_BUILD_ROOT%{_libexecdir}/gsissh/bin
ln -nrs $RPM_BUILD_ROOT%{_bindir}/gsiscp \
	$RPM_BUILD_ROOT%{_libexecdir}/gsissh/bin/scp
ln -nrs $RPM_BUILD_ROOT%{_bindir}/gsiscp \
	$RPM_BUILD_ROOT%{_libexecdir}/gsissh/bin/hpnscp
perl -pi -e "s|$RPM_BUILD_ROOT||g" $RPM_BUILD_ROOT%{_mandir}/man*/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%pre server

%sysusers_create_compat %{SOURCE19}
semanage port -a -t ssh_port_t -p tcp 2222 2>/dev/null || :
%post server

if [ $1 -gt 1 ]; then
    %{_libexecdir}/gsissh/ssh-host-keys-migration.sh
    touch /var/lib/.gsissh-host-keys-migration
fi
%systemd_post gsisshd.service gsisshd.socket
%preun server

%systemd_preun gsisshd.service gsisshd.socket
%postun server

%systemd_postun_with_restart gsisshd.service
if [ $1 -eq 0 ]; then
    semanage port -d -t ssh_port_t -p tcp 2222 2>/dev/null || :
fi
%files -f %{oreon_filedir}/main.list
%files -n gsi-openssh-clients -f %{oreon_filedir}/gsi-openssh-clients.list
%files -n gsi-openssh-keysign -f %{oreon_filedir}/gsi-openssh-keysign.list
%files -n gsi-openssh-server -f %{oreon_filedir}/gsi-openssh-server.list

%changelog

%autochangelog
