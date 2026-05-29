%global source0_hash none

#%%global git_commit e1045f2d1d6fbcdd29a62b3540b846fa6b2a9153
#%%global git_date %%(date +'%Y%m%d')
#%%global git_date 20220317

%if 0%{?rhel} && 0%{?rhel} < 10
%global user_profiles_dir %{_sysconfdir}/tuned
%global system_profiles_dir %{_prefix}/lib/tuned
%else
%global user_profiles_dir %{_sysconfdir}/tuned/profiles
%global system_profiles_dir %{_prefix}/lib/tuned/profiles
%endif

%if 0%{?fedora}
%if 0%{?fedora} > 27
%bcond_without python3
%else
%bcond_with python3
%endif
%else
%if 0%{?rhel} && 0%{?rhel} < 8
%bcond_with python3
%else
%bcond_without python3
%endif
%endif

%if %{with python3}
%global _py python3
%global make_python_arg PYTHON=%{__python3}
%else
%{!?python2_sitelib:%global python2_sitelib %{python_sitelib}}
%if 0%{?rhel} && 0%{?rhel} < 8
%global make_python_arg PYTHON=%{__python}
%global _py python
%else
%global make_python_arg PYTHON=%{__python2}
%global _py python2
%endif
%endif

%if 0%{?git_commit:1}
%if 0%{!?git_short_commit:1}
%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global archive_topdir %{name}-%{git_commit}
%endif
%global git_suffix %{git_date}git%{git_short_commit}
# ! git_commit
%else
%global archive_topdir %{name}-%{version}%{?prerel2}
%endif

#%%global prerelease rc
#%%global prereleasenum 1

%global prerel1 %{?prerelease:.%{prerelease}%{prereleasenum}}
%global prerel2 %{?prerelease:-%{prerelease}.%{prereleasenum}}

Summary: A dynamic adaptive system tuning daemon
Name: tuned
Version: 2.27.0
Release: 1%{?prerel1}%{?git_suffix:.%{git_suffix}}%{?dist}
License: GPL-2.0-or-later AND CC-BY-SA-3.0
%if 0%{?git_commit:1}
%else
Source0:        https://github.com/redhat-performance/tuned/archive/v2.27.0%{?prerel2}/tuned-2.27.0%{?prerel2}.tar.gz
%endif
URL: http://www.tuned-project.org/
BuildArch: noarch
BuildRequires: systemd
BuildRequires: desktop-file-utils
%if 0%{?rhel}
BuildRequires: asciidoc
%else
BuildRequires: asciidoctor
%endif
Requires(post): systemd, virt-what
Requires(preun): systemd
Requires(postun): systemd
BuildRequires: make
BuildRequires: %{_py}
BuildRequires: %{_py}-devel
# BuildRequires for 'make test'
# python-mock is needed for python-2.7, but it's not available on RHEL-7, only in the EPEL
%if %{without python3} && ( ! 0%{?rhel} || 0%{?rhel} >= 8 || 0%{?epel})
BuildRequires: %{_py}-mock
%endif
BuildRequires: %{_py}-pyudev
Requires: %{_py}-pyudev
Requires: %{_py}-linux-procfs
Requires: %{_py}-inotify
%if %{without python3}
Requires: %{_py}-schedutils
%endif
# requires for packages with inconsistent python2/3 names
%if %{with python3}
# BuildRequires for 'make test'
BuildRequires: python3-dbus
BuildRequires: python3-gobject-base
Requires: python3-dbus
Requires: python3-gobject-base
%else
# BuildRequires for 'make test'
BuildRequires: dbus-python
BuildRequires: pygobject3-base
Requires: dbus-python
Requires: pygobject3-base
%endif
Requires: virt-what
Requires: ethtool
Requires: gawk
Requires: util-linux
Requires: dbus
Requires: polkit
%if 0%{?fedora} > 22 || 0%{?rhel} > 7
Recommends: dmidecode
# https://src.fedoraproject.org/rpms/tuned/pull-request/8
Recommends: %{_py}-perf
# i686 excluded
Recommends: kernel-tools
Requires: hdparm
Requires: kmod
Requires: iproute
%else
Requires: %{_py}-perf
%endif
# syspurpose
%if 0%{?rhel} > 8
# not on CentOS
%if 0%{!?centos:1}
Recommends: subscription-manager
%endif
%else
%if 0%{?rhel} > 7
Requires: python3-syspurpose
%endif
%endif

