%global source0_hash fff8c30764ec5b47236b7e864feb02dfe4f1456c5e3165f98dc24b288b3e58c9

%global _hardened_build 1

Name:           up-imapproxy
Summary:        University of Pittsburgh IMAP Proxy
Version:        1.2.8
Release:        0.34.20250101svn15036%{?dist}
License:        GPL-2.0-or-later
URL:            http://www.imapproxy.org
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  svn export -r 15036 https://svn.code.sf.net/p/squirrelmail/code/trunk/imap_proxy squirrelmail-imap_proxy-1.2.8
#  tar cJvf squirrelmail-imap_proxy-20250101svn15036.tar.gz squirrelmail-imap_proxy-1.2.8
Source0:        squirrelmail-imap_proxy-20250101svn15036.tar.gz
Source1:        imapproxy.service
# handle aarch64 per RH BZ 926684
Patch0:         http://ausil.fedorapeople.org/aarch64/up-imapproxy/up-imapproxy-aarch64.patch
Patch1:         up-imapproxy-ssl.patch
Patch2:         up-imapproxy-configure-c99.patch
Patch3:         up-imapproxy-c99.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  openssl-devel ncurses-devel
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
BuildRequires: systemd

%description
imapproxy was written to compensate for webmail clients that are
unable to maintain persistent connections to an IMAP server. Most
webmail clients need to log in to an IMAP server for nearly every
single transaction. This behaviour can cause tragic performance
problems on the IMAP server. imapproxy tries to deal with this problem
by leaving server connections open for a short time after a webmail
client logs out. When the webmail client connects again, imapproxy
will determine if there's a cached connection available and reuse it
if possible.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n squirrelmail-imap_proxy-%{version}
# handle aarch64
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

# Fixes/changes in default config
# - strip trailing spaces
# - change to Fedora default SSL path
# - use private user/group
# - use chroot in private chroot directory
# - run in foreground for systemd unit
sed -i \
    -e 's/  *$//' \
    -e 's!/usr/share/ssl!/etc/pki/tls!' \
    -e 's/^\(proc_username\) .*/\1 imapproxy/' \
    -e 's/^\(proc_groupname\) .*/\1 imapproxy/' \
    -e 's!^#*\(chroot_directory\) .*!\1 /var/lib/imapproxy!' \
    -e 's/^\(foreground_mode\) .*/\1 yes/' \
    scripts/imapproxy.conf

# Create a sysusers.d config file
cat >up-imapproxy.sysusers.conf <<EOF
u imapproxy - 'IMAP proxy service' /var/lib/imapproxy -
EOF

%build
%configure CFLAGS="%{optflags} -std=gnu17"
[ -d bin ] || mkdir bin
make %{?_smp_mflags}

%install
# The install-* Makefile targets don't support DESTDIR syntax, so work around.
install -D -m 0644 -p scripts/imapproxy.conf \
    $RPM_BUILD_ROOT%{_sysconfdir}/imapproxy.conf
install -D -m 0755 -p %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/imapproxy.service
install -d -m 0755 $RPM_BUILD_ROOT%{_sbindir}
install -D -m 0755 bin/* $RPM_BUILD_ROOT%{_sbindir}

# Use a private chroot directory, also home directory for private user
install -d -m 0755 $RPM_BUILD_ROOT/var/lib/imapproxy

install -m0644 -D up-imapproxy.sysusers.conf %{buildroot}%{_sysusersdir}/up-imapproxy.conf

%post
%systemd_post imapproxy.service

%preun
%systemd_preun imapproxy.service

%postun
%systemd_postun_with_restart imapproxy.service 

%files
%doc COPYING ChangeLog README README.ssl
%doc copyright
%config(noreplace) %{_sysconfdir}/imapproxy.conf
%{_unitdir}/imapproxy.service
%{_sbindir}/in.imapproxyd
%{_sbindir}/pimpstat
%dir /var/lib/imapproxy
%{_sysusersdir}/up-imapproxy.conf

%changelog
%autochangelog
