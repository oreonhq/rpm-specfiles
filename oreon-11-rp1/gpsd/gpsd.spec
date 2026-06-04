%global source0_hash 409873f5048462ef1ac413a51ab35caa8b50b31be62b3347bee1cc2994e7c649
%global source1_hash 810c3f82c23758f8eaa23f7263363e1ac1822253dc8719ffa897ee77604bbe02

%global pkgname gpsd

# RHEL builds the core, EPEL builds the libs
%global with_core %{undefined epel}
# libgps ABI changes too frequently to be provided in RHEL
%global with_libs %[%{defined fedora} || %{defined epel} || %{defined eln}]
# requires qt-4.x
%global with_qt %{defined fedora}
# scons is not available in RHEL
%global with_bundled_scons %{defined rhel}

%if 0%{?epel}
Name:           gpsd-epel
%else
Name:           gpsd
%endif
Version:        3.27.5
Release:        3%{?dist}
Epoch:          1
Summary:        Service daemon for mediating access to a GPS

License:        BSD-2-Clause
URL:            https://gpsd.gitlab.io/gpsd/index.html
Source0:        https://download-mirror.savannah.gnu.org/releases/gpsd/%{pkgname}-%{version}.tar.gz
# used only for building
%global scons_ver 4.9.1
Source1:        https://github.com/SCons/scons/archive/refs/tags/4.9.1/scons-4.9.1.tar.gz
%if %{with_bundled_scons}
%global scons %{python3} scons-%{scons_ver}/scripts/scons.py
%else
%global scons scons
%endif
Source11:       gpsd.sysconfig

# Add old status names to gps.h for compatibility
Patch1:         gpsd-apistatus.patch

BuildRequires:  gcc
BuildRequires:  dbus-devel
BuildRequires:  ncurses-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  gtk3-devel
%if !%{with_bundled_scons}
BuildRequires:  python3-scons
%endif
BuildRequires:  python3-gobject
BuildRequires:  python3-cairo
BuildRequires:  python3-pyserial
BuildRequires:  desktop-file-utils
BuildRequires:  bluez-libs-devel
BuildRequires:  pps-tools-devel
BuildRequires:  systemd-rpm-macros
%if %{with_qt}
BuildRequires:  gcc-c++
BuildRequires:  qt-devel
%endif
BuildRequires:  libusb1-devel
BuildRequires:  gobject-introspection

Requires:       udev
%{?systemd_requires}

%if !%{with_libs}
Obsoletes:      gpsd-libs < %{epoch}:%{version}-%{release}
Obsoletes:      gpsd-devel < %{epoch}:%{version}-%{release}
%endif

%description
gpsd is a service daemon that mediates access to a GPS sensor
connected to the host computer by serial or USB interface, making its
data on the location/course/velocity of the sensor available to be
queried on TCP port 2947 of the host computer.  With gpsd, multiple
GPS client applications (such as navigational and war-driving software)
can share access to a GPS without contention or loss of data.  Also,
gpsd responds to queries with a format that is substantially easier to
parse than NMEA 0183.

%if %{with_libs}
%package -n %{pkgname}-libs
Summary:        Client libraries in C for talking to a running gpsd or GPS

%description -n %{pkgname}-libs
This package contains the gpsd libraries that manage access
to a GPS for applications.

%package -n %{pkgname}-devel
Summary:        Development files for the gpsd library
Requires:       %{pkgname}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description -n %{pkgname}-devel
This package provides C header files for the gpsd shared libraries that
manage access to a GPS for applications
%endif

%if %{with_qt}
%package -n %{pkgname}-qt
Summary:        C++/Qt5 bindings for the gpsd library
%if %{with_libs}
Requires:       %{pkgname}-libs%{?_isa} = %{epoch}:%{version}-%{release}
%endif

%description -n %{pkgname}-qt
This package provide C++ and Qt bindings for use with the libgps library from
gpsd.

%package -n %{pkgname}-qt-devel
Summary:        Development files for the C++/Qt5 bindings for the gpsd library
Requires:       %{pkgname}-qt%{?_isa} = %{epoch}:%{version}-%{release}

%description -n %{pkgname}-qt-devel
This package provides the development files for the C++ and Qt bindings for use
with the libgps library from gpsd.
%endif

%if %{with_core}
%package -n python3-%{name}
Summary:        Python libraries and modules for use with gpsd
Requires:       python3-pyserial
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
This package contains the python3 modules that manage access to a GPS for
applications.

