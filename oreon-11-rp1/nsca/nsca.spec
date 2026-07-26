%global source0_hash 0b36d5c10936f98d278b66c682af95b8e227c5942ad725c4a1949945296f6877

Summary:        Nagios Service Check Acceptor
Name:           nsca
Version:        2.10.3
Release:        4%{?dist}
License:        GPL-2.0-or-later
URL:            http://www.nagios.org/
Source0:        https://github.com/NagiosEnterprises/nsca/releases/download/nsca-%{version}/nsca-%{version}.tar.gz
Source2:        nsca-sysconfig

Patch1:         nsca-2.10.0-confpath.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libmcrypt-devel
BuildRequires:  perl-interpreter
BuildRequires:  systemd-units
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
Requires:       nagios

%description
The purpose of this addon is to allow you to execute Nagios/NetSaint
plugins on a remote host in as transparent a manner as possible.

%package client
Summary:        Client application for sending updates to a nsca server
Requires:       nagios-common

%description client
Client application for sending updates to a nsca server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p1 -b .confpath
# Change defaults in the config file to match the nagios package
sed -i -e "s|^command_file=.*|command_file=%{_localstatedir}/spool/nagios/cmd/nagios.cmd|" \
       -e "s|^alternate_dump_file=.*|alternate_dump_file=%{_localstatedir}/spool/nagios/cmd/nsca.dump|" \
       sample-config/nsca.cfg.in
# Fix typo in unit file
sed -i -e "s/@bindir@/@sbindir@/" nsca.service.in

%build
%configure \
        --sysconfdir="%{_sysconfdir}/nagios" \
        --localstatedir="%{_localstatedir}/log/nagios" \
        --with-nsca-user="nagios" \
        --with-nsca-grp="nagios" \
        --with-nsca-port="5667"
%{make_build} all

%install
install -Dp -m 0755 src/nsca %{buildroot}%{_sbindir}/nsca
install -Dp -m 0755 src/send_nsca %{buildroot}%{_sbindir}/send_nsca
install -Dp -m 0644 sample-config/nsca.cfg %{buildroot}%{_sysconfdir}/nagios/nsca.cfg
install -Dp -m 0644 sample-config/send_nsca.cfg %{buildroot}%{_sysconfdir}/nagios/send_nsca.cfg
install -Dp -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/nsca
install -Dp -m 0644 nsca.service %{buildroot}%{_unitdir}/nsca.service

%post
%systemd_post nsca.service

%preun
%systemd_preun nsca.service

%postun
%systemd_postun_with_restart nsca.service 

%files
%license LICENSE.md
%doc CHANGELOG.md CONTRIBUTORS.md README.md SECURITY.md
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/nagios/nsca.cfg
%config(noreplace) %{_sysconfdir}/sysconfig/nsca
%{_sbindir}/nsca
%{_unitdir}/nsca.service

%files client
%license LICENSE.md
%doc CHANGELOG.md CONTRIBUTORS.md README.md SECURITY.md
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/nagios/send_nsca.cfg
%{_sbindir}/send_nsca

%changelog
%autochangelog
