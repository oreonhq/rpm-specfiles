%global source0_hash f41f5c8a697420c282c603d96f70b25a6f4d3bf330fa0249625bce256e0cce2e
Name: btrfsmaintenance
Version: 0.5.2
Release:        1%{?dist}
Summary:        Scripts for btrfs maintenance tasks
BuildArch: noarch
License: GPL-2.0-or-later
URL: https://github.com/kdave/btrfsmaintenance
Source0:        https://github.com/kdave/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires: btrfs-progs
Enhances: btrfs-progs
# oreon:deps
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Scripts for btrfs maintenance tasks like periodic scrub, balance, trim or
defrag on selected mountpoints or directories. 

This is a set of scripts supplementing the btrfs filesystem and aims to
automate a few maintenance tasks. This means the scrub, balance, trim or
defragmentation.

Each of the tasks can be turned on/off and configured independently. The
default config values were selected to fit the default installation profile
with btrfs on the root filesystem.

Overall tuning of the default values should give a good balance between
effects of the tasks and low impact of other work on the system. If this does
not fit your needs, please adjust the settings.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%install
install -Dpm755 btrfs-defrag.sh -t %{buildroot}%{_datadir}/%{name}
install -Dpm755 btrfs-balance.sh -t %{buildroot}%{_datadir}/%{name}
install -Dpm755 btrfs-scrub.sh -t %{buildroot}%{_datadir}/%{name}
install -Dpm755 btrfs-trim.sh -t %{buildroot}%{_datadir}/%{name}
install -Dpm755 %{name}-refresh-cron.sh -t %{buildroot}%{_datadir}/%{name}
install -Dpm755 %{name}-functions -t %{buildroot}%{_datadir}/%{name}
install -Dpm644 %{name}-refresh.service -t %{buildroot}%{_unitdir}
install -Dpm644 %{name}-refresh.path -t %{buildroot}%{_unitdir}
install -Dpm644 btrfs-balance.service -t %{buildroot}%{_unitdir}
install -Dpm644 btrfs-defrag.service -t %{buildroot}%{_unitdir}
install -Dpm644 btrfs-scrub.service -t %{buildroot}%{_unitdir}
install -Dpm644 btrfs-trim.service -t %{buildroot}%{_unitdir}
install -Dpm644 btrfs-balance.timer -t %{buildroot}%{_unitdir}
install -Dpm644 btrfs-defrag.timer -t %{buildroot}%{_unitdir}
install -Dpm644 btrfs-scrub.timer -t %{buildroot}%{_unitdir}
install -Dpm644 btrfs-trim.timer -t %{buildroot}%{_unitdir}
install -Dpm644 sysconfig.%{name} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
%oreon_autofiles main

%post

%systemd_post %{name}-refresh.service %{name}-refresh.path btrfs-balance.service btrfs-balance.timer btrfs-defrag.service btrfs-defrag.timer btrfs-scrub.service btrfs-scrub.timer btrfs-trim.service btrfs-trim.timer
%preun

%systemd_preun %{name}-refresh.service %{name}-refresh.path btrfs-balance.service btrfs-balance.timer btrfs-defrag.service btrfs-defrag.timer btrfs-scrub.service btrfs-scrub.timer btrfs-trim.service btrfs-trim.timer
%postun

%systemd_postun_with_restart %{name}-refresh.service %{name}-refresh.path btrfs-balance.service btrfs-balance.timer btrfs-defrag.service btrfs-defrag.timer btrfs-scrub.service btrfs-scrub.timer btrfs-trim.service btrfs-trim.timer
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
