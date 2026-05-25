Name:           irqbalance
Version:        1.9.5
Release:        2%{?dist}
Epoch:          2
Summary:        IRQ balancing daemon
License:        GPL-2.0-only
URL:            https://github.com/Irqbalance/irqbalance
Source0:        %{url}/archive/v%{version}/irqbalance-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: glib2-devel
BuildRequires: libcap-ng-devel
BuildRequires: meson
BuildRequires: ncurses-devel
BuildRequires: systemd
BuildRequires: systemd-devel
BuildRequires: libnl3-devel
Requires: ncurses-libs

%ifnarch %{arm}
BuildRequires:  numactl-devel
Requires: numactl-libs
%endif

ExcludeArch: s390 s390x %{ix86}

%description
irqbalance is a daemon that evenly distributes IRQ load across multiple CPUs
for enhanced performance.

%prep
%autosetup -p1

%build
# Move default config file from /usr/etc/default to /usr/lib/irqbalance to not
# conflict with ostree/rpm-ostree/bootc's usage of /usr/etc.
# Use /etc/sysconfig/irqbalance as admin config file to keep compatibility with
# existing installations on update.
%meson \
    -Dpkgconfdir=%{_prefix}/lib/irqbalance \
    -Dusrconfdir=%{_sysconfdir}/sysconfig
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc COPYING AUTHORS
%{_bindir}/irqbalance
%{_bindir}/irqbalance-ui
%{_unitdir}/irqbalance.service
%{_mandir}/man1/*
%{_prefix}/lib/irqbalance/irqbalance.env
%ghost %config(noreplace) %{_sysconfdir}/sysconfig/irqbalance

%post
%systemd_post irqbalance.service

%preun
%systemd_preun irqbalance.service

%postun
%systemd_postun_with_restart irqbalance.service

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2:1.9.5-2
- Import
