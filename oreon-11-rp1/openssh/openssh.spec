# Do we want SELinux & Audit
%if 0%{?!noselinux:1}
%global WITH_SELINUX 1
%else
%global WITH_SELINUX 0
%endif

%global _hardened_build 1

# Do we want to disable building of gnome-askpass? (1=yes 0=no)
%global no_gnome_askpass 0

# Do we want to link against a static libcrypto? (1=yes 0=no)
%global static_libcrypto 0

# Use GTK3 instead of GTK2 in gnome-ssh-askpass
%global gtk3 1

# Build position-independent executables (requires toolchain support)?
%global pie 1

# Do we want kerberos5 support (1=yes 0=no)
%global kerberos5 1

# Do we want libedit support
%global libedit 1

# Reserve options to override askpass settings with:
# rpm -ba|--rebuild --define 'skip_xxx 1'
%{?skip_gnome_askpass:%global no_gnome_askpass 1}

# Add option to build without GTK2 for older platforms with only GTK+.
# Red Hat Linux <= 7.2 and Red Hat Advanced Server 2.1 are examples.
# rpm -ba|--rebuild --define 'no_gtk3 1'
%{?no_gtk3:%global gtk3 0}

%global openssh_ver 10.3p1

Summary: An open source implementation of SSH protocol version 2
Name: openssh
Version: %{openssh_ver}
Release: %autorelease
URL: http://www.openssh.com/portable.html
Source0: https://cdn.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-%{version}.tar.gz
Source1: https://cdn.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-%{version}.tar.gz.asc
Source2: sshd.pam
Source3: gpgkey-736060BA.gpg
Source6: ssh-keycat.pam
Source7: sshd.sysconfig
Source9: sshd@.service
Source10: sshd.socket
Source11: sshd.service
Source12: sshd-keygen@.service
Source13: sshd-keygen
Source15: sshd-keygen.target
Source16: ssh-agent.service
Source17: ssh-agent.socket
Source19: openssh-server-systemd-sysusers.conf
Source20: ssh-host-keys-migration.sh
Source21: ssh-host-keys-migration.service
Source22: parallel_test.sh
Source23: parallel_test.Makefile

