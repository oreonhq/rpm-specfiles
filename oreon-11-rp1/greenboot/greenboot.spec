%global source0_hash 035b509604e138ab18b16962cc375d7bc827786343927403a0ca56834a115a3c
%global debug_package %{nil}
Name:               greenboot
Version:            0.15.9
Release:        1%{?dist}
Summary:        Generic Health Check Framework for systemd
License:            LGPL-2.1-or-later
%global repo_owner  fedora-iot
%global repo_name   %{name}
%global repo_tag    v%{version}
URL:                https://github.com/%{repo_owner}/%{repo_name}
Source0:        https://github.com/%{repo_owner}/%{name}/archive/refs/tags/%{repo_tag}.tar.gz#/%{name}-%{version}.tar.gz
ExcludeArch: s390x {%ix86}
%{?systemd_requires}
Requires:           systemd >= 240
Requires:           grub2-tools-minimal
Requires:           rpm-ostree
Requires:           pam >= 1.4.0
Recommends:         openssh
Provides:           greenboot-auto-update-fallback
Obsoletes:          greenboot-auto-update-fallback <= 0.12.0
Provides:           greenboot-grub2
Obsoletes:          greenboot-grub2 <= 0.12.0
Provides:           greenboot-reboot
Obsoletes:          greenboot-reboot <= 0.12.0
Provides:           greenboot-status
Obsoletes:          greenboot-status <= 0.12.0
Provides:           greenboot-rpm-ostree-grub2
Obsoletes:          greenboot-rpm-ostree-grub2 <= 0.12.0
# oreon:deps
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
%{summary}.

%package default-health-checks
Summary:            Series of optional and curated health checks
Requires:           %{name} = %{version}-%{release}
Requires:           util-linux
Requires:           jq
Provides:           greenboot-update-platforms-check
Obsoletes:          greenboot-update-platforms-check <= 0.12.0
%description default-health-checks
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

%install
mkdir -p %{buildroot}%{_exec_prefix}/lib/motd.d/
mkdir -p %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/check/required.d
mkdir    %{buildroot}%{_sysconfdir}/%{name}/check/wanted.d
mkdir    %{buildroot}%{_sysconfdir}/%{name}/green.d
mkdir    %{buildroot}%{_sysconfdir}/%{name}/red.d
mkdir -p %{buildroot}%{_prefix}/lib/%{name}/check/required.d
mkdir    %{buildroot}%{_prefix}/lib/%{name}/check/wanted.d
mkdir    %{buildroot}%{_prefix}/lib/%{name}/green.d
mkdir    %{buildroot}%{_prefix}/lib/%{name}/red.d
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_unitdir}/greenboot-healthcheck.service.d
mkdir -p %{buildroot}%{_tmpfilesdir}
install -DpZm 0755 usr/libexec/greenboot/* %{buildroot}%{_libexecdir}/%{name}
install -DpZm 0644 usr/lib/motd.d/boot-status %{buildroot}%{_exec_prefix}/lib/motd.d/boot-status
install -DpZm 0644 usr/lib/systemd/system/greenboot-healthcheck.service.d/10-network-online.conf %{buildroot}%{_unitdir}/greenboot-healthcheck.service.d/10-network-online.conf
install -DpZm 0644 usr/lib/systemd/system/*.target %{buildroot}%{_unitdir}
install -DpZm 0644 usr/lib/systemd/system/*.service %{buildroot}%{_unitdir}
install -DpZm 0644 usr/lib/tmpfiles.d/greenboot-status-motd.conf %{buildroot}%{_tmpfilesdir}/greenboot-status-motd.conf
install -DpZm 0755 usr/lib/greenboot/check/required.d/* %{buildroot}%{_prefix}/lib/%{name}/check/required.d
install -DpZm 0755 usr/lib/greenboot/check/wanted.d/* %{buildroot}%{_prefix}/lib/%{name}/check/wanted.d
install -DpZm 0644 etc/greenboot/greenboot.conf %{buildroot}%{_sysconfdir}/%{name}/greenboot.conf
install -DpZm 0644 grub2/08_greenboot.cfg %{buildroot}%{_sysconfdir}/grub.d/greenboot.cfg
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post greenboot-healthcheck.service
%systemd_post greenboot-loading-message.service
%systemd_post greenboot-task-runner.service
%systemd_post redboot-task-runner.service
%systemd_post redboot.target
%systemd_post greenboot-status.service
%systemd_post greenboot-grub2-set-counter.service
%systemd_post greenboot-grub2-set-success.service
%systemd_post greenboot-rpm-ostree-grub2-check-fallback.service
%systemd_post redboot-auto-reboot.service
if [ -d /usr/lib/bootupd/grub2-static/configs.d ]; then
cp /etc/grub.d/greenboot.cfg /usr/lib/bootupd/grub2-static/configs.d
fi
%post default-health-checks

%systemd_post greenboot-loading-message.service
%preun

%systemd_preun greenboot-healthcheck.service
%systemd_preun greenboot-loading-message.service
%systemd_preun greenboot-task-runner.service
%systemd_preun redboot-task-runner.service
%systemd_preun redboot.target
%systemd_preun greenboot-status.service
%systemd_preun greenboot-grub2-set-counter.service
%systemd_preun greenboot-grub2-set-success.service
%systemd_preun greenboot-rpm-ostree-grub2-check-fallback.service
%preun default-health-checks

%systemd_preun greenboot-loading-message.service
%postun

%systemd_postun greenboot-healthcheck.service
%systemd_postun greenboot-loading-message.service
%systemd_postun greenboot-task-runner.service
%systemd_postun redboot-task-runner.service
%systemd_postun redboot.target
%systemd_postun greenboot-status.service
%systemd_postun greenboot-grub2-set-counter.service
%systemd_postun greenboot-grub2-set-success.service
%systemd_postun greenboot-rpm-ostree-grub2-check-fallback.service
if [ -f /usr/lib/bootupd/grub2-static/configs.d/greenboot.cfg ]; then
rm -f /usr/lib/bootupd/grub2-static/configs.d/greenboot.cfg
fi
%postun default-health-checks

%systemd_postun greenboot-loading-message.service
%files -f %{oreon_filedir}/main.list
%files -n greenboot-default-health-checks -f %{oreon_filedir}/greenboot-default-health-checks.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.15.8-3
- Prepare for Oreon 11 (RP1)
