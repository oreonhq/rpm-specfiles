%global source0_hash 02e2ac647c918463202cbe607bb95557a4f7fd237069124333c54da5b2bbb76b

%if 0%{?rhel} && 0%{?rhel} <= 7
# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e '/^.*\/usr\/lib\/rpm\/brp-python-bytecompile.*$/d')
%endif

Name: btrbk
Version: 0.32.6
Release: 11%{?dist}
Summary: Tool for creating snapshots and remote backups of btrfs sub-volumes
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL: https://digint.ch/btrbk/
Source0: https://digint.ch/download/%{name}/releases/%{name}-%{version}.tar.xz
Source1: btrbk-logrotate
BuildArch: noarch
BuildRequires: python3-devel
%if 0%{?rhel} && 0%{?rhel} == 7
BuildRequires: systemd
%else
BuildRequires: systemd-rpm-macros
%endif
BuildRequires: perl-generators
BuildRequires: rubygem-asciidoctor
BuildRequires: asciidoc
BuildRequires: xmlto
BuildRequires: make
Requires: btrfs-progs >= 4.12
%if 0%{?rhel} && 0%{?rhel} <= 7
Requires: openssh-clients
Requires: pv
Requires: mbuffer
%else
Recommends: openssh-clients
Recommends: pv
Recommends: mbuffer
%endif

%description
Backup tool for btrfs sub-volumes, using a configuration file, allows
creation of backups from multiple sources to multiple destinations,
with ssh and flexible retention policy support (hourly, daily,
weekly, monthly)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%install
%make_install
rm -rf %{buildroot}/%{_docdir}/%{name}
%if 0%{?rhel} && 0%{?rhel} <= 7
find %{buildroot}%{_datadir}/%{name} -type f -exec sed -i '1s=^#!/usr/bin/\(python\|env python\)[23]\?=#!%{__python3}=' {} +
%else
%py3_shebang_fix %{buildroot}%{_datadir}/%{name}
%endif
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

%post
%systemd_post %{name}.service
%systemd_post %{name}.timer

%preun
%systemd_preun %{name}.service
%systemd_preun %{name}.timer

%postun
%systemd_postun_with_restart %{name}.service
%systemd_postun_with_restart %{name}.timer

%files
%doc README.md ChangeLog doc/FAQ.md doc/upgrade_to_v0.23.0.md
%license COPYING
%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/btrbk.conf.example
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_unitdir}/%{name}.*
%{_datadir}/%{name}
%{_bindir}/btrbk
%{_bindir}/lsbtr
%{_datadir}/bash-completion/completions/btrbk
%{_datadir}/bash-completion/completions/lsbtr
%{_mandir}/man1/btrbk.1*
%{_mandir}/man1/lsbtr.1*
%{_mandir}/man1/ssh_filter_btrbk.1*
%{_mandir}/man5/btrbk.conf.5*

%changelog
%autochangelog