Patch0001: 0001-Add-SELinux-role-and-MLS-Multi-Level-Security-suppor.patch
Patch0002: 0002-Implement-SELinux-environment-variable-setup-for-sub.patch
Patch0003: 0003-Pass-inetd-flags-and-auth-context-to-subprocess-call.patch
Patch0004: 0004-openssh-6.6p1-keycat.patch
Patch0005: 0005-openssh-6.6p1-allow-ip-opts.patch
Patch0006: 0006-openssh-5.9p1-ipv6man.patch
Patch0007: 0007-openssh-5.8p2-sigpipe.patch
Patch0008: 0008-openssh-7.2p2-x11.patch
Patch0009: 0009-openssh-5.1p1-askpass-progress.patch
Patch0010: 0010-openssh-4.3p2-askpass-grab-info.patch
Patch0011: 0011-openssh-8.7p1-redhat.patch
Patch0012: 0012-openssh-7.8p1-UsePAM-warning.patch
Patch0013: 0013-openssh-9.6p1-gssapi-keyex.patch
Patch0014: 0014-openssh-6.6p1-force_krb.patch
Patch0015: 0015-openssh-7.7p1-gssapi-new-unique.patch
Patch0016: 0016-openssh-7.2p2-k5login_directory.patch
Patch0017: 0017-openssh-6.6p1-kuserok.patch
Patch0018: 0018-openssh-6.4p1-fromto-remote.patch
Patch0019: 0019-openssh-6.6.1p1-log-in-chroot.patch
Patch0020: 0020-openssh-6.6.1p1-scp-non-existing-directory.patch
Patch0021: 0021-openssh-6.6p1-GSSAPIEnablek5users.patch
Patch0022: 0022-openssh-6.8p1-sshdT-output.patch
Patch0023: 0023-openssh-6.7p1-sftp-force-permission.patch
Patch0024: 0024-openssh-7.2p2-s390-closefrom.patch
Patch0025: 0025-openssh-7.5p1-sandbox.patch
Patch0026: 0026-openssh-7.8p1-scp-ipv6.patch
Patch0027: 0027-openssh-8.0p1-crypto-policies.patch
Patch0028: 0028-openssh-8.0p1-openssl-kdf.patch
Patch0029: 0029-openssh-8.2p1-visibility.patch
Patch0030: 0030-openssh-8.2p1-x11-without-ipv6.patch
Patch0031: 0031-openssh-8.0p1-preserve-pam-errors.patch
Patch0032: 0032-openssh-8.7p1-scp-kill-switch.patch
Patch0033: 0033-openssh-8.7p1-recursive-scp.patch
Patch0034: 0034-openssh-8.7p1-ibmca.patch
Patch0035: 0035-openssh-7.6p1-audit.patch
Patch0036: 0036-openssh-7.1p2-audit-race-condition.patch
Patch0037: 0037-openssh-9.0p1-audit-log.patch
Patch0038: 0038-openssh-7.7p1-fips.patch
Patch0039: 0039-openssh-8.7p1-negotiate-supported-algs.patch
Patch0040: 0040-openssh-9.0p1-evp-fips-kex.patch
Patch0041: 0041-openssh-8.7p1-nohostsha1proof.patch
Patch0042: 0042-openssh-9.9p1-separate-keysign.patch
Patch0043: 0043-openssh-9.9p1-openssl-mlkem.patch
Patch0044: 0044-openssh-9.9p2-error_processing.patch
Patch0045: 0045-Provide-better-error-for-non-supported-private-keys.patch
Patch0046: 0046-Ignore-bad-hostkeys-in-known_hosts-file.patch
Patch0047: 0047-support-authentication-indicators-in-GSSAPI.patch
Patch0048: 0048-NIST-curves-hybrid-KEX-implementation.patch
Patch0049: 0049-openssh-7.3p1-x11-max-displays.patch
Patch0050: 0050-Fix-ssh-pkcs11-client-helper-termination.patch
Patch0051: 0051-openssh-10.2p1-pam-auth.patch
Patch0052: 0052-gssapi-s4u.patch
Patch0053: 0053-openssh-10.2p1-pkcs11-uri.patch
Patch0054: 0054-gssapi-tests.patch
Patch1000: 1000-openssh-6.7p1-coverity.patch

License: BSD-3-Clause AND BSD-2-Clause AND ISC AND SSH-OpenSSH AND ssh-keyscan AND snprintf AND LicenseRef-Fedora-Public-Domain AND X11-distribute-modifications-variant
Requires: openssl-libs >= 1:3.5.0

%if ! %{no_gnome_askpass}
BuildRequires: libX11-devel
%if %{gtk3}
BuildRequires: gtk3-devel
%else
BuildRequires: gtk2-devel
%endif
%endif

BuildRequires: autoconf, automake, perl-interpreter, perl-generators, zlib-devel
BuildRequires: audit-libs-devel >= 2.0.5
BuildRequires: util-linux, groff
BuildRequires: pam-devel
BuildRequires: openssl-devel >= 1:3.5.0
BuildRequires: perl-podlators
BuildRequires: systemd-devel
BuildRequires: systemd-rpm-macros
BuildRequires: gcc make
BuildRequires: p11-kit-devel
BuildRequires: libfido2-devel
BuildRequires: libxcrypt-devel
Obsoletes: openssh-ldap < 8.3p1-4
Obsoletes: openssh-cavs < 8.4p1-5

%if %{kerberos5}
BuildRequires: krb5-devel
BuildRequires: krb5-workstation
BuildRequires: krb5-server
BuildRequires: nss_wrapper
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
Summary: An open source SSH client applications
Requires: openssh = %{version}-%{release}
Requires: crypto-policies >= 20220824-1

%package keysign
Summary: A helper program used for host-based authentication
Requires: openssh = %{version}-%{release}

