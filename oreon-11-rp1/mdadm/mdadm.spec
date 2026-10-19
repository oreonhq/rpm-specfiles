%global source0_hash e89f24994f403cea90068d03f3c1ee49957303c7a092cc5b2ed2c603df9649a7
%bcond abrt %{undefined rhel}
Name:        mdadm
Version:     4.6
Release:        1%{?dist}
Summary:        The mdadm program controls Linux md devices (software RAID arrays)
URL:         http://www.kernel.org/pub/linux/utils/raid/mdadm/
License:     GPL-2.0-or-later
Source0:        https://git.kernel.org/pub/scm/utils/mdadm/mdadm.git/snapshot/%{name}-%{version}.tar.gz
Source1:     raid-check
Source2:     mdadm-raid-check-sysconfig
Source3:     mdmonitor.service
Source4:     mdadm.conf
Source5:     mdadm_event.conf
Source6:     raid-check.timer
Source7:     raid-check.service
Source8:     mdcheck
Patch:       mdadm-udev.patch
Patch:       mdadm-2.5.2-static.patch
%if %{with abrt}
Requires:         libreport-filesystem
%endif
Requires(post):   coreutils
Requires(postun): coreutils
# oreon:deps
BuildRequires:  binutils-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  mandoc
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
The mdadm program is used to create, manage, and monitor Linux MD (software
RAID) devices.  As such, it provides similar functionality to the raidtools
package.  However, mdadm is a single program, and it can perform
almost all functions without a configuration file, though a configuration
file can be used to help with some common tasks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build CXFLAGS="%{optflags} -std=gnu17 -Wno-error=unterminated-string-initialization -Wno-error=unused-but-set-variable -Wno-error=format-truncation" LDFLAGS="$RPM_LD_FLAGS" SYSCONFDIR="%{_sysconfdir}" mdadm mdmon raid6check raid6check.man
%install
%make_install MANDIR=%{_mandir} BINDIR=%{_sbindir} SYSTEMD_DIR=%{_unitdir} UDEVDIR=%{_prefix}/lib/udev/ install install-systemd
install -Dp -m 755 %{SOURCE1} %{buildroot}%{_sbindir}/raid-check
install -Dp -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/raid-check
mkdir -p -m 710 %{buildroot}/run/%{name}
mkdir -p -m 755 %{buildroot}%{_datadir}/%{name}
install -Dp -m 755 %{SOURCE8} %{buildroot}%{_datadir}/%{name}/mdcheck
install -Dm644 %{SOURCE3} %{buildroot}%{_unitdir}
install -Dm644 %{SOURCE6} %{buildroot}%{_unitdir}
install -Dm644 %{SOURCE7} %{buildroot}%{_unitdir}
install -Dm 0644 %{SOURCE4} %{buildroot}%{_tmpfilesdir}/%{name}.conf
mkdir -p %{buildroot}%{_localstatedir}/run/
install -d -m 0710 %{buildroot}/run/%{name}/
%if %{with abrt}
install -Dm644 %{SOURCE5} %{buildroot}%{_sysconfdir}/libreport/events.d/%{name}_event.conf
%endif
install -Dm755 raid6check %{buildroot}/%{_sbindir}/raid6check
install -Dm644 raid6check.man %{buildroot}/%{_mandir}/man8/raid6check.man
%oreon_autofiles main

%post

%systemd_post mdmonitor.service raid-check.timer
%{_bindir}/systemctl disable mdmonitor-takeover.service  >/dev/null 2>&1 || :
%preun

%systemd_preun mdmonitor.service raid-check.timer
%postun

%systemd_postun_with_restart mdmonitor.service
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.3-10
- Prepare for Oreon 11 (RP1)
