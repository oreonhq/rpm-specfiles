%global source0_hash none

Name: lm_sensors
Version: 3.6.0
Release: 24%{?dist}
Summary: Hardware monitoring tools

%define upstream_version %(echo %{version} | sed -e 's/\\./-/g')

# Some man pages are licensed Linux-man-pages-copyleft-var and Linux-man-pages-copyleft (lib/sensors.conf.5,
# prog/sensors/sensors.1). Files from dist-git are licensed
# MIT (according to the Fedora Project Contributor Agreement
# https://docs.fedoraproject.org/en-US/legal/fedora-linux-license/).
# lib/* are LGPL-2.1-or-later (in subpackage)
# The rest is GPL-2.0-or-later.
License: GPL-2.0-or-later AND Linux-man-pages-copyleft-var AND Linux-man-pages-copyleft AND MIT

URL: http://github.com/lm-sensors/lm-sensors/

Source0: https://github.com/lm-sensors/lm-sensors/archive/V%{upstream_version}/lm-sensors-%{upstream_version}.tar.gz
Source1: lm_sensors.sysconfig
# This one was taken from PLD-linux, Thanks!
Source2: sensord.sysconfig
Source3: lm_sensors-modprobe-wrapper
Source4: lm_sensors-modprobe-r-wrapper
Source5: sensord.service
Source6: sensord-service-wrapper
Source7: lm_sensors.service
Source8: lm_sensors-wrapper

# Downstream-only:
Patch0: 0001-Revert-unnecessary-soname-bump.patch

# Upstream patch:
Patch1: 0001-Change-PIDFile-path-from-var-run-to-run.patch
Patch2: lm_sensors-3.6.0-allow_no_sensors.patch
# Upstream commit 5deee7d0c301df779:
Patch3: lm_sensors-3.6.0-sensors-detect-Add-support-for-AMD-CPU-Family-19h.patch
# rrdtool has constified all argv
Patch4: lm_sensors-3.6.0-rrd-const-argv.patch

Requires: /usr/sbin/modprobe
%ifarch %{ix86} x86_64
Requires: /usr/sbin/dmidecode
%endif
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires(post): systemd-units
BuildRequires: kernel-headers >= 2.2.16, bison, flex, gawk
BuildRequires: perl-generators
BuildRequires: rrdtool-devel
BuildRequires: gcc
BuildRequires: make


%description
The lm_sensors package includes a collection of modules for general SMBus
access and hardware monitoring.


%package libs
Summary: Lm_sensors core libraries
License: LGPL-2.1-or-later

%description libs
Core libraries for lm_sensors applications


%package devel
Summary: Development files for programs which will use lm_sensors
Requires: %{name}-libs = %{version}-%{release}
# One manual page is licensed Linux-man-pages-copyleft (lib/libsensors.3). The rest is LGPLv2+.
License: LGPL-2.1-or-later AND Linux-man-pages-copyleft

%description devel
The lm_sensors-devel package includes a header files and libraries for use
when building applications that make use of sensor data.


%package sensord
Summary: Daemon that periodically logs sensor readings
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
# One man page is licensed Linux-man-pages-copyleft (prog/sensord/sensord.8). Files from
# dist-git are licensed MIT according to the FPCA. The rest is GPLv2+.
License: GPL-2.0-or-later AND Linux-man-pages-copyleft AND MIT

