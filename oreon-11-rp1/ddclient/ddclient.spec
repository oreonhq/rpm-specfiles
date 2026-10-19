%global source0_hash 4b37c99ac0011102d7db62f1ece7ff899b06df3d4b172e312703931a3c593c93
%global cachedir %{_localstatedir}/cache/ddclient
%global rundir   %{_rundir}/ddclient
Summary:        Client to update dynamic DNS host entries
Name:              ddclient
Version:           4.0.0
Release:        1%{?dist}
License:           GPL-2.0-or-later
URL:               https://ddclient.net/
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:           ddclient.rwtab
Source2:           ddclient.service
Source3:           ddclient.sysconfig
Source4:           ddclient.NetworkManager
Source5:           ddclient-tmpfiles.conf
BuildArch:         noarch
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd
Requires:          perl(Data::Validate::IP)
Requires:          perl(Digest::SHA1)
Requires:          perl(IO::Socket::INET6)
Requires:          perl(IO::Socket::SSL)
Requires:          perl(JSON::PP)
Conflicts:         NetworkManager < 1.20
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  iproute
BuildRequires:  make
BuildRequires:  perl(HTTP::Daemon)
BuildRequires:  perl(HTTP::Daemon::SSL)
BuildRequires:  perl(HTTP::Message::PSGI)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(IO::Socket::INET6)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::MockModule)
BuildRequires:  perl(Test::TCP)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(version)
BuildRequires:  perl-generators
BuildRequires:  systemd
# /oreon:deps
%description
ddclient is a Perl client used to update dynamic DNS entries for accounts
on many different dynamic DNS services. Features include: Operating as a
daemon, manual and automatic updates, static and dynamic updates, optimized
updates for multiple addresses, MX, wildcards, abuse avoidance, retrying
the failed updates and sending update status to syslog and through e-mail.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1
# Send less mail by default, eg. not on every shutdown.
sed -e 's|^mail=|#mail=|' -i ddclient.conf.in
./autogen

# Create a sysusers.d config file
cat >ddclient.sysusers.conf <<EOF
u ddclient - 'Dynamic DNS Client' %{_localstatedir}/cache/%{name} -
EOF

%build

%configure --runstatedir=%{rundir} --with-confdir='${sysconfdir}'
make
%install
install -D -p -m 755 %{name} $RPM_BUILD_ROOT%{_sbindir}/%{name}
install -D -p -m 600 ddclient.conf \
    $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.conf
install -D -p -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_sysconfdir}/rwtab.d/%{name}
install -D -p -m 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
install -D -p -m 644 %{SOURCE3} \
    $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}
install -D -p -m 755 %{SOURCE4} \
    $RPM_BUILD_ROOT%{_prefix}/lib/NetworkManager/dispatcher.d/50-%{name}
install -D -p -m 644 %{SOURCE5} \
    $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf
mkdir -p $RPM_BUILD_ROOT%{cachedir}
mkdir -p $RPM_BUILD_ROOT%{rundir}
touch $RPM_BUILD_ROOT%{cachedir}/%{name}.cache
chmod 644 sample-*
install -m0644 -D ddclient.sysusers.conf %{buildroot}%{_sysusersdir}/ddclient.conf
%oreon_autofiles main

%check

make VERBOSE=1 check
%post

%systemd_post %{name}.service
if [ $1 == 1 ]; then
    mkdir -p %{rundir}
    chown %{name}:%{name} %{rundir}
fi
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