%description
The tuned package contains a daemon that tunes system settings dynamically.
It does so by monitoring the usage of several system components periodically.
Based on that information components will then be put into lower or higher
power saving modes to adapt to the current usage. Currently only ethernet
network and ATA harddisk devices are implemented.

%if 0%{?rhel} <= 7 && 0%{!?fedora:1}
# RHEL <= 7
%global docdir %{_docdir}/%{name}-%{version}
%else
# RHEL > 7 || fedora
%global docdir %{_docdir}/%{name}
%endif

%package gtk
Summary: GTK GUI for tuned
Requires: %{name} = %{version}-%{release}
Requires: powertop, polkit
# requires for packages with inconsistent python2/3 names
%if %{with python3}
Requires: python3-gobject-base
%else
Requires: pygobject3-base
%endif

%description gtk
GTK GUI that can control tuned and provides simple profile editor.

%package utils
Requires: %{name} = %{version}-%{release}
Requires: powertop
Summary: Various tuned utilities

%description utils
This package contains utilities that can help you to fine tune and
debug your system and manage tuned profiles.

%package utils-systemtap
Summary: Disk and net statistic monitoring systemtap scripts
Requires: %{name} = %{version}-%{release}
Requires: systemtap

%description utils-systemtap
This package contains several systemtap scripts to allow detailed
manual monitoring of the system. Instead of the typical IO/sec it collects
minimal, maximal and average time between operations to be able to
identify applications that behave power inefficient (many small operations
instead of fewer large ones).

%package profiles-sap
Summary: Additional tuned profile(s) targeted to SAP NetWeaver loads
Requires: %{name} = %{version}

%description profiles-sap
Additional tuned profile(s) targeted to SAP NetWeaver loads.

%package profiles-mssql
Summary: Additional tuned profile(s) for MS SQL Server
Requires: %{name} = %{version}

%description profiles-mssql
Additional tuned profile(s) for MS SQL Server.

%package profiles-oracle
Summary: Additional tuned profile(s) targeted to Oracle loads
Requires: %{name} = %{version}

%description profiles-oracle
Additional tuned profile(s) targeted to Oracle loads.

%package profiles-sap-hana
Summary: Additional tuned profile(s) targeted to SAP HANA loads
Requires: %{name} = %{version}

%description profiles-sap-hana
Additional tuned profile(s) targeted to SAP HANA loads.

%package profiles-atomic
Summary: Additional tuned profile(s) targeted to Atomic
Requires: %{name} = %{version}

%description profiles-atomic
Additional tuned profile(s) targeted to Atomic host and guest.

%package profiles-realtime
Summary: Additional tuned profile(s) targeted to realtime
Requires: %{name} = %{version}

%description profiles-realtime
Additional tuned profile(s) targeted to realtime.

%package profiles-nfv-guest
Summary: Additional tuned profile(s) targeted to Network Function Virtualization (NFV) guest
Requires: %{name} = %{version}
Requires: %{name}-profiles-realtime = %{version}

%description profiles-nfv-guest
Additional tuned profile(s) targeted to Network Function Virtualization (NFV) guest.

%package profiles-nfv-host
Summary: Additional tuned profile(s) targeted to Network Function Virtualization (NFV) host
Requires: %{name} = %{version}
Requires: %{name}-profiles-realtime = %{version}

%description profiles-nfv-host
Additional tuned profile(s) targeted to Network Function Virtualization (NFV) host.

# this is kept for backward compatibility, it should be dropped for RHEL-8
%package profiles-nfv
Summary: Additional tuned profile(s) targeted to Network Function Virtualization (NFV)
Requires: %{name} = %{version}
Requires: %{name}-profiles-nfv-guest = %{version}
Requires: %{name}-profiles-nfv-host = %{version}

%description profiles-nfv
Additional tuned profile(s) targeted to Network Function Virtualization (NFV).

