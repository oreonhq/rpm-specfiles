%global source0_hash ccc42c0419937959263fa1dbd16dafc18c56b984c03562d2937ce56a60f798b2

# gsi-openssh is openssh with support for GSI authentication
# This gsi-openssh specfile is based on the openssh specfile

# Do we want SELinux & Audit
%if 0%{?!noselinux:1}
%global WITH_SELINUX 1
%else
%global WITH_SELINUX 0
%endif

%global _hardened_build 1

# Build position-independent executables (requires toolchain support)?
%global pie 1

# Do we want kerberos5 support (1=yes 0=no)
# It is not possible to support kerberos5 and GSI at the same time
%global kerberos5 0

# Do we want GSI support (1=yes 0=no)
%global gsi 1

# Do we want libedit support
%global libedit 1

%global openssh_ver 10.2p1

Summary: An implementation of the SSH protocol with GSI authentication
Name: gsi-openssh
Version: %{openssh_ver}
Release: 1%{?dist}
Provides: gsissh = %{version}-%{release}
Obsoletes: gsissh < 5.8p2-2
URL: http://www.openssh.com/portable.html
Source0: https://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-%{version}.tar.gz
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

#https://bugzilla.mindrot.org/show_bug.cgi?id=1641 (WONTFIX)
Patch0001: 0001-openssh-7.8p1-role-mls.patch
Patch0002: 0002-openssh-6.6p1-keycat.patch
#https://bugzilla.mindrot.org/show_bug.cgi?id=1644
Patch0003: 0003-openssh-6.6p1-allow-ip-opts.patch
#(drop?) https://bugzilla.mindrot.org/show_bug.cgi?id=1925
Patch0004: 0004-openssh-5.9p1-ipv6man.patch
Patch0005: 0005-openssh-5.8p2-sigpipe.patch
Patch0006: 0006-openssh-7.2p2-x11.patch
Patch0007: 0007-openssh-5.1p1-askpass-progress.patch
#https://bugzilla.redhat.com/show_bug.cgi?id=198332
Patch0008: 0008-openssh-4.3p2-askpass-grab-info.patch
#https://bugzilla.mindrot.org/show_bug.cgi?id=1635 (WONTFIX)
Patch0009: 0009-openssh-8.7p1-redhat.patch
# warn users for unsupported UsePAM=no (#757545)
Patch0010: 0010-openssh-7.8p1-UsePAM-warning.patch
# GSSAPI Key Exchange (RFC 4462 + RFC 8732)
Patch0011: 0011-openssh-9.6p1-gssapi-keyex.patch
#http://www.mail-archive.com/kerberos@mit.edu/msg17591.html
Patch0012: 0012-openssh-6.6p1-force_krb.patch
# Improve ccache handling in openssh (#991186, #1199363, #1566494)
# https://bugzilla.mindrot.org/show_bug.cgi?id=2775
Patch0013: 0013-openssh-7.7p1-gssapi-new-unique.patch
# Respect k5login_directory option in krk5.conf (#1328243)
Patch0014: 0014-openssh-7.2p2-k5login_directory.patch
#https://bugzilla.mindrot.org/show_bug.cgi?id=1780
Patch0015: 0015-openssh-6.6p1-kuserok.patch
# Use tty allocation for a remote scp (#985650)
Patch0016: 0016-openssh-6.4p1-fromto-remote.patch
# log via monitor in chroots without /dev/log (#2681)
Patch0017: 0017-openssh-6.6.1p1-log-in-chroot.patch
# scp file into non-existing directory (#1142223)
Patch0018: 0018-openssh-6.6.1p1-scp-non-existing-directory.patch
# add new option GSSAPIEnablek5users and disable using ~/.k5users by default (#1169843)
# CVE-2014-9278
Patch0019: 0019-openssh-6.6p1-GSSAPIEnablek5users.patch
# apply upstream patch and make sshd -T more consistent (#1187521)
Patch0020: 0020-openssh-6.8p1-sshdT-output.patch
# Add sftp option to force mode of created files (#1191055)
Patch0021: 0021-openssh-6.7p1-sftp-force-permission.patch
# make s390 use /dev/ crypto devices -- ignore closefrom
Patch0022: 0022-openssh-7.2p2-s390-closefrom.patch
# Pass inetd flags for SELinux down to openbsd compat level
Patch0023: 0023-openssh-7.6p1-cleanup-selinux.patch
# Sandbox adjustments for s390 and audit
Patch0024: 0024-openssh-7.5p1-sandbox.patch
# Unbreak scp between two IPv6 hosts (#1620333)
Patch0025: 0025-openssh-7.8p1-scp-ipv6.patch
# Mention crypto-policies in manual pages (#1668325)
# clarify rhbz#2068423 on the man page of ssh_config
Patch0026: 0026-openssh-8.0p1-crypto-policies.patch
# Use OpenSSL KDF (#1631761)
Patch0027: 0027-openssh-8.0p1-openssl-kdf.patch
# sk-dummy.so built with -fvisibility=hidden does not work
Patch0028: 0028-openssh-8.2p1-visibility.patch
# Do not break X11 without IPv6
Patch0029: 0029-openssh-8.2p1-x11-without-ipv6.patch
# sshd provides PAM an incorrect error code (#1879503)
Patch0030: 0030-openssh-8.0p1-preserve-pam-errors.patch
# Implement kill switch for SCP protocol
Patch0031: 0031-openssh-8.7p1-scp-kill-switch.patch
# Workaround for lack of sftp_realpath in older versions of RHEL
# https://bugzilla.redhat.com/show_bug.cgi?id=2038854
# https://github.com/openssh/openssh-portable/pull/299
# downstream only
Patch0032: 0032-openssh-8.7p1-recursive-scp.patch
# Downstream alias for MinRSABits
Patch0033: 0033-openssh-8.7p1-minrsabits.patch
# downstream only, IBMCA tentative fix
# From https://bugzilla.redhat.com/show_bug.cgi?id=1976202#c14
Patch0034: 0034-openssh-8.7p1-ibmca.patch
#https://bugzilla.mindrot.org/show_bug.cgi?id=1402
# https://bugzilla.redhat.com/show_bug.cgi?id=1171248
# record pfs= field in CRYPTO_SESSION audit event
Patch0035: 0035-openssh-7.6p1-audit.patch
# Audit race condition in forked child (#1310684)
Patch0036: 0036-openssh-7.1p2-audit-race-condition.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2049947
Patch0037: 0037-openssh-9.0p1-audit-log.patch
Patch0038: 0038-openssh-7.7p1-fips.patch
# Add missing options from ssh_config into ssh manpage
# upstream bug:
# https://bugzilla.mindrot.org/show_bug.cgi?id=3455
Patch0039: 0039-openssh-8.7p1-ssh-manpage.patch
# Don't propose disallowed algorithms during hostkey negotiation
# upstream MR:
# https://github.com/openssh/openssh-portable/pull/323
Patch0040: 0040-openssh-8.7p1-negotiate-supported-algs.patch
Patch0041: 0041-openssh-9.0p1-evp-fips-kex.patch
Patch0042: 0042-openssh-8.7p1-nohostsha1proof.patch
Patch0043: 0043-openssh-9.9p1-separate-keysign.patch
Patch0044: 0044-openssh-9.9p1-openssl-mlkem.patch
# https://www.openwall.com/lists/oss-security/2025/02/22/1
Patch0045: 0045-openssh-9.9p2-error_processing.patch
# https://github.com/openssh/openssh-portable/pull/564
Patch0046: 0046-Provide-better-error-for-non-supported-private-keys.patch
# https://github.com/openssh/openssh-portable/pull/567
Patch0047: 0047-Ignore-bad-hostkeys-in-known_hosts-file.patch
# https://github.com/openssh/openssh-portable/pull/500
Patch0048: 0048-support-authentication-indicators-in-GSSAPI.patch
Patch0049: 0049-NIST-curves-hybrid-KEX-implementation.patch
# landed upstream, to be removed after 10.3
Patch0050: 0050-Provide-a-way-to-disable-GSSAPIDelegateCredentials-s.patch
# Move MAX_DISPLAYS to a configuration option (#1341302)
Patch0051: 0051-openssh-7.3p1-x11-max-displays.patch
# PKCS#11 URIs (upstream #2817, seriously reworked on rebasing to 10.2)
# https://github.com/Jakuje/openssh-portable/commits/jjelen-pkcs11
Patch0052: 0052-openssh-10.2p1-pkcs11-uri.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2423900
Patch0053: 0053-openssh-10.2p1-pam-auth.patch
#https://bugzilla.mindrot.org/show_bug.cgi?id=2581
Patch1000: 1000-openssh-6.7p1-coverity.patch

