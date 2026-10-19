%global source0_hash f209265f27451a7c4a1429ffeec2439c6f1ace8a0f3791c50f023655a7ee9eda
%{?python_enable_dependency_generator}
%global modulenames     ec2hibernatepolicy
%global selinuxtype     targeted
%global moduletype      services
%global project         amazon-ec2-hibinit-agent
%global _format() export %1=""; for x in %{modulenames}; do %1+=%2; %1+=" "; done;
Name:           ec2-hibinit-agent
Version:        1.0.9
Release:        1%{?dist}
Summary:        Hibernation setup utility for Amazon EC2
License:        Apache-2.0
URL:            https://github.com/aws/amazon-%{name}
Source0:        https://github.com/aws/%{project}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:         0001-swapon-with-maximum-priority-before-hibernation.patch
Patch2:         0002-rhel-fix-swapoff-breaks-hibernate-process.patch
BuildArch:  noarch
%{?selinux_requires}
Requires: acpid 
Requires: grubby 
Requires: systemd 
Requires: tuned
# oreon:deps
BuildRequires:  make
BuildRequires:  pkgconfig(systemd)
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
An EC2 agent that creates a setup for instance hibernation

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{project}-%{version}
# Fix build with setuptools 62.1
# https://github.com/aws/amazon-ec2-hibinit-agent/issues/24
sed -i "20i packages=[]," setup.py
 
%build

%py3_build
make -C %{_builddir}/%{project}-%{version}/packaging/rhel/ec2hibernatepolicy
%install
%py3_install
mkdir -p %{buildroot}%{python3_sitelib}
mkdir -p "%{buildroot}%{_unitdir}"
mkdir -p %{buildroot}%{_sysconfdir}/acpi/events 
mkdir -p %{buildroot}%{_sharedstatedir}/hibinit-agent
mkdir -p %{buildroot}%{_sysconfdir}/acpi/actions
install -p -m 644 "%{_builddir}/%{project}-%{version}/hibinit-agent.service" %{buildroot}%{_unitdir}
install -p -m 644 "%{_builddir}/%{project}-%{version}/acpid.sleep.conf" %{buildroot}%{_sysconfdir}/acpi/events/sleepconf
mkdir -p %{buildroot}%{_prefix}/lib/systemd/logind.conf.d
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system-sleep
install -p -m 644 "%{_builddir}/%{project}-%{version}/etc/hibinit-config.cfg" %{buildroot}/%{_sysconfdir}/hibinit-config.cfg
install -p -m 644 "%{_builddir}/%{project}-%{version}/packaging/rhel/00-hibinit-agent.conf" %{buildroot}%{_prefix}/lib/systemd/logind.conf.d/00-hibinit-agent.conf
install -p -m 755 "%{_builddir}/%{project}-%{version}/packaging/rhel/acpid.sleep.sh" %{buildroot}%{_sysconfdir}/acpi/actions/sleep.sh
install -p -m 755 "%{_builddir}/%{project}-%{version}/packaging/rhel/sleep-handler.sh" %{buildroot}%{_prefix}/lib/systemd/system-sleep/sleep-handler.sh
mkdir -p  %{buildroot}%{_sysconfdir}/tuned/nothp_profile
install -p -m 644 "%{_builddir}/%{project}-%{version}/packaging/rhel/tuned.conf" %{buildroot}%{_sysconfdir}/tuned/nothp_profile/tuned.conf
%_format MODULES $x.pp.bz2
install -d %{buildroot}%{_datadir}/selinux/packages
install -m 0644 %{_builddir}/%{project}-%{version}/packaging/rhel/ec2hibernatepolicy/$MODULES \
        %{buildroot}%{_datadir}/selinux/packages
%oreon_autofiles main

%pre

%selinux_relabel_pre -s %{selinuxtype}
%post

%systemd_post hibinit-agent.service
%_format MODULES %{_datadir}/selinux/packages/$x.pp.bz2
%selinux_modules_install -s %{selinuxtype} $MODULES
tuned-adm profile nothp_profile
%preun

%systemd_preun hibinit-agent.service
%postun

%systemd_postun_with_restart hibinit-agent.service
tuned-adm profile virtual-guest
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} $MODULES
fi
%posttrans

%selinux_relabel_post -s %{selinuxtype}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
