%global source0_hash ff4d9543f8f5cb0356c30ffe22255d942ac6128da734c376de211c02630fa5f7
%global confdir %{_sysconfdir}/postfix
Name:              postgrey
Version:           1.37
Release:        1%{?dist}
Summary:        Postfix Greylisting Policy Server
License:           GPL-2.0-or-later
URL:               http://postgrey.schweikert.ch/
Source0:        http://postgrey.schweikert.ch/pub/postgrey-%{version}.tar.gz
Source1:           postgrey.service
Source2:           README-rpm
Source3:           postgrey.sysconfig
BuildArch:         noarch
Recommends:        postfix
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd
# oreon:deps
BuildRequires:  perl-generators
BuildRequires:  perl-podlators
BuildRequires:  systemd
# /oreon:deps
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

pod2man \
    --center="Postgrey Policy Server for Postfix" \
    --section="8" \
    --release="Postgrey %{version}" \
    postgrey > postgrey.8
%install
mkdir -p %{buildroot}%{confdir}
install -pm0644 postgrey_whitelist_{clients,recipients} \
    %{buildroot}%{confdir}/
echo "# Clients that should not be greylisted.  See postgrey(8)." \
    > %{buildroot}%{confdir}/postgrey_whitelist_clients.local
install -pDm0755 postgrey %{buildroot}%{_sbindir}/postgrey
mkdir -p %{buildroot}%{_localstatedir}/spool/postfix/postgrey
install -pDm0644 %{SOURCE1} \
    %{buildroot}%{_unitdir}/postgrey.service
install -pDm0644 %{SOURCE3} \
    %{buildroot}%{_sysconfdir}/sysconfig/postgrey
install -pDm0644 postgrey.8 \
    %{buildroot}%{_mandir}/man8/postgrey.8
install -pDm0755 contrib/postgreyreport \
    %{buildroot}%{_sbindir}/postgreyreport
install -m0644 -D postgrey.sysusers.conf %{buildroot}%{_sysusersdir}/postgrey.conf
%oreon_autofiles main

%post

%systemd_post postgrey.service
%preun

%systemd_preun postgrey.service
%postun

%systemd_postun postgrey.service
%triggerun -- postgrey < 1.34-3

/usr/bin/systemd-sysv-convert --save postgrey >/dev/null 2>&1 ||:
/sbin/chkconfig --del postgrey >/dev/null 2>&1 || :
/bin/systemctl try-restart postgrey.service >/dev/null 2>&1 || :
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
