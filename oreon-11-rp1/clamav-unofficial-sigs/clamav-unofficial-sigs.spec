%global source0_hash f42f9d68e111f892bfd71393e869e53c806f48966c768d219925de6652960c50
%if 0%{?fedora} >= 17 || 0%{?rhel} >= 7 || 0%{?oreon} >= 11
%global with_systemd 1
%global clamupdateuser clamupdate
%global clamupdategrp  clamupdate
%else
%global with_systemd 0
%global clamupdateuser clam-update
%global clamupdategrp  clam-update
%endif
Name:           clamav-unofficial-sigs
Version:        7.2.5
Release:        17%{?dist}
Summary:        Scripts to download unofficial clamav signatures
Group:          Applications/System
License:        BSD-3-Clause
URL:            https://github.com/extremeshok/%{name}
Source0:        https://github.com/extremeshok/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        clamav-unofficial-sigs.cron
Source2:        clamav-unofficial-sigs.logrotate
Source3:        clamav-unofficial-sigs.man8
Patch1:         clamav-unofficial-sigs-grep-backslash.patch
Patch2:         https://patch-diff.githubusercontent.com/raw/extremeshok/clamav-unofficial-sigs/pull/390.patch#/clamav-unofficial-sigs-7.2.5-urlhaus.patch
BuildArch:      noarch
Requires:       clamav clamav-update rsync gnupg diffutils curl bind-utils
# oreon:deps
BuildRequires:  bind-utils
BuildRequires:  rsync
BuildRequires:  systemd
# /oreon:deps
%description
This package contains scripts and configuration files
that provide the capability to download, test, and 
update the 3rd-party signature databases provide by 
Sanesecurity, SecuriteInfo, MalwarePatrol, OITC, 
INetMsg and ScamNailer.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}-%{version}
%autopatch -p1
sed -i -e '/user_configuration_complete/ s/^#//' config/user.conf
sed -i -e '/ExecStart/ s^/usr/local/sbin^/usr/sbin^' systemd/clamav-unofficial-sigs.service

%build

cp %{SOURCE1} clamav-unofficial-sigs.cron
cp %{SOURCE2} clamav-unofficial-sigs.logrotate
cp %{SOURCE3} clamav-unofficial-sigs.man8
sed -i -e 's^/usr/bin/env bash^/bin/bash^g' clamav-unofficial-sigs.sh
sed -i -e 's^/usr/bin/bash^/bin/bash^g' clamav-unofficial-sigs.cron
sed -i -e '/^#pkg_mgr/ s/^#//;s/""/"dnf"/' config/master.conf
sed -i -e '/ExecStart=/ s|/usr/local/sbin|%{_sbindir}|' systemd/clamav-unofficial-sigs.service
sed -i -e '/^enable_yararules/ s/yes/no/' config/master.conf
%install
rm -rf %{buildroot}
install -d -p %{buildroot}%{_unitdir}
install -d -p %{buildroot}%{_sysconfdir}/%{name}
install -d -p %{buildroot}%{_sbindir}
install -d -p %{buildroot}%{_localstatedir}/log/%{name}
install -d -p %{buildroot}%{_localstatedir}/lib/%{name}
install -d -p %{buildroot}%{_sysconfdir}/cron.d
install -d -p %{buildroot}%{_sysconfdir}/logrotate.d
install -d -p %{buildroot}%{_mandir}/man8
install -p -m0755 clamav-unofficial-sigs.sh %{buildroot}%{_sbindir}/clamav-unofficial-sigs.sh
%if 0%{?fedora} >= 17 || 0%{?rhel} >= 7 || 0%{?oreon} >= 11
install -p -m0644 config/packaging/os.centos7.conf %{buildroot}%{_sysconfdir}/%{name}/os.conf
%else
install -p -m0644 config/packaging/os.centos6.conf %{buildroot}%{_sysconfdir}/%{name}/os.conf
%endif
install -p -m0644 config/user.conf %{buildroot}%{_sysconfdir}/%{name}/user.conf
install -p -m0644 config/master.conf %{buildroot}%{_sysconfdir}/%{name}/master.conf
install -Dp -m 0644 systemd/clamav-unofficial-sigs.service %{buildroot}%{_unitdir}/clamav-unofficial-sigs.service
install -Dp -m 0644 systemd/clamav-unofficial-sigs.timer %{buildroot}%{_unitdir}/clamav-unofficial-sigs.timer
install -p -m0644 clamav-unofficial-sigs.cron %{buildroot}%{_sysconfdir}/cron.d/clamav-unofficial-sigs
install -p -m0644 clamav-unofficial-sigs.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/clamav-unofficial-sigs
install -p -m0644 clamav-unofficial-sigs.man8 %{buildroot}%{_mandir}/man8/clamav-unofficial-sigs.8
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
