%global source0_hash 519e639da18762dc084ee214ad57d1c8c425cd480f222b754a3593def6f0f473

Summary: Port Scan Attack Detector (psad) watches for suspect traffic
Name: psad
Version: 2.4.6
Release: 24%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: https://www.cipherdyne.org/psad/
Source0: https://www.cipherdyne.org/psad/download/psad-%{version}.tar.bz2
Source1: https://www.cipherdyne.org/psad/download/psad-%{version}.tar.bz2.asc
# curl -O https://www.cipherdyne.org/signing_key ; gpg --import ./signing_key
# gpg --export --export-options export-minimal 4D6644A9DA036904BDA2CB90E6C9E3350D3E7410 > 4D6644A9DA036904BDA2CB90E6C9E3350D3E7410.gpg
Source2: 4D6644A9DA036904BDA2CB90E6C9E3350D3E7410.gpg
Source4: psad-tmpfiles.conf
# patch to:
# * allow specifying Fedora CFLAGS
# * use system whois
# * set some sensible defaults in /etc/psad/psad.conf
Patch0: psad-fedora.patch
# https://github.com/mrash/psad/issues/53
Patch1: psad-issue53.patch
BuildArch: noarch
BuildRequires: %{_bindir}/gpgv2
BuildRequires: perl-generators
BuildRequires: systemd-rpm-macros
# works with system one, but doesn't crash or break without it
%if 0%{?fedora}
Recommends: %{_bindir}/whois
Recommends: %{_sbindir}/sendmail
Recommends: /bin/mail
%endif
Requires: %{_bindir}/killall
Requires: /bin/ps
Requires: gzip
Requires: iproute
Requires: iptables
# The automatic dependency generator doesn't find these
Requires: perl(Bit::Vector)
Requires: perl(Carp::Clan)
Requires: perl(Date::Calc)
Requires: perl(IPTables::ChainMgr)
Requires: perl(IPTables::Parse)
Requires: perl(NetAddr::IP)
Requires: perl(Storable)
Requires: perl(Unix::Syslog)
Requires(post): policycoreutils >= 2.4
Requires(post): %{_sbindir}/semodule
Requires(postun): %{_sbindir}/semodule