%package profiles-cpu-partitioning
Summary: Additional tuned profile(s) optimized for CPU partitioning
Requires: %{name} = %{version}

%description profiles-cpu-partitioning
Additional tuned profile(s) optimized for CPU partitioning.

%package profiles-spectrumscale
Summary: Additional tuned profile(s) optimized for IBM Spectrum Scale
Requires: %{name} = %{version}

%description profiles-spectrumscale
Additional tuned profile(s) optimized for IBM Spectrum Scale.

%package profiles-compat
Summary: Additional tuned profiles mainly for backward compatibility with tuned 1.0
Requires: %{name} = %{version}

%description profiles-compat
Additional tuned profiles mainly for backward compatibility with tuned 1.0.
It can be also used to fine tune your system for specific scenarios.

%package profiles-postgresql
Summary: Additional tuned profile(s) targeted to PostgreSQL server loads
Requires: %{name} = %{version}

%description profiles-postgresql
Additional tuned profile(s) targeted to PostgreSQL server loads.

%package profiles-openshift
Summary: Additional TuneD profile(s) optimized for OpenShift
Requires: %{name} = %{version}

%description profiles-openshift
Additional TuneD profile(s) optimized for OpenShift.

%package ppd
Summary: PPD compatibility daemon
Requires: %{name} = %{version}
%if 0%{?fedora} >= 41 || 0%{?rhel} >= 10
Obsoletes: power-profiles-daemon < 0.23-2
%endif
# The compatibility daemon is swappable for power-profiles-daemon
Provides: ppd-service
Conflicts: ppd-service

%description ppd
An API translation daemon that allows applications to easily transition
to TuneD from power-profiles-daemon (PPD).

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n %{archive_topdir}

%build
make html %{make_python_arg}

%install
make install DESTDIR="%{buildroot}" BINDIR="%{_bindir}" SBINDIR="%{_sbindir}" \
  DOCDIR="%{docdir}" %{make_python_arg} \
  TUNED_USER_PROFILES_DIR="%{user_profiles_dir}" \
  TUNED_SYSTEM_PROFILES_DIR="%{system_profiles_dir}"
make install-ppd DESTDIR="%{buildroot}" BINDIR="%{_bindir}" \
  SBINDIR="%{_sbindir}" DOCDIR="%{docdir}" %{make_python_arg}

# manual
make install-html DESTDIR=%{buildroot} DOCDIR=%{docdir} %{make_python_arg}

# conditional support for grub2, grub2 is not available on all architectures
# and tuned is noarch package, thus the following hack is needed
mkdir -p %{buildroot}%{_datadir}/tuned/grub2
mv %{buildroot}%{_sysconfdir}/grub.d/00_tuned %{buildroot}%{_datadir}/tuned/grub2/00_tuned
rmdir %{buildroot}%{_sysconfdir}/grub.d

# ghost for persistent storage
mkdir -p %{buildroot}%{_var}/lib/tuned

# ghost for NFV
mkdir -p %{buildroot}%{_sysconfdir}/modprobe.d
touch %{buildroot}%{_sysconfdir}/modprobe.d/kvm.rt.tuned.conf

# validate desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/tuned-gui.desktop

# On RHEL-7 EPEL is needed, because there is no python-mock package and
# python-2.7 doesn't have mock built-in
%if 0%{?rhel} >= 8 || 0%{?epel} || ! 0%{?rhel}
%check
make test %{make_python_arg}
%endif

%post
%systemd_post tuned.service

# convert active_profile from full path to name (if needed)
sed -i 's|.*/\([^/]\+\)/[^\.]\+\.conf|\1|' /etc/tuned/active_profile

# convert GRUB_CMDLINE_LINUX to GRUB_CMDLINE_LINUX_DEFAULT
if [ -r "%{_sysconfdir}/default/grub" ]; then
  sed -i 's/GRUB_CMDLINE_LINUX="$GRUB_CMDLINE_LINUX \\$tuned_params"/GRUB_CMDLINE_LINUX_DEFAULT="$GRUB_CMDLINE_LINUX_DEFAULT \\$tuned_params"/' \
    %{_sysconfdir}/default/grub
