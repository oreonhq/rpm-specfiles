%global source0_hash 91e60f10745ea4f9c27b9e57619a1bf246ab9a88ea1b88c4f39f8af607e2dbae
Summary:        Transparent SMTP/LMTP proxy filter using spamassassin
Name: spampd
Version: 2.61
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: http://www.worlddesign.com/index.cfm/rd/mta/spampd.htm
Source0:        https://github.com/mpaperno/spampd/archive/refs/tags/%{name}-%{version}.tar.gz
Source1: spampd.service
Source2: README.systemd
Source3: spampd.sysconfig
Patch0:  spampd-2.61-no-pid-file.patch
Requires: perl(Net::Server)
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
BuildArch: noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl-Pod-Html
BuildRequires:  perl-generators
BuildRequires:  perl-podlators
BuildRequires:  systemd-units
# /oreon:deps
%description
Spampd is a program used within an e-mail delivery system to scan messages for
possible Unsolicited Commercial E-mail (UCE, aka spam) content. It uses
SpamAssassin (SA) to do the actual message scanning. Spampd acts as a
transparent SMTP/LMTP proxy between two mail servers, and during the
transaction it passes the mail through SA. If SA decides the mail could be
spam, then spampd will ask SA to add some headers and a report to the message
indicating it's spam and why.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .no-pid-file
%{__rm} -f spampd.html
%{__chmod} -x changelog.txt
%{__cp} %{SOURCE2} .

# Create a sysusers.d config file
cat >spampd.sysusers.conf <<EOF
u spampd - - /var/spool/spampd -
EOF

%build

pod2man spampd.pod spampd.8
pod2html --infile=spampd.pod --outfile=spampd.html
%install
%{__rm} -rf %{buildroot}
%{__install} -D -p -m 0755 spampd.pl \
    %{buildroot}%{_sbindir}/spampd
%{__install} -D -p -m 0644 spampd.8 \
    %{buildroot}%{_mandir}/man8/spampd.8
%{__install} -D -p -m 0644 %{SOURCE1} \
    %{buildroot}%{_unitdir}/spampd.service
%{__install} -D -p -m 0644 %{SOURCE3} \
    %{buildroot}%{_sysconfdir}/sysconfig/spampd
%{__mkdir_p} %{buildroot}/var/spool/spampd
install -m0644 -D spampd.sysusers.conf %{buildroot}%{_sysusersdir}/spampd.conf
%oreon_autofiles main

%post

%systemd_post spampd.service
%preun

%systemd_preun spampd.service
%postun

%systemd_postun_with_restart spampd.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
