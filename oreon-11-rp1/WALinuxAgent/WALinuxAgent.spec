%global source0_hash 73f643ea080ece55f48fc04b7d708e391fbfb0ba88c562ab21c398ca3692b99b
%global dracut_modname 97walinuxagent
Name:           WALinuxAgent
Version:        2.16.0.2
Release:        1%{?dist}
Summary:        The Microsoft Azure Linux Agent
License:        Apache-2.0
URL:            https://github.com/Azure/%{name}
Source0:        https://github.com/Azure/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        module-setup.sh
Patch1:         0001-waagent.service-set-ConditionVirtualization-microsof.patch
BuildArch:      noarch
Requires:       %name-udev = %version-%release
%if 0%{?fedora} || (0%{?oreon} >= 11)
Requires:       ntfsprogs
%endif
Requires:       openssh
Requires:       openssh-server
Requires:       openssl
Requires:       parted
Requires:       python3-crypt-r
Requires:       iptables
Requires:       logrotate
Requires(post):  systemd
Requires(preun): systemd
Requires(postun): systemd
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-WALinuxAgent = %{version}-%{release}
# /oreon:deps
%description
The Microsoft Azure Linux Agent supports the provisioning and running of Linux
VMs in the Microsoft Azure cloud. This package should be installed on Linux disk
images that are built to run in the Microsoft Azure environment.

%package udev
Summary:        Udev rules for Microsoft Azure
%description udev
Udev rules specific to Microsoft Azure Virtual Machines.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
rm -rf %{buildroot}/%{python3_sitelib}/{usr,etc}
rm -rf %{buildroot}/%{python3_sitelib}/tests
rm -rf %{buildroot}/%{python3_sitelib}/__main__.py
rm -rf %{buildroot}/%{python3_sitelib}/__pycache__/__main__*.py*
rm -f %{buildroot}%{_sbindir}/waagent2.0
mkdir -p -m 0700 %{buildroot}%{_sharedstatedir}/waagent
mkdir -p %{buildroot}%{_localstatedir}/log
touch %{buildroot}%{_localstatedir}/log/waagent.log
install -m0644 -D --target-directory=%{buildroot}%{_sysconfdir}/ config/waagent.conf
install -m0644 -D --target-directory=%{buildroot}%{_unitdir}/ init/*.slice
install -m0755 -D bin/waagent %{buildroot}%{_sbindir}/waagent
install -m0644 -D init/redhat/waagent.service %{buildroot}%{_unitdir}/
install -m0644 -D config/waagent.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -m0644 -D --target-directory=%{buildroot}%{_udevrulesdir}/ config/*.rules
install -m0755 -D --target-directory=%{buildroot}%{_prefix}/lib/dracut/modules.d/%{dracut_modname}/ %{SOURCE1}
sed -i 's,#!/usr/bin/env python,#!/usr/bin/python3,' %{buildroot}%{_sbindir}/waagent
sed -i 's,/usr/bin/python ,/usr/bin/python3 ,' %{buildroot}%{_unitdir}/waagent.service
sed -i 's,ResourceDisk.Format=y,ResourceDisk.Format=n,' %{buildroot}%{_sysconfdir}/waagent.conf
%oreon_autofiles WALinuxAgent-udev usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post waagent.service
%preun

%systemd_preun waagent.service
%postun

%systemd_postun_with_restart waagent.service
%files
%files -n WALinuxAgent-udev -f %{oreon_filedir}/WALinuxAgent-udev.list

%changelog

%autochangelog
