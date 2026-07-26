%global source0_hash fd38ef21339daf81d6af4a630ba3b2de51a1b42c181843ee77635a5a661fe73c

Name:           ngircd
Version:        27
Release:        7%{?dist}
Summary:        Next Generation IRC Daemon
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://ngircd.barton.de/
Source0:        http://ngircd.barton.de/pub/ngircd/ngircd-%{version}.tar.gz
Source1:        ngircd.init
Source2:        ngircd.service
# Listen only on localhost by default, set user/group
Patch0:         ngircd-fedora.patch
# Use system cipher list
Patch1:         ngircd-cipher.patch
# Patch for service file - no forking, no user/group for SSL key access, add doc,
# add CAP_KILL to allow reload
Patch2:         ngircd-service.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  zlib-devel, avahi-compat-howl-devel
BuildRequires:  gnutls-devel
BuildRequires:  pam-devel
# Needed for tests
BuildRequires:  expect procps-ng telnet openssl
BuildRequires: systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
ngIRCd is a free open source daemon for Internet Relay Chat (IRC), 
developed under the GNU General Public License (GPL). It's written from 
scratch and is not based upon the original IRCd like many others.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Create a sysusers.d config file
cat >ngircd.sysusers.conf <<EOF
u ngircd - 'Next Generation IRC Daemon' /tmp/ -
EOF

%build
%configure \
	--with-syslog \
	--with-zlib \
	--with-epoll \
	--with-gnutls \
	--with-pam \
	--enable-ipv6

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

install -D -m 644 contrib/ngircd.service %{buildroot}%{_unitdir}/ngircd.service
install -D -m 660 doc/sample-ngircd.conf %{buildroot}%{_sysconfdir}/ngircd.conf

mkdir -p %{buildroot}%{_sysconfdir}/pam.d
install -D -m 660 ./contrib/Debian/ngircd.pam %{buildroot}%{_sysconfdir}/pam.d/ngircd

touch  %{buildroot}%{_sysconfdir}/ngircd.motd
rm %{buildroot}%{_docdir}/ngircd/INSTALL.md
mkdir -p %{buildroot}%{_tmpfilesdir}
echo d /run/ngircd 0750 ngircd ngircd - > %{buildroot}%{_tmpfilesdir}/ngircd.conf

install -m0644 -D ngircd.sysusers.conf %{buildroot}%{_sysusersdir}/ngircd.conf

%check
make check

%post
%systemd_post ngircd.service

%preun
%systemd_preun ngircd.service

%postun
%systemd_postun_with_restart ngircd.service

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%config(noreplace) %attr(660, root, ngircd) %{_sysconfdir}/ngircd.conf
%config(noreplace) %attr(660, root, ngircd) %{_sysconfdir}/pam.d/ngircd
%ghost %config(noreplace) %attr(660, root, ngircd) %{_sysconfdir}/ngircd.motd
%{_unitdir}/ngircd.service
%{_sbindir}/ngircd
%{_docdir}/ngircd/
%{_mandir}/man5/ngircd.conf*
%{_mandir}/man8/ngircd.8*
%{_tmpfilesdir}/ngircd.conf
%{_sysusersdir}/ngircd.conf

%changelog
%autochangelog