%package clients
Summary:        Clients for gpsd
Requires:       python3-%{name} = %{epoch}:%{version}-%{release}
%if %{with_libs}
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
%endif

%description clients
This package contains various clients using gpsd.

%package xclients
Summary:        Graphical clients for gpsd
Requires:       python3-%{name} = %{epoch}:%{version}-%{release}
Requires:       python3-cairo
Requires:       python3-gobject
Requires:       gtk3

%description xclients
This package contains X clients using gpsd.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{pkgname}-%{version}
%autopatch -p1

%if %{with_bundled_scons}
%setup -q -T -D -a 1
%endif

# don't try reloading systemd when installing in the build root
sed -i 's|systemctl daemon-reload|true|' SConscript

iconv -f iso8859-1 -t utf8 NEWS > NEWS_ && mv NEWS_ NEWS

%build
export CCFLAGS="%{optflags}"
# scons ignores LDFLAGS. LINKFLAGS partially work (some flags like
# -spec=... are filtered)
export LINKFLAGS="%{__global_ldflags}"

# breaks with %%{_smp_mflags}
%{scons} \
    dbus_export=yes \
    systemd=yes \
%if %{with_qt}
    qt=yes \
%else
    qt=no \
%endif
    debug=yes \
    leapfetch=no \
    manbuild=no \
    prefix="" \
    sysconfdif=%{_sysconfdir} \
    bindir=%{_bindir} \
    includedir=%{_includedir} \
    libdir=%{_libdir} \
    sbindir=%{_sbindir} \
    mandir=%{_mandir} \
    mibdir=%{_docdir}/gpsd \
    docdir=%{_docdir}/gpsd \
    pkgconfigdir=%{_libdir}/pkgconfig \
    icondir=%{_datadir}/gpsd \
    udevdir=$(dirname %{_udevrulesdir}) \
    unitdir=%{_unitdir} \
    target_python=python3 \
    python_shebang=%{python3} \
    python_libdir=%{python3_sitearch} \
    build

%install
# avoid rebuilding
export CCFLAGS="%{optflags}"
export LINKFLAGS="%{__global_ldflags}"

DESTDIR=%{buildroot} %{scons} install systemd_install udev-install

%if %{with_core}
# use the old name for udev rules
mv %{buildroot}%{_udevrulesdir}/{25,99}-gpsd.rules

install -d -m 0755 %{buildroot}%{_sysconfdir}/sysconfig
install -p -m 0644 %{SOURCE11} \
    %{buildroot}%{_sysconfdir}/sysconfig/gpsd

# Install the .desktop files
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    gpsd-%{version}/packaging/X11/xgps.desktop
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    gpsd-%{version}/packaging/X11/xgpsspeed.desktop

# Missed in scons install
install -p -m 0755 gpsinit %{buildroot}%{_sbindir}
%endif

# Remove shebang and fix permissions
sed -i '/^#!.*python/d' %{buildroot}%{python3_sitearch}/gps/{aio,}gps.py
chmod 644 %{buildroot}%{python3_sitearch}/gps/gps.py

rm -f %{buildroot}%{_libdir}/libgpsdpacket.so

# Remove unpackaged files
%if !%{with_core}
rm -rf %{buildroot}%{_sbindir}
rm -rf %{buildroot}%{_bindir}
rm -rf %{buildroot}%{_sysconfdir}
rm -f %{buildroot}%{_libdir}/libgpsdpacket.so*
rm -rf %{buildroot}%{python3_sitearch}
rm -rf %{buildroot}%{_unitdir}
rm -rf %{buildroot}%{_udevrulesdir}
rm -rf %{buildroot}%{_datadir}/gpsd
rm -rf %{buildroot}%{_mandir}/man[18]
%endif
%if !%{with_libs}
rm -f %{buildroot}%{_libdir}/lib{gps*.so,gps.so.*}
rm -rf %{buildroot}%{_libdir}/pkgconfig
rm -rf %{buildroot}%{_includedir}
rm -rf %{buildroot}%{_mandir}/man{3,5}
%endif
%if !%{with_qt}
rm -f %{buildroot}%{_libdir}/libQgpsmm* \
    %{buildroot}%{_libdir}/pkgconfig/Qgpsmm* \
    %{buildroot}%{_mandir}/man3/libQgpsmm.3*
%endif
rm -rf %{buildroot}%{_docdir}/gpsd