# This is the patch that adds GSI support
# Based on hpn_isshd-gsi.7.5p1b.patch from Globus upstream
Patch2000: 2000-openssh-10.2p1-gsissh.patch

# This is the HPN patch
# Based on https://github.com/rapier1/hpn-ssh/ tag: hpn-18.8.0
Patch2001: 2001-openssh-10.2p1-hpn-18.8.0.patch

License: BSD-3-Clause AND BSD-2-Clause AND ISC AND SSH-OpenSSH AND ssh-keyscan AND sprintf AND LicenseRef-Fedora-Public-Domain AND X11-distribute-modifications-variant
Requires: /sbin/nologin
Requires: openssl-libs >= 3.5.0

BuildRequires: autoconf, automake, perl-interpreter, perl-generators, zlib-devel
BuildRequires: audit-libs-devel >= 2.0.5
BuildRequires: util-linux, groff
BuildRequires: pam-devel
BuildRequires: openssl-devel >= 3.5.0
BuildRequires: systemd-devel
BuildRequires: systemd-rpm-macros
BuildRequires: gcc make
BuildRequires: p11-kit-devel
BuildRequires: libfido2-devel
BuildRequires: libxcrypt-devel
Recommends: p11-kit

%if %{kerberos5}
BuildRequires: krb5-devel
%endif

