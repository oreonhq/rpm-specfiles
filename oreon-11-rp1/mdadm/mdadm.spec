%global source0_hash 416727ae1f1080ea6e3090cea36dd076826fc369151e36ab736557ba92196f9f

%bcond abrt %{undefined rhel}

Name:        mdadm
Version:     4.3
Release:     10%{?dist}
Summary:     The mdadm program controls Linux md devices (software RAID arrays)
URL:         http://www.kernel.org/pub/linux/utils/raid/mdadm/
License:     GPL-2.0-or-later

Source:        https://www.kernel.org/pub/linux/utils/raid/mdadm/mdadm-4.3.tar.xz
Source1:     raid-check
Source2:     mdadm-raid-check-sysconfig
Source3:     mdmonitor.service
Source4:     mdadm.conf
Source5:     mdadm_event.conf
Source6:     raid-check.timer
Source7:     raid-check.service
Source8:     mdcheck
Source10:        https://www.kernel.org/pub/linux/utils/raid/mdadm/mdadm-4.3.tar.sign
Source11:    https://git.kernel.org/pub/scm/docs/kernel/pgpkeys.git/plain/keys/6F9E3E9D4EDEBB11.asc

# https://bugzilla.redhat.com/show_bug.cgi?id=2325906
# see: https://github.com/md-raid-utilities/mdadm/pull/165
# https://github.com/md-raid-utilities/mdadm/pull/160
# https://github.com/md-raid-utilities/mdadm/pull/159
# this is a reversion of the initial 'posix check' patch
# that causes all the trouble
Patch:       0001-Revert-mdadm-Follow-POSIX-Portable-Character-Set.patch
Patch:       0002-dont-stop-in-assemble.patch

# Fedora customization patches
Patch:       mdadm-udev.patch
Patch:       mdadm-2.5.2-static.patch

BuildRequires:    make
BuildRequires:    systemd-rpm-macros
BuildRequires:    binutils-devel
BuildRequires:    gcc
BuildRequires:    systemd-devel
BuildRequires:    gnupg2
BuildRequires:    mandoc
%if %{with abrt}
Requires:         libreport-filesystem
%endif
Requires(post):   coreutils
Requires(postun): coreutils


%description
The mdadm program is used to create, manage, and monitor Linux MD (software
RAID) devices.  As such, it provides similar functionality to the raidtools
package.  However, mdadm is a single program, and it can perform
almost all functions without a configuration file, though a configuration
file can be used to help with some common tasks.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
# because the tarball is what is signed, not the compressed tarball
# keyring should be one from https://git.kernel.org/pub/scm/docs/kernel/pgpkeys.git/plain/keys
# which will vary depending on who did the release
%{_bindir}/xz -dcT0 %{SOURCE0} | %{gpgverify} --keyring='%{SOURCE11}' --signature='%{SOURCE10}' --data=-
%autosetup -p1


%build
# CXFLAGS is NOT a typo, it's baked into the makefile, not to be confused with CXXFLAGS
%make_build CXFLAGS="%{optflags} -std=gnu17 -Wno-error=unterminated-string-initialization -Wno-error=unused-but-set-variable" LDFLAGS="$RPM_LD_FLAGS" SYSCONFDIR="%{_sysconfdir}" mdadm mdmon raid6check raid6check.man


%install
%make_install MANDIR=%{_mandir} BINDIR=%{_sbindir} SYSTEMD_DIR=%{_unitdir} UDEVDIR=%{_prefix}/lib/udev/ install install-systemd
install -Dp -m 755 %{SOURCE1} %{buildroot}%{_sbindir}/raid-check
install -Dp -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/raid-check
mkdir -p -m 710 %{buildroot}/run/%{name}
mkdir -p -m 755 %{buildroot}%{_datadir}/%{name}
install -Dp -m 755 %{SOURCE8} %{buildroot}%{_datadir}/%{name}/mdcheck

# systemd
install -Dm644 %{SOURCE3} %{buildroot}%{_unitdir}
install -Dm644 %{SOURCE6} %{buildroot}%{_unitdir}
install -Dm644 %{SOURCE7} %{buildroot}%{_unitdir}

# tmpfile
install -Dm 0644 %{SOURCE4} %{buildroot}%{_tmpfilesdir}/%{name}.conf
mkdir -p %{buildroot}%{_localstatedir}/run/
install -d -m 0710 %{buildroot}/run/%{name}/

# abrt
%if %{with abrt}
install -Dm644 %{SOURCE5} %{buildroot}%{_sysconfdir}/libreport/events.d/%{name}_event.conf
%endif

# raid6check
install -Dm755 raid6check %{buildroot}/%{_sbindir}/raid6check
install -Dm644 raid6check.man %{buildroot}/%{_mandir}/man8/raid6check.man

%post
%systemd_post mdmonitor.service raid-check.timer
# leftover from this service removal years ago (f18 era).
# we probably don't really need this anymore.
# https://bugzilla.redhat.com/show_bug.cgi?id=901651
%{_bindir}/systemctl disable mdmonitor-takeover.service  >/dev/null 2>&1 || :


%preun
%systemd_preun mdmonitor.service raid-check.timer


%postun
%systemd_postun_with_restart mdmonitor.service


%files
%license COPYING
%doc mdadm.conf-example misc/*
%{_udevrulesdir}/*-md-*
%{_sbindir}/%{name}
%{_sbindir}/mdmon
%{_sbindir}/raid-check
%{_sbindir}/raid6check
%{_unitdir}/md*
%{_unitdir}/raid-check.*
%{_mandir}/man*/md*
%{_mandir}/man8/raid6check*
%{_prefix}/lib/systemd/system-shutdown/mdadm.shutdown
%config(noreplace) %{_sysconfdir}/sysconfig/raid-check
%{_rundir}/%{name}/
%config(noreplace) %{_tmpfilesdir}/%{name}.conf
%if %{with abrt}
%{_sysconfdir}/libreport/events.d/mdadm_event.conf
%endif
%{_datadir}/%{name}/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.3-10
- Prepare for Oreon 11 (RP1)