%package server
Summary: An open source SSH server daemon
Requires: openssh = %{version}-%{release}
Requires: /sbin/nologin
Requires(pre): /usr/sbin/useradd
Requires: pam >= 1.0.1-3
Requires: crypto-policies >= 20220824-1
%{?systemd_requires}

%package keycat
Summary: A mls keycat backend for openssh
Requires: openssh = %{version}-%{release}

%package askpass
Summary: A passphrase dialog for OpenSSH and X
Requires: openssh = %{version}-%{release}

%package sk-dummy
Summary: OpenSSH SK driver for test purposes
Requires: openssh = %{version}-%{release}

%description
SSH (Secure SHell) is a program for logging into and executing
commands on a remote machine. SSH is intended to replace rlogin and
rsh, and to provide secure encrypted communications between two
untrusted hosts over an insecure network. X11 connections and
arbitrary TCP/IP ports can also be forwarded over the secure channel.

OpenSSH is OpenBSD's version of the last free version of SSH, bringing
it up to date in terms of security and features.

This package includes the core files necessary for both the OpenSSH
client and server. To make this package useful, you should also
install openssh-clients, openssh-server, or both.

%description clients
OpenSSH is a free version of SSH (Secure SHell), a program for logging
into and executing commands on a remote machine. This package includes
the clients necessary to make encrypted connections to SSH servers.

%description keysign
OpenSSH is a free version of SSH (Secure SHell), a program for logging
into and executing commands on a remote machine. ssh-keysign is a
helper program used for host-based authentication disabled by default.

%description server
OpenSSH is a free version of SSH (Secure SHell), a program for logging
into and executing commands on a remote machine. This package contains
the secure shell daemon (sshd). The sshd daemon allows SSH clients to
securely connect to your SSH server.

%description keycat
OpenSSH mls keycat is backend for using the authorized keys in the
openssh in the mls mode.

%description askpass
OpenSSH is a free version of SSH (Secure SHell), a program for logging
into and executing commands on a remote machine. This package contains
an X11 passphrase dialog for OpenSSH.

%description sk-dummy
This package contains a test SK driver used for OpenSSH test purposes

%prep
gpgv2 --quiet --keyring %{SOURCE3} %{SOURCE1} %{SOURCE0}
%autosetup -T -b 0 -p1

autoreconf

%build
%set_build_flags
%if %{pie}
%ifarch s390 s390x sparc sparcv9 sparc64
CFLAGS="$CFLAGS -fPIC"
%else
CFLAGS="$CFLAGS -fpic"
%endif
SAVE_LDFLAGS="$LDFLAGS"
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
	--sysconfdir=%{_sysconfdir}/ssh \
	--libexecdir=%{_libexecdir}/openssh \
	--datadir=%{_datadir}/openssh \
	--with-default-path=/usr/local/bin:/usr/bin \
	--with-superuser-path=/usr/local/bin:/usr/bin \
	--with-privsep-path=%{_datadir}/empty.sshd \
	--disable-strip \
	--without-zlib-version-check \
	--with-ipaddr-display \
	--with-pie=no \
	--without-hardening `# The hardening flags are configured by system` \
	--with-default-pkcs11-provider=yes \
	--with-security-key-builtin=yes \
	--with-pam \
%if %{WITH_SELINUX}
	--with-selinux --with-audit=linux \
	--with-sandbox=seccomp_filter \
%endif
%if %{kerberos5}
	--with-kerberos5${krb5_prefix:+=${krb5_prefix}} \
%else
	--without-kerberos5 \
%endif
%if %{libedit}
	--with-libedit
%else
	--without-libedit
%endif

%make_build
make regress/misc/sk-dummy/sk-dummy.so

# Define a variable to toggle gtk2/gtk3 building.  This is necessary
# because RPM doesn't handle nested %%if statements.
%if %{gtk3}
	gtk3=yes
%else
	gtk3=no
%endif

%if ! %{no_gnome_askpass}
pushd contrib
if [ $gtk3 = yes ] ; then
	CFLAGS="$CFLAGS %{?__global_ldflags}" \
	    make gnome-ssh-askpass3
	mv gnome-ssh-askpass3 gnome-ssh-askpass
