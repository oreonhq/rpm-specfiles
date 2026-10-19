%global source0_hash c5fc3b1880136437d297afe9a7833781e7849939e104d0780888ffcafc37e339
Name:           irqbalance
Version:        1.9.5
Release:        1%{?dist}
Epoch:          2
Summary:        IRQ balancing daemon
License:        GPL-2.0-only
URL:            https://github.com/Irqbalance/irqbalance
Source0:        https://github.com/Irqbalance/irqbalance/archive/refs/tags/v1.9.5.tar.gz#/irqbalance-1.9.5.tar.gz
Requires: ncurses-libs
%ifnarch %{arm}
Requires: numactl-libs
%endif
ExcludeArch: s390 s390x %{ix86}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  libcap-ng-devel
BuildRequires:  libnl3-devel
BuildRequires:  meson
BuildRequires:  ncurses-devel
BuildRequires:  numactl-devel
BuildRequires:  systemd
BuildRequires:  systemd-devel
# /oreon:deps
%description
irqbalance is a daemon that evenly distributes IRQ load across multiple CPUs
for enhanced performance.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir irqbalance-1.9.5
%oreon_prep
%build

%meson \
    -Dpkgconfdir=%{_prefix}/lib/irqbalance \
    -Dusrconfdir=%{_sysconfdir}/sysconfig
%meson_build
%install
%meson_install
%oreon_autofiles main

%check

%meson_test
%post

%systemd_post irqbalance.service
%preun

%systemd_preun irqbalance.service
%postun

%systemd_postun_with_restart irqbalance.service
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2:1.9.5-2
- Import
