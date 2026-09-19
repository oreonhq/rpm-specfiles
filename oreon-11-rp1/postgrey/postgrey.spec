%global source0_hash ff4d9543f8f5cb0356c30ffe22255d942ac6128da734c376de211c02630fa5f7

%global confdir %{_sysconfdir}/postfix

Name:              postgrey
Version:           1.37
Release:           28%{?dist}
Summary:           Postfix Greylisting Policy Server
# File headers only state "GNU GPL", but the LICENSE sections state v2 and "any
# later version"
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:           GPL-2.0-or-later
URL:               http://postgrey.schweikert.ch/
Source0:           http://postgrey.schweikert.ch/pub/postgrey-%{version}.tar.gz
Source1:           postgrey.service
Source2:           README-rpm
Source3:           postgrey.sysconfig
BuildArch:         noarch
BuildRequires:     perl-generators
BuildRequires:     perl-podlators
BuildRequires:     systemd
## Note: If --privacy specified, perl(Digest::SHA) will be needed.
#Requires:          perl(BerkeleyDB)
#Requires:          perl(Fcntl)
#Requires:          perl(Getopt::Long)
#Requires:          perl(IO::Multiplex)
#Requires:          perl(Net::DNS)
#Requires:          perl(Net::Server)
#Requires:          perl(Pod::Usage)
#Requires:          perl(POSIX)
#Requires:          perl(strict)
#Requires:          perl(Sys::Hostname)
#Requires:          perl(Sys::Syslog)
# Requiring postfix for its directories and GID.
Recommends:        postfix
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd

%description
Postgrey is a Postfix policy server implementing greylisting. When a request
for delivery of a mail is received by Postfix via SMTP, the triplet CLIENT_IP /
SENDER / RECIPIENT is built. If it is the first time that this triplet is
seen, or if the triplet was first seen less than 5 minutes, then the mail gets
rejected with a temporary error. Hopefully spammers or viruses will not try
again later, as it is however required per RFC.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# Set default group tp postgrey.
sed -i 's|nogroup|postgrey|g' postgrey
# No perldoc, man is enough.
sed -i 's|POD ||g;s|perldoc|man|g' README
install -pm0644 %{SOURCE2} README.Fedora

# Create a sysusers.d config file
cat >postgrey.sysusers.conf <<EOF
u postgrey - 'Postfix Greylisting Service' %{_localstatedir}/spool/postfix/postgrey -
EOF

%build
# We only have perl scripts, so just "build" the man page.
pod2man \
    --center="Postgrey Policy Server for Postfix" \
    --section="8" \
    --release="Postgrey %{version}" \
    postgrey > postgrey.8

%install
# Configuration files.
mkdir -p %{buildroot}%{confdir}
install -pm0644 postgrey_whitelist_{clients,recipients} \
    %{buildroot}%{confdir}/
# Local whitelist file.
echo "# Clients that should not be greylisted.  See postgrey(8)." \
    > %{buildroot}%{confdir}/postgrey_whitelist_clients.local

# Main script.
install -pDm0755 postgrey %{buildroot}%{_sbindir}/postgrey

# Spool directory.
mkdir -p %{buildroot}%{_localstatedir}/spool/postfix/postgrey

# Systemd service.
install -pDm0644 %{SOURCE1} \
    %{buildroot}%{_unitdir}/postgrey.service

# Sysconfig file.
install -pDm0644 %{SOURCE3} \
    %{buildroot}%{_sysconfdir}/sysconfig/postgrey

# Manpage.
install -pDm0644 postgrey.8 \
    %{buildroot}%{_mandir}/man8/postgrey.8

# Optional report script.
install -pDm0755 contrib/postgreyreport \
    %{buildroot}%{_sbindir}/postgreyreport

install -m0644 -D postgrey.sysusers.conf %{buildroot}%{_sysusersdir}/postgrey.conf

%post
%systemd_post postgrey.service

%preun
%systemd_preun postgrey.service

%postun
%systemd_postun postgrey.service

%triggerun -- postgrey < 1.34-3
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply postgrey
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save postgrey >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del postgrey >/dev/null 2>&1 || :
/bin/systemctl try-restart postgrey.service >/dev/null 2>&1 || :

%files
%doc Changes README README.exim README.Fedora
%license COPYING
%{_unitdir}/postgrey.service
%{_sysconfdir}/sysconfig/postgrey
%config(noreplace) %{confdir}/postgrey_whitelist_clients
%config(noreplace) %{confdir}/postgrey_whitelist_recipients
%config(noreplace) %{confdir}/postgrey_whitelist_clients.local
%{_sbindir}/postgrey
%{_sbindir}/postgreyreport
%{_mandir}/man8/postgrey.8*
%dir %attr(0751,postgrey,postfix) %{_localstatedir}/spool/postfix/postgrey/
%{_sysusersdir}/postgrey.conf

%changelog
%autochangelog