%check
%{scons} check

%if %{with_core}
%post
%systemd_post gpsd.service gpsd.socket

%preun
%systemd_preun gpsd.service gpsd.socket

%postun
# Don't restart the service
%systemd_postun gpsd.service gpsd.socket
%endif

%if %{with_libs}
%ldconfig_scriptlets libs
%endif

%if %{with_qt}
%ldconfig_scriptlets qt
%endif

%if %{with_core}
%files
%doc README.adoc NEWS
%license COPYING
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_sbindir}/gpsd
%{_sbindir}/gpsdctl
%{_sbindir}/gpsinit
%{_bindir}/gpsmon
%{_bindir}/gpsctl
%{_bindir}/ntpshmmon
%{_bindir}/ppscheck
%{_unitdir}/gpsd.service
%{_unitdir}/gpsd.socket
%{_unitdir}/gpsdctl@.service
%{_udevrulesdir}/*.rules
%{_mandir}/man8/gpsd.8*
%{_mandir}/man8/gpsdctl.8*
%{_mandir}/man8/gpsinit.8*
%{_mandir}/man8/ppscheck.8*
%{_mandir}/man1/gpsmon.1*
%{_mandir}/man1/gpsctl.1*
%{_mandir}/man1/ntpshmmon.1*
%endif

%if %{with_libs}
%files -n %{pkgname}-libs
%{_libdir}/libgps.so.32*

%files -n %{pkgname}-devel
%doc TODO HACKING
%{_libdir}/libgps.so
%{_libdir}/pkgconfig/libgps.pc
%{_includedir}/gps.h
%{_includedir}/libgpsmm.h
%{_mandir}/man3/libgps.3*
%{_mandir}/man3/libgpsmm.3*
%{_mandir}/man5/gpsd_json.5*
%endif

%if %{with_qt}
%files -n %{pkgname}-qt
%{_libdir}/libQgpsmm.so.32*

%files -n %{pkgname}-qt-devel
%{_libdir}/libQgpsmm.so
%{_libdir}/libQgpsmm.prl
%{_libdir}/pkgconfig/Qgpsmm.pc
%{_mandir}/man3/libQgpsmm.3*
%endif

%if %{with_core}
%files -n python3-%{name}
%license COPYING
%{_libdir}/libgpsdpacket.so*
%{python3_sitearch}/gps*

%files clients
%{_bindir}/cgps
%{_bindir}/gegps
%{_bindir}/gps2udp
%{_bindir}/gpscat
%{_bindir}/gpscsv
%{_bindir}/gpsdebuginfo
%{_bindir}/gpsdecode
%{_bindir}/gpslogntp
%{_bindir}/gpspipe
%{_bindir}/gpsplot
%{_bindir}/gpsprof
%{_bindir}/gpsrinex
%{_bindir}/gpssnmp
%{_bindir}/gpssubframe
%{_bindir}/gpxlogger
%{_bindir}/lcdgps
%{_bindir}/gpsfake
%{_bindir}/ubxtool
%{_bindir}/zerk
%{_mandir}/man1/gegps.1*
%{_mandir}/man1/gps.1*
%{_mandir}/man1/gps2udp.1*
%{_mandir}/man1/gpscsv.1*
%{_mandir}/man1/gpsdebuginfo.1*
%{_mandir}/man1/gpsdecode.1*
%{_mandir}/man1/gpslogntp.1*
%{_mandir}/man1/gpspipe.1*
%{_mandir}/man1/gpsplot.1*
%{_mandir}/man1/gpsprof.1*
%{_mandir}/man1/gpsrinex.1*
%{_mandir}/man1/gpssnmp.1*
%{_mandir}/man1/gpssubframe.1*
%{_mandir}/man1/gpxlogger.1*
%{_mandir}/man1/lcdgps.1*
%{_mandir}/man1/cgps.1*
%{_mandir}/man1/gpscat.1*
%{_mandir}/man1/gpsfake.1*
%{_mandir}/man1/ubxtool.1*
%{_mandir}/man1/zerk.1*

%files xclients
%{_bindir}/xgps
%{_bindir}/xgpsspeed
%{_datadir}/applications/*.desktop
%dir %{_datadir}/gpsd
%{_datadir}/gpsd/gpsd-logo.png
%{_mandir}/man1/xgps.1*
%{_mandir}/man1/xgpsspeed.1*
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.27.5-3
- Prepare for Oreon 11 (RP1)
