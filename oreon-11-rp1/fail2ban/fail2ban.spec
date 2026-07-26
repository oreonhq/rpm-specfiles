%global source0_hash 474fcc25afdaf929c74329d1e4d24420caabeea1ef2e041a267ce19269570bae

%if 0%{?rhel} >= 9
%bcond_with     shorewall
%else
%bcond_without  shorewall
%endif

# RHEL < 10 and Fedora < 40 use file context entries in /var/run
%if %{defined rhel} && 0%{?rhel} < 10
%define legacy_var_run 1
%endif

Name: fail2ban
Version: 1.1.0
Release: 16%{?dist}
Summary: Daemon to ban hosts that cause multiple authentication errors

License: GPL-2.0-or-later
URL: https://www.fail2ban.org
Source0: https://github.com/%{name}/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1: https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz.asc
# Releases are signed by Serg G. Brester (sebres) <info AT sebres.de>.  The
# fingerprint can be found in a signature file:
#   gpg --list-packets fail2ban-1.0.2.tar.gz.asc | grep 'issuer fpr'
#
# The following commands can be used to fetch the signing key via fingerprint
# and extract it:
#   fpr=8738559E26F671DF9E2C6D9E683BF1BEBD0A882C
#   gpg --receive-keys $fpr
#   gpg -a --export-options export-minimal --export $fpr >gpgkey-$fpr.asc
Source2: gpgkey-8738559E26F671DF9E2C6D9E683BF1BEBD0A882C.asc
# SELinux policy
Source3: fail2ban.fc
Source4: fail2ban.if
Source5: fail2ban.te
Source6: Makefile

# Give up being PartOf iptables and ipset for now
# https://bugzilla.redhat.com/show_bug.cgi?id=1379141
# https://bugzilla.redhat.com/show_bug.cgi?id=1573185
Patch0: fail2ban-partof.patch
# default port in jail.conf is not compatible with firewalld-cmd syntax
# https://bugzilla.redhat.com/show_bug.cgi?id=1850164
Patch1: fail2ban-nftables.patch
# Work around encoding issues during tests
Patch2: https://github.com/fail2ban/fail2ban/commit/ab9d41e5309b417a3c7a84fa8f03cf4f93831f1b.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2315252
Patch3: https://patch-diff.githubusercontent.com/raw/fail2ban/fail2ban/pull/3782.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2295265
Patch4: https://patch-diff.githubusercontent.com/raw/fail2ban/fail2ban/pull/3728.patch
# Upstream fix to also catch sshd-session logs
# https://bugzilla.redhat.com/show_bug.cgi?id=2332945
Patch5: https://github.com/fail2ban/fail2ban/commit/54c0effceb998b73545073ac59c479d9d9bf19a4.patch
# Needed for Dovecot change to loging format in 2.4, fixed in f2b version 1.1.1.
# https://bugzilla.redhat.com/show_bug.cgi?id=2426440
Patch6: https://github.com/fail2ban/fail2ban/commit/04ff4c060cdc233af9a6deeb85a6523da0416f31.patch

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools
# For testcases
BuildRequires: python3-inotify
# using a python3_version-based conditional does not work here, so
# this is a proxy for "Python version greater than 3.12". asyncore
# and asynchat were dropped from cpython core in 3.12, these modules
# make them available again. See:
# https://github.com/fail2ban/fail2ban/issues/3487
# https://bugzilla.redhat.com/show_bug.cgi?id=2219991
%if 0%{?fedora} || 0%{?rhel} >= 10
BuildRequires: python3-pyasyncore
BuildRequires: python3-pyasynchat
%endif
BuildRequires: sqlite
BuildRequires: systemd
BuildRequires: selinux-policy-devel
BuildRequires: make
%if 0%{?fedora} || 0%{?rhel} >= 11
BuildRequires: bash-completion-devel
%else
BuildRequires: bash-completion
%endif
BuildRequires: gnupg2

# Default components
Requires: %{name}-firewalld = %{version}-%{release}
Requires: %{name}-sendmail = %{version}-%{release}
Requires: %{name}-server = %{version}-%{release}

%description
Fail2Ban scans log files and bans IP addresses that makes too many password
failures. It updates firewall rules to reject the IP address. These rules can
be defined by the user. Fail2Ban can read multiple log files such as sshd or
Apache web server ones.

Fail2Ban is able to reduce the rate of incorrect authentications attempts
however it cannot eliminate the risk that weak authentication presents.
Configure services to use only two factor or public/private authentication
mechanisms if you really want to protect services.

This is a meta-package that will install the default configuration.  Other
sub-packages are available to install support for other actions and
configurations.

%package selinux
Summary: SELinux policies for Fail2Ban
%{?selinux_requires}
%global modulename fail2ban
%global selinuxtype targeted

%description selinux
SELinux policies for Fail2Ban.

%package server
Summary: Core server component for Fail2Ban
Requires: python3-systemd
Requires: nftables
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires: (%{name}-selinux if selinux-policy-%{selinuxtype})
# see note above in BuildRequires section
%if 0%{?fedora} || 0%{?rhel} >= 10
Requires: python3-pyasyncore
Requires: python3-pyasynchat
%endif

