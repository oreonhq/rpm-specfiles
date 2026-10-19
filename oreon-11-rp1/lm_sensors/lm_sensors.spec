%global source0_hash c6a0587e565778a40d88891928bf8943f27d353f382d5b745a997d635978a8f0
Name: lm_sensors
Version: 3.6.2
Release:        1%{?dist}
Summary:        Hardware monitoring tools
%define upstream_version %(echo %{version} | sed -e 's/\\./-/g')
License: GPL-2.0-or-later AND Linux-man-pages-copyleft-var AND Linux-man-pages-copyleft AND MIT
URL: http://github.com/lm-sensors/lm-sensors/
Source0:        https://github.com/lm-sensors/lm-sensors/archive/V3-6-2/lm-sensors-3-6-2.tar.gz
Source1: lm_sensors.sysconfig
Source2: sensord.sysconfig
Source3: lm_sensors-modprobe-wrapper
Source4: lm_sensors-modprobe-r-wrapper
Source5: sensord.service
Source6: sensord-service-wrapper
Source7: lm_sensors.service
Source8: lm_sensors-wrapper
Patch0: 0001-Revert-unnecessary-soname-bump.patch
Patch3: lm_sensors-3.6.0-sensors-detect-Add-support-for-AMD-CPU-Family-19h.patch
Requires: /usr/sbin/modprobe
%ifarch %{ix86} x86_64
Requires: /usr/sbin/dmidecode
%endif
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires(post): systemd-units
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  kernel-headers
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  rrdtool-devel
# /oreon:deps
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
License: LGPL-2.1-or-later AND Linux-man-pages-copyleft
%description devel
The lm_sensors-devel package includes a header files and libraries for use
when building applications that make use of sensor data.

%package sensord
Summary: Daemon that periodically logs sensor readings
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
License: GPL-2.0-or-later AND Linux-man-pages-copyleft AND MIT
%description sensord
Daemon that periodically logs sensor readings to syslog or a round-robin
database, and warns of sensor alarms.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n lm-sensors-%{upstream_version}
%patch -P0 -p1
%patch -P3 -p1

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
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -pm 644 prog/init/fancontrol.service $RPM_BUILD_ROOT%{_unitdir}
install -pm 644 lm_sensors.service           $RPM_BUILD_ROOT%{_unitdir}
install -pm 644 sensord.service              $RPM_BUILD_ROOT%{_unitdir}
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/%{name}
install -pm 755 %{SOURCE3} $RPM_BUILD_ROOT%{_libexecdir}/%{name}/lm_sensors-modprobe-wrapper
install -pm 755 %{SOURCE4} $RPM_BUILD_ROOT%{_libexecdir}/%{name}/lm_sensors-modprobe-r-wrapper
install -pm 755 %{SOURCE8} $RPM_BUILD_ROOT%{_libexecdir}/%{name}/lm_sensors-wrapper
install -pm 755 %{SOURCE6} $RPM_BUILD_ROOT%{_libexecdir}/%{name}/sensord-service-wrapper
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%triggerun -- lm_sensors < 3.3.0-2

if [ -L /etc/rc3.d/S26lm_sensors ]; then
    /bin/systemctl enable lm_sensors.service >/dev/null 2>&1 || :
fi
/sbin/chkconfig --del lm_sensors
%post

%systemd_post lm_sensors.service
%preun

%systemd_preun lm_sensors.service
%postun

%systemd_postun_with_restart lm_sensors.service
%post sensord

%systemd_post sensord.service
%preun sensord

%systemd_preun sensord.service
%postun sensord

%systemd_postun_with_restart sensord.service
%ldconfig_scriptlets libs
%files -f %{oreon_filedir}/main.list
%files -n lm_sensors-libs -f %{oreon_filedir}/lm_sensors-libs.list
%files -n lm_sensors-devel -f %{oreon_filedir}/lm_sensors-devel.list
%files -n lm_sensors-sensord -f %{oreon_filedir}/lm_sensors-sensord.list

%changelog

%autochangelog
