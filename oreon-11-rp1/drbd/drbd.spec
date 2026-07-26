%global source0_hash 7063e6451056b6c51b1ab29e1a33321131286d11aeea3cb9f491458b3ca63dab

Name: drbd
Summary: DRBD user-land tools and scripts
Version: 9.34.0
Release: 1%{?dist}
Source0: https://pkg.linbit.com/downloads/%{name}/utils/%{name}-utils-%{version}.tar.gz
Patch0: drbd-utils-9.28.0-disable_xsltproc_network_read.patch
Patch1: drbd-utils-9.15.0-make_configure-workaround.patch
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
ExclusiveOS: linux
URL: http://www.drbd.org/
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: flex
BuildRequires: libxslt
BuildRequires: docbook-style-xsl
BuildRequires: perl-generators
BuildRequires: pkgconf
BuildRequires: po4a
BuildRequires: rubygem-asciidoctor
BuildRequires: keyutils-libs-devel
BuildRequires: udev
BuildRequires: make
BuildRequires: automake
Requires: %{name}-utils = %{version}
Requires: %{name}-udev = %{version}
Recommends: (%{name}-pacemaker if pacemaker)

%description
DRBD refers to block devices designed as a building block to form high
availability (HA) clusters. This is done by mirroring a whole block device
via an assigned network. DRBD can be understood as network based raid-1.

This is a virtual package, installing the full user-land suite.

%files
%doc COPYING
%doc ChangeLog

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n drbd-utils-%{version}

# Don't let xsltproc make network calls during build
%patch -P 0 -p1
%patch -P 1 -p1

%build
%configure \
    --with-udev \
    --with-pacemaker \
    --with-systemdunitdir=%{_unitdir} \
    --with-selinux \
    --without-sbinsymlinks
%{make_build}
%{__make} selinux

%install
rm -rf $RPM_BUILD_ROOT
%{make_install}
%{__install} -d %{buildroot}%{_datadir}/selinux/packages
%{__install} -m 0644 selinux/drbd.pp.bz2 %{buildroot}%{_datadir}/selinux/packages

# Remove old init script, replace with systemd unit file
rm -f $RPM_BUILD_ROOT/%{_initddir}/drbd
install -d -m755 $RPM_BUILD_ROOT/%{_unitdir}

# Remove old heartbeat files that aren't needed any longer in Fedora
rm -rf $RPM_BUILD_ROOT/etc/ha.d

%package utils
Summary: Management utilities for DRBD
Requires: (drbd-selinux if selinux-policy-targeted)
Obsoletes: drbd-xen <= 9.30.0
Obsoletes: drbd-rgmanager <= 9.31.0
Obsoletes: drbd-heartbeat <= 9.31.0

%description utils
DRBD mirrors a block device over the network to another machine.
Think of it as networked raid 1. It is a building block for
setting up high availability (HA) clusters.

This packages includes the DRBD administration tools.

%files utils
%defattr(755,root,root,755)
%{_sbindir}/drbdsetup
%{_sbindir}/drbdadm
%{_sbindir}/drbdmeta
%{_sbindir}/drbdmon

# systemd-related stuff
%attr(0644,root,root) %{_presetdir}/50-drbd.preset
%attr(0644,root,root) %{_unitdir}/drbd.service
%attr(0644,root,root) %{_unitdir}/drbd-graceful-shutdown.service
%attr(0644,root,root) %{_unitdir}/drbd-lvchange@.service
%attr(0644,root,root) %{_unitdir}/drbd-promote@.service
%attr(0644,root,root) %{_unitdir}/drbd-demote-or-escalate@.service
%attr(0644,root,root) %{_unitdir}/drbd-reconfigure-suspend-or-error@.service
%attr(0644,root,root) %{_unitdir}/drbd-services@.target
%attr(0644,root,root) %{_unitdir}/drbd-wait-promotable@.service
%attr(0644,root,root) %{_unitdir}/drbd@.service
%attr(0644,root,root) %{_unitdir}/drbd@.target
%attr(0644,root,root) %{_unitdir}/drbd-configured.target
%attr(0644,root,root) %{_tmpfilesdir}/%{name}.conf