else
	CFLAGS="$CFLAGS %{?__global_ldflags}" \
	    make gnome-ssh-askpass2
	mv gnome-ssh-askpass2 gnome-ssh-askpass
fi
popd
%endif

%check
#OPENSSL_CONF=/dev/null %{SOURCE22} %{SOURCE23}  # ./parallel_tests.sh parallel_tests.Makefile
make tests

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p -m755 $RPM_BUILD_ROOT%{_sysconfdir}/ssh
mkdir -p -m755 $RPM_BUILD_ROOT%{_sysconfdir}/ssh/ssh_config.d
mkdir -p -m755 $RPM_BUILD_ROOT%{_sysconfdir}/ssh/sshd_config.d
mkdir -p -m755 $RPM_BUILD_ROOT%{_libexecdir}/openssh
%make_install

install -d $RPM_BUILD_ROOT/etc/pam.d/
install -d $RPM_BUILD_ROOT/etc/sysconfig/
install -d $RPM_BUILD_ROOT%{_libexecdir}/openssh
install -m644 %{SOURCE2} $RPM_BUILD_ROOT/etc/pam.d/sshd
install -m644 %{SOURCE6} $RPM_BUILD_ROOT/etc/pam.d/ssh-keycat
install -m644 %{SOURCE7} $RPM_BUILD_ROOT/etc/sysconfig/sshd
install -m644 ssh_config_redhat $RPM_BUILD_ROOT%{_sysconfdir}/ssh/ssh_config.d/50-redhat.conf
install -m644 sshd_config_redhat_cp $RPM_BUILD_ROOT%{_sysconfdir}/ssh/sshd_config.d/40-redhat-crypto-policies.conf
install -m644 sshd_config_redhat $RPM_BUILD_ROOT%{_sysconfdir}/ssh/sshd_config.d/50-redhat.conf
install -d -m755 $RPM_BUILD_ROOT/%{_unitdir}
install -m644 %{SOURCE9} $RPM_BUILD_ROOT/%{_unitdir}/sshd@.service
install -m644 %{SOURCE10} $RPM_BUILD_ROOT/%{_unitdir}/sshd.socket
install -m644 %{SOURCE11} $RPM_BUILD_ROOT/%{_unitdir}/sshd.service
install -m644 %{SOURCE12} $RPM_BUILD_ROOT/%{_unitdir}/sshd-keygen@.service
install -m644 %{SOURCE15} $RPM_BUILD_ROOT/%{_unitdir}/sshd-keygen.target
install -d -m755 $RPM_BUILD_ROOT/%{_userunitdir}
install -m644 %{SOURCE16} $RPM_BUILD_ROOT/%{_userunitdir}/ssh-agent.service
install -m644 %{SOURCE17} $RPM_BUILD_ROOT/%{_userunitdir}/ssh-agent.socket
install -m744 %{SOURCE13} $RPM_BUILD_ROOT/%{_libexecdir}/openssh/sshd-keygen
install -m755 contrib/ssh-copy-id $RPM_BUILD_ROOT%{_bindir}/
install contrib/ssh-copy-id.1 $RPM_BUILD_ROOT%{_mandir}/man1/
install -d -m711 ${RPM_BUILD_ROOT}/%{_datadir}/empty.sshd
install -p -D -m 0644 %{SOURCE19} %{buildroot}%{_sysusersdir}/openssh-server.conf
# Migration service/script for Fedora 38 change to remove group ownership for standard host keys
# See https://fedoraproject.org/wiki/Changes/SSHKeySignSuidBit
install -m744 %{SOURCE20} $RPM_BUILD_ROOT/%{_libexecdir}/openssh/ssh-host-keys-migration.sh
# Pulled-in via a `Wants=` in `sshd.service` & `sshd@.service`
install -m644 %{SOURCE21} $RPM_BUILD_ROOT/%{_unitdir}/ssh-host-keys-migration.service
install -d $RPM_BUILD_ROOT/%{_localstatedir}/lib
touch $RPM_BUILD_ROOT/%{_localstatedir}/lib/.ssh-host-keys-migration

