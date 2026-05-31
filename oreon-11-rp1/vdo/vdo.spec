%global source0_hash d778eb3bd69ff613f88117e17afc57602bde3381401b0f3be8dcf3efe6f2e1fe

Summary: Management tools for Virtual Data Optimizer
Name: vdo
Version: 8.3.2.1
Release: 2%{?dist}

License: GPL-2.0-only
URL: https://github.com/dm-vdo/vdo
Source0:        https://github.com/dm-vdo/vdo/archive/8.3.2.1/vdo-8.3.2.1.tar.gz

%if 0%{?fedora}
ExcludeArch: %{ix86}
%endif
BuildRequires: device-mapper-devel
BuildRequires: device-mapper-event-devel
BuildRequires: gcc
BuildRequires: libblkid-devel
BuildRequires: libuuid-devel
BuildRequires: make
%ifarch %{valgrind_arches}
BuildRequires: valgrind-devel
%endif
BuildRequires: zlib-devel

# Disable an automatic dependency due to a file in examples/monitor.
%global __requires_exclude perl
%if 0%{?rhel}
%global bash_completions_dir %{_datadir}/bash-completion/completions
%endif

%description
Virtual Data Optimizer (VDO) is a device mapper target that delivers
block-level deduplication, compression, and thin provisioning.

This package provides the user-space management tools for VDO.

%package support
Summary: Support tools for Virtual Data Optimizer
License: GPL-2.0-only

Requires: libuuid >= 2.23

%description support
Virtual Data Optimizer (VDO) is a device mapper target that delivers
block-level deduplication, compression, and thin provisioning.

This package provides the user-space support tools for VDO.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
%make_build VDO_VERSION=%{version}

%install
%make_install INSTALLOWNER= name=%{name} bindir=%{_bindir} \
   mandir=%{_mandir} defaultdocdir=%{_defaultdocdir} libexecdir=%{_libexecdir} \
   presetdir=%{_presetdir} python3_sitelib=/%{python3_sitelib} \
   sysconfdir=%{_sysconfdir} unitdir=%{_unitdir}

%files
%license COPYING
%{_bindir}/vdocalculatesize
%{_bindir}/vdoforcerebuild
%{_bindir}/vdoformat
%{_bindir}/vdostats
%{bash_completions_dir}/vdostats
%dir %{_defaultdocdir}/%{name}
%dir %{_defaultdocdir}/%{name}/examples
%dir %{_defaultdocdir}/%{name}/examples/monitor
%doc %{_defaultdocdir}/%{name}/examples/monitor/monitor_check_vdostats_logicalSpace.pl
%doc %{_defaultdocdir}/%{name}/examples/monitor/monitor_check_vdostats_physicalSpace.pl
%doc %{_defaultdocdir}/%{name}/examples/monitor/monitor_check_vdostats_savingPercent.pl
%{_mandir}/man8/vdocalculatesize.8*
%{_mandir}/man8/vdoforcerebuild.8*
%{_mandir}/man8/vdoformat.8*
%{_mandir}/man8/vdostats.8*

%files support
%license COPYING
%{_bindir}/adaptlvm
%{_bindir}/vdoaudit
%{_bindir}/vdodebugmetadata
%{_bindir}/vdodumpblockmap
%{_bindir}/vdodumpmetadata
%{_bindir}/vdolistmetadata
%{_bindir}/vdoreadonly
%{_bindir}/vdorecover
%{_mandir}/man8/adaptlvm.8*
%{_mandir}/man8/vdoaudit.8*
%{_mandir}/man8/vdodebugmetadata.8*
%{_mandir}/man8/vdodumpblockmap.8*
%{_mandir}/man8/vdodumpmetadata.8*
%{_mandir}/man8/vdolistmetadata.8*
%{_mandir}/man8/vdoreadonly.8*
%{_mandir}/man8/vdorecover.8*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 8.3.2.1-2
- Prepare for Oreon 11 (RP1)