fi

%if 0%{?fedora} || 0%{?rhel} >= 10
# migrate all user-defined profiles from /etc/tuned/ to /etc/tuned/profiles/
for f in %{_sysconfdir}/tuned/*; do
  if [ -e "$f/tuned.conf" ]; then
    mv -n "$f" %{_sysconfdir}/tuned/profiles/
  fi
done
%endif


%post ppd
%systemd_post tuned-ppd.service


%preun
%systemd_preun tuned.service
if [ "$1" == 0 ]; then
# clear persistent storage
  rm -f %{_var}/lib/tuned/*
# clear temporal storage
  rm -f /run/tuned/*
fi


%preun ppd
%systemd_preun tuned-ppd.service


%postun
%systemd_postun_with_restart tuned.service

# conditional support for grub2, grub2 is not available on all architectures
# and tuned is noarch package, thus the following hack is needed
if [ "$1" == 0 ]; then
  rm -f %{_sysconfdir}/grub.d/00_tuned || :
# unpatch /etc/default/grub
  if [ -r "%{_sysconfdir}/default/grub" ]; then
    sed -i '/GRUB_CMDLINE_LINUX_DEFAULT="${GRUB_CMDLINE_LINUX_DEFAULT:+$GRUB_CMDLINE_LINUX_DEFAULT }\\$tuned_params"/d' %{_sysconfdir}/default/grub
  fi

# cleanup for Boot loader specification (BLS)

# clear grubenv variables
  grub2-editenv - unset tuned_params tuned_initrd &>/dev/null || :
# unpatch BLS entries
  MACHINE_ID=`cat /etc/machine-id 2>/dev/null`
  if [ "$MACHINE_ID" ]
  then
    for f in /boot/loader/entries/$MACHINE_ID-*.conf
    do
      # Skip non-files and rescue entries
      if [ ! -f "$f" -o "${f: -12}" == "-rescue.conf" ]
      then
        continue
      fi
      # Skip boom managed entries
      if [[ "$f" =~ \w*-[0-9a-f]{7,}-.*-.*.conf ]]
      then
        continue
      fi
      sed -i '/^\s*options\s\+.*\$tuned_params/ s/\s\+\$tuned_params\b//g' "$f" &>/dev/null || :
      sed -i '/^\s*initrd\s\+.*\$tuned_initrd/ s/\s\+\$tuned_initrd\b//g' "$f" &>/dev/null || :
    done
  fi
fi


%postun ppd
%systemd_postun_with_restart tuned-ppd.service


%triggerun -- tuned < 2.0-0
# remove ktune from old tuned, now part of tuned
/usr/sbin/service ktune stop &>/dev/null || :
/usr/sbin/chkconfig --del ktune &>/dev/null || :


%triggerun ppd -- power-profiles-daemon
# if swapping power-profiles-daemon for tuned-ppd, check whether it is active
if systemctl is-active --quiet power-profiles-daemon; then
  mkdir -p %{_localstatedir}/lib/rpm-state/tuned
  touch %{_localstatedir}/lib/rpm-state/tuned/ppd-active
fi


%posttrans
# conditional support for grub2, grub2 is not available on all architectures
# and tuned is noarch package, thus the following hack is needed
if [ -d %{_sysconfdir}/grub.d ]; then
  cp -a %{_datadir}/tuned/grub2/00_tuned %{_sysconfdir}/grub.d/00_tuned
  selinuxenabled &>/dev/null && \
    restorecon %{_sysconfdir}/grub.d/00_tuned &>/dev/null || :
fi


%posttrans ppd
# if power-profiles-daemon was active before installing tuned-ppd,
# start tuned-ppd right away
if [ -f %{_localstatedir}/lib/rpm-state/tuned/ppd-active ]; then
  systemctl start tuned-ppd
  rm -rf %{_localstatedir}/lib/rpm-state/tuned
fi


%files
%exclude %{docdir}/README.utils
%exclude %{docdir}/README.scomes
%exclude %{docdir}/README.NFV
%doc %{docdir}
%{_datadir}/bash-completion/completions/tuned-adm
%if %{with python3}
%exclude %{python3_sitelib}/tuned/gtk
%{python3_sitelib}/tuned
%else
%exclude %{python2_sitelib}/tuned/gtk
%{python2_sitelib}/tuned
%endif
%{_sbindir}/tuned
%{_sbindir}/tuned-adm
%exclude %{_sysconfdir}/tuned/realtime-variables.conf
%exclude %{_sysconfdir}/tuned/realtime-virtual-guest-variables.conf
%exclude %{_sysconfdir}/tuned/realtime-virtual-host-variables.conf
%exclude %{_sysconfdir}/tuned/cpu-partitioning-variables.conf
%exclude %{_sysconfdir}/tuned/cpu-partitioning-powersave-variables.conf
%exclude %{system_profiles_dir}/default
%exclude %{system_profiles_dir}/desktop-powersave
%exclude %{system_profiles_dir}/laptop-ac-powersave
%exclude %{system_profiles_dir}/server-powersave
%exclude %{system_profiles_dir}/laptop-battery-powersave
%exclude %{system_profiles_dir}/enterprise-storage
%exclude %{system_profiles_dir}/spindown-disk
%exclude %{system_profiles_dir}/sap-netweaver
%exclude %{system_profiles_dir}/sap-hana
%exclude %{system_profiles_dir}/sap-hana-kvm-guest
%exclude %{system_profiles_dir}/mssql
%exclude %{system_profiles_dir}/oracle
%exclude %{system_profiles_dir}/atomic-host
%exclude %{system_profiles_dir}/atomic-guest
%exclude %{system_profiles_dir}/realtime
%exclude %{system_profiles_dir}/realtime-virtual-guest
%exclude %{system_profiles_dir}/realtime-virtual-host
%exclude %{system_profiles_dir}/cpu-partitioning
%exclude %{system_profiles_dir}/cpu-partitioning-powersave
%exclude %{system_profiles_dir}/spectrumscale-ece
%exclude %{system_profiles_dir}/postgresql
%exclude %{system_profiles_dir}/openshift
%exclude %{system_profiles_dir}/openshift-control-plane
%exclude %{system_profiles_dir}/openshift-node
%{_prefix}/lib/tuned
%dir %{_sysconfdir}/tuned
%dir %{_sysconfdir}/tuned/recommend.d

%if "%{user_profiles_dir}" != "%{_sysconfdir}/tuned"
%dir %{user_profiles_dir}
%endif

%dir %{_libexecdir}/tuned
%{_libexecdir}/tuned/defirqaffinity*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/tuned/active_profile
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/tuned/profile_mode
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/tuned/post_loaded_profile
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/tuned/ppd_base_profile
%config(noreplace) %{_sysconfdir}/tuned/tuned-main.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/tuned/bootcmdline
%verify(not size mtime md5) %{_sysconfdir}/modprobe.d/tuned.conf
%{_tmpfilesdir}/tuned.conf
%{_unitdir}/tuned.service
%dir %{_localstatedir}/log/tuned
%dir /run/tuned
%dir %{_var}/lib/tuned
%{_mandir}/man5/tuned*
%{_mandir}/man7/tuned-profiles.7*
%{_mandir}/man8/tuned*
%dir %{_datadir}/tuned
%{_datadir}/tuned/grub2
%{_datadir}/dbus-1/system.d/com.redhat.tuned.conf
%{_datadir}/polkit-1/actions/com.redhat.tuned.policy
%ghost %{_sysconfdir}/modprobe.d/kvm.rt.tuned.conf
%{_prefix}/lib/kernel/install.d/92-tuned.install

%files gtk
%{_sbindir}/tuned-gui
%if %{with python3}
%{python3_sitelib}/tuned/gtk
%else
%{python2_sitelib}/tuned/gtk
%endif
%{_datadir}/tuned/ui
%{_datadir}/icons/hicolor/scalable/apps/tuned.svg
%{_datadir}/applications/tuned-gui.desktop

%files utils
%doc COPYING
%{_bindir}/powertop2tuned
%{_libexecdir}/tuned/pmqos-static*

%files utils-systemtap
%doc doc/README.utils
%doc doc/README.scomes
%doc COPYING
%{_sbindir}/varnetload
%{_sbindir}/netdevstat
%{_sbindir}/diskdevstat
%{_sbindir}/scomes
%{_mandir}/man8/varnetload.*
%{_mandir}/man8/netdevstat.*
%{_mandir}/man8/diskdevstat.*
%{_mandir}/man8/scomes.*

%files profiles-sap
%{system_profiles_dir}/sap-netweaver
%{_mandir}/man7/tuned-profiles-sap.7*

%files profiles-sap-hana
%{system_profiles_dir}/sap-hana
%{system_profiles_dir}/sap-hana-kvm-guest
%{_mandir}/man7/tuned-profiles-sap-hana.7*

%files profiles-mssql
%{system_profiles_dir}/mssql
%{_mandir}/man7/tuned-profiles-mssql.7*

%files profiles-oracle
%{system_profiles_dir}/oracle
%{_mandir}/man7/tuned-profiles-oracle.7*

%files profiles-atomic
%{system_profiles_dir}/atomic-host
%{system_profiles_dir}/atomic-guest
%{_mandir}/man7/tuned-profiles-atomic.7*

%files profiles-realtime
%config(noreplace) %{_sysconfdir}/tuned/realtime-variables.conf
%{system_profiles_dir}/realtime
%{_mandir}/man7/tuned-profiles-realtime.7*

%files profiles-nfv-guest
%config(noreplace) %{_sysconfdir}/tuned/realtime-virtual-guest-variables.conf
%{system_profiles_dir}/realtime-virtual-guest
%{_mandir}/man7/tuned-profiles-nfv-guest.7*

%files profiles-nfv-host
%config(noreplace) %{_sysconfdir}/tuned/realtime-virtual-host-variables.conf
%{system_profiles_dir}/realtime-virtual-host
%{_mandir}/man7/tuned-profiles-nfv-host.7*

%files profiles-nfv
%doc %{docdir}/README.NFV

%files profiles-cpu-partitioning
%config(noreplace) %{_sysconfdir}/tuned/cpu-partitioning-variables.conf
%config(noreplace) %{_sysconfdir}/tuned/cpu-partitioning-powersave-variables.conf
%{system_profiles_dir}/cpu-partitioning
%{system_profiles_dir}/cpu-partitioning-powersave
%{_mandir}/man7/tuned-profiles-cpu-partitioning.7*

%files profiles-spectrumscale
%{system_profiles_dir}/spectrumscale-ece
%{_mandir}/man7/tuned-profiles-spectrumscale-ece.7*

%files profiles-compat
%{system_profiles_dir}/default
%{system_profiles_dir}/desktop-powersave
%{system_profiles_dir}/laptop-ac-powersave
%{system_profiles_dir}/server-powersave
%{system_profiles_dir}/laptop-battery-powersave
%{system_profiles_dir}/enterprise-storage
%{system_profiles_dir}/spindown-disk
%{_mandir}/man7/tuned-profiles-compat.7*

%files profiles-postgresql
%{system_profiles_dir}/postgresql
%{_mandir}/man7/tuned-profiles-postgresql.7*

%files profiles-openshift
%{system_profiles_dir}/openshift
%{system_profiles_dir}/openshift-control-plane
%{system_profiles_dir}/openshift-node
%{_mandir}/man7/tuned-profiles-openshift.7*

%files ppd
%{_sbindir}/tuned-ppd
%{_unitdir}/tuned-ppd.service
%{_datadir}/dbus-1/system-services/net.hadess.PowerProfiles.service
%{_datadir}/dbus-1/system.d/net.hadess.PowerProfiles.conf
%{_datadir}/polkit-1/actions/net.hadess.PowerProfiles.policy
%{_datadir}/dbus-1/system-services/org.freedesktop.UPower.PowerProfiles.service
%{_datadir}/dbus-1/system.d/org.freedesktop.UPower.PowerProfiles.conf
%{_datadir}/polkit-1/actions/org.freedesktop.UPower.PowerProfiles.policy
%config(noreplace) %{_sysconfdir}/tuned/ppd.conf

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.27.0-1
- Prepare for Oreon 11 (RP1)