%description server
This package contains the core server components for Fail2Ban with minimal
dependencies.  You can install this directly if you want to have a small
installation and know what you are doing.

%package all
Summary: Install all Fail2Ban packages and dependencies
Requires: %{name}-firewalld = %{version}-%{release}
Requires: %{name}-hostsdeny = %{version}-%{release}
Requires: %{name}-mail = %{version}-%{release}
Requires: %{name}-sendmail = %{version}-%{release}
Requires: %{name}-server = %{version}-%{release}
%if %{with shorewall}
Requires: %{name}-shorewall = %{version}-%{release}
%endif
Requires: perl-interpreter
Requires: python3-inotify
Requires: /usr/bin/whois

%description all
This package installs all of the Fail2Ban packages and dependencies.

%package firewalld
Summary: Firewalld support for Fail2Ban
Requires: %{name}-server = %{version}-%{release}
Requires: firewalld

%description firewalld
This package enables support for manipulating firewalld rules.  This is the
default firewall service in Fedora.

%package hostsdeny
Summary: Hostsdeny (tcp_wrappers) support for Fail2Ban
Requires: %{name}-server = %{version}-%{release}
Requires: ed
Requires: tcp_wrappers

%description hostsdeny
This package enables support for manipulating tcp_wrapper's /etc/hosts.deny
files.

%package tests
Summary: Fail2Ban testcases
Requires: %{name}-server = %{version}-%{release}

%description tests
This package contains Fail2Ban's testscases and scripts.

%package mail
Summary: Mail actions for Fail2Ban
Requires: %{name}-server = %{version}-%{release}
Requires: /usr/bin/mail

%description mail
This package installs Fail2Ban's mail actions.  These are an alternative
to the default sendmail actions.

%package sendmail
Summary: Sendmail actions for Fail2Ban
Requires: %{name}-server = %{version}-%{release}
Requires: /usr/sbin/sendmail

%description sendmail
This package installs Fail2Ban's sendmail actions.  This is the default
mail actions for Fail2Ban.

%if %{with shorewall}
%package shorewall
Summary: Shorewall support for Fail2Ban
Requires: %{name}-server = %{version}-%{release}
Requires: shorewall
Conflicts: %{name}-shorewall-lite

%description shorewall
This package enables support for manipulating shorewall rules.

%package shorewall-lite
Summary: Shorewall lite support for Fail2Ban
Requires: %{name}-server = %{version}-%{release}
Requires: shorewall-lite
Conflicts: %{name}-shorewall

%description shorewall-lite
This package enables support for manipulating shorewall rules.
%endif

%package systemd
Summary: Systemd journal configuration for Fail2Ban
Requires: %{name}-server = %{version}-%{release}

%description systemd
This package configures Fail2Ban to use the systemd journal for its log input
by default.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

# Use Fedora paths
sed -i -e 's/^before = paths-.*/before = paths-fedora.conf/' config/jail.conf

# SELinux sources
cp -p %SOURCE3 %SOURCE4 %SOURCE5 .

%if %{defined legacy_var_run}
sed -i 's|^/run/|/var/run/|' %{name}.fc
%endif

# 2to3 has been removed from setuptools and we already use the binary in
# %%prep.
sed -i "/use_2to3/d" setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
make -f %SOURCE6

%install
%pyproject_install
ln -fs python3 %{buildroot}%{_bindir}/fail2ban-python
mv %{buildroot}%{python3_sitelib}/etc %{buildroot}
mv %{buildroot}%{python3_sitelib}/%{_datadir} %{buildroot}%{_datadir}
rmdir %{buildroot}%{python3_sitelib}%{_prefix}