%description sensord
Daemon that periodically logs sensor readings to syslog or a round-robin
database, and warns of sensor alarms.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n lm-sensors-%{upstream_version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10
%patch -P4 -p1
%endif

# Remove currently unused files to make sure we've got the license right
rm -f prog/init/sysconfig-lm_sensors-convert prog/hotplug/unhide_ICH_SMBus

mv prog/init/README prog/init/README.initscripts
chmod -x prog/init/fancontrol.init

# fixing the sensord-service-wrapper path
cp -p %{SOURCE5} sensord.service
cp -p %{SOURCE7} lm_sensors.service
sed -i "s|\@WRAPPER_DIR\@|%{_libexecdir}/%{name}|" sensord.service
sed -i "s|\@WRAPPER_DIR\@|%{_libexecdir}/%{name}|" lm_sensors.service

sed -i 's|SBINDIR := \$(PREFIX)/sbin|SBINDIR := %_sbindir|' Makefile

%build
%set_build_flags
%{make_build} PREFIX=%{_prefix} LIBDIR=%{_libdir} MANDIR=%{_mandir} ETCDIR=%{_sysconfdir} \
  EXLDFLAGS="$LDFLAGS" PROG_EXTRA=sensord BUILD_STATIC_LIB=0 user


%install
make PREFIX=%{_prefix} LIBDIR=%{_libdir} MANDIR=%{_mandir} ETCDIR=%{_sysconfdir} PROG_EXTRA=sensord \
  DESTDIR=$RPM_BUILD_ROOT BUILD_STATIC_LIB=0 user_install

ln -s sensors.conf.5.gz $RPM_BUILD_ROOT%{_mandir}/man5/sensors3.conf.5.gz

mkdir -p $RPM_BUILD_ROOT%{_initrddir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sensors.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
install -pm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/lm_sensors
install -pm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/sensord

# service files
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -pm 644 prog/init/fancontrol.service $RPM_BUILD_ROOT%{_unitdir}
install -pm 644 lm_sensors.service           $RPM_BUILD_ROOT%{_unitdir}
install -pm 644 sensord.service              $RPM_BUILD_ROOT%{_unitdir}

# customized modprobe calls
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/%{name}
install -pm 755 %{SOURCE3} $RPM_BUILD_ROOT%{_libexecdir}/%{name}/lm_sensors-modprobe-wrapper
install -pm 755 %{SOURCE4} $RPM_BUILD_ROOT%{_libexecdir}/%{name}/lm_sensors-modprobe-r-wrapper
install -pm 755 %{SOURCE8} $RPM_BUILD_ROOT%{_libexecdir}/%{name}/lm_sensors-wrapper

# sensord service wrapper
install -pm 755 %{SOURCE6} $RPM_BUILD_ROOT%{_libexecdir}/%{name}/sensord-service-wrapper


# Note non standard systemd scriptlets, since reload / stop makes no sense
# for lm_sensors
%triggerun -- lm_sensors < 3.3.0-2
if [ -L /etc/rc3.d/S26lm_sensors ]; then
    /bin/systemctl enable lm_sensors.service >/dev/null 2>&1 || :
fi
/sbin/chkconfig --del lm_sensors

# ===== main =====

%post
%systemd_post lm_sensors.service

%preun
%systemd_preun lm_sensors.service

%postun
%systemd_postun_with_restart lm_sensors.service

# ==== sensord ===

%post sensord
%systemd_post sensord.service

%preun sensord
%systemd_preun sensord.service

%postun sensord
%systemd_postun_with_restart sensord.service

# ===== libs =====

%ldconfig_scriptlets libs


%files
%license COPYING
%doc CHANGES CONTRIBUTORS doc README*
%doc prog/init/fancontrol.init prog/init/README.initscripts
%config %{_sysconfdir}/sensors3.conf
%config(noreplace) %{_sysconfdir}/sysconfig/lm_sensors
%dir %{_sysconfdir}/sensors.d
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%if "%{_sbindir}" != "%{_bindir}"
%{_sbindir}/*
%endif
%{_unitdir}/lm_sensors.service
%{_unitdir}/fancontrol.service
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/lm_sensors-modprobe*wrapper
%{_libexecdir}/%{name}/lm_sensors-wrapper
%exclude %{_sbindir}/sensord
%exclude %{_mandir}/man8/sensord.8.gz

%files libs
%{_libdir}/*.so.*
%license COPYING.LGPL

%files devel
%{_includedir}/sensors
%{_libdir}/lib*.so
%{_mandir}/man3/*

%files sensord
%doc prog/sensord/README
%{_sbindir}/sensord
%{_mandir}/man8/sensord.8.gz
%config(noreplace) %{_sysconfdir}/sysconfig/sensord
%{_unitdir}/sensord.service
%{_libexecdir}/%{name}/sensord-service-wrapper


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.6.0-24
- Prepare for Oreon 11 (RP1)