%if %{gsi}
BuildRequires: globus-gss-assist-devel >= 8
BuildRequires: globus-gssapi-gsi-devel >= 12.12
BuildRequires: globus-common-devel >= 14
%endif

%if %{libedit}
BuildRequires: libedit-devel ncurses-devel
%endif

%if %{WITH_SELINUX}
Requires: libselinux >= 2.3-5
BuildRequires: libselinux-devel >= 2.3-5
Requires: audit-libs >= 1.0.8
BuildRequires: audit-libs >= 1.0.8
%endif

BuildRequires: xauth
# for tarball signature verification
BuildRequires: gnupg2

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
%if %{pie}
%ifarch s390 s390x sparc sparcv9 sparc64
CFLAGS="$CFLAGS -fPIC"
%else
CFLAGS="$CFLAGS -fpic"
%endif
LDFLAGS="$LDFLAGS -pie -z relro -z now"

export CFLAGS
export LDFLAGS

%endif
%if %{kerberos5}
if test -r /etc/profile.d/krb5-devel.sh ; then
	source /etc/profile.d/krb5-devel.sh
fi
krb5_prefix=`krb5-config --prefix`
if test "$krb5_prefix" != "%{_prefix}" ; then
	CPPFLAGS="$CPPFLAGS -I${krb5_prefix}/include -I${krb5_prefix}/include/gssapi"; export CPPFLAGS
	CFLAGS="$CFLAGS -I${krb5_prefix}/include -I${krb5_prefix}/include/gssapi"
	LDFLAGS="$LDFLAGS -L${krb5_prefix}/%{_lib}"; export LDFLAGS
else
	krb5_prefix=
	CPPFLAGS="-I%{_includedir}/gssapi"; export CPPFLAGS
	CFLAGS="$CFLAGS -I%{_includedir}/gssapi"
fi
%endif

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
%if %{WITH_SELINUX}
	--with-selinux --with-audit=linux \
	--with-sandbox=seccomp_filter \
%endif
%if %{kerberos5}
	--with-kerberos5${krb5_prefix:+=${krb5_prefix}} \
%else
	--without-kerberos5 \
%endif
%if %{gsi}
	--with-gsi \
%else
	--without-gsi \
%endif
%if %{libedit}
	--with-libedit
%else
	--without-libedit
%endif

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
# Migration service/script for Fedora 38 change to remove group ownership for standard host keys
# See https://fedoraproject.org/wiki/Changes/SSHKeySignSuidBit
install -m744 %{SOURCE20} $RPM_BUILD_ROOT/%{_libexecdir}/gsissh/ssh-host-keys-migration.sh
# Pulled-in via a `Wants=` in `gsisshd.service` & `gsisshd@.service`
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

# Add scp and hpnscp symlinks in gsisshd's path
mkdir $RPM_BUILD_ROOT%{_libexecdir}/gsissh/bin
ln -nrs $RPM_BUILD_ROOT%{_bindir}/gsiscp \
	$RPM_BUILD_ROOT%{_libexecdir}/gsissh/bin/scp
ln -nrs $RPM_BUILD_ROOT%{_bindir}/gsiscp \
	$RPM_BUILD_ROOT%{_libexecdir}/gsissh/bin/hpnscp