mkdir -p %{buildroot}%{_unitdir}
# Note that the tests rewrite build/fail2ban.service, but it uses build/ paths before the rewrite
# so we will do our own modification
sed -e 's,@BINDIR@,%{_bindir},' files/fail2ban.service.in > %{buildroot}%{_unitdir}/fail2ban.service
mkdir -p %{buildroot}%{_mandir}/man{1,5}
install -p -m 644 man/*.1 %{buildroot}%{_mandir}/man1
install -p -m 644 man/*.5 %{buildroot}%{_mandir}/man5
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -p -m 644 files/fail2ban-logrotate %{buildroot}%{_sysconfdir}/logrotate.d/fail2ban
install -d -m 0755 %{buildroot}/run/fail2ban/
install -m 0600 /dev/null %{buildroot}/run/fail2ban/fail2ban.pid
install -d -m 0755 %{buildroot}%{_localstatedir}/lib/fail2ban/
mkdir -p %{buildroot}%{_tmpfilesdir}
install -p -m 0644 files/fail2ban-tmpfiles.conf %{buildroot}%{_tmpfilesdir}/fail2ban.conf
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/jail.d

# Remove non-Linux actions
rm %{buildroot}%{_sysconfdir}/%{name}/action.d/*ipfw.conf
rm %{buildroot}%{_sysconfdir}/%{name}/action.d/{ipfilter,pf,ufw}.conf
rm %{buildroot}%{_sysconfdir}/%{name}/action.d/osx-*.conf

# Remove config files for other distros
rm -f %{buildroot}%{_sysconfdir}/fail2ban/paths-{arch,debian,freebsd,opensuse,osx}.conf

# firewalld configuration
cat > %{buildroot}%{_sysconfdir}/%{name}/jail.d/00-firewalld.conf <<EOF
# This file is part of the fail2ban-firewalld package to configure the use of
# the firewalld actions as the default actions.  You can remove this package
# (along with the empty fail2ban meta-package) if you do not use firewalld
[DEFAULT]
banaction = firewallcmd-rich-rules
banaction_allports = firewallcmd-rich-rules
EOF

# systemd journal configuration
cat > %{buildroot}%{_sysconfdir}/%{name}/jail.d/00-systemd.conf <<EOF
# This file is part of the fail2ban-systemd package to configure the use of
# the systemd journal as the default backend.  You can remove this package
# (along with the empty fail2ban meta-package) if you do not want to use the
# journal backend
[DEFAULT]
backend=systemd
EOF

# Remove installed doc, use doc macro instead
rm -r %{buildroot}%{_docdir}/%{name}

# SELinux
# install policy modules
install -d %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}
install -m 0644 %{modulename}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}

#BASH completion
COMPLETIONDIR=%{buildroot}$(pkg-config --variable=completionsdir bash-completion)
%__mkdir_p $COMPLETIONDIR
%__install -p -m 644 files/bash-completion $COMPLETIONDIR/fail2ban

%check
%python3 bin/fail2ban-testcases --verbosity=2 --no-network

%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
fi

%posttrans selinux
%selinux_relabel_post -s %{selinuxtype}

%post server
%systemd_post fail2ban.service

%preun server
%systemd_preun fail2ban.service

%postun server
%systemd_postun_with_restart fail2ban.service

%files

%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/%{name}.pp.bz2
%ghost %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{name}
%license COPYING

%files server
%doc README.md TODO ChangeLog COPYING doc/*.txt
%{_bindir}/fail2ban-client
%{_bindir}/fail2ban-python
%{_bindir}/fail2ban-regex
%{_bindir}/fail2ban-server
%{python3_sitelib}/*
%exclude %{python3_sitelib}/fail2ban/tests
%{_unitdir}/fail2ban.service
%{_datadir}/bash-completion/
%{_mandir}/man1/fail2ban.1*
%{_mandir}/man1/fail2ban-client.1*
%{_mandir}/man1/fail2ban-python.1*
%{_mandir}/man1/fail2ban-regex.1*
%{_mandir}/man1/fail2ban-server.1*
%{_mandir}/man5/*.5*
%config(noreplace) %{_sysconfdir}/fail2ban/
%exclude %{_sysconfdir}/fail2ban/action.d/complain.conf
%exclude %{_sysconfdir}/fail2ban/action.d/hostsdeny.conf
%exclude %{_sysconfdir}/fail2ban/action.d/mail.conf
%exclude %{_sysconfdir}/fail2ban/action.d/mail-buffered.conf
%exclude %{_sysconfdir}/fail2ban/action.d/mail-whois.conf
%exclude %{_sysconfdir}/fail2ban/action.d/mail-whois-lines.conf
%exclude %{_sysconfdir}/fail2ban/action.d/sendmail-*.conf
%exclude %{_sysconfdir}/fail2ban/action.d/shorewall.conf
%exclude %{_sysconfdir}/fail2ban/jail.d/*.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/fail2ban
%{_tmpfilesdir}/fail2ban.conf
%dir %{_localstatedir}/lib/fail2ban/
%dir /run/%{name}/
%ghost %verify(not size mtime md5) /run/%{name}/%{name}.pid

%files all

%files firewalld
%config(noreplace) %{_sysconfdir}/fail2ban/jail.d/00-firewalld.conf

%files hostsdeny
%config(noreplace) %{_sysconfdir}/fail2ban/action.d/hostsdeny.conf

%files tests
%{_bindir}/fail2ban-testcases
%{_mandir}/man1/fail2ban-testcases.1*
%{python3_sitelib}/fail2ban/tests

%files mail
%config(noreplace) %{_sysconfdir}/fail2ban/action.d/complain.conf
%config(noreplace) %{_sysconfdir}/fail2ban/action.d/mail.conf
%config(noreplace) %{_sysconfdir}/fail2ban/action.d/mail-buffered.conf
%config(noreplace) %{_sysconfdir}/fail2ban/action.d/mail-whois.conf
%config(noreplace) %{_sysconfdir}/fail2ban/action.d/mail-whois-lines.conf

%files sendmail
%config(noreplace) %{_sysconfdir}/fail2ban/action.d/sendmail-*.conf

%if %{with shorewall}
%files shorewall
%config(noreplace) %{_sysconfdir}/fail2ban/action.d/shorewall.conf

%files shorewall-lite
%config(noreplace) %{_sysconfdir}/fail2ban/action.d/shorewall.conf
%endif

%files systemd
%config(noreplace) %{_sysconfdir}/fail2ban/jail.d/00-systemd.conf

%changelog
%autochangelog