%if ! %{no_gnome_askpass}
install contrib/gnome-ssh-askpass $RPM_BUILD_ROOT%{_libexecdir}/openssh/gnome-ssh-askpass
%endif

%if ! %{no_gnome_askpass}
ln -s gnome-ssh-askpass $RPM_BUILD_ROOT%{_libexecdir}/openssh/ssh-askpass
install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/
install -m 755 contrib/redhat/gnome-ssh-askpass.csh $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/
install -m 755 contrib/redhat/gnome-ssh-askpass.sh $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/
%endif

%if %{no_gnome_askpass}
rm -f $RPM_BUILD_ROOT/etc/profile.d/gnome-ssh-askpass.*
%endif

perl -pi -e "s|$RPM_BUILD_ROOT||g" $RPM_BUILD_ROOT%{_mandir}/man*/*

install -m 755 -d $RPM_BUILD_ROOT%{_libdir}/sshtest/
install -m 755 regress/misc/sk-dummy/sk-dummy.so $RPM_BUILD_ROOT%{_libdir}/sshtest

%pre server
%sysusers_create_compat %{SOURCE19}

%post server
if [ $1 -gt 1 ]; then
    # In the case of an upgrade (never true on OSTree systems) run the migration
    # script for Fedora 38 to remove group ownership for host keys.
    %{_libexecdir}/openssh/ssh-host-keys-migration.sh
    # Prevent the systemd unit that performs the same service (useful for
    # OSTree systems) from running.
    touch /var/lib/.ssh-host-keys-migration
fi
%systemd_post sshd.service sshd.socket
# Migration scriptlet for Fedora 31 and 32 installations to sshd_config
# drop-in directory (in F32+).
# Do this only if the file generated by anaconda exists, contains our config
# directive and sshd_config contains include directive as shipped in our package
%global sysconfig_anaconda /etc/sysconfig/sshd-permitrootlogin
test -f %{sysconfig_anaconda} && \
  test ! -f /etc/ssh/sshd_config.d/01-permitrootlogin.conf && \
  grep -q '^PERMITROOTLOGIN="-oPermitRootLogin=yes"' %{sysconfig_anaconda} && \
  grep -q '^Include /etc/ssh/sshd_config.d/\*.conf' /etc/ssh/sshd_config && \
  echo "PermitRootLogin yes" >> /etc/ssh/sshd_config.d/25-permitrootlogin.conf && \
  rm %{sysconfig_anaconda} || :

%preun server
%systemd_preun sshd.service sshd.socket

%postun server
%systemd_postun_with_restart sshd.service

%post clients
%systemd_user_post ssh-agent.service
%systemd_user_post ssh-agent.socket

%preun clients
%systemd_user_preun ssh-agent.service
%systemd_user_preun ssh-agent.socket

%files
%license LICENCE
%doc CREDITS ChangeLog OVERVIEW PROTOCOL* README README.platform README.privsep README.tun README.dns TODO
%attr(0755,root,root) %dir %{_sysconfdir}/ssh
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/ssh/moduli
%attr(0755,root,root) %{_bindir}/ssh-keygen
%attr(0644,root,root) %{_mandir}/man1/ssh-keygen.1*
%attr(0755,root,root) %dir %{_libexecdir}/openssh

%files clients
%attr(0755,root,root) %{_bindir}/ssh
%attr(0644,root,root) %{_mandir}/man1/ssh.1*
%attr(0755,root,root) %{_bindir}/scp
%attr(0644,root,root) %{_mandir}/man1/scp.1*
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/ssh/ssh_config
%dir %attr(0755,root,root) %{_sysconfdir}/ssh/ssh_config.d/
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/ssh/ssh_config.d/50-redhat.conf
%attr(0644,root,root) %{_mandir}/man5/ssh_config.5*
%attr(0755,root,root) %{_bindir}/ssh-agent
%attr(0755,root,root) %{_bindir}/ssh-add
%attr(0755,root,root) %{_bindir}/ssh-keyscan
%attr(0755,root,root) %{_bindir}/sftp
%attr(0755,root,root) %{_bindir}/ssh-copy-id
%attr(0755,root,root) %{_libexecdir}/openssh/ssh-pkcs11-helper
%attr(0755,root,root) %{_libexecdir}/openssh/ssh-sk-helper
%attr(0644,root,root) %{_mandir}/man1/ssh-agent.1*
%attr(0644,root,root) %{_mandir}/man1/ssh-add.1*
%attr(0644,root,root) %{_mandir}/man1/ssh-keyscan.1*
%attr(0644,root,root) %{_mandir}/man1/sftp.1*
%attr(0644,root,root) %{_mandir}/man1/ssh-copy-id.1*
%attr(0644,root,root) %{_mandir}/man8/ssh-pkcs11-helper.8*
%attr(0644,root,root) %{_mandir}/man8/ssh-sk-helper.8*
%attr(0644,root,root) %{_userunitdir}/ssh-agent.service
%attr(0644,root,root) %{_userunitdir}/ssh-agent.socket

%files keysign
%attr(4555,root,root) %{_libexecdir}/openssh/ssh-keysign
%attr(0644,root,root) %{_mandir}/man8/ssh-keysign.8*

%files server
%dir %attr(0711,root,root) %{_datadir}/empty.sshd
%attr(0755,root,root) %{_sbindir}/sshd
%attr(0755,root,root) %{_libexecdir}/openssh/sshd-session
%attr(0755,root,root) %{_libexecdir}/openssh/sshd-auth
%attr(0755,root,root) %{_libexecdir}/openssh/sftp-server
%attr(0755,root,root) %{_libexecdir}/openssh/sshd-keygen
%attr(0644,root,root) %{_mandir}/man5/sshd_config.5*
%attr(0644,root,root) %{_mandir}/man5/moduli.5*
%attr(0644,root,root) %{_mandir}/man8/sshd.8*
%attr(0644,root,root) %{_mandir}/man8/sftp-server.8*
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/ssh/sshd_config
%dir %attr(0700,root,root) %{_sysconfdir}/ssh/sshd_config.d/
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/ssh/sshd_config.d/40-redhat-crypto-policies.conf
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/ssh/sshd_config.d/50-redhat.conf
%attr(0644,root,root) %config(noreplace) /etc/pam.d/sshd
%attr(0640,root,root) %config(noreplace) /etc/sysconfig/sshd
%attr(0644,root,root) %{_unitdir}/sshd.service
%attr(0644,root,root) %{_unitdir}/sshd@.service
%attr(0644,root,root) %{_unitdir}/sshd.socket
%attr(0644,root,root) %{_unitdir}/sshd-keygen@.service
%attr(0644,root,root) %{_unitdir}/sshd-keygen.target
%attr(0644,root,root) %{_sysusersdir}/openssh-server.conf
%attr(0644,root,root) %{_unitdir}/ssh-host-keys-migration.service
%attr(0744,root,root) %{_libexecdir}/openssh/ssh-host-keys-migration.sh
%ghost %attr(0644,root,root) %{_localstatedir}/lib/.ssh-host-keys-migration

%files keycat
%doc HOWTO.ssh-keycat
%attr(0755,root,root) %{_libexecdir}/openssh/ssh-keycat
%attr(0644,root,root) %config(noreplace) /etc/pam.d/ssh-keycat

%if ! %{no_gnome_askpass}
%files askpass
%attr(0644,root,root) %{_sysconfdir}/profile.d/gnome-ssh-askpass.*
%attr(0755,root,root) %{_libexecdir}/openssh/gnome-ssh-askpass
%{_libexecdir}/openssh/ssh-askpass
%endif

%files sk-dummy
%attr(0755,root,root) %{_libdir}/sshtest/sk-dummy.so

%changelog
* Fri May 08 2026 Oreon Packaging Team <packaging@oreonhq.com> - 10.3p1-1
- Rebase to 10.3p1 with refreshed downstream patch stack
- Use HTTPS for portable tarball and signature