# Yes, these paths are peculiar. Upstream is peculiar.
# Be forewarned: rpmlint hates this stuff.
%defattr(755,root,root,-)
%{_prefix}/lib/drbd/scripts/drbd
%{_prefix}/lib/drbd/scripts/drbd-service-shim.sh
%{_prefix}/lib/drbd/scripts/drbd-wait-promotable.sh
%{_prefix}/lib/drbd/drbdadm-*
%{_prefix}/lib/drbd/drbdsetup-*
%{_prefix}/lib/drbd/*.sh
%{_prefix}/lib/drbd/tnf-drbd-fence.py
%{_sbindir}/drbd-events-log-supplier

%defattr(-,root,root,-)
%dir %{_var}/lib/%{name}
%config(noreplace) %{_sysconfdir}/drbd.conf
%dir %{_sysconfdir}/drbd.d
%config(noreplace) %{_sysconfdir}/drbd.d/global_common.conf
%config(noreplace) %{_sysconfdir}/multipath/conf.d/drbd.conf
%{_mandir}/man8/drbd*gz
%{_mandir}/man5/drbd*gz
%{_mandir}/ja/man5/drbd*gz
%{_mandir}/ja/man8/drbd*gz
%{_mandir}/man7/drbd*@.service.*
%{_mandir}/man7/drbd*@.target.*
%{_mandir}/man7/drbd.service.*
%{_mandir}/man7/drbd-graceful-shutdown.service.*
%{_mandir}/man7/drbd-configured.target.*
%doc scripts/drbd.conf.example
%license COPYING
%doc ChangeLog

%package udev
Summary: udev integration scripts for DRBD
Requires: %{name}-utils = %{version}-%{release}, udev
BuildArch: noarch

%description udev
This package contains udev helper scripts for DRBD, managing symlinks to
DRBD devices in /dev/drbd/by-res and /dev/drbd/by-disk.

%files udev
%{_udevrulesdir}/65-drbd.rules

%package pacemaker
Summary: Pacemaker resource agent for DRBD
Requires: %{name}-utils = %{version}-%{release}
# pacemaker is in the RHEL highavailability channel in EL8 and EL9.  EPEL
# packages dependencies must be in the "target base" (baseos, appstream, crb).
# Weak dependencies are allowed on packages from other channels, so use a
# recommends instead of a requires on EPEL8 and EPEL9.
# https://docs.fedoraproject.org/en-US/epel/epel-packaging/#package_dependencies
# https://bugzilla.redhat.com/show_bug.cgi?id=2086146
%if %{defined rhel} && 0%{?rhel} >= 8
Recommends: pacemaker
%else
Requires: pacemaker
%endif
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
BuildArch: noarch

%description pacemaker
This package contains the master/slave DRBD resource agent for the
Pacemaker High Availability cluster manager.

%files pacemaker
%defattr(755,root,root,-)
%dir %{_prefix}/lib/ocf/resource.d/linbit/
%{_prefix}/lib/ocf/resource.d/linbit/drbd
%{_prefix}/lib/ocf/resource.d/linbit/drbd-attr
%{_prefix}/lib/ocf/resource.d/linbit/drbd.shellfuncs.sh
%{_mandir}/man7/ocf_linbit_drbd*gz

%package bash-completion
Summary: Programmable bash completion support for drbdadm
Requires: %{name}-utils = %{version}-%{release}
Requires: bash-completion
BuildArch: noarch

%description bash-completion
This package contains programmable bash completion support for the drbdadm
management utility.

%files bash-completion
%config(noreplace) %{_datadir}/bash-completion/completions/drbdadm

%global selinuxtype             targeted
%global selinuxmodulename       drbd

%package selinux
Summary: SElinux policy for DRBD
BuildArch: noarch
BuildRequires: checkpolicy
BuildRequires: selinux-policy-devel
Requires: selinux-policy >= %{_selinux_policy_version}
# do we need to require drbd-pacemaker, to have it installed before our
# posttrans tries to relabel?
%{?selinux_requires}

%description selinux
drbd-selinux contains the SELinux policy meant to be used with this version of DRBD and related tools.

%files selinux
%attr(0644,root,root) %{_datadir}/selinux/packages/%{selinuxmodulename}.pp.bz2
%ghost %attr(0644,root,root) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{selinuxmodulename}

%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
# install selinux policy module with priority 200 to override the default policy
# maybe we want/need the next line to &> /dev/null
%selinux_modules_install -s %{selinuxtype} -p 200 %{_datadir}/selinux/packages/%{selinuxmodulename}.pp.bz2

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} -p 200 %{selinuxmodulename}
fi

# We we want a "rich forward dependency" of drbd-utils to drbd-selinux,
# we above use
#  Requires: (drbd-selinux if selinux-policy-targeted)
# We need to relabel in posttrans, because in post the files to
# relabel may not be installed yet.
%posttrans selinux
# maybe &> /dev/null
%selinux_relabel_post -s %{selinuxtype}

%post utils
%systemd_post drbd.service

%preun utils
%systemd_preun drbd.service

%changelog
%autochangelog
