%global source0_hash 4a20634e3052f716c2dcf9ec92173c4790bd38d8ca29b9841e2436208caf793d
%global longcommit cf5c2208bad2db2dff9b09624b89b05415c3bc11
%global shortcommit %(echo %{longcommit}|cut -c1-8)
%global modified %(echo %{longcommit}-|cut -f2 -d-)
%global github_owner Clusterlabs
%global baserelease 5
%ifarch s390x s390
%global watchdog_timeout_default 15
%else
%global watchdog_timeout_default 5
%endif
%bcond_without sync_resource_startup_default
%global sync_resource_startup_sysconfig ""
Name:           sbd
Summary:        Storage-based death
License:        GPL-2.0-or-later
Version:        1.5.2
Release:        1%{?dist}
Url:            https://github.com/%{github_owner}/%{name}
Source0:        https://github.com/%{github_owner}/%{name}/archive/refs/tags/%{longcommit}.tar.gz#/%{name}-%{longcommit}.tar.gz
Patch0:         0001-Fix-query-watchdog-avoid-issues-on-heap-allocation-f.patch
Patch1:         0002-Refactor-sbd-md-alloc-de-alloc-reverse-order.patch
Patch2:         0003-spec-convert-license-naming-to-SPDX.patch
Patch3:         0004-Fix-sbd-cluster-cleanly-include-crm-crm.h-for-crm_sy.patch
Patch4:         0005-avoid-parsing-SBD_DELAY_START-as-integer.patch
Patch5:         0006-Fix-sbd-pacemaker-remove-unused-update-counter.patch
Conflicts:      fence-agents-sbd < 4.5.0
Conflicts:      pacemaker-libs < 2.1.0-6
%if %{defined systemd_requires}
%systemd_requires
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  corosync-devel
BuildRequires:  glib2-devel
BuildRequires:  libaio-devel
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  pacemaker-libs-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd
# /oreon:deps
%description

This package contains the storage-based death functionality.

Available rpmbuild rebuild options:
  --with(out) : sync_resource_startup_default

%package tests
Summary:        Storage-based death environment for regression tests
License:        GPL-2.0-or-later
%description tests
This package provides an environment + testscripts for
regression-testing sbd.

###########################################################

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{longcommit} -p1

###########################################################

%build

./autogen.sh
export CFLAGS="$RPM_OPT_FLAGS -Wall -Werror"
%configure --with-watchdog-timeout-default=%{watchdog_timeout_default} \
           --with-sync-resource-startup-default=%{?with_sync_resource_startup_default:yes}%{!?with_sync_resource_startup_default:no} \
           --with-sync-resource-startup-sysconfig=%{sync_resource_startup_sysconfig} \
           --with-runstatedir=%{_rundir}
make %{?_smp_mflags}
%install
make DESTDIR=$RPM_BUILD_ROOT LIBDIR=%{_libdir} install
rm -rf ${RPM_BUILD_ROOT}%{_libdir}/stonith
install -D -m 0755 tests/regressions.sh $RPM_BUILD_ROOT/usr/share/sbd/regressions.sh
%if %{defined _unitdir}
install -D -m 0644 src/sbd.service $RPM_BUILD_ROOT/%{_unitdir}/sbd.service
install -D -m 0644 src/sbd_remote.service $RPM_BUILD_ROOT/%{_unitdir}/sbd_remote.service
%endif
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig
install -m 644 src/sbd.sysconfig ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/sbd
find %{buildroot} -name '*.a' -type f -print0 | xargs -0 rm -f
find %{buildroot} -name '*.la' -type f -print0 | xargs -0 rm -f
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{defined _unitdir}
%post

%systemd_post sbd.service
%systemd_post sbd_remote.service
if [ $1 -ne 1 ] ; then
	if systemctl --quiet is-enabled sbd.service 2>/dev/null
	then
		systemctl --quiet reenable sbd.service 2>/dev/null || :
	fi
	if systemctl --quiet is-enabled sbd_remote.service 2>/dev/null
	then
		systemctl --quiet reenable sbd_remote.service 2>/dev/null || :
	fi
fi
%preun

%systemd_preun sbd.service
%systemd_preun sbd_remote.service
%postun

%systemd_postun sbd.service
%systemd_postun sbd_remote.service
%endif
%files -f %{oreon_filedir}/main.list
%files -n sbd-tests -f %{oreon_filedir}/sbd-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.2-1
- Prepare for Oreon 11 (RP1)
