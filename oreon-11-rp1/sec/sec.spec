%global source0_hash 77fd945980d15ca07f94a9cad6484677f5d3fe8ded5da12ec2c0c444ae7b0994
Name:           sec
Version:        2.9.4
Release:        1%{?dist}
Summary:        Simple Event Correlator script to filter log file entries
License:        GPL-2.0-or-later
URL:            https://simple-evcorr.github.io/
Source0:        https://github.com/simple-evcorr/sec/releases/download/%{version}/sec-%{version}.tar.gz
Source1:        sec.service
Source2:        sec@.service
Source3:        sec.logrotate
Source4:        sec.sysconfig
Source5:        conf.README
BuildArch:      noarch
Requires:       logrotate
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd
# oreon:deps
BuildRequires:  perl-generators
BuildRequires:  systemd
# /oreon:deps
%description
SEC is a simple event correlation tool that reads lines from files, named
pipes, or standard input, and matches the lines with regular expressions,
Perl subroutines, and other patterns for recognizing input events.
Events are then correlated according to the rules in configuration files,
producing output events by executing user-specified shell commands, by
writing messages to pipes or files, etc.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%install
install -D -m 0755 -p sec        %{buildroot}%{_bindir}/sec
install -D -m 0644 -p sec.man    %{buildroot}%{_mandir}/man1/sec.1
install -D -m 0644 -p %{SOURCE1} %{buildroot}%{_unitdir}/sec.service
install -D -m 0644 -p %{SOURCE2} %{buildroot}%{_unitdir}/sec@.service
install -D -m 0644 -p %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/sec
install -D -m 0644 -p %{SOURCE4} %{buildroot}%{_sysconfdir}/sysconfig/sec
install -D -m 0644 -p %{SOURCE5} %{buildroot}%{_sysconfdir}/%{name}/README
chmod 0644 contrib/convert.pl contrib/swatch2sec.pl
%oreon_autofiles main

%post

%systemd_post sec.service
%preun

%systemd_preun sec.service
%postun

%systemd_postun_with_restart sec.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
