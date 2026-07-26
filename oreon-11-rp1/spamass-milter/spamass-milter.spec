%global source0_hash 782f1bb3b08a0447cd51ad4b64e7506926739fa9cce537f3cc62aa9b24d46b07

# Use sysusers from Fedora 43 onwards
%if (0%{?rhel} && 0%{?rhel} <= 10) || (0%{?fedora} && 0%{?fedora} <= 42)
%global use_sysusers 0
%else
%global use_sysusers 1
%endif

# Do a hardened build where possible
%global _hardened_build 1

Summary:	Milter (mail filter) for spamassassin
Name:		spamass-milter
Version:	0.4.0
Release:	32%{?dist}
License:	GPL-2.0-or-later
URL:		http://savannah.nongnu.org/projects/spamass-milt/
Source0:	http://savannah.nongnu.org/download/spamass-milt/spamass-milter-%{version}.tar.gz
Source1:	spamass-milter.README.Postfix
Source2:	spamass-milter-tmpfs.conf
Source3:	spamass-milter-postfix-tmpfs.conf
# systemd
Source20:	spamass-milter.service
Source21:	spamass-milter-root.service
Source22:	spamass-milter-sysconfig.systemd
Source23:	spamass-milter-postfix-sysconfig.systemd
# Patches submitted upstream:
# http://savannah.nongnu.org/bugs/?29326
Patch3:		spamass-milter-0.4.0-rcvd.patch
Patch4:		spamass-milter-0.4.0-bits.patch
Patch5:		spamass-milter-0.4.0-group.patch
# Patches not yet submitted upstream
Patch8:		spamass-milter-0.4.0-auth-no-ssf.patch
Patch9:		spamass-milter-0.4.0-quarantine.patch
# Fedora-specific patches
Patch10:	spamass-milter-0.4.0-pathnames.patch
Patch11:	spamass-milter-0.4.0-rundir.patch
BuildRequires:	coreutils
BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	sendmail-milter-devel
BuildRequires:	spamassassin
Requires:	spamassassin, /usr/sbin/sendmail
# Needed for ownership of %%{_tmpfilesdir}
Requires:	systemd

%if !%{use_sysusers}
Requires(pre): glibc-common, shadow-utils
%endif
BuildRequires: systemd
Requires(post): coreutils, systemd
Requires(preun): systemd
Requires(postun): systemd

%description
A milter (Mail Filter) application that pipes incoming mail (including things
received by rmail/UUCP) through SpamAssassin, a highly customizable spam
filter. A milter-compatible MTA such as Sendmail or Postfix is required.

%package postfix
Summary:	Postfix support for spamass-milter
Requires:	%{name} = %{version}-%{release}
Requires(pre):	postfix
Requires(post):	shadow-utils, %{name} = %{version}-%{release}
BuildArch:	noarch

%description postfix
This package adds support for running spamass-milter using a Unix-domain
socket to communicate with the Postfix MTA.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# Copy in general support files
cp -p %{SOURCE1} README.Postfix
cp -p %{SOURCE2} spamass-milter-tmpfs.conf
cp -p %{SOURCE3} spamass-milter-postfix-tmpfs.conf

# Fix Received-header generation (#496763)
%patch -P 3 -b .rcvd

# Add authentication info to dummy Received-header (#496769)
%patch -P 4 -b .bits

# Add -g option for group-writable socket for Postfix support (#452248)
%patch -P 5 -b .group

# Help for users authenticating to Postfix (#730308)
%patch -P 8 -b .postfix-auth

# Local patch to add ability to quarantine messages
%patch -P 9 -b .quarantine

# Local patch for initscript and socket paths
%patch -P 10 -b .pathnames

# With systemd, the runtime directory is /run rather than /var/run
%patch -P 11 -b .rundir

# Copy in systemd files
cp -p %{SOURCE20} %{SOURCE21} %{SOURCE22} %{SOURCE23} .

# Create a sysusers.d config file
cat >spamass-milter.sysusers.conf <<EOF
u sa-milt - 'SpamAssassin Milter' %{_localstatedir}/lib/spamass-milter -
EOF

%build
export SENDMAIL=/usr/sbin/sendmail
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

