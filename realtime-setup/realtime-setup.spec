Name: realtime-setup
Version: 2.5
Release: 8%{?dist}
License: GPL-2.0-or-later
Summary: Setup RT/low-latency environment details
Source0: https://gitlab.com/rt-linux-tools/%{name}/-/archive/v%{version}/%{name}-%{version}.tar.bz2
URL:  https://gitlab.com/rt-linux-tools/realtime-setup.git

BuildRequires: gcc
BuildRequires: make
BuildRequires: systemd
BuildRequires: systemd-rpm-macros
BuildRequires: annobin-plugin-gcc
Requires: pam
Requires: tuna
Requires: tuned
Requires: tuned-profiles-realtime
Requires: systemd

# disable generation of debuginfo packages for this package
# the only executable from this package is realtime-entsk and it's not really
# something that requires debugging.
%global debug_package %{nil}

%description
Configure details useful for low-latency environments.

Installation of this package results in:
  - creation of a realtime group
  - adds realtime limits configuration for PAM
  - adds udev specific rules for threaded irqs and /dev/rtc access
  - adds /usr/bin/slub_cpu_partial_off to turn off cpu_partials in SLUB
  - adds net-socket timestamp static key daemon (realtime-entsk)

The slub_cpu_partial_off script is used to turn off the SLUB slab allocator's
use of cpu-partials, which has been known to create latency-spikes.

The realtime-entsk program is a workaround for latency spikes caused when the
network stack enables hardware timestamping and activates a static key. The
realtime-entsk progam is activated by the systemd service included and merely
enables the timestamp static key and pauses, effectively activating the static
key and never exiting, so no deactivation/activation sequences will be seen.

Neither the slub script or realtime-entsk are active by default.


%prep
%setup -q -n %{name}-%{version}

# Create a sysusers.d config file
cat >realtime-setup.sysusers.conf <<EOF
g realtime 71
EOF


%build
%make_build CFLAGS="%{build_cflags} -D_GNU_SOURCE" all

%install
%make_install DEST=%{buildroot} install

install -m0644 -D realtime-setup.sysusers.conf %{buildroot}%{_sysusersdir}/realtime-setup.conf


%preun
%systemd_preun realtime-setup.service

%files
%config(noreplace) %{_sysconfdir}/security/limits.d/realtime.conf
%config(noreplace) %{_sysconfdir}/udev/rules.d/99-rhel-rt.rules
%config(noreplace) %{_sysconfdir}/sysconfig/realtime-setup
%{_bindir}/slub_cpu_partial_off
%{_bindir}/realtime-entsk
%{_bindir}/kernel-is-rt
%{_unitdir}/realtime-setup.service
%{_bindir}/realtime-setup
%{_unitdir}/realtime-entsk.service
%{_sysusersdir}/realtime-setup.conf

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.5-8
- Prepare for Oreon 11 (RP1)
