%global source0_hash d4ae5d4f5f13d136f77e7aaff2cdc80fcd3b9a171ac31c28adbae2f4643c04a8
Name:           ngircd
Version:        28
Release:        1%{?dist}
Summary:        Next Generation IRC Daemon
License:        GPL-2.0-or-later
URL:            http://ngircd.barton.de/
Source0:        http://ngircd.barton.de/pub/ngircd/ngircd-%{version}.tar.gz
Source1:        ngircd.init
Source2:        ngircd.service
Patch0:         ngircd-fedora.patch
Patch1:         ngircd-cipher.patch
Patch2:         ngircd-service.patch
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
# oreon:deps
BuildRequires:  avahi-compat-howl-devel
BuildRequires:  expect
BuildRequires:  gcc
BuildRequires:  gnutls-devel
BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  pam-devel
BuildRequires:  procps-ng
BuildRequires:  systemd
BuildRequires:  telnet
BuildRequires:  zlib-devel
# /oreon:deps
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
%oreon_autofiles main

%check

make check
%post

%systemd_post ngircd.service
%preun

%systemd_preun ngircd.service
%postun

%systemd_postun_with_restart ngircd.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
