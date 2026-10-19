%global source0_hash 7063e6451056b6c51b1ab29e1a33321131286d11aeea3cb9f491458b3ca63dab
Name: drbd
Summary:        DRBD user-land tools and scripts
Version: 9.34.0
Release:        1%{?dist}
Source0:        https://pkg.linbit.com/downloads/%{name}/utils/%{name}-utils-%{version}.tar.gz
Patch0: drbd-utils-9.28.0-disable_xsltproc_network_read.patch
Patch1: drbd-utils-9.15.0-make_configure-workaround.patch
License: GPL-2.0-or-later
ExclusiveOS: linux
URL: http://www.drbd.org/
Requires: %{name}-utils = %{version}
Requires: %{name}-udev = %{version}
Recommends: (%{name}-pacemaker if pacemaker)
# oreon:deps
BuildRequires:  automake
BuildRequires:  checkpolicy
BuildRequires:  docbook-style-xsl
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  keyutils-libs-devel
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  pkgconf
BuildRequires:  pkgconfig(systemd)
BuildRequires:  po4a
BuildRequires:  rubygem-asciidoctor
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
BuildRequires:  udev
# /oreon:deps
%description
DRBD refers to block devices designed as a building block to form high
availability (HA) clusters. This is done by mirroring a whole block device
via an assigned network. DRBD can be understood as network based raid-1.

This is a virtual package, installing the full user-land suite.

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
rm -f $RPM_BUILD_ROOT/%{_initddir}/drbd
install -d -m755 $RPM_BUILD_ROOT/%{_unitdir}
rm -rf $RPM_BUILD_ROOT/etc/ha.d
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

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

%package udev
Summary: udev integration scripts for DRBD
Requires: %{name}-utils = %{version}-%{release}, udev
BuildArch: noarch
%description udev
This package contains udev helper scripts for DRBD, managing symlinks to
DRBD devices in /dev/drbd/by-res and /dev/drbd/by-disk.

%package pacemaker
Summary: Pacemaker resource agent for DRBD
Requires: %{name}-utils = %{version}-%{release}
Requires: pacemaker
License: GPL-2.0-only
BuildArch: noarch
%description pacemaker
This package contains the master/slave DRBD resource agent for the
Pacemaker High Availability cluster manager.

%package bash-completion
Summary: Programmable bash completion support for drbdadm
Requires: %{name}-utils = %{version}-%{release}
Requires: bash-completion
BuildArch: noarch
%description bash-completion
This package contains programmable bash completion support for the drbdadm
management utility.

%package selinux
Summary: SElinux policy for DRBD
BuildArch: noarch
BuildRequires: checkpolicy
BuildRequires: selinux-policy-devel
Requires: selinux-policy >= %{_selinux_policy_version}
%{?selinux_requires}
%description selinux
drbd-selinux contains the SELinux policy meant to be used with this version of DRBD and related tools.

%pre selinux

%selinux_relabel_pre -s %{selinuxtype}
%post selinux

%selinux_modules_install -s %{selinuxtype} -p 200 %{_datadir}/selinux/packages/%{selinuxmodulename}.pp.bz2
%postun selinux

if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} -p 200 %{selinuxmodulename}
fi
%posttrans selinux

%selinux_relabel_post -s %{selinuxtype}
%post utils

%systemd_post drbd.service
%preun utils

%systemd_preun drbd.service
%files -f %{oreon_filedir}/main.list
%files -n drbd-utils -f %{oreon_filedir}/drbd-utils.list
%files -n drbd-udev -f %{oreon_filedir}/drbd-udev.list
%files -n drbd-pacemaker -f %{oreon_filedir}/drbd-pacemaker.list
%files -n drbd-bash-completion -f %{oreon_filedir}/drbd-bash-completion.list
%files -n drbd-selinux -f %{oreon_filedir}/drbd-selinux.list

%changelog

%autochangelog