perl -pi -e "s|$RPM_BUILD_ROOT||g" $RPM_BUILD_ROOT%{_mandir}/man*/*

%pre server
%sysusers_create_compat %{SOURCE19}
semanage port -a -t ssh_port_t -p tcp 2222 2>/dev/null || :

%post server
if [ $1 -gt 1 ]; then
    # In the case of an upgrade (never true on OSTree systems) run the migration
    # script for Fedora 38 to remove group ownership for host keys.
    %{_libexecdir}/gsissh/ssh-host-keys-migration.sh
    # Prevent the systemd unit that performs the same service (useful for
    # OSTree systems) from running.
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

%files
%license LICENCE
%doc CREDITS ChangeLog OVERVIEW PROTOCOL* README HPN-README README.platform README.privsep README.tun README.dns README.sshd-and-gsisshd TODO
%attr(0755,root,root) %dir %{_sysconfdir}/gsissh
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/gsissh/moduli
%attr(0755,root,root) %{_bindir}/gsissh-keygen
%attr(0644,root,root) %{_mandir}/man1/gsissh-keygen.1*
%attr(0755,root,root) %dir %{_libexecdir}/gsissh

%files clients
%attr(0755,root,root) %{_bindir}/gsissh
%attr(0644,root,root) %{_mandir}/man1/gsissh.1*
%attr(0755,root,root) %{_bindir}/gsiscp
%attr(0644,root,root) %{_mandir}/man1/gsiscp.1*
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/gsissh/ssh_config
%dir %attr(0755,root,root) %{_sysconfdir}/gsissh/ssh_config.d/
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/gsissh/ssh_config.d/50-redhat.conf
%attr(0644,root,root) %{_mandir}/man5/gsissh_config.5*
%attr(0755,root,root) %{_bindir}/gsisftp
%attr(0755,root,root) %{_libexecdir}/gsissh/ssh-sk-helper
%attr(0644,root,root) %{_mandir}/man1/gsisftp.1*
%attr(0644,root,root) %{_mandir}/man8/gsissh-sk-helper.8*
%attr(0755,root,root) %dir %{_libexecdir}/gsissh/bin
%{_libexecdir}/gsissh/bin/scp
%{_libexecdir}/gsissh/bin/hpnscp

%files keysign
%attr(4555,root,root) %{_libexecdir}/gsissh/ssh-keysign
%attr(0644,root,root) %{_mandir}/man8/gsissh-keysign.8*

%files server
%dir %attr(0711,root,root) %{_datadir}/empty.sshd
%attr(0755,root,root) %{_sbindir}/gsisshd
%attr(0755,root,root) %{_libexecdir}/gsissh/sshd-session
%attr(0755,root,root) %{_libexecdir}/gsissh/sshd-auth
%attr(0755,root,root) %{_libexecdir}/gsissh/sftp-server
%attr(0755,root,root) %{_libexecdir}/gsissh/sshd-keygen
%attr(0644,root,root) %{_mandir}/man5/gsisshd_config.5*
%attr(0644,root,root) %{_mandir}/man5/gsimoduli.5*
%attr(0644,root,root) %{_mandir}/man8/gsisshd.8*
%attr(0644,root,root) %{_mandir}/man8/gsisftp-server.8*
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/gsissh/sshd_config
%dir %attr(0700,root,root) %{_sysconfdir}/gsissh/sshd_config.d/
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/gsissh/sshd_config.d/40-redhat-crypto-policies.conf
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/gsissh/sshd_config.d/50-redhat.conf
%attr(0644,root,root) %config(noreplace) /etc/pam.d/gsisshd
%attr(0640,root,root) %config(noreplace) /etc/sysconfig/gsisshd
%attr(0644,root,root) %{_unitdir}/gsisshd.service
%attr(0644,root,root) %{_unitdir}/gsisshd@.service
%attr(0644,root,root) %{_unitdir}/gsisshd.socket
%attr(0644,root,root) %{_unitdir}/gsisshd-keygen@.service
%attr(0644,root,root) %{_unitdir}/gsisshd-keygen.target
%attr(0644,root,root) %{_sysusersdir}/%{name}-server.conf
%attr(0644,root,root) %{_unitdir}/gsissh-host-keys-migration.service
%attr(0744,root,root) %{_libexecdir}/gsissh/ssh-host-keys-migration.sh
%ghost %attr(0644,root,root) %{_localstatedir}/lib/.gsissh-host-keys-migration

%changelog
%autochangelog
