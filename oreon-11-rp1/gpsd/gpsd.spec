%global source0_hash 409873f5048462ef1ac413a51ab35caa8b50b31be62b3347bee1cc2994e7c649
%global source1_hash 810c3f82c23758f8eaa23f7263363e1ac1822253dc8719ffa897ee77604bbe02
%global pkgname gpsd
%global with_core %{undefined epel}
%global with_libs %[%{defined fedora} || %{defined epel} || %{defined eln}]
%global with_qt %{defined fedora}
%global with_bundled_scons %{defined rhel}
%if 0%{?epel}
Name:           gpsd-epel
%else
Name:           gpsd
%endif
Version:        3.27.5
Release:        1%{?dist}
Epoch:          1
Summary:        Service daemon for mediating access to a GPS
License:        BSD-2-Clause
URL:            https://gpsd.gitlab.io/gpsd/index.html
Source0:        https://download-mirror.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz
%global scons_ver 4.9.1
Source1:        https://github.com/SCons/scons/archive/refs/tags/4.9.1.tar.gz#/scons-4.9.1.tar.gz
%if %{with_bundled_scons}
%global scons %{python3} scons-%{scons_ver}/scripts/scons.py
%else
%global scons scons
%endif
Source11:       gpsd.sysconfig
Patch1:         gpsd-apistatus.patch
%if !%{with_bundled_scons}
%endif
%if %{with_qt}
%endif
Requires:       udev
%{?systemd_requires}
%if !%{with_libs}
Obsoletes:      gpsd-libs < %{epoch}:%{version}-%{release}
Obsoletes:      gpsd-devel < %{epoch}:%{version}-%{release}
%endif
# oreon:deps
BuildRequires:  bluez-libs-devel
BuildRequires:  dbus-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gobject-introspection
BuildRequires:  gtk3-devel
BuildRequires:  libusb1-devel
BuildRequires:  ncurses-devel
BuildRequires:  pps-tools-devel
BuildRequires:  python3-cairo
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  python3-pyserial
BuildRequires:  python3-scons
BuildRequires:  python3-setuptools
BuildRequires:  qt-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
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
export LINKFLAGS="%{__global_ldflags}"
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
export CCFLAGS="%{optflags}"
export LINKFLAGS="%{__global_ldflags}"
DESTDIR=%{buildroot} %{scons} install systemd_install udev-install
%if %{with_core}
mv %{buildroot}%{_udevrulesdir}/{25,99}-gpsd.rules
install -d -m 0755 %{buildroot}%{_sysconfdir}/sysconfig
install -p -m 0644 %{SOURCE11} \
    %{buildroot}%{_sysconfdir}/sysconfig/gpsd
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    gpsd-%{version}/packaging/X11/xgps.desktop
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    gpsd-%{version}/packaging/X11/xgpsspeed.desktop
install -p -m 0755 gpsinit %{buildroot}%{_sbindir}
%endif
sed -i '/^#!.*python/d' %{buildroot}%{python3_sitearch}/gps/{aio,}gps.py
chmod 644 %{buildroot}%{python3_sitearch}/gps/gps.py
rm -f %{buildroot}%{_libdir}/libgpsdpacket.so
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{scons} check
%if %{with_core}
%post

%systemd_post gpsd.service gpsd.socket
%preun

%systemd_preun gpsd.service gpsd.socket
%postun

%systemd_postun gpsd.service gpsd.socket
%endif
%if %{with_libs}
%ldconfig_scriptlets libs
%endif
%if %{with_qt}
%ldconfig_scriptlets qt
%endif
%if %{with_core}
%files -f %{oreon_filedir}/main.list
%files -n gpsd-libs -f %{oreon_filedir}/gpsd-libs.list
%files -n gpsd-devel -f %{oreon_filedir}/gpsd-devel.list
%files -n gpsd-qt -f %{oreon_filedir}/gpsd-qt.list
%files -n gpsd-qt-devel -f %{oreon_filedir}/gpsd-qt-devel.list
%files -n python3-gpsd -f %{oreon_filedir}/python3-gpsd.list
%files -n gpsd-clients -f %{oreon_filedir}/gpsd-clients.list
%files -n gpsd-xclients -f %{oreon_filedir}/gpsd-xclients.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.27.5-3
- Prepare for Oreon 11 (RP1)
%endif