install -m 755 -d %{buildroot}%{_localstatedir}/lib/spamass-milter
install -m 711 -d %{buildroot}/run/spamass-milter
install -m 750 -d %{buildroot}/run/spamass-milter/postfix
install -m 644 -D spamass-milter.service \
	%{buildroot}%{_unitdir}/spamass-milter.service
install -m 644 -D spamass-milter-root.service \
	%{buildroot}%{_unitdir}/spamass-milter-root.service
install -m 644 -D spamass-milter-sysconfig.systemd \
	%{buildroot}%{_sysconfdir}/sysconfig/spamass-milter
install -m 644 -D spamass-milter-postfix-sysconfig.systemd \
	%{buildroot}%{_sysconfdir}/sysconfig/spamass-milter-postfix

# Make sure /run/spamass-milter{,/postfix} exist at boot time (#656692)
install -m 755 -d %{buildroot}%{_tmpfilesdir}
install -m 644 spamass-milter-tmpfs.conf \
	%{buildroot}%{_tmpfilesdir}/spamass-milter.conf
install -m 644 spamass-milter-postfix-tmpfs.conf \
	%{buildroot}%{_tmpfilesdir}/spamass-milter-postfix.conf

# Create dummy sockets for %%ghost-ing
: > %{buildroot}/run/spamass-milter/spamass-milter.sock
: > %{buildroot}/run/spamass-milter/postfix/sock

# sysusers config
%if %{use_sysusers}
install -m0644 -D spamass-milter.sysusers.conf %{buildroot}%{_sysusersdir}/spamass-milter.conf
%endif

%if !%{use_sysusers}
%pre
getent group sa-milt >/dev/null || groupadd -r sa-milt
getent passwd sa-milt >/dev/null || \
	useradd -r -g sa-milt -d %{_localstatedir}/lib/spamass-milter \
		-s /sbin/nologin -c "SpamAssassin Milter" sa-milt
exit 0
%endif

%post
if [ $1 -eq 1 ]; then
	# Initial installation
	systemctl daemon-reload &>/dev/null || :
	systemctl preset spamass-milter.service &>/dev/null || :
	systemctl preset spamass-milter-root.service &>/dev/null || :
fi

%preun
if [ $1 -eq 0 ]; then
	# Package removal, not upgrade
	systemctl --no-reload disable spamass-milter.service &>/dev/null || :
	systemctl stop spamass-milter.service &>/dev/null || :
	systemctl --no-reload disable spamass-milter-root.service &>/dev/null || :
	systemctl stop spamass-milter-root.service &>/dev/null || :
fi

%postun
systemctl daemon-reload &>/dev/null || :
if [ $1 -ge 1 ]; then
	# Package upgrade, not uninstall
	systemctl try-restart spamass-milter.service &>/dev/null || :
	systemctl try-restart spamass-milter-root.service &>/dev/null || :
fi

%post postfix
# This is needed because the milter needs to "give away" the MTA communication
# socket to the postfix group, and it needs to be a member of the group to do
# that.
usermod -a -G postfix sa-milt || :

%files
%doc AUTHORS ChangeLog NEWS README
%{_mandir}/man1/spamass-milter.1*
%config(noreplace) %{_sysconfdir}/sysconfig/spamass-milter
%{_tmpfilesdir}/spamass-milter.conf
%{_unitdir}/spamass-milter.service
%{_unitdir}/spamass-milter-root.service
%{_sbindir}/spamass-milter
%if %{use_sysusers}
%{_sysusersdir}/spamass-milter.conf
%endif
%dir %attr(-,sa-milt,sa-milt) %{_localstatedir}/lib/spamass-milter/
%dir %attr(-,sa-milt,sa-milt) /run/spamass-milter/
%ghost %attr(-,sa-milt,sa-milt) /run/spamass-milter/spamass-milter.sock

%files postfix
%doc README.Postfix
%{_tmpfilesdir}/spamass-milter-postfix.conf
%config(noreplace) %{_sysconfdir}/sysconfig/spamass-milter-postfix
%dir %attr(-,sa-milt,postfix) /run/spamass-milter/postfix/
%ghost %attr(-,sa-milt,postfix) /run/spamass-milter/postfix/sock

%changelog
%autochangelog