%description
Port Scan Attack Detector (psad) is a lightweight
system daemon written in Perl designed to work with Linux
iptables firewalling code to detect port scans and other suspect traffic.  It
features a set of highly configurable danger thresholds (with sensible
defaults provided), verbose alert messages that include the source,
destination, scanned port range, begin and end times, tcp flags and
corresponding nmap options, reverse DNS info, email and syslog alerting,
automatic blocking of offending ip addresses via dynamic configuration of
iptables rulesets, and passive operating system fingerprinting.  In addition,
psad incorporates many of the tcp, udp, and icmp signatures included in the
snort intrusion detection system (https://www.snort.org) to detect highly
suspect scans for various backdoor programs (e.g. EvilFTP, GirlFriend,
SubSeven), DDoS tools (mstream, shaft), and advanced port scans (syn, fin,
xmas) which are easily leveraged against a machine via nmap.  psad can also
alert on snort signatures that are logged via fwsnort
(https://www.cipherdyne.org/fwsnort/), which makes use of the
iptables string match module to detect application layer signatures.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gpgv2 --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%setup -q
%patch -P0 -p1 -b .f
%patch -P1 -p1 -b .i53
# remove bundled stuff
rm -r deps/{Bit-Vector,Carp-Clan,Date-Calc,IPTables-ChainMgr,IPTables-Parse,NetAddr-IP,Storable,Unix-Syslog,whois}

%build
echo Nothing to build.

%install
install  -dm755 %{buildroot}{%{_mandir}/man{1,8},%{_sbindir},%{_sysconfdir}/%{name}}
install  -pm755 -t %{buildroot}%{_sbindir} psad
install -Dpm755 fwcheck_psad.pl %{buildroot}%{_sbindir}/fwcheck_psad
install -Dpm755 nf2csv %{buildroot}%{_bindir}/nf2csv
install -Dpm644 misc/logrotate.psad %{buildroot}%{_sysconfdir}/logrotate.d/psad
install  -pm644 -t %{buildroot}%{_sysconfdir}/%{name} \
 auto_dl \
 icmp_types \
 icmp6_types \
 ip_options \
 pf.os \
 posf \
 protocols \
 psad.conf \
 signatures \
 snort_rule_dl \

install -pm644 -t %{buildroot}%{_mandir}/man8 doc/{fwcheck_psad,psad}.8
install -pm644 -t %{buildroot}%{_mandir}/man1 doc/nf2csv.1

cp -pr deps/snort_rules %{buildroot}%{_sysconfdir}/%{name}

install -Dpm644 init-scripts/systemd/psad.service %{buildroot}%{_unitdir}/psad.service
install -Dpm644 %{S:4} %{buildroot}%{_tmpfilesdir}/psad.conf

# upstream's installer creates those as root-accessible only
install  -dm700 %{buildroot}/{var/{lib,log},run}/%{name}
touch %{buildroot}/var/lib/%{name}/psadfifo
touch %{buildroot}/run/%{name}/psad.cmd

%post
# missing from current SELinux policy (Fedora: #1174309, RHEL7: #1389191)
TMPDIR=$(%{_bindir}/mktemp -d)
cat >> $TMPDIR/psad-rpm.cil << __EOF__
(allow firewalld_t psad_t(dbus (send_msg)))
(allow psad_t firewalld_t(dbus (send_msg)))
(allow psad_t journalctl_exec_t(file (execute execute_no_trans map open read)))
(allow psad_t kernel_t (system (module_request)))
(allow psad_t psad_var_log_t(file (read rename unlink write)))
(allow psad_t self (capability2 (perfmon)))
(allow psad_t self (netlink_tcpdiag_socket (bind create setopt)))
(allow psad_t sysfs_t (dir (read)))
(allow psad_t sysfs_t (file (getattr open read)))
(allow psad_t syslogd_var_run_t (dir (read watch)))
(allow psad_t var_log_t (dir (watch)))
(dontaudit psad_t apmd_exec_t(file (getattr)))
(dontaudit psad_t auditd_exec_t(file (getattr)))
(dontaudit psad_t crond_exec_t(file (getattr)))
(dontaudit psad_t dovecot_exec_t(file (getattr)))
(dontaudit psad_t getty_exec_t(file (getattr)))
(dontaudit psad_t httpd_exec_t(file (getattr)))
(dontaudit psad_t init_exec_t(file (getattr)))
(dontaudit psad_t load_policy_t (dir (getattr search)))
(dontaudit psad_t load_policy_t (file (open read)))
(dontaudit psad_t load_policy_t (lnk_file (read)))
(dontaudit psad_t mandb_t (dir (getattr search)))
(dontaudit psad_t mandb_t (file (open read)))
(dontaudit psad_t radvd_exec_t (file (getattr)))
(dontaudit psad_t rngd_exec_t (file (getattr)))
(dontaudit psad_t rpcd_exec_t (file (getattr)))
(dontaudit psad_t self (capability (dac_override sys_admin sys_ptrace sys_resource)))
(dontaudit psad_t self (cap_userns (sys_ptrace)))
(dontaudit psad_t sshd_exec_t (file (getattr)))
(dontaudit psad_t syslogd_exec_t (file (getattr)))
(dontaudit psad_t systemd_logind_exec_t (file (getattr)))
(dontaudit psad_t systemd_machined_exec_t (file (getattr)))
(dontaudit psad_t udev_exec_t (file (getattr)))
(dontaudit psad_t virtd_exec_t (file (getattr)))
(dontaudit psad_t xserver_log_t (dir (search)))
__EOF__
%{_sbindir}/semodule -i $TMPDIR/psad-rpm.cil
rm -rf $TMPDIR
%systemd_post psad.service
exit 0

%preun
%systemd_preun psad.service

%postun
%systemd_postun_with_restart psad.service
if [ $1 -eq 0 ]; then
  %{_sbindir}/semodule -r psad-rpm > /dev/null || :
fi

%files
%license LICENSE
%doc doc/BENCHMARK ChangeLog CREDITS doc/FW_EXAMPLE_RULES README.md doc/README.SYSLOG doc/SCAN_LOG
%{_bindir}/nf2csv
%{_sbindir}/fwcheck_psad
%{_sbindir}/psad
%{_mandir}/man1/nf2csv.1*
%{_mandir}/man8/fwcheck_psad.8*
%{_mandir}/man8/psad.8*
%{_tmpfilesdir}/psad.conf
%{_unitdir}/psad.service
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/logrotate.d
%config(noreplace) %{_sysconfdir}/logrotate.d/psad
%config(noreplace) %{_sysconfdir}/%{name}/psad.conf
%config(noreplace) %{_sysconfdir}/%{name}/signatures
%config(noreplace) %{_sysconfdir}/%{name}/auto_dl
%config(noreplace) %{_sysconfdir}/%{name}/ip_options
%config(noreplace) %{_sysconfdir}/%{name}/snort_rule_dl
%config(noreplace) %{_sysconfdir}/%{name}/posf
%config(noreplace) %{_sysconfdir}/%{name}/pf.os
%config(noreplace) %{_sysconfdir}/%{name}/icmp_types
%config(noreplace) %{_sysconfdir}/%{name}/icmp6_types
%config(noreplace) %{_sysconfdir}/%{name}/protocols
%dir %{_sysconfdir}/%{name}/snort_rules
%config(noreplace) %{_sysconfdir}/%{name}/snort_rules/*
%dir /var/lib/%{name}
%ghost %attr(0700,root,root) /var/lib/%{name}/psadfifo
%dir /var/log/%{name}
%ghost %dir /run/%{name}
%ghost %attr(0700,root,root) /run/%{name}/psad.cmd

%changelog
%autochangelog
